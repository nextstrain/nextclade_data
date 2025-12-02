# Nextclade dataset for HAV using whole genome human host GenBank sequences with reference NC_001489.1

## Dataset Attributes

| Attribute            | Value                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Name                 | Hepatitis A human host GenBank WGS                                                                               |
| Authors              | Lydia A. Krasilnikova (MASPHL), Mary Godec (MASPHL), Matthew Doucette (MASPHL), Daniel J. Park (Broad Institute) |
| Contact              | dph-bidls-genomics[at]mass[dot]gov                                                                               |
| Data source          | [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) accessed 2025-02-03                                             |
| Reference            | [NC_001489.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001489.1)                                                  |
| Dataset path         | community/masphl-bioinformatics/hav/whole-genome                                                                 |

## Scope of this dataset

This dataset includes human host HAV clades IA, IB, IIA, IIB, IIIA, and IIIB and is suitable for analysis of human host HAV sequences of any length covering any region. There are no whole-genome IC sequences available on GenBank; as a result, IC sequences classified using this dataset may be mis- or unassigned. The VP1-2B junction region Nextclade dataset (community/masphl-bioinformatics/hav/vp1-2b-junction) should be used for analysis of IC sequences.

## Annotations used for this dataset

Note that current Refseq annotations are incorrect for the HAV reference genome as of October 2025. Annotations for this dataset were sourced from Table 1 in [Nainan et al 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC1360271/#t1).

## Sequences included in this dataset

This dataset includes all human host whole genome HAV GenBank sequences. First, all Hepatovirus A GenBank sequences were produced by search term [txid12092\[Organism:exp\]](https://www.ncbi.nlm.nih.gov/nuccore/?term=txid12092[Organism:exp]), accessed 2025-02-03. Sequences were filtered to those with ≥7,125 unambiguous bases (≥95% HAV genome). Sequences were further filtered to human host, using the host field or, when the host field was blank, the isolation_source field and the associated publication(s) in the title field. Sequences for which the host field was blank that were passaged through animals or cell lines were excluded.

## Clade assignment of sequences included in this dataset

A preliminary Nextclade dataset was generated using unpublished CDC GHOST reference sequences (VP1-2B junction region only) of clades IA, IB, IC, IIA, and IIIA along with the VP1-2B junction region of representative GenBank sequences of clades IIB ([AY644670.1](https://www.ncbi.nlm.nih.gov/nuccore/AY644670.1)) and IIIB ([AB279735.1](https://www.ncbi.nlm.nih.gov/nuccore/AB279735.1)). This preliminary dataset was used for clade assignment of sequences included in this dataset.

## Phylogeny used in this dataset

The phylogeny used in this dataset was generated with IQ-TREE with 1000 bootstraps using the Jukes-Cantor (JC) model. The phylogeny was rooted using the nearest non-human host outgroup with no clade assigned in the previous section, [OR452341.1](https://www.ncbi.nlm.nih.gov/nuccore/OR452341.1) (not included in this dataset). This tool, model, and rooting was chosen to match that used in the VP1-2B junction region Nextclade dataset (community/masphl-bioinformatics/hav/vp1-2b-junction).

## Validation of this dataset

Unpublished CDC GHOST reference sequences (VP1-2B junction region only) of clades IA, IB, IC, IIA, and IIIA along with the VP1-2B junction region of representative GenBank sequences of clades IIB ([AY644670.1](https://www.ncbi.nlm.nih.gov/nuccore/AY644670.1)) and IIIB ([AB279735.1](https://www.ncbi.nlm.nih.gov/nuccore/AB279735.1)) were analyzed using this dataset. Clade assignment matched that expected, with the exception that the only IC sequence included in the CDC GHOST reference sequences was misclassified as IA (this dataset does not classify IC).

## What is a Nextclade dataset?

Read more about Nextclade datasets in the [Nextclade documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
