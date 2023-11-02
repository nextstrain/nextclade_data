from lib.fs import find_files, json_read, json_write
from lib.container import dict_get, dict_remove, dict_cleanup, true_or_none


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)

    if type(dict_get(pathogen, ["attributes", "name"])) is not str:
      name = dict_get(pathogen, ["attributes", "name", "valueFriendly"])
      ref_accession = dict_get(pathogen, ["attributes", "reference", "value"])
      ref_name = dict_get(pathogen, ["attributes", "reference", "valueFriendly"])
      experimental = true_or_none(dict_get(pathogen, ["experimental"]))
      deprecated = true_or_none(dict_get(pathogen, ["deprecated"]))

      dict_remove(pathogen, "attributes")
      dict_remove(pathogen, "experimental")
      dict_remove(pathogen, "deprecated")
      dict_remove(pathogen, "enabled")
      dict_remove(pathogen, "official")
      dict_remove(pathogen, "community")

      pathogen = {
        **pathogen,
        "attributes": {
          "name": name,
          "reference name": ref_name,
          "reference accession": ref_accession,
          "experimental": experimental,
          "deprecated": deprecated,
        }
      }

    dict_remove(pathogen, "meta")

    json_write(dict_cleanup({
      **pathogen,
      "maintenance": {
        "website": [
          "https://nextstrain.org",
          "https://clades.nextstrain.org",
        ],
        "documentation": [
          "https://github.com/nextstrain/nextclade_data",
          "https://docs.nextstrain.org/projects/nextclade"
        ],
        "source code": [
          "https://github.com/nextstrain/nextclade_data",
          "https://github.com/neherlab/nextclade_data_workflows",
        ],
        "issues": [
          "https://github.com/nextstrain/nextclade_data",
          "https://github.com/nextstrain/nextclade_data/issues",
        ],
        "organizations": ["Nextstrain"],
        "authors": ["Nextstrain team <https://nextstrain.org>"],
        "provenance": [],
        "acknowledgements": [],
      },
    }), file, no_sort_keys=True)


if __name__ == '__main__':
  main()
