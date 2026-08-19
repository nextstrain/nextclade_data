import copy

from Bio.SeqRecord import SeqRecord
import numpy as np

# Increment this version, if there are changes in the algorithm.
# Backwards compatibility must be ensured to not break client code: all versions must be computed and reffered to
# from the dataset's server 'index.json' file.
MINIMIZER_ALGO_VERSION = "1"

# Increment this version, if there are changes in the layout of the output file.
MINIMIZER_JSON_SCHEMA_VERSION = "3.0.0"

# Number of bits in the minimizer hash space. invertible_hash() masks with (1 << HASH_BITS) - 1,
# so every k-mer hash is a HASH_BITS-wide unsigned integer in [0, 2**HASH_BITS).
HASH_BITS = 32

# Length of the k-mer, in nucleotides, hashed into each minimizer candidate.
KMER_LENGTH = 17

# Default minimizer acceptance threshold: a value in [0, 2**HASH_BITS). A k-mer is kept as a minimizer
# only when its hash is below the cutoff, so the retained fraction is cutoff / 2**HASH_BITS. The default
# 1 << 28 keeps roughly 1/16 of all k-mers.
#
# cutoff is a raw threshold VALUE, not an exponent. Expected-hit math must use cutoff / 2**HASH_BITS,
# never 2**(cutoff - HASH_BITS).
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
    if i % 3 == 2:
      continue  # skip every third nucleotide to pick up conserved patterns
    if nuc not in 'ACGT':
      # Reject: return a hash above every possible cutoff (cutoff < 2**HASH_BITS), so the k-mer is
      # never kept regardless of the caller's cutoff. A fixed CUTOFF+1 sentinel would be wrong for
      # datasets built with a higher cutoff (e.g. 1 << 31), where it would fall below the threshold.
      return 1 << HASH_BITS
    else:  # A=11=3, C=01=1, G=00=0, T=10=2
      if nuc in 'AC':
        x += 1 << j
      if nuc in 'AT':
        x += 1 << (j + 1)
    j += 2

  return invertible_hash(x)


def get_ref_search_minimizers(seq: SeqRecord, k=KMER_LENGTH, cutoff=CUTOFF):
  seq_str = preprocess_seq(seq)
  minimizers = []
  # we know the rough number of minimizers, so we can pre-allocate the array if needed
  for i in range(len(seq_str) - k):
    kmer = seq_str[i:i + k]
    mhash = get_hash(kmer)
    if mhash < cutoff:  # accept only hashes below cutoff --> reduces the size of the index and the number of look-ups
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

    if not ref_list:
      raise ValueError(f"Dataset {name!r}: no reference sequences provided for the minimizer index")

    # collect minimizers from all references for this dataset
    all_minimizers = set()
    total_length = 0
    for ref in ref_list:
      minimizers = get_ref_search_minimizers(ref)
      all_minimizers.update(minimizers)
      total_length += len(ref.seq)

    # use average length for normalization
    avg_length = total_length / len(ref_list)

    # A reference no longer than the k-mer yields no k-mers and a non-positive expected-hit denominator
    # (E <= 0), which would make the score normalization divide by zero or a negative number. Reject it
    # loudly instead of emitting an index with inf/negative scores.
    if avg_length <= KMER_LENGTH:
      raise ValueError(
        f"Dataset {name!r}: average reference length {avg_length} <= k-mer length {KMER_LENGTH}; "
        f"cannot build a minimizer index"
      )

    # Expected number of minimizer hits from a SINGLE reference: the denominator the client divides the
    # query hit count by. A multi-reference dataset stores the UNION of its references' k-mers, but a
    # query only ever matches one reference's k-mers, so the denominator must be the per-reference
    # expectation, not the union size. Using the union size inflates the denominator and depresses the
    # score as references are added.
    #
    #   E = (avg_length - KMER_LENGTH) * CUTOFF / 2**HASH_BITS
    #
    # CUTOFF is a value, so the retained fraction is CUTOFF / 2**HASH_BITS. E is an approximation of the
    # realized count: it ignores non-ACGT k-mers and hash collisions removed by np.unique, so it is
    # generally non-integer and slightly above the true single-reference count.
    expected_minimizer_hits = (avg_length - KMER_LENGTH) * CUTOFF / (1 << HASH_BITS)

    minimizers_by_dataset.append({
      "minimizers": np.array(list(all_minimizers)),
      "meta": {
        "name": name,
        "length": int(avg_length),
        # nMinimizers is the integer field older clients read as the score denominator. It now holds the
        # rounded expectation, not the literal minimizer count (which still builds the index below).
        # max(1, ...) guards against a zero denominator for degenerate short references.
        "nMinimizers": max(1, round(expected_minimizer_hits)),
        # expectedMinimizerHits carries the exact fractional expectation. Newer clients prefer it over
        # the rounded nMinimizers. Additive field: older clients ignore it.
        "expectedMinimizerHits": expected_minimizer_hits,
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

  normalization = np.array([x['length'] / x['expectedMinimizerHits'] for x in index["references"]])

  return {
    "$schema": JSON_SCHEMA_URL_MINIMIZER_JSON,
    "schemaVersion": MINIMIZER_JSON_SCHEMA_VERSION,
    "version": MINIMIZER_ALGO_VERSION,
    "params": {
      "k": KMER_LENGTH,
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


def deserialize_ref_search_index(data: dict) -> dict:
  data = copy.deepcopy(data)
  data["minimizers"] = {int(k): v for k, v in data["minimizers"].items()}
  data["normalization"] = np.array(data["normalization"])
  return data


def search_one_query(
  index: dict,
  qry: SeqRecord,
) -> tuple[np.ndarray, np.ndarray]:
  refs = index["references"]
  n_refs = len(refs)
  # Select query minimizers with the index-wide cutoff (the max over datasets), matching how the client
  # computes query minimizers once for all datasets.
  cutoff = index.get("params", {}).get("cutoff", CUTOFF)
  minimizers = get_ref_search_minimizers(qry, cutoff=cutoff)
  hit_count = np.zeros(n_refs, dtype=np.int32)
  for m in minimizers:
    if m in index["minimizers"]:
      hit_count[index["minimizers"][m]] += 1

  seq_len = len(preprocess_seq(qry))
  ref_len = np.array([r["length"] for r in refs], dtype=float)
  # Denominator mirrors the client: prefer the exact fractional expectation, fall back to the rounded
  # nMinimizers for older indexes that predate expectedMinimizerHits.
  denominator = np.array(
    [r["expectedMinimizerHits"] if r.get("expectedMinimizerHits") is not None else r["nMinimizers"] for r in refs],
    dtype=float,
  )
  # Reproduce the client score exactly (packages/nextclade/src/sort/minimizer_search.rs): the length
  # factor is clamped at 1.0 so a query longer than the reference is not penalized. This is why the score
  # is computed here rather than from the pre-baked `normalization` array, which folds in the ratio
  # without the clamp.
  length_factor = np.maximum(ref_len / seq_len, 1.0)
  normalized_hits = (hit_count / denominator) * length_factor
  return normalized_hits, hit_count


def filter_matches(
  normalized_hits: np.ndarray,
  hit_count: np.ndarray,
  min_score: float,
  min_hits: int,
  max_score_gap: float,
  all_matches: bool,
) -> list[tuple[int, float, int]]:
  total_hits = int(np.sum(hit_count))
  max_score = float(np.max(normalized_hits))
  if max_score < min_score or total_hits < min_hits:
    return []

  order = np.argsort(normalized_hits)[::-1]
  matches = []
  for idx in order:
    score = float(normalized_hits[idx])
    if score < min_score:
      break
    if matches and matches[-1][1] - score > max_score_gap:
      break
    matches.append((int(idx), score, int(hit_count[idx])))
    if not all_matches:
      break
  return matches


def to_bitstring(arr) -> str:
  return "".join([str(x) for x in arr])
