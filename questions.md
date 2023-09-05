# Cornelius' questions re v3

## index.json

- Difference between `version` and `versions`: is `version` the _latest_ version?
- What are `capabilities`? Is `NextcladePango` a capability?
- Does only B.1 have the `mutLabels`?

## Maintenance

- How to add a new dataset
- How to create a new version? Just update? Where do we keep track of old versions? Are old versions added to `data_output` permanently? Is `data` hence the working directory, and `data_output` the permanent storage of the whole history?
- How to request old versions of a dataset for reproducibility?

## Testing new versions

- How to test a new version of a dataset locally?

## Docs

Input data in `data` folder:

- First level is the "group": `community` or `nextstrain`, specifying who contributed the datasets, whether they are official or community datasets.
- This is followed by a path: `dataset_name/reference` followed by the dataset files
- Full set of dataset files is:
  - `CHANGELOG.md`
  - `README.md`
  - `pathogen.json`
  - `reference.fasta`
  - `sequences.fasta`
  - `tree.json`
  - `genome_annotations.gff3`

### Pathogen json

- How to set alignment parameters that differ from default?
  A: See <https://github.com/nextstrain/nextclade/blob/edefa3224175fed4cca8fd4541a36dbd8a7d4a4a/packages_rs/nextclade/src/analyze/virus_properties.rs#L30-L82>
  This shows the schema that's accepted for pathogen.json
  
