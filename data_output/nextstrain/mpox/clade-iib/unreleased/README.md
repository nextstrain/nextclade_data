# Nextclade dataset for "Mpox virus (Clade IIb)"

| Key                    | Value                                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| authors                | [Cornelius Roemer](https://neherlab.org), [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org) |
| data source            | Genbank                                                                                                               |
| workflow               | [github.com/nextstrain/mpox/nextclade](https://github.com/nextstrain/mpox/nextclade)                                  |
| nextclade dataset path | nextstrain/mpox/clade-iib                                                                                             |
| annotation             | [NC_063383.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_063383)                                                         |
| clade definitions      | [github.com/mpxv-lineages/lineage-designation](https://github.com/mpxv-lineages/lineage-designation)                  |
| related datasets       | Mpox virus (All clades): `nextstrain/mpox/all-clades`<br> Mpox virus (Lineage B.1) `nextstrain/mpox/lineage-b.1`      |

## Scope of this dataset

This dataset is for Mpox viruses of clade IIb. A more specific dataset just for outbreak lineage B.1 is available as `nextstrain/mpox/lineage-b.1`. There is also a broader dataset for all clades I, IIa and IIb under `nextstrain/mpox/all-clades`.

## Reference sequence and reference tree

The reference used in this dataset is the clade IIb NCBI refseq `NC_063383.1` (Isolate `MPXV-M5312_HM12_Rivers`).

The reference tree consists of around 500 sequences with representatives from all clade IIb lineages.

## Clade, outbreak and lineage nomenclature

The clade, outbreak and lineage nomenclature used in this dataset is described in [Ruis et al. (2025)](https://www.nature.com/articles/s41591-025-03820-6). Clade IIb sequences belong to outbreak `sh2017`, which has a lineage system that follows [Happi et al. (2022)](https://doi.org/10.1371/journal.pbio.3001769). To unambiguously refer to a lineage, include the outbreak, e.g. `sh2017/B.1` for clade IIb outbreak sh2017 lineage B.1. This matters because other outbreaks (e.g. clade Ib outbreak sh2023) reuse the same lineage names. Up to date outbreak and lineage definitions, including aliases, defining mutations and reference sequences are available at [github.com/mpxv-lineages/lineage-designation](https://github.com/mpxv-lineages/lineage-designation).

## Further reading

Read more about Nextclade datasets in Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
