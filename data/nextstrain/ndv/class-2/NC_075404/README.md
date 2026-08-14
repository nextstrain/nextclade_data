# Newcastle disease virus class 2 - All Genotypes with Reference Genome NC_075404

| Key                    | Value                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------|
| authors                | [Richard Neher](https://neherlab.org), [Nextstrain](https://nextstrain.org)                                          |
| data source            | Genbank, [NDV_Sequence_Datasets](https://github.com/NDVconsortium/NDV_Sequence_Datasets/)                             |
| workflow               | [github.com/nextstrain/newcastle-disease-virus](https://github.com/nextstrain/newcastle-disease-virus)                |
| nextclade dataset path | nextstrain/ndv/class-2/NC_075404                                                                                     |
| reference              | NC_075404                                                                                                            |
| genotype nomenclature  | [Dimitrov et al, 2019](https://doi.org/10.1016/j.meegid.2019.103917), as curated in [NDV_Sequence_Datasets](https://github.com/NDVconsortium/NDV_Sequence_Datasets/) |


## Scope of this dataset
This dataset covers class 2 of Newcastle disease virus (avian orthoavulavirus 1) and uses reference sequence [NC_075404](https://www.ncbi.nlm.nih.gov/nuccore/NC_075404.1/), the 15186 nt complete genome of chicken/N. Ireland/Ulster/67, which is available at NCBI RefSeq. The reference tree is built from the curated class 2 genomes of the NDV consortium sequence set, sampled between 1933 and 2021, and covers genotypes I to XXI (genotype XV is not represented). The reference tree is mid-point rooted.

**Note: class 1 and class 2 are two separate datasets, built from different references and with separate genotype nomenclatures. Class 2 viruses are 15186 nt and class 1 viruses 15198 nt; sequences of the other class will not align well against this reference and should be run against the [class 1 dataset](../class1) instead.**

The reference is the lentogenic Ulster/67 strain, which belongs to genotype I.2 and therefore sits at the periphery of the diversity covered by this dataset.

### Features
This dataset supports:
 - Assignment to the unified genotype nomenclature proposed by [Dimitrov et al, 2019](https://doi.org/10.1016/j.meegid.2019.103917), based on the 2022 release of the NDV consortium sequence set. A node is labelled with a genotype only when every sequence below it carries that genotype; everything else is reported as `unclassified`.
 - Phylogenetic placement
 - Sequence QC
