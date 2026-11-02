# Rubella virus (complete genome) dataset

| Key       | Value                                   |
| --------- | --------------------------------------- |
| name      | Rubella virus complete genome           |
| authors   | [Nextstrain](https://nextstrain.org)    |
| reference | NC_076948.1                             |
| workflow  | <https://github.com/nextstrain/rubella> |
| path      | `nextstrain/rubella/genome`             |

## Scope of this dataset

This dataset assigns genotypes to rubella virus samples based on the WHO nomenclature in [Rubella virus nomenclature update: 2013][]. The nomenclature defines 13 genotypes, 1A to 1J and 2A to 2C, from a 739 nucleotide window of the E1 gene, which encodes one of the two envelope glycoproteins.

The reference tree is built from complete rubella virus genomes. The reference sequence is the complete genome of strain RVi/Bismarck.ND.USA/23.08/2B (genotype 2B). The genotypes on the tree are defined by nucleotide changes in the E1 gene, so they follow the WHO definition.

The dataset aligns sequences against the complete genome and reports mutations in the non-structural polyprotein (NSP) and in the structural polyprotein (SP). For sequences that cover only the E1 region, use the `nextstrain/rubella/E1` dataset.

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html>

[Rubella virus nomenclature update: 2013]: https://www.who.int/publications/i/item/WER8832
