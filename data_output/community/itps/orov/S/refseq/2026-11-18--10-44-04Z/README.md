# Nextclade Dataset for "OROV" S segment based on RefSeq reference genome

## Dataset Attributes

| Attribute            | Value                                    |
| -------------------- | ---------------------------------------- |
| Name                 | orov/S/refseq                            |
| RefName              | Oropouche virus segment S                |
| RefAccession         | NC_005777.1                              |

## Scope of This Dataset

The dataset aims to enable the quality control of segment S of Oropouche virus using ncbi refseq as reference.

This dataset was originally developed by Filipe Dezordi on behalf of Instituto Todos pela Saúde (ITpS)
with [InstitutoTodosPelaSaude/nextclade-datasets-workflows](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/tree/main/orov).
It is now maintained directly in [nextstrain/nextclade_data](https://github.com/nextstrain/nextclade_data/tree/master/data/community/itps/orov/S/refseq), which holds its current files.

## Note on Truncated 3' UTR

The RefSeq reference genome (NC_005777.1) used in this dataset has a **truncated 3' UTR**. As a result, sequences that extend beyond the reference boundary will be clipped during alignment.

If you are working with **full-length S segment sequences**, we recommend using the [S/tefe](../tefe/) dataset instead, which is based on a complete reference and will preserve the full extent of your sequences.

For bugs, please open an [issue](https://github.com/nextstrain/nextclade_data/issues) in nextstrain/nextclade_data.

Read more about Nextclade datasets in the Nextclade documentation: [Nextclade Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
