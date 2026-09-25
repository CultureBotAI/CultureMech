# YAML Record Review: rumen_fluid_xylan_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rumen_fluid_xylan_agar.yaml`
- Started UTC: `2026-09-25T03:08:24Z`
- Finished UTC: `2026-09-25T03:08:24Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `rumen_fluid_xylan_agar`, a single-source merge of `data/normalized_yaml/bacterial/TOGO_M126_Rumen_Fluid-Xylan-Agar.yaml`.

The target represents TOGO M126, `Rumen Fluid-Xylan-Agar`, imported from JCM M135. The source identity and `SOLID_AGAR` physical state are plausible, but several milligram source quantities were imported as grams per liter and liquid volumes were represented as `G_PER_L`.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M126 is the right identity for this generated record: the live TOGO payload identifies `http://togomedium.org/medium/M126`, name `Rumen Fluid-Xylan-Agar`, `original_media_id` `JCM_M135`, and source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=135`.

The original JCM `GRMD=135` URL currently returns "Nothing found.". The live MediaDive REST endpoint for J135 still exposes the same JCM recipe and confirms a 1000 ml main solution with 600 ml distilled water, 400 ml Rumen fluid, and the same direct chemical additions.

This generated record should be reconciled with `data/merge_yaml/merged/rumen_fluid_xylan_agar__21a2a89a.yaml`, the direct MediaDive/JCM J135 import of the same source medium, after both import paths are corrected.

## Evidence

The TOGO M126 payload lists 600 ml `Distilled water`, 90 mg `MgSO4 x 7 H2O`, 0.45 g `NaCl`, 225 mg `KH2PO4`, 225 mg `K2HPO4`, 0.25 g `Na2S x 9 H2O`, 6.37 g `NaHCO3`, 0.45 g `(NH4)2SO4`, 0.45 g `CaCl2`, 15 g `Xylan`, 5 mg `Indigo carmine`, 400 ml `Rumen fluid`, 15 g `Agar`, and 0.25 g `L--Cysteine x HCl x H2O`.

The MediaDive J135 endpoint reports matching final `g_l` values for the milligram source masses: `MgSO4 x 7 H2O` 0.09 g/L, both phosphate salts 0.225 g/L, and `Indigo carmine` 0.005 g/L.

## Completeness

The generated record retains all TOGO M126 rows, but its concentration fields mis-state several source amounts:

- `MgSO4 x 7 H2O` 90 mg is represented as `90 G_PER_L`.
- `KH2PO4` 225 mg and `K2HPO4` 225 mg are represented as `225 G_PER_L`.
- `Indigo carmine` 5 mg is represented as `5 G_PER_L`.
- 600 ml distilled water and 400 ml Rumen fluid are represented as `600 G_PER_L` and `400 G_PER_L`.

## Findings

- `needs curation`: Three mineral or buffer masses have 1000x unit slips. TOGO records 90 mg `MgSO4 x 7 H2O`, 225 mg `KH2PO4`, and 225 mg `K2HPO4`, but the generated record has `90 G_PER_L`, `225 G_PER_L`, and `225 G_PER_L`.
- `needs curation`: `Indigo carmine` has a 1000x unit slip. TOGO records 5 mg, while the generated record has `5 G_PER_L`; the MediaDive J135 `g_l` value is `0.005`.
- `needs curation`: Volumetric biological fluid and water additions were serialized as mass concentrations. `Rumen fluid` is a 400 ml addition and `Distilled water` is a 600 ml addition in the 1000 ml main solution.
- `needs curation`: The generated `high_metal: true` flag appears to be an artifact of the 90 mg to `90 G_PER_L` magnesium sulfate slip, and should be recalculated after the TOGO M126 quantities are corrected.
- `pass with minor issues`: The gram-denominated direct additions for `NaCl`, `Na2S x 9 H2O`, `NaHCO3`, `(NH4)2SO4`, `CaCl2`, `Xylan`, `Agar`, and `L--Cysteine x HCl x H2O` match TOGO M126.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M126_Rumen_Fluid-Xylan-Agar.yaml`, or the TOGO import logic that creates it, rather than hand-editing `data/merge_yaml/merged/rumen_fluid_xylan_agar.yaml`.
- Convert milligram source quantities to gram-scale final concentrations: `MgSO4 x 7 H2O` to 0.09 g/L, `KH2PO4` to 0.225 g/L, `K2HPO4` to 0.225 g/L, and `Indigo carmine` to 0.005 g/L for this 1000 ml medium.
- Preserve `Rumen fluid` and `Distilled water` as volume additions, or otherwise avoid labeling their source milliliter amounts as grams per liter.
- Recompute `high_metal` after the magnesium concentration is fixed.
- After TOGO M126 is fixed, rerun the merge and compare it with the direct MediaDive J135 source for source-duplicate merging.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M126_Rumen_Fluid-Xylan-Agar.yaml`.
- Regenerate `data/merge_yaml/merged/rumen_fluid_xylan_agar.yaml` and verify that `MgSO4 x 7 H2O` is `0.09 G_PER_L`, the phosphate salts are `0.225 G_PER_L`, and `Indigo carmine` is `0.005 G_PER_L`.
- Verify that `Rumen fluid` and `Distilled water` are no longer represented as `400 G_PER_L` and `600 G_PER_L`.
- Run an exact ignored-file-inclusive search for `TOGO_M126_Rumen_Fluid-Xylan-Agar`, `mediadive.medium:J135`, and `rumen_fluid_xylan_agar` before merging or deleting duplicate normalized sources.

## Additional Notes

The TOGO M126 payload does not include preparation comments or a pH value, so neither absence was treated as a generated-record defect. Empty `target_organisms` were not treated as defects.
