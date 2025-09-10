# Nextclade dataset server maintenance

This document describes how Nextclade dataset server operates and how to maintain it.

This is an advanced technical guide for Nextclade dataset server maintainers and people who want to lauch their own Nextclade dataset server. Most people don't need that.

> ⚠️ If you are a user of Nextclade CLI or Nextclade Web and looking for documentation on how to use Nextclade, see [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/index.html) instead.

> ⚠️ If you are looking for how to create and submit a new dataset to the Nextclade community collection of datasets, without launching your own server, see [Dataset curation guide](dataset-curation-guide.md) instead.

> ⚠️ If you are looking for Nextclade software developer documentation, see [Nextclade developer guide](https://github.com/nextstrain/nextclade/blob/master/docs/dev/developer-guide.md) instead.

## Terminology

In this document, the term "dataset server" is used in two related meanings:

- a file directory that contains Nextclade datasets and required index files in the format that is ready for usage by Nextclade software (the `data_output/` directory in this repository)
- an HTTP web server instance that is serving this data directory over the network connection to Nextclade users

A "Nextclade dataset" is a set of files required for Nextclade software to be able to analyze a particular pathogen or strain. Nextclade software is built agnostic to pathogens and a dataset is a required input for it to operate. Nextclade datasets are fetched from a dataset server automatically in Nextclade Web, or can be downloaded and used manually in Nextclade CLI. There are also options to customize this behavior. See [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/index.html) for more details.

A "Nextclade dataset collection" is a collection of multiple datasets grouped by a certain criteria. At the time of writing, there is only the official "nextstrain" collection for datasets maintained by the Nextstrain team, as well as the "community" collection maintained by the community members. There can be more collections in the future.

## Maintenance of the official Nextclade dataset server

### Continuous integration (CI)

Dataset maintenance process is automated using GitHub Actions. The GitHub Actions workflow is described
in [.github/workflows/data-curation.yml](.github/workflows/data-curation.yml). It runs on every pull request on GitHub and push to a major branch.

The GitHub Action rebuilds a fresh, complete data server directory (`data_output/`), including the datasets themselves and required index files. It then uploads the directory to one of the deployment environments, so that the new data becomes available for Nextclade users.

### Deployment

This section describes official deployment of Nextclade dataset server.

This GitHub repository contains 3 major branches and there are 3 associated deployment environments for each of these. Each environment consists of:

- AWS S3 bucket
- AWS Cloudfront distribution
- a set of helper AWS Lambda@Edge functions attached to the Cloudfront distribution (to enable compression and to set various HTTP headers)
- a domain name associated with the AWS Cloudfront distribution

This allows each environment to act as an independent static file web server and to serve data cheaply and at scale. It serves files produced in the build process from the domain name associated with the environment.

This table contains a list of environments:

| Dataset repo branch | Data domain name            | Nextclade Web domain name | Nextclade repo branch | Meaning                                                                                                                       |
| ------------------- | --------------------------- | ------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| release             | data.clades.nextstrain.org  | clades.nextstrain.org     | release               | Final release, targeting all end users                                                                                        |
| staging             | data.staging.nextstrain.org | staging.nextstrain.org    | staging               | Staging release, for last-minute testing and fixes before a final release is made, to not block progress on the master branch |
| master              | data.master.nextstrain.org  | master.nextstrain.org     | all other branches    | Main development branch - accumulates features and bug fixes from pull requests branches                                      |

### Build locally

The build process can also be reproduced locally. This is useful when developing and testing new datasets or Nextclade software, for verification the of results.

### Releasing

> ⚠️ We prefer to make releases on weekdays from Tuesday to Thursday, ideally around Wednesday in UTC zone, to ensure that everyone affected (dev team and users) is full of energy and that there's enough time to react to changes and to fix potential breakage without causing overtime hours. We try to avoid releases before and on major holidays and on Fridays to avoid possible weekend/holiday surprises.
>
> Note that due to 3-tier branch system, development is never blocked by the unreleased changes.

The release is done by simply fast-forwarding the `release` branch to the current `master` branch. The Continuous integration will then deploy the dataset server directory to the `release` environment and the updated datasets will become available in the `release` deployment of Nextclade Web and for release versions of Nextclade CLI.

## Maintenance of a custom Nextclade dataset server

Instead of using official dataset server (at `https://data.clades.nextstrain.org`), Nextclade can also be configured to use any other dataset server.

In order to prepare the dataset server files, you can run the `./scripts/rebuild`, produce the `dataset_output/` directory and deploy the contents of it to any HTTP file server or cloud instance.

As explained earlier, the official deployment uses a setup based on AWS S3 and AWS Cloudfront of Nextstrain organization, but you are free to choose any software or service you like. For example, you could deploy your files to your own AWS account, to Google Cloud Platform. You can use Nginx or Apache to setup a file server. Or you can create a server programmatically, with tools like Python's `http.server` or Node.js `express` or `serve` packages. You can run your server in the cloud, on a remote computer or even on your local computer. You can also use GitHub to store your files, and it can be used it as a file server (although this is typically discouraged for day-to-day operations).

The discussion of file servers is out of scope here, but the minimum requirements to the server are:

- Nextclade software should be able to access the server address over HTTP protocol. The server could be accessible publicly on the internet, or only in your private network, or just locally on your computer - it does not matter. What matter is that there should be an HTTP route from the computer where Nextclade is to the computer where the datasets are deployed. Any authentication should be included into the server URL.

- In order for datasets to be usable in Nextclade Web, [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) should be enabled on your server. This is a requirement of most web browsers. Please refer to your server's documentation on how to enable CORS.

After the dataset server is deployed, make sure files can be accessed (downloaded) from a web browser and/or using `curl` command.

You can then configure Nextclade to use your dataset server. Assuming the files are deployed to the address `https://example.com/`:

- In Nextclade Web, add URL parameter `dataset-server=https://example.com/`

- In Nextclade CLI `run` and `dataset` subcommands, add additional argument `--server=https://example.com/`

Nextclade will then ignore the official servers and will instead use datasets deployed to your custom server.
