import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.lib.reporting import PROJECT_ROOT

REBUILD = PROJECT_ROOT / "scripts" / "rebuild"

COLLECTION_JSON = {
  "meta": {
    "id": "test",
    "title": "Test",
    "description": "Collection without datasets",
    "color": "#868f89",
    "urls": [],
  },
  "dataset_order": [],
}


def run_rebuild(input_dir: Path, output_dir: Path) -> subprocess.CompletedProcess[str]:
  return subprocess.run(
    [
      sys.executable,
      str(REBUILD),
      "--input-dir",
      str(input_dir),
      "--output-dir",
      str(output_dir),
      "--no-pull",
      "--allow-dirty",
    ],
    cwd=PROJECT_ROOT,
    capture_output=True,
    text=True,
    check=False,
  )


class TestRebuild(unittest.TestCase):
  def test_rebuild_writes_index_into_new_output_dir(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      input_dir = Path(tmp_dir) / "input"
      output_dir = Path(tmp_dir) / "output"
      (input_dir / "test").mkdir(parents=True)
      (input_dir / "test" / "collection.json").write_text(json.dumps(COLLECTION_JSON))

      result = run_rebuild(input_dir, output_dir)

      self.assertEqual(result.returncode, 0, result.stderr)
      index = json.loads((output_dir / "index.json").read_text())
      self.assertEqual([c["meta"]["id"] for c in index["collections"]], ["test"])

  def test_rebuild_fails_when_input_dir_has_no_collection(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      input_dir = Path(tmp_dir) / "input"
      output_dir = Path(tmp_dir) / "output"
      input_dir.mkdir()

      result = run_rebuild(input_dir, output_dir)

      self.assertNotEqual(result.returncode, 0)
      self.assertIn("collection.json", result.stderr)
      self.assertFalse((output_dir / "index.json").exists())

  def test_rebuild_removes_dataset_order_entries_of_missing_datasets(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      input_dir = Path(tmp_dir) / "input"
      output_dir = Path(tmp_dir) / "output"
      write_collection(input_dir, dataset_order=["test/renamed/old-path"])

      result = run_rebuild(input_dir, output_dir)

      self.assertEqual(result.returncode, 0, result.stderr)
      # The collection has no datasets, so its order lists none
      expected_order: list[str] = []
      self.assertEqual(expected_order, read_collection(input_dir)["dataset_order"])

  def test_rebuild_removes_unreleased_output_of_missing_dataset(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      input_dir = Path(tmp_dir) / "input"
      output_dir = Path(tmp_dir) / "output"
      write_collection(input_dir, dataset_order=[])
      write_file(output_dir / "test" / "renamed" / "old-path" / "unreleased" / "pathogen.json")

      result = run_rebuild(input_dir, output_dir)

      self.assertEqual(result.returncode, 0, result.stderr)
      self.assertTrue((output_dir / "test").is_dir())
      self.assertFalse((output_dir / "test" / "renamed").exists())

  def test_rebuild_keeps_released_versions_of_missing_dataset(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      input_dir = Path(tmp_dir) / "input"
      output_dir = Path(tmp_dir) / "output"
      write_collection(input_dir, dataset_order=[])
      released = output_dir / "test" / "removed" / "2024-01-01--00-00-00Z" / "pathogen.json"
      write_file(released)

      result = run_rebuild(input_dir, output_dir)

      self.assertEqual(result.returncode, 0, result.stderr)
      self.assertTrue(released.is_file())

  def test_rebuild_keeps_unreleased_output_of_collection_outside_input(self) -> None:
    with TemporaryDirectory() as tmp_dir:
      input_dir = Path(tmp_dir) / "input"
      output_dir = Path(tmp_dir) / "output"
      write_collection(input_dir, dataset_order=[])
      other = output_dir / "other" / "dataset" / "unreleased" / "pathogen.json"
      write_file(other)

      result = run_rebuild(input_dir, output_dir)

      self.assertEqual(result.returncode, 0, result.stderr)
      self.assertTrue(other.is_file())


def write_collection(input_dir: Path, dataset_order: list[str]) -> None:
  (input_dir / "test").mkdir(parents=True)
  (input_dir / "test" / "collection.json").write_text(json.dumps({**COLLECTION_JSON, "dataset_order": dataset_order}))


def read_collection(input_dir: Path) -> dict:
  return json.loads((input_dir / "test" / "collection.json").read_text())


def write_file(path: Path) -> None:
  path.parent.mkdir(parents=True)
  path.write_text("{}")


if __name__ == "__main__":
  unittest.main()
