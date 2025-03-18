#!/bin/env python3
import os
from Bio import SeqIO
from collections import defaultdict


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Annotate sequences using a genbank reference')
    parser.add_argument('--reference', required=True, type=str, help='Genbank accession of reference sequence (will be fetched from genbank)')
    parser.add_argument('--include-parent-features', action='store_true', help='Include parent features of CDS in the output')
    parser.add_argument('--output-dir', required=True, type=str, help='Output directory')
    return parser.parse_args()

def get_reference_sequence(accession):
    from Bio import Entrez
    Entrez.email = "hello@nextstrain.org"
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    print(f"Fetching reference sequence {accession} from genbank")
    return SeqIO.read(handle, "genbank")

def get_gff(accession):
    url = f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id={accession}"
    import urllib
    return [x.decode() for x in urllib.request.urlopen(url).readlines()]

def annotate_sequence(seq, cds):
    from Bio.SeqFeature import SeqFeature
    from Bio.SeqFeature import FeatureLocation, SimpleLocation, CompoundLocation
    strands = {'+':1, '-':-1}
    new_features = [feat for feat in seq.features if feat.type=='source']
    for cdsid, segments in cds.items():
        if len(segments)==0:
            continue
        elif len(segments)==1:
            loc = FeatureLocation(int(segments[0][0][3])-1, int(segments[0][0][4]),
                                  strand = strands.get(segments[0][0][6], 0))
        else:
            loc = CompoundLocation([SimpleLocation(int(seg[0][3])-1, int(seg[0][4]),
                                  strand = strands.get(seg[0][6], 0)) for seg in segments])

        feat = SeqFeature(location = loc, type=segments[0][0][2],
                          qualifiers=segments[0][1], id=cdsid)
        # to appease augur, overwrite 'locus_tag' with the 'Name' attribute used in the GFF file to identify the CDS
        feat.qualifiers['locus_tag'] = feat.qualifiers['Name']
        new_features.append(feat)
    seq.features = new_features
    return seq


def check_name(new_name):
    forbidden_chars = ' ,.;:()[]'
    if any([c in new_name for c in forbidden_chars]):
        print(f"ERROR: the CDS name contains invalid characters '{forbidden_chars}' or spaces.")
        print("These have been replaced by '_', but you might want to start over with different names.")
        for c in forbidden_chars:
            new_name = new_name.replace(c, '_')

    if len(new_name)>20:
        print(f"WARNING: this CDS name '{new_name}' is long, this might result in cumbersome output")
    return new_name

if __name__=="__main__":
    args = parse_args()
    reference = get_reference_sequence(args.reference)
    gff = get_gff(args.reference)
    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    # write the reference sequence to the output directory
    SeqIO.write(reference, f"{args.output_dir}/reference.fasta", "fasta")

    # collect all cds and alternative annotations of protein sequences
    all_cds = defaultdict(lambda: defaultdict(list))
    all_features = defaultdict(list)
    parents = list()
    for line in gff:
        if line[0]=='#':
            continue
        entries = line.strip().split('\t')
        if len(entries)<9:
            continue # invalid line

        # parse attributes and feature type and ID
        attributes = {x.split('=')[0]:x.split('=')[1] for x in entries[-1].split(';')}
        feature_type = entries[2]
        if feature_type in ['CDS', 'mature_protein_region_of_CDS', 'mat_peptide', 'mat_protein']:
            # IDs look like this: ID=id-NP_057850.1:133..363 where the part after to colon is the range in the translated sequence (exists in cases of mature protein annotations)
            # the coordinates need to be trimmed to identify segments as part of the same CDS
            feature_id = attributes['ID'].split(':')[0].split('-')[-1]
        else:
            feature_id = attributes['ID']

        all_features[feature_id].append([entries[:-1], attributes])
        if feature_type=='CDS':
            all_cds[feature_id]['CDS'].append([entries[:-1], attributes])
        elif feature_type in ['mature_protein_region_of_CDS', 'mat_peptide', 'mat_protein']:
            all_cds[feature_id]['mature_protein'].append([entries[:-1], attributes])

        if 'Parent' in attributes:
            parents.append(attributes['Parent'])

    annotation_choice = 0
    if any([len(feat)>1 for feat in all_cds.values()]):
        print("\nFor polypeptides annotated in multiple ways, you need to choose between different annotations (CDS or mature peptides/proteins).\n")
        while True:
            annotation_choice = input("For features with two annotations, use always CDS [1], always mature_protein [2], or pick on a case-by-case basis [0]: ")
            try:
                annotation_choice = int(annotation_choice)
                assert annotation_choice<3
                break
            except:
                print(f"You input '{annotation_choice}' is not valid. Please enter one of [0, 1, 2]")
    elif all([len(feat['CDS'])>0 for feat in all_cds.values()]):
        annotation_choice = 1
    elif all([len(feat['mature_protein'])>0 for feat in all_cds.values()]):
        annotation_choice = 2
    else:
        print("\nNo CDS or mature protein annotations found. Exiting.")
        exit()

    available_attributes_by_type = {'CDS':set(), 'mature_protein': set()}
    for annot, annot_set in available_attributes_by_type.items():
        for feat in all_cds.values():
            if annot in feat:
                for seg in feat[annot]:
                    if len(annot_set):
                        annot_set = annot_set.intersection(list(seg[1].keys()))
                    else:
                        annot_set = annot_set.union(list(seg[1].keys()))
        available_attributes_by_type[annot] = annot_set
        print(f"\nCommon attributes of all available {annot} annotations are:\n", annot_set, '\n')

    available_attributes = available_attributes_by_type['CDS'] if annotation_choice==1 else \
                           available_attributes_by_type['CDS'].intersection(available_attributes_by_type['mature_protein'])

    print("Note that CDS names should be short, unique, and recognizable as they are used to label amino acid mutations. Space, commas, colons, etc are not allowed.\n")
    while True:
        name_choice = input("Specify field to use as CDS name or leave empty for manual choice: ")
        if name_choice in available_attributes or name_choice=='':
            break
        else:
            print("invalid choice: ", name_choice)
            print("pick one of", available_attributes)

    streamlined_cds = {}
    names_by_id = {}
    name_count = defaultdict(int)
    # loop through all CDS and ask the user to pick one of the annotations
    # allow renaming of the CDS to user friendly names
    for cds_id, cds_sets in all_cds.items():
        cds_set = list(cds_sets.keys())[0]
        if annotation_choice==0:
            if len(cds_sets)>1:
                print(f"\nCDS {cds_id} is annotated in multiple ways:")
                for i, (cds_set, segments) in enumerate(cds_sets.items()):
                    print(f"\t{cds_set} with a total of {len(segments)} items [{i+1}]")
                choice = int(input("Please pick number in brackets to choose one (0 for omission): "))
                if choice:
                    cds_set = list(cds_sets.keys())[choice-1]
                else:
                    continue
        else:
            if len(cds_sets)>1:
                cds_set = list(cds_sets.keys())[annotation_choice-1]

        segments = cds_sets[cds_set]

        for segment in segments:
            segment_id = segment[1]["ID"]
            # only needed for one segment per CDS, skip if already in streamlined_cds
            if segment_id not in streamlined_cds:
                if name_choice:
                    new_name = segment[1][name_choice]
                else:
                    print(f"Attributes of the segment with ID='{segment_id}' are:")
                    for k,v in segment[1].items():
                        print(f'\t\t{k}:\t{v}')
                    new_name = input("Enter desired name (leave empty to drop): ")
                    if new_name=='': continue

                streamlined_cds[segment_id] = []
                new_name = check_name(new_name)
                name_count[new_name] += 1
                if name_count[new_name]>1:
                    print(f"\nWARNING: CDS name {new_name} is not unique, attaching index to make unique.\n")
                    new_name = f"{new_name}_{name_count[new_name]:03d}"

                names_by_id[segment_id] = new_name

            # if renamed and selected, add the segment to the list of segments
            if segment_id in names_by_id:
                new_entries, new_attributes = list(segment[0]), dict(segment[1])
                new_entries[2]='CDS'
                new_attributes['Name']=names_by_id[segment_id]
                if not args.include_parent_features:
                    if "Parent" in new_attributes: new_attributes.pop("Parent")
                streamlined_cds[segment_id].append([new_entries, new_attributes])

    def write_gff_line(entry):
        attributes = ';'.join([f"{k}={v}" for k,v in sorted(entry[1].items(), key=lambda x:(x[0]!='Name', len(x[1])))])
        return '\t'.join(entry[0])+'\t' + attributes + '\n'

    gff_fname = f"{args.output_dir}/annotation.gff"
    print(f"\nWriting annotation to GFF file: {gff_fname}\n")
    already_written = set()
    # write the gff file as a simple text file line by line
    with open(gff_fname, "w") as f:
        # write the header and the region line
        for line in gff:
            entries = line.split('\t')
            if entries[0][0]=='#' or (len(entries)>8 and entries[2]=='region'):
                f.write(line)

        # write the CDS lines
        for cds in streamlined_cds:
            if len(streamlined_cds[cds])==0:
                continue
            if 'Parent' in streamlined_cds[cds][0][1]:
                parent = streamlined_cds[cds][0][1]['Parent']
                if parent in already_written:
                    continue
                print(f"Exporting Parent '{parent}' of '{names_by_id[cds]}'.")
                for segment in all_features[parent]:
                    f.write(write_gff_line(segment))
                already_written.add(parent)

            print(f"Exporting CDS '{names_by_id[cds]}' with {len(streamlined_cds[cds])} segments.")
            for segment in streamlined_cds[cds]:
                f.write(write_gff_line(segment))

    gb_fname = f"{args.output_dir}/reference.gb"
    print("\nWriting annotation to genbank file: ", gb_fname)
    reannotated_seq = annotate_sequence(reference, streamlined_cds)
    SeqIO.write(reannotated_seq, gb_fname, "genbank")
