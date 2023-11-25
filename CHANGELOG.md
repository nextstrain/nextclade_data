# CHANGELOG

## 2023-11-25

### RSV-A and RSV-B nomenclature revision (tag `2023-11-25T12:00:00Z`)
Update RSV-A and RSV-B datasets with the revised consortium nomenclature. This update slightly reduces the number of lineages and renames some lineages. The lineage definitions are now available on https://github.com/rsv-lineages.

## 2023-11-22

### Fix for influenza B/Vic dataset version (tag `2023-11-22T12:00:00Z`)

 - the previous dataset was missing two subclades C.2 and C.4.

## 2023-11-18

### New Influenza datasets version (tag `2023-11-18T12:00:00Z`)

 - new subclades for several lineages
 - new alias for A/H3N2 HA

## 2023-10-26

### New SARS-CoV-2 dataset version (tag `2023-10-26T12:00:00Z`)

- Fixed a bug in consensus sequence algorithm that treated ambiguous nucleotides as reference as opposed to unknowns. This only affected a few lineages with few designated sequences where the consensus was wrongly reference when it should have been mutated.
- Pango lineages designated between 2023-09-20 and 2023-10-25 are now included, unfold below to see a list with designation dates:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- XCN (2023-09-21)
- FL.31 (2023-09-21)
- FL.31.1 (2023-09-21)
- FL.20.2 (2023-09-21)
- FL.32 (2023-09-21)
- FL.32.1 (2023-09-21)
- FL.10.3 (2023-09-21)
- FL.33 (2023-09-21)
- FL.33.1 (2023-09-21)
- FL.34 (2023-09-21)
- FL.35 (2023-09-21)
- JM.1 (2023-09-22)
- JM.2 (2023-09-22)
- GS.5 (2023-09-22)
- GK.2.1.1 (2023-09-24)
- EG.4.5 (2023-09-24)
- CH.1.1.31 (2023-09-24)
- JP.1 (2023-09-24)
- CH.1.1.32 (2023-09-24)
- JD.1.1.1 (2023-09-26)
- JD.1.1.2 (2023-09-26)
- XCP (2023-09-26)
- EG.5.1.10 (2023-09-26)
- GA.4.1.1 (2023-09-26)
- FR.1.5 (2023-09-26)
- EP.1.1 (2023-09-26)
- EP.1.1.1 (2023-09-26)
- HC.3 (2023-09-26)
- FL.36 (2023-09-26)
- HC.4 (2023-09-26)
- FL.15.1 (2023-09-27)
- FL.15.1.1 (2023-09-27)
- FL.15.2 (2023-09-27)
- FL.15.3 (2023-09-27)
- JN.1 (2023-09-29)
- JD.1.1.3 (2023-10-04)
- JD.2 (2023-10-04)
- GJ.1.2.6 (2023-10-04)
- GJ.1.2.7 (2023-10-04)
- JE.1.1 (2023-10-04)
- GJ.1.2.8 (2023-10-04)
- GJ.5 (2023-10-04)
- GJ.5.1 (2023-10-04)
- BA.2.86.2 (2023-10-12)
- BA.2.86.3 (2023-10-12)
- JQ.1 (2023-10-12)
- JN.2 (2023-10-12)
- JN.3 (2023-10-12)
- GK.2.4 (2023-10-12)
- HK.12 (2023-10-12)
- EG.6.1.2 (2023-10-12)
- HV.1.1 (2023-10-13)
- HV.1.2 (2023-10-13)
- HV.1.3 (2023-10-13)
- HV.1.4 (2023-10-13)
- HK.13 (2023-10-13)
- HK.13.1 (2023-10-13)
- HK.13.2 (2023-10-13)
- HK.1.1 (2023-10-13)
- HK.1.2 (2023-10-13)
- HK.14 (2023-10-13)
- HK.15 (2023-10-13)
- EG.5.1.11 (2023-10-13)
- JR.1 (2023-10-13)
- JR.1.1 (2023-10-13)
- GA.2.1 (2023-10-13)
- GA.2.1.1 (2023-10-13)
- GA.4.2 (2023-10-13)
- GA.4.3 (2023-10-13)
- GA.4.1.2 (2023-10-13)
- HK.16 (2023-10-13)
- HK.17 (2023-10-13)
- HK.18 (2023-10-13)
- HK.19 (2023-10-13)
- XBB.2.3.15 (2023-10-13)
- JS.1 (2023-10-13)
- JS.2 (2023-10-13)
- XCQ (2023-10-13)
- XBB.2.3.16 (2023-10-13)
- XBB.2.3.17 (2023-10-13)
- JD.2.1 (2023-10-13)
- GW.5.2 (2023-10-13)
- GW.5.3 (2023-10-13)
- GW.5.3.1 (2023-10-13)
- HW.1.2 (2023-10-13)
- HW.1.3 (2023-10-13)
- XBC.1.6.5 (2023-10-13)
- JT.1 (2023-10-13)
- XBC.1.6.6 (2023-10-13)
- GL.2 (2023-10-13)
- GL.3 (2023-10-13)
- XCR (2023-10-13)
- GK.5 (2023-10-15)
- GK.5.1 (2023-10-15)
- GK.6 (2023-10-15)
- GK.7 (2023-10-15)
- GK.8 (2023-10-15)
- GK.8.1 (2023-10-15)
- GK.9 (2023-10-15)
- GK.10 (2023-10-15)
- GK.11 (2023-10-15)
- GK.1.5 (2023-10-15)
- GK.1.6 (2023-10-15)
- GK.1.6.1 (2023-10-15)
- GK.1.2.1 (2023-10-15)
- GK.1.7 (2023-10-15)
- GK.1.8 (2023-10-15)
- GK.12 (2023-10-15)
- GK.1.9 (2023-10-15)
- XBB.1.16.25 (2023-10-15)
- XCS (2023-10-15)
- GK.1.1.1 (2023-10-15)
- FU.1.1 (2023-10-15)
- FU.1.1.1 (2023-10-15)
- HG.3 (2023-10-15)
- HG.1.1 (2023-10-15)
- XBB.2.3.18 (2023-10-15)
- GS.6 (2023-10-15)
- GS.4.1.1 (2023-10-15)
- GS.7 (2023-10-15)
- GS.7.1 (2023-10-15)
- GS.8 (2023-10-15)
- GJ.6 (2023-10-15)
- GJ.7 (2023-10-15)
- JU.1 (2023-10-15)
- JV.1 (2023-10-15)
- JV.2 (2023-10-15)
- JC.2 (2023-10-15)
- JC.3 (2023-10-15)
- JC.4 (2023-10-15)
- JC.5 (2023-10-15)
- JC.6 (2023-10-15)
- XBB.1.41.3 (2023-10-15)
- JW.1 (2023-10-15)
- FL.30.1 (2023-10-15)
- FL.13.2.1 (2023-10-15)
- FL.13.4 (2023-10-15)
- FL.13.4.1 (2023-10-15)
- FL.13.5 (2023-10-15)
- JG.4 (2023-10-15)
- DV.7.1.3 (2023-10-15)
- DV.7.1.4 (2023-10-15)
- DV.7.1.5 (2023-10-15)
- XCT (2023-10-15)
- XBC.1.7.2 (2023-10-15)
- XBC.1.7.1 (2023-10-15)
- FL.23.2.1 (2023-10-15)
- FL.23.2 (2023-10-15)
- XCU (2023-10-15)
- HH.2.1 (2023-10-15)
- HH.3 (2023-10-15)
- HH.4 (2023-10-15)
- HH.5 (2023-10-15)
- HH.6 (2023-10-15)
- HH.7 (2023-10-15)
- HH.8 (2023-10-15)
- HH.8.1 (2023-10-15)
- GE.1.4 (2023-10-15)
- GE.1.5 (2023-10-15)
- GE.1.6 (2023-10-15)
- XBB.2.3.19 (2023-10-15)
- JY.1 (2023-10-15)
- JY.1.1 (2023-10-15)
- JG.3.1 (2023-10-15)
- HK.2.1 (2023-10-15)
- HK.3.4 (2023-10-15)
- HK.3.5 (2023-10-15)
- HK.3.6 (2023-10-15)
- HK.3.7 (2023-10-15)
- HK.11.1 (2023-10-15)
- FL.35.1 (2023-10-15)
- GA.7 (2023-10-15)
- GA.7.1 (2023-10-15)
- GA.7.2 (2023-10-15)
- GA.8 (2023-10-15)
- GA.8.1 (2023-10-15)
- GA.9 (2023-10-15)
- GA.10 (2023-10-15)
- XCV (2023-10-15)
- XBB.2.3.20 (2023-10-15)
- XCW (2023-10-15)
- XBB.1.5.107 (2023-10-16)
- JZ.1 (2023-10-16)
- FD.5 (2023-10-16)
- FD.5.1 (2023-10-16)
- HE.2 (2023-10-16)
- FE.1.1.5 (2023-10-16)
- KA.1 (2023-10-16)
- GN.1.2 (2023-10-16)
- GN.1.3 (2023-10-16)
- XCY (2023-10-16)
- XCZ (2023-10-16)
- FY.8 (2023-10-16)
- FY.6.2 (2023-10-16)
- FY.6.1 (2023-10-16)
- FY.9 (2023-10-16)
- FY.1.4 (2023-10-16)
- FY.1.4.1 (2023-10-16)
- FY.5.1 (2023-10-16)
- FY.5.1.1 (2023-10-16)
- HN.2 (2023-10-17)
- HN.2.1 (2023-10-17)
- HN.3 (2023-10-17)
- HN.3.1 (2023-10-17)
- HN.4 (2023-10-17)
- HN.5 (2023-10-17)
- HN.6 (2023-10-17)
- GA.4.1.3 (2023-10-17)
- XDA (2023-10-18)
- XDB (2023-10-18)
- XDC (2023-10-18)

</details>

## 2023-10-03

### New RSV datasets with consortium nomenclature (tag `2023-10-02T12:00:00Z`)

- this adds a new developed nomenclature for RSV-A and RSV-B by the international RSV nomenclature consortium
- the old `G_clade` nomenclature is kept for backwards compatibility

## 2023-09-21

### New SARS-CoV-2 dataset version (tag `2023-09-21T12:00:00Z`)

- Add extra example sequences (GL.1, FL.1.5.1, EG.5.1, HV.1, DV.7.1, GK.2, BA.2.86)
- Add new frame shifts and stop codons to be ignored by QC
- Pango lineages designated between 2023-08-09 and 2023-09-20 are now included, unfold below to see a list with designation dates:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- JA.1 (2023-08-10)
- JB.1 (2023-08-10)
- JB.2 (2023-08-10)
- FW.1.1 (2023-08-22)
- JC.1 (2023-08-22)
- XBB.1.41.2 (2023-08-22)
- GA.4.1 (2023-08-22)
- GE.1.1 (2023-08-22)
- GE.1.2 (2023-08-22)
- XBB.1.5.102 (2023-08-22)
- JD.1 (2023-08-22)
- FL.1.5.2 (2023-08-23)
- JB.2.1 (2023-08-24)
- HK.6 (2023-08-24)
- GS.2 (2023-08-24)
- GS.3 (2023-08-24)
- GS.4 (2023-08-24)
- GS.4.1 (2023-08-24)
- GE.1.3 (2023-08-24)
- JE.1 (2023-08-24)
- HG.2 (2023-08-24)
- JF.1 (2023-08-24)
- JF.2 (2023-08-24)
- GK.1.4 (2023-08-24)
- GK.2.1 (2023-08-24)
- HK.3.1 (2023-08-24)
- XCH (2023-08-24)
- XCJ (2023-08-24)
- GM.3 (2023-08-24)
- GM.3.1 (2023-08-24)
- HC.2 (2023-08-25)
- EG.5.1.7 (2023-08-25)
- JD.1.1 (2023-08-25)
- JD.1.2 (2023-08-25)
- XBB.1.5.103 (2023-08-30)
- XCH.1 (2023-08-30)
- JG.1 (2023-08-30)
- HK.7 (2023-08-30)
- EG.2.2 (2023-08-30)
- EG.2.3 (2023-08-30)
- EG.2.4 (2023-08-30)
- EG.2.5 (2023-08-30)
- EG.13 (2023-08-31)
- FL.4.8 (2023-08-31)
- FL.4.9 (2023-08-31)
- FL.4.10 (2023-08-31)
- FY.3.2 (2023-08-31)
- FY.3.3 (2023-08-31)
- JH.1 (2023-08-31)
- JH.2 (2023-08-31)
- FL.2.6 (2023-08-31)
- XCK (2023-08-31)
- FL.10.2 (2023-08-31)
- XCL (2023-09-01)
- FL.30 (2023-09-01)
- GW.1.1 (2023-09-01)
- GK.2.2 (2023-09-01)
- HF.1.1 (2023-09-01)
- HF.1.2 (2023-09-01)
- XBB.1.5.104 (2023-09-01)
- XBB.1.16.23 (2023-09-01)
- XBB.1.5.105 (2023-09-01)
- HK.8 (2023-09-01)
- HK.9 (2023-09-01)
- JJ.1 (2023-09-01)
- HK.10 (2023-09-01)
- JK.1 (2023-09-01)
- HS.1.1 (2023-09-01)
- HK.11 (2023-09-04)
- JG.2 (2023-09-04)
- XBB.1.16.24 (2023-09-04)
- JL.1 (2023-09-04)
- BA.2.86.1 (2023-09-05)
- XCM (2023-09-05)
- FY.4.1.2 (2023-09-06)
- EG.6.1.1 (2023-09-07)
- GJ.1.2.2 (2023-09-10)
- GJ.1.2.3 (2023-09-10)
- GJ.1.2.4 (2023-09-10)
- GJ.1.2.5 (2023-09-10)
- FL.4.11 (2023-09-10)
- HK.3.2 (2023-09-10)
- HK.3.3 (2023-09-10)
- EG.14 (2023-09-10)
- GK.3.2 (2023-09-10)
- CK.1.1.2 (2023-09-10)
- EF.3 (2023-09-10)
- GW.5.1 (2023-09-11)
- GW.5.1.1 (2023-09-11)
- DV.7.1.1 (2023-09-11)
- DV.7.1.2 (2023-09-11)
- EG.5.1.8 (2023-09-11)
- GK.2.3 (2023-09-17)
- GK.4 (2023-09-17)
- EG.5.1.9 (2023-09-17)
- JG.3 (2023-09-17)
- XBB.1.5.106 (2023-09-17)

</details>

## 2023-08-22

### New influenza dataset version (tag `2023-08-10T12:00:00Z`)

All seasonal influenza datasets were updated to include an additional subclade designation the provides a more fine-grained breakdown of the currently circulating diversity.
These subclades are suggested using a [computational pipeline](https://github.com/neherlab/flu_clades) and follow a Pango-style nomenclature, albeit without hard automatic aliasing.

## 2023-08-17

### New SARS-CoV-2 dataset version (tag `2023-08-17T12:00:00Z`)

Ad-hoc update to include the [saltation variant BA.2.86](https://github.com/cov-lineages/pango-designation/issues/2183).
Note that this is not a regular data set update, but an update outside of the usual cycle specifically to enable detection of the BA.2.86.

## 2023-08-09

### New SARS-CoV-2 dataset version (tag `2023-08-09T12:00:00Z`)

- New Nextstrain clades 23C (CH.1.1), 23D (XBB.1.9), 23E (XBB.2.3), 23F (EG.5.1) are added. See [ncov PR](https://github.com/nextstrain/ncov/pull/1078) for a detailed discussion of the clades.
- Pango lineages designated between 2023-06-16 and 2023-08-08 are now included, unfold below to see a list with designation dates:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- FU.2.1 (2023-06-20)
- GU.1 (2023-06-20)
- GV.1 (2023-06-20)
- FL.4.3 (2023-06-20)
- EG.5.1.1 (2023-06-20)
- DV.7.1 (2023-06-26)
- GW.1 (2023-06-26)
- GW.2 (2023-06-26)
- GY.1 (2023-06-26)
- GY.2 (2023-06-26)
- BN.1.2.7 (2023-06-26)
- GJ.1.2 (2023-06-26)
- FL.13.2 (2023-06-28)
- FL.18 (2023-06-28)
- FL.18.1 (2023-06-28)
- FL.18.1.1 (2023-06-28)
- XBB.1.5.88 (2023-06-28)
- GZ.1 (2023-06-28)
- HA.1 (2023-06-28)
- HA.2 (2023-06-28)
- XBB.1.5.89 (2023-06-28)
- HB.1 (2023-06-28)
- EG.2.1 (2023-06-28)
- HC.1 (2023-06-28)
- FL.19 (2023-06-28)
- FU.3 (2023-06-28)
- BQ.1.1.79 (2023-06-28)
- FL.20 (2023-06-29)
- XBB.1.31.1 (2023-06-29)
- FL.1.7 (2023-06-29)
- FL.1.1.1 (2023-06-29)
- FL.4.4 (2023-06-30)
- FL.4.5 (2023-06-30)
- FL.4.6 (2023-06-30)
- FL.4.1.1 (2023-06-30)
- FL.4.7 (2023-06-30)
- GY.3 (2023-06-30)
- GY.2.1 (2023-06-30)
- XBB.1.16.12 (2023-06-30)
- XBB.1.16.13 (2023-06-30)
- FL.21 (2023-06-30)
- FL.5.1 (2023-06-30)
- EG.1.4.1 (2023-06-30)
- GD.2 (2023-06-30)
- GD.3 (2023-06-30)
- EG.1.5 (2023-06-30)
- EG.8 (2023-06-30)
- FL.22 (2023-06-30)
- FL.23 (2023-06-30)
- FY.6 (2023-06-30)
- CM.8.1.5 (2023-07-09)
- CK.1.1.1 (2023-07-09)
- CK.1.3 (2023-07-09)
- CK.1.4 (2023-07-09)
- CK.1.5 (2023-07-09)
- FR.1.4 (2023-07-09)
- GQ.1.1 (2023-07-09)
- FK.1.3.1 (2023-07-09)
- FK.1.3.2 (2023-07-09)
- FK.1.5 (2023-07-09)
- CJ.1.3.1 (2023-07-09)
- CJ.1.3.2 (2023-07-09)
- EU.1.1.3 (2023-07-09)
- FL.24 (2023-07-09)
- XBB.1.16.14 (2023-07-10)
- XBB.1.5.90 (2023-07-10)
- XBB.1.5.91 (2023-07-10)
- FL.25 (2023-07-10)
- FL.2.4 (2023-07-10)
- XCF.1 (2023-07-10)
- XCF.2 (2023-07-10)
- FL.26 (2023-07-10)
- FL.26.1 (2023-07-10)
- FU.4 (2023-07-11)
- XBB.1.5.92 (2023-07-11)
- XBB.1.5.93 (2023-07-11)
- HD.1 (2023-07-11)
- XBB.1.16.15 (2023-07-13)
- GK.1.1 (2023-07-13)
- GK.1.2 (2023-07-13)
- GK.1.3 (2023-07-13)
- AY.3.5 (2023-07-13)
- HE.1 (2023-07-14)
- FE.1.1.3 (2023-07-14)
- FE.1.1.4 (2023-07-14)
- HF.1 (2023-07-14)
- XBB.1.16.16 (2023-07-14)
- HG.1 (2023-07-14)
- XBB.2.3.13 (2023-07-14)
- XBB.2.3.14 (2023-07-14)
- XBB.1.49 (2023-07-14)
- GJ.3 (2023-07-14)
- XBB.1.5.94 (2023-07-14)
- EG.1.6 (2023-07-14)
- HH.1 (2023-07-14)
- HH.1.1 (2023-07-14)
- HH.2 (2023-07-14)
- CM.7.1.1 (2023-07-14)
- XBB.1.42.1 (2023-07-17)
- XBB.1.12.1 (2023-07-17)
- GY.4 (2023-07-19)
- GY.5 (2023-07-19)
- GY.6 (2023-07-19)
- EG.4.1 (2023-07-19)
- EG.4.2 (2023-07-19)
- EG.4.3 (2023-07-19)
- XBB.1.31.2 (2023-07-19)
- GY.7 (2023-07-19)
- XBB.1.5.95 (2023-07-19)
- HJ.1 (2023-07-19)
- XBB.1.5.96 (2023-07-19)
- FU.3.1 (2023-07-19)
- GW.3 (2023-07-19)
- GW.4 (2023-07-19)
- FL.23.1 (2023-07-19)
- FL.27 (2023-07-19)
- FD.4.1 (2023-07-19)
- GN.2 (2023-07-23)
- GN.1.1 (2023-07-23)
- GN.3 (2023-07-23)
- GN.4 (2023-07-23)
- GN.5 (2023-07-23)
- EG.5.1.2 (2023-07-23)
- EG.5.1.3 (2023-07-23)
- EG.5.1.4 (2023-07-23)
- EG.5.1.5 (2023-07-23)
- HK.1 (2023-07-23)
- HK.2 (2023-07-23)
- HK.3 (2023-07-23)
- HK.4 (2023-07-23)
- HK.5 (2023-07-23)
- EG.5.1.6 (2023-07-23)
- FT.2 (2023-07-23)
- FT.3 (2023-07-23)
- FT.3.1 (2023-07-23)
- FT.4 (2023-07-23)
- GA.4 (2023-07-23)
- GA.5 (2023-07-23)
- GA.6 (2023-07-23)
- GA.6.1 (2023-07-23)
- FW.3 (2023-07-23)
- HD.1.1 (2023-07-23)
- FL.13.3 (2023-07-23)
- FL.13.3.1 (2023-07-23)
- FL.2.3.1 (2023-07-23)
- XBB.1.16.17 (2023-07-23)
- FY.2.1 (2023-07-23)
- FY.4.1.1 (2023-07-23)
- FY.7 (2023-07-23)
- XBB.1.42.2 (2023-07-23)
- HL.1 (2023-07-23)
- HL.2 (2023-07-23)
- HM.1 (2023-07-23)
- FL.28 (2023-07-23)
- XBB.1.5.97 (2023-07-24)
- EG.1.7 (2023-07-24)
- EG.1.8 (2023-07-24)
- EG.4.4 (2023-07-24)
- FK.1.4.1 (2023-07-24)
- FK.1.1.1 (2023-07-24)
- FK.1.1.2 (2023-07-24)
- HN.1 (2023-07-24)
- FL.29 (2023-07-24)
- EG.9 (2023-07-24)
- EG.9.1 (2023-07-24)
- EG.10 (2023-07-24)
- EG.10.1 (2023-07-24)
- DV.7.2 (2023-07-25)
- EG.5.2.1 (2023-07-25)
- EG.5.2.2 (2023-07-25)
- EG.5.2.3 (2023-07-25)
- XBB.1.16.18 (2023-07-25)
- XBB.1.16.19 (2023-07-25)
- XBB.1.16.20 (2023-07-25)
- XBB.1.16.21 (2023-07-25)
- XBB.1.16.22 (2023-07-25)
- XBB.1.5.98 (2023-07-25)
- XBB.1.5.99 (2023-07-25)
- HP.1 (2023-07-26)
- HP.1.1 (2023-07-26)
- HQ.1 (2023-07-26)
- HR.1 (2023-07-26)
- HS.1 (2023-07-26)
- HT.1 (2023-07-26)
- HT.2 (2023-07-26)
- XBB.1.19.2 (2023-07-26)
- GW.5 (2023-07-26)
- FL.20.1 (2023-07-26)
- FL.21.1 (2023-07-27)
- FL.21.2 (2023-07-27)
- FT.3.1.1 (2023-07-27)
- FL.19.1 (2023-07-27)
- FU.5 (2023-07-27)
- HU.1 (2023-07-27)
- HU.2 (2023-07-28)
- FP.2.1.1 (2023-07-28)
- FP.2.1.2 (2023-07-28)
- HV.1 (2023-08-02)
- GK.3 (2023-08-02)
- GK.3.1 (2023-08-02)
- HW.1 (2023-08-02)
- HW.1.1 (2023-08-02)
- XBB.1.5.100 (2023-08-02)
- HY.1 (2023-08-02)
- GJ.1.2.1 (2023-08-04)
- HZ.1 (2023-08-04)
- HZ.2 (2023-08-04)
- HZ.3 (2023-08-04)
- BN.1.3.13 (2023-08-06)
- EG.11 (2023-08-07)
- GY.8 (2023-08-07)
- FY.4.2 (2023-08-07)
- XBB.1.22.3 (2023-08-07)
- HU.1.1 (2023-08-07)
- GJ.4 (2023-08-07)
- XBB.1.5.101 (2023-08-07)
- FL.2.5 (2023-08-07)
- EG.12 (2023-08-07)

</details>

## 2023-08-02

### Minor fix for SARS-CoV-2-21L dataset (tag `2023-08-02T12:00:00Z`)

- The SARS-CoV-2-21L dataset (`SARS-CoV-2-21L`) has been updated to show correct mutations in the auspice.json file. Nextclade output other than the tree json will not change in this release. It is mostly necessary for Nextclade version 3. Nothing else is changed, e.g. no new lineages.

## 2023-08-01

### New Mpox datasets (tag `2023-08-01T12:00:00Z`)

- Mpox datasets (`MPXV`, `hMPXV`, `hMPXV_B1`) now contain newly designate B.1 sublineages:
  - C.1 (alias of B.1.3.1)
  - B.1.18
  - B.1.19
  - B.1.20
    See <https://github.com/mpxv-lineages/lineage-designation/pull/33> for details
- Datasets have been updated to include sequences uploaded since the last release in January 2023

## 2023-06-16

### New SARS-CoV-2 dataset version (tag `2023-06-16T12:00:00Z`)

- Pango lineages designated between 2023-05-09 and 2023-06-15 are now included, unfold below to see a list with designation dates:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- XBB.2.9 (2023-05-11)
- XBB.1.5.70 (2023-05-22)
- FL.4.1 (2023-05-23)
- FL.4.2 (2023-05-23)
- FL.1.4 (2023-05-23)
- FL.13 (2023-05-23)
- FL.13.1 (2023-05-23)
- FL.14 (2023-05-23)
- GF.1 (2023-05-23)
- GG.1 (2023-05-23)
- FK.1.3 (2023-05-24)
- FK.1.4 (2023-05-24)
- FK.1.2.1 (2023-05-24)
- FY.1.1 (2023-05-24)
- FY.3.1 (2023-05-24)
- XBB.1.41 (2023-05-24)
- EG.5.2 (2023-05-24)
- FY.4.1 (2023-05-24)
- XBB.1.5.71 (2023-05-25)
- XBB.1.16.7 (2023-05-25)
- XBB.1.16.8 (2023-05-26)
- FL.15 (2023-05-29)
- EG.6 (2023-05-30)
- EG.6.1 (2023-05-30)
- FP.2 (2023-05-30)
- FP.3 (2023-05-30)
- FP.4 (2023-05-30)
- FP.2.1 (2023-05-30)
- XBB.1.16.9 (2023-05-30)
- CM.7.1 (2023-05-30)
- XBB.2.10 (2023-05-30)
- FL.16 (2023-05-30)
- XBB.1.9.7 (2023-05-30)
- XBB.1.5.72 (2023-05-31)
- FR.1.1 (2023-05-31)
- FR.1.2 (2023-05-31)
- XBB.1.42 (2023-05-31)
- XBB.1.43 (2023-05-31)
- XBB.1.43.1 (2023-05-31)
- XBB.2.6.1 (2023-06-01)
- GH.1 (2023-06-01)
- XBB.2.6.2 (2023-06-01)
- XBB.2.3.12 (2023-06-01)
- XBB.1.5.73 (2023-06-01)
- FD.2.1 (2023-06-01)
- XBB.1.5.74 (2023-06-01)
- XBB.1.5.75 (2023-06-01)
- XBB.1.5.76 (2023-06-01)
- XBB.1.5.77 (2023-06-01)
- XBB.1.5.78 (2023-06-01)
- XBB.1.5.79 (2023-06-01)
- XBB.1.5.80 (2023-06-01)
- XBB.1.5.81 (2023-06-01)
- GJ.1 (2023-06-02)
- FL.1.5 (2023-06-06)
- FL.1.5.1 (2023-06-06)
- GK.1 (2023-06-06)
- XBB.1.34.1 (2023-06-06)
- XBB.1.34.2 (2023-06-06)
- XBB.8.2 (2023-06-07)
- XCD (2023-06-08)
- EG.7 (2023-06-09)
- GJ.1.1 (2023-06-09)
- GJ.2 (2023-06-09)
- FL.1.10.1 (2023-06-09)
- XBB.1.41.1 (2023-06-09)
- XCE (2023-06-09)
- FE.1.1.1 (2023-06-09)
- FE.1.1.2 (2023-06-09)
- GL.1 (2023-06-09)
- GM.2 (2023-06-10)
- GM.1 (2023-06-10)
- XCF (2023-06-10)
- BQ.1.1.75 (2023-06-10)
- XBB.1.5.82 (2023-06-10)
- XBB.1.5.83 (2023-06-10)
- XBB.1.5.84 (2023-06-10)
- GN.1 (2023-06-10)
- XBB.1.5.85 (2023-06-10)
- XBB.1.5.86 (2023-06-10)
- DV.7 (2023-06-10)
- DV.8 (2023-06-10)
- CH.1.1.29 (2023-06-10)
- DV.6.2 (2023-06-10)
- DV.6.1 (2023-06-10)
- GK.2 (2023-06-10)
- GP.1 (2023-06-10)
- GP.2 (2023-06-10)
- GP.3 (2023-06-10)
- FK.1.2.2 (2023-06-10)
- FR.1.3 (2023-06-10)
- BN.1.3.12 (2023-06-10)
- BQ.1.1.76 (2023-06-10)
- BQ.1.1.77 (2023-06-10)
- BQ.1.1.78 (2023-06-10)
- EN.1.1 (2023-06-10)
- XBC.1.7 (2023-06-10)
- XBC.1.1.2 (2023-06-10)
- XBL.3.1 (2023-06-10)
- GQ.1 (2023-06-10)
- CH.1.1.30 (2023-06-10)
- BR.5.1 (2023-06-10)
- FL.10.1 (2023-06-10)
- XBB.1.15.1 (2023-06-11)
- XBB.1.44 (2023-06-11)
- XBB.1.44.1 (2023-06-11)
- XBB.1.45 (2023-06-11)
- XBB.1.45.1 (2023-06-11)
- EU.1.1.2 (2023-06-11)
- XBB.1.46 (2023-06-11)
- XBB.1.47 (2023-06-11)
- XBB.1.47.1 (2023-06-11)
- XBB.2.11 (2023-06-11)
- XBB.2.11.1 (2023-06-11)
- XCG (2023-06-11)
- XBB.1.14.1 (2023-06-11)
- XBB.2.6.3 (2023-06-11)
- XBB.1.48 (2023-06-11)
- XBB.1.13.1 (2023-06-11)
- XBB.1.38.1 (2023-06-11)
- XBB.1.4.2 (2023-06-11)
- XBB.2.12 (2023-06-11)
- FL.2.3 (2023-06-12)
- FY.1.2 (2023-06-12)
- FY.1.3 (2023-06-12)
- FY.5 (2023-06-12)
- FL.2.2.1 (2023-06-12)
- XBB.1.16.10 (2023-06-12)
- GR.1 (2023-06-12)
- GB.2 (2023-06-12)
- GS.1 (2023-06-12)
- XBB.1.5.87 (2023-06-13)
- FL.1.6 (2023-06-13)
- FL.17 (2023-06-14)
- FL.17.1 (2023-06-14)
- FL.17.2 (2023-06-14)
- XBB.1.16.11 (2023-06-14)
- XBC.1.6.4 (2023-06-14)
- GT.1 (2023-06-14)

</details>

## 2023-05-10

### New SARS-CoV-2 dataset version (tag `2023-05-10T12:00:00Z`)

- The most terminal 50bp are now ignored/masked for reference tree placement purposes, see the [Nextclade changelog](https://github.com/nextstrain/nextclade/blob/master/CHANGELOG.md#algorithm--datasets-enable-masked-sites-for-distance-calculation) for details. This feature requires Nextclade v2.14.0 or later. Most sequences will be unaffected. As the only mutation appearing in this range in the reference tree is C44T in some BA.2/4/5 and XBB sequences.
- Labeled mutations have been updated. Criteria for inclusion have been relaxed to show slightly more non-clade defining mutations that commonly occurred within a clade, e.g. BN.1 and CH.1.1 defining mutations are now included under clade 22D (BA.2.75). This potentially worsens quality score for some sequences with such mutations.
- Pango lineages designated between 2023-04-18 and 2023-05-09 are now included, unfold below to see a list with designation dates:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- XBL.1 (2023-04-19)
- XBL.2 (2023-04-19)
- XBL.3 (2023-04-19)
- XBB.2.3.6 (2023-04-19)
- XBB.2.3.7 (2023-04-19)
- XBB.1.34 (2023-04-20)
- FR.1 (2023-04-21)
- FS.1 (2023-04-21)
- XCC (2023-04-22)
- EG.3 (2023-04-22)
- EG.1.2 (2023-04-22)
- EG.1.3 (2023-04-22)
- EG.1.4 (2023-04-22)
- EG.4 (2023-04-22)
- EG.5 (2023-04-22)
- FL.3 (2023-04-22)
- FL.4 (2023-04-22)
- FL.5 (2023-04-22)
- FK.1.2 (2023-04-22)
- FT.1 (2023-04-22)
- XAY.2.3 (2023-04-22)
- XAY.1.1.2 (2023-04-22)
- XAY.1.1.3 (2023-04-22)
- XBB.1.16.2 (2023-04-22)
- XBB.1.16.3 (2023-04-22)
- FU.1 (2023-04-22)
- FU.2 (2023-04-22)
- XBB.1.5.41 (2023-04-22)
- XBB.1.5.42 (2023-04-22)
- FL.2.1 (2023-04-22)
- FL.2.2 (2023-04-22)
- XBC.1.6.1 (2023-04-23)
- XBC.1.6.2 (2023-04-23)
- XBC.1.6.3 (2023-04-23)
- XBC.1.5.43 (2023-04-23)
- XBB.1.35 (2023-04-23)
- XBB.1.5.44 (2023-04-23)
- XBB.1.5.45 (2023-04-23)
- XBB.1.5.46 (2023-04-23)
- XBB.1.6.1 (2023-04-23)
- XBB.1.5.43 (2023-04-24)
- XBB.1.36 (2023-04-24)
- XBB.8.1 (2023-04-24)
- XBB.9 (2023-04-24)
- XBB.3.4 (2023-04-24)
- XBB.1.5.47 (2023-04-25)
- XBB.1.5.48 (2023-04-25)
- XBB.1.5.49 (2023-04-25)
- EU.1.1.1 (2023-04-26)
- XBB.1.5.50 (2023-04-26)
- XBB.1.5.51 (2023-04-26)
- XBB.1.5.52 (2023-04-26)
- FV.1 (2023-04-26)
- XBB.1.5.53 (2023-04-26)
- XBB.1.9.6 (2023-04-26)
- BQ.1.2.2 (2023-04-28)
- FW.1 (2023-05-01)
- FW.2 (2023-05-01)
- XBB.1.5.54 (2023-05-01)
- EK.4 (2023-05-01)
- XBB.2.3.8 (2023-05-01)
- FD.3 (2023-05-03)
- XBB.1.5.55 (2023-05-03)
- FL.6 (2023-05-03)
- XBB.2.3.9 (2023-05-04)
- XBB.2.3.10 (2023-05-04)
- FY.1 (2023-05-04)
- FY.2 (2023-05-04)
- FY.3 (2023-05-04)
- FY.4 (2023-05-04)
- FZ.1 (2023-05-05)
- FZ.1.1 (2023-05-05)
- FZ.2 (2023-05-05)
- XBB.1.5.56 (2023-05-05)
- XBB.1.16.4 (2023-05-05)
- XBB.1.5.57 (2023-05-05)
- FE.1.1 (2023-05-05)
- FE.1.2 (2023-05-05)
- GA.1 (2023-05-06)
- GA.2 (2023-05-06)
- GA.3 (2023-05-06)
- CH.1.1.24 (2023-05-06)
- CH.1.1.25 (2023-05-06)
- CH.1.1.26 (2023-05-06)
- DV.6 (2023-05-06)
- CH.1.1.27 (2023-05-06)
- XBB.1.5.58 (2023-05-06)
- XBB.1.5.59 (2023-05-06)
- XBB.1.5.60 (2023-05-06)
- XBB.1.5.61 (2023-05-06)
- XBB.1.5.62 (2023-05-06)
- XBB.1.5.63 (2023-05-06)
- XBB.1.5.64 (2023-05-06)
- XBB.1.5.65 (2023-05-06)
- XBB.1.5.66 (2023-05-06)
- XBB.1.5.67 (2023-05-06)
- GB.1 (2023-05-06)
- XBB.1.16.5 (2023-05-06)
- FD.4 (2023-05-06)
- FL.7 (2023-05-06)
- XBB.1.5.68 (2023-05-06)
- XBB.1.37 (2023-05-06)
- XBB.1.37.1 (2023-05-06)
- XBB.1.5.69 (2023-05-07)
- XBB.1.16.6 (2023-05-07)
- EG.5.1 (2023-05-07)
- GC.1 (2023-05-07)
- GC.2 (2023-05-07)
- FL.8 (2023-05-07)
- FL.9 (2023-05-07)
- FL.10 (2023-05-07)
- FL.11 (2023-05-07)
- CH.1.1.28 (2023-05-07)
- FL.3.1 (2023-05-07)
- FL.3.2 (2023-05-07)
- FL.3.3 (2023-05-07)
- FL.3.4 (2023-05-07)
- XBB.1.24.1 (2023-05-07)
- XBB.1.24.2 (2023-05-07)
- XBB.1.24.3 (2023-05-07)
- XBB.1.38 (2023-05-07)
- GD.1 (2023-05-07)
- XBB.1.39 (2023-05-07)
- XBB.1.40 (2023-05-07)
- GE.1 (2023-05-07)
- XBB.2.3.11 (2023-05-07)
- FL.1.1 (2023-05-07)
- FL.1.2 (2023-05-07)
- FL.1.3 (2023-05-07)
- XBB.3.5 (2023-05-07)
- BN.1.2.5 (2023-05-07)
- FR.2 (2023-05-07)
- BN.1.2.6 (2023-05-07)
- EJ.3 (2023-05-07)
- BN.1.3.11 (2023-05-07)
- BQ.1.2.3 (2023-05-07)
- BQ.1.3.1 (2023-05-07)
- BQ.1.3.2 (2023-05-07)
- BQ.1.33 (2023-05-07)
- DN.2 (2023-05-07)
- DN.3 (2023-05-07)
- DN.3.1 (2023-05-07)
- XBB.1.32.1 (2023-05-08)
- FL.12 (2023-05-08)

</details>

## 2023-04-18

### New SARS-CoV-2 dataset version (tag `2023-04-18T12:00:00Z`)

#### `SARS-CoV-2` and `SARS-CoV-2-21L`

- New Nextstrain clade 23B (XBB.1.16) was added, see this [ncov PR](https://github.com/nextstrain/ncov/pull/1059) for a detailed discussion of this clade
- The `SARS-CoV-2` dataset now shows WHO variant name in the web results table instead of unaliased Pango lineage. This is a web-display-only change: All output files (web/CLI) are unchanged. Unaliased Pango lineage is still available in the `SARS-CoV-2-21L` dataset.
- Pango lineages designated between 2023-03-15 and 2023-04-17 are now included, unfold below to see a list with designation dates:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- ET.1 (2023-03-16)
- XBC.1.6 (2023-03-16)
- XBB.1.17 (2023-03-18)
- XBB.1.17.1 (2023-03-18)
- XBB.1.17.2 (2023-03-18)
- XBB.1.5.22 (2023-03-18)
- XBB.1.5.23 (2023-03-18)
- XBB.1.18 (2023-03-18)
- XBB.1.18.1 (2023-03-18)
- XBB.1.5.24 (2023-03-18)
- XBB.1.5.25 (2023-03-18)
- XBU (2023-03-19)
- XBB.1.19 (2023-03-19)
- XBB.1.19.1 (2023-03-19)
- XBB.1.20 (2023-03-19)
- XBV (2023-03-19)
- DV.1.1 (2023-03-19)
- CP.8 (2023-03-19)
- XBW (2023-03-19)
- XBY (2023-03-19)
- XBB.1.5.26 (2023-03-19)
- EU.1 (2023-03-19)
- EU.1.1 (2023-03-19)
- XBF.8.1 (2023-03-19)
- XBB.1.21 (2023-03-19)
- XBC.2.1 (2023-03-19)
- XBB.1.22 (2023-03-19)
- XBB.1.22.1 (2023-03-19)
- XBB.1.22.2 (2023-03-19)
- XBB.1.9.5 (2023-03-19)
- XBB.1.9.4 (2023-03-19)
- XBB.1.23 (2023-03-19)
- XBJ.1 (2023-03-19)
- XBJ.1.1 (2023-03-19)
- XBJ.2 (2023-03-19)
- XBJ.3 (2023-03-19)
- XBJ.4 (2023-03-19)
- XBB.2.7 (2023-03-19)
- XBB.1.27 (2023-03-19)
- XBB.1.24 (2023-03-20)
- XBB.1.25 (2023-03-20)
- XBB.1.26 (2023-03-20)
- CH.1.1.16 (2023-03-20)
- CH.1.1.17 (2023-03-20)
- DV.5 (2023-03-20)
- EV.1 (2023-03-21)
- EW.1 (2023-03-21)
- EW.2 (2023-03-21)
- EW.3 (2023-03-21)
- EY.1 (2023-03-21)
- EZ.1 (2023-03-21)
- XBB.1.16.1 (2023-03-22)
- XBB.1.5.27 (2023-03-22)
- EK.3 (2023-03-22)
- EK.2.1 (2023-03-22)
- XBB.1.5.28 (2023-03-22)
- BE.11 (2023-03-22)
- BE.12 (2023-03-22)
- BE.13 (2023-03-22)
- FA.1 (2023-03-22)
- FA.2 (2023-03-22)
- DR.2 (2023-03-22)
- FB.1 (2023-03-22)
- FB.2 (2023-03-22)
- BQ.1.1.72 (2023-03-22)
- FC.1 (2023-03-22)
- FD.1 (2023-03-22)
- FD.1.1 (2023-03-22)
- FE.1 (2023-03-22)
- XBB.1.5.29 (2023-03-22)
- XBB.1.5.30 (2023-03-22)
- FF.1 (2023-03-22)
- CP.8.1 (2023-03-23)
- BN.1.3.9 (2023-03-23)
- XBB.1.5.31 (2023-03-24)
- XBB.1.5.32 (2023-03-24)
- XBB.1.5.33 (2023-03-24)
- XBB.2.3.1 (2023-03-24)
- XBB.2.3.2 (2023-03-24)
- CH.1.1.18 (2023-03-24)
- XBB.1.28 (2023-03-24)
- XBB.1.29 (2023-03-24)
- XBB.1.5.34 (2023-03-24)
- XBB.1.30 (2023-03-24)
- XBB.1.5.35 (2023-03-24)
- XBB.1.5.36 (2023-03-24)
- BL.1.5 (2023-03-24)
- BQ.1.26.2 (2023-03-24)
- XBF.9 (2023-03-24)
- FG.1 (2023-03-24)
- FG.2 (2023-03-24)
- FG.3 (2023-03-24)
- CH.1.1.19 (2023-03-24)
- CH.1.1.20 (2023-03-24)
- CM.8.1.3 (2023-03-24)
- CM.8.1.4 (2023-03-24)
- DN.1.1.3 (2023-03-24)
- DN.1.1.4 (2023-03-24)
- XBB.2.8 (2023-03-24)
- XBB.2.7.1 (2023-03-24)
- BF.5.5 (2023-03-24)
- XBB.1.5.37 (2023-03-27)
- FD.2 (2023-03-27)
- XBB.1.5.38 (2023-03-27)
- FH.1 (2023-03-27)
- XBB.1.5.39 (2023-03-27)
- XBZ (2023-03-28)
- CH.1.1.21 (2023-03-29)
- CH.1.1.22 (2023-03-29)
- FJ.1 (2023-03-29)
- BN.1.3.10 (2023-03-30)
- FK.1 (2023-03-31)
- BQ.1.1.73 (2023-04-03)
- XCA (2023-04-03)
- EG.2 (2023-04-04)
- XBB.1.31 (2023-04-04)
- XBB.1.32 (2023-04-04)
- FL.1 (2023-04-04)
- XBB.2.3.3 (2023-04-04)
- XBB.2.3.4 (2023-04-04)
- XBB.1.5.40 (2023-04-04)
- FM.1 (2023-04-04)
- FM.2 (2023-04-04)
- FL.2 (2023-04-04)
- BQ.1.1.74 (2023-04-05)
- FN.1 (2023-04-05)
- EG.1.1 (2023-04-07)
- XBB.1.28.1 (2023-04-07)
- CJ.1.2 (2023-04-07)
- CJ.1.3 (2023-04-07)
- XBF.1.1 (2023-04-08)
- XBF.10 (2023-04-08)
- FP.1 (2023-04-11)
- BF.42 (2023-04-11)
- CH.1.1.23 (2023-04-11)
- XBB.2.3.5 (2023-04-12)
- FK.1.1 (2023-04-13)
- XCB (2023-04-14)
- FQ.1 (2023-04-17)
- XBB.1.33 (2023-04-18)

</details>

#### `SARS-CoV-2-no-recomb` will no longer be updated

Starting with this update, the `SARS-CoV-2-no-recomb` dataset - an auxiliary dataset with niche usage - will no longer be updated. This dataset was created to mitigate bias Nextclade had in previous versions to attach incomplete sequences to recombinants. This bias has been fixed in Nextclade version 2.13.0 (see this [CHANGELOG entry](https://github.com/nextstrain/nextclade/blob/master/CHANGELOG.md#attach-sequences-to-a-priori-most-likely-node-if-reference-tree-contains-placement_prior) for a detailed discussion). Furthermore, with the majority of current circulation being recombinant (mostly XBB), this dataset is no longer adequate. Users should simply use the main `SARS-CoV-2` dataset instead.

## 2023-04-02

### New dataset version (tag `2023-04-02T12:00:00Z`)

#### Influenza virus datasets

All Influenza virus datasets were updated with more recent sequences. The trees now include more older reference viruses for more robust designation of older clades.
The B/Vic annotation of the HA segment was fixed -- it was previously off by 3 nucleotides resulting in amino acid numbering being off by one.

## 2023-03-28

### Internal

- A typo in the configuration of the default reference sequence configuration for Flu H1N1pdm NA dataset prevented the dataset from being downloaded by Nextclade CLI. This is now fixed. This only affects dataset server infrastruture (index file) and does not change dataset files, so no new version of any dataset is released. See [#70](https://github.com/nextstrain/nextclade_data/pull/70).

## 2023-03-16

### New dataset version (tag `2023-03-16T12:00:00Z`)

#### SARS-CoV-2 datasets

- Placement priors: Every tree node is now annotated with a `placement_prior`, an approximate probability (on log10 scale) that a random sequence is attached to this node. For this dataset, the prior was caluclated after placing 300k sequences on the tree. A value of `-10` is chosen when no sequence in the sample attached to a node. The placement priors will improve placement accuracy of incomplete sequences (such as Spike only) - but only with a recent version of Nextclade (probably 2.13.0 and above). In that release, we will introduce a new placement tie-breaking feature: when a query sequence can attach to multiple nodes with equal number of mismatches, the sequence will be attached to the reference tree node with the highest prior. This is in contrast to the previous naive tie breaking logic which always chose the node with the fewest number of parent nodes. This lead to a bias towards attaching to recombinants. See <https://github.com/neherlab/nextclade_data_workflows/pull/38> for the code calculating the placement priors, and <https://github.com/nextstrain/nextclade/pull/1119> to see how the priors are used in Nextclade.
- Pango lineages designated between 2023-02-24 and 2023-03-15 are now included, unfold below to see a list of them:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- XBB.2.6 (2023-02-26)
- XBB.8 (2023-02-26)
- EM.1 (2023-02-26)
- XBB.1.5.15 (2023-02-26)
- EK.2 (2023-02-26)
- XBB.1.5.16 (2023-02-26)
- XBB.1.5.17 (2023-02-26)
- XBB.1.5.18 (2023-02-26)
- XBB.1.5.19 (2023-02-26)
- XBB.1.5.20 (2023-02-26)
- XBB.1.5.21 (2023-02-26)
- EN.1 (2023-02-26)
- EP.2 (2023-02-26)
- EP.1 (2023-02-26)
- XBC.1.5 (2023-02-26)
- EQ.1 (2023-02-28)
- CY.2 (2023-02-28)
- CP.7 (2023-03-02)
- BQ.1.1.71 (2023-03-03)
- XBB.1.16 (2023-03-05)
- ER.1 (2023-03-05)
- ER.1.1 (2023-03-07)
- ES.1 (2023-03-09)
- CH.1.1.15 (2023-03-09)
- BF.7.4.3 (2023-03-10)
- BQ.1.32 (2023-03-11)

</details>

### Internal

Add robots.txt to prevent data endpoints from indexing by search engines.

## 2023-02-25

### New dataset version (tag `2023-02-25T12:00:00Z`)

#### SARS-CoV-2 datasets

- Recombinant trees are now built using IQtree which results in shared mutations on internal nodes. In the past, recombinant trees were purely based on the Pango hierarchy. This change makes lineage assignment for recombinants more robust and reduces the number of private mutations. See e.g. the XBB tree here: <https://next.nextstrain.org/staging/nextclade/sars-cov-2/21L?label=clade:22F>
- Known stop codons and frame shifts were updated to reduce the number of false positive warnings
- The set of labeled mutations was updated (in `virus_properties.json`), including the addition of characteristic 23A mutations. This will help identifying recombinants.
- Pango lineages desiganted between 2023-02-01 and 2022-02-24 are now included, unfold below to see a list of them:

<details>
  <summary> Newly included lineages, with designation date in parentheses</summary>

- BN.1.3.5 (2023-02-02)
- XBB.1.9.2 (2023-02-03)
- XBB.2.4 (2023-02-03)
- DT.2 (2023-02-03)
- BA.4.1.11 (2023-02-03)
- BF.5.3 (2023-02-08)
- XBB.1.12 (2023-02-09)
- XBB.1.5.4 (2023-02-10)
- XBB.1.5.5 (2023-02-10)
- XBB.1.5.6 (2023-02-10)
- XBB.1.5.7 (2023-02-10)
- XBB.1.5.8 (2023-02-10)
- XBB.1.5.9 (2023-02-10)
- XBB.1.5.10 (2023-02-10)
- XBB.1.13 (2023-02-10)
- BQ.1.1.50 (2023-02-10)
- BF.5.4 (2023-02-10)
- XBB.1.14 (2023-02-10)
- BQ.1.1.51 (2023-02-10)
- XBF.1 (2023-02-11)
- XBF.2 (2023-02-11)
- XBF.3 (2023-02-11)
- XBC.1.3 (2023-02-11)
- XBC.1.4 (2023-02-11)
- XAY.2.1 (2023-02-11)
- XAY.2.2 (2023-02-11)
- XAY.1.1.1 (2023-02-11)
- BW.1.2 (2023-02-11)
- BW.1.1.1 (2023-02-11)
- BW.1.1.2 (2023-02-11)
- BQ.1.29 (2023-02-11)
- BQ.1.15.2 (2023-02-11)
- BQ.1.15.1 (2023-02-11)
- BQ.1.1.52 (2023-02-11)
- EA.1 (2023-02-11)
- EA.2 (2023-02-11)
- BQ.1.10.2 (2023-02-11)
- CL.1.2 (2023-02-11)
- CL.1.3 (2023-02-11)
- CL.1.1 (2023-02-11)
- BA.5.1.33 (2023-02-11)
- BA.5.1.34 (2023-02-11)
- BA.5.1.35 (2023-02-11)
- EB.1 (2023-02-11)
- BA.5.1.36 (2023-02-11)
- BA.5.1.37 (2023-02-11)
- BA.5.1.38 (2023-02-11)
- BF.7.16 (2023-02-11)
- BF.7.16.1 (2023-02-11)
- BF.7.17 (2023-02-11)
- BF.7.18 (2023-02-11)
- BF.35 (2023-02-11)
- BF.36 (2023-02-11)
- BF.37 (2023-02-11)
- BF.38 (2023-02-11)
- BF.38.1 (2023-02-11)
- BF.38.2 (2023-02-11)
- BF.38.3 (2023-02-11)
- BF.39 (2023-02-11)
- BF.39.1 (2023-02-11)
- BF.40 (2023-02-11)
- BF.41 (2023-02-11)
- BF.41.1 (2023-02-11)
- BA.5.2.51 (2023-02-11)
- BA.5.2.52 (2023-02-11)
- BA.5.2.53 (2023-02-11)
- BA.5.2.54 (2023-02-11)
- BA.5.2.55 (2023-02-11)
- BA.5.2.56 (2023-02-11)
- BA.5.2.57 (2023-02-11)
- BA.5.2.58 (2023-02-11)
- BA.5.2.59 (2023-02-11)
- BQ.1.30 (2023-02-11)
- EC.1 (2023-02-11)
- EC.1.1 (2023-02-11)
- BQ.1.31 (2023-02-11)
- BQ.1.10.3 (2023-02-11)
- BQ.1.1.53 (2023-02-11)
- BQ.1.1.54 (2023-02-11)
- BQ.1.1.55 (2023-02-11)
- BQ.1.1.56 (2023-02-11)
- BQ.1.1.57 (2023-02-11)
- BQ.1.1.58 (2023-02-11)
- BQ.1.1.59 (2023-02-11)
- BQ.1.1.60 (2023-02-11)
- BQ.1.1.61 (2023-02-11)
- BQ.1.1.62 (2023-02-11)
- BQ.1.1.63 (2023-02-11)
- BQ.1.1.64 (2023-02-11)
- BQ.1.1.65 (2023-02-11)
- BQ.1.1.66 (2023-02-11)
- BQ.1.1.67 (2023-02-11)
- DT.3 (2023-02-11)
- BQ.1.1.68 (2023-02-11)
- BQ.1.1.69 (2023-02-11)
- BQ.1.1.70 (2023-02-11)
- CZ.2 (2023-02-11)
- BA.5.2.60 (2023-02-12)
- BZ.2 (2023-02-12)
- BA.5.2.61 (2023-02-12)
- BA.5.2.62 (2023-02-12)
- BF.7.19 (2023-02-12)
- BF.7.20 (2023-02-12)
- BF.7.21 (2023-02-12)
- BF.7.22 (2023-02-12)
- BF.7.23 (2023-02-12)
- BF.7.24 (2023-02-12)
- BF.7.19.1 (2023-02-12)
- BF.7.26 (2023-02-12)
- ED.1 (2023-02-12)
- ED.2 (2023-02-12)
- ED.3 (2023-02-12)
- EE.1 (2023-02-12)
- EE.2 (2023-02-12)
- EE.3 (2023-02-12)
- EE.4 (2023-02-12)
- EE.5 (2023-02-12)
- EF.1 (2023-02-12)
- EF.2 (2023-02-12)
- EF.1.1 (2023-02-12)
- EF.1.1.1 (2023-02-12)
- EF.1.2 (2023-02-12)
- EF.1.3 (2023-02-12)
- BA.5.2.63 (2023-02-14)
- XBQ (2023-02-19)
- XBB.1.15 (2023-02-19)
- EG.1 (2023-02-19)
- XBB.1.9.3 (2023-02-19)
- XBB.2.5 (2023-02-19)
- XBF.4 (2023-02-19)
- XBK.1 (2023-02-19)
- XBR (2023-02-19)
- XBS (2023-02-19)
- XBT (2023-02-19)
- EH.1 (2023-02-19)
- XBF.5 (2023-02-19)
- XBF.6 (2023-02-19)
- XBF.7 (2023-02-19)
- XBF.7.1 (2023-02-19)
- XBF.8 (2023-02-19)
- DY.2 (2023-02-19)
- DY.3 (2023-02-19)
- DY.4 (2023-02-19)
- BF.7.14.4 (2023-02-19)
- BF.7.14.5 (2023-02-19)
- BF.7.14.6 (2023-02-19)
- BF.7.27 (2023-02-19)
- CH.1.1.10 (2023-02-19)
- CH.1.1.11 (2023-02-19)
- CH.1.1.12 (2023-02-19)
- CH.1.1.13 (2023-02-19)
- CH.1.1.14 (2023-02-19)
- BN.1.3.7 (2023-02-19)
- BN.1.3.6 (2023-02-19)
- BN.1.3.8 (2023-02-19)
- EJ.1 (2023-02-19)
- EJ.2 (2023-02-19)
- BN.1.2.2 (2023-02-19)
- BN.1.2.3 (2023-02-19)
- BN.1.2.4 (2023-02-19)
- BN.1.5.2 (2023-02-19)
- BN.1.4.2 (2023-02-19)
- BN.1.4.3 (2023-02-19)
- BN.1.4.4 (2023-02-19)
- BN.1.4.5 (2023-02-19)
- DS.3 (2023-02-19)
- XBB.1.5.11 (2023-02-19)
- XBB.1.5.12 (2023-02-19)
- XBB.1.5.13 (2023-02-19)
- EK.1 (2023-02-19)
- DV.4 (2023-02-19)
- XBB.1.5.14 (2023-02-21)
- EL.1 (2023-02-21)
- DB.3 (2023-02-23)
- DV.3.1 (2023-02-24)
- BF.7.14.7 (2023-02-24)

</details>

### New dataset version (tag `2023-02-03T12:00:00Z`)

#### RSV A and B data sets

- fix definition of some older clades
- include older sequences to make sure older clades are included.

## 2023-02-01

### New dataset version (tag `2023-02-01T12:00:00Z`)

#### SARS-CoV-2 datasets

- Change: Values output into the `clade` column of Nextclade csv/tsv files change from composite type: `20H (Beta, V2)` to simple year-letter: `20H`. If you do not want this change, simply use the column `clade_legacy` that is also output into the csv/tsv files. Other clade types are unchanged: `clade_nextstrain` (now same as `clade`), `clade_who` and `Nextclade_pango`.
- New Nextstrain clade `23A` added, equivalent to Pango lineage `XBB.1.5`, see <https://github.com/nextstrain/ncov/pull/1043> for details
- Data update: 55 new Pango lineages, with designation date between 2023-01-10 and 2023-01-31, are now included, unfold below to see all the lineages:

  <details>
    <summary> Newly included lineages, with designation date in parentheses</summary>

  - DU.1 (2023-01-12)
  - CH.1.1.5 (2023-01-13)
  - BQ.1.1.35 (2023-01-14)
  - DV.1 (2023-01-14)
  - BQ.1.1.36 (2023-01-14)
  - XBN (2023-01-14)
  - BA.5.1.32 (2023-01-15)
  - BA.5.2.50 (2023-01-21)
  - DW.1 (2023-01-23)
  - BQ.1.1.37 (2023-01-23)
  - BQ.1.1.38 (2023-01-24)
  - BF.7.14.1 (2023-01-25)
  - BQ.1.11.1 (2023-01-26)
  - BR.5 (2023-01-27)
  - BQ.1.1.39 (2023-01-27)
  - BQ.1.2.1 (2023-01-28)
  - DV.2 (2023-01-28)
  - DV.3 (2023-01-28)
  - CH.1.1.6 (2023-01-28)
  - CH.1.1.7 (2023-01-28)
  - CH.1.1.8 (2023-01-28)
  - CH.1.1.9 (2023-01-28)
  - BN.1.10 (2023-01-28)
  - BN.1.11 (2023-01-28)
  - BQ.1.1.40 (2023-01-28)
  - BQ.1.1.41 (2023-01-28)
  - BQ.1.1.42 (2023-01-28)
  - BQ.1.1.43 (2023-01-28)
  - BQ.1.1.44 (2023-01-28)
  - BQ.1.1.45 (2023-01-28)
  - BQ.1.1.46 (2023-01-28)
  - BQ.1.1.47 (2023-01-28)
  - CM.8.1.2 (2023-01-28)
  - CM.8.1.1 (2023-01-28)
  - DS.2 (2023-01-28)
  - XBB.1.10 (2023-01-28)
  - DY.1 (2023-01-28)
  - BF.7.14.2 (2023-01-28)
  - BF.7.14.3 (2023-01-28)
  - DZ.1 (2023-01-28)
  - XBB.1.5.1 (2023-01-28)
  - XBB.1.5.2 (2023-01-29)
  - XBB.1.5.3 (2023-01-29)
  - DN.1.1.1 (2023-01-30)
  - DN.1.1.2 (2023-01-30)
  - XBP (2023-01-30)
  - BQ.1.1.48 (2023-01-30)
  - BQ.1.1.49 (2023-01-30)
  - DZ.2 (2023-01-31)
  - XBB.7 (2023-01-31)
  - XBB.2.3 (2023-01-31)
  - XBB.1.11 (2023-01-31)
  - XBB.1.11.1 (2023-01-31)
  - DY.1.1 (2023-01-31)
  - DJ.1.1.1 (2023-01-31)

  </details>

#### Seasonal flu datasets

- removes a synonymous mutation from the definition of A/H3N2 clade 2a.3b. Some viruses that should be in this clade didn't have this change.
- adds glycosylation to the remaining flu data sets

## 2023-01-27

### Seasonal flu datasets

#### New dataset version (tag `2023-01-27T12:00:00Z`)

- fixes the omitted A/H3N2 clade 2d (very rare, had dropped out)
- adds more contextual sequences to the trees
- adds NA datasets for A/H3N2, A/H1N1pdm, B/Vic

### Monkeypox datasets

#### New dataset version (tag `2023-01-26T12:00:00Z`)

- New monkeypox lineages B.1.15, B.1.16, and B.1.17 were added to the datasets, see <https://github.com/mpxv-lineages/lineage-designation/pull/31> for details on these lineages.

## 2023-01-19

### Influenza datasets

#### New clade definitions for default influenza datasets (tag `2023-01-19T12:00:00Z`)

The default influenza datasets were updated to include recent consensus on clade definitions and more recent sequences in their reference tree to better reflect current circulation.
In addition, these data sets contain a `short_clade` column which omits the long prefix and definition of glycosylation motifs for a future software release.

## 2023-01-09

### All SARS-CoV-2 datasets

#### New dataset version (tag `2023-01-09T12:00:00Z`)

- Data update: 71 new Pango lineages, with designation date between 2022-12-14 and 2023-01-09 are now included, unfold below to see all the lineages:

  <details>
    <summary> Newly included lineages, with designation date in parentheses</summary>

  - CJ.1.1 (2022-12-14)
  - CM.5.2 (2022-12-15)
  - CM.4.1 (2022-12-15)
  - CN.2 (2022-12-15)
  - BE.10 (2022-12-15)
  - XBK (2022-12-15)
  - CH.3.1 (2022-12-15)
  - CH.1.1.3 (2022-12-15)
  - XBB.1.6 (2022-12-16)
  - CR.1.3 (2022-12-16)
  - BF.10.1 (2022-12-18)
  - BQ.1.25.1 (2022-12-21)
  - BN.1.3.2 (2022-12-21)
  - BN.1.3.3 (2022-12-22)
  - XBB.3.2 (2022-12-22)
  - XBB.2.1 (2022-12-22)
  - XBB.2.2 (2022-12-22)
  - XBB.1.7 (2022-12-22)
  - DN.1 (2022-12-22)
  - BQ.1.1.29 (2022-12-22)
  - BQ.1.27 (2022-12-22)
  - BQ.1.1.30 (2022-12-22)
  - DJ.1.3 (2022-12-23)
  - BQ.1.1.31 (2022-12-24)
  - DP.1 (2022-12-24)
  - BN.1.3.4 (2022-12-24)
  - XBB.3.3 (2022-12-24)
  - DN.1.1 (2022-12-25)
  - BQ.1.13.1 (2022-12-25)
  - BF.5.1 (2022-12-27)
  - BF.5.2 (2022-12-27)
  - CK.1.1 (2022-12-29)
  - BA.5.2.46 (2022-12-30)
  - BQ.1.28 (2022-12-31)
  - BQ.1.1.32 (2022-12-31)
  - BQ.1.1.33 (2022-12-31)
  - DF.1.1 (2023-01-01)
  - BA.5.2.47 (2023-01-01)
  - DQ.1 (2023-01-01)
  - DR.1 (2023-01-03)
  - BF.7.14 (2023-01-06)
  - BA.5.2.48 (2023-01-06)
  - DS.1 (2023-01-07)
  - CM.10 (2023-01-07)
  - XBC.1.1 (2023-01-07)
  - XBC.1.1.1 (2023-01-07)
  - XBC.1.2 (2023-01-07)
  - XBC.1.2.1 (2023-01-07)
  - XBB.1.8 (2023-01-07)
  - BL.6 (2023-01-07)
  - CH.1.1.4 (2023-01-07)
  - BF.7.15 (2023-01-09)
  - XBL (2023-01-09)
  - CM.11 (2023-01-09)
  - DT.1 (2023-01-09)
  - BQ.1.1.34 (2023-01-09)
  - CM.12 (2023-01-09)
  - CK.1.2 (2023-01-09)
  - BA.2.3.22 (2023-01-09)
  - XBM (2023-01-09)
  - BM.1.1.4 (2023-01-09)
  - BM.1.1.5 (2023-01-09)
  - BN.1.4.1 (2023-01-09)
  - XBB.6 (2023-01-09)
  - XBB.6.1 (2023-01-09)
  - XBB.1.9 (2023-01-09)
  - XBB.1.9.1 (2023-01-09)
  - BA.5.2.49 (2023-01-09)
  - XAY.3 (2023-01-09)
  - XAY.1.2 (2023-01-09)
  - BN.1.5.1 (2023-01-09)

  </details>

## 2022-12-22

### Addition of RSV A and RSV B datasets

#### New dataset version (tag `2022-12-20T22:00:12Z`)

First release of RSV A and RSV A datasets by Laura Urbanska.
With permission of the authors, these datasets use the reference sequences hRSV/A/England/397/2017 for RSV-A and hRSV/B/Australia/VIC-RCH056/2019 for RSV-B.
The datasets implement two clade designation each.
One is primarily based on the G gene and was proposed by [Goya et al](https://onlinelibrary.wiley.com/doi/abs/10.1111/irv.12715), the other is based on the entire genome and was proposed by [Ramaekers et al](https://doi.org/10.1093/ve/veaa052).

## 2022-12-14

### All SARS-CoV-2 datasets

#### New dataset version (tag `2022-12-14T12:00:00Z`)

- Data update: 28 new Pango lineages, with designation date between 2022-11-14 and 2022-12-10 are now included, unfold below to see all the lineages:

  <details>
    <summary> 28 new Pango lineages included in this release, with designation date in parentheses</summary>

  - XBG (2022-11-14)
  - BA.5.1.31 (2022-11-15)
  - XBH (2022-11-16)
  - BW.1.1 (2022-11-20)
  - BN.1.8 (2022-11-22)
  - BQ.1.1.25 (2022-11-22)
  - CM.2.1 (2022-11-22)
  - DJ.1 (2022-11-23)
  - DJ.1.1 (2022-11-23)
  - BA.5.2.42 (2022-11-23)
  - XBB.1.4.1 (2022-11-25)
  - BA.5.2.43 (2022-11-26)
  - BN.1.9 (2022-11-28)
  - CH.1.1.1 (2022-11-29)
  - CH.1.1.2 (2022-11-29)
  - BA.5.2.44 (2022-11-29)
  - DK.1 (2022-11-30)
  - BQ.1.1.26 (2022-12-01)
  - XBJ (2022-12-01)
  - CH.3 (2022-12-01)
  - BQ.1.1.27 (2022-12-02)
  - DL.1 (2022-12-03)
  - BA.5.2.45 (2022-12-03)
  - BQ.1.1.28 (2022-12-04)
  - BQ.1.26.1 (2022-12-04)
  - CV.2 (2022-12-06)
  - DM.1 (2022-12-07)
  - DJ.1.2 (2022-12-10)

  </details>

- Added 5 new XBB.1.5 example sequences

## 2022-12-07

### Influenza datasets

#### New dataset version (tag `2022-12-07T08:35:53Z`)

#### A/H3N2: Update and addition of new reference sequence A/Darwin/6/2021

The existing dataset with reference sequence A/Wisconsin/67/2005 (CY163680) was updated to reflect recently circulating viruses.
A new dataset with reference sequence A/Darwin/6/2021 (EPI1857216), the current vaccine strain, was added.
In this latter data set, sequences are aligned to A/Darwin/6/2021 and mutations are called relative to this reference sequence.
This additional data set allows the more direct identification of changes relative to the vaccine virus.

#### A/H1N1dpm: Update and addition of new reference sequence A/Wisconsin/588/2019

The existing dataset with reference sequence A/California/07/2009 (CY121680) was updated to reflect recently circulating viruses.
A new dataset with reference sequence A/Wisconsin/599/2019 (MW626062), the current vaccine strain, was added.
In this latter data set, sequences are aligned to A/Wisconsin/599/2019 and mutations are called relative to this reference sequence.
This additional data set allows the more direct identification of changes relative to the vaccine virus.

#### B/Vic: Update

The existing dataset with reference sequence B/Brisbane/60/2008 (KX058884) was updated to reflect recently circulating viruses.

## 2022-11-15

### All SARS-CoV-2 datasets

#### New dataset version (tag `2022-11-15T12:00:00Z`)

- Data update: New Pango lineages, with designation date between 2022-10-27 and 2022-11-14 are now included, unfold below to see all the lineages:

  <details>
    <summary>New Pango lineages included in this release, with designation date in parentheses</summary>

  - BQ.1.1.14 (2022-10-31)
  - CW.1 (2022-10-31)
  - BQ.1.1.15 (2022-10-31)
  - BQ.1.1.16 (2022-10-31)
  - BQ.1.1.17 (2022-10-31)
  - BQ.1.1.18 (2022-10-31)
  - BQ.1.1.19 (2022-10-31)
  - BN.1.3.1 (2022-10-31)
  - BF.7.4.1 (2022-10-31)
  - BF.31 (2022-11-01)
  - BF.31.1 (2022-11-01)
  - BF.32 (2022-11-01)
  - BQ.1.21 (2022-11-01)
  - CY.1 (2022-11-01)
  - BA.2.9.7 (2022-11-01)
  - BQ.1.22 (2022-11-02)
  - BF.7.4.2 (2022-11-02)
  - CP.1.2 (2022-11-02)
  - CP.1.3 (2022-11-02)
  - CP.2 (2022-11-02)
  - CP.3 (2022-11-02)
  - CP.4 (2022-11-02)
  - CP.5 (2022-11-02)
  - CP.6 (2022-11-02)
  - CR.1.1 (2022-11-02)
  - BS.1.2 (2022-11-02)
  - CM.5.1 (2022-11-02)
  - BL.5 (2022-11-02)
  - XAY.1.1 (2022-11-03)
  - BQ.1.1.20 (2022-11-03)
  - BQ.1.1.21 (2022-11-03)
  - BQ.1.1.22 (2022-11-03)
  - CZ.1 (2022-11-03)
  - XBB.4.1 (2022-11-03)
  - BQ.1.23 (2022-11-03)
  - BA.5.2.38 (2022-11-03)
  - DA.1 (2022-11-03)
  - BF.7.13 (2022-11-03)
  - BF.7.13.1 (2022-11-03)
  - BF.7.13.2 (2022-11-03)
  - XBF (2022-11-03)
  - CA.3.1 (2022-11-03)
  - CM.7 (2022-11-04)
  - BA.5.2.39 (2022-11-04)
  - DB.1 (2022-11-04)
  - BF.33 (2022-11-04)
  - BA.4.6.5 (2022-11-04)
  - DC.1 (2022-11-04)
  - BQ.1.1.23 (2022-11-04)
  - BQ.1.1.24 (2022-11-04)
  - DD.1 (2022-11-04)
  - BE.6 (2022-11-04)
  - BE.7 (2022-11-04)
  - BE.8 (2022-11-04)
  - BA.5.11 (2022-11-04)
  - DB.2 (2022-11-04)
  - BQ.1.24 (2022-11-04)
  - BA.5.2.40 (2022-11-04)
  - BQ.1.25 (2022-11-05)
  - CQ.1.1 (2022-11-05)
  - CR.1.2 (2022-11-05)
  - DE.1 (2022-11-05)
  - DE.2 (2022-11-05)
  - CM.8 (2022-11-05)
  - DF.1 (2022-11-06)
  - XBB.1.4 (2022-11-06)
  - BF.34 (2022-11-08)
  - XBB.1.5 (2022-11-08)
  - DG.1 (2022-11-09)
  - DH.1 (2022-11-09)
  - BR.2.1 (2022-11-09)
  - BN.1.7 (2022-11-10)
  - CM.8.1 (2022-11-10)
  - CM.9 (2022-11-10)
  - CM.6.1 (2022-11-10)
  - BE.9 (2022-11-12)
  - BQ.1.26 (2022-11-12)
  - BF.7.5.1 (2022-11-13)
  - BA.5.2.41 (2022-11-13)
  - CK.3 (2022-11-14)

  </details>

## 2022-11-03

### All monkeypox datasets

#### New dataset version (tag `2022-11-03T00:00:00Z`)

- New monkeypox lineages A.2.3, A.3, B.1.13 and B.1.14 were added to the dataset, see https://github.com/mpxv-lineages/lineage-designation/pull/28 for details on these lineages.

## 2022-10-27

### All SARS-CoV-2 datasets

#### New dataset version (tag `2022-10-27T12:00:00Z`)

- Phase 1 of migration of clade labels started: We will migrate clade labels from being a composite of Nextstrain clade, WHO name and legacy names (e.g. `20J (Gamma, V3)`) to a set of independent clade labels.
  Phase 1 does not make braking changes. `clade` remains composite as in the past. However, 3 new clade columns are introduced (in the TSV/CSV only so far): `clade_nextstrain` (e.g. `20J`) and `clade_who` (e.g. `Gamma`) and `clade_legacy` (e.g. `20J (Gamma, V3`).
  If you don't want to change your code, you can future proof it by starting to use `clade_legacy` instead of `clade`, which is identical at the moment, but in the mid-term (earliest a month) `clade` may change. However, `clade_legacy` will remain part of the dataset for much longer.
  If you want to start using new split clades, you can start using `clade_nextstrain` and `clade_who` from now on.
  Phase 2 which will happen at the earliest in a month (2022-12-01) will involve changing `clade` from being composite and identical with `clade_legacy` to being identical with `clade_nextstrain`.
  Phase 3 which will happen at the earliest in 6 months (2022-04-01) may involve dropping `clade_legacy` and `clade_nextstrain`.
- New clade `22F (Omicron)` (XBB) added, see <https://github.com/nextstrain/ncov/pull/1020> for details, e.g. on the reasons for elevation
- `virus_properties.json` has been updated with mutations characteristic of clades `22E` (BQ.1) and `22F` (XBB) to enable detection of contamination/recombination involving these clades
- `qc.json` has been updated with common frameshifts and stop codons that appear in hundreds of sequences and plausibly occur in viable virus
- Data update: New Pango lineages, with designation date between 2022-09-20 and 2022-10-27 are now included, unfold below to see all the lineages:

  <details>
    <summary>New Pango lineages included in this release</summary>

  - XBB.4 (2022-10-20)
  - XBB.3.1 (2022-10-20)
  - XBB.5 (2022-10-20)
  - BQ.1.1.3 (2022-10-20)
  - BQ.1.1.4 (2022-10-20)
  - BQ.1.1.5 (2022-10-20)
  - BQ.1.1.6 (2022-10-20)
  - BQ.1.1.7 (2022-10-20)
  - BQ.1.1.8 (2022-10-20)
  - BQ.1.1.9 (2022-10-20)
  - BQ.1.1.10 (2022-10-20)
  - BN.1.2.1 (2022-10-20)
  - BN.1.4 (2022-10-20)
  - BN.1.5 (2022-10-20)
  - BN.1.6 (2022-10-20)
  - CK.2 (2022-10-20)
  - CK.2.1 (2022-10-20)
  - CK.2.1.1 (2022-10-20)
  - CQ.2 (2022-10-20)
  - BQ.1.1.11 (2022-10-21)
  - BQ.1.1.12 (2022-10-21)
  - BY.1.1 (2022-10-21)
  - BY.1.1.1 (2022-10-21)
  - BY.1.2 (2022-10-21)
  - BY.1.2.1 (2022-10-21)
  - CM.4 (2022-10-21)
  - CM.5 (2022-10-21)
  - CM.6 (2022-10-21)
  - XBE (2022-10-22)
  - BU.3 (2022-10-23)
  - BA.5.1.30 (2022-10-23)
  - CV.1 (2022-10-23)
  - XBB.1.3 (2022-10-23)
  - BQ.1.1.13 (2022-10-23)
  - CA.7 (2022-10-24)

  </details>

## 2022-10-19

### All SARS-CoV-2 datasets

#### New dataset version (tag `2022-10-19T12:00:00Z`)

- New clade `22E (Omicron)` (BQ.1\*) added, see <https://github.com/nextstrain/ncov/pull/1012> for details
- The SARS-CoV-2 trees are now purely based on Pango consensus sequences, and no longer contain any actual sequences. This makes builds more stable and helps mitigate issues with sequence artefacts. For the Omicron part of the tree, no actual sequences were ever included, so this change only affects the pre-Omicron part of the reference tree.
- This release contains the first recombinant sublineages. These work in the same way as the other sublineages.
- Data update: New Pango lineages, with designation date between 2022-09-25 and 2022-10-19 are now included, unfold below to see all the lineages:

  <details>
    <summary>New Pango lineages included in this release</summary>

  - BA.5.2.26 (designation date: 2022-09-29)
  - BA.5.2.27 (designation date: 2022-09-29)
  - BA.5.2.28 (designation date: 2022-09-29)
  - BA.5.1.22 (designation date: 2022-09-29)
  - BA.5.1.23 (designation date: 2022-09-29)
  - BA.5.1.24 (designation date: 2022-09-29)
  - BA.5.1.25 (designation date: 2022-09-29)
  - BF.26 (designation date: 2022-09-29)
  - BF.27 (designation date: 2022-09-29)
  - BF.28 (designation date: 2022-09-29)
  - CA.2 (designation date: 2022-09-30)
  - BA.2.75.9 (designation date: 2022-09-30)
  - CB.1 (designation date: 2022-09-30)
  - BL.1.3 (designation date: 2022-09-30)
  - BS.1.1 (designation date: 2022-09-30)
  - BA.2.85 (designation date: 2022-09-30)
  - BA.5.2.29 (designation date: 2022-09-30)
  - BE.4 (designation date: 2022-09-30)
  - BE.4.1 (designation date: 2022-09-30)
  - BE.4.1.1 (designation date: 2022-09-30)
  - BE.1.1.2 (designation date: 2022-09-30)
  - CC.1 (designation date: 2022-09-30)
  - BA.5.2.30 (designation date: 2022-09-30)
  - BA.5.2.31 (designation date: 2022-09-30)
  - CD.1 (designation date: 2022-09-30)
  - CD.2 (designation date: 2022-09-30)
  - BA.5.2.32 (designation date: 2022-09-30)
  - BA.5.2.33 (designation date: 2022-09-30)
  - CE.1 (designation date: 2022-09-30)
  - BA.5.1.26 (designation date: 2022-09-30)
  - BA.5.1.27 (designation date: 2022-09-30)
  - BA.5.1.28 (designation date: 2022-09-30)
  - CF.1 (designation date: 2022-09-30)
  - CG.1 (designation date: 2022-10-03)
  - XBB.1 (designation date: 2022-10-03)
  - BQ.1.4 (designation date: 2022-10-03)
  - XBC.1 (designation date: 2022-10-03)
  - BF.7.1 (designation date: 2022-10-05)
  - BA.5.3.5 (designation date: 2022-10-07)
  - BA.5.1.29 (designation date: 2022-10-07)
  - BQ.1.5 (designation date: 2022-10-11)
  - BQ.1.6 (designation date: 2022-10-11)
  - BQ.1.7 (designation date: 2022-10-11)
  - BQ.1.8 (designation date: 2022-10-11)
  - BQ.1.9 (designation date: 2022-10-11)
  - BA.5.6.3 (designation date: 2022-10-11)
  - BG.7 (designation date: 2022-10-11)
  - BA.4.6.2 (designation date: 2022-10-11)
  - BE.4.2 (designation date: 2022-10-11)
  - BA.4.6.3 (designation date: 2022-10-11)
  - CH.1 (designation date: 2022-10-11)
  - CH.2 (designation date: 2022-10-11)
  - CJ.1 (designation date: 2022-10-11)
  - CK.1 (designation date: 2022-10-11)
  - CL.1 (designation date: 2022-10-11)
  - CM.1 (designation date: 2022-10-11)
  - BR.4 (designation date: 2022-10-12)
  - CN.1 (designation date: 2022-10-12)
  - BA.5.2.34 (designation date: 2022-10-12)
  - XBD (designation date: 2022-10-12)
  - BA.2.38.4 (designation date: 2022-10-12)
  - BF.29 (designation date: 2022-10-12)
  - CH.1.1 (designation date: 2022-10-13)
  - BQ.1.10 (designation date: 2022-10-13)
  - BQ.1.11 (designation date: 2022-10-13)
  - BQ.1.12 (designation date: 2022-10-13)
  - BQ.1.13 (designation date: 2022-10-13)
  - BQ.1.14 (designation date: 2022-10-13)
  - BQ.1.15 (designation date: 2022-10-13)
  - BQ.1.16 (designation date: 2022-10-13)
  - XAY.1 (designation date: 2022-10-13)
  - XAY.2 (designation date: 2022-10-13)
  - BA.2.3.21 (designation date: 2022-10-13)
  - CM.2 (designation date: 2022-10-13)
  - BQ.2 (designation date: 2022-10-13)
  - BQ.1.17 (designation date: 2022-10-13)
  - CP.1 (designation date: 2022-10-13)
  - CP.1.1 (designation date: 2022-10-13)
  - BA.5.2.35 (designation date: 2022-10-13)
  - BE.5 (designation date: 2022-10-13)
  - CQ.1 (designation date: 2022-10-13)
  - BF.7.2 (designation date: 2022-10-13)
  - BN.1.1 (designation date: 2022-10-13)
  - CR.1 (designation date: 2022-10-13)
  - CR.2 (designation date: 2022-10-13)
  - CS.1 (designation date: 2022-10-14)
  - BL.2.1 (designation date: 2022-10-14)
  - BF.7.3 (designation date: 2022-10-14)
  - BF.30 (designation date: 2022-10-14)
  - BM.2.1 (designation date: 2022-10-14)
  - BM.2.2 (designation date: 2022-10-14)
  - BM.2.3 (designation date: 2022-10-14)
  - BM.6 (designation date: 2022-10-14)
  - BA.4.6.4 (designation date: 2022-10-14)
  - XBC.2 (designation date: 2022-10-14)
  - BN.1.2 (designation date: 2022-10-15)
  - BN.1.1.1 (designation date: 2022-10-15)
  - BN.1.3 (designation date: 2022-10-15)
  - BN.3 (designation date: 2022-10-15)
  - BR.1.1 (designation date: 2022-10-15)
  - BR.1.2 (designation date: 2022-10-15)
  - BA.2.75.10 (designation date: 2022-10-15)
  - BM.1.1.2 (designation date: 2022-10-15)
  - BQ.1.1.1 (designation date: 2022-10-15)
  - BQ.1.18 (designation date: 2022-10-15)
  - BQ.1.8.1 (designation date: 2022-10-15)
  - BQ.1.8.2 (designation date: 2022-10-15)
  - BQ.1.10.1 (designation date: 2022-10-15)
  - XBB.2 (designation date: 2022-10-15)
  - XBB.3 (designation date: 2022-10-15)
  - XBB.1.1 (designation date: 2022-10-15)
  - BA.5.2.36 (designation date: 2022-10-15)
  - CT.1 (designation date: 2022-10-15)
  - BN.3.1 (designation date: 2022-10-15)
  - BN.4 (designation date: 2022-10-15)
  - BN.5 (designation date: 2022-10-15)
  - BN.6 (designation date: 2022-10-15)
  - CA.3 (designation date: 2022-10-15)
  - CA.4 (designation date: 2022-10-15)
  - CA.5 (designation date: 2022-10-15)
  - BM.1.1.3 (designation date: 2022-10-15)
  - CM.3 (designation date: 2022-10-15)
  - BQ.1.19 (designation date: 2022-10-15)
  - BU.2 (designation date: 2022-10-15)
  - BL.1.4 (designation date: 2022-10-16)
  - BQ.1.20 (designation date: 2022-10-16)
  - CA.6 (designation date: 2022-10-16)
  - BF.11.1 (designation date: 2022-10-16)
  - BF.11.3 (designation date: 2022-10-16)
  - BF.11.2 (designation date: 2022-10-16)
  - BF.11.4 (designation date: 2022-10-16)
  - BF.11.5 (designation date: 2022-10-16)
  - BF.7.4 (designation date: 2022-10-16)
  - BF.7.5 (designation date: 2022-10-16)
  - BF.7.6 (designation date: 2022-10-16)
  - BF.7.8 (designation date: 2022-10-16)
  - BF.7.7 (designation date: 2022-10-16)
  - BF.7.9 (designation date: 2022-10-16)
  - BF.7.10 (designation date: 2022-10-16)
  - BF.7.11 (designation date: 2022-10-16)
  - BF.7.12 (designation date: 2022-10-16)
  - BE.1.4 (designation date: 2022-10-16)
  - BE.1.4.2 (designation date: 2022-10-16)
  - BE.1.4.1 (designation date: 2022-10-16)
  - BE.1.4.3 (designation date: 2022-10-16)
  - BE.1.4.4 (designation date: 2022-10-16)
  - CU.1 (designation date: 2022-10-16)
  - XBB.1.2 (designation date: 2022-10-17)
  - BT.2 (designation date: 2022-10-17)
  - BA.5.6.4 (designation date: 2022-10-17)
  - BA.5.2.37 (designation date: 2022-10-17)
  - BQ.1.1.2 (designation date: 2022-10-19)
  </details>

## 2022-09-27

### New dataset version (tag `2022-09-27T12:00:00Z`)

#### All SARS-CoV-2 datasets

- Data update: New Pango lineages are included, see <https://github.com/cov-lineages/pango-designation/compare/efabcb6...cfe736> for new designations that are included
- Identical sequences have been removed from B.1\* lineages to reduce size of that part of the tree from ~1.6k to ~800.

##### BA.2 dataset (experimental)

- Reversions to wild type (Wuhan-Hu-1) are now labelled as `rev` to make it easier to spot problematic sequences
- The dataset now contains antibody escape and ACE2 binding data from two repositories of Jesse Bloom's group on Github: <https://jbloomlab.github.io/SARS-CoV-2-RBD_DMS_Omicron/epistatic-shifts/> and <https://jbloomlab.github.io/SARS2_RBD_Ab_escape_maps/escape-calc/>. For more information, please refer to: <https://doi.org/10.1093/ve/veac021>, <https://doi.org/10.1101/2022.09.15.507787> and <https://doi.org/10.1101/2022.09.20.508745>.

#### Monkeypox datasets

- New lineages A.2.2 and B.1.10-B.1.12 have been added, see here for details: <https://github.com/mpxv-lineages/lineage-designation/blob/master/designation_records/B.1.10-A.2.2_2022-09-26.md>

##### hMPXV B.1 dataset

- Mutations to a genotype found in MPXV-UK_P2 or MPXV-M5312_HM12_Rivers are now "labelled" as `rev` (reversion to reference). This should help identify wrong calls to reference when using the B.1 dataset. Until now, these artefacts were only visible as `reversions` when using the hMPXV or all-clades datasets.

##### MPXV (All clades)

- Frame shifts and stop codons that are encountered in a majority of sequences from clades IIa or I are now annotated as "known" mutations, which means that they do not influence the quality score. This should help increase the signal to noise ratio when uploading sequences from either of the clades.

## 2022-09-13

### New dataset version (tag `2022-09-13T12:00:00Z`)

#### All monkeypox datasets

- New lineages A.2.1 and B.1.9 have been added, see here for details: <https://github.com/mpxv-lineages/lineage-designation/blob/master/designation_records/B.1.9-A.2.1_2022-09-13.md>

## 2022-09-09

### New dataset version (tag `2022-09-09T12:00:00Z`)

#### All SARS-CoV-2 datasets

- Data update: New pango lineages are included, see <https://github.com/cov-lineages/pango-designation/compare/fcad365...efabcb6> for new designations that are included

#### Experimental BA.2 dataset (sars-cov-2-21L)

(Use this dataset via web as it is not guaranteed to be continued as the other datasets)

- Unaliased column: To help sort Nextclade web results by Pango lineage in a way that respects the meaning of aliases, there is now an unaliased column included, that writes out full lineage names as if there were no alias, e.g. BA.5.2 becomes B.1.1.529.5.2 and so forth. This has the additional advantage that you can learn what new aliases stand for.

## 2022-08-26

### New dataset version (tag `2022-08-26T12:00:00Z`)

#### All Monkeypox datasets

- New lineages B.1.6-B.1.8 have been added, see this PR for details: <https://github.com/mpxv-lineages/lineage-designation/pull/13/files>.
- Lineages are now colored using color ordering, making it easier to spot lineages that are closely related on the Auspice tree.

## 2022-08-23

### New dataset version (tag `2022-08-23T12:00:00Z`)

#### All SARS-CoV-2 datasets

- Data update: New pango lineages are included up to commit <https://github.com/cov-lineages/pango-designation/compare/42134608ae645853c333591ddadc345bfaf7ec13...fcad365d2fc11507a793c97e7ff26059d093c79f>)

## 2022-08-19

### Monkeypox datasets

#### New dataset version (tag `2022-08-19T12:00:00Z`)

##### All monkeypox datasets

Clade names now follow the convention agreed during WHO consultation:

- Clade 1 -> Clade I
- Clade 2 -> Clade IIa
- Clade 3 -> Clade IIb

The common ancestor of clade IIa and clade IIb is called clade II.

The clade/lineage hierarchy now has a middle level called `outbreak`. For now there is just one outbreak called `hMPXV-1` but in the future other clusters that may be worth naming may get an `outbreak` name - even if they don't get lineages of their own.

This middle level is output into Nextclade web and TSV/CSV files in the same way as `lineages`. The field is called `outbreak`. If a sequence does not belong to an outbreak, the field will be empty.

Sequences released by Genbank up to 2022-08-18 are included in the new dataset.

##### MPXV (All clades)

The reconstructed ancestor is now assigned clade `outgroup` - until now the clade field was empty.

The reference.fasta ID has been renamed to `reconstructed_ancestral_mpox_in_NC_063383_coordinates` as requested in issue [#35](https://github.com/nextstrain/nextclade_data/issues/35). This should not impact most users - the change only affects the name of the reference sequence as output to the alignment if you use Nextclade-CLI and include the `--include-reference` flag.

##### hMPXV-1 B.1 dataset

The reference.fasta ID has been renamed to `MPXV_USA_2022_MA001_in_NC_063383_coordinates`, see above for a description of the impact (for most people none).

## 2022-08-09

### New dataset version (tag `2022-08-09T12:00:00Z`)

#### All Monkeypox datasets

The datasets now include hMPXV-1 lineages B.1.1 to B.1.5. See details in <https://github.com/nextstrain/monkeypox/pull/95>

Sequences released to Genbank up to 2022-08-08 have been included in the new trees.

A B.1.5 sequence from Genbank has been added to the example sequences

##### MPXV (All clades)

Sequence KJ642615 (W-Nigeria/1971) has been excluded as it appears to be recombinant of clade 2 and clade 3. See details in <https://github.com/nextstrain/monkeypox/pull/102> - this sequence is not present in the other datasets, so no change there

### Experimental, SARS-CoV-2 dataset relative to BA.2 (`sars-cov-2-21L`)

This release includes a new type of SARS-CoV-2 dataset that is recommended for web use only.

It uses the Wuhan reference but with the SNPs that occur in BA.2.

This way, the mutation view is less overloaded and individual Spike mutations are easier to spot by eye.

Only lineages that descend from BA.2, BA.4 or BA.5 are included in this dataset.

Please do not use this dataset for tools that rely on data continuity as the dataset is comparatively new and brittle and may not be maintained indefinitely.

The current version has the tag `2022-07-26T12:00:00` and name `sars-cov-2-21L`

## 2022-07-27

### Influenza Yamagata HA

#### Bug fix release (tag `2022-07-27T12:00:00Z`)

Fix: The old tree used an incorrect genemap which caused Nextclade to crash. Now it works again.

Beware that Nextclade v2.0.0 until v2.3.0 have had a bug that means this dataset will crash.

You will have to upgrade to Nextclade v2.3.1 or use Nextclade v1 to use this dataset.

## 2022-07-26

### SARS-CoV-2 and SARS-CoV-2-no-recomb

#### Bug fix release (tag `2022-07-26T12:00:00Z`)

Fix: Ancestral reconstruction of mutations was wrong due to recombinants attaching directly to the root and causing the root mutations to be different from Wuhan.

This caused:

- _displayed_ mutations in Auspice to be wrong for all tips since around the time recombinants were first included in the tree (since `2022-03-24T12:00:00Z`)
- Some of the _calculated_ reconstructed mutations on _recombinants_ to be wrong, affecting nearest neighbor placement of _some_ recombinants.

The fix will cause a few recombinants to become recombinants and improve QC values of some recombinants but should not have large effects overall.
The biggest perceived impact will be that mutations displayed by Auspice will now be correct.

## 2022-07-22

### SARS-CoV-2 and SARS-CoV-2-no-recomb

#### New dataset version (tag `2022-07-22T12:00:00Z`)

- Clades: BA.2.75 has been given the Nextstrain clade name `22D`. Read more about the reasoning for the decision to give this lineage a name here <https://github.com/nextstrain/ncov/pull/984>
- Data update: New pango lineages are included up to commit <https://github.com/cov-lineages/pango-designation/compare/65cb2e04de0dc311600b396f7119babeb051b40e...42134608ae645853c333591ddadc345bfaf7ec13>)
- Fix: BA.2.38 no longer contains `6091T` as defining mutation, should therefore catch many more Indian BA.2.38 (report by @silcn in <https://github.com/nextstrain/nextclade/issues/935>)
- Fix: Genemap format now correct, compliant with GFF3, see <https://github.com/nextstrain/nextclade_data/issues/33> (report by @huddlej)
- virus_properties.json has been updated, including clade `22D`

## 2022-07-12

### SARS-CoV-2

#### New dataset version (tag `2022-07-12T12:00:00Z`)

- Fix: BA.2.75 lacked the characteristic S:R493Q reversion in the previous release, this is now fixed. This is the only change, otherwise this dataset is identical to `2022-07-11T12:00:00Z`.

## 2022-07-11

### SARS-CoV-2

#### New dataset version (tag `2022-07-11T12:00:00Z`)

- Pango lineages: In this release, Nextclade can assign Pango lineages up to BA.2.75 (commit <https://github.com/cov-lineages/pango-designation/commit/65cb2e04de0dc311600b396f7119babeb051b40e>)
- Alignment params: Retry reverse complement flag is now set to true, so that reverse complement is tried if seed matching fails.
- Fixes: Some synthetic pango lineage sequences had wrong mutations, this is now fixed through a manually curated override file.

## 2022-06-29

### MPXV B.1

#### New dataset version (tag `2022-06-29T12:00:00Z`)

- Increased number of B.1 samples from ~100 to ~200 to improve phylogenetic placement of analyzed 2022 outbreak sequences

## 2022-06-27

### New dataset version (tag `2022-06-27T12:00:00Z`)

#### SARS-CoV-2

- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.11, featuring a host of new BA.2, BA.4 and BA.5 sublineages and recombinants.
- Alignment params: Retry reverse complement flag is now set to true, so that reverse complement is tried if seed matching fails.

## 2022-06-16

### New dataset version (tag `2022-06-16T12:00:00Z`)

#### MPXV All Clades

- Reduced number of sample sequences to reduce number of markers and therefore improve web display performance

## 2022-06-14

### 3 Monkeypox (MPXV) datasets introduced

Three MPXV datasets are added with differing zoom levels containing:

- MPXV (All clades)
- hMPXV-1 (part of clade 3, source of 2017/2018/2022 outbreaks)
- hMPXV-1 B.1 (2022 outbreak lineage)

All 3 use the coordinate system of the recently designated NCBI Monkeypox reference sequence NC_063383 (MPXV-M5312_HM12_Rivers).

However, SNPs from two different ref sequences are added to the "all clades" and B.1 datasets to reduce the number of total mutations.

The B.1 dataset uses SNPs of ON563414.3 (MPXV_USA_2022_MA001) on top of a NC_063383 backbone.

The "all clades" build uses the SNPs of a reconstructed ancestral MPXV sequence that is the inferred most recent common ancestor of clades 1, 2 and 3, rooted with a Cowpox outgroup.

Only the MPXV (All clades) dataset can assign all clades 1, 2 and 3.
The hMPXV-1 dataset can be used if all viruses are from hMPXV-1.
The B.1 dataset is useful for 2022 outbreak sequences but will not be able to assign anything but B.1 lineages.

Gene annotations follow the annotation used by NC_063383 and is of the form `OPG001` (for OrthoPox Gene 001).
Since the alignment reference is always in NC_063383 coordinates, nucleotide and protein mutation position should usually be identical in alignments done with all three datasets.

Quality control parameters are subject to change, especially since "known" frame shifts and stop codons have not been annotated. For example, clade 1 sequences will always show around 7 frame shifts, yet these do not indicate quality problems.

### New dataset version (tag `2022-06-14T12:00:00Z`)

#### SARS-CoV-2

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.9 and beyond are now included, including among others `BA.5.1-BA.5.3`, `BA.2.35-BA.2.48` and `XV-XY`

## 2022-04-28

### New dataset version (tag `2022-04-28T12:00:00Z`)

#### SARS-CoV-2 (with and without recombinants)

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.8 are now included, including among others `BA.3.1`, `BA.2.14-BA.2.34` and `XT-XU` (in the default build, excluded from special "without recombinants" dataset).
- Clades: New Nextstrain clades included. `BA.4` is `22A (Omicron)`, `BA.5` is `22B (Omicron)` and `BA.2.12.1` is `22C (Omicron)`.

## 2022-04-08

### New dataset version (tag `2022-04-08T12:00:00Z`)

#### SARS-CoV-2 (with and without recombinants)

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.4 are now included, including among others `BA.4-5`, `BA.2.9-BA.2.13` and `XM-XS` (in the default build, excluded from special "without recombinants" dataset). For now, `BA.4-5` are included in Nextstrain clade `21L`, together with `BA.2` which is the most similar Omicron.
- Reference tree: The first 100 and last 200 sites (with respect to Wuhan reference) are now masked in the reference tree to reduce noise due to sites like `21` that were artifactually polymorphic.

## 2022-03-31

### New dataset version (tag `2022-03-31T12:00:00Z`)

#### SARS-CoV-2 (with and without recombinants)

- Pango lineages: New lineages added up till [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.137 are now included, including among others `BA.1.18-19`, `BA.2.4-BA.2.8` and `XG-XK` (in the default build, excluded from special "without recombinants" dataset).
- Dataset: The sampling of sequences has changed slightly. Previously, every Nextstrain clade got around 30 random sequences belonging to this clade causing quite a bit of movement between releases. This is no longer the case. The tree is thus slightly smaller. The change is most noticeable for small Nextstrain clades like `20F`.

## 2022-03-24

### New dataset version (tag `2022-03-24T12:00:00Z`)

#### SARS-CoV-2

- Recombinants: Recombinant Pango lineages are now included in the reference tree. Each recombinant is attached to the root node so as not to spawn false internal nodes in the tree that would attract bad sequences. As long as recombinants do not qualify for a Nextstrain clade, they will receive the place holder clade name `recombinant`. Pango lineages are provided if present. Beware that new unnamed recombinants with similar donors but slightly different breakpoint will attach to existing recombinants in the reference tree and thus get a wrong Pango lineage. A number of reversions and labeled mutations is a sign that you may have a similar but different recombinant.
- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.133, featuring Omicron recombinants like `XD`, `XE` and `XF`.
- QC: `qc.json` was updated with the most common stop codons and frameshifts that appear to be real and not artefacts (in ORFs 3a, 6, 7a, 7b,8, 9b)
- QC: `virus_properties.json` was updated and now contains more mutations that are common in `21K` which should help identifying recombinants

#### SARS-CoV-2 without recombinants

- New dataset: Now that recombinants are included in the default SARS-CoV-2 tree, it is no longer easy to identify breakpoints and donors of new recombinants if they attach to existing recombinants on the tree. To facilitate the analysis of new potential recombinants, we have added a new dataset named "SARS-CoV-2 without recombinants" that does not include recombinants and can thus be used for recombinant analysis as before the inclusion of recombinants. This dataset should only be used for recombinant analysis, it will receive less attention than the main (default) SARS-CoV-2 dataset.
- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.133, except recombinants (lineages starting with `X`).

## 2022-03-14

### New dataset version (tag `2022-03-14T12:00:00Z`)

#### SARS-CoV-2

- Pango lineages: Nextclade now assigns sequences a pango lineage, similar to how clades are assigned. Output is visible in both web and tsv/csv output (column `Nextclade_pango`). The classifier is about 98% accurate for sequences from the past 12 months. Older lineages are deprioritised, and accuracy is thus worse. Read more about the method and validation against pangoLEARN and UShER in this report: [Nextclade as pango lineage classifier: Methods and Validation](https://docs.nextstrain.org/projects/nextclade/en/latest/user/algorithm/nextclade-pango.html).
- Pango lineages: In this release, Nextclade can assign Pango lineages up to [pango-designation release](https://github.com/cov-lineages/pango-designation/releases) v1.2.132, featuring lineages like `BA.2.3`, `BA.1.17` and `BA.1.1.16`.
- Reference tree: Every pango lineage that's sampled in gets a synthetic sequence that is chosen to represent a hypothetical common ancestor of the lineage, according to the sequences listed as members in the pango-designation repo.

## 2022-02-07

### New dataset version (tag `2022-02-07T12:00:00Z`)

#### SARS-CoV-2

- Reference tree: Updated with new data. New algorithm for choosing how many of each pango lineage to include improves coverage of common and recent lineages. Every pango lineage that's included gets one relatively basal (early) sequence to keep number of false positive reversions down.

## 2022-01-18

### New dataset version (tag `2022-01-18T12:00:00Z`)

- Backwards incompatibility: New datasets no longer work for Nextclade versions before 1.10.0

#### SARS-CoV-2

- Files: added `virus_properties.json` containing common mutations per clade
- QC: higher penalty for private mutations that are reversions or common in other clades

#### Influenza

- Files: Stub `virus_properties.json` added to be compatible with new Nextclade version 1.10.0

## 2022-01-05

### SARS-CoV-2

#### New dataset version (tag `2022-01-05T19:54:31Z`)

- Reference tree: Added more Omicron sequences, from all of BA.1/BA.2/BA.3
- Reference tree: General data update with new pango lineages
- Sample sequences: Added BA.2 and BA.3 to sample sequences

## 2021-12-16

### Influenza

#### New dataset version (tag `2021-12-16T20:15:53Z`)

- Clades: New WHO clades names are used
- Reference tree: Data source is now GISAID which means better global coverage

### SARS-CoV-2

#### New dataset version (tag `2021-12-16T20:57:35Z`)

- Clades: `21M (Omicron)` added as Omicron catch all equivalent to pango `B.1.1.529`
- Clades: `21L` elevated to `21L (Omicron)` in line with WHO practice
- QC: Fixed known frameshift `ORF7b:3` (was erroneously `ORF7a:3`)

## 2021-12-09

### SARS-CoV-2

#### New dataset version (tag `2021-12-09T18:09:18Z`)

- Clades: Omicron is split into `21K (Omicron)` (pango `BA.1`) and `21L` (pango `BA.2`). The minor clade `21L` is at this point not called Omicron by WHO so it does not get the Omicron label for now.
- Reference tree: Data has been updated to early December
- Pango lineages designated until early December have been sampled in

## 2021-12-03--00-14-37--UTC

### General

- Added explicit cache-control headers

### SARS-CoV-2

#### New dataset version (tag `2021-12-03T00:20:15Z`)

- Sample sequences: Added two `21K (Omicron)` sequences

## 2021-11-27

### SARS-CoV-2

#### New dataset version (tag `2021-11-27T11:53:22Z`)

##### Changes

- Clades: `21K` is renamed `21K (Omicron)` in line with WHO elevation to VOC status

## 2021-11-26

### SARS-CoV-2

#### New dataset version (tag `2021-11-26T14:02:45Z`)

##### Changes

- Data source: GISAID data is now used to generate the reference tree. This switch is necessary, because the new clade 21K (B.1.1.529) is only present in GISAID data, thus far.

##### Updates

- New clade: 21K (B.1.1.529) has been added to the reference tree
- Reference tree: Data has been updated to sequences submitted to GISAID by 2021-11-24
- Reference tree: Pango lineages designated until 2021-11-24 have been sampled into the tree

## 2021-11-16

### SARS-CoV-2

#### New dataset version (tag `2021-11-16T16:38:05Z`)

##### Changes

- Reference tree: Recombinant pango lineages (= those starting with `X`) have been excluded in order to reduce clade misassignment noise, in particular for short sequences like just `S`. Only one recombinant has been designated so far (`XA`) and it broke up the branch leading up to Alpha exerting bad influence that warranted removal.
- QC rules: The lists of known, (likely) biological and thus acceptable frame shifts and stop codons have been extended. The ~20 most common frame shifts and ~40 most common stop codons on genes `ORF3a/6/7a/7b/8` are now declared known. Common frame shifts and stops on `ORF1a/b` and `S` are not declared known since these are most likely sequencing artefacts and not biological.

##### Updates

- Reference tree: Data has been updated to sequences submitted to Genbank by mid November
- Reference tree: Pango lineages designated until 2021-11-04 have been sampled into the tree
- Sample sequences

## 2021-10-11

### SARS-CoV-2

#### New dataset version (tag `2021-10-11T19:00:32Z`)

- Clades: Two Delta subclades have been designated by Nextstrain and are now included in Nextclade, see [Twitter announcement](https://twitter.com/nextstrain/status/1446903892864737280):
  > We've just updated Nextstrain clade designations to partition clade 21A (corresponding to the Delta WHO variant) into subclades 21I and 21J following our previously defined rules for defining clades when mutational and frequency thresholds are met.
  > Clade 21I is still a Delta variant virus, but possesses additional spike mutation A222V and ORF1a mutations P1640L, A3209V, V3718A and T3750I.
  > Clade 21J is still a Delta variant virus, but possesses additional ORF1a mutations A1306S, P2046L, P2287S, V2930L, T3255I and T3646A, ORF7b mutation T40I, as well as N mutation G215C. Clade 21J is now the predominate form of Delta with an estimated ~79% global frequency.
  > Clade defining mutations for clades 21I and 21J can be found in our public GitHub repo at: <https://github.com/nextstrain/ncov/blob/master/defaults/clades.tsv#L102>.
- Reference tree: Data has been updated to sequences submitted to Genbank by the first week of October.
- Reference tree: Pango lineages designated until 2021-10-10 have been sampled into the tree, including among others: AY.4.1-3, AY.34-39 [see pango release changes](https://github.com/cov-lineages/pango-designation/compare/v1.2.77...v1.2.84)

## 2021-09-30

### SARS-CoV-2

#### New dataset version (tag `2021-09-30T08:13:05Z`)

- Clades: changed name of clade "21H" to "21H (Mu)", as it has been designated a VOC by WHO
- Reference tree: masked a number of mutations that were either homoplasic (occurred independently in multiple lineages) or were error-prone (in Delta), to prevent these mutations from distorting the tree.
- Reference tree: now produced from a dedicated workflow that’s openly available and can be reproduced by anyone interested. The data used comes from Genbank, so it's publicly available and sharable by anyone without restrictions.
- Reference tree: changed sequence filtering to improve diversity on the tree, while excluding low quality sequences. For this we use the list of designated pango lineages. Every designated pango lineage with sequences in the last few months is represented on the reference tree.
- Reference tree: The new tree contains sequences that were published to Genbank up to mid September
- Example sequences: New example sequences are provided. Every Nextstrain clade is represented by at least 3 sequences. Furthermore, sequences that make the two QC rules `SNP cluster` and `rare mutations` fire have been added, to allow users to observe how such problematic sequences are flagged by Nextclade.
- QC rules: The following premature stop codons are treated as known and thus not indicative of quality problems: `ORF7a:62, ORF7a:94, ORF7b:33, ORF7b:39, ORF8:18, ORF8:19, ORF8:26, ORF8:27, ORF8:59, ORF8:67, ORF8:68, ORF8:106`.
- QC rules: The following frameshifts are treated as known and thus not indicative of quality problems: `ORF3a:257-276, ORF3a:259-276, ORF7a:62-122, ORF7a:63-122, ORF7a:77-122, ORF7a:102-122, ORF7b:42-44, ORF8:108-122, ORF8:120-122, ORF8:121-122, ORF8:122-123`.
- QC rules: The known stop codons and frameshifts were selected based on roughly the following criteria:
  - observed at least 5 times
  - observed in more than one lab
  - observed in sequences that are otherwise devoid of quality issues
  - observed in genes that are probably not essential for virus function

The Snakemake workflow producing the reference tree is now available at [github.com/neherlab/nextclade_data_workflows](https://github.com/neherlab/nextclade_data_workflows).

## 2021-08-31

Initial release of Nextclade Datasets.

It includes the existing SARS-CoV-2 dataset from
[github.com/nextstrain/nextclade/data/sars-cov-2](https://github.com/nextstrain/nextclade/tree/0817313f674471a49803cf1970bc92832207b4f5/data/sars-cov-2) as well as 4 new flu datasets:

- Influenza A H1N1pdm (rooted at "A/California/07/2009")
- Influenza A H3N2 (rooted at "A/Wisconsin/67/2005")
- Influenza B Victoria (rooted at "B/Brisbane/60/2008")
- Influenza B Yamagata (rooted at "B/Wisconsin/01/2010")
