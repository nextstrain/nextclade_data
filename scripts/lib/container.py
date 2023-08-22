from collections import namedtuple, Counter
from functools import reduce
from typing import List, Iterable, TypeVar, Callable, Union

T = TypeVar('T')


def dict_to_namedtuple(name: str, dic: dict):
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


def list_cleanup(data: List) -> List:
  new_data = []
  for v in data:
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data.append(v)
  return new_data


def dict_cleanup(data: dict) -> dict:
  new_data = {}
  for k, v in data.items():
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data[k] = v
  return new_data


def find(predicate: Callable, it: Iterable[Union[T, None]]) -> Union[T, None]:
  return first(filter(predicate, iter(it)))


def find_index_by(predicate: Callable, it: Iterable[Union[T, None]]):
  return next((i for i, e in enumerate(it) if predicate(e)), None)


def first(it: Iterable[Union[T, None]]) -> Union[T, None]:
  return next(iter(it), None)


def unique(it: Iterable[T]):
  return iter(set(it))


def find_duplicates(it: Iterable[T]) -> List[T]:
  return [x for x, occurrences in Counter(it).items() if occurrences > 1]


def format_list(it: Iterable, sep: str = ", ", marker="", quote="'") -> str:
  if quote == False or quote is None:
    quote = ""
  return sep.join(map(lambda x: f"{quote}{marker}{x}{quote}", it))
