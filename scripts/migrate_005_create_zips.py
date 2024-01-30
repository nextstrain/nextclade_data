from os.path import join, dirname
from shutil import move

from lib.fs import find_files, make_zip, rmrf

tmp_dir = "data_temp/"


def main():
  files = list(find_files("pathogen.json", here="data_output/"))
  for file in files:
    dataset_dir = dirname(file)
    zip_basename_tmp = join(tmp_dir, "dataset")
    zip_basename = join(dataset_dir, "dataset")
    rmrf(f"{zip_basename}.zip")
    make_zip(dataset_dir, zip_basename_tmp)
    move(f"{zip_basename_tmp}.zip", f"{zip_basename}.zip")


if __name__ == '__main__':
  main()
