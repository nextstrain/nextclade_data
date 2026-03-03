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
