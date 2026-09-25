# YAML Record Review: modified_gam_agar_horse_blood_acetate

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_gam_agar_horse_blood_acetate.yaml
- Started UTC: 2026-09-24T10:57:58Z
- Finished UTC: 2026-09-24T10:59:00Z
- Verdict: needs curation

## Target

Generated record `CultureMech:008756` for TOGO medium `M2162`, `Modified GAM agar + horse blood & acetate`, which imports NBRC medium 1535.

The generated record merges `modified_gam_agar_horse_blood_acetate` from `data/normalized_yaml/bacterial/modified_gam_agar_horse_blood_acetate.yaml`. The generated YAML was compared with that maintained owner, TOGO `M2162`, and NBRC 1535.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO `M2162` and NBRC 1535 identity.

`Nissui Modified GAM Broth*` is a commercial powdered medium component in NBRC 1535, but the import migrated it to an empty `solutions` entry. That makes the main ingredient list omit the 41.7 g/L GAM broth row even though the source treats it as a direct component.

## Evidence

NBRC 1535 and TOGO `M2162` list 41.7 g Nissui Modified GAM Broth, 2.7 g sodium acetate, 50 ml defibrinated horse blood, 15 g agar, and 1 L distilled water. NBRC additionally states `pH unadjusted`; TOGO preserves the footnote that the Nissui product is from Tokyo, Japan and that horse blood is added after autoclaving.

The generated YAML stores 1 L water as `1` `G_PER_L`, stores 50 ml defibrinated horse blood as `50` `G_PER_L`, moves 41.7 g/L Nissui Modified GAM Broth into an empty solution stub, and omits the `pH unadjusted` and post-autoclave horse-blood instruction.

## Completeness

The generated record preserves the TOGO/NBRC identity plus the sodium acetate and agar rows.

It is incomplete for the commercial GAM broth row, water and blood units, source pH note, and post-autoclave preparation detail.

## Findings

- High: The source 41.7 g/L Nissui Modified GAM Broth row is represented as an empty `Unknown solution` instead of a direct commercial ingredient.
- High: The 1 L distilled-water solvent row is represented as 1 g/L.
- High: The 50 ml defibrinated-horse-blood addition is represented as 50 g/L.
- Medium: The pH-unadjusted note and post-autoclave horse-blood addition are absent.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_gam_agar_horse_blood_acetate.yaml` so Nissui Modified GAM Broth stays as a 41.7 g/L complex ingredient.
- Store distilled water as 1 L or 1000 ml/L and defibrinated horse blood as a 50 ml/L post-autoclave addition.
- Add structured preparation or notes for `pH unadjusted` and `After autoclaving, add horse blood`.
- Regenerate `data/merge_yaml/merged/modified_gam_agar_horse_blood_acetate.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against NBRC 1535 and TOGO `M2162` to verify the GAM broth, sodium acetate, agar, water, horse blood, pH, and post-autoclave addition instruction.

## Additional Notes

None found.
