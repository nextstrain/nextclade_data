#!/usr/bin/env python3
from os.path import dirname, join

from lib.changelog import changelog_get_unreleased_section
from lib.container import dict_set
from lib.fs import find_files, json_read, json_write, file_read, file_write

"""
Replace .meta.extensions.nextclade.ref_nodes" in all tree.json files matching a subdirectory recursively
"""

# Map from subdirectory path(s) to the ref_nodes object
SUBDIRS = {
  "nextstrain/sars-cov-2": {
    "default": "__root__",
    "search": [
      {
        "name": "clade-founder-by-clade",
        "displayName": "Clade founder (by node clade)",
        "description": "Mutations relative to founder of clade (earliest ancestor by clade)",
        "criteria": [
          {
            "qry": [{"clade": ["20A"]}],
            "node": [{"clade": ["20A"], "searchAlgo": "ancestor-earliest"}],
          },
          {
            "qry": [{"clade": ["23A"]}],
            "node": [{"clade": ["23A"], "searchAlgo": "ancestor-earliest"}],
          },
          {
            "qry": [{"clade": ["23B"]}],
            "node": [{"clade": ["23B"], "searchAlgo": "ancestor-earliest"}],
          }
        ]
      },
      {
        "name": "clade-founder-by-name",
        "displayName": "Clade founder (by node name)",
        "description": "Mutations relative to founder of clade (full search by name)",
        "criteria": [
          {
            "qry": [{"clade": ["20A"]}],
            "node": [{"name": ["NODE_0000000"]}],
          },
          {
            "qry": [{"clade": ["23A"]}],
            "node": [{"name": ["XBB.1.5"]}],
          },
          {
            "qry": [{"clade": ["23B"]}],
            "node": [{"name": ["NODE_0000862"]}],
          },
        ]
      },
      {
        "name": "22B",
        "displayName": "22B",
        "description": "Earliest ancestor having clade 22B (only for samples having clade 22B)",
        "criteria": [
          {
            "qry": [{"clade": ["22B"]}],
            "node": [{"clade": ["22B"], "searchAlgo": "ancestor-earliest"}],
          }
        ]
      },
      {
        "name": "BA.2.86",
        "displayName": "BA.2.86 (23I)",
        "description": "Full search by name: NODE_0000659 (only for samples having clade 22I)",
        "criteria": [
          {
            "qry": [{"clade": ["23I"]}],
            "node": [{"name": ["NODE_0000659"]}],
          }
        ],
      },
      {
        "name": "XBB.1.5",
        "displayName": "XBB.1.5 (23A)",
        "description": "Full search by name: XBB.1.5 (only for samples having clade 23A)",
        "criteria": [
          {
            "qry": [{"clade": ["23A"]}],
            "node": [{"name": ["XBB.1.5"]}],
          }
        ],
      },
      {
        "name": "BA.5",
        "displayName": "BA.5 (22B)",
        "description": "Full search by name: NODE_0000862 (only for samples having clade 22B)",
        "criteria": [
          {
            "qry": [{"clade": ["22B"]}],
            "node": [{"name": ["NODE_0000862"]}],
          }
        ],
      }
    ]
  },
  "nextstrain/flu/h1n1pdm/ha/CY121680": {
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
  ("nextstrain/flu/h1n1pdm/ha/MW626062", "nextstrain/flu/h1n1pdm/na/MW626056"): {
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
  ("nextstrain/flu/h3n2/ha/EPI1857216", "nextstrain/flu/h3n2/na/EPI1857216"): {
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
  ("nextstrain/flu/vic/ha/KX058884", "nextstrain/flu/vic/na/KX058884"): {
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
  },
  ("nextstrain/flu/h3n2/ha/CY163680"): {
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
}


def main():
  for (subdirs, ref_nodes) in SUBDIRS.items():
    if not isinstance(subdirs, tuple):
      subdirs = (subdirs,)

    for subdir in subdirs:
      for file in find_files("tree.json", here=f"data/{subdir}"):
        tree = json_read(file)
        tree = apply(tree, ref_nodes)
        json_write(tree, file, no_sort_keys=True)

        changelog_path = join(dirname(file), "CHANGELOG.md")
        if len(changelog_get_unreleased_section(changelog_path)) == 0:
          changelog = file_read(changelog_path)
          file_write(f"## Unreleased\n\nTest\n\n{changelog}", changelog_path)


def apply(tree, ref_nodes):
  dict_set(tree, ["meta", "extensions", "nextclade", "ref_nodes"], ref_nodes)
  return tree


if __name__ == '__main__':
  main()
