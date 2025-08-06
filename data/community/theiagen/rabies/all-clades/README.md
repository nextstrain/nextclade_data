# Example dataset for Rabies virus

This is a minimal example dataset for *Lyssavirus rabies*. 

# Overview

The phylogenetic tree was generated from all complete *Lyssavirus rabies* genomes obtained from [NCBI Nucleotide](https://ftp.ncbi.nlm.nih.gov/genomes/Viruses/AllNuclMetadata/) (accessed 2025/05/01) with > 95% unambiguous nucleotides and < 15,000 bp. Clade, subclade, and other associated metadata were acquired referencing the original rabies Nextstrain build and [RABV-GLUE's metadata](https://github.com/giffordlabcvr/RABV-GLUE/blob/master/tabular/reference-set-data.tsv). Clade- and subclade-specific mutations [were extracted for all monophyletic major and minor lineages](https://github.com/theiagen/utilities/pull/21), and disregarded for previously assigned clades that were not monophyletic in the phylogeny. Complete genome assemblies were aligned with `mafft v7.525` using default parameters and the phylogeny was reconstructed using `iqtree v2.4.0` with 1000 ultrafast bootstrap iterations and GTR+F+I+R7 selected as the evolutionary model by the *ModelFinder* module. A root node internal to the *L. rabies* phylogeny was selected by reconstructing an additional phylogeny using the same methodology with *L. australis* (NC_003243.1) and *L. gannoruwa* (KU244266.2) included as known outgroups ([Baynard & Fooks, 2021](https://www.sciencedirect.com/science/article/abs/pii/B9780128096338209369)).

# Metadata acquisition

Clade classification metadata was acquired from [RABV-GLUE's metadata](https://github.com/giffordlabcvr/RABV-GLUE/blob/master/tabular/reference-set-data.tsv) (referenced [2025/06/01](https://github.com/giffordlabcvr/RABV-GLUE/blob/357613e78c397e10499e77bbd6f2b5aeeb9d10e6/tabular/reference-set-data.tsv#L4)). Sample, submitter, location, and host metadata was acquired from NCBI using the following `datasets` command:

```bash
datasets summary virus genome accession \
  --inputfile <ACCESIONS> \
  --as-json-lines | \
dataformat tsv virus-genome \
  --fields accession,geo-region,host-common-name,submitter-names,isolate-collection-date
```

# Included clades

We conservatively assigned clades as all accessions that descend from a most-recent common ancestor (MRCA) of classified accessions within the metadata. Subclades that were not monophyletic or did not contain uniquely defining mutations were removed. The following are the accounted clades, except where exclusion criteria are noted:

| Clade | Subclade | Exclusion Criteria |
|-------|----------|-------------------|
| Africa-2 | - | - |
| Africa-3 | - | - |
| Arctic | - | - |
| Arctic | A | - |
| Arctic | AL1a | - |
| Arctic | AL1b | - |
| Arctic | AL2 | - |
| Arctic | <s>AL3</s> | Mutations are not unique |
| Asian | - | - |
| Asian | SEA1a | - |
| Asian | SEA1b | - |
| Asian | SEA2a | - |
| Asian | SEA2b | - |
| Asian | SEA3 | - |
| Asian | SEA4 | - |
| Asian | SEA5 | - |
| Bats | - | - |
| Bats | <s>AP</s> | Mutations are not unique |
| Bats | DR | - |
| Bats | <s>EF-E1</s> | Mutations are not unique |
| Bats | <s>EF-E2</s> | Mutations are not unique |
| Bats | EF-W1 | - |
| Bats | EF-W2 | - |
| Bats | <s>LB1</s> | Mutations are not unique |
| Bats | <s>LB2</s> | Mutations are not unique |
| Bats | <s>LC</s> | Mutations are not unique |
| Bats | LI | - |
| Bats | <s>LN</s> | Mutations are not unique |
| Bats | <s>LS</s> | Mutations are not unique |
| Bats | <s>LX</s> | Mutations are not unique |
| Bats | MYsp | - |
| Bats | <s>MYu</s> | Mutations are not unique |
| Bats | <s>PH</s> | Not monophyletic |
| Bats | PS | - |
| Bats | TB1 | - |
| Bats | TB2 | - |
| Cosmopolitan | - | - |
| Cosmopolitan | AF1a | - |
| Cosmopolitan | AF1b | - |
| Cosmopolitan | AF1c | - |
| Cosmopolitan | AF4 | - |
| Cosmopolitan | AM1 | - |
| Cosmopolitan | AM2a | - |
| Cosmopolitan | AM2b | - |
| Cosmopolitan | AM3a | - |
| Cosmopolitan | AM3b | - |
| Cosmopolitan | AM4 | - |
| Cosmopolitan | CA1 | - |
| Cosmopolitan | CA2 | - |
| Cosmopolitan | CA3 | - |
| Cosmopolitan | CE | - |
| Cosmopolitan | EE | - |
| Cosmopolitan | ME1a | - |
| Cosmopolitan | ME1b | - |
| Cosmopolitan | ME2 | - |
| Cosmopolitan | NEE | - |
| Cosmopolitan | Vac | - |
| Cosmopolitan | <s>Vac2</s> | Mutations are not unique |
| Cosmopolitan | WE | - |
| Cosmopolitan | <s>YUGCOW</s> | Mutations are not unique |
| Cosmopolitan | <s>YUGFOX</s> | Mutations are not unique |
| Indian-Sub | - | - |
| RAC-SK | - | - |


# Phylogenetic tree reconstruction

The tree was generated from the multifasta containing the sequences depicted above using the following commands:

Align relative to the reference sequence
```bash
augur align -s rabv.fna --nthreads 8 --output rabv.mafft.fna --reference-name NC_001542.1 --debug
```

Build the tree with 1000 ultrafast bootstrap iterations
```bash
iqtree -s rabv.mafft.fna -B 1000 -m GTR+F+I+R7
```

Root the tree with the MRCA of the identified outgroup sequences
```python
from ete3 import Tree

t = Tree('rabv.mafft.fna.contree')
mrca = t.get_common_ancestor(['OU524413.1', 'JQ685954.1'])
t.set_outgroup(mrca)

with open('rabv.rooted.newick', 'w') as out:
    out.write(t.write())
```