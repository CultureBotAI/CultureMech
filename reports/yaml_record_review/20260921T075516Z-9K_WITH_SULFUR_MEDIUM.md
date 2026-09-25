# YAML Record Review: 9k_with_sulfur_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
- Started UTC: 2026-09-21T07:54:34Z
- Finished UTC: 2026-09-21T07:55:16Z
- Verdict: pass

## Target

- Reviewed generated record `data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml`.
- Stable identifier: `CultureMech:002485`.
- Source identity asserted by the record: JCM / MediaDive `J1321`, `9K WITH SULFUR MEDIUM`.
- The generated record was merged from one owner, `9k_with_sulfur_medium.yaml`, on fingerprint `9284e6c5a5781e63f68dd6172d9ba6ebfd4dfe083a05410c4e82906bffc67c68`.
- Current authoritative owner: `data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The direct JCM / MediaDive identity is coherent: `mediadive.medium:J1321`, original name `9K WITH SULFUR MEDIUM`, and the linked JCM `GRMD=1321` page all identify JCM medium 1321.
- JCM's current `GRMD=1321` page returns the same ingredient table represented in DSMZ/BacMedia's `text/j1321` rendering.
- A gitignore-independent exact search with a digit boundary for `mediadive.medium:J1321` found only one active normalized owner and its generated merge.
- A gitignore-independent exact search with a digit boundary for the `GRMD=1321` URL found only the same owner and generated merge.

## Evidence

- JCM medium 1321 lists 0.5 g `K2HPO4`, 3 g `(NH4)2SO4`, 0.1 g KCl, 0.5 g `MgSO4 x 7 H2O`, 10 mg `Ca(NO3)2`, 5 g sulfur powder, and 1 L distilled water.
- JCM instructs to mix the components except sulfur, adjust pH to 2.5 with `H2SO4`, autoclave, and separately sterilize sulfur by steaming for 3 hr on each of 3 successive days.
- The generated target represents the source solutes and sulfur at the correct per-litre concentrations and preserves the pH and sulfur-sterilization instruction.

## Completeness

- The generated target omits the explicit distilled-water source row, matching the usual direct MediaDive/JCM solvent omission pattern.
- The generated target has ChEBI grounding for every retained ingredient.
- The JCM URL is present in `notes`, but there is no structured `references` entry.

## Findings

- MINOR: distilled water is omitted as an explicit ingredient row.
- MINOR: source provenance is note-only; the linked JCM URL should be promoted to a structured reference or source slot.

## Recommended Edits

- Add a structured source or reference for the JCM medium 1321 page.
- If direct JCM imports standardize solvent rows in the future, add distilled water 1 L to this recipe at the same time.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after any provenance edit.
- Re-run exact source searches for `mediadive.medium:J1321` and `GRMD=1321` with digit boundaries; JCM medium 1321 should remain uniquely represented.
- Confirm that the record still carries 10 mg/L calcium nitrate, 5 g/L sulfur powder, pH 2.5, and the separate sulfur steaming instruction.

## Additional Notes

- The adjacent plain 9K records have duplicate-source and sulfuric-acid stock issues that are not present in this JCM 1321 sulfur variant.
