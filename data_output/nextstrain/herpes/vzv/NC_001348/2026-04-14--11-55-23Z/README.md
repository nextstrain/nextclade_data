# Varicella-Zoster Virus (VZV) dataset with reference NC_001348.1 and full genome annotation

| Key                    | Value                                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| authors                | Veronica Renne, [Aleksandr Kuznetsov](https://neherlab.org), [Nextstrain](https://nextstrain.org),                                                                                                          |
| reference              | [NC_001348.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001348.1)                                                                   |
| genome annotation      | 71 annotated ORFs, including duplicated regions (ORF62/71, ORF63/70, ORF64/69)                                                    |
| workflow               | [https://github.com/nextstrain/vzv](https://github.com/nextstrain/vzv)                                                            |
| nextclade dataset path | `nextstrain/herpes/vzv/NC_001348`                                                                                      |
| clade definitions      | Genotypes and subclades of VZV defined in `clades.tsv`, based on literature-supported classification schemes                      |

---

## Scope of this dataset

This dataset shows nucleotide and amino acid mutations relative to the *Varicella-Zoster Virus* (VZV) reference sequence [NC_001348.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001348).

It supports analysis of partial and full-genome VZV sequences, including quality control, alignment, and amino acid mutation calling across all annotated ORFs. All coding sequences (CDS) are annotated from ORF0 to ORF68, including duplicated genes in the inverted repeat regions of the genome (ORF62/71, ORF63/70, ORF64/69).

---

## Genome structure of VZV

VZV has a class E herpesvirus genome structure, consisting of a long and short unique region (U<sub>L</sub> and U<sub>S</sub>) flanked by inverted repeats. This allows for isomerization of the genome and results in duplicated genes (e.g. ORF62/71, ORF63/70, ORF64/69), which are important to consider in alignment and phylogenetic analysis.
Below is an illustration of the Varicella-Zoster Virus (VZV) genome, highlighting the repeat regions and gene organization:

![VZV genome structure](https://github.com/user-attachments/assets/95a1f277-6cf8-4b9c-85ca-3e999e5dd6dd)

*Figure from: [Schmid et al., 2010](https://journals.asm.org/doi/10.1128/cmr.00031-09).* The linear map of the VZV genome shows the terminal repeats (TR<sub>L</sub>/TR<sub>S</sub>) and internal repeats (IR<sub>L</sub>/IR<sub>S</sub>) flanking the unique long (U<sub>L</sub>) and unique short (U<sub>S</sub>) regions. The R1–R5 indicate major repeat elements. OriS represents the origin of replication. Mutations in the vaccine strains are indicated by inverted triangles at the top of the figure.


## Reference sequence and genome annotation

The reference genome used is **[NC_001348.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001348)**, corresponding to the *Varicella-Zoster Virus Dumas strain*.

The GFF3 genome annotation includes 71 coding sequences, with duplicated genes manually curated and assigned distinct ORF names (e.g., ORF62_002, ORF63_002, etc.) to reflect repeated regions. Repeated regions are masked during tree reconstruction, but mutations in these regions are annotated on the tree.

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

VZV clades are described in [Breuer et al. 2010](https://doi.org/10.1099/vir.0.017814-0) and [Jensen et al, 2017](https://www.microbiologyresearch.org/content/journal/jgv/10.1099/jgv.0.000772).
In the Nextclade reference tree, clades are assigned using signature mutations ancestral to genome representative for the different clades. These SNPs can be found in the `clades.tsv` file in the workflow. All clades other than VII are represented and annotated in the tree.

Defined clades:

| **Clade name** | **Synonyms (CDC/UK/Iowa–Canada nomenclatures)** | **Geographic association**  | **Notes**                                       |
| :------------: | ------------ | --------------------------- | ----------------------------------------------- |
|   1   |  E1/C/A   |    Europe, North America  |    Common western lineage  |
|   2   |   J/J/B   |   Japan, China    |   Dominant East Asian lineage; vaccine-origin clade |
|   3   |  E2/B/D   |  Europe, North America    | Common western lineage |
|   4   |   M2/J/C  | Africa, Asia  |  |
|   5   | M1/A/--   | Africa, Indian subcontinent |    |
|   6   | M4/--/--  | Global circulation    |   Recombinant of clades 1/3 and 4/5   |
|   VII | M3/--/--  | --    |   Not circulating; only one partial-genome strain |
|   VIII    | --    | Global circulation   | Putative clade; closely related to clade 6  |
|   9   | --    | Identified in India for the first time   | Europe (UK, Germany, USA), India (newly reported)|


Note: Clades VIII and 9 are rare and poorly sampled. Their placement and interpretation may change as more genomes become available.



### References

#### Clade Nomenclature Guidelines
- [*Judith Breuer et al. (2010). A proposal for a common nomenclature for viral clades that form the species varicella-zoster virus: summary of VZV Nomenclature Meeting 2008, Barts and the London School of Medicine and Dentistry, 24–25 July 2008*](https://doi.org/10.1099/vir.0.017814-0)

#### Global Distribution
- [*Jonas Schmidt-Chanasit et al. (2011). Evolution and world-wide distribution of varicella–zoster virus clades*](https://doi.org/10.1016/j.meegid.2010.08.014.)

#### Discovery of Novel Clades (8 & 9)
- [*Zell et al. (2012). Sequencing of 21 Varicella-Zoster Virus Genomes Reveals Two Novel Genotypes and Evidence of Recombination*](https://doi.org/10.1128/JVI.06233-11)

#### VZV in India and Emerging Clades
- [*Kumar et al. (2023). First detection of Varicella Zoster Virus clade 9 cases in India during mpox surveillance*](https://doi.org/10.1080/07853890.2023.2253733)

---