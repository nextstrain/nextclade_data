#!/usr/bin/env python3
"""Add Augur clade-inheritance rows using lineage annotations in a NEXUS tree."""
import argparse
import csv
import re
from pathlib import Path

from Bio import Phylo


LINEAGE = re.compile(r'lineage="([^"]+)"')


def lineage_of(clade):
    match = LINEAGE.search(clade.comment or "")
    return match.group(1) if match else None


def descendants(clade):
    return len(clade.get_terminals())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--definitions", required=True, type=Path)
    parser.add_argument("--nexus", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    with args.definitions.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    defined = {row["clade"] for row in rows if row.get("clade")}

    tree = Phylo.read(args.nexus, "nexus")
    parents = {}
    nodes_by_lineage = {}

    def visit(node, parent=None):
        parents[id(node)] = parent
        label = lineage_of(node)
        if label and label != "Unassigned":
            nodes_by_lineage.setdefault(label, []).append(node)
        for child in node.clades:
            visit(child, node)

    visit(tree.root)
    inheritance = {}
    report = []
    for child in sorted(defined):
        candidates = nodes_by_lineage.get(child, [])
        if not candidates:
            report.append([child, "skipped", "", "no annotated NEXUS node"])
            continue
        # The basal occurrence has the largest descendant set when an
        # annotation appears on both a lineage root and its descendants.
        node = max(candidates, key=descendants)
        parent = parents[id(node)]
        while parent is not None:
            ancestor = lineage_of(parent)
            if ancestor and ancestor not in {child, "Unassigned"}:
                if ancestor in defined:
                    inheritance[child] = ancestor
                    report.append([child, "inherited", ancestor, ""])
                else:
                    report.append([child, "skipped", ancestor, "parent has no direct definition"])
                break
            parent = parents[id(parent)]
        else:
            report.append([child, "skipped", "", "no named ancestral lineage"])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["clade", "gene", "site", "alt"])
        for row in rows:
            writer.writerow([row.get("clade", ""), row.get("gene", ""), row.get("site", ""), row.get("alt", "")])
        for child, parent in sorted(inheritance.items()):
            writer.writerow([child, "clade", parent, ""])

    with args.report.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["clade", "status", "parent_clade", "reason"])
        writer.writerows(report)


if __name__ == "__main__":
    main()
