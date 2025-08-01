# Nextclade dataset creation guide

This guide describes how to create a new Nextclade dataset from scratch.
Datasets are how Nextclade is customized to work with a particular virus.
Once a dataset is created, it can be optionally shared with other users via the Nextclade data repository or a separate Github repository.
This page provides a detailed walk-through on how to put together a Nextclade dataset. Answers to [Frequently Asked Questions](#faqs) is provided below.

> ⚠️ This guide serves for advanced Nextclade users and enthusiasts who want to create and maintain their own Nextclade datasets, e.g. to add a yet unsupported pathogen or strain. It assumes basic familiarity with Nextclade CLI and Nextclade Web and some experience with different datasets as a user. If you are not yet comfortable using Nextclade and want to learn more about Nextclade datasets, please refer to the [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/) first.

> ⚠️ If you are looking for Nextclade software developer documentation, see [Nextclade developer guide](https://github.com/nextstrain/nextclade/blob/master/docs/dev/developer-guide.md) instead.

> ⚠️ If you are looking how you can share your dataset using the Nextclade data repository please consult the [Nextclade dataset curation guide](dataset-curation-guide.md).

## Recommended prerequisites

- Knowledge of command line bioinformatics
- Basic knowledge of Nextclade, in particular of the Nextclade CLI
- Familiarity with Nextstrain's augur toolchain (not strictly necessary, but helpful)
- Ability to read a simple Snakemake workflow

## Overview

A Nextclade dataset is a collection of files. While Nextclade CLI can be used with as little as a reference sequence, a full dataset to be used with Nextclade web requires a general configuration file as well. The full set of files is as follows:

1. A reference sequence in fasta format against which query sequences are aligned (required)
1. A genome annotation for the reference sequence in GFF3 format (recommended)
1. A phylogenetic tree in Auspice JSON format (optional)
1. A general configuration file (`pathogen.json`) in JSON format (required for Nextclade Web)

The official specification of these files is available in the Nextclade docs at <https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/index.html>.

The guide here complements the specifications by going through a concrete workflow that produces these files for an example virus (Zika).

## Choosing a reference sequence

As all sequences are aligned to the reference sequence and all mutations are reported relative to it, the choice of the reference sequence is important.

A good reference sequence should be of high quality and cover the entire genome (or at least the regions of interest).

A good default choice is an NCBI refseq. For example, for Zika virus, the most recent NCBI refseq is `NC_035889.1`. It is available on GenBank at <https://www.ncbi.nlm.nih.gov/nuccore/NC_012532.1>.

If all current circulation is derived from a more recent common ancestor, it may be better to use a more recent reference sequence to reduce the number of mutations reported.

See the Nextclade docs for the [full specification of the reference sequence file](https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/02-reference-sequence.html).

## Preparing the genome annotation

Nextclade uses the genome annotation to determine how to extract amino acid sequences from aligned nucleotide sequences. Nextclade requires the genome annotation to be in [GFF3 format](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md). Nextclade only uses the `CDS` feature type, but parent features such as genes can be included in the annotation.
Each `CDS` feature is treated separately for translation, alignment and amino acid mutation reporting. CDS consisting of multiple segments are represented as multiple CDS entries in the GFF files and linked via a common `ID`.

While Genbank provides annotations in GFF3 format, there is often a discrepancy between what the dataset creator wants to be translated and what is annotated as a CDS in the Genbank provided GFF3 file. In addition, users may want to change names of CDS features to make them more readable in Nextclade output.

For example, the Genbank GFF3 file for the Zika refseq has a single CDS feature for the entire polyprotein with a cryptic `Name` "YP_009428568.1". Instead, one may want to translate each mature protein separately and give them more readable names. This can be done by editing the GFF3 file by hand, or by using a custom script. By hand, we can remove the existing CDS feature and renaming all `mature_protein_region_of_CDS` feature types to `CDS`. Overlapping precursors can be removed as well, as appropriate. In addition, a `gene` attribute can be added with the name one wants to see in Nextclade. Unfold the section below to see both the original and the modified GFF3 files:

<details>
<summary> Genbank provided GFF3 file for the Zika refseq `NC_035889.1` </summary>

```gff3
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
##sequence-region NC_035889.1 1 10808
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=64320
NC_035889.1	RefSeq	region	1	10808	.	+	.	ID=NC_035889.1:1..10808;Dbxref=taxon:64320;collection-date=2015;country=Brazil: Rio Grande do Norte%2C Natal;gbkey=Src;genome=genomic;isolation-source=fetus' brain autopsy;mol_type=genomic RNA;nat-host=Homo sapiens;strain=Natal RGN
NC_035889.1	RefSeq	region	1	10808	.	+	.	ID=id-NC_035889.1:1..10808;Note=Mature peptides were annotated by RefSeq staff using homoloy to NC_012532.1 and the cleavage sites reported in Kuno and Chang%2C 2007 (PMID 17195954). Questions about the annotation of this sequence should be directed to info@ncbi.nlm.nih.gov.;gbkey=Comment
NC_035889.1	RefSeq	gene	108	10379	.	+	.	ID=gene-CPG35_gp1;Dbxref=GeneID:34443389;Name=POLY;gbkey=Gene;gene=POLY;gene_biotype=protein_coding;locus_tag=CPG35_gp1
NC_035889.1	RefSeq	CDS	108	10379	.	+	0	ID=cds-YP_009428568.1;Parent=gene-CPG35_gp1;Dbxref=GenBank:YP_009428568.1,GeneID:34443389;Name=YP_009428568.1;gbkey=CDS;gene=POLY;locus_tag=CPG35_gp1;product=polyprotein;protein_id=YP_009428568.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	108	473	.	+	.	ID=id-YP_009428568.1:1..122;Parent=cds-YP_009428568.1;gbkey=Prot;product=anchored capsid protein C;protein_id=YP_009430295.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	108	419	.	+	.	ID=id-YP_009428568.1:1..104;Parent=cds-YP_009428568.1;gbkey=Prot;product=capsid protein C;protein_id=YP_009430296.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	474	977	.	+	.	ID=id-YP_009428568.1:123..290;Parent=cds-YP_009428568.1;gbkey=Prot;product=membrane glycoprotein precursor M;protein_id=YP_009430297.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	474	752	.	+	.	ID=id-YP_009428568.1:123..215;Parent=cds-YP_009428568.1;gbkey=Prot;product=protein pr;protein_id=YP_009430298.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	753	977	.	+	.	ID=id-YP_009428568.1:216..290;Parent=cds-YP_009428568.1;gbkey=Prot;product=membrane glycoprotein M;protein_id=YP_009430299.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	978	2489	.	+	.	ID=id-YP_009428568.1:291..794;Parent=cds-YP_009428568.1;gbkey=Prot;product=envelope protein E;protein_id=YP_009430300.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	2490	3545	.	+	.	ID=id-YP_009428568.1:795..1146;Parent=cds-YP_009428568.1;gbkey=Prot;product=nonstructural protein NS1;protein_id=YP_009430301.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	3546	4223	.	+	.	ID=id-YP_009428568.1:1147..1372;Parent=cds-YP_009428568.1;gbkey=Prot;product=nonstructural protein NS2A;protein_id=YP_009430302.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	4224	4613	.	+	.	ID=id-YP_009428568.1:1373..1502;Parent=cds-YP_009428568.1;gbkey=Prot;product=nonstructural protein NS2B;protein_id=YP_009430303.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	4614	6464	.	+	.	ID=id-YP_009428568.1:1503..2119;Parent=cds-YP_009428568.1;gbkey=Prot;product=nonstructural protein NS3;protein_id=YP_009430304.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	6465	6845	.	+	.	ID=id-YP_009428568.1:2120..2246;Parent=cds-YP_009428568.1;gbkey=Prot;product=nonstructural protein NS4A;protein_id=YP_009430305.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	6846	6914	.	+	.	ID=id-YP_009428568.1:2247..2269;Parent=cds-YP_009428568.1;gbkey=Prot;product=protein 2K;protein_id=YP_009430306.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	6915	7667	.	+	.	ID=id-YP_009428568.1:2270..2520;Parent=cds-YP_009428568.1;gbkey=Prot;product=nonstructural protein NS4B;protein_id=YP_009430307.1
NC_035889.1	RefSeq	mature_protein_region_of_CDS	7668	10376	.	+	.	ID=id-YP_009428568.1:2521..3423;Parent=cds-YP_009428568.1;gbkey=Prot;product=RNA-dependent RNA polymerase NS5;protein_id=YP_009430308.1
```

</details>

<details>
<summary> Modified GFF3 file for the Zika refseq `NC_012532.1` </summary>

```gff3
##gff-version 3
##sequence-region NC_035889.1 1 10808
NC_035889.1	RefSeq	region	1	10808	.	+	.	ID=NC_035889.1:1..10808;Dbxref=taxon:64320;collection-date=2015;country=Brazil: Rio Grande do Norte%2C Natal;gbkey=Src;genome=genomic;isolation-source=fetus' brain autopsy;mol_type=genomic RNA;nat-host=Homo sapiens;strain=Natal RGN
NC_035889.1	RefSeq	CDS	108	473	.	+	.	Name=CA;gbkey=Prot;protein_id=YP_009430295.1;ID=id-YP_009428568.1:1..122;product=anchored capsid protein C
NC_035889.1	RefSeq	CDS	474	752	.	+	.	Name=PRO;gbkey=Prot;product=protein pr;protein_id=YP_009430298.1;ID=id-YP_009428568.1:123..215
NC_035889.1	RefSeq	CDS	753	977	.	+	.	Name=MP;gbkey=Prot;protein_id=YP_009430299.1;product=membrane glycoprotein M;ID=id-YP_009428568.1:216..290
NC_035889.1	RefSeq	CDS	978	2489	.	+	.	Name=ENV;gbkey=Prot;protein_id=YP_009430300.1;product=envelope protein E;ID=id-YP_009428568.1:291..794
NC_035889.1	RefSeq	CDS	2490	3545	.	+	.	Name=NS1;gbkey=Prot;protein_id=YP_009430301.1;product=nonstructural protein NS1;ID=id-YP_009428568.1:795..1146
NC_035889.1	RefSeq	CDS	3546	4223	.	+	.	Name=NS2A;gbkey=Prot;protein_id=YP_009430302.1;product=nonstructural protein NS2A;ID=id-YP_009428568.1:1147..1372
NC_035889.1	RefSeq	CDS	4224	4613	.	+	.	Name=NS2B;gbkey=Prot;protein_id=YP_009430303.1;product=nonstructural protein NS2B;ID=id-YP_009428568.1:1373..1502
NC_035889.1	RefSeq	CDS	4614	6464	.	+	.	Name=NS3;gbkey=Prot;protein_id=YP_009430304.1;product=nonstructural protein NS3;ID=id-YP_009428568.1:1503..2119
NC_035889.1	RefSeq	CDS	6465	6845	.	+	.	Name=NS4A;gbkey=Prot;protein_id=YP_009430305.1;product=nonstructural protein NS4A;ID=id-YP_009428568.1:2120..2246
NC_035889.1	RefSeq	CDS	6846	6914	.	+	.	Name=2K;gbkey=Prot;product=protein 2K;protein_id=YP_009430306.1;ID=id-YP_009428568.1:2247..2269
NC_035889.1	RefSeq	CDS	6915	7667	.	+	.	Name=NS4B;gbkey=Prot;protein_id=YP_009430307.1;product=nonstructural protein NS4B;ID=id-YP_009428568.1:2270..2520
NC_035889.1	RefSeq	CDS	7668	10376	.	+	.	Name=NS5;gbkey=Prot;protein_id=YP_009430308.1;ID=id-YP_009428568.1:2521..3423;product=RNA-dependent RNA polymerase NS5
```

</details>

Alternatively, one can use a custom script to perform these tasks. We provide an interactive script in [`example-workflow/scripts/generate_from_genbank.py`](./example-workflow/scripts/generate_from_genbank.py) that requires an NCBI accession as input and walks the user through the process of picking the CDS features and naming them.

Further details on the genome annotation file format are available in the [Nextclade docs](https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/03-genome-annotation.html).

If Nextclade errors reading your annotation, please read the error message carefully. Common problems include (i) references to non-existing parents, (ii) non-unique names or IDs, and (iii) CDS that are not multiples of 3. To check you annotation, you can run

```bash
nextclade read-annotation my_annotation.gff3
```

## Preparing a minimal `pathogen.json` config file and accompanying files

A `pathogen.json` config file is required to use a dataset with Nextclade web. Luckily, it is very simple to create by hand. All that is required is the schema version, a manifest of files and their paths. In addition, it is recommended to include basic attributes for display in the UI, such as name of the virus and the reference sequence.

Lastly, one can enable basic quality control for frame shifts, stop codons, missing or ambiguous nucleotides and mutation clusters.

```json
{
  "schemaVersion": "3.0.0",
  "files": {
    "reference": "reference.fasta",
    "pathogenJson": "pathogen.json",
    "genomeAnnotation": "genome_annotation.gff3",
    "examples": "sequences.fasta",
    "readme": "README.md",
    "changelog": "CHANGELOG.md"
  },
  "attributes": {
    "name": "Zika virus",
    "reference name": "Zika virus strain MR 766",
    "reference accession": "NC_012532.1"
  },
  "qc": {
    "missingData": {
      "enabled": true,
      "missingDataThreshold": 2000,
      "scoreBias": 500,
      "scoreWeight": 50
    },
    "snpClusters": {
      "enabled": true,
      "windowSize": 100,
      "clusterCutOff": 6,
      "scoreWeight": 50
    },
    "mixedSites": {
      "enabled": true,
      "mixedSitesThreshold": 15,
      "scoreWeight": 50
    },
    "frameShifts": {
      "enabled": true,
      "scoreWeight": 20
    },
    "stopCodons": {
      "enabled": true,
      "scoreWeight": 50
    }
  }
}
```

Further details on the `pathogen.json` file format are available in the [Nextclade docs](https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/05-pathogen-config.html).
The `files` field of the `pathogen.json` is mandatory and has to list all input files Nextclade should expect to find in the dataset.

While only the `reference.fasta` and the `pathogen.json` are required input files, we recommend adding example sequences. These allow users to quickly explore available datasets and help during dataset creation. A README is useful to provide additional information about the dataset. Lastly, a CHANGELOG helps users understand what has changed between different versions of the dataset. As a starting point, they can be minimal:

`README.md`:

```md
# Example dataset for Zika virus

This is a minimal example dataset for demonstration purposes.
```

`CHANGELOG.md`:

```md
## Unreleased

Initial release.
```

(The heading `## Unreleased` is required for the CHANGELOG to be accepted by the Nextclade data repo).
Ultimately, both README and CHANGELOG are intended for users of the dataset and should provide information on what the dataset is intended for and what has changed in the dataset at each update. Notes for dataset creators and curators should instead be documented in the workflow that creates the dataset, not in the dataset itself.

## Testing the minimal dataset

All the files described above are contained in the [`minimal-dataset`](./minimal-dataset) directory with a flat structure:

```txt
minimal-dataset
├── CHANGELOG.md
├── README.md
├── sequences.fasta
├── genome_annotation.gff3
├── pathogen.json
└── reference.fasta
```

The easiest way to test the dataset is via the Nextclade CLI:

```sh
nextclade run \
  minimal-dataset/sequences.fasta \
  --input-dataset minimal-dataset \
  --output-all tmp
```

This runs Nextclade on the example sequences in `minimal-dataset/sequences.fasta` using the dataset in `minimal-dataset`. The results are saved to the `tmp` directory and contain alignment, aligned translations and a summary TSV file.

One can also use the dataset in Nextclade Web by hosting the dataset through a local web server. For example, after having installed `node` and run `npm install -g serve`, one can host the dataset via:

```sh
serve --cors minimal-dataset -l 3000
```

And open Nextclade Web with a URL parameter `dataset-url` pointing to the local web server:

```url
https://master.clades.nextstrain.org/?dataset-url=http://localhost:3000
```

Once the web page loads, you can click "Load example" and click run to test. You may want to reduce the maximum number of nucleotide markers to 500 to prevent Nextclade from freezing (click "Settings" at the top right, then select the "Sequence view" tab and reduce "Max. nucleotide markers to 500).

If the dataset is committed in a Github repository, one can bypass the local web server step and use a Github URL directly:

```url
https://master.clades.nextstrain.org/?dataset-url=gh:nextstrain/nextclade_data@master@/docs/minimal-dataset
```

Due to the lack of reference tree and QC configuration, there will neither be any QC information nor tree view. This will be tackled in the next section.

## Creating a reference tree

While Nextclade can be used without a reference tree, a lot of the functionality is lost. In particular, without reference tree, there is no tree view, no clade assignment and no private mutations QC.

The reference tree is a standard Nextstrain tree in Auspice JSON format, so the general Nextstrain documentation applies. Nextclade specific details are described in the [Nextclade docs](https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/04-reference-tree.html).

We provide a simple Snakemake workflow in this repository at [`example-workflow`](./example-workflow) that builds a reference tree with minimal effort. The workflow can be configured to work with viruses other than Zika by changing the constants (in particular `REFERENCE_ACCESSION`, `TAXON_ID`, and `GENES`) at the top of the [Snakefile](./example-workflow/Snakefile).

You also need to provide paths to the reference sequence (in fasta and genbank formats) and the genome annotation.

The example workflow is a good starting point, but if you want to customize the workflow, it's recommended to consult the Nextstrain documentation, for example the [Creating a pathogen workflow tutorial](https://docs.nextstrain.org/en/latest/tutorials/creating-a-workflow.html).

## Next steps

Once you have your dataset created and committed in a Github repository, you can share it with others through a custom URL, e.g.

```url
https://master.clades.nextstrain.org/?dataset-url=gh:nextstrain/nextclade_data@master@/docs/example-workflow/dataset
```

To make your dataset easily discoverable by all Nextclade users, you can submit it to the Nextclade data repository via a pull request. See the [dataset curation guide](dataset-curation-guide.md) for details. If you have any questions, please post them in the [Nextstrain discussion forum](https://discussion.nextstrain.org/).

## FAQs

### What to do with segmented viruses?

Each segment of a segmented virus should be treated separately and have its own dataset.

### Does Nextclade work for circular genomes?

Nextclade supports circular genomes. Genes that cross the origin are translated according to the GFF3 specifications.

### Does Nextclade support spliced genes?

Yes, Nextclade supports spliced genes. Each exon should be annotated as a separate CDS feature according to the GFF3 specifications. Features belonging to the same translated sequence have to be linked by a common `ID`.

### Does Nextclade support ribosomal slippage?

Yes, Nextclade supports genes with programmed ribosomal frameshifting as long as the CDS is annotated according to the GFF3 specifications.

### Must the reference sequence be at the root of the reference tree?

No, this is not required. However, the mutations from the reference sequence to the root of the tree must be added to the root branch of the tree. This can be achieved automatically by passing the reference sequence to the `--root-sequence` argument of [`augur ancestral`](https://docs.nextstrain.org/projects/augur/en/stable/usage/cli/ancestral.html).

### My virus is very diverse; many sequences don't align!

Nextclade was initially built for the analysis of SARS-COV-2 genomes that were all very similar to the reference. This is reflected in the default alignment parameters. For more diverse viruses, you can tune the alignment and seed-matching parameters by setting these parameters in the `pathogen.json`.
Suggested parameters for high diversity viruses are given below (note that comments are not allowed in JSON, please remove `//...` when copying this into your `pathogen.json`):

```json5
    "alignmentParams": {
        "penaltyGapExtend": 0,             // alignment: allow long gaps (same as default)
        "penaltyGapOpen": 10,              // alignment: make gaps more expensive relative to mismatches (default 6)
        "penaltyGapOpenInFrame": 15,       // alignment: increase the gap opening in coding regions (default 7)
        "penaltyGapOpenOutOfFrame": 17,    // alignment: increase the gap opening in coding regions (default 8)
        "excessBandwidth": 20,             // alignment: increase to allow for compensated indels. (default 9)
        "minSeedCover": 0.1,               // seedmatching: attempt alignment even if less of the sequence is covered by extended seed matched (default 0.33)
        "kmerLength": 6,                   // seedmatching: reduce seed length to find more matches (default 10)
        "kmerDistance": 25,                // seedmatching: reduce to try more seeds (default 50)
        "minMatchLength": 30,              // seedmatching: reduce minimal extended match length to keep more seeds (default 40)
        "allowedMismatches": 15,           // seedmatching: increase allowed mismatches in window_size during seed extension to keep more seeds (default 8)
        "windowSize": 30,
    }
```

You can tweak these parameters further if you think gap penalties should be even higher.

Nextclade CLI uses multiple sources to decide final alignment parameter values. In order of preference:

- CLI arguments of the `nextclade run` command, if provided (e.g. `--min-seed-cover`)
- the fields in `alignmentParams` section of `pathogen.json` file in the dataset, if dataset is used and `alignmentParams` are provided (e.g. `alignmentParams.minSeedCover`)
- built-in hardcoded parameters (in Nextclade software code), when neither of the above is provided

Note that CLI argument names use kebab-case (e.g. `--min-seed-cover`) while the corresponding JSON field names use camelCase (e.g. `minSeedCover`).

You can see the resulting parameter values for a given dataset and command-line by invoking `nextclade run` command in verbose mode: add `--verbose` (`-v`) argument. This will display the final resolved values for all alignment parameters before processing begins.

### My virus is very long with lots of indels; sequences align very poorly!

Long viral genomes, such as mpox or herpes viruses, often have significant length variation in form of large insertions or deletions. In such cases, it can happen that the bandwidth Nextclade provisions in the banded alignment is insufficient and therefore does not align the sequences properly. In such cases, the bandwidth parameters should be adjusted by setting parameters in the `pathogen.json`.
The `mpox/all-clades` dataset uses the following parameters:

```json
  "alignmentParams": {
      "excessBandwidth": 100,
      "terminalBandwidth": 300
  }
```

The `excessBandwidth` is added in addition to what is estimated from the sketched band, `terminalBandwidth` is used for parts of the sequence before the first or after the last seed where indel variation is common and can't be reliably sketched.

> ⚠️ Increasing these parameters increases the memory requirements and run-times of Nextclade.

### How can I align short fragments?

By default, Nextclade requires sequences to be at least 100 bases long. You can reduce this by setting

```json
  "alignmentParams": {
      "minLength": 30,
      "minMatchLength": 20,
      "kmerDistance": 3,
      "kmerLength": 6,
  }
```

### Can I preview how Nextclade reads my annotation file?

Yes. Try to run

```bash
nextclade read-annotation my_annotation.gff3
```

Nextclade will print a formatted output of how your gff3 is interpreted. If there are problems reading your annotation, Nextclade tries to identify the problem and prints an informative error message.

### How many example sequences should I include?

Example sequences are meant for users to test the dataset and to help curators to develop the dataset. A few dozen sequences that cover viral diversity and different use cases (partial/complete, high quality/low quality) are usually sufficient. Too large example datasets make testing cumbersome, and increase storage and compute requirements necessarily. Ideally, the example sequences are different from the sequences use for the reference tree.

### Should I make multiple datasets for the same virus with different reference sequences?

In earlier versions, Nextclade only reported mutations relative to the alignment reference and private mutations. At that time, it was useful to have datasets that use different reference sequences (e.g. ancestral SARS-CoV-2 Wuhan-Hu-1 and Omicron). Now, Nextclade also reports mutations relative to clade/lineage founders as well as specific strains that can be specified in the `auspice.json`.
Unless the virus is very diverse and there are clearly recognized 'types' (e.g. Dengue 1-4), it is preferable to provide only a single dataset. This reduces ambiguities with what dataset sequences should be analyzed and simplifies the automated dataset suggestion.

The documentation on how to specify reference strains relative to which mutations should be reported can be found [here](https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/04-reference-tree.html#relative-mutations).

### Are whole-genome datasets preferable to partial genome datasets?

Yes, at least for viruses with limited recombination. A full genome dataset will cover most use cases and will provide all the functionality that a partial genome dataset does.
Exceptions to this recommendation include cases where relevant diversity is not represented in the available complete sequences.

### How do I add multiple nomenclature systems to my dataset?

Nextclade supports adding multiple 'clade-like' attributes to the reference tree. These need to be assigned to the nodes of the reference tree (for example using `augur clades`) and specified in the `tree.json` file. Please consult the documentation on [clade-like attributes](https://docs.nextstrain.org/projects/nextclade/en/latest/user/input-files/04-reference-tree.html#clade-like-attributes).
