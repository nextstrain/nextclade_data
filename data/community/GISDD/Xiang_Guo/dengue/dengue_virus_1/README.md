# Dengue dataset

| Key  | Value  |
| :-- | :-- |
| name  | GISDD dengue virus serotype 1  |
| authors | Xiang Guo |
| reference | KM204119.1 |
| workflow  | http://www.bic.ac.cn/GISDD/  |
| path  | `GISDD/dengue/dengue_virus_1` |


## Scope of this dataset

This dataset assigns serotype (e.g. DENV1) to dengue samples based on GISDD criteria [WHO](https://idpjournal.biomedcentral.com/articles/10.1186/s40249-022-01024-5) and tree placement nearest references [KM204119 (DENV1)].

## Features

This dataset supports:

- Assignment of serotypes
- Phylogenetic placement
- Sequence quality control (QC)

## Note on sequence coverage

This dataset uses the full DENV1 genome (KM204119.1, 10736bp) as the reference sequence. The reference tree is built based on E gene sequences (~1485bp, genome positions 936-2420). Users submitting E gene sequences will have their sequences aligned to the E gene region of the reference genome.
