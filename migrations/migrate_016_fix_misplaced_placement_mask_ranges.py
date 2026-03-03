"""
Move 'placementMaskRanges' from pathogen.json to tree.json.

This field belongs in tree.json at '.meta.extensions.nextclade.placement_mask_ranges'.
In pathogen.json it is silently ignored, so placement masking is not applied.

One-time fix for existing datasets. Dataset authors must also update their
upstream build pipelines to place this field in tree.json directly, otherwise
the next dataset update will re-introduce the defect.
"""

import json
from os.path import dirname, isfile, join

from scripts.lib.fs import file_read, file_write, find_files, json_read, json_write


def move_placement_mask_ranges(pathogen: dict, tree: dict) -> tuple[dict, dict]:
  ranges = pathogen.pop("placementMaskRanges", None)
  if ranges is None:
    return pathogen, tree

  meta = tree.setdefault("meta", {})
  extensions = meta.setdefault("extensions", {})
  nextclade = extensions.setdefault("nextclade", {})
  nextclade.setdefault("placement_mask_ranges", ranges)

  return pathogen, tree


def _detect_indent(text: str) -> int | None:
  """Return indent width if pretty-printed, None if compact."""
  for line in text.split("\n")[1:6]:
    stripped = line.lstrip(" ")
    if stripped and len(line) != len(stripped):
      return len(line) - len(stripped)
  return None


def _json_write_preserving_format(obj: dict, filepath: str, original_text: str) -> None:
  indent = _detect_indent(original_text)
  content = json.dumps(obj, indent=indent, ensure_ascii=False, sort_keys=False)
  if indent is not None:
    content += "\n"
  file_write(content, filepath)


def main():
  for pathogen_file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(pathogen_file)
    if "placementMaskRanges" not in pathogen:
      continue

    tree_file = join(dirname(pathogen_file), "tree.json")
    if not isfile(tree_file):
      continue

    tree_text = file_read(tree_file)
    tree = json.loads(tree_text)
    if tree.get("meta", {}).get("extensions", {}).get("nextclade", {}).get("placement_mask_ranges"):
      continue

    pathogen, tree = move_placement_mask_ranges(pathogen, tree)
    json_write(pathogen, pathogen_file, no_sort_keys=True)
    _json_write_preserving_format(tree, tree_file, tree_text)


if __name__ == '__main__':
  main()
