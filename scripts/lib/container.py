from collections import namedtuple, Counter
from functools import reduce
from typing import List, Iterable, TypeVar, Callable, Union, Dict, Any, Hashable, Optional, Sequence

T = TypeVar('T')


def is_iterable(obj):
  return issubclass(type(obj), Iterable)


def type_check(value, expected_type):
  if not isinstance(value, expected_type):
    raise TypeError(f"Expected type {expected_type.__name__}, but received type {type(value).__name__}")

def dict_to_namedtuple(name: str, dic: dict):
  type_check(name, str)
  type_check(dic, dict)
  return namedtuple(name, dic.keys())(*dic.values())

def dict_set(obj: dict, key_path: List[str], value):
  type_check(obj, dict)
  type_check(key_path, list)
  for key in key_path:
    type_check(key, str)
  for key in key_path[:-1]:
    obj = obj.setdefault(key, {})
  obj[key_path[-1]] = value

def dict_get(obj: dict, keys: List[str]):
  type_check(obj, dict)
  type_check(keys, list)
  for key in keys:
    type_check(key, str)
  return reduce(lambda d, key: d.get(key) if d else None, keys, obj)

def dict_get_required(obj: dict, keys: List[str]):
  type_check(obj, dict)
  type_check(keys, list)
  val = dict_get(obj, keys)
  if val is None:
    raise KeyError(f"Key not found: '{'.'.join(keys)}'")
  return val

def dict_remove(obj: dict, key: str):
  type_check(obj, dict)
  type_check(key, str)
  if obj.get(key) is not None:
    obj.pop(key)

def dict_remove_many(obj: dict, keys: List[str]):
  type_check(obj, dict)
  type_check(keys, list)
  for key in keys:
    dict_remove(obj, key)

def dict_rename_one_unordered_inplace(d: Dict[str, Any], old_key: str, new_key: str):
  type_check(d, dict)
  type_check(old_key, str)
  type_check(new_key, str)
  if old_key == new_key:
    return
  if old_key in d:
    value = d.pop(old_key)
    if value is not None:
      d[new_key] = value

def dict_rename_many(d: Dict[str, Any], replacements: Dict[str, str]):
  type_check(d, dict)
  type_check(replacements, dict)
  return {replacements.get(k, k): v for k, v in d.items()}

def list_cleanup(data: List):
  type_check(data, list)
  new_data = []
  for v in data:
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data.append(v)
  return new_data

def dict_cleanup(data: dict):
  type_check(data, dict)
  new_data = {}
  for k, v in data.items():
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data[k] = v
  return new_data

def find(predicate: Callable, it: Iterable[Union[T, None]]):
  type_check(predicate, Callable)
  type_check(it, Iterable)
  return first(filter(predicate, iter(it)))

def find_index_by(predicate: Callable, it: Iterable[Union[T, None]]):
  type_check(predicate, Callable)
  type_check(it, Iterable)
  return next((i for i, e in enumerate(it) if predicate(e)), None)

def first(it: Iterable[Union[T, None]]):
  type_check(it, Iterable)
  return next(iter(it), None)

def unique(it: Iterable[T]):
  type_check(it, Iterable)
  return iter(set(it))

def unique_by(values: Sequence[T], key: Optional[Callable[[T], Hashable]] = None):
  type_check(values, Sequence)
  if key is not None:
    type_check(key, Callable)
  return list(
    dict.fromkeys(values)
    if key is None
    else dict((key(value), value) for value in reversed(values)).values()
  )

def find_duplicates(it: Iterable[T]):
  type_check(it, Iterable)
  return [x for x, occurrences in Counter(it).items() if occurrences > 1]

def format_list(it: Iterable, sep: str = ", ", marker="", quote="'"):
  type_check(it, Iterable)
  type_check(sep, str)
  type_check(marker, str)
  type_check(quote, (str, type(None)))
  if quote == False or quote is None:
    quote = ""
  return sep.join(map(lambda x: f"{quote}{marker}{x}{quote}", it))

def true_or_none(x: Union[bool, None]):
  type_check(x, (bool, type(None)))
  return True if x == True else None
