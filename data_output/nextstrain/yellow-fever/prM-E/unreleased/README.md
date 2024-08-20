# Yellow Fever Virus Nextclade Dataset Tree

This workflow creates a phylogenetic tree that can be used as part of
a Nextclade dataset to assign clades to yellow fever virus samples
based on [Mutebi et al.][] (J Virol. 2001 Aug;75(15):6999-7008) and
[Bryant et al.][] (PLoS Pathog. 2007 May 18;3(5):e75).

* Build a tree using samples from the `ingest` output, with the following
  sampling criteria:
  * Force-include the following samples:
    * genotype reference strains from the 2 papers cited above
* Assign genotypes to each sample and internal nodes of the tree with
  `augur clades`, using clade-defining mutations in `defaults/clades.tsv`
* Provide the following coloring options on the tree:
  * Genotype assignment from `augur clades`

The clades we annotate (Clade I-VII) are roughly equivalent with the
following genotypes as described in the aforementioned two papers:

| Clade     | Genotype            |
|-----------|---------------------|
| Clade I   | Angola              |
| Clade II  | East Africa         |
| Clade III | East Central/Africa |
| Clade IV  | West Africa I       |
| Clade V   | West Africa II      |
| Clade VI  | South America I     |
| Clade VII | South America II    |

## How to create a new tree

* Run the workflow: `nextstrain build .`
* Inspect the output tree by comparing genotype assignments from the following sources:
  * `augur clades` output
* If unwanted samples are present in the tree, add them to
  `defaults/dropped_strains.tsv` and re-run the workflow
* If any changes are needed to the clade-defining mutations, add
  changes to `defaults/clades.tsv` and re-run the workflow
* Repeat as needed

[Mutebi et al.]: https://pubmed.ncbi.nlm.nih.gov/11435580/
[Bryant et al.]: https://pubmed.ncbi.nlm.nih.gov/17511518/
