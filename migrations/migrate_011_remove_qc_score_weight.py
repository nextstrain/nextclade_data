"""
Remove nonexistent 'scoreWeight' from 'qc.missingData' and 'qc.mixedSites'.

These QC rules have no 'scoreWeight' parameter in Nextclade.
Sensitivity is controlled via 'missingDataThreshold'/'scoreBias' and
'mixedSitesThreshold' respectively.
"""

from scripts.lib.container import dict_get
from scripts.lib.fs import find_files, json_read, json_write


def remove_qc_score_weight(pathogen: dict) -> dict:
  for rule_name in ("missingData", "mixedSites"):
    rule = dict_get(pathogen, ["qc", rule_name])
    if isinstance(rule, dict):
      rule.pop("scoreWeight", None)
  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = remove_qc_score_weight(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
