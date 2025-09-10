# Nextclade

Previously, all "official" Nextclade workflows lived in a [central GitHub repository](https://github.com/neherlab/nextclade_data_workflows).
The new standard would be to include the Nextclade workflow within the pathogen repo.

This workflow is used to create the Nextclade datasets for this pathogen.
All official Nextclade datasets are available at https://github.com/nextstrain/nextclade_data.

> [!IMPORTANT]
> We do not have a generalized nextclade workflow so the rules files are empty and
> will need to be filled in with your own rules. We suggest that you go through the
> [Nextclade dataset creation guide](https://github.com/nextstrain/nextclade_data/blob/@/docs/dataset-creation-guide.md)
> to understand how to create a Nextclade dataset from scratch. Then use
> [mpox](https://github.com/nextstrain/mpox) as an example to create your own
> Nextclade workflow.

## Workflow Usage

The workflow can be run from the top level pathogen repo directory:
```
nextstrain build nextclade
```

Alternatively, the workflow can also be run from within the nextclade directory:
```
cd nextclade
nextstrain build .
```

This produces the default outputs of the nextclade workflow:

- nextclade_dataset(s) = datasets/<build_name>/*

## Defaults

The defaults directory contains all of the default configurations for the Nextclade workflow.

[defaults/config.yaml](defaults/config.yaml) contains all of the default configuration parameters
used for the Nextclade workflow. Use Snakemake's `--configfile`/`--config`
options to override these default values.

## Snakefile and rules

The rules directory contains separate Snakefiles (`*.smk`) as modules of the core Nextclade workflow.
The modules of the workflow are in separate files to keep the main nextclade [Snakefile](Snakefile) succinct and organized.

The `workdir` is hardcoded to be the nextclade directory so all filepaths for
inputs/outputs should be relative to the nextclade directory.

Modules are all [included](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#includes)
in the main Snakefile in the order that they are expected to run.

## Build configs

The build-configs directory contains custom configs and rules that override and/or
extend the default workflow.

- [test-dataset](build-configs/test-dataset/) - build to test new Nextclade dataset
