# YAML Record Review: modified_schaedler_medium_infect_immun_29_768_777_1980_without_glucose_but_supplemented_with_0_1_m_sodium_lactate

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_schaedler_medium_infect_immun_29_768_777_1980_without_glucose_but_supplemented_with_0_1_m_sodium_lactate.yaml
- Started UTC: 2026-09-24T13:02:50Z
- Finished UTC: 2026-09-24T13:04:00Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:009251`, `modified_schaedler_medium_infect_immun_29_768_777_1980_without_glucose_but_supplemented_with_0_1_m_sodium_lactate`, generated from `data/normalized_yaml/bacterial/modified_schaedler_medium_infect_immun_29_768_777_1980_without_glucose_but_supplemented_with_0_1_m_sodium_lactate.yaml`.
- The record represents TOGO `M2699`, named `Modified Schaedler medium (Infect. Immun. 29:768-777,1980) without glucose but supplemented with 0.1 M sodium lactate`.
- The generated TOGO record was compared with TOGO `M2699` and the referenced DSMZ Medium 1669 PDF.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M2699` identifies a modified Schaedler medium that omits glucose from DSMZ Medium 1669 and adds 0.1 M sodium lactate.
- A gitignore-independent exact search for the TOGO identifier and DSMZ PDF found one maintained YAML record for this lactate variant, plus a separate `schaedler_broth_roth_5772` record for the DSMZ base medium.
- `Tris (hydroxymethyl aminomethane) 3.00 g`, the undefined peptone rows, and the two gas rows are not cleanly grounded.
- No inspected source payload identified a target organism for this medium.

## Evidence

- DSMZ Medium 1669 lists Casein peptone, Soy peptone, Yeast extract, Peptone mixture, Glucose, K2HPO4, NaCl, Tris (hydroxymethyl aminomethane), 1 mg Resazurin, 0.01 g Hemin, 0.40 g Cysteine-HCl x H2O, and 1000 ml distilled water.
- TOGO `M2699` represents the named variant without the DSMZ glucose row and with 0.1 M Sodium lactate.
- DSMZ instructs boiling under CO2 until the resazurin indicator changes from pink to colorless, cooling under CO2, adjusting pH to 7.6, switching to N2, filling Hungate tubes under N2, and autoclaving.

## Completeness

- The non-glucose DSMZ ingredients and 0.1 M Sodium lactate are present.
- The 1 mg Resazurin source row is present as `1` `G_PER_L`.
- The 1000 ml Distilled water row is present as `1000` `G_PER_L`.
- The pH 7.6 target and the CO2/N2 Hungate-tube preparation procedure are absent.
- The Tris row retains its amount in the preferred term string.

## Findings

- Blocker: 1 mg Resazurin is represented as `1` `G_PER_L`, turning a milligram indicator row into a gram-per-liter final concentration.
- Major: 1000 ml Distilled water is represented as `1000` `G_PER_L`, conflating the source final volume with a mass concentration.
- Major: generated YAML drops the CO2/N2 preparation comments, including the resazurin color endpoint, pH 7.6 adjustment, switch from CO2 to N2, and Hungate-tube filling under N2.
- Minor: `Tris (hydroxymethyl aminomethane) 3.00 g` should be split into a clean preferred term and a 3.00 g/L concentration.

## Recommended Edits

- Correct Resazurin to 1 mg/L.
- Preserve the 1000 ml distilled water row as a volume or final-volume statement rather than `G_PER_L`.
- Preserve the DSMZ anaerobic preparation instructions and pH 7.6 target from the TOGO comments.
- Normalize the Tris preferred term and keep its amount only in the concentration field.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting TOGO unit and preparation-comment handling.
- Recompare the regenerated record against TOGO `M2699` and DSMZ Medium 1669, with attention to the glucose omission and sodium lactate addition.
- Confirm with a gitignore-independent exact identifier search that TOGO `M2699` remains distinct from the DSMZ base Schaedler broth record.

## Additional Notes

None found.
