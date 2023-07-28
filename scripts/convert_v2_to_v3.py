#!/usr/bin/env python3

"""
Converts datasets from v2 to v3 format
"""
import csv
import fnmatch
import json
import os
import shutil
from functools import reduce
from os.path import join, dirname, exists, basename
from collections import namedtuple
from typing import List

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT_DIR = os.path.realpath(join(THIS_DIR, ".."))
DATA_V2_INPUT_DIR = os.path.realpath(join(PROJECT_ROOT_DIR, "data/datasets"))
DATA_V2_EXPERIMENTAL_INPUT_DIR = os.path.realpath(join(PROJECT_ROOT_DIR, "data/datasets_experimental"))
DATA_V3_OUTPUT_DIR = os.path.realpath(join(PROJECT_ROOT_DIR, "data_v3"))


def dict_to_namedtuple(name, dic):
  return namedtuple(name, dic.keys())(*dic.values())


def dict_set(obj: dict, key_path: List[str], value):
  for key in key_path[:-1]:
    obj = obj.setdefault(key, {})
  obj[key_path[-1]] = value


def dict_get(obj: dict, keys: List[str]):
  return reduce(lambda d, key: d.get(key) if d else None, keys, obj)


def dict_remove(obj: dict, key: str):
  if obj.get(key) is not None:
    obj.pop(key)


def dict_remove_many(obj: dict, keys: List[str]):
  for key in keys:
    dict_remove(obj, key)


def list_cleanup(data):
  new_data = []
  for v in data:
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data.append(v)
  return new_data


def dict_cleanup(data):
  new_data = {}
  for k, v in data.items():
    if isinstance(v, dict):
      v = dict_cleanup(v)
    elif isinstance(v, list):
      v = list_cleanup(v)
    if v not in (None, str(), list(), dict(),):
      new_data[k] = v
  return new_data


def find_files(pattern, here):
  for path, dirs, files in os.walk(os.path.abspath(here)):
    for filename in fnmatch.filter(files, pattern):
      yield join(path, filename)


def find_dirs(here):
  for path, dirs, _ in os.walk(os.path.abspath(here)):
    for dirr in dirs:
      yield join(path, dirr)


def find_dirs_here(here):
  return filter(os.path.isdir, [join(here, e) for e in os.listdir(here)])


def json_read(json_path) -> dict:
  with open(json_path, 'r') as f:
    return json.load(f)


def json_write(obj, filepath, no_sort_keys=False):
  ensure_dir(filepath)
  with open(filepath, "w") as f:
    json.dump(obj, f, indent=2, sort_keys=not no_sort_keys)
    f.write("\n")


def csv_read(csv_file_path) -> List[dict]:
  with open(csv_file_path, mode='r') as f:
    return list(csv.DictReader(f))


def copy(input_filepath, output_filepath):
  ensure_dir(output_filepath)
  shutil.copy2(input_filepath, output_filepath)


def rmrf(some_path):
  shutil.rmtree(some_path, ignore_errors=True)


def mkdir(dir_path):
  os.makedirs(dir_path, exist_ok=True)


def ensure_dir(file_path):
  mkdir(dirname(file_path))


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
