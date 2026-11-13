# Hepatitis C virus dataset (all genotypes) with reference H77

| Key               | Value                                                                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name              | Hepatitis C virus (all genotypes)                                                                                                                                                                                    |
| authors           | [Richard Neher](https://neherlab.org), [Duyen Bao Le](https://www.uniklinik-duesseldorf.de/institut-fuer-virologie/forschung/ag-timm/team), [Stefannie Hoffmann](https://www.uniklinik-duesseldorf.de/institut-fuer-virologie/forschung/ag-timm/team), [Andreas Wagner](https://www.uniklinik-duesseldorf.de/institut-fuer-virologie/forschung/ag-timm/team)                                                                    |
| reference         | `NC_038882.1` (isolate H77, genotype 1a)                                                                                                                                                                             |
| workflow          | TODO                                                                                                                                                                                                                 |
| path              | TODO                                                                                                                                                                                                                 |
| clade definitions | HCV genotypes and subtypes following the ICTV consensus classification ([Smith et al., 2014](https://doi.org/10.1002/hep.26744); genotype 8: [Borgia et al., 2018](https://doi.org/10.1093/infdis/jiy401))          |

## Scope of this dataset

This dataset assigns genotypes and subtypes to hepatitis C virus (HCV)
sequences of all known genotypes (1–8), and reports mutations relative to the
H77 reference (`NC_038882.1`, genotype 1a).

HCV is highly diverse: genotypes differ by more than 30% and subtypes by
15–30% at the nucleotide level. Since all sequences are aligned against a
single genotype 1a reference, sequences of other genotypes will show many
mutations relative to the reference. Highly variable and gap-rich regions of
the alignment (e.g. in NS5A and the 3' end) are excluded from phylogenetic
placement.

The dataset is designed for near full-length genomes or sequences spanning
the complete coding region. TODO: describe performance on partial sequences
(e.g. NS5B, core/E1 or E2 fragments).

## Reference sequence and reference tree

The reference sequence is the RefSeq `NC_038882.1` of isolate H77 (genotype
1a). Amino acid mutations are reported for the mature proteins core, E1, E2,
p7, NS2, NS3, NS4A, NS4B, NS5A and NS5B.

The reference tree contains near full-length genomes from GenBank, sampled
evenly across genotypes and subtypes. Genotypes and subtypes of the tips are
based on the NCBI taxonomy; clades in the tree are defined by the most recent
common ancestor of all tips of a genotype or subtype.

## Features

This dataset supports:

- Assignment of genotypes (`clade`)
- Assignment of subtypes (`subtype`)
- Phylogenetic placement
- Sequence quality control (QC)

## Genotypes and subtypes

HCV is classified into 8 genotypes and more than 90 subtypes. Genotypes are
labeled by numbers (1–8) and subtypes by a genotype number followed by a
letter (e.g. 1a, 3b). The genotype is reported in the `clade` column and the
subtype in the `subtype` column of the Nextclade output.

Subtypes that are rare in public databases may be represented by few
sequences in the reference tree, or not at all. Sequences of such subtypes
are assigned the genotype, but may not get a subtype assignment.
Recombinant viruses (e.g. 2k/1b) are not labeled as such and are assigned
the genotype and subtype of their closest relative in the tree.

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation:
<https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html>
