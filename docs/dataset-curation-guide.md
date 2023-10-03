### Dataset paths

The path of a given dataset directory in the data repo is used to uniquely indentify this dataset. So if you want to submit your dataset to the Nextclade community datasets repository, then we recommend that you follow certain conventions for the path segments in your pull request:

- `data/community`: this is the root of the community
- `your-lab/your-name`: replace this with your GitHub nickname, and/or name of your lab. This way every lab and lab member has its own directory. Feel free to use multiple directories or some nested structure. You can nest the subdirectories arbitrarily and this is not limited to 2 levels. We only ask to not submit datasets directly into the root of the community, to avoid clashes between different organizations.
- `pathogen-name/strain-name`: In these segments feel free to use the name of the pathogen and potentially strain name and/or an accession of the reference sequence. Again, you can nest the subdirectories arbitrarily and this is not limited to 2 levels.
- `other/features`: if you need some more levels of path segments to describe a particular dataset, for example a particular location, time period or a host organism, then you can as many path segments as you like.

### Requirements for dataset paths

- These path segments are used in directory names and URLs, sot it is advisable to avoid using spaces and special characters

- These paths are used as dataset identifiers, for example in an argument of Nextclade CLI, so they should not be excessively long

- Meaningful names and directory structure is encouraged. At the time of submission of the pull request, please avoid "temporary" names or names that cannot be understood by the potential users of the dataset.

- Once a dataset is submitted and released, the paths cannot be changed. You can of course submit the same dataset under new path, but your potential users won't know about it and will not be able to receive updates, because they will still be using the old path. So design your dataset paths carefully and with consideration for further updates and potential future additions to your community directory.


