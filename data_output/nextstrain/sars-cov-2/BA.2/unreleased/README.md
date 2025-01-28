# SARS-CoV-2 dataset with mutations relative to BA.2

| Key               | Value                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authors           | [Cornelius Roemer](https://neherlab.org), [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                            |
| reference         | `Wuhan-Hu-1/2019` with BA.2 SNPs added                                                                                                                           |
| workflow          | https://github.com/neherlab/nextclade_data_workflows/tree/v3-sc2/sars-cov-2                                                                                      |
| path              | `nextstrain/sars-cov-2/BA.2`                                                                                                                                     |
| clade definitions | [Nextstrain clades](https://nextstrain.org/blog/2022-04-29-SARS-CoV-2-clade-naming-2022) and [Pango lineages](https://www.nature.com/articles/s41564-020-0770-5) |

## Scope of this dataset

This dataset shows mutations relative to the prototypical BA.2 sequence and is particularly useful for the analysis of SARS-CoV-2 sequences that are descended from the BA.2 lineage.

For the analysis of sequences not descended from BA.2, the `wuhan-hu-1/orfs` is more appropriate as it includes lineages from the start of the pandemic. The `wuhan-hu-1/proteins` dataset shows amino acid mutations in coordinates of mature proteins (nsp1-16) instead of ORF1a/b polyproteins.

## Reference sequence and reference tree

The reference sequence in this dataset is `Wuhan-Hu-1/2019` but with BA.2 SNPs added. SNPs (but not indels) are thus shown with respect to BA.2 while the mutation positions remain within the familiar `Wuhan-Hu-1` coordinate system.

The reference tree contains one sequence for each Pango lineage descended from BA.2 (including recombinants such as XBB) and is rooted on BA.2.

## Features

This dataset supports:

- Assignment of Nextstrain clades
- Assignment of Pango lineages
- Sequence QC
- Phylogenetic placement
- Calculation of immune escape scores relative to BA.2 neutralizing antibodies as described in [Greaney et al. 2022](https://doi.org/10.1093/ve/veac021)
- Calculation of ACE2 binding scores relative to BA.2 as described in [Starr et al. 2022](https://doi.org/10.1371/journal.ppat.1010951)

## Nextstrain clades

Since its emergence in late 2019, SARS-CoV-2 has evolved into many co-circulating variants. To facilitate discussion of these variants, we have grouped them into clades which are defined by specific signature mutations.

Nextstrain clade names consist of two numbers representing a year and then a single letter representing the clade within that year. For example, 21A is the first clade we named in 2021.

We define each clade by a combination of signature mutations. You can find the exact clade definition on Github in this [file](https://github.com/nextstrain/ncov/blob/master/defaults/clades.tsv).

Below is an illustration of the phylogenetic relationships of Nextstrain clades ([source](https://github.com/nextstrain/ncov-clades-schema/)):

![Illustration of phylogenetic relationships of SARS-CoV-2 clades, as defined by Nextstrain](https://raw.githubusercontent.com/nextstrain/ncov-clades-schema/master/clades.svg)

Learn more about how Nextclade assigns clades in the [documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/algorithm/).

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
