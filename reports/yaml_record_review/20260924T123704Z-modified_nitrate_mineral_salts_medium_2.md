# YAML Record Review: modified_nitrate_mineral_salts_medium_2

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_nitrate_mineral_salts_medium_2.yaml
- Started UTC: 2026-09-24T12:37:04Z
- Finished UTC: 2026-09-24T12:37:04Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:007848`, `modified_nitrate_mineral_salts_medium_2`, generated from `data/normalized_yaml/bacterial/TOGO_M1312_Modified_Nitrate_Mineral_Salts_Medium-2.yaml`.
- The record represents TOGO `M1312`, which points back to JCM `JCM_M1221` / `GRMD=1221`, named `MODIFIED NITRATE  MINERAL SALTS MEDIUM-2`.
- The generated TOGO record was compared with TOGO `M1312`, JCM `GRMD=1221`, and the parallel MediaDive `J1221` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M1312`, MediaDive `J1221`, and JCM `GRMD=1221` all identify the same Modified Nitrate Mineral Salts Medium-2 recipe.
- A gitignore-independent duplicate check for the exact normalized name and JCM/TOGO/MediaDive identifiers found a parallel MediaDive maintained record, `data/normalized_yaml/bacterial/modified_nitrate_mineral_salts_medium_2.yaml`, and a separate generated record, `data/merge_yaml/merged/modified_nitrate_mineral_salts_medium_2__4cc0cd9a.yaml`, for the same JCM 1221 source.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists a 1 L basal medium with MgSO4 x 7 H2O, CaCl2 x 2 H2O, KNO3, 1 ml FeCl2 solution, 1 ml Trace element solution, 2 ml 1 M HEPES solution at pH 7.0, 4 mg ammonium ferric citrate, and 1 L distilled water.
- JCM then instructs adding 2 ml Phosphate buffer solution and 10 ml Vitamin solution after cooling.
- The local Phosphate buffer solution is 1.4 g KH2PO4 and 3.6 g Na2HPO4 x 2 H2O in 100 ml distilled water.
- The local Vitamin solution is 1 L Trace vitamins plus 20 mg Vitamin B12, 5 mg L-Ascorbic acid, and 5 mg Nicotinamide.
- JCM describes two substrate modes: a 75:25 air-methane gas mixture for methane and 4.0 ml per liter filter-sterilized methanol for methanol cultures.

## Completeness

- The basal salts and ammonium ferric citrate are present.
- The six source solution additions are migrated to empty `solutions` stubs with `G_PER_L` concentrations instead of source volume units.
- Phosphate buffer and vitamin solution components are flattened into top-level ingredients with incorrect gram-per-liter amounts.
- The methanol supplement option is absent from structured ingredients or solutions.
- The 1 L basal water and 100 ml Phosphate buffer water rows are merged into a single `101.0` `G_PER_L` water row.

## Findings

- Blocker: source solution additions were migrated into empty stubs with bogus gram-per-liter units. The 1 ml FeCl2 solution, 1 ml Trace element solution, 2 ml 1 M HEPES solution, 2 ml Phosphate buffer solution, 10 ml Vitamin solution, and 1 L Trace vitamins rows are all represented as `G_PER_L` solution concentrations.
- Blocker: the local Phosphate buffer and Vitamin solution were flattened into top-level ingredients with source amounts copied as grams per liter. For example, 20 mg Vitamin B12 became `20` `G_PER_L`, 5 mg L-Ascorbic acid became `5` `G_PER_L`, and 3.6 g Na2HPO4 x 2 H2O in a 100 ml stock became `3.6` `G_PER_L`.
- Major: 1 L basal water and 100 ml phosphate-buffer water were merged into one `101.0` `G_PER_L` Distilled water row, losing both the volume units and the solution scopes.
- Major: the 4.0 ml per liter methanol substrate option from JCM is missing.
- Major: the same JCM 1221 medium is maintained and generated twice, once through TOGO `M1312` and once through MediaDive `J1221`.

## Recommended Edits

- Preserve the six JCM solution additions with milliliter or liter units instead of migrating them to empty `G_PER_L` solution stubs.
- Keep Phosphate buffer and Vitamin solution components scoped under their stock recipes.
- Preserve basal and buffer water rows with their original volume contexts.
- Represent the methanol cultivation option as a 4.0 ml/L filter-sterilized methanol supplement or another structured optional substrate.
- Merge or explicitly cross-link the TOGO `M1312` and MediaDive `J1221` maintained records before regeneration so JCM `GRMD=1221` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting TOGO solution migration.
- Recompare the regenerated record against JCM `GRMD=1221`, including both local stock recipes and both methane and methanol substrate modes.
- Confirm that generated YAML no longer contains both `modified_nitrate_mineral_salts_medium_2.yaml` and `modified_nitrate_mineral_salts_medium_2__4cc0cd9a.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
