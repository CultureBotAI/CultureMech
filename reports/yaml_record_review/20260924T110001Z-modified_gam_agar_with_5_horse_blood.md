# YAML Record Review: modified_gam_agar_with_5_horse_blood

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_gam_agar_with_5_horse_blood.yaml
- Started UTC: 2026-09-24T10:59:00Z
- Finished UTC: 2026-09-24T11:00:01Z
- Verdict: needs curation

## Target

Generated record `CultureMech:009536` for TOGO medium `M3025`, `Modified GAM Agar With 5% Horse Blood`, which imports JCM medium 1370.

The generated record merges `modified_gam_agar_with_5_horse_blood` from `data/normalized_yaml/bacterial/modified_gam_agar_with_5_horse_blood.yaml`. The generated YAML was compared with that maintained owner, TOGO `M3025`, and JCM 1370.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO `M3025` and JCM 1370 identity and preserves the 56.7 g/L Nissui modified GAM agar row.

The generated artifact is stale relative to a 2026-09-12 `RESOLVED_TOGO_M3025_SCORE15` repair in `data/normalized_yaml/bacterial/modified_gam_agar_with_5_horse_blood.yaml`. The maintained owner now restores the 1 L water unit, 5% final defibrinated horse blood, MICRO grounding for blood, source references, and JCM preparation sequence.

## Evidence

TOGO `M3025` imports JCM 1370 with 1 L distilled water, 56.7 g GAM agar, modified (Nissui), and defibrinated horse blood. JCM 1370 says to prepare JCM Medium 655, sterilize and cool it to about 45 C, aseptically add 5% final sterile defibrinated horse blood, mix, and quickly dispense into sterile tubes or petri dishes.

The generated YAML stores distilled water as `1` `G_PER_L`, keeps defibrinated horse blood as a variable placeholder, and has no preparation steps. The maintained owner already corrects water to `1.0` `L`, represents defibrinated horse blood as `5.0` `PERCENT_V_V`, and adds the four-step mix, autoclave, cool, and aseptic blood-addition workflow.

## Completeness

The generated record is complete for the TOGO/JCM identity and Nissui commercial base ingredient.

It is incomplete for the water unit, 5% blood amount, blood grounding, preparation sequence, source references, and explicit curation flags.

## Findings

- High: The generated YAML is stale relative to the 2026-09-12 source-backed repair in `modified_gam_agar_with_5_horse_blood.yaml`.
- High: The source 1 L distilled-water row is represented as 1 g/L.
- High: The 5% final sterile defibrinated-horse-blood addition is represented as a variable placeholder.
- Medium: The JCM 1370 cool-and-aseptically-add-blood workflow is absent.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_gam_agar_with_5_horse_blood.yaml` from the repaired 2026-09-12 maintained owner.
- Confirm that the regenerated artifact keeps 56.7 g/L GAM agar, modified (Nissui), 1 L distilled water, 5% final sterile defibrinated horse blood, and the JCM preparation workflow.
- Preserve the repaired MICRO grounding, source references, curation flags, and intentional-unmapped treatment for GAM agar, modified (Nissui).

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Recompare the regenerated record against TOGO `M3025` and JCM 1370 to verify the Nissui modified GAM agar row, water row, horse-blood final concentration, and 45 C cooling instruction.

## Additional Notes

None found.
