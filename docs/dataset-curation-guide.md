# Nextclade dataset curation guide

This guide explains how Nextclade datasets are structured and how to you can contribute or update datasets into the official Nextclade dataset collection.

> ⚠️ If you are a user of Nextclade Web or Nextclade CLI and looking for documentation on how to use Nextclade, see [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/index.html) instead.

> ⚠️ If you are looking for Nextclade software developer documentation, see [Nextclade developer guide](https://github.com/nextstrain/nextclade/blob/master/docs/dev/developer-guide.md) instead.

> ⚠️ This guide serves for advanced Nextclade users and enthusiasts who want to create and maintain their own Nextclade datasets, e.g. to add a yet unsupported pathogen or strain. It assumes basic familiarity with Nextclade CLI and Nextclade Web and some experience with different datasets as a user. If you are not yet comfortable using Nextclade and want to learn more about Nextclade datasets, please refer to the [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/) first.

> ⚠️ If you are looking for guidance on how to assemble a dataset from scratch and tweak its parameters for a particular virus, see [Nextclade dataset creation guide](dataset-creation-guide.md) instead.


## Basic principles

Nextclade software is built to be agnostic to pathogens it analyzes. Instead, the information about particularities of certain pathogens is provided in the form of so-called Nextclade datasets. A Nextclade dataset is a set of predefined files (in a directory or in a zip archive) which adds support for a particular pathogen or a strain to Nextclade CLI and Nextclade Web.

In this repository:

- The `data/` directory contains source data for datasets. It contains datasets grouped into dataset collections. For technical purposes, a dataset is defined as a leaf directory containing a `pathogen.json` file. It can be a part of the arbitrarily nested directory tree.

- The rebuild script (`./scripts/rebuild`) processes all dataset sources from the `data/` directory and produces `data_output/` directory.

- The `data_output/` directory is the current snapshot of the dataset server state. It contains versioned datasets as well as index files containing metadata which is necessary for Nextclade software to operate.

  > ⚠️ Never modify `data_output/` directory! All manual changes will be overwritten by the automation.

- The contents of `data_output/` directory is deployed to the production dataset servers (see [Dataset server maintenance guide](dataset-server-maintenance.md)), which makes it available to all Nextclade Web and Nextclade CLI users. The GitHub URL to this directory can also be used as a temporary substitute for a dataset server (in this case GitHub website acts as a server for us).

## Curating datasets

### Migrating from v2 to v3

If you already have a dataset for Nextclade v2 and want to upgrade it to Nextclade v3, see instructions in the [Dataset migration guide](migration-guide-v3.md).

### Obtaining source code of this repository

We use GitHub pull requests to manage contributions to Nextclade datasets.

In order to add or modify datasets you will need to have a local copy of the GitHub repository [`nextstrain/nextclade_data`](https://github.com/nextstrain/nextclade_data) on your computer, make the desired changes, commit & push the changes to a new git branch, and submit a pull request to [`nextstrain/nextclade_data`](https://github.com/nextstrain/nextclade_data). The pull request will be reviewed by Nextclade maintainers and considered for inclusion to the Nextclade dataset collection.

Make sure you have [git](https://git-scm.com/) installed, have an account on [GitHub](https://github.com) and can pull and push code from and to GitHub repositories.

[Make a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the [nextstrain/nextclade_data upstream repository](https://github.com/nextstrain/nextclade_data) and clone your forked repository:

```bash
git clone git@github.com:<your_github_username>/nextclade_data
```

Add changes to your forked repository, commit and submit a pull request to the upstream repository `nextstrain/nextclade_data`. When submitting, tick the checkbox ["Allow edits from maintainers"](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork), so that `nextstrain-bot` and project maintainers can contribute back to your pull request branch.

Refer to [GitHub documentation "Contributing to projects"](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) for more details.

> 💡 Make sure you [keep your local code up to date](https://github.com/git-guides/git-pull) with the origin repo,  [especially if it's forked](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).

> 💡 If you are a member of Nextstrain team, then you don't need a fork, and you can contribute directly to the origin repository `nextstrain/nextclade_data`. Nonetheless, please still submit a pull requests for review, rather than pushing changes to branches directly.

### Adding a new dataset

This section describes a sequence of steps to add a new Nextclade dataset for a pathogen or a strain. It assumes that you have a local copy of the nextstrain/nextclade_data repo available.

- Optionally, [create a new git branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches). Give it a name that briefly explains planned additions. Refer to documentation of git and of GitHub for more details.

- Add a directory under `data/community/<dataset_path>`.

  > ⚠️ We will discuss some important considerations about dataset paths in the [Dataset paths](#dataset-paths) section later on. If you want to submit your dataset to the community dataset collection, please follow these recommendations carefully.

  > 💡 If you are a member of Nextstrain organization, then submit to the "nextstrain" collection (`data/nextstrain`), rather than to "community" (`data/community`).

- Add `pathogen.json` file. Use `pathogen.json` files of the existing datasets as a template and modify them as needed.

- Add a `CHANGELOG.md` file containing second-level heading `## Unreleased` (spelled exactly like this) and free-form text under it, describing proposed changes. You can use Markdown syntax. In this case you can write that it's the first release of this dataset.

  > ⚠️ It is important to name the section exactly: two hashes, space and the word "Unreleased", starting with the capital letter "U". This text will be used to automatically find and extract release notes, which are then published along with the next dataset release.

- Add remaining dataset files. At a very minimum, you should have required files: `reference.fasta`, `pathogen.json` and `CHANGELOG.md`. See [dataset creation guide](dataset-creation-guide.md) for a detailed walkthrough.

- Optionally, [test your dataset locally](#testing-datasets-locally)

- Commit and push your changes to your forked repository on GitHub. Refer to documentation of git and of GitHub for more details.

- Submit your changes as a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to the `nextstrain/nextclade_data` repository on GitHub.

  > ⚠️ Note that `nextstrain-bot` will automatically run the rebuild script, and will commit changes to the `data/` and `data_output/` directories on your git branch. Don't forget to pull these changes if you are going to make more commits.

- Optionally, [test your dataset from GitHub](#testing-datasets-from-github)

- Wait for maintainers and community members to review and either accept or reject your proposal. Be ready to discuss the proposed changes, and to apply modifications if requested.

### Updating an existing dataset

- Find your dataset in the `data/` directory and modify dataset files as you see fit.

- On the very top of the `CHANGELOG.md`, add a second-level heading `## Unreleased` (spelled exactly like this) and a paragraph under it describing proposed changes in free form. You can use the usual Markdown syntax. Keep records for previous releases in place. If there's already an `## Unreleased` section (meaning this dataset already has changes that are yet to be released) append the summary of your changes to the existing summary.

- Submit the result for consideration as a pull request (similarly to how it was done in the "Adding a new dataset" section)

- Wait for maintainers and community members to review and either accept or reject your proposal. Be ready to discuss the proposed changes, and to apply some modifications if requested.

### Removing a dataset

> ⚠️ Once released, datasets cannot be removed!

> ⚠️ Note that because the GitHub repository is public, we cannot control any copies of your data that people could be making before it is removed from our repository. Never commit and push any sensitive or copyrighted data. Remember: once something is on the internet, it stays there forever!

> ⚠️ Before submitting something, make sure you have correct legal rights and/or author's permission to do so. We recommend to acknowledge authors of all materials and require to do so if the materials require acknowledgment.

If your pull request got merged, the changes weren't yet released, and you want to remove them, then open a pull request which rolls back your previously submitted changes as soon as possible.

If your pull request is not merged yet, simply close the pull request. Explain your decision in a comment message.

If you want to signal users that a dataset is no longer maintained, is inaccurate or obsolete, rather than deleting it you can set the field `"deprecated": true` in `pathogen.json` file. In this case the dataset will be listed in Nextclade with a "deprecated" badge and at the bottom of the list. Please explain the reason for deprecation in the changelog section (as described in the usual update steps), and add some details to the readme file if there is one, so that users could make an informed decision themselves whether to use it or not.

### What happens to accepted datasets

If your pull request is accepted and merged, your data enters `master` branch and is automatically deployed to the `master` environment. In a few minutes after merge it should be visible at https://master.clades.nextstrain.org

Nextclade server maintainers, after ensuring that there is no obvious bugs or crashes, periodically trigger deployment of the changes accumulated on `master` to the `release` environment, and then it becomes visible at the main site at https://clades.nextstrain.org.

There is no set schedule for releases, so let us know in the pull request if you have any particular preference.

## Dataset paths

The path of a given dataset directory in this repository is used to uniquely indentify this dataset, and has important consequences for its usage in Nextclade software. In this section we explain the best practices for Nextclade dataset paths.

### Recommended directory structure

If you want to submit your dataset for consideration for the inclusion to the Nextclade community datasets, then we ask that you follow certain conventions for the path segments when placing files and creating your pull request.

We currently recommend the following directory structure for your dataset directories:

```
data/community/your-org/your-name/pathogen-name/strain-name/other/features/
```

Let's split this path into segments and describe meaning of each segment:

- `data/`: this is the root of the dataset collection storage
- `community/`: this is the root of the "community" dataset collection
- `your-org/your-name/`: replace these path segments with your organization name, if you are submitting on behalf of an organization, as well as with your GitHub nickname. This way every organization (and organization member) has its own directory. Feel free to create some nested structure relevant for your organization - you can nest the subdirectories arbitrarily and this is not limited to 2 levels. We only ask to not submit datasets directly into the `community/`, to avoid clashes between datasets from different authors and organizations.
- `pathogen-name/strain-name/`: in these segments feel free to use the name of the pathogen and potentially strain name and/or an accession of the reference sequence. Again, you can nest the subdirectories arbitrarily and this is not limited to 2 levels.
- `other/features/`: if you need some more levels of path segments to describe a particular dataset, for example a particular geographic location, time period or a host organism, then you can create additional path segments for it.

Note, that this structure is only relevant if you want to submit your datasets into this repository. You can of course use any dataset directory structure on your local computer or in your own repositories.

### Requirements for dataset paths

- Dataset paths are used as dataset identifiers, for example in an argument of Nextclade CLI invocation and in URL parameters of Nextclade WEb, so they should not be excessively long.

- These paths are used in directory names and URLs, so please avoid using spaces and special characters. Prefer lowercase letters and dashes (`-`) over underscores (`_`) where possible.

- Meaningful, readable names and directory structure is encouraged. At the time of submission of the pull request, please avoid temporary names or names that cannot be understood by the potential users of the dataset.

- Be consistent in your naming conventions to avoid confusion. For example, choose between "flu" and "influenza", stick to it, and avoid mixing both names. You can explain your naming and other choices in the `README.md` file, which will be visible for all users.

- In order to allow reproducibility of Nextclade analysis results, released datasets are immutable. Once a dataset is submitted and released, it cannot be revoked and the path cannot be changed! You can of course later submit the same dataset under a new path, but this will lose continuity of versioning - your potential users won't know about this new dataset and will not be able to receive updates, because they will still be using the old path (for example hardcoded in their analysis pipeline's code). So design your dataset path hierarchies carefully and with consideration for further updates and potential future additions, such that the paths are final and won't need to be modified.

Take a look at the "nextstrain" dataset collection for concrete examples of how maintainers of official dataset collection like to organize their datasets.

## Testing datasets locally

The guide in [Test datasets locally](https://github.com/nextstrain/nextclade/blob/master/docs/dev/developer-guide.md#trying-custom-datasets-locally) describes how to change the datasets server URL used by Nextclade and Nextclade CLI as well as how to run a local dataset server. This is useful for testing the datasets modifications locally.

## Testing datasets from GitHub

Once the pull request is submitted, a [GitHub Actions](https://docs.github.com/en/actions) instance will be started. It will run `./scripts/rebuild` and commit and push the produced build to the `data_output/` directory on behalf of `nextstrain-bot` GitHub user. You will see the new commits appearing in your pull request. Once this is in place, the link to the `data_output/` GitHub directory can be used in Nextclade Web and Nextclade CLI as an alternative dataset server:

- First wait the GitHub Action runs in the "checks" section in your pull request to complete successfully.
- Wait for `nextstrain-bot` commit to appear in the list of commits of the pull request (refresh the page if needed).
- Obtain a full URL to the `data_output/` directory on your pull request's branch. For example, you can select your branch on GitHub, navigate to `data_output/` in the directory tree and copy the resulting URL in the address bar of your browser.
- In Nextclade CLI, use `--server=<github_url>` argument for `run` and `dataset get` commands.
- In Nextclade Web, add `dataset-server=<github_url>` URL parameter.

This will tell Nextclade to fetch your modified datasets right from GitHub (GitHub acts a dataset "server" here).

## Deploying own dataset server

If you don't want to submit your datasets to this repository, or prefer to deploy your datasets to your own GitHub repository or to your own web server, then follow [Dataset server maintenance guide](dataset-server-maintenance.md) for how to set it up.

## Questions, ideas, bug reports

For all questions, ideas, bug reports relevant to datasets, please open [a GitHub issue](https://github.com/nextstrain/nextclade_data/issues) in this repository or join our [discussion forum](https://discussion.nextstrain.org/).
