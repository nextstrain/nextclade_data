"""
Subworkflow for downloading sequences and metadata for a given taxon ID from NCBI GenBank.
This workflow is optinal, a user can provide their own sequences and metadata in "data/" and skip this step.
"""


rule all:
    input:
        "data/sequences.fasta",
        "data/metadata.tsv",


rule download_reference:
    output:
        reference="data/reference.fasta",
    shell:
        """
        wget -O {output.reference} "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=fasta&id={REFERENCE_ACCESSION}"
        """


rule fetch_ncbi_dataset_package:
    output:
        dataset_package=temp("data/ncbi_dataset.zip"),
    retries: 5
    shell:
        """
        datasets download virus genome taxon {TAXON_ID} \
            --no-progressbar \
            --filename {output.dataset_package}
        """


rule extract_ncbi_dataset_sequences:
    input:
        dataset_package="data/ncbi_dataset.zip",
    output:
        ncbi_dataset_sequences="data/sequences.fasta",
    shell:
        """
        unzip -jp {input.dataset_package} \
            ncbi_dataset/data/genomic.fna \
        | seqkit seq -i -w0 \
        > {output.ncbi_dataset_sequences}
        """


rule format_ncbi_dataset_report:
    input:
        dataset_package="data/ncbi_dataset.zip",
    output:
        ncbi_dataset_tsv=temp("data/metadata_raw.tsv"),
    params:
        fields_to_include="accession,isolate-collection-date,geo-location,geo-region,isolate-lineage,release-date,submitter-affiliation,submitter-names",
    shell:
        """
        dataformat tsv virus-genome \
            --package {input.dataset_package} \
            --fields {params.fields_to_include:q} \
            > {output.ncbi_dataset_tsv}
        """


rule rename_columns:
    input:
        ncbi_dataset_tsv="data/metadata_raw.tsv",
    output:
        ncbi_dataset_tsv="data/metadata.tsv",
    shell:
        """
        csvtk rename -t -f Accession,"Isolate Collection date" -n strain,date \
            {input.ncbi_dataset_tsv} \
            > {output.ncbi_dataset_tsv}
        """
