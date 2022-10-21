## Guide for making a reference dataset

### 0. Install nextclade and augur

Foobar lorum ipsom

### 1. Choose a well-annotated reference sequence

Create one copy in fasta format and one copy in genbank format. This sequence should have the same name in both files. These are used for creating your reference tree with augur and assigning ancestral amino acid mutations to internal nodes, which is how nextclade identifies the most appropriate phylogenetic placement for new sequences.

Note that the annotations in the genbank file need to match the annotations in the `genemap.gff` file. For viruses with a genome structure that encodes a polyprotein later cleaved to `mat_peptide`s, you'll need to relabel these features as separate `CDS` and `gene` entries like so:

```
                    gene            340..912
                                    /gene="C"
                    CDS             340..912
                                    /gene="C"
```

Note that the white space in these genbank files is important for parsing and is very difficult to keep track of when editing by hand. Be very careful as you're making these edits!

Places these files into the directory `references-files/` as `reference.fasta` and `reference.gb`

### 2. Make your gene map by filling in the template file `genemap.gff`

Based on your gene map in the genbank file above, create your `genemap.gff`.

- This is a tab-delimited file, not comma- or space-delimited.
- `seqname` is always the name of your reference sequence
- `source` is always `feature`
- `feature` is always `gene`.
  - Note that this differs from the default for many viruses that have a genome which encodes a polyprotein which is then cleaved into separate `mat_peptide`s. For these viruses, simply change `mat_peptide` to read `gene`.
- `score` is irrelevant and can be filled in with a `.` placeholder
- `frame` is important for some viruses which use ribosomal slippage to encode multiple overlapping gene products with the same sequence (e.g., HIV, HCV). This value is always either `0` (default) `1` or `2`.
- `attribute` is always `gene=genenamefoobar`

```
## seqname source feature start end score strand frame attribute
NC_009824 feature gene 340 912 . + 0 gene=C
```

### 3. Fill in any other template files you wish to use

We have provided "placeholder" files in `reference-files/` for `primers.csv`, `qc.json`, and `virus_properties.json`. Note that these files contain only headings and/or the minimum viable information. To see what other values are possible, consult the [docs]() or one of our [public datasets]().

### 4. Create your reference `tree.json` using augur

#### 4A. Assemble a sequence dataset that represents the diversity of your pathogen

This dataset does not need to be particularly large (~500 - 1,000 sequences is plenty), but should span the relevant geographic, temporal and genetic diversity as much as possible.
**If you wish to contribute your nextclade reference dataset to the open-science community, make sure to use only data that is publicly available -- i.e., no GISAID or private data!**

We recommend starting with [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/).
Don't worry about subsampling yet at this stage; we'll take care of that as part of the tree-building process.

This dataset should consist of two files:

- `prepare-reference-tree/data/metadata.tsv`

  - The only required fields are `strain` `date` and `clade_membership`
  - Including `country` +/- the other geographic fields can be helpful for subsampling later.
  - If `clade_membership` is irrelevant to your purposes, simply fill in this column with any dummy non-null value of your choice.

- `prepare-reference-tree/data/sequences.fasta`, where each sequence is named as `>this/strain/name/foobar`, where strain names correspond to rows in the metadata file.

See the nextstrain docs for more details on formatting these files.

##### Note: if you want to use nextclade to assign clade_membership designations (aka variants / lineages / genotypes / serotypes / subtypes)

Make sure each clade is well-represented in your sequence dataset, and that the `clade_membership` column is filled in for these representative sequences. Add the strain names of these represetative sequences to the file `include.txt`, one per line. It is okay if other sequences in the dataset do not yet have this column filled in.

#### 4B. Build your reference tree

At the top of the file `prepare-reference-tree/Snakefile`, update:

- Line 12: `reference_name = 'NC_009824'` with the name of your reference sequence
- Lines 49-51: subsampling parameters
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

##### Note / pro tip: you may need to iterate through this step twice to get good representation for each clade if you care about assigning clade_membership

If your input dataset doesn't have `clade_membership` annotations for each sample, you won't be able to subsample this dataset by `clade_membership` without throwing out all samples without a label. One way to get around this is a bit circular, but you can basically build the tree twice:

1. Build the tree, subsampling only on `year`
2. Look at the resulting tree in `auspice.us`. If the `clade_membership` values that were inferred by augur look good, then scroll to the bottom and click "download > metadata.tsv"
3. Merge the `clade_membership` column from this downloaded `nextstrain__metadata.tsv` file into your original `metadata.tsv` file used to build your tree.
4. Now build your final tree, subsampling on both `year` and `clade_membership` to get a nice distribution of the genetic and temporal diversity.

### 5. Name your reference dataset

By updating the first 10 lines of `tag.json`
\*\*N.B. -- @Ivan -- what's the difference between `tag.json` and `dataset.json` / `datasetRef.json` you sent me? Do we need to update the instructions in step 7?

### 6. Test your reference dataset

`nextclade run -D reference-files/ -O test-output/ my-test-sequences.fasta`

### 7. Optionally, help the community by submitting a PR with your dataset for others to use!

Foo bar contributor guidelines / processes / code of conduct / link to explainer on how to use github / etc here. I think this also includes restructuring the files in `reference-files/` to be in
`references/referenceName/versions/2020-10-10T12:00:00Z/files/` ?

(Is this something we want to encourage people to do?)

### Suggestions that would this process easier for other folks

Not all of these are feasible / reasonable to do -- you guys already do a tremendous job of documentation and supporting users! While I figure it's probably helpful to see the full list, I've put these roughly in order of what I suspect has the highest ROI.

1. [Nextclade] Make a mapping of which input files are required to generate which output files. If the user is requesting specific output files, only check for the existence of the relevant input files.

2. [Augur] Adapt `augur translate` to take the same `genemap.gff` file as input alongside the `reference.fasta`, instead of needing to construct a genbank-formatted reference sequence, too.

3. [Augur] Add an option to `augur filter` to treat missing values as a bucket during subsampling. For example, if I run `augur filter --group-by year clade_membership`, but I only have _a priori_ assigned values for `clade_membership` for 20% of my samples, it's automatically going to filter out 80% of my data, even though by the end of the tree run we'll have inferred the missing metadata values for all of those samples. Instead, add a flag like `--include-unknown-as-deme` to include N samples per year that have unknown `clade_membership`. This would have been extremely helpful in saving me from having to iterate through this twice (i.e., build the tree once, subsampling only by `year`, to assign values of `clade_membership` for more samples --> merge that metadata into the data frame --> rerun the tree, now subsampling on `year clade_membership` to get my final tree dataset).

4. [Ncov-ingest] Generalize `ncov_ingest` to a general-purpose CLI tool for constructing representative pathogen sequence datasets. Internally, our team was able to tweak a few things in the bit that constructs the genbank query request to get beautifully curated sequence and metadata files for monkeypox and hepatitis C. If useful, we can help roll this into a more general-purpose CLI wrapper so folks can re-use this pipeline for data ingest.
