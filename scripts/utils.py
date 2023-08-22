import csv
import fnmatch
import json
import shutil
import subprocess
from collections import namedtuple, Counter
from datetime import datetime
from functools import reduce
from os import getcwd, walk, listdir, makedirs
from os.path import dirname, join, abspath, isdir
from typing import List, Iterable, TypeVar, Union, Callable

T = TypeVar('T')


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


def unique(it: Iterable[T]):
  return iter(set(it))


def find_duplicates(it: Iterable[T]) -> List[T]:
  return [x for x, occurrences in Counter(it).items() if occurrences > 1]


def format_list(it: Iterable, sep: str = ", ") -> str:
  return sep.join(map(lambda x: f"\"{x}\"", it))


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


def rmrf(some_path):
  shutil.rmtree(some_path, ignore_errors=True)


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


def now():
  return datetime.utcnow()


def now_iso():
  return to_iso(now())


def to_iso(date):
  return date.replace(microsecond=0).isoformat() + "Z"


def iso_to_iso_safe(date: str):
  return date.replace(":", "-").replace("T", "--")


def surround(strs: List[str], symbol: str):
  return list(f"{symbol}{s}{symbol}" for s in strs)


def quote(strs: List[str]):
  return surround(strs, "'")


def run(command, none_if_empty=False, error_if_empty=False, ignore_errors=False, custom_error_msg=None, stdin=None):
  res = subprocess.run(command, shell=True, check=False, capture_output=True, text=True, input=stdin)

  message = str(res.stderr) or str(res.stdout) or custom_error_msg
  message = f"\n  Message: {message}" if message else ''

  if not ignore_errors and (res.returncode != 0 or res.stderr):
    raise ValueError(
      f"The external process failed:\n  Command: {command}\n  Return code: {res.returncode}{message}")
  stdout = res.stdout.strip()
  if len(stdout) == 0:
    if none_if_empty:
      return None
    if error_if_empty:
      raise ChildProcessError(
        f"Received empty output, while expected non-empty:\n  Command: {command}\n  Return code: {res.returncode}{message}")
    return ""
  return stdout


def prepare_paths_args(paths: Union[str, List[str]] = getcwd()):
  return ' '.join(quote([paths] if type(paths) == str else paths))


def get_lines(s: str):
  lines = s.split("\n")
  lines = map(str.strip, lines)
  return iter(filter(len, lines))


def git_get_dirty_files(dirs: Union[str, List[str]] = getcwd()):
  lines = get_lines(run(f"git status --untracked --porcelain -- {prepare_paths_args(dirs)}"))
  return iter(map(lambda line: line.split(" ")[1], lines))


def git_dir_is_clean(dirs: Union[str, List[str]] = getcwd()):
  return len(list(git_get_dirty_files(dirs))) == 0


def git_get_initial_commit_hash():
  return run("git rev-list --max-parents=0 HEAD")


def git_get_current_commit_hash(branch: str = "HEAD", short=False):
  short_flag = "--short" if short else ""
  return run(f"git rev-parse {short_flag} '{branch}'", error_if_empty=True)


def git_get_modified_files(
  from_revision: str,
  to_revision: str = git_get_current_commit_hash(),
  dirs: Union[str, List[str]] = getcwd()
):
  return get_lines(
    run(f"git diff --name-only '{from_revision}' '{to_revision}' -- {prepare_paths_args(dirs)}")
  )


def git_check_tag(tag: str):
  try:
    return run(f"git check-ref-format 'tags/{tag}'")
  except Exception as e:
    raise ValueError(
      f"Invalid git tag format: '{tag}'. See: https://git-scm.com/docs/git-check-ref-format") from e


def git_add_all():
  return run("git add -A")


def git_commit(commit_message: str):
  run(f"git commit -q -m '{commit_message}'")


def git_push():
  run("git push -q")


def git_pull():
  run("git pull -q")


def git_commit_all(commit_message: str):
  git_add_all()
  git_commit(commit_message)
  return git_get_current_commit_hash()


def github_create_release(repo: str, version: str, commit_hash: str, release_notes: str, files=None):
  if files is None:
    files = []
  files = " ".join(quote(files))
  run(
    f"""
    gh release create \
      '{version}' \
      --repo "{repo}" \
      --title "{version}" \
      --target "{commit_hash}" \
      --notes-file - \
      {files}
    """,
    stdin=release_notes
  )


def find(predicate: Callable, it: Iterable[Union[T, None]]) -> Union[T, None]:
  return first(filter(predicate, iter(it)))


def find_index_by(predicate: Callable, it: Iterable[Union[T, None]]):
  return next((i for i, e in enumerate(it) if predicate(e)), None)


def first(it: Iterable[Union[T, None]]) -> Union[T, None]:
  return next(iter(it), None)
