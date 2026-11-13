## Unreleased

QC: the thresholds of the private mutations, mixed sites and missing data rules scale with the length of each sequence. A sequence that covers only a part of the genome, such as one gene, is judged by the density of mutations, ambiguous nucleotides and missing data, instead of by thresholds for the full genome. Nextclade versions without QC length scaling ignore this setting and keep the thresholds for the full genome.

## 2026-04-14T11:55:23Z

- Move `placementMaskRanges` to tree.json
- Unify attributes per schema update

## 2025-09-09T12:13:13Z

Add schema definition url to `pathogen.json`. This is a purely technical change, for convenience of dataset authors. The data itself is not modified.

## 2024-05-08T11:39:52Z

Initial release of an HIV-1 dataset for subtype classification.
