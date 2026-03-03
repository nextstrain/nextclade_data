"""
Rename 'geneOrderPreference' to 'cdsOrderPreference'.

The old name is silently ignored, so CDS display order falls back
to default.
"""

from scripts.lib.fs import find_files, json_read, json_write


def rename_gene_order_preference(pathogen: dict) -> dict:
  if "geneOrderPreference" in pathogen:
    value = pathogen.pop("geneOrderPreference")
    if value and "cdsOrderPreference" not in pathogen:
      pathogen["cdsOrderPreference"] = value
  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = rename_gene_order_preference(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
