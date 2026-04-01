"""
Remove legacy v2 'nucMutLabelMapReverse' field.

Not used by Nextclade v3 - the reverse map is computed at runtime.
Removes from both root level and 'mutLabels' section.
"""

from scripts.lib.fs import find_files, json_read, json_write


def remove_nuc_mut_label_map_reverse(pathogen: dict) -> dict:
  pathogen.pop("nucMutLabelMapReverse", None)

  mut_labels = pathogen.get("mutLabels")
  if isinstance(mut_labels, dict):
    mut_labels.pop("nucMutLabelMapReverse", None)

  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = remove_nuc_mut_label_map_reverse(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
