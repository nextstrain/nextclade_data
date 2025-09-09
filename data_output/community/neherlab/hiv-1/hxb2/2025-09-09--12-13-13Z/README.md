# EXPERIMENTAL: HIV-1 group M subtype and CRF classification

| Key                    | Value                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------|
| authors                | [Richard Neher (U Basel)](https://neherlab.org), [Thomas Leitner (LANL)](https://public.lanl.gov/tkl/)              |
| data source            | LANL database and Genbank                                                                                           |
| workflow               | [github.com/neherlab/HIV-nextclade](https://github.com/neherlab/HIV-nextclade)                                      |
| nextclade dataset path | community/neherlab/hiv-1/hxb2                                                                                                      |
| reference              | [NC_001802](https://www.ncbi.nlm.nih.gov/nuccore/NC_001802)                                                         |

This Nextclade data set aligns sequences to the HXB2 reference and finds the closest match in a reference tree build from the [2021 Super filtered Alignment](https://www.hiv.lanl.gov/content/sequence/NEWALIGN/help.html#filter) provided by LANL.
Due to extensive recombination in HIV-1 group M, the tree is not a proper phylogenetic tree, but a collection of trees inferred for each subtype or recombinant form. These individuals trees are then grafted together. Rare CRFs, URFs, or subtypes represented less then 3 times in the reference alignment are labeled as subtype `other`.

Note that the classification is **EXPERIMENTAL** and might be unreliable for sequences that lack a close representative in the tree. 
The closeness to sequences in the reference set is quantified by the `private mutations` 
As a general guide, the more private mutations a sequence has, the less reliable the subtype assignment will be. 

Note that alignments of sequences that are far from the subtype B HXB2 reference will have 

## Reference sequence HXB2 (NC_001802)

This data set uses the NCBI reference sequence [NC_001802](https://www.ncbi.nlm.nih.gov/nuccore/NC_001802) based on the HXB2 genome [K03455](https://www.ncbi.nlm.nih.gov/nuccore/K03455.1). The primary reason for choosing it is to ensure amino acid substitutions in conserved proteins such as `Pol` are numbered consistently.
Note that this sequence as a few problems, including a premature stop-codon in `nef`.

## Treatment of indel-rich regions

There are multiple regions in the HIV-1 genome where deletions and insertions are common. Such regions are often not consistently aligned when aligning sequences individually to a reference. For the purposes of finding closely matching sequences in the reference tree, these regions are ignored. Specifically, tree placement ignores

 - The LTR before the beginning of `gag` (until position 336 in `NC_001802`)
 - Positions 5780 until 5870 at the end of `vpu` and the beginning of `gp120`
 - Positions 6160 until 6240 in `gp120`. 
 - Position 6940 unitl 7020 in `gp120`.
 - The 5' LTR from end of `nef` (positions 9863 until the end of the genome)


