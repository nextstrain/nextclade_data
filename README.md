<h1 id="nextclade-datasets" align="center">
💾 Nextclade Datasets
</h1>

These are the tools for curating public Nextclade datasets.

> ⚠️ This functionality is meant for the maintainers of Nextclade. We do not support using this outside of the team, but you can try anyways (you will need your own server infrastructure for that).


<h2 id="dataset-curators-guide" align="center">
🧑💾 Dataset curator's guide
</h2>

Dataset curation process is automated using GitHub Actions. The GitHub Actions workflow is described
in [.github/workflows/data-curation.yml](.github/workflows/data-curation.yml). It runs on every push to the repository.

The Github Action rebuilds a fresh, complete data repository, including the new `index.json` file. It then uploads data repository to a remote server, so that the new data becomes available for Nextclade users. The process can also be reproduced locally, for verification the of results. 


### Data source

View the contents of the `data/` directory. It contains the source data for creating a complete dataset repository.
During rebuild, some files copied to the dataset repository output directory as is, others are modified, or generated on the fly. 

 ```
 data
 ├── flu_vic_ha
 │   ├── dataset.json
 │   └── versions
 │       └── 2021-08-11T19:47:59Z
 │           └── files
 │               ├── genemap.gff
 │               ├── tag.json
 │               ├── primers.csv
 │               ├── qc.json
 │               ├── reference.fasta
 │               ├── sequences.fasta
 │               └── tree.json
 ├── sars-cov-2
 │   ├── dataset.json
 │   └── versions
 │       ├── 2021-06-20T00:00:00Z
 │       │   └── files
 │       │       ├── genemap.gff
 │       │       ├── tag.json
 │       │       ├── primers.csv
 │       │       ├── qc.json
 │       │       ├── reference.fasta
 │       │       ├── sequences.fasta
 │       │       └── tree.json
 │       └── 2021-06-25T00:00:00Z
 │           └── files
 │               ├── genemap.gff
 │               ├── tag.json
 │               ├── primers.csv
 │               ├── qc.json
 │               ├── reference.fasta
 │               ├── sequences.fasta
 │               └── tree.json
 └── settings.json
 ```


 - The file `settings.json` contains global settings, for all datasets.
 - Each directory contains a dataset
 - Each dataset is described by a `dataset.json` file. The `name` property of the `dataset.json` should match the directory name of the dataset.
 - Each dataset contains multiple versions, each under `versions/` subdirectory
 - Each dataset version is identified by a tag and described by `tag.json` file.
 - Each dataset version contains a set of files in `files/` subdirectory. The `files` property in `tag.json` should list these files.
 - A dataset version is uniquely identified by a tag (`datetime` currently)
 - A dataset version directory name should match the tag



### Adding new dataset

- Add a directory `data/<dataset_name>`, where `<dataset_name>` is the unique dataset name.
- Add `dataset.json` file. Use `dataset.json` files in existing datasets as a reference.
- Proceed to adding a dataset version as described in [Adding a version of the dataset](#adding-a-version-of-the-dataset).

### Adding a version of the dataset
- Add a directory `data/<dataset_name>/<version_tag>`, where `<version_tag>` is the current datetime. Datetime precision is not required, write manually or try this and tweak slightly to match existing tags (use `gdate` instead of `date` on MacOS):
     ```bash
     echo "$(date --iso-8601=seconds)Z"
     echo "$(date +"%Y-%m-%dT%H:%M:%S")Z"
     echo "python3 -c "import datetime; print(datetime.datetime.now().isoformat())"
   2021-08-13T01:03:28.052350"
     ```
- Add `tag.json` describing the new version tag. If there are breaking changes, adjust `compatibility` fields accordingly.
- Add files under `files/` in this subdirectory. File list should match the `files` entry in `tag.json`.
- Rebuild locally by running `./scripts/rebuild`, observe the result in the `data_output/` directory.
- If the result is satisfactory, commit `data/` files to git. This will launch the automated rebuild and will upload the resulting fresh data repo to the remote server.
- Wait up to 5-10 minutes for Cloudfront cache to be updated
- Verify that the modified data is available in Nextclade Web and Nextclade CLI

### Removing a version
 - Remove the corresponding version directory and commit to git. On rebuild, the version will be removed from the index. The scripts do not actually remove the files from S3 bucket, to avoid accidental data loss. We might clean up the bucket manually periodically. 

### Removing a dataset
 - Remove `dataset.json` corresponding to this dataset (optionally, the dataset directory too) and commit to git.

> ⚠️ Once committed and pushed to GitHub, all the files, source and generated become public. If any sensitive information was exposed, or if something needs to be deleted, ask someone with direct access to AWS to delete manually.


## Testing datasets locally

The guide in [Test datasets locally](https://github.com/nextstrain/nextclade/blob/master/docs/dev/datasets-local.md) describes how to change the datasets server URL used by Nextclade and Nextclade CLI as well as how to run a local dataset server. This is useful for testing the datasets modifications locally.


## Maintenance

The data is deployed automatically to 3 independent environments:

 - master
 - staging
 - release

There are 3 corresponding git branches with the same names. Upon a push or a merge to one of these branches branch, [the GitHub Action](https://github.com/nextstrain/nextclade_data/blob/master/.github/workflows/data-curation.yml) starts and deploys the data to the corresponding AWS S3 bucket in the Nextstrain organization. Each bucket acts as a static file server and has an AWS Cloudfront distribution attached to it for edge caching, as well as an AWS Lambda@Edge function, to modify HTTP headers. Each Cloudfront distribution have a domain name assigned to it:

 - data.master.clades.nextstrain.org
 - data.staging.clades.nextstrain.org
 - data.release.clades.nextstrain.org

Nextclade Web also has the 3 environments with the domain names derived from environment names:

 - master.clades.nextstrain.org
 - staging.clades.nextstrain.org
 - release.clades.nextstrain.org
 
Each environment draws data from the corresponding AWS S3 bucket. 

### Dataset release process

 - Submit a Pull request with proposed changes
 - Ask for someone to review it
 - In case of positive review (or if the changes are already agreed), merge this Pull request to the master branch
 - Manually verify the changes in the master environment:
     - on https://master.clades.nextstrain.org
     - see "Testing datasets locally" section above on how to test with Nextclade CLI
 - If verification is successful, merge master branch to staging branch using "fast-forward only" option (see the example steps for release branch below)
 - Manually verify the changes in the staging environment: https://staging.clades.nextstrain.org
 - if verification is successful, merge master branch to release branch using "fast-forward only" option (see the example steps for release branch below)
 - make release either manually on Github or using `gh` CLI: `gh release create 2021-11-16 -d -t 2021-11-16 --target release -n ''` before editing the changelog and converting from draft to actual release

If at any step in the process an error is found, or more features need to be implemented before releasing, start over from the beginning of this list.

Most of the time fast-forward merge should be possible. If it's not, then there might be a problem in git repo and unintended changes might be released. In this case, ask someone in Nextstrain org for help and for review of your plan before proceeding further.


### Fast-forward merge

Terminal commands for the "merge master branch to staging branch using fast-forward only option" step of the release process (for staging branch replace every occurrence of word "release" with word "staging"):

```bash
# If you have forks, make sure to set `git config --global checkout.defaultRemote origin`
# Make sure that you local machine has the latest changes from the remote server
git pull --all

# Switch to release branch
git checkout staging

# Fast-forward release branch to master locally
git merge master staging --ff-only

# Push release branch to the remote server
git push origin staging

git checkout release
git merge master release --ff-only
git push origin release

# Switch away from the release branch to avoid accidental commits later
git checkout master
```

It is often helpful to visualize the correctness of the branch state on every step by using a GUI git client, such as GitKraken, SourceTree, and [others](https://git-scm.com/downloads/guis).

### Infrastructure

AWS S3 buckets, AWS Cloudfront distributions, AWS Lambda and domain names are managed internally by Nextstrain AWS admins. Ping them on Slack if you need help.

### Copying from staging into the appropriate folder

```sh
TIMESTAMP="2022-10-27T12:00:00Z"
aws s3 cp s3://nextstrain-staging/nextclade_sars-cov-2_21L.json - | gzcat >~/code/nextclade_data/data/datasets/sars-cov-2-21L/references/BA.2/versions/$TIMESTAMP/files/tree.json 

aws s3 cp s3://nextstrain-staging/nextclade_sars-cov-2.json - | gzcat >~/code/nextclade_data/data/datasets/sars-cov-2/references/MN908947/versions/$TIMESTAMP/files/tree.json

aws s3 cp s3://nextstrain-staging/nextclade_sars-cov-2-no-recomb.json - | gzcat >~/code/nextclade_data/data/datasets/sars-cov-2-no-recomb/references/MN908947/versions/$TIMESTAMP/files/tree.json
```

### Creating a new dataset version

```sh
cp -pr /Users/corneliusromer/code/nextclade_data/data/datasets/sars-cov-2/references/MN908947/versions/2022-10-04T12:00:00Z /Users/corneliusromer/code/nextclade_data/data/datasets/sars-cov-2/references/MN908947/versions/2022-10-19T12:00:00Z

cp -pr /Users/corneliusromer/code/nextclade_data/data/datasets/sars-cov-2-no-recomb/references/MN908947/versions/2022-09-27T12:00:00Z /Users/corneliusromer/code/nextclade_data/data/datasets/sars-cov-2-no-recomb/references/MN908947/versions/2022-10-19T12:00:00Z

cp -pr /Users/corneliusromer/code/nextclade_data/data/datasets/sars-cov-2-21L/references/BA.2/versions/2022-09-27T12:00:00Z /Users/corneliusromer/code/nextclade_data/data/datasets/sars-cov-2-21L/references/BA.2/versions/2022-10-19T12:00:00Z
```

