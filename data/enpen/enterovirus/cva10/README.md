# Coxsackievirus A10 dataset with reference Kowalik

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Nadia Neuner-Jehle](https://eve-lab.org/people/nadia-neuner), [Emma B. Hodcroft](https://eve-lab.org/people/emma-hodcroft/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)                                                 |
| name                 | Coxsackievirus A10                                                        |
| reference            | [AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767.1)         |
| workflow             | <https://github.com/enterovirus-phylo/nextclade_a10>                          |
| path                 | `enpen/enterovirus/cva10`                                                                 |
| clade definitions    |  A-H                                                                  |

## Scope of this dataset

Based on the full genome sequence, this dataset uses the **Kowalik prototype sequence** ([AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767.1)), originally isolated in 1950. It provides a framework for quality control, clade assignment, and mutation calling across global CVA10 diversity.

***Note:** Kowalik reference sequence is substantially diverged from currently circulating strains. This is common for many enterovirus datasets, in contrast to some other virus datasets (e.g., seasonal influenza) where the reference is updated more frequently to match recent sequences.*

To address this, the dataset is *rooted* on a Static Inferred Ancestor — a phylogenetically reconstructed ancestral sequence near the tree root. This provides a stable reference point that can be used, optionally, as an alternative for mutation calling.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Coxsackievirus A10

Coxsackievirus A10 is divided into subgenogroups A, B, C, D, E (VP1 only), F, G and H (VP1 only).

***Note:** Genotypes E and H are based on VP1 sequences only.*

These designations are based on the phylogenetic structure and mutations, and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses. Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universal, standardized global lineage nomenclature for enteroviruses. Naming follows conventions from published studies and surveillance practices.

## Reference types

This dataset includes several reference points used in analyses:

- *Reference:* RefSeq or similarly established reference sequence. Here Kowalik.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., A, B). Mutations "since clade founder" describe changes that define that clade.

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, representing the likely founder of Coxsackievirus A10. Serves as a stable reference.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the Kowalik sequence.

## Issues & Contact

- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_a10/issues) or email: eve-group[at]swisstph.ch.

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
