# Newcastle disease virus class 1 - All Genotypes with Reference Genome AB524405

| Key                    | Value                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------|
| authors                | [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                          |
| data source            | Genbank, [NDV_Sequence_Datasets](https://github.com/NDVconsortium/NDV_Sequence_Datasets/)                             |
| workflow               | [github.com/nextstrain/newcastle-disease-virus](https://github.com/nextstrain/newcastle-disease-virus)                |
| nextclade dataset path | nextstrain/ndv/class-1/AB524405                                                                                      |
| reference              | AB524405                                                                                                             |
| genotype nomenclature  | [Dimitrov et al, 2019](https://doi.org/10.1016/j.meegid.2019.103917), as curated in [NDV_Sequence_Datasets](https://github.com/NDVconsortium/NDV_Sequence_Datasets/) |


## Scope of this dataset
This dataset covers class 1 of Newcastle disease virus (avian orthoavulavirus 1) and uses reference sequence [AB524405](https://www.ncbi.nlm.nih.gov/nuccore/AB524405.1/), the 15198 nt complete genome of goose/Alaska/415/91. The reference tree is built from the curated class 1 genomes of the NDV consortium sequence set, sampled between 1991 and 2020, and covers genotypes 1.1.1, 1.1.2 and 1.2. The reference tree is mid-point rooted.

**Note: class 1 and class 2 are two separate datasets, built from different references and with separate genotype nomenclatures. Class 1 viruses are 15198 nt and class 2 viruses 15186 nt; sequences of the other class will not align well against this reference and should be run against the [class 2 dataset](../class2) instead.**

The reference itself (annotated as lineage 6 in GenBank, under the pre-2019 class 1 nomenclature) carries no genotype assignment in the curated set.

### Features
This dataset supports:
 - Assignment to the unified genotype nomenclature proposed by [Dimitrov et al, 2019](https://doi.org/10.1016/j.meegid.2019.103917), based on the 2022 release of the NDV consortium sequence set. A node is labelled with a genotype only when every sequence below it carries that genotype; everything else is reported as `unclassified`.
 - Phylogenetic placement
 - Sequence QC
