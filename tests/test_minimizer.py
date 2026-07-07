import random
import unittest

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from scripts.lib.minimizer import (
  CUTOFF,
  HASH_BITS,
  KMER_LENGTH,
  cutoff_from_exponent,
  deserialize_ref_search_index,
  get_hash,
  get_ref_search_minimizers,
  make_ref_search_index,
  search_one_query,
  serialize_ref_search_index,
)


def make_ref(length: int) -> SeqRecord:
  # Expected-hit math depends only on length and cutoff, not on content, so a repeated valid ACGT
  # sequence of the requested length is sufficient for denominator tests.
  return SeqRecord(Seq(("ACGT" * (length // 4 + 1))[:length]))


def random_ref(length: int, seed: int) -> SeqRecord:
  # Distinct pseudo-random sequences have (essentially) disjoint minimizer sets, needed for the
  # multi-reference union and scoring-invariant tests.
  rng = random.Random(seed)
  return SeqRecord(Seq("".join(rng.choice("ACGT") for _ in range(length))))


def expected_hits(length: int, cutoff: int) -> float:
  # Oracle: the implementation contract is the realized k-mer count `length - KMER_LENGTH` (the loop
  # iterates range(len - k)), not the spec's `length - k + 1`. Kept explicit so a change to either the
  # loop or the formula breaks this test.
  return (length - KMER_LENGTH) * cutoff / (1 << HASH_BITS)


def built_index(refs, cutoffs=None) -> dict:
  # Round-trip through (de)serialization to mimic the real load path (integer minimizer keys).
  return deserialize_ref_search_index(serialize_ref_search_index(make_ref_search_index(refs, cutoffs)))


class TestMakeRefSearchIndex(unittest.TestCase):
  def test_minimizer_single_reference_denominator_is_expected_hits(self) -> None:
    index = make_ref_search_index({"alpha": make_ref(7000)})
    ref = index["references"][0]

    self.assertEqual(7000, ref["length"])
    self.assertEqual(expected_hits(7000, CUTOFF), ref["expectedMinimizerHits"])
    self.assertEqual(436.4375, ref["expectedMinimizerHits"])  # 6983/16, hand-computed
    self.assertEqual(round(436.4375), ref["nMinimizers"])  # 436
    self.assertEqual(CUTOFF, index["params"]["cutoff"])

  def test_minimizer_multi_reference_uses_average_length(self) -> None:
    index = make_ref_search_index({"beta": [make_ref(6000), make_ref(8000)]})
    ref = index["references"][0]

    self.assertEqual(7000, ref["length"])  # int(avg(6000, 8000))
    self.assertEqual(expected_hits(7000, CUTOFF), ref["expectedMinimizerHits"])

  def test_minimizer_per_dataset_cutoff_drives_e_and_index_cutoff_is_max(self) -> None:
    index = make_ref_search_index(
      {"alpha": make_ref(7000), "beta": make_ref(7000)},
      cutoffs={"beta": 1 << 31},
    )
    refs = {r["name"]: r for r in index["references"]}

    self.assertEqual(expected_hits(7000, CUTOFF), refs["alpha"]["expectedMinimizerHits"])
    self.assertEqual(expected_hits(7000, 1 << 31), refs["beta"]["expectedMinimizerHits"])  # 3491.5
    self.assertEqual(round(3491.5), refs["beta"]["nMinimizers"])  # 3492
    # query minimizers are selected once, so the index cutoff must reach the widest dataset
    self.assertEqual(1 << 31, index["params"]["cutoff"])

  def test_minimizer_multi_reference_stores_union_of_reference_minimizers(self) -> None:
    ref_a, ref_b = random_ref(7000, seed=1), random_ref(7000, seed=2)
    set_a = set(int(m) for m in get_ref_search_minimizers(ref_a))
    set_b = set(int(m) for m in get_ref_search_minimizers(ref_b))
    index = built_index({"beta": [ref_a, ref_b]})

    self.assertEqual(set_a | set_b, set(index["minimizers"].keys()))

  def test_minimizer_score_not_depressed_when_reference_added(self) -> None:
    # The branch's namesake invariant: a query matching one reference must not lose score just because
    # a second (disjoint) reference is merged into the same dataset. Under the old union-size denominator
    # the multi-reference score would roughly halve.
    ref_a, ref_b = random_ref(7000, seed=1), random_ref(7000, seed=2)
    query = SeqRecord(ref_a.seq)

    single = built_index({"ds": ref_a})
    multi = built_index({"ds": [ref_a, ref_b]})

    score_single = float(search_one_query(single, query)[0][0])
    score_multi = float(search_one_query(multi, query)[0][0])

    self.assertGreater(score_single, 0.5)
    self.assertAlmostEqual(score_single, score_multi, places=9)

  def test_minimizer_search_length_clamp_matches_client(self) -> None:
    # A query longer than the reference is not penalized: the length factor clamps at 1.0 (mirrors
    # minimizer_search.rs). A 2x-length query keeps the same score, not half.
    ref_a = random_ref(7000, seed=1)
    index = built_index({"ds": ref_a})

    score_equal = float(search_one_query(index, SeqRecord(ref_a.seq))[0][0])
    longer = SeqRecord(ref_a.seq + random_ref(7000, seed=9).seq)
    score_longer = float(search_one_query(index, longer)[0][0])

    self.assertAlmostEqual(score_equal, score_longer, places=9)

  def test_minimizer_degenerate_reference_raises(self) -> None:
    with self.assertRaises(ValueError):
      make_ref_search_index({"short": make_ref(KMER_LENGTH)})  # avg_length == k -> E <= 0
    with self.assertRaises(ValueError):
      make_ref_search_index({"empty": []})


class TestGetHash(unittest.TestCase):
  def test_minimizer_get_hash_rejects_non_acgt_above_any_cutoff(self) -> None:
    kmer = "N" + "A" * (KMER_LENGTH - 1)  # non-ACGT at position 0 (not a skipped codon position)
    sentinel = get_hash(kmer)

    self.assertEqual(1 << HASH_BITS, sentinel)
    self.assertGreaterEqual(sentinel, 1 << 31)  # dominates the widest supported cutoff

  def test_minimizer_higher_cutoff_stores_superset(self) -> None:
    ref = random_ref(7000, seed=5)
    low = set(int(m) for m in get_ref_search_minimizers(ref, cutoff=1 << 28))
    high = set(int(m) for m in get_ref_search_minimizers(ref, cutoff=1 << 31))

    self.assertTrue(low.issubset(high))
    self.assertGreater(len(high), len(low))


class TestCutoffFromExponent(unittest.TestCase):
  def test_minimizer_cutoff_exponent_resolution(self) -> None:
    self.assertEqual(CUTOFF, cutoff_from_exponent(None))
    self.assertEqual(1 << 28, cutoff_from_exponent(28))
    self.assertEqual(1 << 31, cutoff_from_exponent(31))

  def test_minimizer_cutoff_exponent_rejects_invalid(self) -> None:
    for bad in (0, HASH_BITS + 1, -1, 1 << 31, True, 3.0):
      with self.assertRaises(ValueError):
        cutoff_from_exponent(bad)


if __name__ == "__main__":
  unittest.main()
