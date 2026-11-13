## Unreleased

Added the mature products of the M-segment glycoprotein precursor as separate CDS, so that amino
acid changes are now reported against Gn, NSm and Gc in addition to the precursor. The RefSeq
record NC_005775.1 annotates only the uncleaved precursor.

| CDS | Precursor residues | Nucleotides in NC_005775.1 |
| --- | ------------------ | ------------------- |
| M (precursor, unchanged) | 1-1420 | 32..4294 |
| Gn | 17-306 | 80..949 |
| NSm | 307-481 | 950..1474 |
| Gc | 481-1420 | 1472..4294 |

The boundaries follow the conserved domain regions annotated on the reference's own protein record
(Bunya_G2 and bunya_NSm) together with the chain boundaries of reviewed Orthobunyavirus envelopment
polyproteins (Schmallenberg H2AM12, Bunyamwera P04505, La Crosse P09612, snowshoe hare P04875,
Guaroa P12430) projected onto the Oropouche precursor by alignment.

The precursor CDS keeps the name `M`, so existing `M:` amino acid mutation labels are unaffected.
The reference tree carries amino acid mutations for the new CDS.

Because Gc overlaps the precursor, a frameshift in the overlap is detected once per CDS and would
be scored twice by the frameshift QC rule. The known frameshift at the 3' end of the precursor is
therefore listed in `qc.frameShifts.ignoredFrameShifts` for Gc, so that it is still reported but
scored only once, as in the previous release.

## 2026-05-12T16:39:06Z

Initial release of a Oropouche Virus (OROV) dataset for segment M based on NCBI refseq reference genome.

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
