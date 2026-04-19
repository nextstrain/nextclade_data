# Coxsackievirus A16 dataset

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Nadia Neuner-Jehle](https://eve-lab.org/people/nadia-neuner-jehle/), [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Emma B. Hodcroft](https://eve-lab.org/people/emma-hodcroft/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)                                                 |
| name                 | Coxsackievirus A16                                                     |
| reference            | [ancestral sequence](https://github.com/enterovirus-phylo/nextclade_a16/blob/master/resources/inferred-root.fasta)               |
| workflow             | https://github.com/enterovirus-phylo/nextclade_a16                          |
| path                 | `enpen/enterovirus/cva16`                                                                 |
| clade definitions    | A–F                                                                   |

## Scope of this dataset

This dataset uses the [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_a16/blob/master/resources/inferred-root.fasta) instead of the historical G-10 prototype sequence ([U05876.1](https://www.ncbi.nlm.nih.gov/nuccore/U05876)). It is intended for broad subgenogroup classification, mutation quality control, and phylogenetic analysis of CVA16 diversity.

*Note: The G-10 reference differs substantially from currently circulating strains.* This is common for enterovirus datasets, in contrast to some other virus datasets (e.g., seasonal influenza), where the reference is updated more frequently to reflect recent lineages.

To address this, the dataset is *rooted* on a Static Inferred Ancestor, a phylogenetically reconstructed ancestral sequence near the tree root. This provides a stable reference point that can be used as an alternative for mutation calling.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Coxsackievirus A16

Subgenogroups B1a, B1b and B1c represent the major phylogenetic divisions of CVA16 and are commonly used in virological surveillance and the literature. They are defined based on phylogenetic clustering and do not necessarily reflect antigenic differences. 

In recent years, additional recombinant forms have been identified and labeled C-F (also referred to as B2, B3, and D). These recombinant forms cluster with the prototype strain (clade A).

Overall, these designations are based on phylogenetic structure and characteristic mutations, and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses. Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universally standardized global lineage nomenclature for enteroviruses; naming instead follows conventions established in published studies and surveillance practices.

## Related Enteroviruses

CVA16 is closely related to other EV-A viruses, including EV-A71, EV-A120, and CVA5. If you are not certain that your sequences contain only CVA16, we recommend using the "[Multiple Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-web/getting-started.html#multi-dataset-mode)" tab instead of "Single Dataset".

This prevents Nextclade from forcing sequences to align to the CVA16 reference tree. For example, EV-A71 sequences may still align and receive a clade assignment (often near recombinant forms).

Please be cautious when working with short genes or fragments (e.g., 5'UTR sequences). These regions can be highly conserved across EV-A viruses, making genogroup and subgenogroup assignment prone to errors. In addition, such fragments may originate from recombinant genomes. Recombination is common in enteroviruses, and when analyzing only a fragment, this may go undetected.

If you are unsure how to proceed, please contact us. We are happy to assist.

## Reference types

This dataset includes several reference points used in analyses:
- *Reference:* RefSeq or similarly established prototype sequence. Here G-10.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., B1a, B2). Mutations "since clade founder" describe changes that define that clade.

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, representing the likely founder of CVA16. Serves as a stable reference.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the G-10 sequence.

## Issues & Contact
- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_a16/issues) or email: eve-group[at]swisstph.ch

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
