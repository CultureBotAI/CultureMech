# YAML Record Review: pplo_glucose_broth

- Repository: CultureMech
- Record: data/merge_yaml/merged/pplo_glucose_broth.yaml
- Started UTC: 2026-09-24T21:48:01Z
- Finished UTC: 2026-09-24T21:48:01Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008098
- Name: pplo_glucose_broth
- Source import: TOGO M154 / JCM_M163
- Primary external ID: TOGO:M154
- Maintained input: data/normalized_yaml/bacterial/TOGO_M154_PPLO-Glucose_Broth.yaml

This generated record represents the TOGO import of PPLO-Glucose Broth from JCM Medium 163.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pplo_glucose_broth.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

TOGO M154 imports JCM_M163, PPLO-Glucose Broth. The current JCM URL for Medium 163 returns no recipe, but MediaDive J163 mirrors the retired JCM recipe: 21 g PPLO broth from BD-Difco, 5 g glucose, 5 ml of 0.4% phenol red, 200 ml sterile horse serum, 100 ml 25% fresh Baker's yeast extract from Gibco 360-8180, 1,000,000 U penicillin, 700 ml distilled water, and pH 7.6.

The generated record still reflects stale TOGO import artifacts: the 700 ml distilled water and 200 ml horse serum rows are 700 and 200 G_PER_L; the 5 ml 0.4% phenol red solution and the 100 ml 25% yeast extract solution are empty `Unknown solution` entries with 5 and 100 G_PER_L concentrations; and pH 7.6 is missing. Its maintained normalized input already has a later `RESOLVED_TOGO_M154_SCORE15` repair that changes the volume rows to ML_PER_L, adds pH 7.6, models the phenol red solution with a nested 0.4% phenol red component, and keeps penicillin as variable because the source amount is in activity units.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M154`, `JCM_M163`, `GRMD=163`, `TOGO_M154_PPLO-Glucose_Broth`, and `pplo_glucose_broth` found this repaired TOGO M154 input, this generated record, and a separate direct MediaDive/JCM J163 `pplo_glucose_broth__66449f8d` generated record.

## Evidence

- MediaDive J163 lists 21 g PPLO broth, 5 g glucose, 5 ml phenol red with a 0.4% attribute, 200 ml sterile horse serum, 100 ml fresh Baker's yeast extract with a 25% attribute, 1,000,000 U penicillin, and 700 ml distilled water.
- The maintained TOGO M154 input records that the current JCM 163 URL no longer exposes the recipe and preserves MediaDive J163 as the evidence source for the retired JCM values.
- The maintained TOGO M154 input already converted the water and serum rows to ML_PER_L and modelled phenol red and yeast extract as solution additions.

## Completeness

The generated record is incomplete and stale against the already-corrected normalized input. It lacks pH 7.6, leaves volume additions as G_PER_L rows or empty G_PER_L solutions, and does not propagate the phenol red stock composition, corrected yeast-extract solution, references, or repaired source notes.

## Findings

1. Major: Source volume rows are still represented as mass concentrations: 700 ml water as 700 G_PER_L, 200 ml serum as 200 G_PER_L, 5 ml 0.4% phenol red solution as a 5 G_PER_L empty solution, and 100 ml 25% yeast extract solution as a 100 G_PER_L empty solution.
2. Major: The source pH 7.6 is absent from the generated record.
3. Major: The generated record is stale relative to `data/normalized_yaml/bacterial/TOGO_M154_PPLO-Glucose_Broth.yaml`, which already corrected the volume imports and modelled the phenol red solution.
4. Major: The same former JCM 163 / MediaDive J163 recipe is emitted twice: once here through TOGO M154 and once as `data/merge_yaml/merged/pplo_glucose_broth__66449f8d.yaml`.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/pplo_glucose_broth.yaml` from the already-repaired TOGO M154 normalized input.
- Reconcile TOGO M154 with the direct MediaDive/JCM J163 import so the retired JCM 163 recipe is not emitted twice.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Run exact ignored-file searches for `TOGO:M154`, `JCM_M163`, `GRMD=163`, and `mediadive.medium:J163` after duplicate reconciliation.
- Spot-check regenerated output for 21 g PPLO broth, 5 g glucose, 700 ml distilled water, 200 ml sterile horse serum, 5 ml 0.4% phenol red solution, 100 ml 25% yeast extract solution, variable-concentration penicillin, and pH 7.6.

## Additional Notes

None found.
