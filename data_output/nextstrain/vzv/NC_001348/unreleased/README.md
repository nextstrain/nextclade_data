# Varicella-Zoster Virus (VZV) dataset with reference NC_001348.1 and full genome annotation

| Key                    | Value                                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| authors                | Veronica Renne, [Aleksander Kuznetsov](https://neherlab.org), [Nextstrain](https://nextstrain.org),                                                                                                          |
| reference              | [NC_001348.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001348.1)                                                                   |
| genome annotation      | 71 annotated ORFs, including duplicated regions (ORF62/71, ORF63/70, ORF64/69)                                                    |
| workflow               | [https://github.com/nextstrain/vzv](https://github.com/nextstrain/vzv)                                                            |
| nextclade dataset path | `nextstrain/vzv/nextclade/nextclade_dataset`                                                                                      |
| clade definitions      | Genotypes and subclades of VZV defined in `clades.tsv`, based on literature-supported classification schemes                      |

---

## Scope of this dataset

This dataset shows nucleotide and amino acid mutations relative to the *Varicella-Zoster Virus* (VZV) reference sequence [NC_001348.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001348).

It supports analysis of partial and full-genome VZV sequences, including quality control, alignment, and amino acid mutation calling across all annotated ORFs. All coding sequences (CDS) are annotated from ORF0 to ORF68, including duplicated genes in the inverted repeat regions of the genome (ORF62/71, ORF63/70, ORF64/69).

---

## Genome structure of VZV

VZV has a class E herpesvirus genome structure, characterized by **inverted repeats** a long and short unique region (U<sub>L</sub> and U<sub>S</sub>) flanked by inverted repeats. This allows for **isomerization** of the genome and results in duplicated genes (e.g. ORF62/71, ORF63/70, ORF64/69), which are important to consider in alignment and phylogenetic analysis.
Below is an illustration of the Varicella-Zoster Virus (VZV) genome, illustrating the repeat regions and gene organization:

![VZV genome structure](https://journals.asm.org/cms/10.1128/cmr.00031-09/asset/07b0b0b7-1ba8-41db-a063-212ba5e66ebf/assets/graphic/zcm0011023060002.jpeg)

*Figure from: [Zerboni et al., 2009](https://journals.asm.org/doi/10.1128/cmr.00031-09).* The linear map of the VZV genome shows the terminal repeats (TR<sub>L</sub>/TR<sub>S</sub>) and internal repeats (IR<sub>L</sub>/IR<sub>S</sub>) flanking the unique long (U<sub>L</sub>) and unique short (U<sub>S</sub>) regions. The R1–R5 indicate major repeat elements. OriS represents the origin of replication. Mutations in the vaccine strains are indicated by inverted triangles at the top of the figure.


## Reference sequence and genome annotation

The reference genome used is **[NC_001348.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001348)**, corresponding to the *Varicella-Zoster Virus Dumas strain*.

The GFF3 genome annotation includes 71 coding sequences, with duplicated genes manually curated and assigned distinct ORF names (e.g., ORF62_002, ORF63_002, etc.) to reflect repeated regions.

---

## Features

This dataset supports:

- Assignment of clades based on literature-supported classification schemes (`clades.tsv`)
- Alignment and mutation calling with Nextclade
- CDS translation and amino acid mutation annotation
- Sequence QC
- Phylogenetic placement

---

## Clade Definitions

VZV clades are based on fixed SNPs, as described in [Jensen et al, 2017](https://www.microbiologyresearch.org/content/journal/jgv/10.1099/jgv.0.000772):

Defined clades:

| Clade | Description                             | Geographic Association        |
|-------|-----------------------------------------|-------------------------------|
| 1     | European/North American lineage 1       | Europe, North America         |
| 2     | European/North American lineage 2       | Europe, North America         |
| 3     | Japanese lineage                        | Japan                         |
| 4     | Mosaic recombinant clade (Africa)       | West Africa                   |
| 5     | Mosaic recombinant clade (Africa/India) | Africa, Indian Subcontinent   |
| 6     | Recombinant lineage with clade 4/5 SNPs | Africa/Asia                   |
| 8     | Rare divergent lineage with unclear placement  | Not determined                         |
| 9     | Basal divergent lineage, ancestral to other clades         | Europe                        |


Note: Clades 8 and 9 are rare and poorly sampled. Their placement and interpretation may change as more genomes become available.

### Sources

- [*Genomic characterization and clade classification of Varicella-Zoster Virus (VZV) strains from India*](https://www.researchgate.net/publication/390730426_Genomic_analysis_of_Varicella_zoster_virus_strains_during_an_outbreak_with_atypical_clinical_presentations_in_Biswanath_district_of_Assam_India)

- [*A Full-Genome Phylogenetic Analysis of Varicella-Zoster Virus Reveals a Novel Origin of Replication-Based Genotyping Scheme and Evidence of Recombination between Major Circulating Clades*](https://pubmed.ncbi.nlm.nih.gov/16973589/)

- [*Phylogenetic Analysis of Varicella–Zoster Virus in Cerebrospinal Fluid from Individuals with Acute Central Nervous System Infection: An Exploratory Study* ](https://www.mdpi.com/1999-4915/17/2/286)

- [*Genomic analysis of Varicella zoster virus strains during an outbreak with atypical clinical presentations in Biswanath district of Assam, India*](https://www.researchgate.net/publication/390730426_Genomic_analysis_of_Varicella_zoster_virus_strains_during_an_outbreak_with_atypical_clinical_presentations_in_Biswanath_district_of_Assam_India)
---