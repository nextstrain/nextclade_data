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

## Conversion from v2 to v3: migration steps

Requirements: git, python 3.

1. Check out `nextclade_data` repository locally:

    ```bash
    git clone https://github.com/nextstrain/nextclade_data
    cd nextclade_data
    ```

2. Run conversion script:

    ```bash
    ./scripts/convert_v2_to_v3.py \
      --input-dir='path/to/dataset/v2/files' \
      --output-dir='data/community/your-lab/your-name/pathogen-name/strain-name/other/features'
    ```

    In this example, we take your Nextclade v2 dataset located at `path/to/dataset/v2/files` and output a new dataset in Nextclade v3 format into `data/community/your-lab/your-name/pathogen-name/strain-name/other/features`.
  
    The output path can be anything and the dataset directory is relocatable, so you can move it around later. However, if you want to submit your dataset to the Nextclade community dataset collection, please follow the rules described in the [dataset curation guide](dataset-curation-guide.md).

3. Navigate to the generated output directory and open the `pathogen.json`. You will find the `attributes` fields containing string values `UNKNOWN`:

    ```
    "attributes": {
      "name": {
        "value": "UNKNOWN",
        "valueFriendly": "UNKNOWN"
      },
      "reference": {
        "value": "UNKNOWN",
        "valueFriendly": "UNKNOWN"
      }
    }
    ```
    
    Fill these values with meaningful name and reference. For example, you can use short pathogen name in `"value"` and full name of the pathogen in `"valueFriendly"`. Similarly, you could use accession of the reference sequence in `"value"` and full name of the reference sequence in `"valueFriendly"`. The `"valueFriendly"` fields will be displayed in Nextclade Web and Nextclade CLI.

4. Fill in `README.md` with information about pathogen and the authors of the dataset. Alternatively, you can delete it. This is an optional file.

5. Fill in `CHANGELOG.md` file as you see fit. The `CHANGELOG.md` must contain a second-level heading spelled exactly `## Unreleased` with release notes under it. This is used for automated processing during new releases.

6. Follow the [dataset curation guide](dataset-curation-guide.md) on how to test your dataset in Nextclade CLI and Nextclade Web.
