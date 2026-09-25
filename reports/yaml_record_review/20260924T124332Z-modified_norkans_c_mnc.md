# YAML Record Review: modified_norkans_c_mnc

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_norkans_c_mnc.yaml
- Started UTC: 2026-09-24T12:43:32Z
- Finished UTC: 2026-09-24T12:44:13Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:008440`, `modified_norkans_c_mnc`, generated from `data/normalized_yaml/bacterial/modified_norkans_c_mnc.yaml`.
- The record represents TOGO `M1865`, sourced from NBRC `NBRC_M1109`, named `Modified Norkans' C (MNC)`.
- The generated TOGO record was compared with TOGO `M1865` and the primary NBRC `NO=1109` page.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` exited 0 with no failure diagnostics.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M1865` points to NBRC `NBRC_M1109`, and NBRC `NO=1109` identifies Modified Norkans' C (MNC).
- A gitignore-independent exact search for the TOGO and NBRC identifiers found only one maintained YAML record, `data/normalized_yaml/bacterial/modified_norkans_c_mnc.yaml`, plus this generated record and index metadata.
- `NH4-tartrate`, `Yeast extract`, and `Casein hydrolysate` have no primary ontology grounding.
- No inspected source payload identified a target organism for this medium.

## Evidence

- NBRC lists 1 g KH2PO4, 0.5 g MgSO4, 0.5 ml ZnSO4 0.2 percent solution, 0.5 g NH4-tartrate, 0.5 ml Fe-citrate 1.0 percent solution, 50 ug Thiamine-HCl, 0.23 g Casein hydrolysate, 0.5 g Yeast extract, 10 g Glucose, 15 g Agar, and 1 L distilled water.
- TOGO preserves the same NBRC component names, including the two 0.5 ml solution additions and the 50 ug thiamine quantity.
- The NBRC and TOGO source payloads do not define the internal formulas for the Fe-citrate or ZnSO4 percentage solutions.

## Completeness

- The gram-scale salts, undefined nutrients, glucose, and agar are present at the source numeric values.
- The two 0.5 ml percentage-solution additions were migrated to empty `solutions` stubs with `G_PER_L` units.
- The 50 ug Thiamine-HCl row was imported as `50` `G_PER_L`.
- The 1 L distilled water row was imported as `1` `G_PER_L`.

## Findings

- Blocker: the 50 ug Thiamine-HCl source row is represented as `50` `G_PER_L`, which is a severe unit error for a microgram vitamin addition.
- Blocker: the 0.5 ml Fe-citrate 1.0 percent solution and 0.5 ml ZnSO4 0.2 percent solution additions are represented as empty solution stubs with `0.5` `G_PER_L`, losing the milliliter unit while failing to preserve any usable solution composition.
- Major: the 1 L distilled water row is represented as `1` `G_PER_L`, conflating a final volume with a mass concentration.
- Minor: NH4-tartrate, Yeast extract, and Casein hydrolysate lack primary term grounding.

## Recommended Edits

- Correct Thiamine-HCl to 50 ug/L, or convert it to the equivalent 0.05 mg/L final concentration.
- Preserve Fe-citrate 1.0 percent solution and ZnSO4 0.2 percent solution as 0.5 ml additions with no fabricated gram-per-liter concentration.
- Preserve the 1 L distilled water row as a volume or final-volume statement rather than `G_PER_L`.
- Add primary ontology grounding for NH4-tartrate and the undefined proteinaceous nutrients where suitable terms exist.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting TOGO solution and microgram unit migration.
- Recompare the regenerated record against NBRC `NBRC_M1109`, especially the two 0.5 ml solution additions, the 50 ug Thiamine-HCl row, and the 1 L distilled water row.
- Confirm with a gitignore-independent exact identifier search that NBRC `NBRC_M1109` remains represented by only one generated record.

## Additional Notes

None found.
