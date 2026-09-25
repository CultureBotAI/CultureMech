# YAML Record Review: postgate_j_rs_medium_c

- Repository: CultureMech
- Record: data/merge_yaml/merged/postgate_j_rs_medium_c.yaml
- Started UTC: 2026-09-24T21:30:05Z
- Finished UTC: 2026-09-24T21:30:05Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:010074
- Name: postgate_j_rs_medium_c
- Source import: TOGO_M670_Postgate_J._R_S_Medium_C
- Primary external ID: TOGO:M670
- Maintained input: data/normalized_yaml/bacterial/TOGO_M670_Postgate_J._R_S_Medium_C.yaml

This generated record represents TOGO Medium M670 / JCM Medium 654, POSTGATE J. R'S MEDIUM C.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/postgate_j_rs_medium_c.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M670 / JCM 654 identity. Exact ignored-file searches across `data` for `TOGO:M670`, `M670`, `JCM_M654`, `GRMD=654`, `TOGO_M670_Postgate_J._R_S_Medium_C`, and `postgate_j_rs_medium_c` found this TOGO normalized recipe and this TOGO merge, plus a direct-JCM normalized recipe and generated merge with the same JCM 654 formulation that remain split.

Ingredient identities are mostly recognizable, but several source quantities and preparation semantics are wrong. JCM 654 lists FeSO4 x 7H2O as 4.0 mg, 900 ml distilled water, a post-autoclave 100 ml addition of 6.0% filter-sterilized sodium lactate solution, and cultivation under N2. The generated record instead has 4 G_PER_L FeSO4 x 7H2O, 900 G_PER_L water, an empty `Unknown solution` with 100 G_PER_L concentration, and N2 as a variable ingredient.

## Evidence

- TOGO M670 imports JCM_M654 and points to the JCM GRMD=654 page.
- JCM 654 lists 0.5 g KH2PO4, 1 g NH4Cl, 4.5 g Na2SO4, 0.06 g CaCl2 x 2H2O, 0.06 g MgSO4 x 7H2O, 1 g yeast extract, 4.0 mg FeSO4 x 7H2O, 0.3 g sodium citrate, and 900 ml distilled water.
- JCM 654 then says to mix and autoclave those components, add 100 ml of 6.0% filter-sterilized sodium lactate solution, and cultivate under an N2 atmosphere.
- A separate direct-JCM import at `data/normalized_yaml/bacterial/postgate_j_rs_medium_c.yaml` has the same JCM GRMD=654 source and normalized slug, but it is still generated as `postgate_j_rs_medium_c__f76663b6.yaml`.

## Completeness

The generated TOGO record is incomplete as a source-faithful Postgate J. R'S Medium C representation:

- 4.0 mg FeSO4 x 7H2O was promoted to 4 G_PER_L.
- 900 ml distilled water was promoted to 900 G_PER_L.
- 100 ml 6.0% sodium lactate solution was migrated to an empty default-named solution with concentration 100 G_PER_L; it should be a post-autoclave solution addition, not an orphan stock recipe.
- N2 belongs to incubation or headspace atmosphere metadata, not the ingredient list.
- The TOGO and direct-JCM imports from the same JCM 654 source remain split.

## Findings

1. Major: FeSO4 x 7H2O and distilled water units are wrong in the TOGO M670 normalized source and generated merge. Future repair belongs in `data/normalized_yaml/bacterial/TOGO_M670_Postgate_J._R_S_Medium_C.yaml` or the TOGO importer.
2. Major: The 6.0% sodium lactate addition was migrated into an empty `Unknown solution` with the wrong amount semantics. Future repair belongs in the TOGO normalized source and solution migration logic.
3. Major: N2 was represented as a variable ingredient rather than anaerobic cultivation atmosphere metadata.
4. Major: The TOGO M670 and direct-JCM imports of the same JCM 654 medium remain split across `postgate_j_rs_medium_c.yaml` and `postgate_j_rs_medium_c__f76663b6.yaml`.

## Recommended Edits

- Rebuild TOGO M670 from JCM 654 so the main solution has 4 mg FeSO4 x 7H2O, 900 ml water, 100 ml of 6.0% filter-sterilized sodium lactate added after autoclaving, and N2 recorded as atmosphere metadata.
- Reconcile `data/normalized_yaml/bacterial/TOGO_M670_Postgate_J._R_S_Medium_C.yaml` with `data/normalized_yaml/bacterial/postgate_j_rs_medium_c.yaml` so the direct JCM and TOGO imports no longer produce two generated records for JCM 654.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M670`, `JCM_M654`, and `GRMD=654` with ignored files included to verify the JCM 654 direct and TOGO branches are reconciled or intentionally linked.
- Spot-check the rendered Postgate J. R'S Medium C page to verify N2 appears in atmosphere/preparation context, not as a medium ingredient.

## Additional Notes

None found.
