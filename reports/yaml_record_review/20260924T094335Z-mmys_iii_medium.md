# YAML Record Review: mmys_iii_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mmys_iii_medium.yaml
- Started UTC: 2026-09-24T09:42:20Z
- Finished UTC: 2026-09-24T09:43:35Z
- Verdict: needs curation

## Target

Generated bacterial recipe for `CultureMech:008508`, `mmys_iii_medium`, from a merge of `TOGO_M186_Mmys-I_Medium` and `TOGO_M192_Mmys-III_Medium`.

The record carries the MMYS-III source identity, `TOGO:M192` / `JCM_M199`, but it also absorbed the MMYS-I source recipe, `TOGO:M186` / `JCM_M193`.

## Validation

Open LinkML validation passed with `No issues found`.

Strict schema-layer validation passed with 0 error rows; `/private/tmp/mmys_iii_medium.strict.tsv` contained only the header line.

Reference validation passed, but performed 0 checks.

Term validation passed. The run emitted the expected `eutils` / `pkg_resources` deprecation warning before `Validation passed`.

Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries inside generated YAML.

## Identity and Grounding

The media identity is internally contradictory. The generated record is named and sourced as MMYS-III, but its ingredient list stores MMYS-I's 30.2 g/L NaCl concentration instead of MMYS-III's 50.2 g/L final NaCl concentration.

The normalized parent and child relationship before merging was correct: `TOGO_M186_Mmys-I_Medium.yaml` used 30.2 g/L NaCl and listed `TOGO_M192_Mmys-III_Medium.yaml` as a salinity-variant child; `TOGO_M192_Mmys-III_Medium.yaml` used 50.2 g/L NaCl and listed MMYS-I as the salinity-variant parent.

The generated merge collapsed that parent and child into one output record, retained the MMYS-III identity, kept the MMYS-I NaCl value, and added `mmys_i_medium` as a synonym. An exact generated-file search found no `mmys_i_medium*.yaml` record left under `data/merge_yaml/merged`.

Hydrate-sensitive CHEBI groundings for `CaCl2 x 2H2O`, `MgCl2 x 6H2O`, and `Na2S2O3 x 5H2O` are consistent with the source strings.

## Evidence

TOGO `M186` and JCM `GRMD=193` define MMYS-I Medium as a 1 L liquid recipe with 30.2 g NaCl, 1 g `KH2PO4`, 1 g `(NH4)2SO4`, 0.2 g `MgCl2 x 6H2O`, 0.05 g `CaCl2 x 2H2O`, 1 ml trace element solution SL8, 3.6 g sodium DL-malate, 1 g yeast extract, 0.5 g `Na2S2O3 x 5H2O`, and 1 L distilled water, with pH adjusted to 6.8.

JCM `GRMD=199` does not define an independent table for MMYS-III. It says to use MMYS-I, JCM medium 193, with 50.2 g/L final NaCl.

TOGO `M192` expands that MMYS-III delta into a complete 1 L recipe whose only formula change relative to TOGO M186 is the NaCl row: 50.2 g/L instead of 30.2 g.

Both TOGO imports encode `Trace element solution SL8 (see Medium [M183])` as a 1 ml cross-reference. JCM 193 points that stock to JCM medium 190, and TOGO M183 is the corresponding `LYS Medium` record for JCM_M190 that contains the actual SL8 subrecipe.

The generated record was created from both `TOGO_M186_Mmys-I_Medium` and `TOGO_M192_Mmys-III_Medium` on one merge fingerprint, so the salinity variant was treated as a duplicate rather than preserved as a distinct generated recipe.

## Completeness

The output has a fatal quantitative omission: the only source-defining MMYS-III change, 50.2 g/L final NaCl, is missing from the top-level ingredients.

The SL8 stock remains an empty placeholder even though the source cross-reference is resolvable through JCM 190 / TOGO M183.

The source pH 6.8 instruction is present in TOGO M186 and inherited by the TOGO M192 expansion, but no pH or preparation instruction is preserved in the generated record.

No target organism, incubation temperature, atmosphere, or growth evidence is present in TOGO M192 or JCM 199, so those absences are not defects for this source-only import.

## Findings

1. Needs curation: the generated merge destroyed a real salinity variant. `mmys_iii_medium.yaml` should contain 50.2 g/L NaCl, but after merging with MMYS-I it contains 30.2 g/L NaCl under the MMYS-III `TOGO:M192` identity.

2. Needs curation: MMYS-I and MMYS-III should survive as two generated recipes linked by `SALINITY_VARIANT`. The current generated output collapses the parent into the child, leaks `mmys_i_medium` into `synonyms`, and leaves `parent_media` pointing at a normalized source that no longer has its own generated record.

3. Needs curation: the SL8 stock composition is absent. The output stores an empty `Trace element solution SL8` solution with `1 G_PER_L`, even though the source row is 1 ml and can be resolved to the JCM 190 / TOGO M183 SL8 recipe.

4. Minor: the 1 L water row is stored as `1 G_PER_L`, which confuses the source solvent volume with a mass-per-liter concentration.

5. Minor: the pH 6.8 instruction from the parent MMYS-I formulation is absent from structured generated fields and source notes.

## Recommended Edits

Change recipe merging so a salinity-variant parent and child do not collapse onto the same generated record when a defining concentration differs.

Regenerate MMYS-I and MMYS-III as separate outputs: MMYS-I with 30.2 g/L NaCl and MMYS-III with 50.2 g/L final NaCl.

Keep the `SALINITY_VARIANT` relationship between those two outputs, but remove `TOGO_M186_Mmys-I_Medium` from the MMYS-III `merged_from` list and remove `mmys_i_medium` from MMYS-III synonyms.

Resolve the SL8 cross-reference to JCM 190 / TOGO M183 and represent the 1 ml SL8 addition as a volume stock addition, not as `1 G_PER_L`.

Preserve pH 6.8 from the MMYS-I base formula on both MMYS-I and its MMYS-III salinity variant.

## Follow-up Checks

Re-run open LinkML, strict, reference, and term validation after any normalized-record or merge-logic edits.

After regeneration, assert that `data/merge_yaml/merged/mmys_i_medium.yaml` and `data/merge_yaml/merged/mmys_iii_medium.yaml` both exist and differ in only the source identity, variant metadata, and NaCl amount.

Re-check the MMYS-II records after fixing SL8 resolution, because the same JCM 190 / TOGO M183 cross-reference pattern appears there.

## Additional Notes

No GitHub issues or PR comments were created by this record review.

The check for a missing generated `mmys_i_medium*.yaml` record included ignored files via `find` and `rg --no-ignore --hidden`.
