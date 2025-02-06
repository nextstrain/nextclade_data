#!/usr/bin/env python3

"""
Runs minimizers test: creates an index of refs and performs search on query sequences.

Example:

  ./scripts/suggest_datasets.py \
    --input-refs tests/minimizers/data/all_refs.fasta \
    --input-qrys data/nextstrain/flu/h3n2/ha/EPI1857216/sequences.fasta  \
       data/nextstrain/flu/h1n1pdm/ha/MW626062/sequences.fasta \
       data/nextstrain/flu/h1n1pdm/ha/MW626062/sequences.fasta \
       data/nextstrain/dengue/all/sequences.fasta
"""

import argparse

import numpy as np

from lib.fasta import fasta_read
from lib.minimizer import make_ref_search_index, get_ref_search_minimizers

def parse_args():
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument(
    '--input-refs', required=True, nargs='+',
    help='One or more fasta files with reference sequences',
  )
  parser.add_argument(
    '--input-qrys', required=True, nargs='+',
    help='One or more fasta files with query sequences. If omitted, only minimizer index will be '
         'calculated, the search in query sequences will not be performed',
  )

  args = parser.parse_args()

  return args



def run_search(index, qrys):
  normalization = index['normalization']
  hit_by_qry = {}
  no_hits = {}
  for qry in qrys:
    minimizers = get_ref_search_minimizers(qry)
    hit_count = np.zeros(len(index["references"]), dtype=np.int32)
    for m in minimizers:
      if m in index["minimizers"]:
        hit_count[index["minimizers"][m]] += 1

    # we expect hits to be proportional to the length of the sequence and the number of minimizers per reference
    normalized_hits = normalization * hit_count / len(qry.seq)
    # require at least 30% of the maximal hits and at least 10 hits
    if np.max(normalized_hits) < 0.1 or np.sum(hit_count) < 10:
      print(qry.name, "no hit")
      no_hits.add(qry.name)
    else:
      match_counts = np.sum(normalized_hits > 0.1)
      hit_by_qry[qry.name] = np.argsort(normalized_hits)[::-1][:match_counts]

  return hit_by_qry, no_hits

if __name__ == '__main__':
  args = parse_args()

  refs = fasta_read(args.input_refs)
  refs = {ref.name: ref for ref in refs}

  index = make_ref_search_index(refs)

  qrys = fasta_read(args.input_qrys)
  hit_by_qry, no_hits = run_search(index, qrys)

  print("no hits", no_hits)
  unmatched = set(hit_by_qry.keys())
  max_dataset = 10
  data_sets_to_run = []
  top_hit_matches = 0
  total_matches = 0
  for si in range(max_dataset):
    hit_by_ref = np.zeros(len(refs))
    tophit_by_ref = np.zeros(len(refs))
    for qry in unmatched:
      hit_by_ref[hit_by_qry[qry]] += 1
      tophit_by_ref[hit_by_qry[qry][0]] += 1

    # determine the best dataset to add. This is the dataset that matches most queries. If multiple datasets have the same number of hits, take the one with the most top hits
    best_dataset = np.argmax(hit_by_ref)
    best_top_dataset = np.argmax(tophit_by_ref)

    if hit_by_ref[best_top_dataset] == hit_by_ref[best_dataset]:
      best_dataset = best_top_dataset

    # add dataset, filter unmatched queries to exclude those that are already matched
    data_sets_to_run.append(best_dataset)
    unmatched = set([qry for qry in unmatched if best_dataset not in hit_by_qry[qry]])
    top_hit_matches += tophit_by_ref[best_dataset]
    total_matches += hit_by_ref[best_dataset]

    print("\n##iteration ", si)
    print("added dataset ", best_dataset, "with ", hit_by_ref[best_dataset], "hits and ", tophit_by_ref[best_dataset], "top hits")
    print("total matches", total_matches)
    print("top hit matches", top_hit_matches)
    print("unmatched remaining", len(unmatched))

    # break if all are covered
    if len(unmatched) == 0:
      break


