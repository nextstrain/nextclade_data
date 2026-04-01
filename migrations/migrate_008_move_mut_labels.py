"""
Move misplaced mutation label maps from root level into 'mutLabels'.

- 'nucMutLabelMap' at root -> 'mutLabels.nucMutLabelMap'
- 'mutLabelMap' at root -> contents moved into 'mutLabels'
"""

from scripts.lib.fs import find_files, json_read, json_write


def move_mut_labels(pathogen: dict) -> dict:
  mut_labels = pathogen.setdefault("mutLabels", {})

  if "nucMutLabelMap" in pathogen:
    value = pathogen.pop("nucMutLabelMap")
    if value and value != {}:
      mut_labels.setdefault("nucMutLabelMap", value)

  if "mutLabelMap" in pathogen:
    value = pathogen.pop("mutLabelMap")
    if isinstance(value, dict):
      for sub_key, sub_value in value.items():
        if sub_value and sub_value != {}:
          mut_labels.setdefault(sub_key, sub_value)

  if mut_labels == {}:
    pathogen.pop("mutLabels", None)

  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = move_mut_labels(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
