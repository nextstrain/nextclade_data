# Nextclade dataset for "Mpox virus (All Clades)"

| Key                    | Value                                                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authors                | [Cornelius Roemer](https://neherlab.org), [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                            |
| data source            | Genbank                                                                                                                                                          |
| workflow               | [github.com/nextstrain/mpox/nextclade](https://github.com/nextstrain/mpox/nextclade)                                                                             |
| nextclade dataset path | nextstrain/mpox/all-clades                                                                                                                                       |
| annotation             | [NC_063383.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_063383)                                                                                                    |
| clade definitions      | [github.com/mpxv-lineages/lineage-designation](https://github.com/mpxv-lineages/lineage-designation)                                                             |
| related datasets       | Mpox virus (Clade IIb): `nextstrain/mpox/clade-iib`<br>Mpox virus (Lineage B.1) `nextstrain/mpox/lineage-b.1`<br>Mpox virus (Clade I): `nextstrain/mpox/clade-i` |

## Scope of this dataset

TODO: Copy to other datasets before merging to main

This dataset is for Mpox viruses of all clades (Ia, Ib, IIa and IIb). For a focused analysis of sequences from clade IIb, you may want to use the more specific dataset: "Clade IIb" (`nextstrain/mpox/clade-iib`). For an even more focused analysis of clade IIb outbreak sh2023 lineage B.1 outbreak sequences (lineage B.1 and sublineages), you may want to use the even more specific dataset: "Lineage B.1" (`nextstrain/mpox/lineage-b.1`). For clade I sequences, you may want to use the dataset "Clade I" (`nextstrain/mpox/clade-i`).

## Clade, outbreak and lineage nomenclature

The clade, outbreak and lineage nomenclature used in this dataset is described in [Ruis et al. (2025)](https://www.nature.com/articles/s41591-025-03820-6). Clades comprise Ia, Ib, IIa, and IIb. Outbreaks are labeled as `sh2017` (clade IIb), `sh2023` (clade Ib), and `sh2024` (clade Ia). Some outbreaks have lineage systems that follow [Happi et al. (2022)](https://doi.org/10.1371/journal.pbio.3001769). To unambigously refer to a lineage, include the outbreak, e.g. `sh2017/B.1` for clade IIb outbreak sh2017 lineage B.1. Up to date outbreak and lineage definitions, including aliases, defining mutations and reference sequences are available at [github.com/mpxv-lineages/lineage-designation](https://github.com/mpxv-lineages/lineage-designation).

## Reference sequence and reference tree

The reference used in this dataset is the clade IIb NCBI refseq `NC_063383.1` (Isolate `MPXV-M5312_HM12_Rivers`).

Sequences for the reference tree come from NCBI/Genbank and are downsampled to around 900 sequences from the diversity of clades, lineages, countries and collection dates.

## Further reading

Read more about Nextclade datasets in Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
