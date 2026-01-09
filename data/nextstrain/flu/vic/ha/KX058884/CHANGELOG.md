## 2025-10-22T18:11:36Z

 - make `subclade` the default clade like feature, while including a column `subclade` into the tabular output to maintain backwards compatibility of other pipelines. The previous `clade` that hasn't been updated in for 2y as now `legacy-clade`.

## 2025-09-09T12:13:13Z

Add schema definition url to `pathogen.json`. This is a purely technical change, for convenience of dataset authors. The data itself is not modified.

## 2025-08-07T09:22:32Z

 - addition of subclade [C.3.1](https://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/main/subclades/C.3.1.yml)
 - addition of subclade [C.3.2](hhttps://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/3bc8c7bc52de6d7dc32c1ac2e11a1d6187dde7d5/subclades/C.3.2.yml)
 - addition of subclade [C.5.6.1](https://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/main/subclades/C.5.6.1.yml)

## 2025-01-22T09:54:14Z

 - update reference trees

## 2024-11-05T09:19:52Z

 - update reference trees

## 2024-07-03T08:29:55Z

Added configuration of current and recent vaccine strains as 'reference nodes' on the reference tree, against which query sequences can be compared. This feature is in addition to the new 'compare to clade founder' feature, allowing to compare each query sequence to the most ancestral node of a clade or lineage.

The datasets themselves remain unchanged.

See Nextclade documentation for more details about 'relative mutations' functionality.

## 2024-04-19T07:50:39Z

Update of the datasets with more recent data. No new clades were added on this occasion.

## 2024-01-16T20:31:02Z

 - fix subclade definition of C.2 and C.4

## 2023-11-18

Initial release for Nextclade v3!

 - addition of subclade [C.5.4](https://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/main/subclades/C.5.4.yml)
 - addition of subclade [C.5.5](https://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/main/subclades/C.5.5.yml)
 - addition of subclade [C.5.6](https://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/main/subclades/C.5.6.yml)
 - addition of subclade [C.5.7](https://github.com/influenza-clade-nomenclature/seasonal_B-Vic_HA/blob/main/subclades/C.5.7.yml)

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
