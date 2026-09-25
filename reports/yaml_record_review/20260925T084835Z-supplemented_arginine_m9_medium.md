# YAML Record Review: SUPPLEMENTED (ARGININE) M9 MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/supplemented_arginine_m9_medium.yaml
- Started UTC: 2026-09-25T08:46:17Z
- Finished UTC: 2026-09-25T08:48:35Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:005290` in `data/merge_yaml/merged/supplemented_arginine_m9_medium.yaml`.
- Canonical source: `data/normalized_yaml/bacterial/KOMODO_450_SUPPLEMENTED_ARGININE_M9_MEDIUM.yaml`.
- Parent source: `data/normalized_yaml/bacterial/supplemented_arginine_m9_medium.yaml`.
- Canonical media term: `komodo.medium:450`, `SUPPLEMENTED (ARGININE) M9 MEDIUM`.
- Parent media term: `mediadive.medium:450`, `DSMZ Medium 450`.
- Merge fingerprint: `dc8675a3926302af3a02b5c9ac30ef5f2bb50e46d24a74cf605a1323657f071f`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record merges `komodo.medium:450` with `mediadive.medium:450`; the KOMODO source states `DSMZ Medium: 450 (mediadive.medium:450)`.
- Exact ignored-file-inclusive searches found `CultureMech:005290`, `CultureMech:001560`, `komodo.medium:450`, `mediadive.medium:450`, and the `dc8675a3926302af3a02b5c9ac30ef5f2bb50e46d24a74cf605a1323657f071f` fingerprint in the generated and normalized target files at expected locations.
- DSMZ Medium 450 is a derivative instruction to add 20 mg/L arginine to DSMZ Medium 382.
- DSMZ/MediaDive 382 define Medium 382 as Mineral Medium M9 for E. coli JM strains with 100 ml of `10 x M9 salts (per l)` in 1 L of final medium.

## Evidence

- MediaDive 450 expands DSMZ 450 into a 1 L recipe containing 100 ml 10x M9 salts, 1 ml 1 M MgSO4, 1 ml 0.1 M CaCl2, 1 ml filter-sterilized 1 M Thiamine-HCl x 2 H2O, 10 ml 20% glucose, 20 mg proline, 20 mg/L arginine, and 900 ml water.
- DSMZ/MediaDive 382 define the 10x M9 salts stock as 60 g Na2HPO4, 30 g KH2PO4, 10 g NH4Cl, and 5 g NaCl per liter.
- DSMZ 450 itself only says to add 20 mg/L arginine to Medium 382; the current DSMZ 450 PDF does not mention proline.
- The DSMZ/MediaDive preparation text says to sterilize the solutions separately by filtration for thiamine and glucose or by autoclaving, then adjust pH to 7.4.

## Completeness

- The generated record preserves the KOMODO and DSMZ identities, pH 7.4, defined/liquid classification, and the ingredient set from the normalized DSMZ expansion.
- The generated record does not preserve the 10x M9 salts stock recipe or the 100 ml stock addition.
- The generated record drops the DSMZ preparation steps when the KOMODO duplicate becomes canonical.

## Findings

- The 10x M9 salts stock is flattened at stock strength. The generated `Na2HPO4`, `KH2PO4`, `NH4Cl`, and `NaCl` concentrations are the 10x stock values even though only 100 ml of that stock is added per liter.
- The source-duplicate merge chose the KOMODO record as canonical and did not carry over the DSMZ preparation steps for separate sterilization and pH adjustment.
- The current DSMZ 450 PDF supports adding arginine to DSMZ 382 but does not support the generated proline row; curators should confirm whether MediaDive 450 is preserving older DSMZ 450 content or whether proline was introduced spuriously.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/supplemented_arginine_m9_medium.yaml` or the MediaDive import path so `10 x M9 salts (per l)` remains a stock solution added at 100 ml/L rather than four final ingredients at 10x concentration.
- Ensure source-duplicate merging retains preparation steps from the authoritative DSMZ parent when merging with the KOMODO mirror.
- Verify the proline addition against DSMZ history or another primary source; remove it if it is not actually part of DSMZ Medium 450.
- Regenerate `data/merge_yaml/merged/supplemented_arginine_m9_medium.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized DSMZ 450 and KOMODO 450 sources after stock-solution and preparation-retention fixes.
- Regenerate merged YAML and verify the M9 salt rows are either nested under `10 x M9 salts` or diluted 10-fold in any final flat view.
- Confirm that the final generated record still preserves pH 7.4 after preparation steps are restored.

## Additional Notes

- Empty optional fields were not treated as defects.
- DSMZ 450, DSMZ 382, MediaDive 450, and MediaDive 382 were checked.
