# SARS-CoV-2 dataset BA.2-like reference (except for indels)

| Key     | Value                                                                          |
| ------- | ------------------------------------------------------------------------------ |
| authors | [Cornelius Roemer](https://neherlab.org), [Nextstrain](https://nextstrain.org) |

## Scope of this dataset

This dataset is useful for the analysis of SARS-CoV-2 sequences that are descended from the BA.2 lineage, which is most of the circulation since mid-2022, including BA.4/5, XBB, BA.2.86.

The reference used is Wuhan-Hu-1 but with BA.2 SNPs added to make it easier to interpret the results.

For the analysis of pre-BA.2 sequences, the dataset using the original Wuhan-Hu-1 reference might be more appropriate.

For the analysis of sequences descended from XBB and BA.2.86, there are more specific datasets available.

## Features

This dataset supports:

- Assignment of Nextstrain clades
- Assignment of Pango lineages
- Sequence QC
- Phylogenetic placement
- Calculation of immune escape scores relative to BA.2 neutralizing antibodies as described in [Greaney et al. 2022](https://doi.org/10.1093/ve/veac021)
- Calculation of ACE2 binding scores relative to BA.2 as described in [Starr et al. 2022](https://doi.org/10.1371/journal.ppat.1010951)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
