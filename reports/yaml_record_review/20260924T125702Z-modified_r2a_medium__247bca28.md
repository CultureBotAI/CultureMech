# YAML Record Review: modified_r2a_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_r2a_medium__247bca28.yaml
- Started UTC: 2026-09-24T12:57:02Z
- Finished UTC: 2026-09-24T12:57:38Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:010207`, `modified_r2a_medium`, generated from `data/normalized_yaml/bacterial/TOGO_M797_Modified_R2A_Medium.yaml`.
- The record represents TOGO `M797`, sourced from JCM `JCM_M769-2`, named `Modified R2A Medium`.
- The generated TOGO record was compared with TOGO `M797` and the primary JCM `GRMD=769` page that describes the R2A base and its washed-agar solid variant.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M797` points to JCM `JCM_M769-2`, the solid washed-agar version of Modified R2A Medium.
- A gitignore-independent exact search for `TOGO:M797` and `JCM_M769-2` found one maintained YAML record, `data/normalized_yaml/bacterial/TOGO_M797_Modified_R2A_Medium.yaml`, plus this generated record and index metadata.
- The three undefined BD-Difco ingredients and `washed agar` are ungrounded.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists 0.5 g Yeast extract, 0.5 g Proteose peptone No. 3, 0.5 g Casamino acids, 0.5 g Glucose, 0.5 g Sodium pyruvate, 3.0 g Trisodium citrate, 0.3 g K2HPO4, 20 g MgSO4 x 7 H2O, and 230 g NaCl.
- JCM instructs adding components to distilled water and bringing the volume to 1.0 L, then adjusting pH to 7.0-7.2.
- JCM notes that solid medium should be prepared by adding 18.0 g/L washed agar.
- TOGO `M797` preserves the solid-medium washed agar row and the two JCM preparation comments.

## Completeness

- The nine base ingredients and 18 g/L washed agar are present.
- The 1 L Distilled water row is present as `1` `G_PER_L`.
- The JCM pH 7.0-7.2 adjustment and the comments that contextualize washed agar as solid-medium preparation are absent.

## Findings

- Major: 1 L Distilled water is represented as `1` `G_PER_L`, conflating source final volume with a mass concentration.
- Major: the preparation comments from TOGO/JCM are absent, so the generated record loses the pH 7.0-7.2 adjustment and the statement that 18.0 g/L washed agar is specifically for solid medium.
- Minor: washed agar and the undefined BD-Difco nutrient products are ungrounded.

## Recommended Edits

- Preserve the final 1.0 L volume as a volume statement rather than a `G_PER_L` water concentration.
- Preserve the JCM preparation comments, including the pH adjustment and washed-agar context.
- Add suitable ontology or product grounding for the Yeast extract, Proteose peptone No. 3, Casamino acids, and washed agar rows where stable terms exist.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting water and preparation-comment handling.
- Recompare the regenerated record against TOGO `M797` and JCM `GRMD=769`, especially the pH 7.0-7.2 statement and the 18 g/L washed agar solid-medium variant.
- Confirm with a gitignore-independent exact identifier search that TOGO `M797` remains represented by only one generated record.

## Additional Notes

None found.
