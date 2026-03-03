"""
Move 'includeReference' and 'includeNearestNodeInfo' from
'alignmentParams' to 'generalParams'.

These control output behavior, not the alignment algorithm.
Under 'alignmentParams' they are silently ignored.
"""

from scripts.lib.container import dict_get
from scripts.lib.fs import find_files, json_read, json_write


def move_general_params(pathogen: dict) -> dict:
  alignment_params = dict_get(pathogen, ["alignmentParams"])
  if not isinstance(alignment_params, dict):
    return pathogen

  general_params = pathogen.setdefault("generalParams", {})

  for param in ("includeReference", "includeNearestNodeInfo"):
    if param in alignment_params:
      value = alignment_params.pop(param)
      general_params.setdefault(param, value)

  if alignment_params == {}:
    pathogen.pop("alignmentParams")

  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = move_general_params(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
