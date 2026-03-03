import json
import os
import urllib.request
from dataclasses import dataclass, field
from enum import Enum, auto
from functools import lru_cache
from pathlib import Path
from urllib.error import HTTPError
from typing import Any

from jsonschema import Draft7Validator, ValidationError

from .logger import l
from .process import run

NEXTCLADE_REPO = "nextstrain/nextclade"
SCHEMA_FILENAME = "input-pathogen-json.schema.json"
SCHEMA_PATH = f"packages/nextclade-schemas/{SCHEMA_FILENAME}"
SCHEMA_URL_TEMPLATE = "https://raw.githubusercontent.com/{repo}/refs/heads/{branch}/{path}"
SCHEMA_DOCS_URL = "https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html"


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


_defect_reports: dict[str, DefectReport] = {}


def get_defect_reports() -> list[DefectReport]:
  return list(_defect_reports.values())


def clear_defect_reports() -> None:
  _defect_reports.clear()


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


def fetch_schema(schemas_dir: Path | None = None) -> dict:
  if schemas_dir is not None:
    return _load_local_schema(schemas_dir)
  return _fetch_remote_schema()


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


def validate_pathogen_json(
  data: Any,
  filepath: str,
  schemas_dir: Path | None = None,
  dataset_path: str | None = None,
) -> None:
  schema = fetch_schema(schemas_dir)
  validator = Draft7Validator(schema)
  errors = []
  for error in validator.iter_errors(data):
    path = '.'.join(str(p) for p in error.absolute_path) or '(root)'
    errors.append(f"  {path}: {error.message}")
  if errors:
    raise ValidationError(f"Schema validation failed for '{filepath}':\n" + '\n'.join(errors))

  for warning in _find_extra_properties(data, schema):
    _emit_ci_warning(filepath, warning)

  report = DefectReport(
    filepath=filepath,
    dataset_path=dataset_path or _extract_dataset_path(filepath),
  )
  report.defects = _check_known_defects(data, report.infer_upstream_repo())

  if report.defects:
    if filepath not in _defect_reports:
      _defect_reports[filepath] = report
      for defect in report.defects:
        _emit_defect(filepath, defect)


def _extract_dataset_path(filepath: str) -> str:
  parts = Path(filepath).parts
  try:
    data_idx = parts.index("data")
    return "/".join(parts[data_idx + 1 : -1])
  except ValueError:
    return filepath


def _find_extra_properties(data: Any, schema: dict) -> list[str]:
  strict_schema = _make_strict_schema(schema)
  validator = Draft7Validator(strict_schema)
  return _collect_extra_property_warnings(validator.iter_errors(data))


def _collect_extra_property_warnings(errors: Any) -> list[str]:
  """Recursively collect additionalProperties errors from nested contexts."""
  warnings = []
  for error in errors:
    if error.validator == "additionalProperties":
      path_parts = [str(p) for p in error.absolute_path]
      extras = [e for e in error.message.split("'")[1::2] if e != "$schema"]
      for extra in extras:
        full_path = '.'.join(path_parts + [extra]) if path_parts else extra
        warnings.append(f"Unknown property '{full_path}'")
    if error.context:
      warnings.extend(_collect_extra_property_warnings(error.context))
  return warnings


def _make_strict_schema(schema: dict) -> dict:
  """Recursively add additionalProperties: false to all objects."""
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


def _emit_ci_warning(filepath: str, message: str) -> None:
  if os.environ.get("GITHUB_ACTIONS"):
    print(f"::warning file={filepath}::{message}")
  else:
    l.warning(f"{filepath}: {message}")


def _emit_defect(filepath: str, defect: Defect) -> None:
  message = defect.format_message()
  if os.environ.get("GITHUB_ACTIONS"):
    level = "error" if defect.severity == Severity.ERROR else "warning"
    print(f"::{level} file={filepath}::{message}")
  else:
    log_fn = l.error if defect.severity == Severity.ERROR else l.warning
    log_fn(f"{filepath}: {message}")


def print_defect_summary() -> None:
  reports = [r for r in _defect_reports.values() if r.defects]
  if not reports:
    return

  errors = [r for r in reports if r.has_errors]
  warnings = [r for r in reports if r.has_warnings and not r.has_errors]
  info_only = [r for r in reports if not r.has_errors and not r.has_warnings]

  print("\n" + "=" * 60)
  print("DATASET DEFECTS SUMMARY")
  print("=" * 60)

  if errors:
    print(f"\n{len(errors)} dataset(s) with ERRORS (features broken):")
    for r in errors:
      upstream = r.infer_upstream_repo()
      upstream_hint = f" [upstream: {upstream}]" if upstream else ""
      print(f"  - {r.dataset_path}{upstream_hint}")
      for d in r.defects:
        if d.severity == Severity.ERROR:
          print(f"      {d.problem}")

  if warnings:
    print(f"\n{len(warnings)} dataset(s) with WARNINGS (using defaults):")
    for r in warnings:
      upstream = r.infer_upstream_repo()
      upstream_hint = f" [upstream: {upstream}]" if upstream else ""
      print(f"  - {r.dataset_path}{upstream_hint}")
      for d in r.defects:
        if d.severity == Severity.WARNING:
          print(f"      {d.problem}")

  if info_only:
    print(f"\n{len(info_only)} dataset(s) with INFO (deprecated fields):")
    for r in info_only:
      print(f"  - {r.dataset_path}")

  print("\n" + "-" * 60)
  print("Run migration scripts to fix locally.")
  print("Notify upstream maintainers to prevent defect recurrence.")
  print(f"Docs: {SCHEMA_DOCS_URL}")
  print("=" * 60 + "\n")


def _upstream_hint(repo: str | None) -> str:
  if repo:
    return f"Fix in upstream pipeline ({repo}) to prevent recurrence on next dataset update"
  return "Fix in upstream build pipeline to prevent recurrence on next dataset update"


def _check_known_defects(data: dict, upstream_repo: str | None) -> list[Defect]:
  defects: list[Defect] = []
  defects.extend(_check_misplaced_mut_labels(data, upstream_repo))
  defects.extend(_check_qc_defects(data, upstream_repo))
  defects.extend(_check_misplaced_properties(data, upstream_repo))
  defects.extend(_check_alignment_param_typos(data, upstream_repo))
  return defects


def _check_misplaced_mut_labels(data: dict, upstream_repo: str | None) -> list[Defect]:
  """Detect mutation label maps at wrong nesting level."""
  defects: list[Defect] = []

  if "nucMutLabelMap" in data:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Misplaced 'nucMutLabelMap' at root level",
      impact="Nucleotide mutation labels not applied to results",
      migration="migrations/migrate_008_move_mut_labels.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  if "nucMutLabelMapReverse" in data:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Legacy v2 field 'nucMutLabelMapReverse' at root level",
      impact="No effect (reverse map computed at runtime in v3)",
      migration="migrations/migrate_009_remove_nuc_mut_label_map_reverse.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  if "mutLabelMap" in data:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Misplaced 'mutLabelMap' at root level",
      impact="Mutation labels not applied to results",
      migration="migrations/migrate_008_move_mut_labels.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  mut_labels = data.get("mutLabels")
  if isinstance(mut_labels, dict) and "nucMutLabelMapReverse" in mut_labels:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Legacy v2 field 'mutLabels.nucMutLabelMapReverse'",
      impact="No effect (reverse map computed at runtime in v3)",
      migration="migrations/migrate_009_remove_nuc_mut_label_map_reverse.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  return defects


def _check_qc_defects(data: dict, upstream_repo: str | None) -> list[Defect]:
  """Detect nonexistent or renamed QC properties."""
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
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  missing_data = qc.get("missingData")
  if isinstance(missing_data, dict) and "scoreWeight" in missing_data:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Unknown field 'qc.missingData.scoreWeight'",
      impact="No effect (use 'missingDataThreshold' and 'scoreBias' instead)",
      migration="migrations/migrate_011_remove_qc_score_weight.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  mixed_sites = qc.get("mixedSites")
  if isinstance(mixed_sites, dict) and "scoreWeight" in mixed_sites:
    defects.append(Defect(
      severity=Severity.INFO,
      problem="Unknown field 'qc.mixedSites.scoreWeight'",
      impact="No effect (use 'mixedSitesThreshold' instead)",
      migration="migrations/migrate_011_remove_qc_score_weight.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  frame_shifts = qc.get("frameShifts")
  if isinstance(frame_shifts, dict) and "ignoreFrameShifts" in frame_shifts:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Renamed field 'qc.frameShifts.ignoreFrameShifts'",
      impact="Frame shift exclusions NOT applied (use 'ignoredFrameShifts')",
      migration="migrations/migrate_010_rename_ignore_frame_shifts.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  return defects


def _check_misplaced_properties(data: dict, upstream_repo: str | None) -> list[Defect]:
  """Detect properties at wrong location or with old names."""
  defects: list[Defect] = []

  if "geneOrderPreference" in data:
    defects.append(Defect(
      severity=Severity.WARNING,
      problem="Renamed field 'geneOrderPreference'",
      impact="CDS display order falls back to default (use 'cdsOrderPreference')",
      migration="migrations/migrate_013_rename_gene_order_preference.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))

  if "placementMaskRanges" in data:
    defects.append(Defect(
      severity=Severity.ERROR,
      problem="Misplaced 'placementMaskRanges' in pathogen.json",
      impact="Placement masking NOT applied (belongs in tree.json at .meta.extensions.nextclade.placement_mask_ranges)",
      migration="migrations/migrate_016_fix_misplaced_placement_mask_ranges.py",
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
        upstream_fix=_upstream_hint(upstream_repo),
      ))

    if "includeNearestNodeInfo" in alignment_params:
      defects.append(Defect(
        severity=Severity.WARNING,
        problem="Misplaced 'alignmentParams.includeNearestNodeInfo'",
        impact="Setting ignored (move to 'generalParams.includeNearestNodeInfo')",
        migration="migrations/migrate_014_move_general_params.py",
        upstream_fix=_upstream_hint(upstream_repo),
      ))

  return defects


def _check_alignment_param_typos(data: dict, upstream_repo: str | None) -> list[Defect]:
  """Detect known typos in alignment parameters."""
  defects: list[Defect] = []
  alignment_params = data.get("alignmentParams")
  if isinstance(alignment_params, dict) and "excessBandwith" in alignment_params:
    defects.append(Defect(
      severity=Severity.WARNING,
      problem="Typo 'alignmentParams.excessBandwith' (missing 'd')",
      impact="Default bandwidth (9) used instead (rename to 'excessBandwidth')",
      migration="migrations/migrate_015_fix_excess_bandwidth_typo.py",
      upstream_fix=_upstream_hint(upstream_repo),
    ))
  return defects
