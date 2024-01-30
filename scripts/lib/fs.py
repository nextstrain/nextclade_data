import csv
import fnmatch
import json
import os
import shutil
from os import walk, listdir, makedirs
from os.path import dirname, join, abspath, isdir, isfile, islink
from typing import List


def find_files(pattern, here):
  for path, dirs, files in walk(abspath(here)):
    for filename in fnmatch.filter(files, pattern):
      yield join(path, filename)


def find_dirs(here):
  for path, dirs, _ in walk(abspath(here)):
    for dirr in dirs:
      yield join(path, dirr)


def find_dirs_here(here):
  return filter(isdir, [join(here, e) for e in listdir(here)])


def file_read(json_path) -> str:
  with open(json_path, 'r') as f:
    return f.read()


def file_write(data, filepath):
  ensure_dir(filepath)
  with open(filepath, "w") as f:
    f.write(f"{data.strip()}\n")


def json_read(json_path) -> dict:
  return json.loads(file_read(json_path))


def json_write(obj, filepath, no_sort_keys=False):
  content = json.dumps(obj, indent=2, sort_keys=not no_sort_keys, ensure_ascii=False)
  content += "\n"
  file_write(content, filepath)


def csv_read(csv_file_path) -> List[dict]:
  with open(csv_file_path, mode='r') as f:
    return list(csv.DictReader(f))


def copy(input_filepath, output_filepath):
  ensure_dir(output_filepath)
  shutil.copy2(input_filepath, output_filepath)


def rmrf(some_path, ignore_errors=True):
  if isfile(some_path) or islink(some_path):
    os.unlink(some_path)
  elif isdir(some_path):
    shutil.rmtree(some_path, ignore_errors=ignore_errors)
  elif not ignore_errors:
    raise FileNotFoundError(some_path)


def mkdir(dir_path):
  makedirs(dir_path, exist_ok=True)


def ensure_dir(file_path):
  dir_path = dirname(file_path)
  if len(dir_path.strip()) == 0:
    return
  mkdir(dir_path)


def make_zip(input_dir, out_zip):
  shutil.make_archive(
    base_name=out_zip,
    format='zip',
    root_dir=input_dir,
  )
