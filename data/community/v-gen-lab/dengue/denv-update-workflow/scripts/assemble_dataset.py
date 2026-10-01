#!/usr/bin/env python3
"""Assemble a DENV Nextclade dataset from an update workflow result."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from pathlib import Path
from data_use import COLUMNS, accession_for, load_snapshot, metadata_for


STATIC_FILES = (
    "reference.fasta",
    "pathogen.json",
    "genome_annotation.gff3",
)


def updated_readme(previous: str, notice: str) -> str:
    """Update the outgroup wording and workflow-managed data-use notice."""
    previous = previous.replace(
        'The systems are independent, so sequences from other serotypes may not be classified or may be assigned as "Outgroup."',
        'The systems are independent, so sequences from other serotypes may be reported as `unassigned`.',
    )
    start = "<!-- workflow:data-use:start -->"
    end = "<!-- workflow:data-use:end -->"
    block = f"{start}\n{notice.strip()}\n{end}"
    if start in previous or end in previous:
        if previous.count(start) != 1 or previous.count(end) != 1:
            raise ValueError("README has malformed data-use notice markers")
        begin = previous.index(start)
        finish = previous.index(end)
        if finish < begin:
            raise ValueError("README has reversed data-use notice markers")
        return previous[:begin] + block + previous[finish + len(end):]
    return previous.rstrip() + "\n\n" + block + "\n"


def open_examples(source: Path, records: dict) -> tuple[str, list[str], int]:
    """Keep example FASTA records unless Pathoplexus marks them RESTRICTED."""
    records_out = []
    names = []
    removed = 0
    current_name = None
    current_lines = []

    def finish_record() -> None:
        nonlocal removed
        if current_name is None:
            return
        accession = accession_for(current_name)
        if accession and accession not in records:
            raise ValueError(f"Pathoplexus terms missing from snapshot: {accession}")
        if accession and records[accession]["dataUseTerms"] == "RESTRICTED":
            removed += 1
        else:
            names.append(current_name)
            records_out.extend(current_lines)

    with source.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith(">"):
                finish_record()
                current_name = line[1:].split()[0]
                current_lines = [line]
            else:
                if current_name is None:
                    raise ValueError(f"FASTA content before first header: {source}")
                current_lines.append(line)
    finish_record()
    if not names:
        raise ValueError(f"No example sequences remain after filtering: {source}")
    return "".join(records_out), names, removed


def copy_file(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Required input is missing: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def latest_dataset(history_root: Path, build: str) -> Path:
    build_root = history_root / build
    candidates = sorted(path for path in build_root.iterdir() if path.is_dir())
    if not candidates:
        raise FileNotFoundError(f"No released dataset found in: {build_root}")
    return candidates[-1]


def updated_changelog(previous: str, notes: list[str]) -> str:
    """Prepend the pending release notes, replacing a stale Unreleased section."""
    previous = re.sub(
        r"\A## Unreleased\s*\n.*?(?=^## |\Z)",
        "",
        previous,
        flags=re.DOTALL | re.MULTILINE,
    ).lstrip()
    entries = "\n".join(f"- {note}" for note in notes)
    return f"## Unreleased\n\n{entries}\n\n{previous}"


def definition_lineages(path: Path) -> set[str]:
    """Return lineages with direct markers, excluding inherited-parent rows."""
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if not reader.fieldnames or not {"clade", "gene"}.issubset(reader.fieldnames):
            raise ValueError(f"{path} must contain clade and gene columns")
        return {
            row["clade"].strip()
            for row in reader
            if row["clade"].strip() and row["gene"].strip() != "clade"
        }


def new_lineage_note(build: str, baseline: Path, current: Path) -> str:
    added = sorted(definition_lineages(current) - definition_lineages(baseline))
    if not added:
        return f"New lineages: none for {build.upper()}"
    return "New lineages: " + ", ".join(added)


def prepare_pathogen_for_publication(path: Path) -> None:
    """Reset release metadata so the dataset can be committed under data/."""
    pathogen = json.loads(path.read_text(encoding="utf-8"))
    pathogen["version"] = {"tag": "unreleased"}
    path.write_text(
        json.dumps(pathogen, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Assemble one updated DENV dataset without modifying its published source."
    )
    parser.add_argument("--build", required=True, choices=("denv1", "denv2", "denv3", "denv4"))
    parser.add_argument("--dataset-history-root", required=True, type=Path)
    parser.add_argument("--test-set", required=True, type=Path)
    parser.add_argument("--tree", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--release-note", action="append", required=True)
    parser.add_argument("--data-use-notice", required=True, type=Path)
    parser.add_argument("--data-use-snapshot", required=True, type=Path)
    parser.add_argument("--baseline-definitions", required=True, type=Path)
    parser.add_argument("--current-definitions", required=True, type=Path)
    args = parser.parse_args()

    records = load_snapshot(args.data_use_snapshot)
    examples_fasta, example_names, removed = open_examples(args.test_set, records)
    tree = json.loads(args.tree.read_text())
    pending = [tree['tree']]
    names = []
    while pending:
        node = pending.pop()
        if node.get('children'):
            pending.extend(node['children'])
        else:
            names.append(node['name'])
    terms_rows = [
        {'strain': name, 'set': role, **metadata_for(name, records)}
        for role, strains in [('representatives', sorted(names)), ('examples', example_names)]
        for name in strains
    ]

    current_dataset = latest_dataset(args.dataset_history_root, args.build)
    readme = updated_readme(
        (current_dataset / "README.md").read_text(encoding="utf-8"),
        args.data_use_notice.read_text(encoding="utf-8"),
    )

    # Everything that is not generated by the workflow is recovered from the
    # most recent archived dataset for this serotype.
    for filename in STATIC_FILES:
        copy_file(current_dataset / filename, args.output_dir / filename)
    (args.output_dir / "README.md").write_text(readme, encoding="utf-8")
    with (args.output_dir / "data-use.tsv").open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['strain', 'set', *COLUMNS], delimiter='\t')
        writer.writeheader()
        writer.writerows(terms_rows)
    prepare_pathogen_for_publication(args.output_dir / "pathogen.json")

    changelog = current_dataset / "CHANGELOG.md"
    if not changelog.is_file():
        raise FileNotFoundError(f"Required input is missing: {changelog}")
    (args.output_dir / "CHANGELOG.md").write_text(
        updated_changelog(
            changelog.read_text(encoding="utf-8"),
            [*args.release_note, new_lineage_note(args.build, args.baseline_definitions, args.current_definitions)],
        ),
        encoding="utf-8",
    )
    (args.output_dir / "sequences.fasta").write_text(examples_fasta, encoding="utf-8")
    print(f"{args.build}: excluded {removed} RESTRICTED examples; kept {len(example_names)}")
    copy_file(args.tree, args.output_dir / "tree.json")


if __name__ == "__main__":
    main()
