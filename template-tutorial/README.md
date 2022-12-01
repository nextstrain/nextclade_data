# Guide for making a reference dataset

## Quickstart: making a reference dataset for QC and mutations only

### 1. Install the nextclade CLI

See instructions [here](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli.html#installation-local)

### 2. Choose a well-annotated reference sequence

We recommend using NCBI's refseq database as a starting point. Save this reference sequence as the only entry in `./reference-files/reference.fasta`

### 3. Make your gene map by filling in the template file `genemap.gff`

Based on the genbank record of your reference sequence, create your `genemap.gff`.

- This is a tab-delimited file, not comma- or space-delimited.
- `seqname` is always the name of your reference sequence
- `source` is always `feature`
- `feature` is always `gene`.
  - Note that for viruses with genomes which encode a polyprotein which is then cleaved into separate `mat_peptide`s, these are listed in genbank records as `matpeptide` features instead of as `gene`s. For these viruses, list each `mat_peptide` feature as a `gene` in the genemap file.
- `score` is irrelevant and can be filled in with a `.` placeholder
- `frame` is important for some viruses which use ribosomal slippage to encode multiple overlapping gene products with the same sequence (e.g., HIV, HCV). This value is always either `0` (default) `1` or `2`.
- `attribute` is always `gene=genenamefoobar`

```
## seqname source feature start end score strand frame attribute
NC_009824 feature gene 340 912 . + 0 gene=C
```

### 4. Update values in `qc.json`

See the [main docs](https://docs.nextstrain.org/projects/nextclade/en/stable/user/algorithm/07-quality-control.html) for an explanation of each QC rule.

As a starting point, we've initialized this file with the values we use for SARS-CoV-2.

### 5. [Optional] Fill in `primers.csv` and/or `virus_properties.json`

If you wish to be alerted when primers change, add these to the template file `primers.csv`. Similarly, if you wish to tweak seed matching parameters or specify clade-specific mutations, add these to `virus_properties.json`. For both of these files, we suggest referring to the `sars-cov-2` reference dataset as an example. This dataset is available to download by running

```
nextclade dataset get --name sars-cov-2 --output-dir foo
```

### 6. Test run!

Try out your new reference dataset by running:

```
nextclade run -D ./reference-files/ -O foo/bar/ input_sequences.fasta
```

Note that while a list of lineages and an output tree will still be provided, it will not be informative and should not be used.

## Optional Extension: create a reference `tree.json` for lineage calling and phylogenetic placements

### 7. Install augur

See instructions [here](https://docs.nextstrain.org/projects/augur/en/stable/installation/installation.html).

### 8. Assemble a sequence dataset that represents the diversity of your pathogen

This dataset does not need to be particularly large (~500 - 1,000 sequences is plenty), but should span the relevant geographic, temporal and genetic diversity as much as possible.
**If you wish to contribute your nextclade reference dataset to the open-science community, make sure to use only data that is publicly available -- i.e., no GISAID or private data!**

We recommend starting with [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) and [`augur curate`]().
Don't worry about subsampling yet at this stage; we'll take care of that as part of the tree-building process.

This dataset should consist of two files:

- `prepare-reference-tree/data/metadata.tsv`

  - The only required fields are `strain` `date` and `clade_membership`
  - Including `country` +/- the other geographic fields can be helpful for subsampling later.
  - If `clade_membership` is irrelevant to your purposes, simply fill in this column with any dummy non-null value of your choice.

- `prepare-reference-tree/data/sequences.fasta`, where each sequence is named as `>this/strain/name/foobar`, where strain names correspond to rows in the metadata file.

[See augur docs](https://docs.nextstrain.org/projects/augur/en/stable/faq/metadata.html) for more information on formatting these files

##### Note: if you want to use nextclade to assign clade_membership designations (aka variants / lineages / genotypes / serotypes / subtypes)

Make sure each clade is well-represented in your sequence dataset, and that the `clade_membership` column is filled in for these representative sequences. Add the strain names of these represetative sequences to the file `include.txt`, one per line. It is okay if other sequences in the dataset do not yet have this column filled in.

### 9. Make a copy of your reference sequence in genbank format

The reference sequence should have the same name in both files. These are used for creating your reference tree with augur and assigning ancestral amino acid mutations to internal nodes, which is how nextclade identifies the most appropriate phylogenetic placement for new sequences.

Note that the annotations in the genbank file need to match the annotations in the `genemap.gff` file. For viruses with a genome structure that encodes a polyprotein later cleaved to `mat_peptide`s, you'll need to relabel these features as separate `CDS` and `gene` entries like so:

```
                    gene            340..912
                                    /gene="C"
                    CDS             340..912
                                    /gene="C"
```

Note that the white space in these genbank files is important for parsing and is very difficult to keep track of when editing by hand. Be very careful as you're making these edits!

Places these files into the directory `references-files/` as `reference.fasta` and `reference.gb`

### 10. Build your reference tree

At the top of the file `prepare-reference-tree/Snakefile`, update:

- Line 12: `reference_name = 'NC_009824'` with the name of your reference sequence
- Lines 49-51: subsampling parameters - as appropriate
  - ````group_by = "country year",
        sequences_per_group = 10,
        min_date = 1990```
    ````

Then run the tree build with:

```
cd prepare-reference-tree/
Snakemake .
```

This should create an output tree JSON file in `reference-files/tree.json`. Examine this tree in your browser at `https://auspice.us` to verify that the tree looks reasonable. If relevant, color by `clade_membership` to verify that your clade assignments look correct.

### 11. Test run!

`nextclade run -D ./reference-files/ -O foo/bar/ input-sequences.fasta`

## Optional extension: submit your dataset to help the community! :)

### 12. Clone the nextclade_data repository from github

```
git clone https://github.com/nextstrain/nextclade_data.git
```

### 13. Update descriptive JSON files to help others understand your dataset

- `dataset.json` lists the species name and which reference sequence to use by default for that species
- `datasetRef.json` describes each reference sequence and where it came from
- `tag.json` describes each "release" or version of the reference dataset bundle as a whole

Take a look at the template files provided. As always, if you have questions please feel free to get in touch via our [discussion board](https://discussion.nextstrain.org)!

### 14. Set up your directory structure

For others to use your dataset directly through nextclade, you'll need to restructure your directory a bit so that it looks like:

```
nextclade_data/data/datasets/speciesNameHere/
                              └──dataset.json
                              └──references/accessionNumberHere/
                                            ├──datasetRef.json
                                            └──versions/timeStampHere/
                                                        ├──reference.fasta
                                                        ├──genemap.gff
                                                        ├──primers.csv
                                                        ├──tree.json
                                                        ├──qc.json
                                                        └──tag.json
```

E.g., the path to `reference.fasta` for the `sars-cov-2` dataset looks like:
`nextclade_data/data/datasets/sars-cov-2/references/MN908947/versions/2021-06-25T00:00:00Z/files/reference.fasta`

### 15. Make a pull request!

See this [friendly youtube video](https://www.youtube.com/watch?v=rgbCcBNZcdQ&ab_channel=JakeVanderplas) for help. Thanks so much for supporting the scientific community!
