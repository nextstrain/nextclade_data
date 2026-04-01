from collections import namedtuple, Counter
from dataclasses import dataclass
from typing import List, Iterable, TypeVar, Callable, Union, Dict, Any, Hashable, Optional, Sequence, Iterator

T = TypeVar('T')


@dataclass(frozen=True)
class JsonPath:
  """Path-tracking wrapper for JSON traversal with automatic error context."""
  data: Any
  path: str = ""

  def get(self, key: str) -> "JsonPath":
    new_path = f"{self.path}.{key}" if self.path else key
    if self.data is None:
      return JsonPath(None, new_path)
    if not isinstance(self.data, dict):
      raise TypeError(f"expected dict at '{self.path or '(root)'}' while accessing '{key}', got {type(self.data).__name__}")
    return JsonPath(self.data.get(key), new_path)

  def items(self) -> Iterator[tuple[str, "JsonPath"]]:
    if self.data is None:
      return
    if not isinstance(self.data, dict):
      raise TypeError(f"expected dict at '{self.path or '(root)'}', got {type(self.data).__name__}")
    for k, v in self.data.items():
      yield k, JsonPath(v, f"{self.path}.{k}" if self.path else k)

  def __iter__(self) -> Iterator["JsonPath"]:
    if self.data is None:
      return
    if not isinstance(self.data, list):
      raise TypeError(f"expected list at '{self.path or '(root)'}', got {type(self.data).__name__}")
    for i, v in enumerate(self.data):
      yield JsonPath(v, f"{self.path}[{i}]")

  def __bool__(self) -> bool:
    return self.data is not None and bool(self.data)

  @property
  def val(self) -> Any:
    return self.data

  def or_default(self, default: T) -> T:
    return self.data if self.data is not None else default


def is_iterable(obj):
  return issubclass(type(obj), Iterable)


def dict_to_namedtuple(name: str, dic: dict):
  return namedtuple(name, dic.keys())(*dic.values())


def dict_set(obj: dict, key_path: List[str], value):
  for i, key in enumerate(key_path[:-1]):
    _assert_dict(obj, key_path, i)
    obj = obj.setdefault(key, {})
  _assert_dict(obj, key_path, len(key_path) - 1)
  obj[key_path[-1]] = value


def dict_get(obj: dict, keys: List[str]):
  current = obj
  for i, key in enumerate(keys):
    if current is None:
      return None
    _assert_dict(current, keys, i)
    current = current.get(key)
  return current


def _assert_dict(obj: Any, keys: List[str], index: int):
  if isinstance(obj, dict):
    return
  try:
    traversed = '.'.join(str(k) for k in keys[:index]) if index > 0 else None
    remaining = '.'.join(str(k) for k in keys[index:]) or '?'
    location = f"after '{traversed}'" if traversed else "at root"
    type_name = type(obj).__name__
  except Exception:
    location, remaining, type_name = "at unknown", "?", "?"
  raise TypeError(f"expected dict {location} while accessing '{remaining}', got {type_name}")


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


def dict_rename_one_unordered_inplace(d: Dict[str, Any], old_key: str, new_key: str):
  """
  Rename one key. Do not preserve key order.
  """
  if old_key == new_key:
    return

  if old_key in d:
    value = d.pop(old_key)
    if value is not None:
      d[new_key] = value


def dict_rename_many(d: Dict[str, Any], replacements: Dict[str, str]):
  """
  Rename keys given a mapping dict. Slow for large dicts.
  """
  return {replacements.get(k, k): v for k, v in d.items()}


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


# https://stackoverflow.com/a/49168973
def unique_by(values: Sequence[T], key: Optional[Callable[[T], Hashable]] = None) -> List[T]:
  return list(
    dict.fromkeys(values)
    if key is None
    else dict((key(value), value) for value in reversed(values)).values()
  )


def find_duplicates(it: Iterable[T]) -> List[T]:
  return [x for x, occurrences in Counter(it).items() if occurrences > 1]


def format_list(it: Iterable, sep: str = ", ", marker="", quote="'") -> str:
  if not quote:
    quote = ""
  return sep.join(map(lambda x: f"{quote}{marker}{x}{quote}", it))


def true_or_none(x: bool | None) -> bool | None:
  return True if x else None
