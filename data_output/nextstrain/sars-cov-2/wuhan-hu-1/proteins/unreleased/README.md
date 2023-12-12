# SARS-CoV-2 dataset with reference Wuhan-Hu-1/2019 and mature protein annotations

| Key               | Value                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authors           | [Cornelius Roemer](https://neherlab.org), [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                            |
| reference         | `Wuhan-Hu-1/2019`                                                                                                                                                |
| workflow          | https://github.com/neherlab/nextclade_data_workflows/tree/v3-sc2/sars-cov-2                                                                                      |
| path              | `nextstrain/sars-cov-2/proteins`                                                                                                                                 |
| clade definitions | [Nextstrain clades](https://nextstrain.org/blog/2022-04-29-SARS-CoV-2-clade-naming-2022) and [Pango lineages](https://www.nature.com/articles/s41564-020-0770-5) |

## Scope of this dataset

This dataset shows mutations relative to `Wuhan-Hu-1/2019` and is particularly useful for the analysis of datasets with sequence collection dates spanning the entire pandemic.

In contrast to the other Nextclade SARS-CoV-2 datasets, this dataset annotates amino acids relative to their position in the mature proteins nsp1-16. The other datasets annotate amino acids relative to ORF1a and ORF1b.

For the analysis of recent sequences, the BA.2, XBB and BA.2.86 datasets may be more appropriate, as they show mutations relative to the respective variants.

## Reference sequence and reference tree

The reference sequence in this dataset is `Wuhan-Hu-1/2019`.

The reference tree contains one sequence for each Pango lineage designated since mid-2021 and most lineages designated before that.

## Features

This dataset supports:

- Assignment of Nextstrain clades
- Assignment of Pango lineages
- Sequence QC
- Phylogenetic placement

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
