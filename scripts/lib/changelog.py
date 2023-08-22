from .container import dict_get_required, dict_get
from .fs import file_read, file_write


def changelog_prepare(dataset, updated_at, changelog_path):
  path = dataset["path"]
  release_notes = changelog_get_unreleased_section(changelog_path)
  if len(release_notes) == 0:
    raise ValueError(
      f"Cannot release dataset '{path}' without changelog. Please modify file '{changelog_path}': add '## Unreleased' section and briefly summarize the changes being released"
    )

  full_changelog = file_read(changelog_path).replace(f"## Unreleased", f"## {updated_at}")
  file_write(full_changelog, changelog_path)

  attr_table = format_dataset_attributes_md_table(dataset)
  release_notes = release_notes.replace(
    "## Unreleased",
    f"""### {path}\n\n{attr_table}""".strip("\n ")
  )

  return release_notes


def changelog_get_unreleased_section(changelog_path: str):
  release_notes = ""
  found_release_notes_block = False
  with open(changelog_path) as f:
    for line in f:
      if not found_release_notes_block and line.startswith("## Unreleased"):
        found_release_notes_block = True
        release_notes += line
      elif found_release_notes_block:
        if line.startswith("## "):
          return release_notes
        else:
          release_notes += line
  return release_notes.strip()


def format_dataset_attributes_md_table(dataset):
  attr_table = f"| {'attribute':20} | {'value':20} | {'value friendly':40} |\n"
  attr_table += f"| {'-' * 20} | {'-' * 20} | {'-' * 40} |\n"
  for attr_name, attr_val in dict_get_required(dataset, ["attributes"]).items():
    value = attr_val["value"]
    value_friendly = dict_get(attr_val, ["valueFriendly"]) or ""
    attr_table += f'| {attr_name:20} | {value:20} | {value_friendly:40} |\n'
  return attr_table
