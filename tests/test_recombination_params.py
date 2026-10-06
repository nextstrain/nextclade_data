"""Cross-implementation parity tests for the recombination parameter estimator.

The authoritative implementation is the Rust estimator in
`packages/nextclade/src/analyze/recombination_estimate.rs` of the nextclade repository. Each fixture and
expected value here is transcribed from that file's unit tests, which serve as the oracle: the Python
helper must produce bit-identical parameters so a dataset can carry frozen, reviewed values.

The estimator does deterministic integer arithmetic (small counts divided by ref_len), so the results
are exact; the tight `delta` compares them to the Rust literals essentially exactly.
"""

import json
import subprocess
import sys
import unittest
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

# The helper is an extensionless executable, so load it by explicit path rather than a normal import.
_SCRIPT_PATH = Path(__file__).resolve().parent.parent / "scripts" / "recombination_params"
_loader = SourceFileLoader("recombination_params", str(_SCRIPT_PATH))
_spec = spec_from_loader(_loader.name, _loader)
assert _spec is not None
rp = module_from_spec(_spec)
# Register before executing so `@dataclass` can resolve the `Node` forward reference (dataclasses look
# the module up in `sys.modules` to evaluate string annotations under `from __future__ import annotations`).
sys.modules[_loader.name] = rp
_loader.exec_module(rp)

# Reference length used by every Rust fixture; keeps the expected literals identical to the oracle.
REF_LEN = 100

# Tightest tolerance that passes for the exact integer/ref_len arithmetic.
DELTA = 1e-12


def _leaf(name: str, clade: str, nuc: list[str]) -> dict[str, Any]:
  return {
    "name": name,
    "node_attrs": {"clade_membership": {"value": clade}},
    "branch_attrs": {"mutations": {"nuc": nuc}},
  }


def _params(tree: dict[str, Any]) -> dict[str, float] | None:
  return rp.estimate_params(rp.build_tree(tree), REF_LEN)


class TestRecombinationParamsParity(unittest.TestCase):
  def _assert_params(self, params: dict[str, float] | None, gamma: float, mu_w: float, mu_r: float) -> None:
    assert params is not None, "expected resolved parameters, got None"
    self.assertAlmostEqual(gamma, params["gamma"], delta=DELTA)
    self.assertAlmostEqual(mu_w, params["muW"], delta=DELTA)
    self.assertAlmostEqual(mu_r, params["muR"], delta=DELTA)

  def test_recombination_params_all_params_from_two_clade_tree(self) -> None:
    # Rust `test_recombination_estimate_all_params_from_tree`: gamma 0.01, mu_w 0.02, mu_r 0.05.
    # Leaves A1 (rd 2), B1 (rd 2), B2 (rd 4); mean terminal (2+1+3)/3 = 2. Inter-clade leaf pairs
    # A1<->B1 = 4, A1<->B2 = 6; median{4, 6} = 5.
    tree = {
      "name": "root",
      "children": [
        _leaf("A1", "A", ["A10C", "A20G"]),
        {
          "name": "B",
          "node_attrs": {"clade_membership": {"value": "B"}},
          "branch_attrs": {"mutations": {"nuc": ["A30T"]}},
          "children": [
            _leaf("B1", "B", ["A40C"]),
            _leaf("B2", "B", ["A50C", "A60G", "A70T"]),
          ],
        },
      ],
    }
    self._assert_params(_params(tree), gamma=1.0 / 100.0, mu_w=2.0 / 100.0, mu_r=5.0 / 100.0)

  def test_recombination_params_three_clades_uses_nonroot_mrca(self) -> None:
    # Rust `test_recombination_estimate_three_clades_uses_nonroot_mrca`: mu_w 0.04, mu_r 0.09.
    # A1 and B1 share the non-root MRCA I, exercising the `- 2 * root_distance(mrca)` term.
    # Root distances A1=3, B1=5, C1=6; leaf pairs {6, 9, 11}, median 9. Terminals 2, 4, 6 -> mean 4.
    tree = {
      "name": "root",
      "children": [
        {
          "name": "I",
          "node_attrs": {},
          "branch_attrs": {"mutations": {"nuc": ["A5C"]}},
          "children": [
            _leaf("A1", "A", ["A10C", "A20G"]),
            _leaf("B1", "B", ["A30T", "A40C", "A50G", "A60T"]),
          ],
        },
        _leaf("C1", "C", ["A70C", "A80G", "A90T", "A100C", "A110G", "A120T"]),
      ],
    }
    self._assert_params(_params(tree), gamma=1.0 / 100.0, mu_w=4.0 / 100.0, mu_r=9.0 / 100.0)

  def test_recombination_params_nested_clades_uses_leaf_distance(self) -> None:
    # Rust `test_recombination_estimate_nested_clades_uses_leaf_distance`: mu_w 0.04, mu_r 0.09.
    # Clade ancestors sit one mutation apart, but mu_r reflects inter-clade LEAF divergence.
    # Leaf pairs sorted {6, 6, 8, 8, 10, 10, 12, 14} -> median (8+10)/2 = 9. Terminals 1,8,6,1,4 -> 4.
    tree = {
      "name": "root",
      "children": [
        {
          "name": "P",
          "node_attrs": {"clade_membership": {"value": "parent"}},
          "branch_attrs": {"mutations": {"nuc": ["A1C"]}},
          "children": [
            _leaf("P1", "parent", ["A2C"]),
            {
              "name": "C",
              "node_attrs": {"clade_membership": {"value": "child"}},
              "branch_attrs": {"mutations": {"nuc": ["A3C"]}},
              "children": [
                _leaf("C1", "child", ["A10C", "A11C", "A12C", "A13C", "A14C", "A15C", "A16C", "A17C"]),
                _leaf("C2", "child", ["A20C", "A21C", "A22C", "A23C", "A24C", "A25C"]),
              ],
            },
            _leaf("P2", "parent", ["A30C"]),
          ],
        },
        _leaf("O1", "other", ["A40C", "A41C", "A42C", "A43C"]),
      ],
    }
    self._assert_params(_params(tree), gamma=1.0 / 100.0, mu_w=4.0 / 100.0, mu_r=9.0 / 100.0)

  def test_recombination_params_excludes_deletions_from_branch_length(self) -> None:
    # Rust `test_recombination_estimate_excludes_deletions_from_branch_length`: the `A15-` deletion is
    # excluded, so B1's terminal branch is 1 (substitution A40C only); mean (2+1)/2 = 1.5 -> mu_w 0.015.
    tree = {
      "name": "root",
      "children": [
        _leaf("A1", "A", ["A10C", "A20G"]),
        _leaf("B1", "B", ["A40C", "A15-"]),
      ],
    }
    params = _params(tree)
    assert params is not None
    self.assertAlmostEqual(1.5 / 100.0, params["muW"], delta=DELTA)

  def test_recombination_params_excludes_insertions_from_branch_length(self) -> None:
    # Rust `test_recombination_estimate_excludes_insertions`: the `-10A` insertion (gap reference) is
    # an indel the decoder never observes, so it is excluded; B1's terminal branch is 1 (substitution
    # A40C only); mean (2+1)/2 = 1.5 -> mu_w 0.015.
    tree = {
      "name": "root",
      "children": [
        _leaf("A1", "A", ["A10C", "A20G"]),
        _leaf("B1", "B", ["A40C", "-10A"]),
      ],
    }
    params = _params(tree)
    assert params is not None
    self.assertAlmostEqual(1.5 / 100.0, params["muW"], delta=DELTA)

  def test_recombination_params_single_clade_is_unresolved(self) -> None:
    # Rust `test_recombination_estimate_single_clade_is_unresolved`: mu_r undefined with one clade.
    tree = {
      "name": "root",
      "children": [
        _leaf("L1", "A", ["A10C"]),
        _leaf("L2", "A", ["A20G"]),
      ],
    }
    self.assertIsNone(_params(tree))

  def test_recombination_params_internal_only_clade_is_unresolved(self) -> None:
    # Rust `test_recombination_estimate_internal_only_clade_is_fewer_than_two_clades`: internal node I
    # is labeled clade "B" but no leaf is, so only one LEAF clade ("A") exists and mu_r is undefined.
    tree = {
      "name": "root",
      "children": [
        {
          "name": "I",
          "node_attrs": {"clade_membership": {"value": "B"}},
          "branch_attrs": {"mutations": {"nuc": ["A5C"]}},
          "children": [
            _leaf("A1", "A", ["A10C"]),
            _leaf("A2", "A", ["A20G"]),
          ],
        },
      ],
    }
    self.assertIsNone(_params(tree))

  def test_recombination_params_no_branch_mutations_is_unresolved(self) -> None:
    # Rust `test_recombination_estimate_no_branch_mutations_skip_reason`: two clades but no `nuc`
    # branch mutations, so every rate is zero and the model is left unresolved.
    tree = {
      "name": "root",
      "children": [
        {"name": "A1", "node_attrs": {"clade_membership": {"value": "A"}}},
        {"name": "B1", "node_attrs": {"clade_membership": {"value": "B"}}},
      ],
    }
    self.assertIsNone(_params(tree))

  def test_recombination_params_errors_on_malformed_branch_mutation(self) -> None:
    # Rust `test_recombination_estimate_errors_on_malformed_branch_mutation`: a malformed annotation
    # surfaces as an error instead of being silently miscounted.
    tree = {
      "name": "root",
      "children": [
        _leaf("A1", "A", ["not-a-mutation"]),
        _leaf("B1", "B", ["A40C"]),
      ],
    }
    with self.assertRaises(ValueError) as ctx:
      _params(tree)
    self.assertEqual("Unable to parse nucleotide mutation: 'not-a-mutation'", str(ctx.exception))


class TestCountBranchSubstitutions(unittest.TestCase):
  def test_count_branch_substitutions_counts_substitutions(self) -> None:
    self.assertEqual(2, rp.count_branch_substitutions(["A10C", "A20G"]))

  def test_count_branch_substitutions_empty_is_zero(self) -> None:
    self.assertEqual(0, rp.count_branch_substitutions([]))

  def test_count_branch_substitutions_excludes_deletion(self) -> None:
    # `A15-` has a gap query base (deletion) and is not counted; `A40C` is.
    self.assertEqual(1, rp.count_branch_substitutions(["A40C", "A15-"]))

  def test_count_branch_substitutions_excludes_insertion(self) -> None:
    # `-10A` has a gap reference base (insertion) and is not counted; only the substitution `A40C` is.
    self.assertEqual(1, rp.count_branch_substitutions(["A40C", "-10A"]))

  def test_count_branch_substitutions_counts_ambiguous_iupac(self) -> None:
    # `N` and `R` are valid IUPAC nucleotide codes accepted by the Rust `to_nuc`.
    self.assertEqual(1, rp.count_branch_substitutions(["N5R"]))

  def test_count_branch_substitutions_raises_on_unparseable(self) -> None:
    with self.assertRaises(ValueError):
      rp.count_branch_substitutions(["not-a-mutation"])

  def test_count_branch_substitutions_raises_on_invalid_nucleotide(self) -> None:
    # `Z` matches the position regex `[A-Z-]` but is not a nucleotide, so `to_nuc` (mirrored by the
    # VALID_NUCS check) rejects it.
    with self.assertRaises(ValueError):
      rp.count_branch_substitutions(["A10Z"])


# The two-clade oracle tree (gamma 0.01, mu_w 0.02, mu_r 0.05 at ref_len 100) as an Auspice file body.
_TWO_CLADE_AUSPICE = {
  "version": "v2",
  "meta": {},
  "tree": {
    "name": "root",
    "children": [
      _leaf("A1", "A", ["A10C", "A20G"]),
      {
        "name": "B",
        "node_attrs": {"clade_membership": {"value": "B"}},
        "branch_attrs": {"mutations": {"nuc": ["A30T"]}},
        "children": [
          _leaf("B1", "B", ["A40C"]),
          _leaf("B2", "B", ["A50C", "A60G", "A70T"]),
        ],
      },
    ],
  },
}


class TestRecombinationParamsCli(unittest.TestCase):
  """End-to-end CLI smoke tests over the full argument-parsing and I/O path."""

  def _write_inputs(self, tmp: Path) -> tuple[Path, Path]:
    tree = tmp / "tree.json"
    tree.write_text(json.dumps(_TWO_CLADE_AUSPICE))
    ref = tmp / "reference.fasta"
    ref.write_text(">ref\n" + "A" * REF_LEN + "\n")
    return tree, ref

  def _run(self, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
      [sys.executable, str(_SCRIPT_PATH), *args],
      capture_output=True,
      text=True,
      check=True,
    )

  def test_recombination_params_cli_prints_json_when_no_pathogen(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      tree, ref = self._write_inputs(Path(tmp_dir))
      result = self._run("--input-tree", str(tree), "--input-ref", str(ref))
      params = json.loads(result.stdout)
      self.assertAlmostEqual(1.0 / 100.0, params["gamma"], delta=DELTA)
      self.assertAlmostEqual(2.0 / 100.0, params["muW"], delta=DELTA)
      self.assertAlmostEqual(5.0 / 100.0, params["muR"], delta=DELTA)

  def test_recombination_params_cli_writes_pathogen_in_place(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      tmp = Path(tmp_dir)
      tree, ref = self._write_inputs(tmp)
      pathogen = tmp / "pathogen.json"
      pathogen.write_text(json.dumps({"schemaVersion": "3.0.0"}))
      self._run("--input-tree", str(tree), "--input-ref", str(ref), "--pathogen", str(pathogen))
      written = json.loads(pathogen.read_text())["recombination"]
      self.assertEqual(True, written["enabled"])
      self.assertAlmostEqual(5.0 / 100.0, written["muR"], delta=DELTA)


if __name__ == "__main__":
  unittest.main()
