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

Standard rebuild command requires clean repo (no uncommitted changes), set `--allow-dirty` to override:

```bash
./scripts/rebuild_v3 --input-dir 'data/' --output-dir 'data_output/' --allow-dirty
```

Even then, when you are on a local testing branch, you need to push it upstream first, otherwise:

```bash
./scripts/rebuild_v3 --input-dir 'data/' --output-dir 'data_output/' --allow-dirty
Traceback (most recent call last):
  File "/Users/corneliusromer/code/nextclade_data/./scripts/rebuild_v3", line 366, in <module>
    main()
  File "/Users/corneliusromer/code/nextclade_data/./scripts/rebuild_v3", line 164, in main
    git_pull()
  File "/Users/corneliusromer/code/nextclade_data/scripts/lib/git.py", line 71, in git_pull
    run("git pull -q")
  File "/Users/corneliusromer/code/nextclade_data/scripts/lib/process.py", line 11, in run
    raise ValueError(
ValueError: The external process failed:
  Command: git pull -q
  Return code: 1
  Message: There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> tmp/tests
```

Unclear how this would work for independent contributors who want to test their changes before submitting a PR.
They can probably host the files dirfectly without going through whole rebuild process, but how?

- Can I point web/cli to use a particular branch's `data_output`?
- How to release a dataset?
- How to set the tag?


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
  
