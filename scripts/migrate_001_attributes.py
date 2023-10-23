from lib.fs import find_files, json_read, json_write
from lib.container import dict_get, dict_remove, dict_cleanup, true_or_none


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
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

    json_write(dict_cleanup({
      **pathogen,
      "attributes": {
        "name": name,
        "reference name": ref_name,
        "reference accession": ref_accession,
        "experimental": experimental,
        "deprecated": deprecated,
      },
      "meta": {
        "source code": "https://github.com/nextstrain/nextclade_data",
        "bugs": "https://github.com/nextstrain/nextclade_data/issues",
        "authors": [
          "Nextstrain team <https://nextstrain.org>",
        ],
      },
    }), file, no_sort_keys=True)


if __name__ == '__main__':
  main()
