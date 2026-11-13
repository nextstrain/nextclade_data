# Nextclade Dataset for "OROV" M segment based on RefSeq reference genome

## Dataset Attributes

| Attribute            | Value                                    |
| -------------------- | ---------------------------------------- |
| Name                 | orov/M/refseq                            |
| RefName              | Oropouche virus segment M                |
| RefAccession         | NC_005775.1                              |

## Genome Annotation

The RefSeq record NC_005775.1 annotates only the uncleaved M-segment glycoprotein precursor. This
dataset additionally annotates its mature products, so that amino acid changes are reported per
protein:

| CDS | Product | Precursor residues | Nucleotides |
| --- | ------- | ------------------ | ----------- |
| M   | glycoprotein precursor | 1-1420 | 32..4294 |
| Gn  | glycoprotein Gn | 17-306 | 80..949 |
| NSm | nonstructural protein NSm | 307-481 | 950..1474 |
| Gc  | glycoprotein Gc | 481-1420 | 1472..4294 |

The product boundaries follow the conserved domain regions annotated on the reference's own protein
record (Bunya_G2, bunya_NSm) together with the chain boundaries of reviewed Orthobunyavirus
envelopment polyproteins projected onto the Oropouche precursor by alignment. Gn, NSm and Gc overlap
the precursor CDS, which is retained unchanged under the name `M`.

## Scope of This Dataset

The dataset aims to enable the quality control of segment M of Oropouche virus using ncbi refseq as reference.

The source code is available at [InstitutoTodosPelaSaude/nextclade-datasets-workflows](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/tree/main/orov).

For bugs, please open an [issue](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/issues).

Read more about Nextclade datasets in the Nextclade documentation: [Nextclade Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
