# Nextclade Dataset for "OROV" M segment based on Reference "ILMD_TF29"

## Dataset Attributes

| Attribute            | Value                                       |
| -------------------- | ------------------------------------------- |
| Name                 | orov/M/tefe                                 |
| RefName              | Oropouche virus isolate ILMD_TF29 segment M |
| RefAccession         | PP154171.1                                  |

## Genome Annotation

The GenBank record PP154171.1 annotates only the uncleaved M-segment glycoprotein precursor as a
single CDS. This dataset names that CDS `Gpc` and additionally annotates its mature products, so
that amino acid changes are reported per protein:

| CDS | Product | Precursor residues | Nucleotides |
| --- | ------- | ------------------ | ----------- |
| Gpc | glycoprotein precursor | 1-1420 | 21..4283 |
| Gn  | glycoprotein Gn | 17-335 | 69..1025 |
| NSm | nonstructural protein NSm | 336-481 | 1026..1463 |
| Gc  | glycoprotein Gc | 482-1420 | 1464..4283 |

The boundaries follow [Barbosa et al., J Virol 2023](https://doi.org/10.1128/jvi.01331-22), which
studied processing of the OROV M polyprotein directly:

- Residues 1-16 are the secretion signal sequence, so mature Gn starts at residue 17.
- SignalP 5.0 predicts signal peptidase cleavage between G335 and E336. Unlike Bunyamwera virus,
  OROV retains both Gn transmembrane domains during maturation, so Gn extends to residue 335
  rather than ending near residue 312.
- The study expresses Gc as precursor residues 482-1420. That boundary is inferred by homology
  with the experimentally mapped Bunyamwera Gc N-terminus ([Shi et al., PNAS
  2016](https://doi.org/10.1073/pnas.1603364113)), not measured for OROV.

Processing of the orthobunyavirus M polyprotein is an active research topic and further cleavage
events may exist, so these product boundaries should be treated as provisional. Gn, NSm and Gc
overlap the precursor CDS `Gpc`, so a change inside residues 17-1420 is reported both on `Gpc` and
on the product that contains it.

## Scope of This Dataset

The dataset aims to enable the quality control of segment M of Oropouche virus using a genome from [Tefe outbreak](https://pubmed.ncbi.nlm.nih.gov/29623245/) (ILMD_TF29) as reference.

This dataset was originally developed by Filipe Dezordi on behalf of Instituto Todos pela Saúde (ITpS)
with [InstitutoTodosPelaSaude/nextclade-datasets-workflows](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/tree/main/orov).
It is now maintained directly in [nextstrain/nextclade_data](https://github.com/nextstrain/nextclade_data/tree/master/data/community/itps/orov/M/tefe), which holds its current files.

For bugs, please open an [issue](https://github.com/nextstrain/nextclade_data/issues) in nextstrain/nextclade_data.

Read more about Nextclade datasets in the Nextclade documentation: [Nextclade Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
