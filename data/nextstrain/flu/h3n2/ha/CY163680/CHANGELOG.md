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
