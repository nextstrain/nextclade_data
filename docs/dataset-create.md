# How to create a new Nextclade dataset

This guide will tell how to add support for a new pathogen or a new variant of a pathogen to Nextclade.

This guide assumes you have some basic knowledge about Nextclade and is capable of using either Nextclade Web, Nextclade CLI or both. If it's not the case, please refer to [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/index.html).

## General information

[Nextclade software](https://github.com/nextstrain/nextclade) is able to perform general tasks, such as alignment, translation and analysis of genetic sequences, however it has no knowledge of concrete pathogens. For example, Nextclade does not know about the structure of a particular genome or about phylogenetic relationships between clades. Instead, it relies on so-called "datasets" to get this information. A Nextclade dataset is a directory of files (or a zip archive of this directory).

A certain number of the "official" datasets is hosted on the internet, along with a [datasets index file](https://data.clades.nextstrain.org/index_v2.json), allowing Nextclade Web and Nextclade CLI to discover these datasets and perform analysis of sequences of the pathogens they describe.

## Creating a dataset

This section assumes general familiarity with Nextclade datasets from a user standpoint. If this is not the case, please refer to [Nextclade user documentation on datasets](https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html).

> Note that building datasets have been mostly handled by the Nextclade team internally so far. The process has evolved over time and might contain various nuances that are not obvious without knowing historical context. Not everything is very well documented and external contributors may find the process challenging. But we are hoping to improve this as the feedback comes in.
>
> Additionally, please note that maintainers may not necessarily be experts on a particular pathogen you are interested in. It is important to know the pathogen's specifics to make Nextclade analysis results sound and practically useful. And yes, Nextclade can produce unsound and nonsensical results if the dataset is wrong. There is a certain amount of work and experimentation involved in creating a high-quality dataset, so be prepared for a journey, rather than a quick sprint.
>
> In any case, feel free to reach out to the team if you notice bugs, have questions, or ideas on how to improve Nextclade software or its dataset infrastructure.


Here we describe how to build a directory of files that constitute a single dataset. Having these files makes it possible for Nextclade to analyze a particular pathogen or a variant of a pathogen. It's up to you to decide what you call a pathogen - a whole species or a very narrow variant (e.g. a particular vaccine strain or a local outbreak). This information will be encoded into the dataset and Nextclade will obey your rules, no matter what they are.

If you have multiple variants of a pathogen, and you want to analyze them all separately, you can have multiple related datasets with different names or with the same name, but different set of dataset attributes (e.g. different reference sequence). If you haven't decided on the granularity of variants, you could try to start with fewer, coarse grained datasets (or even one, global dataset) and if it does not suit your needs, to create more specialized datasets.

A Nextclade dataset consists of the following files:

- Reference sequence (`reference.fasta`)
- Reference tree (`tree.json`)
- Genome annotation (`genemap.gff`)
- Table describing PCR primer regions of the genome (`primers.csv`)
- Quality Control for this pathogen (`qc.json`)
- Remaining properties specific to this pathogen (`virus_properties.json`)
- (optional) Example query sequence data (`sequences.fasta`)

Read more about Nextclade input files in the [user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/input-files.html).

The most certain way of getting started, is to look at one of the existing datasets and try to mimic it, while adjusting things that are specific to your new pathogen. The most mature are the SARS-CoV-2 datasets.

The next sections will describe how to create each file.

### Reference tree (`tree.json`)

This is the hardest and most important side of the dataset. The reference tree provide information about phylogenetic relationships, clades and mutations characteristic of particular clades.

### Reference sequence (`reference.fasta`)

TODO

### (optional) Example query sequence data (`sequences.fasta`)

During dataset development, you might want to test your dataset on a particular subset of interesting or representative sequences. You could gather these sequences and provide them as a part of the dataset. For end-users these samples allow to quickly look at the results Nextclade provides, asses practical utility of Nextclade for their work, and also they may serve as a reference to compare their own sequences to.

The official datasets typically attempt to cover the whole diversity of different clades present in the reference tree, for the whole species, or to highlight Nextclade software features, such as visualizing particular mutations or frame shifts.

### Genome annotation (`genemap.gff`)

TODO

### Table describing PCR primer regions of the genome (`primers.csv`)

TODO

### Quality Control for this pathogen (`qc.json`)

TODO

### Remaining properties specific to this pathogen (`virus_properties.json`)

TODO
