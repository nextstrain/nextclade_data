# Nextclade Dataset for "OROV" M segment based on Reference "ILMD_TF29"

## Dataset Attributes

| Attribute            | Value                                       |
| -------------------- | ------------------------------------------- |
| Name                 | orov/M/tefe                                 |
| RefName              | Oropouche virus isolate ILMD_TF29 segment M |
| RefAccession         | PP154171.1                                  |

## Genome Annotation

The GenBank record PP154171.1 annotates only the uncleaved M-segment glycoprotein precursor. This
dataset additionally annotates its mature products, so that amino acid changes are reported per
protein:

| CDS | Product | Precursor residues | Nucleotides |
| --- | ------- | ------------------ | ----------- |
| M   | glycoprotein precursor | 1-1420 | 21..4283 |
| Gn  | glycoprotein Gn | 17-306 | 69..938 |
| NSm | nonstructural protein NSm | 307-481 | 939..1463 |
| Gc  | glycoprotein Gc | 481-1420 | 1461..4283 |

The product boundaries follow the conserved domain regions annotated on the reference's own protein
record (Bunya_G2, bunya_NSm) together with the chain boundaries of reviewed Orthobunyavirus
envelopment polyproteins projected onto the Oropouche precursor by alignment. Gn, NSm and Gc overlap
the precursor CDS, which is retained unchanged under the name `M`.

## Scope of This Dataset

The dataset aims to enable the quality control of segment M of Oropouche virus using a genome from [Tefe outbreak](https://pubmed.ncbi.nlm.nih.gov/29623245/) (ILMD_TF29) as reference.

The source code is available at [InstitutoTodosPelaSaude/nextclade-datasets-workflows](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/tree/main/orov).

For bugs, please open an [issue](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/issues).

Read more about Nextclade datasets in the Nextclade documentation: [Nextclade Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
