"""
Rename 'alignmentParams.excessBandwith' to 'alignmentParams.excessBandwidth'.

The misspelled key is silently ignored, so the default bandwidth (9)
is used instead of the intended value.
"""

from scripts.lib.container import dict_get
from scripts.lib.fs import find_files, json_read, json_write


def fix_excess_bandwidth_typo(pathogen: dict) -> dict:
  alignment_params = dict_get(pathogen, ["alignmentParams"])
  if isinstance(alignment_params, dict) and "excessBandwith" in alignment_params:
    value = alignment_params.pop("excessBandwith")
    alignment_params.setdefault("excessBandwidth", value)
  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = fix_excess_bandwidth_typo(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
