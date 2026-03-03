import json
import urllib.request
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


def validate_pathogen_json(data: Any, filepath: str, schemas_dir: Path | None = None) -> None:
  schema = fetch_schema(schemas_dir)
  validator = Draft7Validator(schema)
  errors = []
  for error in validator.iter_errors(data):
    path = '.'.join(str(p) for p in error.absolute_path) or '(root)'
    errors.append(f"  {path}: {error.message}")
  if errors:
    raise ValidationError(f"Schema validation failed for '{filepath}':\n" + '\n'.join(errors))

  for warning in _find_extra_properties(data, schema):
    emit_ci_warning(filepath, warning)

  for warning in _check_known_defects(data):
    emit_ci_warning(filepath, warning)


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
        warnings.append(f"Unknown property '{full_path}' - may be a typo or misplaced field")
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


def emit_ci_warning(filepath: str, message: str) -> None:
  import os
  if os.environ.get("GITHUB_ACTIONS"):
    print(f"::warning file={filepath}::{message}")
  else:
    l.warning(f"{filepath}: {message}")


def _check_known_defects(data: dict) -> list[str]:
  warnings: list[str] = []
  warnings.extend(_check_misplaced_mut_labels(data))
  warnings.extend(_check_qc_defects(data))
  warnings.extend(_check_misplaced_properties(data))
  warnings.extend(_check_alignment_param_typos(data))
  return warnings


def _check_misplaced_mut_labels(data: dict) -> list[str]:
  """Detect mutation label maps at wrong nesting level."""
  warnings: list[str] = []

  if "nucMutLabelMap" in data:
    warnings.append(
      "Misplaced 'nucMutLabelMap' at root level. "
      "Move to 'mutLabels.nucMutLabelMap'. "
      "Fix: migrations/migrate_008_move_mut_labels.py"
    )

  if "nucMutLabelMapReverse" in data:
    warnings.append(
      "Legacy v2 field 'nucMutLabelMapReverse' at root level. "
      "This field is not used by Nextclade v3 (reverse map is computed at runtime). "
      "Fix: migrations/migrate_009_remove_nuc_mut_label_map_reverse.py"
    )

  if "mutLabelMap" in data:
    warnings.append(
      "Misplaced 'mutLabelMap' at root level. "
      "Move contents to 'mutLabels' (e.g. 'mutLabels.aaMutLabelMap'). "
      "Fix: migrations/migrate_008_move_mut_labels.py"
    )

  mut_labels = data.get("mutLabels")
  if isinstance(mut_labels, dict) and "nucMutLabelMapReverse" in mut_labels:
    warnings.append(
      "Legacy v2 field 'mutLabels.nucMutLabelMapReverse'. "
      "This field is not used by Nextclade v3 (reverse map is computed at runtime). "
      "Fix: migrations/migrate_009_remove_nuc_mut_label_map_reverse.py"
    )

  return warnings


def _check_qc_defects(data: dict) -> list[str]:
  """Detect nonexistent or renamed QC properties."""
  warnings: list[str] = []
  qc = data.get("qc")
  if not isinstance(qc, dict):
    return warnings

  if "divergence" in qc:
    warnings.append(
      "Unknown QC rule 'qc.divergence'. "
      "Divergence is computed at runtime, not a configurable QC rule. "
      "Fix: migrations/migrate_012_remove_qc_divergence.py"
    )

  missing_data = qc.get("missingData")
  if isinstance(missing_data, dict) and "scoreWeight" in missing_data:
    warnings.append(
      "Unknown field 'qc.missingData.scoreWeight'. "
      "This QC rule has no scoreWeight parameter. "
      "Tune sensitivity via 'missingDataThreshold' and 'scoreBias' instead. "
      "Fix: migrations/migrate_011_remove_qc_score_weight.py"
    )

  mixed_sites = qc.get("mixedSites")
  if isinstance(mixed_sites, dict) and "scoreWeight" in mixed_sites:
    warnings.append(
      "Unknown field 'qc.mixedSites.scoreWeight'. "
      "This QC rule has no scoreWeight parameter. "
      "Tune sensitivity via 'mixedSitesThreshold' instead. "
      "Fix: migrations/migrate_011_remove_qc_score_weight.py"
    )

  frame_shifts = qc.get("frameShifts")
  if isinstance(frame_shifts, dict) and "ignoreFrameShifts" in frame_shifts:
    warnings.append(
      "Renamed field 'qc.frameShifts.ignoreFrameShifts'. "
      "Use 'ignoredFrameShifts' (past tense). "
      "The current value is silently ignored, so listed frame shifts are NOT being excluded from QC. "
      "Fix: migrations/migrate_010_rename_ignore_frame_shifts.py"
    )

  return warnings


def _check_misplaced_properties(data: dict) -> list[str]:
  """Detect properties at wrong location or with old names."""
  warnings: list[str] = []

  if "geneOrderPreference" in data:
    warnings.append(
      "Renamed field 'geneOrderPreference'. "
      "Use 'cdsOrderPreference'. "
      "The current value is silently ignored, so CDS display order falls back to default. "
      "Fix: migrations/migrate_013_rename_gene_order_preference.py"
    )

  if "placementMaskRanges" in data:
    warnings.append(
      "Misplaced 'placementMaskRanges' in pathogen.json. "
      "This field belongs in tree.json at '.meta.extensions.nextclade.placementMaskRanges'. "
      "The current value is silently ignored, so placement masking is NOT applied. "
      "Requires manual edit of tree.json."
    )

  alignment_params = data.get("alignmentParams")
  if isinstance(alignment_params, dict):
    if "includeReference" in alignment_params:
      warnings.append(
        "Misplaced 'alignmentParams.includeReference'. "
        "This is not an alignment parameter. Move to 'generalParams.includeReference'. "
        "Fix: migrations/migrate_014_move_general_params.py"
      )

    if "includeNearestNodeInfo" in alignment_params:
      warnings.append(
        "Misplaced 'alignmentParams.includeNearestNodeInfo'. "
        "This is not an alignment parameter. Move to 'generalParams.includeNearestNodeInfo'. "
        "Fix: migrations/migrate_014_move_general_params.py"
      )

  return warnings


def _check_alignment_param_typos(data: dict) -> list[str]:
  """Detect known typos in alignment parameters."""
  warnings: list[str] = []
  alignment_params = data.get("alignmentParams")
  if isinstance(alignment_params, dict) and "excessBandwith" in alignment_params:
    warnings.append(
      "Typo 'alignmentParams.excessBandwith' (missing 'd'). "
      "Rename to 'alignmentParams.excessBandwidth'. "
      "The current value is silently ignored, so the default bandwidth (9) is used instead. "
      "Fix: migrations/migrate_015_fix_excess_bandwidth_typo.py"
    )
  return warnings
