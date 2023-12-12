# SARS-CoV-2 dataset with mutations relative to BA.2.86

| Key               | Value                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authors           | [Cornelius Roemer](https://neherlab.org), [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                            |
| reference         | `Wuhan-Hu-1/2019` with BA.2.86 SNPs added                                                                                                                        |
| workflow          | https://github.com/neherlab/nextclade_data_workflows/tree/v3-sc2/sars-cov-2                                                                                      |
| path              | `nextstrain/sars-cov-2/BA.2.86`                                                                                                                                  |
| clade definitions | [Nextstrain clades](https://nextstrain.org/blog/2022-04-29-SARS-CoV-2-clade-naming-2022) and [Pango lineages](https://www.nature.com/articles/s41564-020-0770-5) |

## Scope of this dataset

This dataset shows mutations relative to the prototypical BA.2.86 sequence and is particularly useful for the analysis of SARS-CoV-2 sequences that are descended from BA.2.86.

For the analysis of non-BA.2.86 sequences, other Nextclade datasets for SARS-CoV-2 may be more appropriate. In addition, the `wuhan-hu-1/proteins` dataset shows amino acid mutations in coordinates of mature proteins (nsp1-16) instead of ORF1a and ORF1b coordinates.

## Reference sequence and reference tree

The reference sequence in this dataset is `Wuhan-Hu-1/2019` but with BA.2.86 SNPs added. SNPs (but not indels) are thus shown with respect to BA.2.86 while the mutation positions remain within the familiar `Wuhan-Hu-1` coordinate system.

The reference tree contains one sequence for each Pango lineage descended from BA.2 (including recombinants such as XBB) and is rooted on BA.2.

## Features

This dataset supports:

- Assignment of Nextstrain clades
- Assignment of Pango lineages
- Sequence QC
- Phylogenetic placement
- Calculation of ACE2 binding scores relative to BA.2.86 as described in [Starr et al. 2022](https://doi.org/10.1371/journal.ppat.1010951)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
