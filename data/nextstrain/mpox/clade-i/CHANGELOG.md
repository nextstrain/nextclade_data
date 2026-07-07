## Unreleased

- Breaking change: Clade Ib outbreak sh2023 now has lineages defined. Those lineages follow the same scheme as the existing clade IIb outbreak sh2017 lineage system. The root lineage is A, and B might become an alias for another lineage than in IIb/sh2017. Hence, to unambiguously refer to a lineage, the outbreak must be included as well. To facilitate this, a new `outbreakLineage` field has been added that concatenates outbreak and lineage separated by a slash, e.g. `sh2023/A.1`. Existing `clade`, `outbreak`, and `lineage` fields remain unchanged - except that `lineage` `A` is now assigned to both clade Ib/sh2023 lineage `A` and (in datasets that contain it) clade IIb/sh2017 lineage `A`. The new `outbreakLineage` field is the way to unambiguously refer to a lineage.
- New sequences that have become available on Pathoplexus between December 2025 and June 2026 are now included in the dataset.
- The range 185990-186092 is no longer masked for placement. It is informative, reliable and relevant for assignment `sh2023/A.1`.

## 2026-04-14T11:55:23Z

- Align `pathogen.json` metadata with the current Nextclade schema layout.

## 2025-12-10T14:52:38Z

- Breaking change: outbreak nomenclature now follows the system described in [Ruis et al. (2025)](https://www.nature.com/articles/s41591-025-03820-6). As a result, outbreak `hMPXV-1` is now called `sh2017`. In addition, the clade Ib outbreak is labeled as outbreak `sh2023`, and the clade Ia outbreak described in [Wawina-Bokalanga et al. (2025)](<https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)00294-6>) is labeled as outbreak `sh2024`.

## 2025-09-09T12:13:13Z

- Sequences released since the last update in April 2025 are now included.
- Add schema definition url to `pathogen.json`. This is a purely technical change, for convenience of dataset authors. The data itself is not modified.

## 2025-04-25T12:24:24Z

- Newly released sequences are included.
- Sequences are now downloaded from Pathoplexus instead of NCBI virus. This allows inclusion of restricted-use clade I sequences from INRB (Placide Mbala-Kingebeni's group) in the DRC. This nearly doubles clade I sequences available.
- Based on user feedback, the QC rule for missing data (Ns) has been made more lenient.
- Masked ranges that are ignored for placement have been updated.

## 2025-03-26T11:47:13Z

Fix GFF3 format issues in genome annotation

## 2024-11-19T14:18:53Z

- Newly shared sequences are now included

## 2024-08-01T22:31:31Z

Initial release of this dataset.
