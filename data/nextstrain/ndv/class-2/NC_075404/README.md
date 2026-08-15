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
This dataset covers class 2 of Newcastle disease virus (avian orthoavulavirus 1) and uses reference sequence [NC_075404](https://www.ncbi.nlm.nih.gov/nuccore/NC_075404.1/), the 15186 nt complete genome of chicken/N. Ireland/Ulster/67, which is available at NCBI RefSeq. The reference tree is built from the curated class 2 genomes of the NDV consortium sequence set, sampled between 1933 and 2021, and covers genotypes I to XXI (genotype XV is not represented). The class 2 part of the tree is mid-point rooted; it hangs, together with the class 1 outgroup described below, off a root that represents the common ancestor of the two classes.

**Note: class 1 and class 2 are two separate datasets, built from different references and with separate genotype nomenclatures. Class 2 viruses are 15186 nt and class 1 viruses 15198 nt, but the two classes are close enough that a sequence of either class aligns against either reference. The class 1 reference [AB524405](https://www.ncbi.nlm.nih.gov/nuccore/AB524405.1/) is therefore part of this reference tree, as an outgroup: a class 1 sequence attaches to it rather than being placed somewhere inside the class 2 diversity, and is reported as `class 1` with no genotype. Run such a sequence against the [class 1 dataset](../class1) to get a genotype for it.**

The reference is the lentogenic Ulster/67 strain, which belongs to genotype I.2 and therefore sits at the periphery of the diversity covered by this dataset.

### Features
This dataset supports:
 - Assignment to the unified genotype nomenclature proposed by [Dimitrov et al, 2019](https://doi.org/10.1016/j.meegid.2019.103917), based on the 2022 release of the NDV consortium sequence set. A node is labelled with a genotype only when every sequence below it carries that genotype; everything else is reported as `unclassified`.
 - Phylogenetic placement
 - Sequence QC
