#!/usr/bin/env python3
"""
Script to add $schema line to all pathogen.json files in the data/ directory
and add "Unreleased" section to corresponding CHANGELOG.md files.
Only adds the schema if it's not already present.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any

SCHEMA_URL = "https://raw.githubusercontent.com/nextstrain/nextclade/refs/heads/release/packages/nextclade-schemas/input-pathogen-json.schema.json"

CHANGELOG_ENTRY = """## Unreleased

Add schema definition url to `pathogen.json`. This is a purely technical change, for convenience of dataset authors. The data itself is not modified.

"""

def has_schema(data: Dict[str, Any]) -> bool:
    """Check if the JSON data already has a $schema field."""
    return "$schema" in data

def has_unreleased_section(content: str) -> bool:
    """Check if the changelog already has an Unreleased section."""
    return "## Unreleased" in content

def add_unreleased_to_changelog(file_path: Path) -> bool:
    """
    Add "Unreleased" section to a CHANGELOG.md file if it doesn't already have one.
    Returns True if the file was modified, False otherwise.
    """
    try:
        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if "Unreleased" section already exists
        if has_unreleased_section(content):
            print(f"Unreleased section already exists in: {file_path}")
            return False

        # Add the unreleased section at the beginning
        new_content = CHANGELOG_ENTRY + content

        # Write back the modified content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Added Unreleased section to: {file_path}")
        return True

    except Exception as e:
        print(f"Error processing changelog {file_path}: {e}")
        return False

def process_dataset_directory(dataset_dir: Path) -> tuple[bool, bool]:
    """
    Process a dataset directory containing pathogen.json and CHANGELOG.md.
    Returns (json_modified, changelog_modified).
    """
    pathogen_json = dataset_dir / "pathogen.json"
    changelog_md = dataset_dir / "CHANGELOG.md"

    json_modified = False
    changelog_modified = False

    # Process pathogen.json
    if pathogen_json.exists():
        json_modified = add_schema_to_json(pathogen_json)
    else:
        print(f"Warning: pathogen.json not found in {dataset_dir}")

    # Process CHANGELOG.md
    if changelog_md.exists():
        changelog_modified = add_unreleased_to_changelog(changelog_md)
    else:
        print(f"Warning: CHANGELOG.md not found in {dataset_dir}")

    return json_modified, changelog_modified

def add_schema_to_json(file_path: Path) -> bool:
    """
    Add schema to a pathogen.json file if it doesn't already have one.
    Returns True if the file was modified, False otherwise.
    """
    try:
        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse JSON
        data = json.loads(content)

        # Check if schema already exists
        if has_schema(data):
            print(f"Schema already exists in: {file_path}")
            return False

        # Create new ordered dict with schema first
        new_data = {"$schema": SCHEMA_URL}
        new_data.update(data)

        # Write back with proper formatting (2-space indentation to match existing files)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
            f.write('\n')  # Add final newline

        print(f"Added schema to: {file_path}")
        return True

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all dataset directories in data/ directory."""
    script_dir = Path(__file__).parent.parent  # Go up one level since we're in scripts/
    data_dir = script_dir / "data"

    if not data_dir.exists():
        print(f"Data directory not found: {data_dir}")
        return

    # Find all directories containing pathogen.json files
    pathogen_files = list(data_dir.rglob("pathogen.json"))
    dataset_dirs = [f.parent for f in pathogen_files]

    if not dataset_dirs:
        print("No dataset directories found in data/ directory")
        return

    print(f"Found {len(dataset_dirs)} dataset directories")

    json_modified_count = 0
    changelog_modified_count = 0

    for dataset_dir in sorted(dataset_dirs):
        print(f"\nProcessing: {dataset_dir}")
        json_modified, changelog_modified = process_dataset_directory(dataset_dir)

        if json_modified:
            json_modified_count += 1
        if changelog_modified:
            changelog_modified_count += 1

    print(f"\nProcessing complete!")
    print(f"Total dataset directories: {len(dataset_dirs)}")
    print(f"Modified pathogen.json files: {json_modified_count}")
    print(f"Modified CHANGELOG.md files: {changelog_modified_count}")
    print(f"Unchanged pathogen.json files: {len(dataset_dirs) - json_modified_count}")
    print(f"Unchanged CHANGELOG.md files: {len(dataset_dirs) - changelog_modified_count}")

if __name__ == "__main__":
    main()
