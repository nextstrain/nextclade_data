#!/usr/bin/env python3
"""Archive a manually approved set of definition TSV files as a new version."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import tempfile

from compare_definitions import read_rows, sha256


BUILDS = ("denv1", "denv2", "denv3", "denv4")
VERSION = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approved-root", type=Path, required=True,
                        help="directory containing denv1/clades.tsv through denv4/clades.tsv")
    parser.add_argument("--definitions-root", type=Path, default=Path("definitions"))
    parser.add_argument("--parent-version", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--input-file", type=Path, action="append", required=True,
                        help="reviewed input/provenance file to hash in the manifest; repeat as needed")
    parser.add_argument("--dry-run", action="store_true", help="validate inputs without publishing")
    args = parser.parse_args()

    if not VERSION.fullmatch(args.version) or not VERSION.fullmatch(args.parent_version):
        parser.error("version names may contain only letters, digits, dots, underscores and hyphens")
    if args.version == args.parent_version:
        parser.error("new version must differ from parent version")
    destination = args.definitions_root / args.version
    if destination.exists():
        parser.error(f"version already exists: {destination}")

    files = {}
    inputs = []
    for input_file in args.input_file:
        if not input_file.is_file():
            parser.error(f"input file does not exist: {input_file}")
        inputs.append({"path": str(input_file), "sha256": sha256(input_file)})
    for build in BUILDS:
        source = args.approved_root / build / "clades.tsv"
        parent = args.definitions_root / args.parent_version / build / "clades.tsv"
        if not source.is_file() or not parent.is_file():
            parser.error(f"missing approved or parent TSV for {build}: {source}, {parent}")
        read_rows(source)
        read_rows(parent)
        files[build] = {
            "parent_sha256": sha256(parent),
            "approved_sha256": sha256(source),
            "approved_rows": sum(read_rows(source).values()),
        }

    if args.dry_run:
        print(json.dumps({"version": args.version, "parent_version": args.parent_version,
                          "input_files": inputs, "files": files}, indent=2, sort_keys=True))
        return

    args.definitions_root.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{args.version}.", dir=args.definitions_root))
    try:
        for build in BUILDS:
            output = temporary / build / "clades.tsv"
            output.parent.mkdir()
            shutil.copyfile(args.approved_root / build / "clades.tsv", output)
            if sha256(output) != files[build]["approved_sha256"]:
                raise OSError(f"copy changed unexpectedly: {output}")
        manifest = {
            "created_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "version": args.version,
            "parent_version": args.parent_version,
            "input_files": inputs,
            "files": files,
        }
        (temporary / "manifest.json").write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        if destination.exists():
            raise FileExistsError(destination)
        temporary.rename(destination)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    print(destination)


if __name__ == "__main__":
    main()
