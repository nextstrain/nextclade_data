#!/usr/bin/env python3

"""
Converts datasets from v2 to v3 format
"""
import argparse
from os.path import join, isfile

from lib.changelog import format_dataset_attributes_md_table
from lib.container import dict_set, dict_cleanup, dict_get, dict_remove_many
from lib.date import now_iso
from lib.fs import json_write, copy, json_read, file_write


def check_file(dataset_dir, filename):
  if isfile(join(dataset_dir, filename)):
    return filename
  return None


def process_tree_json(tree: dict, virus_properties: dict, output_tree_json_path: str):
  placementMaskRanges = virus_properties.get("placementMaskRanges")
  if placementMaskRanges is not None:
    dict_set(tree, ["meta", "extensions", "nextclade", "placement_mask_ranges"], placementMaskRanges)
  meta = dict_cleanup(dict_get(tree, ["meta"]))
  dict_set(tree, ["meta"], meta)
  json_write(tree, output_tree_json_path, no_sort_keys=True)


def process_pathogen_json(tag_json, input_dir, output_dir):
  copy(join(input_dir, 'reference.fasta'), join(output_dir, 'reference.fasta'))

  if isfile(join(input_dir, 'genemap.gff')):
    copy(join(input_dir, 'genemap.gff'), join(output_dir, "genome_annotation.gff3"))

  if isfile(join(input_dir, 'sequences.fasta')):
    copy(join(input_dir, 'sequences.fasta'), join(output_dir, 'sequences.fasta'))

  qc = {}
  if isfile(join(input_dir, 'qc.json')):
    qc = json_read(join(input_dir, 'qc.json'))

  virus_properties = {}
  if isfile(join(input_dir, 'virus_properties.json')):
    virus_properties = json_read(join(input_dir, 'virus_properties.json'))

  primers = {}
  pathogen_json_path = join(output_dir, "pathogen.json")
  if isfile(pathogen_json_path):
    primers = dict_get(json_read(pathogen_json_path), ["primers"])

  if isfile(join(input_dir, "tree.json")):
    tree = json_read(join(input_dir, 'tree.json'))
    process_tree_json(tree, virus_properties, join(output_dir, 'tree.json'))

  attributes = {
    "name": tag_json["nameFriendly"],
    "refName": tag_json["reference"]["strainName"],
    "refAccession": tag_json["reference"]["accession"],
  }

  dict_remove_many(qc, ["schemaVersion"])

  readme_path = join(output_dir, "README.md")
  if not isfile(readme_path):
    attr_table = format_dataset_attributes_md_table(attributes)

    name = tag_json['nameFriendly'] if tag_json['nameFriendly'] != "UNKNOWN" else tag_json['name']
    ref = tag_json["reference"]["strainName"] if tag_json["reference"]["strainName"] != "UNKNOWN" \
      else tag_json["reference"]["accession"] if tag_json["reference"]["accession"] != "UNKNOWN" \
      else ""

    if len(ref) != 0:
      ref = f" based on reference \"{ref}\""

    file_write(
      f"# Nextclade dataset for \"{name}\"{ref} ({input_dir})\n\n\n## Dataset attributes\n\n"
      f"{attr_table}\n\n## Authors and contacts\n\nSource code: \n\nAuthor1: \n\nAuthor2: \n\n## What is "
      f"Nextclade dataset\n\nRead more about Nextclade datasets in Nextclade documentation: "
      f"https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html",
      readme_path
    )

  changelog_path = join(output_dir, "CHANGELOG.md")
  if not isfile(changelog_path):
    file_write(
      "## Unreleased\n\nInitial release for Nextclade v3!\n\nRead more about "
      "Nextclade datasets in the documentation: "
      "https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html",
      changelog_path
    )

  dict_remove_many(tag_json, ["schemaVersion"])
  dict_remove_many(virus_properties, ["schemaVersion"])

  pathogen_json = {
    "schemaVersion": "3.0.0",
    **tag_json,
    "files": {
      "reference": "reference.fasta",
      "pathogenJson": "pathogen.json",
      "genomeAnnotation": check_file(output_dir, "genome_annotation.gff3"),
      "treeJson": check_file(output_dir, "tree.json"),
      "examples": check_file(output_dir, "sequences.fasta"),
      "readme": check_file(output_dir, "README.md"),
      "changelog": check_file(output_dir, "CHANGELOG.md"),
    },
    "attributes": attributes,
    "meta": {
      "source code": "https://github.com/nextstrain/nextclade_data",
      "bugs": "https://github.com/nextstrain/nextclade_data/issues",
      "authors": [
      ],
    },
    "compatibility": {
      "cli": "3.0.0-alpha.0",
      "web": "3.0.0-alpha.0",
    },
    "primers": primers,
    "qc": qc,
    "mutLabels": {
      "nucMutLabelMap": virus_properties.get("nucMutLabelMap"),
    },
    **virus_properties,
    "experimental": tag_json.get("experimental") or False,
    "deprecated": tag_json.get("deprecated") or False,
    "version": {"tag": "unreleased"},
  }

  dict_remove_many(pathogen_json, [
    "comment",
    "defaultRef",
    "metadata",
    "name",
    "nameFriendly",
    "nucMutLabelMap",
    "nucMutLabelMapReverse",
    "placementMaskRanges",
    "reference",
    "tag",
  ])

  pathogen_json = dict_cleanup(pathogen_json)

  json_write(pathogen_json, join(output_dir, "pathogen.json"))


def convert_dataset_v2_to_v3(input_dir, output_dir):
  tag_json_path = join(input_dir, "tag.json")
  tag_json = {}
  if isfile(tag_json_path):
    tag_json = json_read(tag_json_path)

  name = dict_get(tag_json, ["name"]) or "UNKNOWN"
  name_friendly = dict_get(tag_json, ["name"]) or "UNKNOWN"
  ref_accession = dict_get(tag_json, ["reference", "accession"]) or "UNKNOWN"
  strain_name = dict_get(tag_json, ["reference", "accession"]) or "UNKNOWN"

  tag_json = {
    **tag_json,
    "name": name,
    "nameFriendly": name_friendly,
    "reference": {
      "accession": ref_accession,
      "strainName": strain_name,
    },
    "experimental": True,
  }

  process_pathogen_json(tag_json, input_dir, output_dir)


def parse_args():
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--input-dir', required=True, help='Directory a datasets in Nextclade v2 format')
  parser.add_argument('--output-dir', required=True,
                      help='Directory to output the converted dataset in the Nextclade v3 format')
  return parser.parse_args()


if __name__ == '__main__':
  args = parse_args()

  updated_at = now_iso()

  convert_dataset_v2_to_v3(
    input_dir=args.input_dir,
    output_dir=args.output_dir,
  )
