"""
Remove nonexistent 'qc.divergence' rule.

Divergence is computed at runtime, not a configurable QC rule.
"""

from scripts.lib.container import dict_get
from scripts.lib.fs import find_files, json_read, json_write


def remove_qc_divergence(pathogen: dict) -> dict:
  qc = dict_get(pathogen, ["qc"])
  if isinstance(qc, dict):
    qc.pop("divergence", None)
  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = remove_qc_divergence(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
