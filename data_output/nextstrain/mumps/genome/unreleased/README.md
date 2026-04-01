# Nextclade dataset for "Mumps virus (genome)"

| Key  | Value  |
| :-- | :-- |
| name  | Mumps MuV Genotypes (genome) |
| authors | [Nextstrain](https://nextstrain.org) |
| reference | Jeryl-Lynn strain, Isolate S79; [HQ416907](https://www.ncbi.nlm.nih.gov/nuccore/HQ416907) |
| workflow  | https://github.com/nextstrain/mumps/tree/main/nextclade  |
| path  | `nextstrain/mumps/genome` |


## Scope of this dataset

Based on the full genome sequence, this dataset assigns genotypes (e.g. A to N) to Mumps samples based on [criteria outlined by the WHO](https://iris.who.int/bitstream/handle/10665/241922/WER8722_217-224.PDF) and tree placement.

Strains picked from a combination of the following papers:

* Jin et al 2005 - https://doi.org/10.1007/s00705-005-0563-4
* Jin et al 2015 - https://doi.org/10.1002/rmv.1819
* WHO 2012 - https://iris.who.int/bitstream/handle/10665/241922/WER8722_217-224.PDF

There is a "Mumps MuV Genotypes (SH gene 315nt region)" Nextclade dataset based on the SH gene and flanking region available at `nextstrain/mumps/sh`.

## Features

This dataset supports:

- Assignment of genotype
- Phylogenetic placement
- Translation of annotated reading frames
- Quality metrics based on unexpected frameshifts, stop codons, and coverage.

### Note on translation of P-gene products
The Mumps virus genome undergoes RNA editing in the P-gene before translation. The translation of edited products (addition of 2 or 4 guanine in a poly-G tract) is accommodated in the GFF genome annotation by ``slippage'' of 2 or 4 nucleotides backwards inside the poly-G tract.


## What are Nextclade datasets

Read more about Nextclade datasets in the Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
