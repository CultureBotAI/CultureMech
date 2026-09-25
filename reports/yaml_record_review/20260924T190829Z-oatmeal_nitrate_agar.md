# YAML Record Review: oatmeal_nitrate_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/oatmeal_nitrate_agar.yaml
- Started UTC: 2026-09-24T19:08:29Z
- Finished UTC: 2026-09-24T19:09:49Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oatmeal_nitrate_agar.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:009836` and source term `TOGO:M44`.

This is a single-source generated record from `data/normalized_yaml/bacterial/TOGO_M44_Oatmeal-Nitrate_Agar.yaml`.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oatmeal_nitrate_agar.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target is correctly grounded to TOGO Medium M44, which snapshots JCM Medium 52. The fetched TOGO M44 payload and official JCM 52 page agree on the Oatmeal-Nitrate Agar formulation:

- 3 g Oatmeal, powdered, Quaker White Oats
- 0.2 g KNO3
- 0.5 g K2HPO4
- 0.2 g MgSO4 x 7H2O
- 15 g Agar
- 1 L Distilled water
- final pH 7.0

The generated identity is still split from its direct JCM sibling. `data/merge_yaml/merged/oatmeal_nitrate_agar__1bd3b90f.yaml` is the same JCM 52 source imported via MediaDive as `mediadive.medium:J52`, but the two source records are emitted as independent generated records instead of being related as `SOURCE_DUPLICATE`.

## Evidence

Checked the generated TOGO record, the normalized TOGO owner, the direct normalized JCM 52 record, the generated direct JCM 52 sibling, an ignored-inclusive exact repository search for the TOGO/JCM ids and `oatmeal_nitrate_agar` slug, the TOGO M44 REST payload, and the JCM GRMD 52 page.

The source rows confirm that the generated non-water mass concentrations are source-faithful and that the record's `physical_state: SOLID_AGAR` is correct.

## Completeness

The generated record carries the full six-component recipe from TOGO M44, but three fields need curation:

- The source lists 1 L distilled water, while the YAML records water as `1 G_PER_L`.
- The TOGO source metadata and JCM page both give pH 7.0, but the generated TOGO record has no `ph_value`.
- KNO3 still uses legacy `mediaingredientmech_term`, and MgSO4 x 7H2O has a primary CHEBI term but no matching `mediaingredientmech_chebi_term`.

Preparation is also thin: the source says to adjust pH to 7.0, but the TOGO import did not generate an `ADJUST_PH` preparation step.

## Findings

- MAJOR: Distilled water is encoded as `value: 1`, `unit: G_PER_L`, although TOGO M44 and JCM 52 list 1 L distilled water. This should be normalized as 1000 ML_PER_L or the repository's equivalent final-liter water representation.
- MAJOR: TOGO M44 and direct JCM 52 are source duplicates but remain separate generated records, so this medium appears twice with different ingredient surfaces and only the direct JCM copy has `ph_value: 7.0`.
- MAJOR: The generated TOGO record omits `ph_value: 7.0` and lacks the source's final pH adjustment step.
- MINOR: KNO3 still has a legacy `mediaingredientmech_term` despite the June 2026 migration history, and MgSO4 x 7H2O lacks the `mediaingredientmech_chebi_term` mirror for CHEBI:31795.

## Recommended Edits

- Correct the normalized TOGO M44 water ingredient to a liter-of-final-medium representation rather than `1 G_PER_L`.
- Add `ph_value: 7.0` and an `ADJUST_PH` preparation step to the normalized TOGO M44 record.
- Link direct JCM 52 / `mediadive.medium:J52` to TOGO M44 / `TOGO:M44` as a source duplicate, or otherwise merge the two normalized records before generating `data/merge_yaml/merged`.
- Finish CHEBI mirror cleanup for KNO3 and MgSO4 x 7H2O.
- Regenerate merged YAML and confirm Oatmeal-Nitrate Agar emits once with one source-duplicate cluster.

## Follow-up Checks

- Run an ignored-inclusive exact search for `TOGO:M44`, `mediadive.medium:J52`, `JCM_M52`, and `GRMD=52` to confirm only one generated canonical record owns this formulation after regeneration.
- Re-run open-schema, strict, reference, and term validation after the normalized owner is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
