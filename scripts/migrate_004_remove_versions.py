from lib.container import dict_remove
from lib.fs import find_files, json_read, json_write


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    dict_remove(pathogen, "version")
    dict_remove(pathogen, "versions")
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
