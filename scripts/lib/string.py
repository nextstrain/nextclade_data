from typing import List


def surround(strs: List[str], symbol: str):
  return list(f"{symbol}{s}{symbol}" for s in strs)


def quote(strs: List[str]):
  return surround(strs, "'")



def removesuffix(s, suffix):
  if s.endswith(suffix):
    return s[:-len(suffix)]
  else:
    return s
