import json
import os
import re
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.error import HTTPError

from jsonschema import Draft7Validator, ValidationError
from rapidfuzz import fuzz, process

from .logger import l
from .process import run


NEXTCLADE_REPO = "nextstrain/nextclade"
SCHEMA_FILENAME = "input-pathogen-json.schema.json"
SCHEMA_PATH = f"packages/nextclade-schemas/{SCHEMA_FILENAME}"
SCHEMA_URL_TEMPLATE = "https://raw.githubusercontent.com/{repo}/refs/heads/{branch}/{path}"
SCHEMA_DOCS_URL = "https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html"

FUZZY_MATCH_THRESHOLD = 80.0


def validate_pathogen_json(
  data: Any,
  filepath: str,
  ctx: "ValidationContext",
  schemas_dir: Path | None = None,
  dataset_path: str | None = None,
) -> None:
  if filepath in ctx.reports:
    return

  schema = fetch_schema(schemas_dir)
  validator = Draft7Validator(schema)
  errors = []
  for error in validator.iter_errors(data):
    path = '.'.join(str(p) for p in error.absolute_path) or '(root)'
    errors.append(f"  {path}: {error.message}")
  if errors:
    raise ValidationError(f"Schema validation failed for '{filepath}':\n" + '\n'.join(errors))

  report = DefectReport(
    filepath=filepath,
    dataset_path=dataset_path or _extract_dataset_path(filepath),
  )
  report.defects = _check_known_defects(data, report.infer_upstream_repo())
  ctx.reports[filepath] = report

  known_defect_paths = {d.json_path for d in report.defects}

  schema_index = _build_schema_index(schema)
  for message, json_path in _find_unknown_properties(data, schema, schema_index):
    if json_path not in known_defect_paths:
      _emit_ci_warning(filepath, message, json_path)

  for defect in report.defects:
    _emit_defect(filepath, defect, defect.json_path)


def fetch_schema(schemas_dir: Path | None = None) -> dict:
  if schemas_dir is not None:
    return _load_local_schema(schemas_dir)
  return _fetch_remote_schema()


def print_defect_summary(ctx: "ValidationContext") -> None:
  reports = [r for r in ctx.reports.values() if r.defects]
  if not reports:
    return

  datasets: dict[str, list[DefectReport]] = {}
  for r in reports:
    datasets.setdefault(r.dataset_path, []).append(r)

  error_count = sum(1 for r in reports if r.has_errors)
  warning_count = sum(1 for r in reports if r.has_warnings)

  print("\n" + "=" * 60)
  print("DATASET DEFECTS SUMMARY")
  print("=" * 60)
  print(f"\n{len(datasets)} dataset(s), {error_count} error(s), {warning_count} warning(s)\n")

  for dataset_path in sorted(datasets.keys()):
    dataset_reports = datasets[dataset_path]
    upstream = dataset_reports[0].infer_upstream_repo()
    upstream_hint = f" [upstream: {upstream}]" if upstream else ""

    has_errors = any(r.has_errors for r in dataset_reports)
    has_warnings = any(r.has_warnings for r in dataset_reports)
    marker = "ERROR" if has_errors else "WARNING" if has_warnings else "INFO"

    print(f"[{marker}] {dataset_path}{upstream_hint}")

    for r in sorted(dataset_reports, key=lambda x: x.filepath):
      filename = Path(r.filepath).name
      print(f"  {filename}:")
      for d in sorted(r.defects, key=lambda x: (x.severity.value, x.json_path)):
        severity_tag = d.severity.name
        print(f"    [{severity_tag}] {d.problem}")

    print()

  print("-" * 60)
  print("Run migration scripts to fix locally.")
  print("Notify upstream maintainers to prevent defect recurrence.")
  print(f"Docs: {SCHEMA_DOCS_URL}")
  print("=" * 60 + "\n")


class Severity(Enum):
  ERROR = auto()
  WARNING = auto()
  INFO = auto()


@dataclass(frozen=True)
class Defect:
  severity: Severity
  problem: str
  impact: str
  migration: str
  json_path: str
  upstream_fix: str | None = None

  def format_message(self) -> str:
    lines = [f"{self.problem}. {self.impact}.", f"Run {self.migration} to fix locally."]
    if self.upstream_fix:
      lines.append(self.upstream_fix + ".")
    return " ".join(lines)


@dataclass
class DefectReport:
  filepath: str
  dataset_path: str
  defects: list[Defect] = field(default_factory=list)

  @property
  def has_errors(self) -> bool:
    return any(d.severity == Severity.ERROR for d in self.defects)

  @property
  def has_warnings(self) -> bool:
    return any(d.severity == Severity.WARNING for d in self.defects)

  def infer_upstream_repo(self) -> str | None:
    parts = self.dataset_path.split("/")
    if len(parts) >= 2:
      collection, org = parts[0], parts[1]
      if collection == "nextstrain":
        return f"nextstrain/{org}"
      if collection == "community":
        return f"{org}/{parts[2]}" if len(parts) >= 3 else org
    return None


@dataclass
class ValidationContext:
  reports: dict[str, DefectReport] = field(default_factory=dict)

  def get_reports(self) -> list[DefectReport]:
    return list(self.reports.values())


@dataclass(frozen=True)
class SchemaIndex:
  path_to_props: dict[str, frozenset[str]]
  prop_to_paths: dict[str, tuple[str, ...]]


def get_current_branch() -> str:
  branch = run("git rev-parse --abbrev-ref HEAD", error_if_empty=True)
  assert branch is not None
  return branch


def remote_branch_exists(repo: str, branch: str) -> bool:
  url = f"https://api.github.com/repos/{repo}/branches/{branch}"
  req = urllib.request.Request(url, method="HEAD")
  try:
    with urllib.request.urlopen(req, timeout=10) as response:
      return response.status == 200
  except HTTPError:
    return False


@lru_cache(maxsize=1)
def get_schema_branch() -> str:
  current = get_current_branch()
  if remote_branch_exists(NEXTCLADE_REPO, current):
    l.info(f"Using schema from '{NEXTCLADE_REPO}' branch '{current}'")
    return current
  l.info(f"Branch '{current}' not found in '{NEXTCLADE_REPO}', using 'master'")
  return "master"


def _load_local_schema(schemas_dir: Path) -> dict:
  schema_path = schemas_dir / SCHEMA_FILENAME
  with schema_path.open() as f:
    return json.load(f)


@lru_cache(maxsize=1)
def _fetch_remote_schema() -> dict:
  branch = get_schema_branch()
  url = SCHEMA_URL_TEMPLATE.format(repo=NEXTCLADE_REPO, branch=branch, path=SCHEMA_PATH)
  l.info(f"Fetching schema from {url}")
  with urllib.request.urlopen(url, timeout=30) as response:
    return json.loads(response.read().decode('utf-8'))


def _extract_dataset_path(filepath: str) -> str:
  parts = Path(filepath).parts
  try:
    data_idx = parts.index("data")
    return "/".join(parts[data_idx + 1 : -1])
  except ValueError:
    return filepath


def _build_schema_index(schema: dict) -> SchemaIndex:
  path_to_props: dict[str, set[str]] = defaultdict(set)
  prop_to_paths: dict[str, list[str]] = defaultdict(list)

  def resolve_ref(ref: str) -> dict | None:
    if not ref.startswith("#/"):
      return None
    parts = ref[2:].split("/")
    node = schema
    for part in parts:
      if isinstance(node, dict) and part in node:
        node = node[part]
      else:
        return None
    return node if isinstance(node, dict) else None

  def traverse(node: Any, current_path: str, visited: frozenset[int] | None = None) -> None:
    if not isinstance(node, dict):
      return

    node_id = id(node)
    visited = visited or frozenset()
    if node_id in visited:
      return
    visited = visited | {node_id}

    if "$ref" in node:
      ref_schema = resolve_ref(node["$ref"])
      if ref_schema:
        traverse(ref_schema, current_path, visited)
      return

    if "properties" in node:
      props = node["properties"]
      path_to_props[current_path].update(props.keys())
      for prop_name, prop_schema in props.items():
        full_path = f"{current_path}.{prop_name}" if current_path else prop_name
        prop_to_paths[prop_name].append(full_path)
        traverse(prop_schema, full_path, visited)

    for keyword in ("allOf", "anyOf", "oneOf"):
      if keyword in node:
        for item in node[keyword]:
          traverse(item, current_path, visited)

    if isinstance(node.get("additionalProperties"), dict):
      traverse(node["additionalProperties"], current_path, visited)

    if isinstance(node.get("items"), dict):
      traverse(node["items"], current_path, visited)

  traverse(schema, "")

  return SchemaIndex(
    path_to_props={k: frozenset(v) for k, v in path_to_props.items()},
    prop_to_paths={k: tuple(v) for k, v in prop_to_paths.items()},
  )


def _suggest_correction(
  unknown_prop: str,
  parent_path: str,
  schema_index: SchemaIndex,
) -> str | None:
  valid_at_level = schema_index.path_to_props.get(parent_path, frozenset())

  if valid_at_level:
    match = process.extractOne(
      unknown_prop,
      valid_at_level,
      scorer=fuzz.ratio,
      score_cutoff=FUZZY_MATCH_THRESHOLD,
    )
    if match:
      suggested_prop = match[0]
      full_suggestion = f"{parent_path}.{suggested_prop}" if parent_path else suggested_prop
      return f"did you mean '{full_suggestion}'?"

  if unknown_prop in schema_index.prop_to_paths:
    valid_locations = schema_index.prop_to_paths[unknown_prop]
    current_full = f"{parent_path}.{unknown_prop}" if parent_path else unknown_prop
    other_locations = [loc for loc in valid_locations if loc != current_full]
    if other_locations:
      if len(other_locations) == 1:
        return f"belongs at '{other_locations[0]}'"
      return f"belongs at one of: {', '.join(repr(loc) for loc in other_locations)}"

  all_props = set(schema_index.prop_to_paths.keys())
  if all_props:
    match = process.extractOne(
      unknown_prop,
      all_props,
      scorer=fuzz.ratio,
      score_cutoff=FUZZY_MATCH_THRESHOLD,
    )
    if match:
      suggested_prop = match[0]
      valid_locations = schema_index.prop_to_paths[suggested_prop]
      if len(valid_locations) == 1:
        return f"did you mean '{valid_locations[0]}'?"
      return f"did you mean '{suggested_prop}'? Valid locations: {', '.join(repr(loc) for loc in valid_locations)}"

  return None


def _find_unknown_properties(
  data: Any,
  schema: dict,
  schema_index: SchemaIndex,
) -> list[tuple[str, str]]:
  strict_schema = _make_strict_schema(schema)
  validator = Draft7Validator(strict_schema)
  return _collect_unknown_property_warnings(validator.iter_errors(data), schema_index)


def _collect_unknown_property_warnings(
  errors: Any,
  schema_index: SchemaIndex,
) -> list[tuple[str, str]]:
  warnings: list[tuple[str, str]] = []
  for error in errors:
    if error.validator == "additionalProperties":
      path_parts = [str(p) for p in error.absolute_path]
      parent_path = '.'.join(path_parts)
      extras = [e for e in error.message.split("'")[1::2] if e != "$schema"]
      for extra in extras:
        full_path = f"{parent_path}.{extra}" if parent_path else extra
        suggestion = _suggest_correction(extra, parent_path, schema_index)
        message = f"Unknown property '{full_path}' - {suggestion}" if suggestion else f"Unknown property '{full_path}'"
        warnings.append((message, full_path))
    if error.context:
      warnings.extend(_collect_unknown_property_warnings(error.context, schema_index))
  return warnings


def _make_strict_schema(schema: dict) -> dict:
  import copy
  schema = copy.deepcopy(schema)
  _add_strict_recursive(schema)
  return schema


def _add_strict_recursive(node: Any) -> None:
  if isinstance(node, dict):
    if node.get("type") == "object" and "properties" in node:
      node.setdefault("additionalProperties", False)
    for v in node.values():
      _add_strict_recursive(v)
  elif isinstance(node, list):
    for item in node:
      _add_strict_recursive(item)


def _find_line_number(filepath: str, json_path: str) -> int | None:
  if not json_path:
    return None
  key = json_path.split(".")[-1]
  pattern = re.compile(rf'^\s*"{re.escape(key)}"\s*:')
  try:
    with open(filepath, encoding="utf-8") as f:
      for lineno, line in enumerate(f, start=1):
        if pattern.match(line):
          return lineno
  except OSError:
    pass
  return None


def _format_location(filepath: str, lineno: int | None) -> str:
  return f"{filepath}:{lineno}" if lineno else filepath


def _emit_ci_warning(filepath: str, message: str, json_path: str | None = None) -> None:
  lineno = _find_line_number(filepath, json_path) if json_path else None
  location = _format_location(filepath, lineno)
  if os.environ.get("GITHUB_ACTIONS"):
    line_part = f",line={lineno}" if lineno else ""
    print(f"::warning file={filepath}{line_part}::{message}")
  else:
    l.warning(f"{location}: {message}")


def _emit_defect(filepath: str, defect: Defect, json_path: str | None = None) -> None:
  lineno = _find_line_number(filepath, json_path) if json_path else None
  location = _format_location(filepath, lineno)
  message = defect.format_message()
  if os.environ.get("GITHUB_ACTIONS"):
    level = "error" if defect.severity == Severity.ERROR else "warning"
    line_part = f",line={lineno}" if lineno else ""
    print(f"::{level} file={filepath}{line_part}::{message}")
  else:
    log_fn = l.error if defect.severity == Severity.ERROR else l.warning
    log_fn(f"{location}: {message}")


def _upstream_hint(repo: str | None) -> str:
  if repo:
    return f"Fix in upstream pipeline ({repo}) to prevent recurrence"
  return "Fix in upstream build pipeline to prevent recurrence"


def _check_known_defects(data: dict, upstream_repo: str | None) -> list[Defect]:
  defects: list[Defect] = []
  defects.extend(_check_misplaced_mut_labels(data, upstream_repo))
  defects.extend(_check_qc_defects(data, upstream_repo))
  defects.extend(_check_misplaced_properties(data, upstream_repo))
  defects.extend(_check_alignment_param_typos(data, upstream_repo))
  return defects


def _check_misplaced_mut_labels(data: dict, upstream_repo: str | None) -> list[Defect]:
  defects: list[Defect] = []

  if "nucMutLabelMap" in data:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Misplaced 'nucMutLabelMap' at root level",
      impact="Nucleotide mutation labels not applied to results",
      migration="migrations/migrate_008_move_mut_labels.py",
      json_path="nucMutLabelMap",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  if "nucMutLabelMapReverse" in data:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Legacy v2 field 'nucMutLabelMapReverse' at root level",
      impact="No effect (reverse map computed at runtime in v3)",
      migration="migrations/migrate_009_remove_nuc_mut_label_map_reverse.py",
      json_path="nucMutLabelMapReverse",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  if "mutLabelMap" in data:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Misplaced 'mutLabelMap' at root level",
      impact="Mutation labels not applied to results",
      migration="migrations/migrate_008_move_mut_labels.py",
      json_path="mutLabelMap",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  mut_labels = data.get("mutLabels")
  if isinstance(mut_labels, dict) and "nucMutLabelMapReverse" in mut_labels:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Legacy v2 field 'mutLabels.nucMutLabelMapReverse'",
      impact="No effect (reverse map computed at runtime in v3)",
      migration="migrations/migrate_009_remove_nuc_mut_label_map_reverse.py",
      json_path="mutLabels.nucMutLabelMapReverse",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  return defects


def _check_qc_defects(data: dict, upstream_repo: str | None) -> list[Defect]:
  defects: list[Defect] = []
  qc = data.get("qc")
  if not isinstance(qc, dict):
    return defects

  if "divergence" in qc:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Unknown QC rule 'qc.divergence'",
      impact="No effect (divergence computed at runtime, not a QC rule)",
      migration="migrations/migrate_012_remove_qc_divergence.py",
      json_path="qc.divergence",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  missing_data = qc.get("missingData")
  if isinstance(missing_data, dict) and "scoreWeight" in missing_data:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Unknown field 'qc.missingData.scoreWeight'",
      impact="No effect (use 'missingDataThreshold' and 'scoreBias' instead)",
      migration="migrations/migrate_011_remove_qc_score_weight.py",
      json_path="qc.missingData.scoreWeight",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  mixed_sites = qc.get("mixedSites")
  if isinstance(mixed_sites, dict) and "scoreWeight" in mixed_sites:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Unknown field 'qc.mixedSites.scoreWeight'",
      impact="No effect (use 'mixedSitesThreshold' instead)",
      migration="migrations/migrate_011_remove_qc_score_weight.py",
      json_path="qc.mixedSites.scoreWeight",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  frame_shifts = qc.get("frameShifts")
  if isinstance(frame_shifts, dict) and "ignoreFrameShifts" in frame_shifts:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Field 'qc.frameShifts.ignoreFrameShifts' was renamed to 'ignoredFrameShifts'",
      impact="Frame shift exclusions not applied",
      migration="migrations/migrate_010_rename_ignore_frame_shifts.py",
      json_path="qc.frameShifts.ignoreFrameShifts",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  return defects


def _check_misplaced_properties(data: dict, upstream_repo: str | None) -> list[Defect]:
  defects: list[Defect] = []

  if "geneOrderPreference" in data:
    defects.append(Defect(
      severity=Severity.WARNING,
      problem="Field 'geneOrderPreference' was renamed to 'cdsOrderPreference'",
      impact="CDS display order uses default",
      migration="migrations/migrate_013_rename_gene_order_preference.py",
      json_path="geneOrderPreference",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  if "placementMaskRanges" in data:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Misplaced 'placementMaskRanges' in pathogen.json",
      impact="Placement masking not applied (belongs in tree.json at .meta.extensions.nextclade.placement_mask_ranges)",
      migration="migrations/migrate_016_fix_misplaced_placement_mask_ranges.py",
      json_path="placementMaskRanges",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  alignment_params = data.get("alignmentParams")
  if isinstance(alignment_params, dict):
    if "includeReference" in alignment_params:
      defects.append(Defect(
        severity=Severity.WARNING,
        problem="Misplaced 'alignmentParams.includeReference'",
        impact="Setting ignored (move to 'generalParams.includeReference')",
        migration="migrations/migrate_014_move_general_params.py",
        json_path="alignmentParams.includeReference",
        upstream_fix=_upstream_hint(upstream_repo),
      ))

    if "includeNearestNodeInfo" in alignment_params:
      defects.append(Defect(
        severity=Severity.WARNING,
        problem="Misplaced 'alignmentParams.includeNearestNodeInfo'",
        impact="Setting ignored (move to 'generalParams.includeNearestNodeInfo')",
        migration="migrations/migrate_014_move_general_params.py",
        json_path="alignmentParams.includeNearestNodeInfo",
        upstream_fix=_upstream_hint(upstream_repo),
      ))

  return defects


def _check_alignment_param_typos(data: dict, upstream_repo: str | None) -> list[Defect]:
  defects: list[Defect] = []
  alignment_params = data.get("alignmentParams")
  if isinstance(alignment_params, dict) and "excessBandwith" in alignment_params:
    defects.append(Defect(
      severity=Severity.WARNING,
      problem="Typo 'alignmentParams.excessBandwith' (missing 'd')",
      impact="Default bandwidth (9) used instead (rename to 'excessBandwidth')",
      migration="migrations/migrate_015_fix_excess_bandwidth_typo.py",
      json_path="alignmentParams.excessBandwith",
      upstream_fix=_upstream_hint(upstream_repo),
    ))
  return defects
