# YAML Record Review: modified_gam_broth_glucose

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_gam_broth_glucose.yaml
- Started UTC: 2026-09-24T11:00:01Z
- Finished UTC: 2026-09-24T11:01:02Z
- Verdict: needs curation

## Target

Generated record `CultureMech:008759` for TOGO medium `M2165`, `Modified GAM broth + glucose`, which imports NBRC medium 1545.

The generated record merges `modified_gam_broth_glucose` from `data/normalized_yaml/bacterial/modified_gam_broth_glucose.yaml`. The generated YAML was compared with that maintained owner and NBRC 1545.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO `M2165` and NBRC 1545 identity.

`Nissui Modified GAM Broth*` is a direct 41.7 g commercial powdered-medium component in NBRC 1545, but the import migrated it to an empty `solutions` entry. That leaves the main ingredient list with only glucose plus a mis-united water row.

## Evidence

NBRC 1545 lists 41.7 g Nissui Modified GAM Broth, 9.5 g glucose, and 1 L distilled water, followed by `pH unadjusted`.

The generated YAML stores glucose correctly as 9.5 g/L, but it stores 1 L water as `1` `G_PER_L`, moves 41.7 g/L Nissui Modified GAM Broth into an empty solution stub, and drops the pH-unadjusted note.

TOGO `M2165` returned an empty API body during this review; NBRC 1545 was reachable and matched the TOGO source pointers stored in the YAML.

## Completeness

The generated record preserves the TOGO/NBRC identity and glucose row.

It is incomplete for the commercial GAM broth row, solvent unit, and pH-unadjusted note.

## Findings

- High: The source 41.7 g/L Nissui Modified GAM Broth row is represented as an empty `Unknown solution` instead of a direct commercial ingredient.
- High: The 1 L distilled-water solvent row is represented as 1 g/L.
- Medium: The pH-unadjusted note is absent.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_gam_broth_glucose.yaml` so Nissui Modified GAM Broth stays as a 41.7 g/L complex ingredient.
- Store distilled water as 1 L or 1000 ml/L.
- Preserve the NBRC `pH unadjusted` note.
- Regenerate `data/merge_yaml/merged/modified_gam_broth_glucose.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against NBRC 1545 to verify the Nissui Modified GAM Broth, glucose, distilled-water, and pH rows.

## Additional Notes

None found.
