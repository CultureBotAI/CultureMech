# YAML Record Review: mj_n_basal_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mj_n_basal_medium.yaml
- Started UTC: 2026-09-24T07:45:32Z
- Finished UTC: 2026-09-24T07:46:16Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009748`
- Generated name: `mj_n_basal_medium`
- Generated source file: `data/merge_yaml/merged/mj_n_basal_medium.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/TOGO_M368_MJ-N_Basal_Medium.yaml`
- Duplicate generated record: `data/merge_yaml/merged/mj_n_basal_medium__47625802.yaml`
- Upstream source: TOGO Medium `M368`, preserving JCM medium `M374`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mj_n_basal_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with TOGO `M368`, whose metadata points at JCM `M374`.
- The `media_term` points to `TOGO:M368`.
- An ignored-file-inclusive exact path search found a separate generated record, `mj_n_basal_medium__47625802.yaml`, for the same snake-cased JCM recipe.
- The retained NaNO3 ingredient is grounded to sodium nitrate.
- Carbon dioxide and nitrogen were preserved only as variable-concentration gas ingredients.

## Evidence

- TOGO `M368` contains 2 g/L NaNO3, 1 L `MJ BASAL MEDIUM (see Medium [M350])`, carbon dioxide gas, and nitrogen gas.
- The TOGO `M368` preparation comment says to use Medium No. 356 supplemented with 2.0 g/L NaNO3, replace the gas phase with an N2-CO2 80:20 gas mixture, and pressurize to 150 kPa.
- TOGO `M350`, MJ Basal Medium, contains 0.25 g NH4Cl, 1.5 g NaHCO3, 1.5 g `Na2S2O3 x 5 H2O`, 1 L `MJ(-N) synthetic seawater` from Medium `M260`, 1 ml Trace vitamins from Medium `M190`, carbon dioxide, nitrogen, and oxygen.
- TOGO `M260` carries the nested `MJ(-N) synthetic seawater` formula and depends on 10 ml Trace minerals from Medium `M142`.

## Completeness

- The generated record has `composition: []` for the entire 1 L MJ Basal Medium reference.
- The generated top-level `ingredients` contain only NaNO3 plus carbon dioxide and nitrogen gas placeholders.
- All M350 basal-medium ingredients are absent from structured ingredient rows.
- The nested M260 synthetic seawater, M142 Trace minerals, and M190 Trace vitamins recipes are also absent.
- The N2-CO2 80:20 gas-ratio instruction and 150 kPa pressure are not represented as preparation steps.

## Findings

- High: The 1 L M350 basal-medium reference was migrated into an empty solution, dropping the recipe that makes up nearly all of this medium.
- High: Nested M260, M190, and M142 cross-references were not resolved or preserved, so seawater salts, trace minerals, and vitamins are missing.
- Medium: TOGO `M368` gas-phase instructions were collapsed to variable CO2 and N2 ingredients without the 80:20 ratio or 150 kPa pressure.
- Medium: The TOGO `M368` import and a MediaDive/JCM import generated two records for the same MJ-N Basal Medium identity.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/TOGO_M368_MJ-N_Basal_Medium.yaml` with an explicit MJ Basal Medium solution rather than an empty M350 stub.
- Resolve or preserve the M350 contents, including the M260 synthetic seawater, M142 Trace minerals, and M190 Trace vitamins dependencies.
- Keep 2 g/L NaNO3 as the direct M368 supplement.
- Add preparation semantics for the N2-CO2 80:20 gas phase and 150 kPa pressure.
- Reconcile the TOGO `M368` and MediaDive/JCM duplicate records so MJ-N Basal Medium is not published twice.
- Regenerate the merged record after repairing the normalized sources.

## Follow-up Checks

- Re-fetch TOGO `M368`, `M350`, `M260`, `M190`, and `M142` before rebuilding the nested solution graph.
- Confirm no generated MJ Basal Medium solution has `composition: []`.
- Confirm the regenerated M368 record still has a 2 g/L NaNO3 supplement outside the copied basal medium.
- Repeat the ignored-file-inclusive exact path search for `mj_n_basal_medium` to verify the duplicate hashed generated record is gone or intentionally aliased.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.

## Additional Notes

- None found.
