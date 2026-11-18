## 2026-11-18T10:44:04Z

Renamed the precursor CDS from `M` to `Gpc` and added the mature products of the M-segment
glycoprotein precursor as separate CDS, so that amino acid changes are now reported against Gn,
NSm and Gc in addition to the precursor. The RefSeq record NC_005775.1 annotates only the
uncleaved precursor.

| CDS | Precursor residues | Nucleotides in NC_005775.1 |
| --- | ------------------ | -------------------------- |
| Gpc (precursor) | 1-1420 | 32..4294 |
| Gn | 17-335 | 80..1036 |
| NSm | 336-481 | 1037..1474 |
| Gc | 482-1420 | 1475..4294 |

The boundaries follow Barbosa et al., J Virol 2023 (https://doi.org/10.1128/jvi.01331-22): the
secretion signal sequence is residues 1-16, SignalP 5.0 predicts signal peptidase cleavage between
G335 and E336, and the study expresses Gc as residues 482-1420. Unlike Bunyamwera virus, OROV
retains both Gn transmembrane domains during maturation. The Gc boundary is inferred by homology
with the Bunyamwera Gc N-terminus rather than measured for OROV, and processing of the polyprotein
is an active research topic, so the boundaries are provisional.

**Breaking change**: the precursor CDS is now named `Gpc` instead of `M`, because `M` names the
segment rather than a protein. Amino acid mutation labels that previously read `M:` now read
`Gpc:`, and `defaultCds` changed accordingly.

Because the products overlap the precursor, a frameshift or a premature stop codon inside residues
17-1420 is detected once for `Gpc` and once for the product that contains it. The frame shift and
stop codon QC score weights are therefore halved to 37.5, so that such an event contributes the
same QC score as in the previous release.

The exception is residues 1-16, the secretion signal sequence, which belong to no product. An
event there is detected once, so it now scores 37.5 rather than 75, and such a sequence can be
reported as `good` where the previous release reported `mediocre`.

The dataset is now maintained directly in nextstrain/nextclade_data rather than rebuilt from
InstitutoTodosPelaSaude/nextclade-datasets-workflows. `meta.bugs`, `meta["source code"]` and the README
now point to this repository, and `pathogen.json` gains a `maintenance` block naming the maintainers.

## 2026-05-12T16:39:06Z

Initial release of a Oropouche Virus (OROV) dataset for segment M based on NCBI refseq reference genome.

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
