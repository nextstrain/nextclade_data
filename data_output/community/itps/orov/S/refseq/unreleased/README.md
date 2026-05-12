# Nextclade Dataset for "OROV" S segment based on RefSeq reference genome

## Dataset Attributes

| Attribute            | Value                                    |
| -------------------- | ---------------------------------------- |
| Name                 | orov/S/refseq                            |
| RefName              | Oropouche virus segment S                |
| RefAccession         | NC_005777.1                              |

## Scope of This Dataset

The dataset aims to enable the quality control of segment S of Oropouche virus using ncbi refseq as reference.

The source code is available at [InstitutoTodosPelaSaude/nextclade-datasets-workflows](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/tree/main/orov).

## Note on Truncated 3' UTR

The RefSeq reference genome (NC_005777.1) used in this dataset has a **truncated 3' UTR**. As a result, sequences that extend beyond the reference boundary will be clipped during alignment.

If you are working with **full-length S segment sequences**, we recommend using the [S/tefe](../tefe/) dataset instead, which is based on a complete reference and will preserve the full extent of your sequences.

For bugs, please open an [issue](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/issues).

Read more about Nextclade datasets in the Nextclade documentation: [Nextclade Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
