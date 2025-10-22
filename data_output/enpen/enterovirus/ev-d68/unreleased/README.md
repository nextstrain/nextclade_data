# Enterovirus D68 dataset with reference Fermon

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Nadia Neuner-Jehle](https://www.swisstph.ch/en/staff/profile/people/nadia-neuner-jehle), [Emma B. Hodcroft](http://emmahodcroft.com/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)                                                 |
| name                 | Enterovirus D68                                                       |
| reference            | [AY426531.1](https://www.ncbi.nlm.nih.gov/nuccore/AY426531.1)         |
| workflow             | https://github.com/enterovirus-phylo/nextclade_d68                    |
| path                 | `TBD`                                                                 |
| clade definitions    |  A–C (D)                                                              |

## Scope of this dataset

Based on the full genome sequence, this dataset uses the Fermon reference sequence ([AY426531.1](https://www.ncbi.nlm.nih.gov/nuccore/AY426531.1)), originally isolated in 1962. It provides a framework for quality control, clade assignment, and mutation calling across global EV-D68 diversity.

***Note:** The Fermon reference is substantially diverged from currently circulating strains. This is common for many enterovirus datasets, in contrast to some other virus datasets (e.g., seasonal influenza) where the reference is updated more frequently to match recent sequences.*

To address this, we also provide an **Static inferred ancestor**: a phylogenetically reconstructed ancestral sequence representative of the diversity in this dataset, which can serve as an alternative reference for analyses and improve interpretation of recent strains.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Enterovirus D68

EV-D68 is divided into three clades: A (A1–A2), B (B1–B3) and C. Clade A2 is sometimes referred to as clade D.

These designations are based on phylogenetic structure and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses.  
Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universal, standardized global lineage nomenclature for enteroviruses — naming follows conventions from published studies and surveillance practice.

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).