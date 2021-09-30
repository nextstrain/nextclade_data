## 2021-09-30

### SARS-CoV-2 

#### New dataset version (tag `2021-09-30T08:13:05Z`)

 - Clades: changed name of clade "21H" to "21H (Mu)", as it has been designated a VOC by WHO
 - Reference tree: masked a number of mutations that were either homoplasic (occurred independently in multiple lineages) or were error-prone (in Delta), to prevent these mutations from distorting the tree.
 - Reference tree: now produced from a dedicated workflow that’s openly available and can be reproduced by anyone interested. The data used comes from Genbank, so it's publicly available and sharable by anyone without restrictions.
 - Reference tree: changed sequence filtering to improve diversity on the tree, while excluding low quality sequences. For this we use the list of designated pango lineages. Every designated pango lineage with sequences in the last few months is represented on the reference tree.
 - Reference tree: The new tree contains sequences that were published to Genbank up to mid September
 - Example sequences: New example sequences are provided. Every Nextstrain clade is represented by at least 3 sequences. Furthermore, sequences that make the two QC rules `SNP cluster` and `rare mutations` fire have been added, to allow users to observe how such problematic sequences are flagged by Nextclade.
 - QC rules: The following premature stop codons are treated as known and thus not indicative of quality problems: `ORF7a:62, ORF7a:94, ORF7b:33, ORF7b:39, ORF8:18, ORF8:19, ORF8:26, ORF8:27, ORF8:59, ORF8:67, ORF8:68, ORF8:106`.
 - QC rules: The following frameshifts are treated as known and thus not indicative of quality problems: `ORF3a:257-276, ORF3a:259-276, ORF7a:62-122, ORF7a:63-122, ORF7a:77-122, ORF7a:102-122, ORF7b:42-44, ORF8:108-122, ORF8:120-122, ORF8:121-122, ORF8:122-123`.
 - QC rules: The known stop codons and frameshifts were selected based on roughly the following criteria:
   - observed at least 5 times
   - observed in more than one lab
   - observed in sequences that are otherwise devoid of quality issues
   - observed in genes that are probably not essential for virus function

The Snakemake workflow producing the reference tree is now available at [github.com/neherlab/nextclade_data_workflows](https://github.com/neherlab/nextclade_data_workflows).


## 2021-08-31

Initial release of Nextclade Datasets.

It includes the existing SARS-CoV-2 dataset from 
[github.com/nextstrain/nextclade/data/sars-cov-2](https://github.com/nextstrain/nextclade/tree/0817313f674471a49803cf1970bc92832207b4f5/data/sars-cov-2) as well as 4 new flu datasets: 

 - Influenza A H1N1pdm (rooted at "A/California/07/2009")
 - Influenza A H3N2 (rooted at "A/Wisconsin/67/2005")
 - Influenza B Victoria (rooted at "B/Brisbane/60/2008")
 - Influenza B Yamagata (rooted at "B/Wisconsin/01/2010")
