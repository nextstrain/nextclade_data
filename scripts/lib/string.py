from typing import List


def surround(strs: List[str], symbol: str):
  return list(f"{symbol}{s}{symbol}" for s in strs)


def quote(strs: List[str]):
  return surround(strs, "'")
