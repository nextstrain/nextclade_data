#!/usr/bin/env python3
"""Set Nextclade placement masks from GFF3 coding bounds and reference length."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from crop_coding_region import coding_bounds


def reference_length(path: Path) -> int:
    names = 0
    length = 0
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith(">"):
                names += 1
            elif line.strip():
                if names != 1:
                    raise ValueError(f"Expected one FASTA record in {path}")
                length += len(line.strip())
    if names != 1 or length == 0:
        raise ValueError(f"Expected one nonempty FASTA record in {path}")
    return length


def placement_mask_ranges(gff: Path, reference: Path) -> list[dict[str, int]]:
    first_coding_base, last_coding_base = coding_bounds(gff)
    length = reference_length(reference)
    if not 1 <= first_coding_base <= last_coding_base <= length:
        raise ValueError(
            f"Coding bounds [{first_coding_base}, {last_coding_base}] "
            f"are outside the {length}-nt reference"
        )
    ranges = []
    if first_coding_base > 1:
        ranges.append({"begin": 0, "end": first_coding_base - 1})
    if last_coding_base < length:
        ranges.append({"begin": last_coding_base, "end": length})
    return ranges


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gff", required=True, type=Path)
    parser.add_argument("--reference", required=True, type=Path)
    parser.add_argument("--target-tree", required=True, type=Path)
    args = parser.parse_args()

    with args.target_tree.open(encoding="utf-8") as handle:
        tree = json.load(handle)
    tree.setdefault("meta", {}).setdefault("extensions", {}).setdefault("nextclade", {})[
        "placement_mask_ranges"
    ] = placement_mask_ranges(args.gff, args.reference)
    args.target_tree.write_text(
        json.dumps(tree, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
