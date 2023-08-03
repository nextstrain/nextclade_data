#!/usr/bin/env python3

"""
Converts datasets from v2 to v3 format
"""
import json
import os
from os.path import join, dirname, exists, basename
from typing import List

from utils import json_read, find_files, json_write, now_iso, dict_set, dict_cleanup, dict_get, dict_remove_many, copy, \
  csv_read

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT_DIR = os.path.realpath(join(THIS_DIR, ".."))
DATA_V2_INPUT_DIR = os.path.realpath(join(PROJECT_ROOT_DIR, "data/datasets"))
DATA_V2_EXPERIMENTAL_INPUT_DIR = os.path.realpath(join(PROJECT_ROOT_DIR, "data/datasets_experimental"))
DATA_V3_OUTPUT_DIR = os.path.realpath(join(PROJECT_ROOT_DIR, "data_v3"))


def process_tree_json(tree: dict, virus_properties: dict, output_tree_json_path: str):
  placementMaskRanges = virus_properties.get("placementMaskRanges")
  if placementMaskRanges is not None:
    dict_set(tree, ["meta", "extensions", "nextclade", "placement_mask_ranges"], placementMaskRanges)
  meta = dict_cleanup(dict_get(tree, ["meta"]))
  dict_set(tree, ["meta"], meta)
  json_write(tree, output_tree_json_path, no_sort_keys=True)


def process_pathogen_json(inputs, output_pathogen_json_path):
  tag_json = inputs["tag_json"]
  primers = inputs["primers"]
  qc = inputs["qc"]
  virus_properties = inputs["virus_properties"]

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

  pathogen_json = {
    **tag_json,
    "updatedAt": now_iso(),
    "attributes": attributes,
    "primers": primers,
    "qc": qc,
    "mutLabels": {
      "nucMutLabelMap": virus_properties.get("nucMutLabelMap"),
    },
    **virus_properties,
    "experimental": tag_json.get("experimental") or False,
    "deprecated": False,
    "schemaVersion": "3.0.0",
  }

  dict_remove_many(pathogen_json, [
    "comment",
    "compatibility",
    "defaultRef",
    "files",
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

  json_write(pathogen_json, output_pathogen_json_path)


def convert_datasets_mature():
  for dataset_json_path in find_files("dataset.json", DATA_V2_INPUT_DIR):
    with open(dataset_json_path, 'r') as f:
      dataset_json: dict = json.load(f)

    dataset_dir = os.path.dirname(dataset_json_path)
    for dataset_ref_json_path in find_files("datasetRef.json", dataset_dir):

      with open(dataset_ref_json_path, 'r') as f:
        dataset_ref_json: dict = json.load(f)

      dataset_ref_dir = os.path.dirname(dataset_ref_json_path)

      version_jsons: List[dict] = []
      for tag_path in find_files("tag.json", dataset_ref_dir):
        with open(tag_path, 'r') as f:
          version_json: dict = json.load(f)
        version_jsons.append(version_json)

      version_jsons.sort(key=lambda x: x["tag"], reverse=True)
      last_version_json = version_jsons[0]

      tag_json = {**last_version_json, **dataset_json, **dataset_ref_json}
      name = tag_json["name"]
      ref_accession = tag_json["reference"]["accession"]
      tag = tag_json["tag"]

      input_dir = join(DATA_V2_INPUT_DIR, name, "references", ref_accession, "versions", tag, "files")
      output_dir = join(DATA_V3_OUTPUT_DIR, name, ref_accession)

      copy(join(input_dir, 'genemap.gff'), join(output_dir, "genome_annotation.gff3"))
      copy(join(input_dir, 'reference.fasta'), output_dir)
      copy(join(input_dir, 'sequences.fasta'), output_dir)

      qc = json_read(join(input_dir, 'qc.json'))
      virus_properties = json_read(join(input_dir, 'virus_properties.json'))
      primers = csv_read(join(input_dir, 'primers.csv'))
      tree = json_read(join(input_dir, 'tree.json'))

      process_tree_json(tree, virus_properties, join(output_dir, 'tree.json'))

      process_pathogen_json({
        "tag_json": tag_json,
        "qc": qc,
        "virus_properties": virus_properties,
        "primers": primers,
      },
        join(output_dir, "pathogen.json")
      )


def convert_datasets_experimental():
  for tag_path in find_files("tag.json", DATA_V2_EXPERIMENTAL_INPUT_DIR):
    tag_json = json_read(tag_path)

    name = basename(dirname(dirname(tag_path)))
    ref_accession = dict_get(tag_json, ["reference", "accession"]) or "UNKNOWN"

    tag_json = {
      **tag_json,
      "name": name,
      "nameFriendly": "UNKNOWN",
      "reference": {
        "accession": ref_accession,
        "strainName": "UNKNOWN",
      },
      "experimental": True,
    }

    input_dir = join(DATA_V2_EXPERIMENTAL_INPUT_DIR, name, "files")
    output_dir = join(DATA_V3_OUTPUT_DIR, name, ref_accession)

    copy(join(input_dir, 'genemap.gff'), join(output_dir, "genome_annotation.gff3"))
    copy(join(input_dir, 'reference.fasta'), output_dir)

    sequences_fasta_path = join(input_dir, 'sequences.fasta')
    if exists(sequences_fasta_path):
      copy(sequences_fasta_path, output_dir)

    qc = json_read(join(input_dir, 'qc.json'))
    virus_properties = json_read(join(input_dir, 'virus_properties.json'))
    primers = csv_read(join(input_dir, 'primers.csv'))
    tree = json_read(join(input_dir, 'tree.json'))

    process_tree_json(tree, virus_properties, join(output_dir, 'tree.json'))

    process_pathogen_json({
      "tag_json": tag_json,
      "qc": qc,
      "virus_properties": virus_properties,
      "primers": primers,
    },
      join(output_dir, "pathogen.json")
    )


if __name__ == '__main__':
  convert_datasets_mature()
  convert_datasets_experimental()
