from lib.container import dict_rename_many
from lib.fs import find_files, json_read, json_write


def rename_default_gene(pathogen):
  return dict_rename_many(
    pathogen, {
      "defaultGene": "defaultCds",
      "geneOrderPreference": "cdsOrderPreference"
    }
  )


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = rename_default_gene(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
