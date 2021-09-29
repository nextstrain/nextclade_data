## 2021-09-30

### SARS-CoV-2 

#### New dataset version (tag `2021-09-30T20:13:05Z`)

 - Clades: changed name of clade "21H" to "21H (Mu)", as it became a WHO VoC
 - Reference tree: masked a number of mutations that were either homoplasic (occurred independently in multiple lineages) or were error-prone, to prevent these mutations from distorting the tree is now produced from a dedicated workflow that’s openly available and thus reproducible
 - Reference tree: changed sequence filtering to improve diversity on the tree, while excluding low quality sequences. For this we use the list of designated pango lineages.
 - Included newer sample data

The Augur workflow for reference tree generation is now available at [TODO: add a link to the workflow](https://example.com)


## 2021-08-31

Initial release of Nextclade Datasets.

It includes the existing SARS-CoV-2 dataset from 
[github.com/nextstrain/nextclade/data/sars-cov-2](https://github.com/nextstrain/nextclade/tree/0817313f674471a49803cf1970bc92832207b4f5/data/sars-cov-2) as well as 4 new flu datasets: 

 - Influenza A H1N1pdm (rooted at "A/California/07/2009")
 - Influenza A H3N2 (rooted at "A/Wisconsin/67/2005")
 - Influenza B Victoria (rooted at "B/Brisbane/60/2008")
 - Influenza B Yamagata (rooted at "B/Wisconsin/01/2010")
