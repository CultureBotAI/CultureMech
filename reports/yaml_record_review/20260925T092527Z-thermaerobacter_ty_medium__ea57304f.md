# YAML Record Review: thermaerobacter_ty_medium__ea57304f

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermaerobacter_ty_medium__ea57304f.yaml
- Started UTC: 2026-09-25T09:25:27Z
- Finished UTC: 2026-09-25T09:26:04Z
- Verdict: pass with minor issues

## Target

Generated merged MediaRecipe `CultureMech:003077`, `thermaerobacter_ty_medium`, grounded to `mediadive.medium:J734` / JCM Medium 734.

## Validation

- LinkML schema validation passed.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- JCM `GRMD=734` is live and serves `THERMAEROBACTER TY MEDIUM`.
- MediaDive `J734` currently resolves to status 200, count 1, source `JCM`, name `THERMAEROBACTER TY MEDIUM`, and the JCM `GRMD=734` source URL.
- TOGO `M757` identifies the same JCM page as `Thermaerobacter TY Medium`, `original_media_id: JCM_M734`, and `src_url` JCM `GRMD=734`.
- TOGO `M758` identifies the same JCM page as `Thermaerobacter TY Medium`, `original_media_id: JCM_M734-2`, and `src_url` JCM `GRMD=734`.
- An exact `J734` / `GRMD=734` / `TOGO:M758` / `JCM_M734` / `thermaerobacter_ty_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this MediaDive `J734` generated record, the TOGO `M757` and `M758` generated duplicates, and their normalized source files.

## Evidence

- JCM `GRMD=734`, MediaDive `J734`, TOGO `M757`, and TOGO `M758` agree on 1 g tryptone, 2 g yeast extract, 1 g NaCl, 1 g `MgSO4 x 7 H2O`, 2 g `CaCl2 x 2 H2O`, and 1 L distilled water.
- The final MediaDive concentrations are 1 G_PER_L tryptone, 2 G_PER_L yeast extract, 1 G_PER_L NaCl, 1 G_PER_L `MgSO4 x 7 H2O`, and 2 G_PER_L `CaCl2 x 2 H2O`, matching the 1 L JCM formulation.
- JCM and MediaDive put the optional solid-medium gellan-gum addition only in a preparation note.

## Completeness

- All non-water medium solutes are present with source-matching concentrations.
- The optional 20 g/L gellan gum addition for solid medium is preserved as a preparation step, not incorrectly modeled as part of the liquid formulation.
- The source-equivalent TOGO `M757` and `M758` imports remain split out as `data/merge_yaml/merged/THERMAEROBACTER_TY_MEDIUM.yaml` and `data/merge_yaml/merged/thermaerobacter_ty_medium__cc9fc2e5.yaml`.

## Findings

- The MediaDive/JCM target is source-faithful for the liquid TY recipe.
- Two TOGO records grounded to the same JCM `GRMD=734` page remain unmerged.

## Recommended Edits

- Merge TOGO `M757` and MediaDive `J734` as source-equivalent records for the same liquid TY medium.
- Treat TOGO `M758`, which imported the optional gellan gum note, as a solid-medium variant of the liquid TY parent rather than a separate liquid `MediaRecipe`.

## Follow-up Checks

- After duplicate merging, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `J734`, `JCM_M734`, `TOGO:M757`, `TOGO:M758`, and `GRMD=734` with ignored files included.

## Additional Notes

None found
