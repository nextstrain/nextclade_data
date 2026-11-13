## Unreleased
- Initial dataset creation
- GFF3 annotation with CDS
- Reference FASTA AF009606.1
- QC: the thresholds of the private mutations, mixed sites and missing data rules scale with the length of each sequence. A sequence that covers only a part of the genome, such as one gene, is judged by the density of mutations, ambiguous nucleotides and missing data, instead of by thresholds for the full genome. Nextclade versions without QC length scaling ignore this setting and keep the thresholds for the full genome.