# Nextclade Dataset for "OROV" M segment based on RefSeq reference genome

## Dataset Attributes

| Attribute            | Value                                    |
| -------------------- | ---------------------------------------- |
| Name                 | orov/M/refseq                            |
| RefName              | Oropouche virus segment M                |
| RefAccession         | NC_005775.1                              |

## Genome Annotation

The RefSeq record NC_005775.1 annotates only the uncleaved M-segment glycoprotein precursor as a
single CDS. This dataset names that CDS `Gpc` and additionally annotates its mature products, so
that amino acid changes are reported per protein:

| CDS | Product | Precursor residues | Nucleotides |
| --- | ------- | ------------------ | ----------- |
| Gpc | glycoprotein precursor | 1-1420 | 32..4294 |
| Gn  | glycoprotein Gn | 17-335 | 80..1036 |
| NSm | nonstructural protein NSm | 336-481 | 1037..1474 |
| Gc  | glycoprotein Gc | 482-1420 | 1475..4294 |

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

The dataset aims to enable the quality control of segment M of Oropouche virus using ncbi refseq as reference.

The source code is available at [InstitutoTodosPelaSaude/nextclade-datasets-workflows](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/tree/main/orov).

For bugs, please open an [issue](https://github.com/InstitutoTodosPelaSaude/nextclade-datasets-workflows/issues).

Read more about Nextclade datasets in the Nextclade documentation: [Nextclade Datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).
