#!/usr/bin/env python3

"""
Converts datasets from v2 to v3 format
"""
import argparse
import json
from os.path import join, dirname, isfile, relpath
from typing import List
from lib.changelog import format_dataset_attributes_md_table
from lib.container import dict_set, dict_cleanup, dict_get, dict_remove_many
from lib.date import now_iso
from lib.fs import json_write, find_files, copy, json_read, file_write
from lib.string import removesuffix


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


def process_pathogen_json(tag_json, path, input_dir, output_dir, params=None, params_individual=None):
  if params is None:
    params = {}

  if params_individual is None:
    params_individual = {}

  copy(join(input_dir, 'reference.fasta'), output_dir)

  if isfile(join(input_dir, 'genemap.gff')):
    copy(join(input_dir, 'genemap.gff'), join(output_dir, "genome_annotation.gff3"))

  if isfile(join(input_dir, 'sequences.fasta')):
    copy(join(input_dir, 'sequences.fasta'), output_dir)

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
    "name": {
      "value": tag_json["name"],
      "valueFriendly": tag_json["nameFriendly"],
    },
    "reference": {
      "value": tag_json["reference"]["accession"],
      "valueFriendly": tag_json["reference"]["strainName"],
    }
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
      f"# Nextclade dataset for \"{name}\"{ref} ({path})\n\n\n## Dataset attributes\n\n{attr_table}\n\n## What is "
      f"Nextclade dataset\n\nRead more about Nextclade datasets in Nextclade documentation: "
      f"https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html",
      readme_path
    )

  changelog_path = join(output_dir, "CHANGELOG.md")
  if not isfile(changelog_path):
    file_write(
      "## Unreleased\n\nInitial release for Nextclade v3!\n\nThis dataset is converted from the corresponding older "
      "dataset for Nextclade v2. You can find old versions of datasets here: "
      "https://github.com/nextstrain/nextclade_data/tree/2023-08-17--15-51-24--UTC/data/datasets\n\nRead more about "
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
    "primers": primers,
    "qc": qc,
    "mutLabels": {
      "nucMutLabelMap": virus_properties.get("nucMutLabelMap"),
    },
    **virus_properties,
    "official": tag_json.get("official") or False,
    "experimental": tag_json.get("experimental") or False,
    "deprecated": tag_json.get("deprecated") or False,
    "version": {"tag": "unreleased"},
    **params,
    **(dict_get(params_individual, [path]) or {}),
  }

  dict_remove_many(pathogen_json, [
    "comment",
    "compatibility",
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


def convert_datasets_mature(input_dir, output_dir, params=None, params_individual=None):
  if params is None:
    params = {}

  if params_individual is None:
    params_individual = {}

  for dataset_json_path in find_files("dataset.json", input_dir):
    dataset_json = json_read(dataset_json_path)
    dataset_dir = dirname(dataset_json_path)
    for dataset_ref_json_path in find_files("datasetRef.json", dataset_dir):
      dataset_ref_json = json_read(dataset_ref_json_path)
      dataset_ref_dir = dirname(dataset_ref_json_path)

      version_jsons: List[dict] = []
      for tag_path in find_files("tag.json", dataset_ref_dir):
        with open(tag_path, 'r') as f:
          version_json: dict = json.load(f)
        version_jsons.append(version_json)

      version_jsons.sort(key=lambda x: x["tag"], reverse=True)
      last_version_json = version_jsons[0]

      tag_json = {
        **last_version_json,
        **dataset_json,
        **dataset_ref_json,
      }

      name = tag_json["name"]
      ref_accession = tag_json["reference"]["accession"]
      tag = tag_json["tag"]
      path = f"{name}/{ref_accession}"

      full_input_dir = f'{join(input_dir, name, "references", ref_accession, "versions", tag, "files")}/'
      full_output_dir = f'{join(output_dir, path)}/'

      process_pathogen_json(tag_json, path, full_input_dir, full_output_dir, params, params_individual)


def convert_datasets_experimental(input_dir, output_dir, params):
  for ref_fasta_path in find_files("reference.fasta", input_dir):
    full_input_dir = f"{dirname(ref_fasta_path)}/"
    path = removesuffix(relpath(full_input_dir, input_dir), "/files")
    full_output_dir = f"{join(output_dir, path)}/"

    tag_json_path = join(full_input_dir, "tag.json")
    tag_json = {}
    if isfile(tag_json_path):
      tag_json = json_read(tag_json_path)

    name = dict_get(tag_json, ["name"]) or path
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
      **params,
    }

    process_pathogen_json(tag_json, path, full_input_dir, full_output_dir)


def parse_args():
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--input-dir', required=True, help='Directory with datasets in the old format')
  parser.add_argument('--output-dir', required=True, help='Where to output datasets in the new format')
  return parser.parse_args()


if __name__ == '__main__':
  args = parse_args()

  updated_at = now_iso()

  convert_datasets_mature(
    input_dir=join(args.input_dir, "datasets"),
    output_dir=join(args.output_dir, "nextstrain"),
    params={"official": True},
    params_individual={"sars-cov-2-21L/BA.2": {"deprecated": True}},
  )

  convert_datasets_experimental(
    input_dir=join(args.input_dir, "datasets_experimental"),
    output_dir=join(args.output_dir, "nextstrain"),
    params={"official": True, "experimental": True},
  )

  convert_datasets_experimental(
    input_dir=join(args.input_dir, "datasets_community"),
    output_dir=join(args.output_dir, "community"),
    params={"experimental": True},
  )
