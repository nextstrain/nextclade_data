# Coxsackievirus A16 dataset based on reference "G-10"

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Nadia Neuner-Jehle](https://eve-lab.org/people/nadia-neuner-jehle/), [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Emma B. Hodcroft](https://eve-lab.org/people/emma-hodcroft/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)                                                 |
| name                 | Coxsackievirus A16                                                     |
| reference            | [U05876.1](https://www.ncbi.nlm.nih.gov/nuccore/U05876)               |
| workflow             | https://github.com/enterovirus-phylo/nextclade_a16                          |
| path                 | `enpen/enterovirus/cva16`                                                                 |
| clade definitions    | A–F                                                                   |

## Scope of this dataset

This dataset uses the historical G-10 prototype sequence ([U05876.1](https://www.ncbi.nlm.nih.gov/nuccore/U05876)), which may differ from contemporary global CVA16 strains. It is intended for broad subgenogroup classification, mutation quality control, and phylogenetic analysis of CVA16 diversity.

*Note: The G-10 reference differs substantially from currently circulating strains.* This is common for enterovirus datasets, in contrast to some other virus datasets (e.g., seasonal influenza), where the reference is updated more frequently to reflect recent lineages.

To address this, the dataset is *rooted* on a Static Inferred Ancestor — a phylogenetically reconstructed ancestral sequence near the tree root. This provides a stable reference point that can be used, optionally, as an alternative for mutation calling.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Cocksackievirus A16

Subgenogroups B1 and B2 are the major phylogenetic divisions of CVA16 and are commonly used in virological surveillance and literature. They are defined by phylogenetic clustering and do not necessarily indicate antigenic differences. In recent years, recombinant forms were identified and labeled C-F (also known as B2, B3, and D). These recombinant forms cluster with the prototype strain, clade A.

These designations are based on the phylogenetic structure and mutations, and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses. Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universal, standardized global lineage nomenclature for enteroviruses. Naming follows conventions from published studies and surveillance practices.

## Reference types

This dataset includes several reference points used in analyses:
- *Reference:* RefSeq or similarly established reference sequence. Here G-10.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., B1a, B2). Mutations "since clade founder" describe changes that define that clade.

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, representing the likely founder of CVA16. Serves as a stable reference.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the G-10 sequence.

## Issues & Contact
- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_a16/issues) or email: eve-group[at]swisstph.ch

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).