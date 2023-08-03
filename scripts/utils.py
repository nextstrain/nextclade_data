import csv
import fnmatch
import json
import os
import shutil
from collections import namedtuple
from datetime import datetime
from functools import reduce
from os.path import join, dirname
from typing import List


def dict_to_namedtuple(name, dic):
  return namedtuple(name, dic.keys())(*dic.values())


def dict_set(obj: dict, key_path: List[str], value):
  for key in key_path[:-1]:
    obj = obj.setdefault(key, {})
  obj[key_path[-1]] = value


def dict_get(obj: dict, keys: List[str]):
  return reduce(lambda d, key: d.get(key) if d else None, keys, obj)


def dict_get_required(obj: dict, keys: List[str]):
  val = dict_get(obj, keys)
  if val is None:
    raise KeyError(f"Key not found: '{'.'.join(keys)}'")
  return val


def dict_remove(obj: dict, key: str):
  if obj.get(key) is not None:
    obj.pop(key)


def dict_remove_many(obj: dict, keys: List[str]):
  for key in keys:
    dict_remove(obj, key)


def list_cleanup(data):
  new_data = []
  for v in data:
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data.append(v)
  return new_data


def dict_cleanup(data):
  new_data = {}
  for k, v in data.items():
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data[k] = v
  return new_data


def find_files(pattern, here):
  for path, dirs, files in os.walk(os.path.abspath(here)):
    for filename in fnmatch.filter(files, pattern):
      yield join(path, filename)


def find_dirs(here):
  for path, dirs, _ in os.walk(os.path.abspath(here)):
    for dirr in dirs:
      yield join(path, dirr)


def find_dirs_here(here):
  return filter(os.path.isdir, [join(here, e) for e in os.listdir(here)])


def json_read(json_path) -> dict:
  with open(json_path, 'r') as f:
    return json.load(f)


def json_write(obj, filepath, no_sort_keys=False):
  ensure_dir(filepath)
  with open(filepath, "w") as f:
    json.dump(obj, f, indent=2, sort_keys=not no_sort_keys)
    f.write("\n")


def csv_read(csv_file_path) -> List[dict]:
  with open(csv_file_path, mode='r') as f:
    return list(csv.DictReader(f))


def copy(input_filepath, output_filepath):
  ensure_dir(output_filepath)
  shutil.copy2(input_filepath, output_filepath)


def rmrf(some_path):
  shutil.rmtree(some_path, ignore_errors=True)


def mkdir(dir_path):
  os.makedirs(dir_path, exist_ok=True)


def ensure_dir(file_path):
  mkdir(dirname(file_path))


def now():
  return datetime.utcnow()


def now_iso():
  return now().replace(microsecond=0).isoformat() + "Z"
