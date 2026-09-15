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

This dataset uses a [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_a10/blob/master/resources/inferred-root.fasta) rather than the historical Kowalik prototype sequence ([AY421767.1](https://www.ncbi.nlm.nih.gov/nuccore/AY421767)). The inferred ancestor represents the reconstructed common ancestor of contemporary CVA10 diversity. It serves as the reference for sequence alignment and it is used to root the reference tree. Kowalik serves as the default reference for mutation calling on Nextclade Web.

This dataset is intended for subgenotype assignment, mutation analysis, sequence quality control, and phylogenetic placement of CVA10 genomes.

*The Kowalik prototype differs substantially from currently circulating CVA10 strains.* Unlike viruses such as seasonal influenza, where reference sequences are updated regularly, enterovirus analyses have traditionally relied on historical prototype sequences. Using an inferred ancestral sequence instead provides a stable reference that is genetically closer to circulating viruses while remaining independent of any extant lineage.

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

CVA10 is closely related to other EV-A viruses, including CVA8, CVA16, and EV-A71. If you are not certain that your sequences contain only CVA10, we recommend using the "[Multiple Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-web/getting-started.html#multi-dataset-mode)" tab instead of "Single Dataset".

This allows Nextclade to select the most appropriate dataset instead of forcing all sequences onto the CVA10 reference tree. For example, CVA16 sequences may still align and receive a clade assignment (often near recombinant forms).

Please be cautious when working with short genes or fragments (e.g., 5'UTR sequences). These regions can be highly conserved across EV-A viruses, making genogroup and subgenogroup assignment prone to errors. In addition, such fragments may originate from recombinant genomes. Recombination is common in enteroviruses, and when analyzing only a fragment, this may go undetected.

If you are unsure how to proceed, please contact us. We are happy to assist.

## Reference types

This dataset includes several reference points used in analyses:

- *Reference:* RefSeq or similarly established prototype sequence. Here Kowalik (AY421767.1).

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, used to root the tree and serving as the default reference for mutation calling. Appears in the tree as the rooting outgroup, not as the tree's root node itself — see *Tree root*.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., B5, C4). Mutations "since clade founder" describe changes that define that clade.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the Kowalik sequence.

## Issues & Contact

- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_a10/issues) or email: eve-group[at]swisstph.ch

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
