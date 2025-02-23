# H5Nx clade `2.3.2.1` dataset with A/duck/Vietnam/NCVD-1584/2012 reference

| attribute            | value                                    |
| -------------------- | ---------------------------------------- |
| authors              |[Jordan Ort](https://lmoncla.github.io/monclalab/team/JordanOrt/), [Louise Moncla](https://lmoncla.github.io/monclalab/team/LouiseMoncla/)|
| dataset name         | H5Nx clade `2.3.2.1` (provisional)         |
| reference strain     | A/duck/Vietnam/NCVD-1584/2012(H5N1)      |
| reference accession  | EPI424984                                |


## Authors and contacts

Maintained by: [Jordan Ort](https://lmoncla.github.io/monclalab/team/JordanOrt/)

With the help from: [Louise Moncla](https://lmoncla.github.io/monclalab/team/LouiseMoncla/), Todd Davis, Tommy Lam, Samuel Shephard, Richard Neher

## Scope of this dataset
This dataset uses a current H5 candidate vaccine virus (CVV) from clade `2.3.2.1` (A/duck/Vietnam/NCVD-1584/2012) as a reference and is suitable for the analysis of H5 sequences belonging to clade `2.3.2.1` and its sub-clades `2.3.2.1a` through `2.3.2.1g`. Sequences belonging to other clades cannot be annotated by this dataset and will be left `unassigned`.

## Features
This dataset supports

 * Assignment to clades and subclades based on the provisional nomenclature defined by the WHO/FAO/WOAH H5 Nomenclature Working Group
 * Sequence quality control (QC)
 * Phylogenetic placement
 * Annotations for glycosylation sties, HA cleavage site sequence, and presence/absence of a polybasic cleavage site

## Clades of H5Nx avian influenza viruses

The WHO/FAO/WOAH H5 Nomenclature Working Group define "clades" using HA gene seguences, and define clades as genetically distinct, monophyletic groups of viruses. Viruses falling into a given clade share a common ancestor with significant bootstrap support and have low levels of within-clade diversity. [Past nomenclature updates](https://onlinelibrary.wiley.com/doi/10.1111/irv.12324) have required viruses in the same clade to be monophyletic with bootstrap suppor of at least 60%, with within-clade pairwise distances of less than 1.5%. These requirements are sometimes relaxed, and clades are periodically updated to account for expanding viral diversity.

Clade `2.3.2.1` viruses and their descendants have circulated since 2007 and are endemic in Southeast Asia. These viruses have diversified into eight additional sub-clades, named `2.3.2.1a` through `2.3.2.1g` due to high circulating diversity within the clade.
This Nextclade dataset incorporates these provisional `2.3.2.1` sub-clades.

## Alternative, and complementary approaches for H5 clade assignment
Two additional tools exist for assigning clades to H5 viruses that accommodate the recent `2.3.2.1` clade splits.

1. [LABEL](https://wonder.cdc.gov/amd/flu/label/): this command-line tool is built and maintained by Sam Shepard, and performs clade assignment for all current `2.3.4.4` and `2.3.2.1` clade splits.
2. [BVBRC Subspecies Classification Tool](https://www.bv-brc.org/app/SubspeciesClassification): this is a drag and drop tool that classifies a variety of viruses, including influenza A H1N1, H3N2, and H5N1.

The clade assignments in this Nextclade dataset were validated against LABEL assignments and shown to be generally well-matched across subclades. The figure below shows a direct comparison of assignments for 1671 HA sequences from GISAID, performed using LABEL and this NextClade dataset for clade `2.3.2.1` and its subclades.

![Figure 1: Comparison between LABEL and Nextclade for 2.3.2.1 assignments](https://raw.githubusercontent.com/moncla-lab/h5nx-Clades/main/jordan-h5-clades/testing-nextclade-datasets/2321/files/20240430_2321.png)

## What is Nextclade dataset

Read more about Nextclade datasets in Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html