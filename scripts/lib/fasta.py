from itertools import chain
from typing import List, Union

from Bio import SeqIO

from .container import is_iterable


def fasta_read(filepaths: Union[str, List[str]]):
  """
  Read one or more FASTA files
  """
  if isinstance(filepaths, str) or (not is_iterable(filepaths)):
    filepaths = [filepaths]
  return chain(*[SeqIO.parse(filepath, 'fasta') for filepath in filepaths])


def fasta_read_exactly_one_seq(filepath: str):
  it = fasta_read(filepath)
  first = next(it)
  try:
    next(it)
    raise ValueError("Expected only one sequence in fasta, but found multiple")
  except StopIteration:
    return first
