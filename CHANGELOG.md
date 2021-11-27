## 2021-11-27

### SARS-CoV-2

#### New dataset version (tag `2021-11-27T11:53:22Z`)

##### Changes

- Clades: `21K` is renamed `21K (Omicron)` in line with WHO elevation to VOC status

## 2021-11-26

### SARS-CoV-2

#### New dataset version (tag `2021-11-26T14:02:45Z`)

##### Changes

- Data source: GISAID data is now used to generate the reference tree. This switch is necessary, because the new clade 21K (B.1.1.529) is only present in GISAID data, thus far.

##### Updates

- New clade: 21K (B.1.1.529) has been added to the reference tree
- Reference tree: Data has been updated to sequences submitted to GISAID by 2021-11-24
- Reference tree: Pango lineages designated until 2021-11-24 have been sampled into the tree

## 2021-11-16

### SARS-CoV-2

#### New dataset version (tag `2021-11-16T16:38:05Z`)

##### Changes

- Reference tree: Recombinant pango lineages (= those starting with `X`) have been excluded in order to reduce clade misassignment noise, in particular for short sequences like just `S`. Only one recombinant has been designated so far (`XA`) and it broke up the branch leading up to Alpha exerting bad influence that warranted removal.
- QC rules: The lists of known, (likely) biological and thus acceptable frame shifts and stop codons have been extended. The ~20 most common frame shifts and ~40 most common stop codons on genes `ORF3a/6/7a/7b/8` are now declared known. Common frame shifts and stops on `ORF1a/b` and `S` are not declared known since these are most likely sequencing artefacts and not biological.

##### Updates

- Reference tree: Data has been updated to sequences submitted to Genbank by mid November
- Reference tree: Pango lineages designated until 2021-11-04 have been sampled into the tree
- Sample sequences

## 2021-10-11

### SARS-CoV-2

#### New dataset version (tag `2021-10-11T19:00:32Z`)

- Clades: Two Delta subclades have been designated by Nextstrain and are now included in Nextclade, see [Twitter announcement](https://twitter.com/nextstrain/status/1446903892864737280):
   > We've just updated Nextstrain clade designations to partition clade 21A (corresponding to the Delta WHO variant) into subclades 21I and 21J following our previously defined rules for defining clades when mutational and frequency thresholds are met.
   > Clade 21I is still a Delta variant virus, but possesses additional spike mutation A222V and ORF1a mutations P1640L, A3209V, V3718A and T3750I.
   > Clade 21J is still a Delta variant virus, but possesses additional ORF1a mutations A1306S, P2046L, P2287S, V2930L, T3255I and T3646A, ORF7b mutation T40I, as well as N mutation G215C. Clade 21J is now the predominate form of Delta with an estimated ~79% global frequency.
   > Clade defining mutations for clades 21I and 21J can be found in our public GitHub repo at: <https://github.com/nextstrain/ncov/blob/master/defaults/clades.tsv#L102>.
- Reference tree: Data has been updated to sequences submitted to Genbank by the first week of October.
- Reference tree: Pango lineages designated until 2021-10-10 have been sampled into the tree, including among others: AY.4.1-3, AY.34-39 [see pango release changes](https://github.com/cov-lineages/pango-designation/compare/v1.2.77...v1.2.84)

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
