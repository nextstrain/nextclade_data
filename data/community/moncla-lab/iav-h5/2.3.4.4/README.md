# H5Nx clade `2.3.4.4` dataset with A/Astrakhan/3212/2020 reference

| attribute            | value                                    |
| -------------------- | ---------------------------------------- |
| authors              |[Jordan Ort](https://lmoncla.github.io/monclalab/team/JordanOrt/), [Louise Moncla](https://lmoncla.github.io/monclalab/team/LouiseMoncla/)|
| dataset name         | H5Nx clade `2.3.4.4` (provisional)         |
| reference strain     | A/Astrakhan/3212/2020(H5N8)              |
| reference accession  | EPI1846961                               |


## Authors and contacts

Maintained by: [Jordan Ort](https://lmoncla.github.io/monclalab/team/JordanOrt/)

With the help from: [Louise Moncla](https://lmoncla.github.io/monclalab/team/LouiseMoncla/), Todd Davis, Tommy Lam, Samuel Shephard, Richard Neher

## Scope of this dataset
This dataset uses a current H5 candidate vaccine virus (CVV) from clade `2.3.4.4` (A/Astrakhan/3212/2020) as a reference and is suitable for the analysis of H5 sequences belonging to clade `2.3.4.4` and its sub-clades `2.3.4.4a` through `2.3.4.4h`. Sequences belonging to other clades cannot be annotated by this dataset and will be left `unassigned`.

## Features
This dataset supports

 * Assignment to clades and subclades based on the provisional nomenclature defined by the WHO/FAO/WOAH H5 Nomenclature Working Group
 * Sequence quality control (QC)
 * Phylogenetic placement
 * Annotations for glycosylation sties, HA cleavage site sequence, and presence/absence of a polybasic cleavage site


## Clades of H5Nx avian influenza viruses

The WHO/FAO/WOAH H5 Nomenclature Working Group define "clades" using HA gene seguences, and define clades as genetically distinct, monophyletic groups of viruses. Viruses falling into a given clade share a common ancestor with significant bootstrap support and have low levels of within-clade diversity. [Past nomenclature updates](https://onlinelibrary.wiley.com/doi/10.1111/irv.12324) have required viruses in the same clade to be monophyletic with bootstrap suppor of at least 60%, with within-clade pairwise distances of less than 1.5%. These requirements are sometimes relaxed, and clades are periodically updated to account for expanding viral diversity. 

Since 2006, clade `2.3.4.4` viruses have circulated continuously and diversified extensively into multiple sub-clades. To account for this expansion, clade `2.3.4.4` is being split into eight additional sub-clades, named `2.3.4.4a` through `2.3.4.4h` due to high circulating diversity within the clade.

This Nextclade dataset incorporates these provisional `2.3.4.4` sub-clades.

## Alternative, and complementary approaches for H5 clade assignment
Two additional tools exist for assigning clades to H5 viruses that accommodate the recent `2.3.4.4` clade splits. 

1. [LABEL](https://wonder.cdc.gov/amd/flu/label/): this command-line tool is built and maintained by Sam Shepard, and performs clade assignment for all current `2.3.4.4` and `2.3.2.1` clade splits. 
2. [BVBRC Subspecies Classification Tool](https://www.bv-brc.org/app/SubspeciesClassification): this is a drag and drop tool that classifies a variety of viruses, including influenza A H1N1, H3N2, and H5N1. 

The clade assignments in this Nextclade dataset were validated against LABEL assignments and shown to be generally well-matched across subclades. The figure below shows a direct comparison of assignments for 1883 HA sequences from GISAID, performed using LABEL and this NextClade dataset for clade `2.3.4.4` and its subclades.

![Figure 1: Comparison between LABEL and Nextclade for 2.3.2.1 assignments](https://github.com/moncla-lab/h5nx-Clades/blob/main/jordan-h5-clades/testing-nextclade-datasets/2344/files/20240430_2344.png)

## What is Nextclade dataset

Read more about Nextclade datasets in Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html