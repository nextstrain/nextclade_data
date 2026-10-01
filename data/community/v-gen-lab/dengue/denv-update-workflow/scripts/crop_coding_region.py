#!/usr/bin/env python3
"""Crop an aligned FASTA to the outer bounds of coding features in a GFF3."""
import argparse


def coding_bounds(gff):
    starts, ends = [], []
    with open(gff) as handle:
        for line in handle:
            if not line.strip() or line.startswith("#"):
                continue
            fields = line.rstrip("\n").split("\t")
            if len(fields) == 9 and fields[2] in {"CDS", "gene"}:
                starts.append(int(fields[3]))
                ends.append(int(fields[4]))
    if not starts:
        raise ValueError(f"No coding features found in {gff}")
    return min(starts), max(ends)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alignment", required=True)
    parser.add_argument("--gff", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    start, end = coding_bounds(args.gff)
    with open(args.alignment) as source, open(args.output, "w") as target:
        name, sequence = None, []
        for line in source:
            if line.startswith(">"):
                if name is not None:
                    target.write(name)
                    target.write("".join(sequence)[start - 1:end] + "\n")
                name, sequence = line, []
            else:
                sequence.append(line.strip())
        if name is not None:
            target.write(name)
            target.write("".join(sequence)[start - 1:end] + "\n")


if __name__ == "__main__":
    main()
