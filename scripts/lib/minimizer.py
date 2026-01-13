import copy

from Bio.SeqRecord import SeqRecord
import numpy as np

# Increment this version, if there are changes in the algorithm.
# Backwards compatibility must be ensured to not break client code: all versions must be computed and reffered to
# from the dataset's server 'index.json' file.
MINIMIZER_ALGO_VERSION = "1"

# Increment this version, if there are changes in the layout of the output file.
MINIMIZER_JSON_SCHEMA_VERSION = "3.0.0"

# What is this?
MAGIC_NUMBER_K = 17

# minimizer cutoff. The max is 1<<32 - 1, so with 28 uses roughly 1/16 of all kmers
CUTOFF = 1 << 28

JSON_SCHEMA_URL_MINIMIZER_JSON=  "https://raw.githubusercontent.com/nextstrain/nextclade/refs/heads/release/packages/nextclade-schemas/internal-minimizer-index-json.schema.json"


# from lh3
def invertible_hash(x):
  m = (1 << 32) - 1
  x = (~x + (x << 21)) & m
  x = x ^ (x >> 24)
  x = (x + (x << 3) + (x << 8)) & m
  x = x ^ (x >> 14)
  x = (x + (x << 2) + (x << 4)) & m
  x = x ^ (x >> 28)
  x = (x + (x << 31)) & m
  return x


# turn a kmer into an integer
def get_hash(kmer):
  x = 0
  j = 0
  for i, nuc in enumerate(kmer):
    if i % 3 == 2: continue  # skip every third nucleotide to pick up conserved patterns
    if nuc not in 'ACGT':
      return CUTOFF + 1  # break out of loop, return hash above cutoff
    else:  # A=11=3, C=10=2, G=00=0, T=01=1
      if nuc in 'AC':
        x += 1 << j
      if nuc in 'AT':
        x += 1 << (j + 1)
    j += 2

  return invertible_hash(x)


def get_ref_search_minimizers(seq: SeqRecord, k=MAGIC_NUMBER_K):
  seq_str = preprocess_seq(seq)
  minimizers = []
  # we know the rough number of minimizers, so we can pre-allocate the array if needed
  for i in range(len(seq_str) - k):
    kmer = seq_str[i:i + k]
    mhash = get_hash(kmer)
    if mhash < CUTOFF:  # accept only hashes below cutoff --> reduces the size of the index and the number of look-ups
      minimizers.append(mhash)
  return np.unique(minimizers)


def make_ref_search_index(refs):
  """
  Build minimizer search index from reference sequences.

  Args:
    refs: dict mapping dataset name to either:
      - a single SeqRecord (backward compatible)
      - a list of SeqRecords (multiple references per dataset)

  Returns:
    Minimizer index dict ready for JSON serialization.
  """
  # collect minimizers for each dataset (possibly from multiple references)
  minimizers_by_dataset = list()
  for name, ref_or_refs in sorted(refs.items()):
    # normalize to list for uniform handling
    ref_list = ref_or_refs if isinstance(ref_or_refs, list) else [ref_or_refs]

    # collect minimizers from all references for this dataset
    all_minimizers = set()
    total_length = 0
    for ref in ref_list:
      minimizers = get_ref_search_minimizers(ref)
      all_minimizers.update(minimizers)
      total_length += len(ref.seq)

    # use average length for normalization
    avg_length = total_length / len(ref_list)

    minimizers_by_dataset.append({
      "minimizers": np.array(list(all_minimizers)),
      "meta": {
        "name": name,
        "length": int(avg_length),
        "nMinimizers": len(all_minimizers)
      }
    })

  # construct an index where each minimizer maps to the datasets it belongs to
  index = {"minimizers": {}, "references": []}
  for ri, minimizer_set in enumerate(minimizers_by_dataset):
    for m in minimizer_set["minimizers"]:
      if m not in index["minimizers"]:
        index["minimizers"][m] = []
      index["minimizers"][m].append(ri)

    # reference will be a list in same order as the bit set
    index["references"].append(minimizer_set['meta'])

  normalization = np.array([x['length'] / x['nMinimizers'] for x in index["references"]])

  return {
    "$schema": JSON_SCHEMA_URL_MINIMIZER_JSON,
    "schemaVersion": MINIMIZER_JSON_SCHEMA_VERSION,
    "version": MINIMIZER_ALGO_VERSION,
    "params": {
      "k": MAGIC_NUMBER_K,
      "cutoff": CUTOFF,
    },
    **index,
    "normalization": normalization
  }


def preprocess_seq(seq: SeqRecord) -> str:
  return str(seq.seq).upper().replace('-', '')


def serialize_ref_search_index(index):
  index = copy.deepcopy(index)
  index["minimizers"] = {str(k): v for k, v in index["minimizers"].items()}
  index["normalization"] = index["normalization"].tolist()
  return index


def to_bitstring(arr) -> str:
  return "".join([str(x) for x in arr])
