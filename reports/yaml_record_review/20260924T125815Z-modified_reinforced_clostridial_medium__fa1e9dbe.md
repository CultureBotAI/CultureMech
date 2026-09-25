# YAML Record Review: modified_reinforced_clostridial_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_reinforced_clostridial_medium__fa1e9dbe.yaml
- Started UTC: 2026-09-24T12:58:15Z
- Finished UTC: 2026-09-24T12:59:02Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:007841`, `modified_reinforced_clostridial_medium`, generated from `data/normalized_yaml/bacterial/TOGO_M1306_Modified_Reinforced_Clostridial_Medium.yaml`.
- The record represents TOGO `M1306`, sourced from JCM `JCM_M1217-2`, named `Modified Reinforced Clostridial Medium`.
- The generated TOGO record was compared with TOGO `M1306` and the primary JCM `GRMD=1217` page that describes the reinforced clostridial base and its solid-medium variant.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M1306` points to JCM `JCM_M1217-2`, the solid agar version of Modified Reinforced Clostridial Medium.
- A gitignore-independent exact search for `TOGO:M1306`, `JCM_M1217-2`, and `GRMD=1217` found this branch plus related JCM 1217 variants, including a TOGO `M1305` branch and a MediaDive branch for the non-solid version.
- `Yeast extract`, `Tryptone`, `Beef extract`, and `agar` are ungrounded.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists 3.0 g Yeast extract, 10.0 g Tryptone, 10.0 g Beef extract, 5.0 g Glucose, 0.5 g L-Cysteine HCl x H2O, 3.0 g NaCl, 3.0 g Sodium acetate, 1.0 g Soluble starch, and 1 L distilled water.
- JCM instructs mixing components, adjusting pH to 6.0-6.5, adding 20.0 g agar per liter for solid medium, bringing the medium to a boil to dissolve agar, cooling it, distributing it into culture vessels under N2, sealing with butyl rubber stoppers, and autoclaving.
- TOGO `M1306` preserves the agar row and the JCM preparation comment.

## Completeness

- The eight basal non-water ingredients and 20 g/L agar are present.
- The 1 L Distilled water row is present as `1` `G_PER_L`.
- The pH 6.0-6.5 range and the detailed boil, distribute-under-N2, seal, and autoclave instructions are absent.
- N2 is present as a variable ingredient, but its role as the tube distribution gas is absent.

## Findings

- Major: 1 L Distilled water is represented as `1` `G_PER_L`, conflating source final volume with a mass concentration.
- Major: the generated record drops the only source preparation comment, losing the pH 6.0-6.5 adjustment, the instruction to boil and dissolve agar, and the under-N2 distribution and sealing procedure.
- Minor: the generated `N2` row records the gas name but not how N2 is used.
- Minor: the undefined nutrients and agar row are ungrounded.

## Recommended Edits

- Preserve the final 1 L water row as a volume statement rather than `G_PER_L`.
- Preserve the JCM preparation text or split it into structured preparation steps.
- Keep N2 attached to the anaerobic distribution instruction rather than only as a variable ingredient.
- Add suitable ontology or product grounding for Yeast extract, Tryptone, Beef extract, and agar where stable terms exist.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting water and preparation-comment handling.
- Recompare the regenerated record against TOGO `M1306` and JCM `GRMD=1217`, especially the pH range, 20 g/L agar row, and under-N2 Balch-tube preparation procedure.
- Confirm with a gitignore-independent exact identifier search that TOGO `M1306` remains represented by its intended solid-medium variant rather than a duplicate of the related liquid JCM 1217 branch.

## Additional Notes

None found.
