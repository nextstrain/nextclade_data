# Yellow fever virus dataset (full genome)

| Key          | Value                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| name         | Yellow Fever Virus (full genome)                                                                        |
| workflow     | <https://github.com/hodcroftlab/nextclade-yellow-fever>                                                 |
| authors      | [Hodcroft Lab](https://github.com/hodcroftlab)                                                          |
| reference    | [NC_002031.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_002031.1)                                        |
| dataset path | `community/pathoplexus/yellow-fever-virus`                                                              |

## Scope of this dataset

This dataset can be used for clade assignment of yellow fever virus samples. 
In contrast to the existing `nextstrain/yellow-fever/prM-E` dataset (which aligns only a short 600 nucleotide subsection of the yellow fever virus genome), this dataset aligns versus the full yellow fever virus genome.
It also uses the NCBI reference sequence [NC_002031.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_002031.1) instead of [AY640589.1](https://www.ebi.ac.uk/ena/browser/view/AY640589).

### Clade system

Since the clade system described in `nextstrain/yellow-fever/prM-E` maps well onto the tree produced by this dataset, it is used for clade assignment here as well.
The system is based on strain and genotype information from [Mutebi et al.][] (J Virol. 2001 Aug;75(15):6999-7008) and [Bryant et al.][] (PLoS Pathog. 2007 May 18;3(5):e75), and consists of seven clades:

| Clade     | Genotype            |
|-----------|---------------------|
| Clade I   | Angola              |
| Clade II  | East Africa         |
| Clade III | East Central/Africa |
| Clade IV  | West Africa I       |
| Clade V   | West Africa II      |
| Clade VI  | South America I     |
| Clade VII | South America II    |

The set of mutations used for clade assignment in the current dataset was extended with mutations spread throughout the yellow fever virus genome.
Therefore, this dataset also supports clade assignment of sequences generated from genomic regions outside of the prM-E subsection.

## Features

This dataset was created using open data from NCBI Virus and the pipeline in https://github.com/hodcroftlab.

This dataset offers:

- Phylogenetic placement
- Clade assignment
- Genome Annotation and Alignment
- QC

## What is Nextclade dataset

Read more about Nextclade datasets in Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html

[Mutebi et al.]: https://pubmed.ncbi.nlm.nih.gov/11435580/
[Bryant et al.]: https://pubmed.ncbi.nlm.nih.gov/17511518/
