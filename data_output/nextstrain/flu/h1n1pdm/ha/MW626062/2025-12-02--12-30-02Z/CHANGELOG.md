## 2025-12-02T12:30:02Z
 - Define subclade [D.3.1.1](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/D.3.1.1.yml)

## 2025-10-22T18:11:36Z

 - make `subclade` the default clade like feature, while including a column `subclade` into the tabular output to maintain backwards compatibility of other pipelines. The previous `clade` that hasn't been updated in for 2y as now `legacy-clade`.

## 2025-09-09T12:13:13Z

Add schema definition url to `pathogen.json`. This is a purely technical change, for convenience of dataset authors. The data itself is not modified.

## 2025-08-07T09:22:32Z
 - Define subclade [D.3.1](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/D.3.1.yml)

## 2025-01-22T09:54:14Z

 - include subclades C.1.9.1 - C.1.9.4 based on subclade proposals C.1.9.a/b/c/d


## 2025-01-09T08:17:24Z

 - add subclade proposals C.1.9.a/b/c/d

## 2024-11-27T02:51:00Z

 - update reference trees
 - include subclade D.5 (included as proposed clades on 2024-11-05)

## 2024-11-05T09:19:52Z

 - update reference trees
 - include subclade proposals

## 2024-07-03T08:29:55Z

Added configuration of current and recent vaccine strains as 'reference nodes' on the reference tree, against which query sequences can be compared. This feature is in addition to the new 'compare to clade founder' feature, allowing to compare each query sequence to the most ancestral node of a clade or lineage.

The datasets themselves remain unchanged.

See Nextclade documentation for more details about 'relative mutations' functionality.

## 2024-04-19T07:50:39Z

 - aliasing of C.1.1.1 as D
 - addition of subclades D.1 - D.4: [D.1](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/D.1.yml), [D.2](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/D.2.yml), [D.3](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/D.3.yml), [D.4](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/D.4.yml)
 - addition of subclades [C.1.8](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/C.1.8.yml) and [C.1.9](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/C.1.9.yml)
 - addition of subclades [C.1.7.1](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/C.1.7.1.yml) and [C.1.7.2](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/C.1.7.2.yml)


## 2024-01-16T20:31:02Z

Initial release for Nextclade v3!

 - addition of subclade [C.1.7](https://github.com/influenza-clade-nomenclature/seasonal_A-H1N1pdm_HA/blob/main/subclades/C.1.7.yml)

Read more about Nextclade datasets in the documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html
