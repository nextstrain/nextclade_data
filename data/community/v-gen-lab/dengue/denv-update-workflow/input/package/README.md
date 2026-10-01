# DENV lineage-assignment reference data - 2026 update

Package date 2026-09-15, including all material (alignments, trees, designations) for 
lineage attribution tools. 

## Contents

| File | Content |
| --- | --- |
| `DENV{1,2,3,4}_representatives.fasta` | 417 / 515 / 209 / 160 aligned representatives |
| `DENV{1,2,3,4}_representatives.tree` | NEXUS, pruned from the full round tree, tips annotated with `[&lineage=]` |
| `DENV{1,2,3,4}_test_set.fasta` | 70 / 92 / 38 / 31 held-out sequences |
| `representative_sequences.csv` | panel, `sequence,designation`, unchanged from pipeline output |
| `test_set.csv` | held-out set |
| `sequence_lineages.csv` | panel with terminal designation for each sequence |

## How to read `representative_sequences.csv`

The `designation` column records a **role**, not a label. It answers "which lineage was
this sequence picked to anchor", not "which lineage does this sequence belong to". One
sequence therefore appears in several rows: 1627 rows for 1301 distinct sequences, with
223 sequences carrying more than one role. `sequence_lineages.csv` includes terminal 
designations for each sequence included in representative and test sets.

A representative of lineage `X.1` is a member of the clade `X`. It is **not** required to
carry `X` as its own terminal designation, and often cannot:

* `1V_D`, `1I_K.1` and `2II_A.2` are fully partitioned into child lineages. No sequence in
  the dataset carries those labels terminally, so every representative of `1V_D` is
  necessarily a `1V_D.1` or `1V_D.2` sequence. There is no alternative.
* More generally, 254 of the 1387 in-group rows pair a sequence with an ancestor of its own
  terminal lineage. Zero rows pair a sequence with a lineage it does not belong to, and
  zero lineages lack in-group coverage.


## Pathoplexus data-use snapshot

`pathoplexus-data-use.json` records terms retrieved on 2026-09-24 for the 1,524
Pathoplexus accessions in the representative and example FASTAs (1,488 OPEN,
36 RESTRICTED). It includes API provenance, retrieval time, and input hashes.
It was collected by `scripts/snapshot_data_use.py` as the accepted per-sequence
metadata change from F1 of the PR #478 review. Preserve it with this input
package; see the workflow README for the explicit refresh procedure.

The current initial baseline is `pathoplexus-metadata-2026-09-28.json`, which
also records `geoLocCountry`. New updates use `scripts/update_dataset.py` to
collect fresh metadata and save a separate snapshot and change report under
`input/metadata-runs/`. The dated files in this package remain preserved.

## Contact

If any issue comes up, please reach out to Filipe Moreira (filipe.moreira@itps.org.br) and
Anderson Brito (anderson.brito@itps.org.br).
