# Rubella virus (E1 region only) dataset

| Key               | Value                                                            |
| ----------------- | -----------------------------------------------------------------|
| name              | Rubella virus E1 region                                          |
| authors           | [Nextstrain](https://nextstrain.org)                             |
| reference         | NC_001545.2                                                      |
| workflow          | <https://github.com/nextstrain/rubella/tree/main/nextclade>      |
| path              | `nextstrain/rubella/E1`                                          |

## Scope of this dataset

This dataset assigns clades to rubella virus samples based on strain
and genotype information from [Rubella virus nomenclature update:
2013][].

This paper defines 13 distinct rubella virus genotypes based on a 739
nucleotide region of the rubella virus genome, (bases 8258-9700),
comprising a portion of the E1 gene, which encodes one of the two
spike proteins.

This dataset can be used to assign genotypes to any sequence that
includes at least 700 bp of the E1 region, including whole genome
sequences. Sequence data beyond the E1 region will be reported as an
insertion in the Nextclade output.

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation:
<https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html>

[Rubella virus nomenclature update: 2013]: https://www.who.int/publications/i/item/WER8832
