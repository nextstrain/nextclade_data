# Nextclade dataset for "Mpox virus (Clade I)"

| Key                    | Value                                                                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authors                | [Cornelius Roemer](https://neherlab.org), [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                                                  |
| data source            | Genbank                                                                                                                                                                                |
| workflow               | [github.com/nextstrain/mpox/nextclade](https://github.com/nextstrain/mpox/nextclade)                                                                                                   |
| nextclade dataset path | nextstrain/mpox/clade-i                                                                                                                                                                |
| reference              | [DQ011155.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ011155.1), isolate `Zaire_1979-005`, an early complete clade I sequence                                                            |
| annotation             | based on [DQ011155.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ011155.1), but with genes called by modern names (OPGXXX)                                                                 |
| clade definitions      | [github.com/mpxv-lineages/lineage-designation](https://github.com/mpxv-lineages/lineage-designation)                                                                                   |
| related datasets       | Mpox virus (All clades): `nextstrain/mpox/all-clades`<br>Mpox virus (clade IIb) `nextstrain/mpox/clade-iib`<br>Mpox virus (Lineage B.1 within clade IIb) `nextstrain/mpox/lineage-b.1` |

## Scope of this dataset

This dataset is for Mpox viruses of clade I (Ia and Ib). A broader dataset for all clades I, IIa and IIb is available under `nextstrain/mpox/all-clades`.

## Reference sequence and reference tree

The reference used in this dataset is [DQ011155.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ011155.1), an early complete clade I sequence (Isolate `Zaire_1979-005`).

This is in contrast to the reference used in the other Nextclade mpox datasets, which use a clade IIb reference sequence.

The reference tree consists of all good quality clade I sequences available within Genbank at the time of dataset creation (with identical sequences deduplicated to 1), as well as 3 outgroup genomes (a reconstructed ancestor of all clades, and one sequence for each of clade IIa and clade IIb).

## Clade, outbreak and lineage nomenclature

The clade, outbreak and lineage nomenclature used in this dataset is described in [Ruis et al. (2025)](https://www.nature.com/articles/s41591-025-03820-6). Clade I comprises clades Ia and Ib. The clade Ib outbreak is labeled `sh2023` and the clade Ia outbreak described in [Wawina-Bokalanga et al. (2025)](<https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)00294-6>) is labeled `sh2024`. Clade Ib outbreak sh2023 now has a lineage system that follows [Happi et al. (2022)](https://doi.org/10.1371/journal.pbio.3001769), reusing the same lineage names as clade IIb outbreak sh2017. To unambiguously refer to a lineage, include the outbreak, e.g. `sh2023/A.1` for clade Ib outbreak sh2023 lineage A.1. Up to date outbreak and lineage definitions, including aliases, defining mutations and reference sequences are available at [github.com/mpxv-lineages/lineage-designation](https://github.com/mpxv-lineages/lineage-designation).

## Further reading

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
