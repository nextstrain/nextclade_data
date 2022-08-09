# CHANGELOG

## 2022-08-09

### New dataset version (tag `2022-08-09T12:00:00Z`)

#### All Monkeypox datasets

The datasets now include  hMPXV-1 lineages B.1.1 to B.1.5. See details in https://github.com/nextstrain/monkeypox/pull/95

Sequences released to Genbank up to 2022-08-08 have been included in the new trees.

A B.1.5 sequence from Genbank has been added to the example sequences

##### MPXV (All clades)

Sequence KJ642615 (W-Nigeria/1971) has been excluded as it appears to be recombinant of clade 2 and clade 3. See details in https://github.com/nextstrain/monkeypox/pull/102 - this sequence is not present in the other datasets, so no change there

## 2022-07-27

### Influenza Yamagata HA

#### Bug fix release (tag `2022-07-27T12:00:00Z`)

Fix: The old tree used an incorrect genemap which caused Nextclade to crash. Now it works again.

Beware that Nextclade v2.0.0 until v2.3.0 have had a bug that means this dataset will crash.

You will have to upgrade to Nextclade v2.3.1 or use Nextclade v1 to use this dataset.

## 2022-07-26

### SARS-CoV-2 and SARS-CoV-2-no-recomb

#### Bug fix release (tag `2022-07-26T12:00:00Z`)

Fix: Ancestral reconstruction of mutations was wrong due to recombinants attaching directly to the root and causing the root mutations to be different from Wuhan.

This caused:

- _displayed_ mutations in Auspice to be wrong for all tips since around the time recombinants were first included in the tree (since `2022-03-24T12:00:00Z`)
- Some of the _calculated_ reconstructed mutations on _recombinants_ to be wrong, affecting nearest neighbor placement of _some_ recombinants.

The fix will cause a few recombinants to become recombinants and improve QC values of some recombinants but should not have large effects overall.
The biggest perceived impact will be that mutations displayed by Auspice will now be correct.

## 2022-07-22

### SARS-CoV-2 and SARS-CoV-2-no-recomb

#### New dataset version (tag `2022-07-22T12:00:00Z`)

- Clades: BA.2.75 has been given the Nextstrain clade name `22D`. Read more about the reasoning for the decision to give this lineage a name here <https://github.com/nextstrain/ncov/pull/984>
- Data update: New pango lineages are included up to commit <https://github.com/cov-lineages/pango-designation/compare/65cb2e04de0dc311600b396f7119babeb051b40e...42134608ae645853c333591ddadc345bfaf7ec13>)
- Fix: BA.2.38 no longer contains `6091T` as defining mutation, should therefore catch many more Indian BA.2.38 (report by @silcn in https://github.com/nextstrain/nextclade/issues/935)
- Fix: Genemap format now correct, compliant with GFF3, see https://github.com/nextstrain/nextclade_data/issues/33 (report by @huddlej)
- virus_properties.json has been updated, including clade `22D`

## 2022-07-12

### SARS-CoV-2

#### New dataset version (tag `2022-07-12T12:00:00Z`)

- Fix: BA.2.75 lacked the characteristic S:R493Q reversion in the previous release, this is now fixed. This is the only change, otherwise this dataset is identical to `2022-07-11T12:00:00Z`.

## 2022-07-11

### SARS-CoV-2

#### New dataset version (tag `2022-07-11T12:00:00Z`)

- Pango lineages: In this release, Nextclade can assign Pango lineages up to BA.2.75 (commit https://github.com/cov-lineages/pango-designation/commit/65cb2e04de0dc311600b396f7119babeb051b40e)
- Alignment params: Retry reverse complement flag is now set to true, so that reverse complement is tried if seed matching fails.
- Fixes: Some synthetic pango lineage sequences had wrong mutations, this is now fixed through a manually curated override file.

## 2022-06-29

### MPXV B.1

#### New dataset version (tag `2022-06-29T12:00:00Z`)

- Increased number of B.1 samples from ~100 to ~200 to improve phylogenetic placement of analyzed 2022 outbreak sequences

## 2022-06-27

### New dataset version (tag `2022-06-27T12:00:00Z`)

#### SARS-CoV-2

- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.11, featuring a host of new BA.2, BA.4 and BA.5 sublineages and recombinants.
- Alignment params: Retry reverse complement flag is now set to true, so that reverse complement is tried if seed matching fails.

## 2022-06-16

### New dataset version (tag `2022-06-16T12:00:00Z`)

#### MPXV All Clades

- Reduced number of sample sequences to reduce number of markers and therefore improve web display performance

## 2022-06-14

### 3 Monkeypox (MPXV) datasets introduced

Three MPXV datasets are added with differing zoom levels containing:

- MPXV (All clades)
- hMPXV-1 (part of clade 3, source of 2017/2018/2022 outbreaks)
- hMPXV-1 B.1 (2022 outbreak lineage)

All 3 use the coordinate system of the recently designated NCBI Monkeypox reference sequence NC_063383 (MPXV-M5312_HM12_Rivers).

However, SNPs from two different ref sequences are added to the "all clades" and B.1 datasets to reduce the number of total mutations.

The B.1 datset uses SNPs of ON563414.3 (MPXV_USA_2022_MA001) on top of a NC_063383 backbone.

The "all clades" build uses the SNPs of a reconstructed ancestral MPXV sequence that is the inferred most recent common ancestor of clades 1, 2 and 3, rooted with a Cowpox outgroup.

Only the MPXV (All clades) dataset can assign all clades 1, 2 and 3.
The hMPXV-1 dataset can be used if all viruses are from hMPXV-1.
The B.1 dataset is useful for 2022 outbreak sequences but will not be able to assign anything but B.1 lineages.

Gene annotations follow the annotation used by NC_063383 and is of the form `OPG001` (for OrthoPox Gene 001).
Since the alignment reference is always in NC_063383 coordinates, nucleotide and protein mutation position should usually be identical in alignments done with all three datasets.

Quality control parameters are subject to change, especially since "known" frame shifts and stop codons have not been annotated. For example, clade 1 sequences will always show around 7 frame shifts, yet these do not indicate quality problems.

### New dataset version (tag `2022-06-14T12:00:00Z`)

#### SARS-CoV-2

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.9 and beyond are now included, including among others `BA.5.1-BA.5.3`, `BA.2.35-BA.2.48` and `XV-XY`

## 2022-04-28

### New dataset version (tag `2022-04-28T12:00:00Z`)

#### SARS-CoV-2 (with and without recombinants)

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.8 are now included, including among others `BA.3.1`, `BA.2.14-BA.2.34` and `XT-XU` (in the default build, excluded from special "without recombinants" dataset).
- Clades: New Nextstrain clades included. `BA.4` is `22A (Omicron)`, `BA.5` is `22B (Omicron)` and `BA.2.12.1` is `22C (Omicron)`.

## 2022-04-08

### New dataset version (tag `2022-04-08T12:00:00Z`)

#### SARS-CoV-2 (with and without recombinants)

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.4 are now included, including among others `BA.4-5`, `BA.2.9-BA.2.13` and `XM-XS` (in the default build, excluded from special "without recombinants" dataset). For now, `BA.4-5` are included in Nextstrain clade `21L`, together with `BA.2` which is the most similar Omicron.
- Reference tree: The first 100 and last 200 sites (with respect to Wuhan reference) are now masked in the reference tree to reduce noise due to sites like `21` that were artifactually polymorphic.

## 2022-03-31

### New dataset version (tag `2022-03-31T12:00:00Z`)

#### SARS-CoV-2 (with and without recombinants)

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.137 are now included, including among others `BA.1.18-19`, `BA.2.4-BA.2.8` and `XG-XK` (in the default build, excluded from special "without recombinants" dataset).
- Dataset: The sampling of sequences has changed slightly. Previously, every Nextstrain clade got around 30 random sequences belonging to this clade causing quite a bit of movement between releases. This is no longer the case. The tree is thus slightly smaller. The change is most noticeable for small Nextstrain clades like `20F`.

## 2022-03-24

### New dataset version (tag `2022-03-24T12:00:00Z`)

#### SARS-CoV-2

- Recombinants: Recombinant Pango lineages are now included in the reference tree. Each recombinant is attached to the root node so as not to spawn false internal nodes in the tree that would attract bad sequences. As long as recombinants do not qualify for a Nextstrain clade, they will receive the place holder clade name `recombinant`. Pango lineages are provided if present. Beware that new unnamed recombinants with similar donors but slightly different breakpoint will attach to existing recombinants in the reference tree and thus get a wrong Pango lineage. A number of reversions and labeled mutations is a sign that you may have a similar but different recombinant.
- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.133, featuring Omicron recombinants like `XD`, `XE` and `XF`.
- QC: `qc.json` was updated with the most common stop codons and frameshifts that appear to be real and not artefacts (in ORFs 3a, 6, 7a, 7b,8, 9b)
- QC: `virus_properties.json` was updated and now contains more mutations that are common in `21K` which should help identifying recombinants

#### SARS-CoV-2 without recombinants

- New dataset: Now that recombinants are included in the default SARS-CoV-2 tree, it is no longer easy to identify breakpoints and donors of new recombinants if they attach to existing recombinants on the tree. To facilitate the analysis of new potential recombinants, we have added a new dataset named "SARS-CoV-2 without recombinants" that does not include recombinants and can thus be used for recombinant analysis as before the inclusion of recombinants. This dataset should only be used for recombinant analysis, it will receive less attention than the main (default) SARS-CoV-2 dataset.
- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.133, except recombinants (lineages starting with `X`).

## 2022-03-14

### New dataset version (tag `2022-03-14T12:00:00Z`)

#### SARS-CoV-2

- Pango lineages: Nextclade now assigns sequences a pango lineage, similar to how clades are assigned. Output is visible in both web and tsv/csv output (column `Nextclade_pango`). The classifier is about 98% accurate for sequences from the past 12 months. Older lineages are deprioritised, and accuracy is thus worse. Read more about the method and validation against pangoLEARN and UShER in this report: [Nextclade as pango lineage classifier: Methods and Validation](https://docs.nextstrain.org/projects/nextclade/en/latest/user/algorithm/nextclade-pango.html).
- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.132, featuring lineages like `BA.2.3`, `BA.1.17` and `BA.1.1.16`.
- Reference tree: Every pango lineage that's sampled in gets a synthetic sequence that is chosen to represent a hypothetical common ancestor of the lineage, according to the sequences listed as members in the pango-designation repo.

## 2022-02-07

### New dataset version (tag `2022-02-07T12:00:00Z`)

#### SARS-CoV-2

- Reference tree: Updated with new data. New algorithm for choosing how many of each pango lineage to include improves coverage of common and recent lineages. Every pango lineage that's included gets one relatively basal (early) sequence to keep number of false positive reversions down.

## 2022-01-18

### New dataset version (tag `2022-01-18T12:00:00Z`)

- Backwards incompatibility: New datasets no longer work for Nextclade versions before 1.10.0

#### SARS-CoV-2

- Files: added `virus_properties.json` containing common mutations per clade
- QC: higher penalty for private mutations that are reversions or common in other clades

#### Influenza

- Files: Stub `virus_properties.json` added to be compatible with new Nextclade version 1.10.0

## 2022-01-05

### SARS-CoV-2

#### New dataset version (tag `2022-01-05T19:54:31Z`)

- Reference tree: Added more Omicron sequences, from all of BA.1/BA.2/BA.3
- Reference tree: General data update with new pango lineages
- Sample sequences: Added BA.2 and BA.3 to sample sequences

## 2021-12-16

### Influenza

#### New dataset version (tag `2021-12-16T20:15:53Z`)

- Clades: New WHO clades names are used
- Reference tree: Data source is now GISAID which means better global coverage

### SARS-CoV-2

#### New dataset version (tag `2021-12-16T20:57:35Z`)

- Clades: `21M (Omicron)` added as Omicron catch all equivalent to pango `B.1.1.529`
- Clades: `21L` elevated to `21L (Omicron)` in line with WHO practice
- QC: Fixed known frameshift `ORF7b:3` (was erroneously `ORF7a:3`)

## 2021-12-09

### SARS-CoV-2

#### New dataset version (tag `2021-12-09T18:09:18Z`)

- Clades: Omicron is split into `21K (Omicron)` (pango `BA.1`) and `21L` (pango `BA.2`). The minor clade `21L` is at this point not called Omicron by WHO so it does not get the Omicron label for now.
- Reference tree: Data has been updated to early December
- Pango lineages designated until early December have been sampled in

## 2021-12-03--00-14-37--UTC

### General

- Added explicit cache-control headers

### SARS-CoV-2

#### New dataset version (tag `2021-12-03T00:20:15Z`)

- Sample sequences: Added two `21K (Omicron)` sequences

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
