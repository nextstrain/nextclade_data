# Zenodo Storage for nextclade_data: Status and Optimization

## Background

The `nextclade_data` repository is archived on Zenodo via GitHub integration. Each GitHub release automatically creates a new Zenodo version under concept DOI [10.5281/zenodo.17880000](https://zenodo.org/records/20446446). The archive is a full `git archive` snapshot of the repository.

## Current Storage Footprint

- 17 versions archived since Dec 2025
- ~496 MB per version (latest), growing from 418 MB over 7 months
- 8.0 GB cumulative across all versions
- ~12 GB/year projected at current release cadence (~24 releases/year)

All 17 existing versions are permanent -- Zenodo does not allow deletion after 30 days.

## Cost

Zenodo is free, funded by CERN and EU grants. Data is stored in CERN data centres (Geneva + Budapest), backed up to tape nightly, retained for the lifetime of CERN (20+ years). No paid tier exists.

Current limits: 50 GB per record, 100 files per record, 150 GB account-level quota. We are well within limits but consuming storage at a pace that adds up over years.

## What's in the 496 MB

The archive is dominated by `data_output/`, the built dataset server directory (3.8 GB uncompressed, ~460 MB compressed). Within it:

| Content                            | Uncompressed | Share of archive |
| ---------------------------------- | ------------ | ---------------- |
| `dataset.zip` (pre-built bundles)  | 1.9 GB       | ~48%             |
| `tree.json` (phylogenetic trees)   | 1.3 GB       | ~33%             |
| `sequences.fasta` (examples)       | 579 MB       | ~12%             |
| Other (configs, refs, annotations) | ~170 MB      | ~7%              |

The `dataset.zip` files are fully redundant -- each bundles the same loose files (`tree.json`, `pathogen.json`, `reference.fasta`, etc.) already present in the same directory.

## Accepted Optimization

Exclude `dataset.zip` from `git archive` via `.gitattributes`.

A single line in `.gitattributes` at the repository root:

```
data_output/**/dataset.zip export-ignore
```

This tells `git archive` (used by GitHub and Zenodo to produce release archives) to skip all `dataset.zip` files. Normal git operations (clone, pull, push) are unaffected.

Verified result: archive size drops from 473 MB to 252 MB, a 47% reduction. Projected annual Zenodo consumption drops from ~12 GB to ~6 GB.

## Future Opportunity: Delta-only Releases

Analysis of recent releases shows that typical releases change only 1-3 datasets, producing deltas of 0.3-1 MB compressed. Even SC2 updates (the heaviest) produce ~35 MB deltas. A custom upload script using the Zenodo REST API could upload only changed datasets instead of full snapshots, reducing per-release storage by 90-99%. This would require replacing the automatic GitHub-Zenodo integration with a CI script (~4-5 HTTP calls via `curl`/`jq`).

This option is deferred but remains available if storage growth warrants it.
