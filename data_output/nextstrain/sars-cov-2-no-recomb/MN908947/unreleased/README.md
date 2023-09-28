# Nextclade dataset for "(Deprecated) SARS-CoV-2 without recombinants" based on reference "Wuhan-Hu-1/2019" (sars-cov-2-no-recomb/MN908947)


## Dataset attributes

| attribute            | value                | value friendly                           |
| -------------------- | -------------------- | ---------------------------------------- |
| name                 | sars-cov-2-no-recomb | (Deprecated) SARS-CoV-2 without recombinants |
| reference            | MN908947             | Wuhan-Hu-1/2019                          |


## What is Nextclade dataset

Read more about Nextclade datasets in Nextclade documentation: https://docs.nextstrain.org/projects/nextclade/en/stable/user/datasets.html


### What are the SARS-CoV-2 clades?

Nextclade was originally developed during COVID-19 pandemic, primarily focused on SARS-CoV-2. This section describes clades with application to SARS-CoV-2, but Nextclade can analyse other pathogens too.

<figure>
  <a href="https://raw.githubusercontent.com/nextstrain/ncov-clades-schema/master/clades.svg">
    <picture>
      <img
        src="https://raw.githubusercontent.com/nextstrain/ncov-clades-schema/master/clades.svg"
        alt="Illustration of phylogenetic relationships of SARS-CoV-2 clades, as defined by Nextstrain"
      />
    </picture>
  </a>
  <figcaption>
    <small>
      Fig.1. Illustration of phylogenetic relationships of SARS-CoV-2 clades, as defined by Nextstrain (<a href="https://github.com/nextstrain/ncov-clades-schema/">source</a>)
    </small>
  </figcaption>
</figure>

Since its emergence in late 2019, SARS-CoV-2 has diversified into several different co-circulating variants. To facilitate discussion of these variants, we have grouped them into __clades__ which are defined by specific signature mutations.

We currently define more than 30 clades (see [this blog post](https://nextstrain.org/blog/2021-01-06-updated-SARS-CoV-2-clade-naming) for details):

- 19A and 19B emerged in Wuhan and have dominated the early outbreak
- 20A emerged from 19A out of dominated the European outbreak in March and has since spread globally
- 20B and 20C are large genetically distinct subclades 20A emerged in early 2020
- 20D to 20J have emerged over the summer of 2020 and include three "Variants of Concern" (VoC).
- 21A to 21F include the VoC __delta__ and several Variants of Interest (VoI).
- 21K onwards are different clades within the diverse VoC __omicron__.

Within Nextstrain, we define each clade by its combination of signature mutations. You can find the exact clade definition in [github.com/nextstrain/ncov/defaults/clades.tsv](https://github.com/nextstrain/ncov/blob/master/defaults/clades.tsv). When available, we will include [WHO labels for VoCs and VoIs](https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/).

Learn more about how Nextclade assigns clades in the [documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/user/algorithm/).
