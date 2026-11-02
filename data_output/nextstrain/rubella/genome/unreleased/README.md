# Rubella virus complete genome dataset

| Key       | Value                                                                          |
| --------- | ------------------------------------------------------------------------------ |
| name      | Rubella                                                                        |
| authors   | [Nextstrain](https://nextstrain.org)                                           |
| reference | NC_076948.1                                                                    |
| workflow  | <https://github.com/nextstrain/rubella/tree/nextclade/genome/nextclade_genome> |
| path      | `nextstrain/rubella/genome`                                                    |

## Scope of this dataset

This dataset assigns genotypes to rubella virus sequences according to the WHO nomenclature in [Rubella virus nomenclature update: 2013][]. The nomenclature recognizes 12 genotypes (1B to 1J and 2A to 2C) and the provisional genotype 1a, which this dataset labels `1A`. WHO genotype assignment requires the sequence of the 739 nucleotide genotyping window in the E1 gene, which encodes the E1 envelope glycoprotein. Sequences that the dataset places outside all labeled genotypes receive the label `unassigned`. These include some genotype 1a viruses, such as the WHO reference viruses AF188704 and M30776.

The reference sequence is the complete genome of strain RVi/Bismarck.ND.USA/23.08/2B (genotype 2B). The reference tree contains the WHO reference viruses and other rubella virus sequences. Most of these sequences are complete or nearly complete genomes, and the others cover parts of the genome, such as the E1 gene or the structural polyprotein gene. The genotypes on the tree are defined by nucleotide changes in the E1 gene.

The dataset reports mutations in the non-structural polyprotein (NSP) and in the structural polyprotein (SP). It accepts complete genomes and shorter sequences, including sequences of the E1 genotyping window only. A sequence that does not cover the E1 genotyping window still receives the label of its position on the tree, but this result does not meet the WHO requirement for genotype assignment. For sequences of the E1 gene only, the `nextstrain/rubella/E1` dataset is also available.

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html>

[Rubella virus nomenclature update: 2013]: https://www.who.int/publications/i/item/WER8832
