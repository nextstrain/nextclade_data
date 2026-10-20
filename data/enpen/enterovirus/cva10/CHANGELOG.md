## Unreleased

Initial release of an Coxsackievirus A10 dataset for lineage classification!

The dataset adds a penalty for deletions that start before a CDS and run into it (`penaltyGapEnterCds: 6`, requires Nextclade 3.25.0 or newer), so that ambiguous deletions in the 5' UTR do not remove the VP4 start codon. The example sequences include MW929252, a genome with such a deletion.

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
