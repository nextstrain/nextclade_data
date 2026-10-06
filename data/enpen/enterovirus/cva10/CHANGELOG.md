## Unreleased

Initial release of an Coxsackievirus A10 dataset for lineage classification!

The dataset adds a penalty for deletions that start before a CDS and run into it (`penaltyGapEnterCds: 6`, available in Nextclade versions newer than 3.24.0), so that ambiguous deletions in the 5' UTR do not remove the VP4 start codon. Older Nextclade versions ignore this setting.

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
