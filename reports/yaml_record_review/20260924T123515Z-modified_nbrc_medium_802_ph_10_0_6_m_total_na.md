# YAML Record Review: modified_nbrc_medium_802_ph_10_0_6_m_total_na

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_nbrc_medium_802_ph_10_0_6_m_total_na.yaml
- Started UTC: 2026-09-24T12:35:15Z
- Finished UTC: 2026-09-24T12:35:15Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:008430`, `modified_nbrc_medium_802_ph_10_0_6_m_total_na`, generated from `data/normalized_yaml/bacterial/modified_nbrc_medium_802_ph_10_0_6_m_total_na.yaml`.
- The record represents TOGO `M1856`, which points back to NBRC `NBRC_M1099` / NBRC medium detail `NO=1099`.
- The generated record and maintained normalized record have the same curation-significant content for the inspected fields.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M1856` and NBRC `NO=1099` both identify `Modified NBRC medium 802 (pH 10, 0.6 M total Na+)`.
- An exact gitignore-independent search for the normalized name, TOGO ID, NBRC ID, and NBRC URL parameter found only the maintained `data/normalized_yaml/bacterial/modified_nbrc_medium_802_ph_10_0_6_m_total_na.yaml` record, the generated `data/merge_yaml/merged/modified_nbrc_medium_802_ph_10_0_6_m_total_na.yaml` record, and index entries for `TOGO:M1856`; no second YAML recipe for this exact NBRC source was found.
- No inspected TOGO or NBRC payload identified a target organism for this medium.

## Evidence

- NBRC `NO=1099` lists a 900 ml basal medium with 10 g Hipolypepton, 2 g yeast extract, 1 g MgSO4 x 7 H2O, 1 g K2HPO4, 900 ml distilled water, and 15 g agar if needed.
- NBRC then instructs adding 100 ml sodium carbonate buffer after autoclaving; that buffer is for pH 10 and 0.6 M total Na+ and contains 22% Na2CO3, 8% NaHCO3, 6% NaCl, and 0.5% K2HPO4.
- TOGO `M1856` preserves the same split into a `main solution 1` with the 900 ml base and a `main solution 2` with 100 ml water plus the four carbonate-buffer percentage components.
- The generated record merges 900 ml and 100 ml water into `1000.0` `G_PER_L`, migrates Hipolypepton into an empty `solutions` stub, keeps K2HPO4 only as the 1 g/L basal ingredient, and emits the buffer-specific NaCl, NaHCO3, and Na2CO3 rows as variable top-level ingredients.

## Completeness

- Basal MgSO4 x 7 H2O, yeast extract, K2HPO4, optional agar, and both water contexts are recognizable by name or amount.
- Hipolypepton is misplaced under `solutions` with an empty composition instead of remaining a 10 g ingredient.
- The sodium carbonate buffer is not preserved as a 100 ml post-autoclave addition with 22% Na2CO3, 8% NaHCO3, 6% NaCl, and 0.5% K2HPO4.
- `physical_state` is `SOLID_AGAR`, but agar is optional in the NBRC source.

## Findings

- Blocker: the 100 ml sodium carbonate buffer is flattened and its percentages are not retained. NBRC specifies 22% Na2CO3, 8% NaHCO3, 6% NaCl, and 0.5% K2HPO4 in a post-autoclave buffer; the generated record drops the percentage values and represents most of those components as variable top-level ingredients.
- Major: the generated K2HPO4 row conflates only the 1 g basal addition while losing the separate 0.5% K2HPO4 buffer context.
- Major: `Hipolypepton*` is incorrectly migrated to an empty solution stub, even though NBRC lists it as a 10 g basal ingredient and the asterisk only points to the vendor note, `Wako Pure Chemical Ind., Ltd., Osaka, Japan`.
- Major: 900 ml basal water and 100 ml buffer water are merged into one `1000.0` `G_PER_L` row, losing both the source unit and the two recipe contexts.
- Major: `physical_state: SOLID_AGAR` overstates an optional ingredient; the source says `Agar (if needed)` rather than requiring a solid medium.

## Recommended Edits

- Model the sodium carbonate buffer as a distinct 100 ml post-autoclave solution with 22% Na2CO3, 8% NaHCO3, 6% NaCl, and 0.5% K2HPO4.
- Keep Hipolypepton as a 10 g basal ingredient and move the asterisk text into a note or source annotation rather than interpreting it as a solution marker.
- Preserve the 900 ml basal water and 100 ml buffer water contexts separately.
- Represent optional agar without forcing the whole recipe to `SOLID_AGAR`.
- Replace the variable top-level NaCl, NaHCO3, and Na2CO3 defaults with values scoped to the carbonate buffer.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting TOGO solution migration for the carbonate-buffer paragraph.
- Recompare the regenerated record against NBRC `NO=1099`, including the Hipolypepton vendor note and the full carbonate-buffer statement.
- Confirm that the generated record no longer has `Hipolypepton*` as an empty solution.

## Additional Notes

None found.
