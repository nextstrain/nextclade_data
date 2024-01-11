# Nextclade dataset creation guide

This guide describes how to create a new Nextclade dataset from scratch. Datasets are how Nextclade is customized to work with a particular virus.

Once a dataset is created, it can be shared with other users via the Nextclade data repository or a separate Github repository.

## Recommended prerequisites

- Knowledge of command line bioinformatics
- Basic knowledge of Nextclade, in particular of the Nextclade CLI
- Familiarity with Nextstrain's augur toolchain (not strictly necessary, but helpful)
- Ability to read a simple Snakemake workflow

## Overview

A Nextclade dataset is a collection of files. While Nextclade CLI can be used with as little as a reference sequence, a full dataset to be used with Nextclade web requires a general configuration file as well. The full set of files is as follows:

1. A reference sequence against which to align user-provided sequences (required)
1. A genome annotation for the reference sequence in GFF3 format (recommended)
1. A phylogenetic tree in Auspice JSON format (optional)
1. A general configuration file (`pathogen.json`) in JSON format (required for Nextclade Web)

The official specification of these files is available in the Nextclade docs at https://docs.nextstrain.org/projects/nextclade/en/latest/.

The guide here complements the specifications by going through a concrete workflow that produces these files for an example virus (Zika).

## Choosing a reference sequence

As all sequences are aligned to the reference sequence and all mutations are reported relative to it, the choice of the reference sequence is important.

A good reference sequence should be of high quality and cover the entire genome (or at least the regions of interest).

A good default choice is an NCBI refseq. For example, for Zika virus, the NCBI refseq is `NC_012532.1`. It is available in GenBank at <https://www.ncbi.nlm.nih.gov/nuccore/NC_012532.1>.

If all current circulation is derived from a more recent common ancestor, it may be better to use a more recent reference sequence to reduce the number of mutations reported.

## Preparing the genome annotation

Nextclade uses the genome annotation to determine how to extract amino acid sequences from aligned nucleotide sequences. Nextclade requires the genome annotation to be in [GFF3 format](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md). Nextclade only uses the `CDS` feature type. Each `CDS` feature is treated separately for translation, alignment and amino acid mutation reporting.

While Genbank provides annotations in GFF3 format, there is often a discrepancy between what the dataset creator wants to be translated and what is annotated as a CDS in the Genbank provided GFF3 file. In addition, users may want to change names of CDS features to make them more readable in Nextclade output.

For example, the Genbank GFF3 file for the Zika refseq has a single CDS feature for the entire polyprotein with a cryptic `Name` "YP_002790881.1". Instead, one may want to translate each mature protein separately and give them more readable names. This can be done by editing the GFF3 file by hand, or by using a custom script. By hand, we can remove the existing CDS feature and renaming all `mature_protein_region_of_CDS` feature types to `CDS`. Overlapping precursors can be removed as well, as appropriate. In addition, a `gene` attribute can be added with the name one wants to see in Nextclade. Unfold the section below to see both the original and the modified GFF3 files:

<details>
<summary> Genbank provided GFF3 file for the Zika refseq `NC_012532.1` </summary>

```gff3
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
##sequence-region NC_012532.1 1 10794
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=64320
NC_012532.1	RefSeq	region	1	10794	.	+	.	ID=NC_012532.1:1..10794;Dbxref=taxon:64320;country=Uganda;gbkey=Src;genome=genomic;mol_type=genomic RNA;nat-host=sentinel monkey;note=mosquito-borne flavivirus;strain=MR 766
NC_012532.1	RefSeq	five_prime_UTR	1	106	.	+	.	ID=id-NC_012532.1:1..106;gbkey=5'UTR
NC_012532.1	RefSeq	gene	107	10366	.	+	.	ID=gene-ZIKV_gp1;Dbxref=GeneID:7751225;Name=POLY;gbkey=Gene;gene=POLY;gene_biotype=protein_coding;locus_tag=ZIKV_gp1
NC_012532.1	RefSeq	CDS	107	10366	.	+	0	ID=cds-YP_002790881.1;Parent=gene-ZIKV_gp1;Dbxref=GenBank:YP_002790881.1,GeneID:7751225;Name=YP_002790881.1;gbkey=CDS;gene=POLY;locus_tag=ZIKV_gp1;product=polyprotein;protein_id=YP_002790881.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	107	472	.	+	.	ID=id-YP_002790881.1:1..122;Parent=cds-YP_002790881.1;gbkey=Prot;product=anchored capsid protein ancC;protein_id=YP_009227206.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	107	418	.	+	.	ID=id-YP_002790881.1:1..104;Parent=cds-YP_002790881.1;gbkey=Prot;product=capsid protein C;protein_id=YP_009227196.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	473	976	.	+	.	ID=id-YP_002790881.1:123..290;Parent=cds-YP_002790881.1;gbkey=Prot;product=membrane glycoprotein precursor prM;protein_id=YP_009227197.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	473	751	.	+	.	ID=id-YP_002790881.1:123..215;Parent=cds-YP_002790881.1;gbkey=Prot;product=protein pr;protein_id=YP_009227207.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	752	976	.	+	.	ID=id-YP_002790881.1:216..290;Parent=cds-YP_002790881.1;gbkey=Prot;product=membrane glycoprotein M;protein_id=YP_009227208.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	977	2476	.	+	.	ID=id-YP_002790881.1:291..790;Parent=cds-YP_002790881.1;gbkey=Prot;product=envelope protein E;protein_id=YP_009227198.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	2477	3532	.	+	.	ID=id-YP_002790881.1:791..1142;Parent=cds-YP_002790881.1;gbkey=Prot;product=nonstructural protein NS1;protein_id=YP_009227199.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	3533	4210	.	+	.	ID=id-YP_002790881.1:1143..1368;Parent=cds-YP_002790881.1;gbkey=Prot;product=nonstructural protein NS2A;protein_id=YP_009227200.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	4211	4600	.	+	.	ID=id-YP_002790881.1:1369..1498;Parent=cds-YP_002790881.1;gbkey=Prot;product=nonstructural protein NS2B;protein_id=YP_009227201.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	4601	6451	.	+	.	ID=id-YP_002790881.1:1499..2115;Parent=cds-YP_002790881.1;gbkey=Prot;product=nonstructural protein NS3;protein_id=YP_009227202.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	6452	6832	.	+	.	ID=id-YP_002790881.1:2116..2242;Parent=cds-YP_002790881.1;gbkey=Prot;product=nonstructural protein NS4A;protein_id=YP_009227203.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	6833	6901	.	+	.	ID=id-YP_002790881.1:2243..2265;Parent=cds-YP_002790881.1;gbkey=Prot;product=protein 2K;protein_id=YP_009227209.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	6902	7654	.	+	.	ID=id-YP_002790881.1:2266..2516;Parent=cds-YP_002790881.1;gbkey=Prot;product=nonstructural protein NS4B;protein_id=YP_009227204.1
NC_012532.1	RefSeq	mature_protein_region_of_CDS	7655	10363	.	+	.	ID=id-YP_002790881.1:2517..3419;Parent=cds-YP_002790881.1;gbkey=Prot;product=RNA-dependent RNA polymerase NS5;protein_id=YP_009227205.1
NC_012532.1	RefSeq	three_prime_UTR	10367	10794	.	+	.	ID=id-NC_012532.1:10367..10794;gbkey=3'UTR
```

</details>

<details>
<summary> Modified GFF3 file for the Zika refseq `NC_012532.1` </summary>

```gff3
##gff-version 3
##sequence-region NC_012532.1 1 10794
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=64320
NC_012532.1	RefSeq	region	1	10794	.	+	.	ID=NC_012532.1:1..10794;Dbxref=taxon:64320;country=Uganda;gbkey=Src;genome=genomic;mol_type=genomic RNA;nat-host=sentinel monkey;note=mosquito-borne flavivirus;strain=MR 766
NC_012532.1	RefSeq	gene	107	10366	.	+	.	ID=gene-ZIKV_gp1;Dbxref=GeneID:7751225;Name=POLY;gbkey=Gene;gene=POLY;gene_biotype=protein_coding;locus_tag=ZIKV_gp1
NC_012532.1	RefSeq	CDS	107	472	.	+	.	ID=id-YP_002790881.1:1..122;gene-ZIKV_gp1;gbkey=Prot;product=anchored capsid protein ancC;protein_id=YP_009227206.1;gene=CA
NC_012532.1	RefSeq	CDS	473	751	.	+	.	ID=id-YP_002790881.1:123..215;gene-ZIKV_gp1;gbkey=Prot;product=protein pr;protein_id=YP_009227207.1;gene=PRO
NC_012532.1	RefSeq	CDS	752	976	.	+	.	ID=id-YP_002790881.1:216..290;gene-ZIKV_gp1;gbkey=Prot;product=membrane glycoprotein M;protein_id=YP_009227208.1;gene=MP
NC_012532.1	RefSeq	CDS	977	2476	.	+	.	ID=id-YP_002790881.1:291..790;gene-ZIKV_gp1;gbkey=Prot;product=envelope protein E;protein_id=YP_009227198.1;gene=ENV
NC_012532.1	RefSeq	CDS	2477	3532	.	+	.	ID=id-YP_002790881.1:791..1142;gene-ZIKV_gp1;gbkey=Prot;product=nonstructural protein NS1;protein_id=YP_009227199.1;gene=NS1
NC_012532.1	RefSeq	CDS	3533	4210	.	+	.	ID=id-YP_002790881.1:1143..1368;gene-ZIKV_gp1;gbkey=Prot;product=nonstructural protein NS2A;protein_id=YP_009227200.1;gene=NS2A
NC_012532.1	RefSeq	CDS	4211	4600	.	+	.	ID=id-YP_002790881.1:1369..1498;gene-ZIKV_gp1;gbkey=Prot;product=nonstructural protein NS2B;protein_id=YP_009227201.1;gene=NS2B
NC_012532.1	RefSeq	CDS	4601	6451	.	+	.	ID=id-YP_002790881.1:1499..2115;gene-ZIKV_gp1;gbkey=Prot;product=nonstructural protein NS3;protein_id=YP_009227202.1;gene=NS3
NC_012532.1	RefSeq	CDS	6452	6832	.	+	.	ID=id-YP_002790881.1:2116..2242;gene-ZIKV_gp1;gbkey=Prot;product=nonstructural protein NS4A;protein_id=YP_009227203.1;gene=NS4A
NC_012532.1	RefSeq	CDS	6833	6901	.	+	.	ID=id-YP_002790881.1:2243..2265;gene-ZIKV_gp1;gbkey=Prot;product=protein 2K;protein_id=YP_009227209.1;gene=2K
NC_012532.1	RefSeq	CDS	6902	7654	.	+	.	ID=id-YP_002790881.1:2266..2516;gene-ZIKV_gp1;gbkey=Prot;product=nonstructural protein NS4B;protein_id=YP_009227204.1;gene=NS4B
NC_012532.1	RefSeq	CDS	7655	10363	.	+	.	ID=id-YP_002790881.1:2517..3419;gene-ZIKV_gp1;gbkey=Prot;product=RNA-dependent RNA polymerase NS5;protein_id=YP_009227205.1;gene=NS5
```

</details>

Alternatively, one can use a custom script to perform these tasks. We provide an interactive script in [`example-workflow/scripts/generate_from_genbank.py`](./example-workflow/scripts/generate_from_genbank.py) that requires an NCBI accession as input and walks the user through the process of picking the CDS features and naming them.

## Preparing a minimal `pathogen.json` configuration file

A `pathogen.json` config file is required to use a dataset with Nextclade web. Luckily, it is very simple to create by hand. All that is required is the schema version, a manifest of files and their paths. In addition, it is recommended to include basic attributes for display in the UI, such as name of the virus and the reference sequence.

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
  }
}
```

Adding example sequences is useful to allow users (and dataset creators) to quickly test the dataset. A README is useful to provide additional information about the dataset. Lastly, a CHANGELOG helps users understand what has changed between different versions of the dataset. As a starting point, they can be minimal:

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

## FAQs

### What to do with segmented viruses?

Each segment of a segmented virus should be treated separately and have its own dataset.

### Does Nextclade work for circular genomes?

Nextclade supports circular genomes. Genes that cross the origin are translated according to the GFF3 specifications.

### Does Nextclade support spliced genes?

Yes, Nextclade supports spliced genes. Each exon should be annotated as a separate CDS feature according to the GFF3 specifications.

### Does Nextclade support ribosomal slippage?

Yes, Nextclade supports genes with programmed ribosomal frameshifting as long as the CDS is annotated according to the GFF3 specifications.

### Must the reference sequence be at the root of the reference tree?

No, generally this is not required, however, the mutations from the reference sequence to the root of the tree must be added to the root branch of the tree. This can be achieved automatically by passing the reference sequence to the `--root-sequence` argument of [`augur ancestral`](https://docs.nextstrain.org/projects/augur/en/stable/usage/cli/ancestral.html).

```

```

```

```
