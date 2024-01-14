# Nextclade dataset creation example workflow

This repository contains a simple example workflow for creating a Nextclade dataset, in this case for Zika virus.

For a more detailed guide on dataset creation, see the [dataset creation tutorial](../dataset-creation-guide.md).

The quickest way to run this workflow is to [install the Nextstrain toolchain](https://docs.nextstrain.org/en/latest/install.html) and then run the following commands (the target `test` generates the dataset and tests it):

```bash
nextstrain build . test
```
Alternatively, you can run the workflow via
```bash
snakemake --cores 4 assemble_dataset
```

## Customization
Basic configuration is supported by editing the constants at the top of the `Snakefile`.
You can adapt this workflow to a different virus by changing the NCBI taxon ID and the reference sequence. You will need to provide a reference sequence and annotation analogous to what is provided in `minimal-dataset` for Zika virus.

You may also want to edit `resources/auspice_config.json` and `resources/pathogen.json`.

If you struggle with customizing the workflow, please post your questions in the [Nextstrain discussion forum](https://discussion.nextstrain.org/).
