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


if __name__ == "__main__":
  unittest.main()
