# YAML Record Review: oatmeal_nitrate_agar__1bd3b90f

- Repository: CultureMech
- Record: data/merge_yaml/merged/oatmeal_nitrate_agar__1bd3b90f.yaml
- Started UTC: 2026-09-24T19:09:50Z
- Finished UTC: 2026-09-24T19:10:26Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oatmeal_nitrate_agar__1bd3b90f.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:002879` and source term `mediadive.medium:J52`.

This is a single-source generated record from `data/normalized_yaml/bacterial/oatmeal_nitrate_agar.yaml`, the direct MediaDive/JCM import for JCM Medium 52.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oatmeal_nitrate_agar__1bd3b90f.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The source identity is valid for JCM Medium 52, `OATMEAL-NITRATE AGAR`. The official JCM page lists 3.0 g Oatmeal, powdered, Quaker White Oats; 0.2 g KNO3; 0.5 g K2HPO4; 0.2 g MgSO4 x 7H2O; 15.0 g Agar; 1.0 L Distilled water; and a final pH adjustment to 7.0.

The duplicate graph is incomplete. TOGO Medium M44 is a TOGO representation of the same JCM_M52 source, and `data/merge_yaml/merged/oatmeal_nitrate_agar.yaml` already emits it as a separate canonical generated record. The direct JCM 52 import should be folded into that source group instead of remaining a parallel generated recipe.

## Evidence

Checked the generated direct JCM record, its normalized owner, the generated TOGO M44 sibling, the normalized TOGO M44 owner, an ignored-inclusive exact repository search for the TOGO/JCM ids and `oatmeal_nitrate_agar` slug, the TOGO M44 REST payload, and the JCM GRMD 52 page.

The source evidence confirms that the five non-water ingredient amounts in this direct JCM record match the official formulation and that `ph_value: 7.0`, `physical_state: SOLID_AGAR`, and the pH adjustment step are appropriate.

## Completeness

The direct JCM generated record is close to the official recipe but is not complete:

- It omits the 1.0 L Distilled water row.
- It degrades the source's `Oatmeal, powdered (Quaker White Oats)` label to `Oatmeal` with the note ` ( powdered)`, dropping the Quaker White Oats specificity that TOGO M44 preserves.
- KNO3 still uses legacy `mediaingredientmech_term`.

## Findings

- MAJOR: The generated direct JCM 52 record omits the 1 L distilled-water component listed by JCM.
- MAJOR: JCM 52 and TOGO M44 are the same source recipe but generate as separate canonical YAML files, so downstream users see duplicate Oatmeal-Nitrate Agar records with different ingredient completeness.
- MINOR: KNO3 still has a legacy `mediaingredientmech_term` despite the June 2026 migration history.
- MINOR: The MediaDive import lost part of the oatmeal label by reducing `Oatmeal, powdered (Quaker White Oats)` to `Oatmeal`.

## Recommended Edits

- Link `mediadive.medium:J52` to `TOGO:M44` as a source duplicate, or otherwise merge the direct JCM 52 import with the TOGO M44 owner before generated YAML is emitted.
- Backfill the JCM 52 normalized record with 1000 ML_PER_L distilled water if that record remains present as a maintained normalized source.
- Preserve the full oatmeal source label or add a source note that retains the Quaker White Oats attribute.
- Finish CHEBI mirror cleanup for KNO3.
- Regenerate merged YAML and confirm only one canonical Oatmeal-Nitrate Agar record is emitted for JCM 52 / TOGO M44.

## Follow-up Checks

- Run an ignored-inclusive exact search for `mediadive.medium:J52`, `TOGO:M44`, `JCM_M52`, and `GRMD=52` after repair to confirm the direct JCM and TOGO paths land in one generated source-duplicate cluster.
- Re-run open-schema, strict, reference, and term validation after the normalized owner is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
