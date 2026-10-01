#!/usr/bin/env python3
"""Compare Nextclade assignments for held-out sequences to expected labels."""
import argparse
import csv


def normalize_lineage(value):
    """Normalize Nextclade's sentinel without changing named lineage IDs."""
    return "unassigned" if value.strip().lower() == "unassigned" else value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assignments", required=True)
    parser.add_argument("--expected", required=True)
    parser.add_argument("--serotype", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    expected = {}
    with open(args.expected, newline="") as handle:
        for row in csv.DictReader(handle):
            expected[row["name"]] = row["lineage"]
    with open(args.assignments, newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    with open(args.output, "w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["sequence", "expected_lineage", "assigned_lineage", "result"])
        for row in rows:
            name = row.get("seqName", "")
            assigned = normalize_lineage(row.get("clade") or row.get("clade_membership") or "")
            wanted = normalize_lineage(expected.get(name, ""))
            result = "match" if wanted == assigned else "mismatch"
            writer.writerow([name, wanted, assigned, result])


if __name__ == "__main__":
    main()
