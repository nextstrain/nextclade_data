#!/usr/bin/env python3
"""Compare versioned TSV definitions as data, without changing either input."""

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path


COLUMNS = ("clade", "gene", "site", "alt")


def read_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != list(COLUMNS):
            raise ValueError(f"{path}: expected TSV columns {COLUMNS}, got {reader.fieldnames}")
        rows = Counter()
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"{path}:{line_number}: too many columns")
            values = tuple((row[column] or "").strip() for column in COLUMNS)
            if not any(values):
                continue
            if not all(values):
                raise ValueError(f"{path}:{line_number}: incomplete row")
            rows[values] += 1
    return rows


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compare(baseline, proposal):
    baseline_rows = read_rows(baseline)
    proposed_rows = read_rows(proposal)
    differences = []
    totals = Counter()
    for row in sorted(baseline_rows.keys() | proposed_rows.keys()):
        old = baseline_rows[row]
        new = proposed_rows[row]
        kept = min(old, new)
        added = max(new - old, 0)
        removed = max(old - new, 0)
        for status, count in (("maintained", kept), ("added", added), ("removed", removed)):
            if count:
                differences.append((*row, status, count))
                totals[status] += count
    return differences, totals, sum(baseline_rows.values()), sum(proposed_rows.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--proposal", type=Path, required=True)
    parser.add_argument("--baseline-version", required=True)
    parser.add_argument("--diff-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    args = parser.parse_args()

    differences, totals, old_count, new_count = compare(args.baseline, args.proposal)
    with args.diff_output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow((*COLUMNS, "status", "count"))
        writer.writerows(differences)
    manifest = {
        "baseline_version": args.baseline_version,
        "baseline": {"path": str(args.baseline), "sha256": sha256(args.baseline), "rows": old_count},
        "proposal": {"path": str(args.proposal), "sha256": sha256(args.proposal), "rows": new_count},
        "comparison": {status: totals[status] for status in ("maintained", "added", "removed")},
    }
    with args.manifest_output.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write("\n")


if __name__ == "__main__":
    main()
