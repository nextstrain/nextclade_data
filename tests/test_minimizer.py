import random
import unittest

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from scripts.lib.minimizer import (
  CUTOFF,
  HASH_BITS,
  KMER_LENGTH,
  deserialize_ref_search_index,
  get_hash,
  get_ref_search_minimizers,
  make_ref_search_index,
  search_one_query,
  serialize_ref_search_index,
)


def make_ref(length: int) -> SeqRecord:
  return SeqRecord(Seq(("ACGT" * (length // 4 + 1))[:length]))


def random_ref(length: int, seed: int) -> SeqRecord:
  rng = random.Random(seed)
  return SeqRecord(Seq("".join(rng.choice("ACGT") for _ in range(length))))


def expected_hits(length: int, cutoff: int) -> float:
  return (length - KMER_LENGTH) * cutoff / (1 << HASH_BITS)


def built_index(refs) -> dict:
  return deserialize_ref_search_index(serialize_ref_search_index(make_ref_search_index(refs)))


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

  def test_minimizer_multi_reference_stores_union_of_reference_minimizers(self) -> None:
    ref_a, ref_b = random_ref(7000, seed=1), random_ref(7000, seed=2)
    set_a = set(int(m) for m in get_ref_search_minimizers(ref_a))
    set_b = set(int(m) for m in get_ref_search_minimizers(ref_b))
    index = built_index({"beta": [ref_a, ref_b]})

    self.assertEqual(set_a | set_b, set(index["minimizers"].keys()))

  def test_minimizer_score_not_depressed_when_reference_added(self) -> None:
    ref_a, ref_b = random_ref(7000, seed=1), random_ref(7000, seed=2)
    query = SeqRecord(ref_a.seq)

    single = built_index({"ds": ref_a})
    multi = built_index({"ds": [ref_a, ref_b]})

    score_single = float(search_one_query(single, query)[0][0])
    score_multi = float(search_one_query(multi, query)[0][0])

    self.assertGreater(score_single, 0.5)
    self.assertAlmostEqual(score_single, score_multi, places=9)

  def test_minimizer_search_length_clamp_matches_client(self) -> None:
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
    self.assertGreaterEqual(sentinel, 1 << 31)


if __name__ == "__main__":
  unittest.main()
