# Nextclade dataset for HAV using the VP1-2B junction region of human host GenBank sequences with reference NC_001489.1

## Dataset Attributes

| Attribute            | Value                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Name                 | Hepatitis A human host GenBank VP1-2B junction sequences                                                         |
| Authors              | Lydia A. Krasilnikova (MASPHL), Mary Godec (MASPHL), Matthew Doucette (MASPHL), Daniel J. Park (Broad Institute) |
| Contact              | dph-bidls-genomics[at]mass[dot]gov                                                                               |
| Data source          | [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) accessed 2025-02-03                                             |
| Reference            | [NC_001489.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001489.1)                                                  |
| Dataset path         | community/masphl-bioinformatics/hav/vp1-2b-junction                                                              |

## Scope of this dataset

This dataset includes human host HAV clades IA, IB, IC, IIA, IIB, IIIA, and IIIB and is suitable for analysis of human host HAV sequences of any length as long as they include the VP1-2B junction region; however, it is best suited for analysis of VP1-2B junction region sequences.

## About the VP1-2B junction region

The HAV VP1-2B junction region covers positions 2,968 through 3,322, 1-indexed, relative to reference [NC_001489.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001489.1). It is used for analysis including clade assignment by CDC GHOST.

## Annotations used for this dataset

Note that current Refseq annotations are incorrect for the HAV reference genome as of October 2025. Annotations for this dataset were sourced from Table 1 in [Nainan et al 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC1360271/#t1).  For this VP1-2B junction dataset, the region includes a portion of both 1D, the complete "2A" (better known now as pX per [Shirasaki et al 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9410543/#sec012)), and a portion of 2B. Both 1D and 2B are listed as "truncated" in the annotations. Note that per Nextclade constraints requiring CDS length to be a multiple of 3, the truncated 2B ends at position 348 (1-indexed).

## Sequences included in this dataset

This dataset includes all human host VP1-2B junction region HAV GenBank sequences. First, all Hepatovirus A GenBank sequences were produced by search term [txid12092\[Organism:exp\]](https://www.ncbi.nlm.nih.gov/nuccore/?term=txid12092[Organism:exp]), accessed 2025-02-03. Sequences were filtered to those fully overlapping the VP1-2B junction region. Sequences were further filtered to human host, using the host field or, when the host field was blank, the isolation_source field and the associated publication(s) in the title field. Sequences for which the host field was blank that were passaged through animals or cell lines were excluded. The VP1-B junction region was retrieved for all included sequences and used for dataset generation.

## Clade assignment of sequences included in this dataset

A preliminary Nextclade dataset was generated using unpublished CDC GHOST reference sequences (VP1-2B junction region only) of clades IA, IB, IC, IIA, and IIIA along with the VP1-2B junction region of representative GenBank sequences of clades IIB ([AY644670.1](https://www.ncbi.nlm.nih.gov/nuccore/AY644670.1)) and IIIB ([AB279735.1](https://www.ncbi.nlm.nih.gov/nuccore/AB279735.1)). This preliminary dataset was used for clade assignment of sequences included in this dataset.

## Phylogeny used in this dataset

The phylogeny used in this dataset was generated with IQ-TREE with 1000 bootstraps using the Jukes-Cantor (JC) model. The phylogeny was rooted using the nearest non-human host outgroup with no clade assigned in the previous section, [OR452341.1](https://www.ncbi.nlm.nih.gov/nuccore/OR452341.1) (not included in this dataset). This was the tool, model, and rooting that produced branches with defining mutations for all clades IA, IB, IC, IIA, IIB, IIIA, and IIIB.

## Validation of this dataset

Unpublished CDC GHOST reference sequences (VP1-2B junction region only) of clades IA, IB, IC, IIA, and IIIA along with the VP1-2B junction region of representative GenBank sequences of clades IIB ([AY644670.1](https://www.ncbi.nlm.nih.gov/nuccore/AY644670.1)) and IIIB ([AB279735.1](https://www.ncbi.nlm.nih.gov/nuccore/AB279735.1)) were analyzed using this dataset. Clade assignment matched that expected.

## What is a Nextclade dataset?

Read more about Nextclade datasets in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
