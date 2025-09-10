#!/usr/bin/env python3
from os.path import dirname, join

from lib.changelog import changelog_get_unreleased_section
from lib.container import dict_set
from lib.fs import find_files, json_read, json_write, file_read, file_write

"""
Replace .meta.extensions.nextclade.ref_nodes" in all tree.json files matching a subdirectory recursively
"""

# Map from subdirectory path(s) to the ref_nodes object
DATA = {
  "nextstrain/sars-cov-2": {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "JN.1",
          "displayName": "JN.1 (24A)",
          "description": "Variant recommended for the 2024/2025 COVID-19 vaccine",
          "criteria": [
            {
              "qry": [{"clade": ["23I","24A", "24B", "24C", "recombinant"]}],
              "node": [{"name": ["JN.1"]}],
            }
          ],
        },
        {
          "name": "XBB.1.5",
          "displayName": "XBB.1.5 (23A)",
          "description": "Variant recommended for the 2023/2024 COVID-19 vaccine",
          "criteria": [
            {
              "qry": [{"clade": ["22F", "23A","23B", "23C", "23D", "23E", "23F", "23G", "recombinant"]}],
              "node": [{"name": ["XBB.1.5"]}],
            }
          ],
        },
      ]
    },
    "clade_node_attrs": [
      {
        "name": "Nextclade_pango",
        "displayName": "Pango lineage (Nextclade)",
        "description": "Pango lineage as inferred by Nextclade from the nearest neighbour in the reference tree. 98% "
                       "accurate for recent sequences, for higher accuracy use dedicated pangolin software in UShER "
                       "or pangoLEARN mode. Recombinants may get (wrongly) assigned to a designated recombinant "
                       "lineage if they have similar breakpoints.",
        "hideInWeb": False
      },
      {
        "name": "partiallyAliased",
        "displayName": "Unaliased",
        "description": "Partially aliased reconstructed Pango lineage",
        "hideInWeb": False,
        "skipAsReference": True
      },
      {
        "name": "clade_nextstrain",
        "displayName": "Nextstrain Clade",
        "description": "Nextstrain Clade",
        "hideInWeb": True,
        "skipAsReference": True
      },
      {
        "name": "clade_who",
        "displayName": "WHO name",
        "description": "Greek letter WHO name",
        "hideInWeb": True,
        "skipAsReference": True
      },
      {
        "name": "clade_display",
        "displayName": "Clade display name",
        "description": "Combination of Nextstrain clade and Pango lineage",
        "hideInWeb": True,
        "skipAsReference": True
      }
    ]
  },
  "nextstrain/flu/h1n1pdm/ha/CY121680": {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "A/Wisconsin/67/2022",
          "displayName": "A/Wisconsin/67/2022",
          "description": "Isolate first used in vaccine for NH season 2023/24",
          "criteria": [
            {
              "node": [{"name": ["A/Wisconsin/67/2022"]}],
            }
          ],
        },
        {
          "name": "A/Sydney/5/2021",
          "displayName": "A/Sydney/5/2021",
          "description": "Isolate first used in vaccine for SH season 2023",
          "criteria": [
            {
              "node": [{"name": ["A/Sydney/5/2021"]}],
            }
          ],
        },
        {
          "name": "A/Wisconsin/588/2019",
          "displayName": "A/Wisconsin/588/2019",
          "description": "Isolate first used in vaccine for SH season 2021",
          "criteria": [
            {
              "node": [{"name": ["A/Wisconsin/588/2019"]}],
            }
          ],
        }
      ]
    },
    "clade_node_attrs": [
      {
        "name": "subclade",
        "displayName": "Subclade",
        "description": "Experimental fine-grained subclade annotation."
      },
      {
        "name": "short-clade",
        "displayName": "short-clade",
        "description": "",
        "skipAsReference": True
      }
    ]
  },
  ("nextstrain/flu/h1n1pdm/ha/MW626062",): {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "A/Wisconsin/67/2022",
          "displayName": "A/Wisconsin/67/2022",
          "description": "Isolate first used in vaccine for NH season 2023/24",
          "criteria": [
            {
              "node": [{"name": ["A/Wisconsin/67/2022"]}],
            }
          ]
        },
        {
          "name": "A/Sydney/5/2021",
          "displayName": "A/Sydney/5/2021",
          "description": "Isolate first used in vaccine for SH season 2023",
          "criteria": [
            {
              "node": [{"name": ["A/Sydney/5/2021"]}],
            }
          ]

        },
        {
          "name": "A/Wisconsin/588/2019",
          "displayName": "A/Wisconsin/588/2019",
          "description": "Isolate first used in vaccine for SH season 2021",
          "criteria": [
            {
              "node": [{"name": ["A/Wisconsin/588/2019"]}],
            }
          ]
        }
      ]
    },
    "clade_node_attrs": [
      {
        "name": "subclade",
        "displayName": "Subclade",
        "description": "Experimental fine-grained subclade annotation."
      },
      {
        "name": "short-clade",
        "displayName": "short-clade",
        "description": "",
        "skipAsReference": True
      }
    ]
  },
  ("nextstrain/flu/h1n1pdm/na/MW626056",): {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "A/Wisconsin/67/2022",
          "displayName": "A/Wisconsin/67/2022",
          "description": "Isolate first used in vaccine for NH season 2023/24",
          "criteria": [
            {
              "node": [{"name": ["A/Wisconsin/67/2022"]}],
            }
          ]
        },
        {
          "name": "A/Sydney/5/2021",
          "displayName": "A/Sydney/5/2021",
          "description": "Isolate first used in vaccine for SH season 2023",
          "criteria": [
            {
              "node": [{"name": ["A/Sydney/5/2021"]}],
            }
          ]

        },
        {
          "name": "A/Wisconsin/588/2019",
          "displayName": "A/Wisconsin/588/2019",
          "description": "Isolate first used in vaccine for SH season 2021",
          "criteria": [
            {
              "node": [{"name": ["A/Wisconsin/588/2019"]}],
            }
          ]
        }
      ]
    }
  },
  ("nextstrain/flu/h3n2/ha/EPI1857216",): {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "A/Massachusetts/18/2022",
          "displayName": "A/Massachusetts/18/2022",
          "description": "Isolate first used in vaccine for SH season 2024",
          "criteria": [
            {
              "node": [{"name": ["A/Massachusetts/18/2022"]}],
            }
          ]
        },
        {
          "name": "A/Darwin/6/2021",
          "displayName": "A/Darwin/6/2021",
          "description": "Isolate first used in vaccine for SH season 2022",
          "criteria": [
            {
              "node": [{"name": ["A/Darwin/6/2021"]}],
            }
          ]
        },
        {
          "name": "A/HongKong/45/2019",
          "displayName": "A/HongKong/45/2019",
          "description": "Isolate first used in vaccine for NH season 2020/2021",
          "criteria": [
            {
              "node": [{"name": ["A/HongKong/45/2019"]}],
            }
          ]
        }
      ]
    },
    "clade_node_attrs": [
      {
        "name": "subclade",
        "displayName": "Subclade",
        "description": "Experimental fine-grained subclade annotation."
      },
      {
        "name": "short-clade",
        "displayName": "short-clade",
        "description": "",
        "skipAsReference": True
      }
    ]
  },
  ("nextstrain/flu/h3n2/na/EPI1857216",): {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "A/Massachusetts/18/2022",
          "displayName": "A/Massachusetts/18/2022",
          "description": "Isolate first used in vaccine for SH season 2024",
          "criteria": [
            {
              "node": [{"name": ["A/Massachusetts/18/2022"]}],
            }
          ]
        },
        {
          "name": "A/Darwin/6/2021",
          "displayName": "A/Darwin/6/2021",
          "description": "Isolate first used in vaccine for SH season 2022",
          "criteria": [
            {
              "node": [{"name": ["A/Darwin/6/2021"]}],
            }
          ]
        },
        {
          "name": "A/HongKong/45/2019",
          "displayName": "A/HongKong/45/2019",
          "description": "Isolate first used in vaccine for NH season 2020/2021",
          "criteria": [
            {
              "node": [{"name": ["A/HongKong/45/2019"]}],
            }
          ]
        }
      ]
    }
  },
  ("nextstrain/flu/vic/ha/KX058884", "nextstrain/flu/vic/na/KX058884"): {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "B/Austria/1359417/2021",
          "displayName": "B/Austria/1359417/2021",
          "description": "Isolate first used in vaccine for SH season 2022",
          "criteria": [
            {
              "node": [{"name": ["B/Austria/1359417/2021"]}],
            }
          ]
        },
        {
          "name": "B/Washington/2/2019",
          "displayName": "B/Washington/2/2019",
          "description": "Isolate first used in vaccine for SH season 2020",
          "criteria": [
            {
              "node": [{"name": ["B/Washington/2/2019"]}],
            }
          ]
        },
        {
          "name": "B/Colorado/6/2017",
          "displayName": "B/Colorado/6/2017",
          "description": "Isolate first used in vaccine for NH season 2018/2019",
          "criteria": [
            {
              "node": [{"name": ["B/Colorado/6/2017"]}],
            }
          ]
        }
      ]
    }
  },
  ("nextstrain/flu/h3n2/ha/CY163680"): {
    "ref_nodes": {
      "default": "__root__",
      "search": [
        {
          "name": "A/Massachusetts/18/2022",
          "displayName": "A/Massachusetts/18/2022",
          "description": "Isolate first used in vaccine for SH season 2024",
          "criteria": [
            {
              "node": [{"name": ["A/Massachusetts/18/2022"]}],
            }
          ]
        },
        {
          "name": "A/Darwin/6/2021",
          "displayName": "A/Darwin/6/2021",
          "description": "Isolate first used in vaccine for SH season 2022",
          "criteria": [
            {
              "node": [{"name": ["A/Darwin/6/2021"]}],
            }
          ]
        },
        {
          "name": "A/HongKong/45/2019",
          "displayName": "A/HongKong/45/2019",
          "description": "Isolate first used in vaccine for NH season 2020/2021",
          "criteria": [
            {
              "node": [{"name": ["A/HongKong/45/2019"]}],
            }
          ]
        }
      ]
    }
  },
    "clade_node_attrs": [
      {
        "name": "subclade",
        "displayName": "Subclade",
        "description": "Experimental fine-grained subclade annotation."
      },
      {
        "name": "short-clade",
        "displayName": "short-clade",
        "description": "",
        "skipAsReference": True
      }
    ]
}


def main():
  for (subdirs, data) in DATA.items():
    if not isinstance(subdirs, tuple):
      subdirs = (subdirs,)

    for subdir in subdirs:
      for file in find_files("tree.json", here=f"data/{subdir}"):
        tree = json_read(file)
        tree = apply(tree, data)
        json_write(tree, file, no_sort_keys=True)

        changelog_path = join(dirname(file), "CHANGELOG.md")
        if len(changelog_get_unreleased_section(changelog_path)) == 0:
          changelog = file_read(changelog_path)
          msg="Added configuration of current and recent vaccine strains as 'reference nodes' on the reference tree, against which query sequences can be compared. This feature is in addition to the new 'compare to clade founder' feature, allowing to compare each query sequence to the most ancestral node of a clade or lineage.\n\nThe datasets themselves remain unchanged.\n\nSee Nextclade documentation for more details about 'relative mutations' functionality."
          file_write(f"## Unreleased\n\n{msg}\n\n{changelog}", changelog_path)


def apply(tree, data):
  if "ref_nodes" in data:
    dict_set(tree, ["meta", "extensions", "nextclade", "ref_nodes"], data["ref_nodes"])
  if "clade_node_attrs" in data:
    dict_set(tree, ["meta", "extensions", "nextclade", "clade_node_attrs"], data["clade_node_attrs"])
  return tree


if __name__ == '__main__':
  main()
