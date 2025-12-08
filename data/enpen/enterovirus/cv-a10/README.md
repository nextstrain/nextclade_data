# Coxsackievirus A10 dataset based on reference "Kowalik"

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Nadia Neuner-Jehle](https://www.swisstph.ch/en/staff/profile/people/nadia-neuner-jehle), [Emma B. Hodcroft](http://emmahodcroft.com/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)     |
| name                 | Coxsackievirus A10                                                     |
| reference            | [AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767)               |
| workflow             | https://github.com/hodcroftlab/nextclade_a10                          |
| path                 | `TBD`                                                                 |
| clade definitions    | B-D, F-G                                                                   |

## Scope of this dataset

Based on full-genome sequences, this dataset uses the historical **Kowalik reference sequence** ([AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767)). It is intended for broad subgenogroup classification, mutation quality control, and phylogenetic analysis of CV-A10 diversity.

*Note: The Kowalik reference differs substantially from currently circulating strains.* This is common for enterovirus datasets, in contrast to some other virus datasets (e.g., seasonal influenza), where the reference is updated more frequently to reflect recent lineages.

To address this, the dataset is rooted on a Static Inferred Ancestor — a phylogenetically reconstructed ancestral sequence near the tree root. This provides a stable reference point that can be used, optionally, as an alternative for mutation calling.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Cocksackievirus A10

Clade designations follow major phylogenetic divisions within CV-A10, commonly used in virological surveillance and literature. The label "G/C" indicates sequences that could not be assigned to either C or G, but they cluster next to both clades. Clades designations are defined by phylogenetic clustering and do not necessarily indicate antigenic differences.

*Note: Clades A and E have no whole genome representative sequence and have not been included in this dataset.*

These designations are based on the phylogenetic structure and mutations, and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses. Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universal, standardized global lineage nomenclature for enteroviruses. Naming follows conventions from published studies and surveillance practices.

## Reference types

This dataset includes several reference points used in analyses:
- *Reference:* RefSeq or similarly established reference sequence. Here Kowalik.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., C, D). Mutations "since clade founder" describe changes that define that clade.

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, representing the likely founder of CV-A10. Serves as a stable reference.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

## Issues & Contact
- For questions or suggestions, please [open an issue](https://github.com/hodcroftlab/nextclade_a10/issues) or email: eve-group[at]swisstph.ch


## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, gene annotations, a phylogenetic tree, and QC configuration. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).