#!/usr/bin/env python3
"""Convert a supplied NEXUS representative tree to clean Newick.

The conversion deliberately preserves topology and branch lengths.  NEXUS
annotations (such as the supplied lineage comments) are removed because they
are not inputs to Augur; lineage labels are read from sequence_lineages.csv.
"""
import argparse
from pathlib import Path

from Bio import Phylo, SeqIO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--expected-fasta", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    tree = Phylo.read(args.input, "nexus")
    for clade in tree.find_clades():
        # The source NEXUS quotes every taxon label.  The matching FASTA and
        # metadata use unquoted IDs, which Augur requires as node names.
        if clade.name:
            clade.name = clade.name.strip("'\"")
        clade.comment = None

    tree_tips = [tip.name for tip in tree.get_terminals()]
    expected_tips = [record.id for record in SeqIO.parse(args.expected_fasta, "fasta")]
    if len(tree_tips) != len(set(tree_tips)):
        raise ValueError("The supplied tree has duplicate terminal names")
    if set(tree_tips) != set(expected_tips):
        missing_from_tree = sorted(set(expected_tips) - set(tree_tips))
        missing_from_fasta = sorted(set(tree_tips) - set(expected_tips))
        raise ValueError(
            "Tree and representative FASTA have different terminal IDs; "
            f"missing_from_tree={missing_from_tree[:5]}, "
            f"missing_from_fasta={missing_from_fasta[:5]}"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    Phylo.write(tree, args.output, "newick")


if __name__ == "__main__":
    main()
