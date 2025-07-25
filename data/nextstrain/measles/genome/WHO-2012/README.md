# Measles dataset

| Key               | Value                                                                         |
| ----------------- | ----------------------------------------------------------------------------- |
| name              | Measles complete genome                                                       |
| authors           | [Nextstrain](https://nextstrain.org)                                          |
| reference         | NC_001498.1                                                                   |
| workflow          | https://github.com/nextstrain/measles/tree/main/nextclade                     |
| path              | `nextstrain/measles/genome/WHO-2012`                                          |


## Scope of this dataset

This dataset assigns genotypes to measles samples based on [criteria outlined by the WHO](https://www.who.int/publications/i/item/WER8709).

The WHO has defined 24 measles genotypes based on N gene and H gene sequences from 28 reference strains based on a short 450 bp segment of the viral genome.
The reference tree used in this dataset includes sequences for the 28 reference strains and a selection of (nearly) complete genomes for most genotypes.
Most major genotypes are well represented by complete genomes in resulting tree and the major genotypes form well-defined monophyletic clades.
Some rare or older genotypes are only represented by short genome segments covering the N450 region.

This Nextclade dataset can assign genotypes using any sufficiently long (a few hundred bases) part of the measles virus genome as long as the corresponding genotype is represented by full genomes.
To assign genotypes that lack full genomes, coverage of the N450 region is required.

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Notes
Some genotypes defined by the WHO lack publicly available complete genome sequences. To represent these genotypes in this whole genome Nextclade dataset, we used partial sequences. As a result, mutation calls relative to clade (genotype) founders for these sequences will include additional mutations.


## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
