# Enterovirus A71 dataset

| Key                  | Value                                                                 |
|----------------------|-----------------------------------------------------------------------|
| authors              | [Nadia Neuner-Jehle](https://eve-lab.org/people/nadia-neuner-jehle/), [Alejandra González-Sánchez](https://www.vallhebron.com/en/professionals/alejandra-gonzalez-sanchez), [Emma B. Hodcroft](https://eve-lab.org/people/emma-hodcroft/), [ENPEN](https://escv.eu/european-non-polio-enterovirus-network-enpen/) |
| name                 | Enterovirus A71                                                       |
| reference            | [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_a71/blob/master/resources/inferred-root.fasta) |
| workflow             | <https://github.com/enterovirus-phylo/nextclade_a71>                  |
| path                 | `enpen/enterovirus/ev-a71`                                            |
| clade definitions    | A–G                                                                   |

## Scope of this dataset

This dataset uses a [Static Inferred Ancestor](https://github.com/enterovirus-phylo/nextclade_a71/blob/master/resources/inferred-root.fasta) rather than the historical BrCr prototype sequence ([U22521.1](https://www.ncbi.nlm.nih.gov/nuccore/U22521)). The inferred ancestor represents the reconstructed common ancestor of contemporary EV-A71 diversity. It serves as the reference for sequence alignment and it is used to root the reference tree. BrCr serves as the default reference for mutation calling on Nextclade Web.

This dataset is intended for subgenotype assignment, mutation analysis, sequence quality control, and phylogenetic placement of EV-A71 genomes.

*The BrCr prototype differs substantially from currently circulating EV-A71 strains.* Unlike viruses such as seasonal influenza, where reference sequences are updated regularly, enterovirus analyses have traditionally relied on historical prototype sequences. Using an inferred ancestral sequence instead provides a stable reference that is genetically closer to circulating viruses while remaining independent of any extant lineage.

## Features

This dataset supports:

- Assignment of subgenotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Subgenotypes of Enterovirus A71

The subgenotypes A–G (with B and C further divided into B1–B5 and C1–C5) represent the major evolutionary lineages of EV-A71 and are widely used in molecular epidemiology and surveillance. They are defined based on phylogenetic clustering and characteristic mutations rather than antigenic properties.

Several recombinant lineages have also been described, including C1.2, C1.3, C2.2, and C2.3. These are inter-subgenotype or inter-typic recombinants whose evolutionary history cannot be accurately represented by a single phylogenetic tree. Not all currently described recombinant forms were included in the dataset, particularly single sequences or small clusters without evidence of wider circulation. Recombinant forms that are observed across multiple outbreaks may be incorporated in future dataset updates.

In the Nextclade reference tree, recombinant lineages are attached directly to the root, creating a more “star-like” topology. This keeps recombinant groups separate from the major evolutionary lineages and supports more stable clade assignment. Newly emerging recombinant forms may be placed with existing recombinant references if they are sufficiently similar, although correct assignment cannot be guaranteed.

Sequences that fall outside the diversity represented by the reference tree may still be assigned to the closest available clade based on sequence similarity and the dataset's clade-defining mutations. Therefore, an assignment does not necessarily indicate that a sequence belongs to the corresponding epidemiological lineage. Sequences that cannot be confidently assigned according to the dataset's rules are reported as `unassigned`.

The clade definitions in this dataset are based on phylogenetic structure and characteristic mutations and follow the nomenclature commonly used in the EV-A71 literature. Unlike SARS-CoV-2 or influenza viruses, enteroviruses currently lack a universally standardized lineage nomenclature.

## Related Enteroviruses

EV-A71 is closely related to other EV-A viruses, including CVA16, CVA7, and EV-A120. If your sequences may contain multiple EV-A types, we recommend using the [Multiple Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-web/getting-started.html#multi-dataset-mode) mode rather than selecting only the EV-A71 dataset.

This allows Nextclade to select the most appropriate dataset instead of forcing all sequences onto the EV-A71 reference tree. For example, CVA16 sequences may still align and receive a clade assignment (often near recombinant forms).

Please be cautious when working with short genes or fragments (e.g., 5'UTR sequences). These regions can be highly conserved across EV-A viruses, making genogroup and subgenogroup assignment prone to errors. In addition, such fragments may originate from recombinant genomes. Recombination is common in enteroviruses, and when analyzing only a fragment, this may go undetected.

If you are unsure how to proceed, please contact us. We are happy to assist.

## Reference types

This dataset includes several reference points used in analyses:

- *Reference:* RefSeq or similarly established prototype sequence. Here BrCr (U22521.1).

- *Static Inferred Ancestor:* Reconstructed ancestral sequence inferred with an outgroup, used to root the tree and serving as the default reference for mutation calling. Appears in the tree as the rooting outgroup, not as the tree's root node itself — see *Tree root*.

- *Parent:* The nearest ancestral node of a sample in the tree, used to infer branch-specific mutations.

- *Clade founder:* The inferred ancestral node defining a clade (e.g., B5, C4). Mutations "since clade founder" describe changes that define that clade.

- *Tree root:* Corresponds to the root of the tree, it may change in future updates as more data become available.

All references use the coordinate system of the BrCr sequence.

## Issues & Contact

- For questions or suggestions, please [open an issue](https://github.com/enterovirus-phylo/nextclade_a71/issues) or email: eve-group[at]swisstph.ch

## What is a Nextclade dataset?

A Nextclade dataset includes the reference sequence, genome annotations, tree, clade definitions, and QC rules. Learn more in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
