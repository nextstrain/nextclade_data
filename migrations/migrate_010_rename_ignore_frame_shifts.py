"""
Rename 'qc.frameShifts.ignoreFrameShifts' to 'ignoredFrameShifts'.

The old name is silently ignored, so listed frame shifts are not
being excluded from QC scoring.
"""

from scripts.lib.container import dict_get
from scripts.lib.fs import find_files, json_read, json_write


def rename_ignore_frame_shifts(pathogen: dict) -> dict:
  frame_shifts = dict_get(pathogen, ["qc", "frameShifts"])
  if isinstance(frame_shifts, dict) and "ignoreFrameShifts" in frame_shifts:
    value = frame_shifts.pop("ignoreFrameShifts")
    frame_shifts["ignoredFrameShifts"] = value
  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    pathogen = rename_ignore_frame_shifts(pathogen)
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
