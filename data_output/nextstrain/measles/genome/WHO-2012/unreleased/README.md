# Measles dataset

| Key               | Value                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | Measles complete genome
| authors           | [Nextstrain](https://nextstrain.org)                                            |
| reference         | NC_001498.1                                                                                                                        |
| workflow          | https://github.com/nextstrain/measles/tree/main/nextclade                                                                                     |
| path              | `nextstrain/measles/genome/WHO-2012`                                                                                                                                  |


## Scope of this dataset

This dataset assigns genotypes to measles samples based on [criteria outlined by the WHO](https://www.who.int/publications/i/item/WER8709).

The WHO has defined 24 measles genotypes based on N gene and H gene sequences from 28 reference strains. For new measles samples, genotypes can be assigned based on genetic similarity to the reference strains at the "N450" region (a 450 bp region of the N gene).

The reference tree used in this dataset includes sequences for the 28 reference strains, along with (nearly) complete genome of other representative strains for most genotype.

This dataset can be used to assign genotypes to any sequence that includes at least 400 bp of the N450 region, including whole genome sequences.

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
