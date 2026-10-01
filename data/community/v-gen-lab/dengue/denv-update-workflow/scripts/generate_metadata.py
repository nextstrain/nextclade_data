#!/usr/bin/env python3
"""Create Augur metadata and the lineage ordering used for color assignment."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from data_use import COLUMNS, load_snapshot, metadata_for


def clade_sort_key(value: str):
    key = []
    for part in re.split(r"[_.]", value):
        key.append((0, int(part)) if part.isdigit() else (1, part))
    return tuple(key)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", required=True, type=Path)
    parser.add_argument("--serotype", required=True)
    parser.add_argument("--data-use-snapshot", required=True, type=Path)
    parser.add_argument("--metadata-output", required=True, type=Path)
    parser.add_argument("--ordering-output", required=True, type=Path)
    args = parser.parse_args()

    with args.labels.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"sequence", "serotype", "lineage", "set"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"{args.labels} must contain: {', '.join(sorted(required))}")
        rows = [
            row for row in reader
            if row["serotype"] == args.serotype and row["set"] == "representatives"
        ]

    if not rows:
        raise ValueError(f"No representative labels found for {args.serotype}")

    assignments: dict[str, str] = {}
    for row in rows:
        strain, lineage = row["sequence"].strip(), row["lineage"].strip()
        if not strain or not lineage:
            raise ValueError("Representative metadata has an empty strain or lineage")
        if strain in assignments and assignments[strain] != lineage:
            raise ValueError(f"Conflicting lineage labels for representative {strain}")
        assignments[strain] = lineage

    records = load_snapshot(args.data_use_snapshot)
    metadata = [
        {"strain": strain, "lineage": lineage, "focal": "True", **metadata_for(strain, records)}
        for strain, lineage in assignments.items()
    ]
    args.metadata_output.parent.mkdir(parents=True, exist_ok=True)
    with args.metadata_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["strain", "lineage", "focal", *COLUMNS], delimiter="\t")
        writer.writeheader()
        writer.writerows(metadata)

    # assign-colors.py applies the final hierarchical sort. This declaration
    # comes entirely from the current update, without an older ordering file.
    lineages = {lineage for lineage in assignments.values() if lineage != "Unassigned"}
    with args.ordering_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        for lineage in sorted(lineages, key=clade_sort_key):
            writer.writerow(["clade_membership", lineage])


if __name__ == "__main__":
    main()
