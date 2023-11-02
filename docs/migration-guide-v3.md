# Migration of datasets from v2 format to v3 format

Nextclade v3 uses new dataset format. This guide will introduce you into the changes and describes migration steps to take in order to convert your Nextclade v2 datasets to the new format.

## Notable changes are:

- Most dataset files are now optional: only reference sequence `reference.fasta` and some basic info in `pathogen.json` is required. Nextclade v3 can run on datasets without reference tree, making it very similar to what previously was Nextalign. This also means that there is no need to create "dummy" empty files for things you don't yet have.

- Files `tag.json`, `qc.json` and `virus_properties.json` got merged into a single file, called `pathogen.json`. Most fields in it are empty. The mandatory fields are created using migration script (described in the next section).

- File `genemap.gff3` was renamed to `genome_annotation.gff3`. Additionally, genome annotation handling in Nextclade v3 is now more [spec](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)-compliant and now takes into account entries of types "gene" and "CDS". Read Nextclade v3 release notes for more details.

- File`primers.csv` was removed. This was a rarely used feature. Please open an issue if you still need it.

- New file `CHANGELOG.md` - markdown file that describes changes in every released version of the dataset. Before a release this file must contain a section heading `## Unreleased`. During next release this section will become release notes for the next release and will be automatically renamed to contain the date of the release. Contents of this file is displayed to the users of Nextclade Web.

- New optional file `README.md` - markdown file that contains basic information about the dataset, pathogen, its particular strain, describes possible defects and drawbacks, other potentially useful information for dataset users, as well as provides contact information about authors. Contents of this file is displayed to the users of Nextclade Web.

- Dataset repository now groups datasets into "dataset collections". We added a collection called "community". Please submit pull requests containing your datasets (and their followup updates) into directory `data/community`. After a review, if accepted, your datasets will be distributed along with the official datasets from Nextstrain team and will be marked as "community" datasets.

## Migration steps

Requirements: git, python 3.

1. Check out `nextclade_data` repository locally:

    ```bash
    git clone https://github.com/nextstrain/nextclade_data
    cd nextclade_data
    ```

2. Run conversion script:

    ```bash
    ./scripts/convert_v2_to_v3.py \
      --input-dir='path/to/input/dataset/v2/dir' \
      --output-dir='path/to/output/dataset/v3/dir'
    ```

   In this example, we take your Nextclade v2 dataset located at `path/to/dataset/v2/files` and output a new dataset in Nextclade v3 format into `path/to/output/dataset/v3/dir`.

   The output path can be anything and the dataset directory is relocatable, so you can move it around later. However, if you want to submit your dataset to the Nextclade community dataset collection, please follow the rules described in the [dataset curation guide](dataset-curation-guide.md).

3. Navigate to the generated output directory and open the `pathogen.json`. You will find the `attributes` fields containing string values `UNKNOWN`. Fill these values with meaningful name and reference. These will be displayed in Nextclade Web and Nextclade CLI.

   For example, our main SARS-CoV-2 dataset has:

    ```json
    {
      "attributes": {
        "name": "SARS-CoV-2",
        "reference name": "Wuhan-Hu-1/2019",
        "reference accession": "MN908947"
      }
    }
    ```

   These are the recognized fields, and they are displayed in Nextclade software. However, you can also add any other custom fields to provide additional information to the users.

   Optionally, add `experimental` flag:

    ```json
    {
      "attributes": {
        "...": "...", 
        "experimental": true
      }
    }
    ```

   While the dataset is in early development or if it has known defects, we recommend to add the attribute flag `"experimental": true`, to signal potential problems to the users. Feel free to explain these particularities in more details for the current version of the dataset in the `README.md` as well as for each version in `CHANGELOG.md`.

   We also recommend to add `maintenance` section to the root of `pathogen.json`. In this section you can add information about authors of the dataset (organization and/or people), contact information, data provenance, acknowledgements, links to source code and documentation. Here is an example from the official datasets:

   ```json
   {
     "attributes": {
        "...": "..." 
     },
     "maintenance": {
       "website": [
         "https://nextstrain.org",
         "https://clades.nextstrain.org"
       ],
       "documentation": [
         "https://github.com/nextstrain/nextclade_data",
         "https://docs.nextstrain.org/projects/nextclade"
       ],
       "source code": [
         "https://github.com/nextstrain/nextclade_data",
         "https://github.com/neherlab/nextclade_data_workflows"
       ],
       "issues": [
         "https://github.com/nextstrain/nextclade_data",
         "https://github.com/nextstrain/nextclade_data/issues"
       ],
       "organizations": [
         "Nextstrain"
       ],
       "authors": [
         "Nextstrain team <https://nextstrain.org>"
       ]
     }
   }
   ```

4. Fill `README.md` file with some information about the pathogen and the authors of the dataset. Provide some details about the purpose and potential limitations of the dataset. It's a freeform document. You can use Markdown syntax as well as some limited subset of HTML there.

   This is an optional file, so you can also delete it, but we encourage you to describe your work to your potential users, so they could understand it better.

5. Fill `CHANGELOG.md` file. You can use Markdown syntax as well as some limited subset of HTML there.

   The file must contain a second-level heading spelled exactly `## Unreleased` with release notes under it. This heading is used for automated processing - the contents will be published as GitHub release notes during the next release.

   For the first release you can simply write "First release" or "Initial release" or similar.

6. Follow the [dataset curation guide](dataset-curation-guide.md) on how to test your dataset in Nextclade CLI and Nextclade Web.

7. Consider submitting your dataset to the Nextclade community dataset collection. Datasets in this collection are easily available for all users of Nextclade: they are deployed to Nextclade dataset server long with the official datasets, they are displayed in the dataset selector in Nextclade Web and are listed in the output of `nextclade dataset list` command of Nextclade CLI. See the [dataset curation guide](dataset-curation-guide.md) for instructions.
