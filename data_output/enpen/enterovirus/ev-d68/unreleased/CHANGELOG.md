## Unreleased

- Ancestral sequence is now root of the tree and taken as the alignment reference
- The ordering in Nextclade Web results of the references has changed to display Fermon first for mutation calling
- The `pre-ABC` clade is now assigned based on a deletion in the 5'UTR
- New sequences in A2/D clade (released in April) were added
- The sequences are now subsampled by country & year
- The seed-match threshold was increased from 0.4 to 0.75 so that other EVs don't align
- The accession numbers in the tree now have a URL to GenBank

## 2026-04-14T11:55:23Z

- Remove deprecated `nucMutLabelMapReverse` field (computed at runtime in v3)
- Remove invalid `qc.divergence` rule (not a configurable parameter)

## 2025-12-10T13:21:04Z

- Update alignment parameters in pathogen.json:
  - Fix gap extension penalty
  - Enable reverse-complement handling
- Recompute tree topology (ML tree rerun)
- Regenerate mutation labels for all clades
- Update reference example sequences

## 2025-11-20T19:02:04Z

Add citation information to README.md

## 2025-11-19T20:40:14Z

Initial release of an Enterovirus D68 dataset for lineage classification!

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
