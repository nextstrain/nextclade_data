# Nextclade dataset creation example workflow

This repository contains a simple example workflow for creating a Nextclade dataset, in this case for Zika virus.

For a more detailed guide on dataset creation, see the [dataset creation tutorial](../dataset-creation-guide.md).

The quickest way to run this workflow is to [install the Nextstrain toolchain](https://docs.nextstrain.org/en/latest/install.html) and then run the following commands:

```bash
nextstrain build . test
```

Basic configuration is supported by editing the constants at the top of the `Snakefile`.

You may also want to edit `resources/auspice_config.json` and `resources/pathogen.json`.

If you struggle with customizing the workflow, please post your questions in the [Nextstrain discussion forum](https://discussion.nextstrain.org/).
