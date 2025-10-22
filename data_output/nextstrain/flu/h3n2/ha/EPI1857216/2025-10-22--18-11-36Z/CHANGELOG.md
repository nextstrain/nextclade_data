## 2025-10-22T18:11:36Z

 - add designation of J.2.4.1
 - make `subclade` the default clade like feature, while including a column `subclade` into the tabular output to maintain backwards compatibility of other pipelines. The previous `clade` that hasn't been updated in for 2y as now `legacy-clade`.

## 2025-09-09T12:13:13Z

Add schema definition url to `pathogen.json`. This is a purely technical change, for convenience of dataset authors. The data itself is not modified.

## 2025-08-07T09:22:32Z

 - addition of subclade [J.2.3](https://github.com/influenza-clade-nomenclature/seasonal_A-H3N2_HA/blob/d79c221035496f273b7e2a31152b21df990a21b4/subclades/J.2.3.yml) with HA1 189R and 158K
 - addition of subclade [J.2.4](https://github.com/influenza-clade-nomenclature/seasonal_A-H3N2_HA/blob/d79c221035496f273b7e2a31152b21df990a21b4/subclades/J.2.4.yml) with HA1 189R and 135K
 - addition of subclade [J.2.5](https://github.com/influenza-clade-nomenclature/seasonal_A-H3N2_HA/blob/aedcba677b359da0ebc18e74c69218f75c516a59/subclades/J.2.5.yml) with HA1 145N and 158K

## 2025-01-22T09:54:14Z

 - update reference trees

## 2025-01-09T08:17:24Z

 - include subclade proposals for J.2.a/b/c/d/e

## 2024-11-27T02:51:00Z

 - update reference trees
 - include subclades J.1.1, J.2.1, J.2.2 (included as proposed clades on 2024-11-05)

## 2024-11-05T09:19:52Z

 - update reference trees
 - include subclade proposals

## 2024-08-08T05:08:21Z

Fix numbering of RBD sites it the `pathogen.json`. The relevant positions were indexed 1-based, when they should have been indexed 0-based.

## 2024-07-03T08:29:55Z

Added configuration of current and recent vaccine strains as 'reference nodes' on the reference tree, against which query sequences can be compared. This feature is in addition to the new 'compare to clade founder' feature, allowing to compare each query sequence to the most ancestral node of a clade or lineage.

The datasets themselves remain unchanged.

See Nextclade documentation for more details about 'relative mutations' functionality.

## 2024-04-19T07:50:39Z

Update of the datasets with more recent data. No new clades were added on this occasion.

## 2024-02-22T16:12:03Z

After discussion with various members of the seasonal influenza virus surveillance community, it was decided that subclade names starting with `H` have the potential to be confused with major influenza hemagglutinin subtypes. These subclades where therefore renamed to start with the alias `J`.

 - `H` --> `J`
 - `H.1` --> `J.1`
 - `H.2` --> `J.2`
 - `H.3` --> `J.3`
 - `H.4` --> `J.4`

The subclades `H` and `H.*` were revoked, and a comment was added to explain the reason. No subclade definitions were changed.


## 2024-01-16T20:31:02Z

Initial release for Nextclade v3!

 - Addition of subclade H.1, H.2, H.3, and H.4
 - Aliasing of G.1.3.1.1 as subclade H

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
