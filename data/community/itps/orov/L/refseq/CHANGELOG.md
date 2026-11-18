## 2026-11-18T10:44:04Z

**Breaking change**: renamed the CDS from `L` to `RdRp`, because `L` names the segment rather than
the encoded RNA-dependent RNA polymerase. Amino acid mutation labels that previously read `L:` now
read `RdRp:`, and `defaultCds` and the CDS names in `ignoredFrameShifts` changed accordingly. The L
protein is not known to be processed into separate mature products, so it remains a single CDS. Its
coordinates, sequence, mutations, QC behavior and tree topology are unchanged.

The dataset is now maintained directly in nextstrain/nextclade_data rather than rebuilt from
InstitutoTodosPelaSaude/nextclade-datasets-workflows. `meta.bugs`, `meta["source code"]` and the README
now point to this repository, and `pathogen.json` gains a `maintenance` block naming the maintainers.

## 2026-05-12T16:39:06Z

Initial release of a Oropouche Virus (OROV) dataset for segment L based on NCBI refseq reference genome.

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
