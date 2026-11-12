# Enterovirus D68 dataset with reference Fermon

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Nadia Neuner-Jehle](https://eve-lab.org/people/nadia-neuner-jehle/), [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Emma B. Hodcroft](https://eve-lab.org/people/emma-hodcroft/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/)                                |
| name                 | Enterovirus D68                                                       |
| reference            | [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_d68/blob/master/resources/inferred-root.fasta)               |
| workflow             | <https://github.com/enterovirus-phylo/nextclade_d68>                  |
| path                 | `enpen/enterovirus/ev-d68`                                            |
| clade definitions    | A–C (D)                                                               |

## Citation

If you use this dataset in your research, please cite:

> Neuner-Jehle, N., González Sánchez, A., Hodcroft, E. B., & European Non-Polio Enterovirus Network (ENPEN). (2025). *enterovirus-phylo/nextclade_d68: Enterovirus D68 Nextclade Dataset v1.0.0* (v1.0.0--2025-11-18). Zenodo. <https://doi.org/10.5281/zenodo.17642338>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17642338.svg)](https://doi.org/10.5281/zenodo.17642338)

## Scope of this dataset

This dataset uses a [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_d68/blob/master/resources/inferred-root.fasta) rather than the RefSeq Fermon ([AY426531](https://www.ncbi.nlm.nih.gov/nuccore/AY426531)). The inferred ancestor represents the reconstructed common ancestor of contemporary EV-D68 diversity. It serves as the reference for sequence alignment and it is used as the root sequence for the reference tree. Fermon serves as the default reference for mutation calling on Nextclade Web.

This dataset is intended for subgenotype assignment, mutation analysis, sequence quality control, and phylogenetic placement of EV-D68 genomes.

*The Fermon reference differs substantially from currently circulating EV-D68 strains.* Unlike viruses such as seasonal influenza, where reference sequences are updated regularly, enterovirus analyses have traditionally relied on historical prototype sequences. Using an inferred ancestral sequence instead provides a stable reference that is genetically closer to circulating viruses while remaining independent of any extant lineage.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenogroups of Enterovirus D68

Clade designations follow the global diversity of EV-D68: A (A1–A2/D), B (B1–B3), and C. The label "pre-ABC" indicates old, basal lineages that are no longer circulating. Sequences labeled "pre-ABC" or "unassigned" may indicate sequencing or assembly issues and should be assessed carefully.

These designations are based on the phylogenetic structure and mutations, and are widely used in molecular epidemiology, similar to subgenotype systems for other enteroviruses. Unlike influenza (H1N1, H3N2) or SARS-CoV-2, there is no universal, standardized global lineage nomenclature for enteroviruses. Naming follows conventions from published studies and surveillance practices.

## Reference types

This dataset includes several reference points used in analyses:

- *Reference:* RefSeq or similarly established reference sequence. Here Fermon.

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, representing the likely founder of EV-D68. Serves as a stable reference.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., A2, B3). Mutations "since clade founder" describe changes that define that clade.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the Fermon sequence.

## Issues & Contact

- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_d68/issues) or email: eve-group[at]swisstph.ch

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).