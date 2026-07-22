# Coxsackievirus A10 dataset

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Nadia Neuner-Jehle](https://eve-lab.org/people/nadia-neuner), [Emma B. Hodcroft](https://eve-lab.org/people/emma-hodcroft/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)                                                 |
| name                 | Coxsackievirus A10                                                    |
| reference            | [AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767.1)         |
| workflow             | <https://github.com/enterovirus-phylo/nextclade_a10>                  |
| path                 | `enpen/enterovirus/cva10`                                             |
| clade definitions    |  A-H                                                                  |

## Scope of this dataset

This dataset uses the [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_a10/blob/master/resources/inferred-root.fasta) instead of the historical Kowalik prototype sequence ([AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767.1)). It is intended for broad subgenogroup classification, mutation quality control, and phylogenetic analysis of CVA10 diversity.

***Note:** Kowalik reference sequence is substantially diverged from currently circulating strains. This is common for many enterovirus datasets, in contrast to some other virus datasets (e.g., seasonal influenza) where the reference is updated more frequently to match recent sequences.*

To address this, the dataset is *rooted* on a Static Inferred Ancestor, a phylogenetically reconstructed ancestral sequence near the tree root. This provides a stable reference point that can be used as an alternative for mutation calling.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Coxsackievirus A10

Coxsackievirus A10 is divided into subgenogroups A, B, C, D, E (VP1 only), F, G and H (VP1 only).

***Note:** Genotypes E and H are based on VP1 sequences only.*

Overall, these designations are based on phylogenetic structure and characteristic mutations, and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses. Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universally standardized global lineage nomenclature for enteroviruses; naming instead follows conventions established in published studies and surveillance practices.

## Related Enteroviruses
CVA2
CVA4
CVA5
CVA3
CVA8
CVA10 is closely related to other EV-A viruses, including CVA8, CVA16, and EV-A71. If you are not certain that your sequences contain only CVA10, we recommend using the "[Multiple Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-web/getting-started.html#multi-dataset-mode)" tab instead of "Single Dataset".

This prevents Nextclade from forcing sequences to align to the CVA10 reference tree. For example, EV-A71 sequences may still align and receive a clade assignment (often near recombinant forms).

Please be cautious when working with short genes or fragments (e.g., 5'UTR sequences). These regions can be highly conserved across EV-A viruses, making genogroup and subgenogroup assignment prone to errors. In addition, such fragments may originate from recombinant genomes. Recombination is common in enteroviruses, and when analyzing only a fragment, this may go undetected.

If you are unsure how to proceed, please contact us. We are happy to assist.

## Reference types

This dataset includes several reference points used in analyses:

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, representing the likely founder of CVA10. Serves as a stable reference.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., A, B). Mutations "since clade founder" describe changes that define that clade.

- *Reference:* RefSeq or similarly established prototype sequence. Here Kowalik (AY421767.1).

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the Kowalik sequence.

## Issues & Contact

- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_a10/issues) or email: eve-group[at]swisstph.ch

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
