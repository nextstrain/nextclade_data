from lib.container import dict_rename_many, dict_get, dict_remove
from lib.fs import find_files, json_read, json_write


def rename_gene_to_cds(pathogen):
  motifs = dict_get(pathogen, ["aaMotifs"])
  if motifs:
    for i, motif in enumerate(motifs):
      motifs[i] = dict_rename_many(motifs[i], {"includeGenes": "includeCdses"})

    for i, motif in enumerate(motifs):
      includes = dict_get(motif, ["includeCdses"])
      if includes:
        for j, include in enumerate(includes):
          motifs[i]["includeCdses"][j] = dict_rename_many(motifs[i]["includeCdses"][j], {"gene": "cds"})

  phenotype_data = dict_get(pathogen, ["phenotypeData"])
  if phenotype_data:
    for i, phenotype_datum in enumerate(phenotype_data):
      phenotype_data[i] = dict_rename_many(phenotype_datum, {"gene": "cds"})

  qc = dict_get(pathogen, ["qc"])
  if qc:
    frame_shifts = dict_get(qc, ["frameShifts"])
    if frame_shifts:
      ignoreds = dict_get(frame_shifts, ["ignoredFrameShifts"])
      if ignoreds:
        for i, ignored in enumerate(ignoreds):
          ignoreds[i] = dict_rename_many(ignoreds[i], {"geneName": "cdsName"})

    stop_codons = dict_get(qc, ["stopCodons"])
    if stop_codons:
      ignoreds = dict_get(stop_codons, ["ignoredStopCodons"])
      if ignoreds:
        for i, ignored in enumerate(ignoreds):
          ignoreds[i] = dict_rename_many(ignoreds[i], {"geneName": "cdsName"})

  return pathogen


def main():
  for file in find_files("pathogen.json", here="data/"):
    pathogen = json_read(file)
    dict_remove(pathogen, "version")
    dict_remove(pathogen, "versions")
    json_write(pathogen, file, no_sort_keys=True)


if __name__ == '__main__':
  main()
