# Yellow fever virus (prM-E region only) dataset

| Key               | Value                                                            |
| ----------------- | -----------------------------------------------------------------|
| name              | Yellow fever virus (YFV) prM-E region                            |
| authors           | [Nextstrain](https://nextstrain.org)                             |
| reference         | AY640589.1                                                       |
| workflow          | <https://github.com/nextstrain/yellow-fever/tree/main/nextclade> |
| path              | `nextstrain/yellow-fever/prM-E`                                  |

## Scope of this dataset

This dataset assigns clades to yellow fever virus samples based on
strain and genotype information from [Mutebi et al.][] (J Virol. 2001
Aug;75(15):6999-7008) and [Bryant et al.][] (PLoS Pathog. 2007 May 18;3(5):e75)

These two papers, collectively, define 7 distinct yellow fever virus
genotypes based on a 670 nucleotide region of the yellow fever virus
genome, (bases 641-1310), called the prM-E region. This region
comprises the 3' end of the pre-membrane protein (prM) gene, the
entire membrane protein (M) gene, and the 5' end of the envelope
protein (E) gene.

The clades we annotate (Clade I-VII) are roughly equivalent with the
following genotypes as described in the aforementioned two papers:

| Clade     | Genotype            |
|-----------|---------------------|
| Clade I   | Angola              |
| Clade II  | East Africa         |
| Clade III | East Central/Africa |
| Clade IV  | West Africa I       |
| Clade V   | West Africa II      |
| Clade VI  | South America I     |
| Clade VII | South America II    |

(N.b., the reference sequence used in this data set is actually 672nt
long, from bases 641-1312 of the genome reference. The 2 extra bases
make the reference a complete open reading frame.)

This dataset can be used to assign genotypes to any sequence that
includes at least 500 bp of the prM-E region, including whole genome
sequences. Sequence data beyond the prM-E region will be reported as an
insertion in the Nextclade output.

## Features

This dataset supports:

- Assignment of genotypes
- Phylogenetic placement
- Sequence quality control (QC)

## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation:
<https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html>

[Mutebi et al.]: https://pubmed.ncbi.nlm.nih.gov/11435580/
[Bryant et al.]: https://pubmed.ncbi.nlm.nih.gov/17511518/
