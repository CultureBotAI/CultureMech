# YAML Record Review: thermaerobacter_ty_medium__cc9fc2e5

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermaerobacter_ty_medium__cc9fc2e5.yaml
- Started UTC: 2026-09-25T09:24:00Z
- Finished UTC: 2026-09-25T09:24:51Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:010164`, `thermaerobacter_ty_medium`, grounded to TOGO `M758` / JCM `JCM_M734-2`.

## Validation

- LinkML schema validation passed; the command exited 0 with no diagnostics.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- JCM `GRMD=734` is live and serves `THERMAEROBACTER TY MEDIUM`.
- MediaDive `J734` currently resolves to status 200, count 1, source `JCM`, name `THERMAEROBACTER TY MEDIUM`, and the JCM `GRMD=734` source URL.
- TOGO `M758` identifies the same JCM page as `Thermaerobacter TY Medium`, `original_media_id: JCM_M734-2`, and `src_url` JCM `GRMD=734`.
- An exact `J734` / `GRMD=734` / `TOGO:M758` / `JCM_M734` / `thermaerobacter_ty_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this TOGO `M758` generated record, the cleaner MediaDive `J734` generated record, a TOGO `M757` generated duplicate from `JCM_M734`, and their normalized source files.

## Evidence

- JCM `GRMD=734`, MediaDive `J734`, and TOGO `M758` agree on 1 g tryptone, 2 g yeast extract, 1 g NaCl, 1 g `MgSO4 x 7 H2O`, 2 g `CaCl2 x 2 H2O`, and 1 L distilled water.
- JCM and MediaDive put gellan gum only in the preparation note: for solid medium, add 20 g/L gellan gum.
- TOGO `M758` represents gellan gum as an item without a numeric amount rather than only as the solid-medium note.

## Completeness

- The core TY liquid formula is present and matches the live JCM page.
- The target includes distilled water as `1 G_PER_L` instead of 1 L.
- The target's `physical_state` is `LIQUID`, but gellan gum is represented as a variable top-level ingredient.
- The MediaDive `J734` record and TOGO `M757` record are generated separately even though all three branches point back to the same JCM `GRMD=734` source.

## Findings

- The optional gellan gum for preparing solid medium is promoted into a top-level variable ingredient in a liquid recipe. It should be represented as a solid-medium variant or retained as a preparation note, not as an undefined final liquid ingredient.
- Water is imported as `1 G_PER_L`; the source says 1 L distilled water.
- `TOGO:M758`, TOGO `M757`, and `mediadive.medium:J734` are source-equivalent records for JCM `GRMD=734` but remain unmerged.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/thermaerobacter_ty_medium__cc9fc2e5.yaml`; repair `data/normalized_yaml/bacterial/TOGO_M758_Thermaerobacter_TY_Medium.yaml` or the TOGO import path, then regenerate this file.
- Treat the 20 g/L gellan gum addition as a solid-medium variant of the liquid TY parent, or keep it in a preparation note if variants are not generated from imported media yet.
- Merge the `M758`, `M757`, and `J734` branches by recognizing their shared JCM `GRMD=734` grounding.
- Preserve 1 L distilled water as a volume, not as a gram-per-liter solute concentration.

## Follow-up Checks

- After importer or merge fixes, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `J734`, `JCM_M734`, `TOGO:M757`, `TOGO:M758`, and `GRMD=734` with ignored files included.
- Verify the regenerated liquid parent has no variable gellan-gum top-level ingredient.
- Verify the solid preparation is captured once, either as a variant or as a note, and that the TOGO/MediaDive duplicate split is gone.

## Additional Notes

The first duplicate search also included bare `M758`; that was too broad because it matched an unrelated `JCM_M758` line. That hit was discarded, and the local duplicate search was rerun with exact `TOGO:M758`, `JCM_M734`, `GRMD=734`, `J734`, and `thermaerobacter_ty_medium` patterns.
