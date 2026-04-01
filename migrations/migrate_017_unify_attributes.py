"""
Move deprecated/experimental from top-level to attributes, remove enabled/official.

Per attributes unification: boolean fields (deprecated, experimental)
are read from attributes. Fields 'enabled' and 'official' are removed
(enabled was never used, official replaced by path-based is_community() check).

Migration rules:
- deprecated=true -> attributes.deprecated=true (omit if false)
- experimental=true -> attributes.experimental=true (omit if false)
- enabled -> removed entirely (dead code)
- official -> removed entirely
"""

from scripts.lib.container import dict_remove_many
from scripts.lib.fs import find_files, json_read, json_write

TOP_LEVEL_FIELDS = ("deprecated", "experimental", "enabled", "official")


def migrate_pathogen(pathogen: dict) -> dict:
    deprecated = pathogen.get("deprecated")
    experimental = pathogen.get("experimental")

    attrs = pathogen.get("attributes", {})

    if deprecated is True:
        attrs["deprecated"] = True
    if experimental is True:
        attrs["experimental"] = True

    dict_remove_many(pathogen, list(TOP_LEVEL_FIELDS))

    if attrs:
        pathogen["attributes"] = attrs

    return pathogen


def needs_migration(pathogen: dict) -> bool:
    return any(pathogen.get(field) is not None for field in TOP_LEVEL_FIELDS)


def main():
    for filepath in find_files("pathogen.json", here="data/"):
        pathogen = json_read(filepath)
        if not needs_migration(pathogen):
            continue

        pathogen = migrate_pathogen(pathogen)
        json_write(pathogen, filepath, no_sort_keys=True)


if __name__ == "__main__":
    main()
