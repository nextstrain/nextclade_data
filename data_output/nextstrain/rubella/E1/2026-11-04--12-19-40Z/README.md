# Rubella virus E1 region dataset

| Key       | Value                                                       |
| --------- | ----------------------------------------------------------- |
| name      | Rubella virus E1 region                                     |
| authors   | [Nextstrain](https://nextstrain.org)                        |
| reference | NC_001545.2                                                 |
| workflow  | <https://github.com/nextstrain/rubella/tree/main/nextclade> |
| path      | `nextstrain/rubella/E1`                                     |

## Scope of this dataset

This dataset assigns genotypes to rubella virus sequences according to the WHO nomenclature in [Rubella virus nomenclature update: 2013][]. The nomenclature recognizes 12 genotypes (1B to 1J and 2A to 2C) and the provisional genotype 1a, which this dataset labels `1A`. WHO genotype assignment requires the sequence of the 739 nucleotide genotyping window in the E1 gene, which encodes the E1 envelope glycoprotein. Sequences that the dataset places outside all labeled genotypes receive the label `unassigned`. These include some genotype 1a viruses, such as the WHO reference viruses AF188704 and M30776.

The reference sequence is the E1 gene of strain F-Therien (positions 8258 to 9700 of NC_001545.2). The genotyping window is at positions 474 to 1212 of this reference. The dataset reports mutations in the E1 protein.

Sequence data outside the E1 gene, for example in complete genomes, is reported as an insertion. For complete genomes, use the `nextstrain/rubella/genome` dataset, which reports mutations in the non-structural polyprotein (NSP) and in the structural polyprotein (SP).

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html>

[Rubella virus nomenclature update: 2013]: https://www.who.int/publications/i/item/WER8832
