#!/usr/bin/env python3
"""
Script to add $schema line to all pathogen.json files in the data/ directory.
Only adds the schema if it's not already present.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any

SCHEMA_URL = "https://raw.githubusercontent.com/nextstrain/nextclade/refs/heads/release/packages/nextclade-schemas/input-pathogen-json.schema.json"

def has_schema(data: Dict[str, Any]) -> bool:
    """Check if the JSON data already has a $schema field."""
    return "$schema" in data

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
    """Main function to process all pathogen.json files in data/ directory."""
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"
    
    if not data_dir.exists():
        print(f"Data directory not found: {data_dir}")
        return
    
    # Find all pathogen.json files recursively in data/ directory
    pathogen_files = list(data_dir.rglob("pathogen.json"))
    
    if not pathogen_files:
        print("No pathogen.json files found in data/ directory")
        return
    
    print(f"Found {len(pathogen_files)} pathogen.json files")
    
    modified_count = 0
    for file_path in sorted(pathogen_files):
        if add_schema_to_json(file_path):
            modified_count += 1
    
    print(f"\nProcessing complete!")
    print(f"Total files: {len(pathogen_files)}")
    print(f"Modified files: {modified_count}")
    print(f"Unchanged files: {len(pathogen_files) - modified_count}")

if __name__ == "__main__":
    main()