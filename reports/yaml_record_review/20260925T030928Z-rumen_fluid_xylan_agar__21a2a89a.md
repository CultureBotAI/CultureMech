# YAML Record Review: rumen_fluid_xylan_agar__21a2a89a

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rumen_fluid_xylan_agar__21a2a89a.yaml`
- Started UTC: `2026-09-25T03:09:28Z`
- Finished UTC: `2026-09-25T03:09:28Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `rumen_fluid_xylan_agar__21a2a89a`, a single-source merge of `data/normalized_yaml/bacterial/rumen_fluid_xylan_agar.yaml`.

The target represents the MediaDive/JCM J135 record for `RUMEN FLUID-XYLAN-AGAR`. It is the same JCM medium also represented by TOGO M126, but it did not merge with the TOGO import because the TOGO import inflated several milligram quantities by 1000x.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The identity is correct: the live MediaDive REST endpoint for J135 reports source `JCM`, name `RUMEN FLUID-XYLAN-AGAR`, and link `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=135`. The live JCM page currently returns "Nothing found.", so MediaDive and TOGO are the available structured representations of this JCM recipe.

This generated record should be reconciled with `data/merge_yaml/merged/rumen_fluid_xylan_agar.yaml`, the TOGO M126 import of the same `original_media_id` `JCM_M135`, after the TOGO milligram rows are corrected.

## Evidence

The MediaDive J135 main solution has final volume 1000 ml and includes 225 mg `K2HPO4`, 225 mg `KH2PO4`, 0.45 g `NaCl`, 0.45 g `(NH4)2SO4`, 0.45 g `CaCl2`, 90 mg `MgSO4 x 7 H2O`, 6.37 g `NaHCO3`, 0.25 g `L-Cysteine HCl x H2O`, 0.25 g `Na2S x 9 H2O`, 5 mg `Indigo carmine`, 400 ml `Rumen fluid`, 15 g `Agar`, 15 g `Xylan`, and 600 ml distilled water.

The generated solute concentrations match MediaDive's `g_l` values for every mass row, including the milligram rows: both phosphate salts are `0.225 G_PER_L`, `MgSO4 x 7 H2O` is `0.09 G_PER_L`, and `Indigo carmine` is `0.005 G_PER_L`.

## Completeness

The generated record preserves all mass-bearing MediaDive solutes at the correct final concentration and uses the correct `SOLID_AGAR` state.

Two volumetric rows are still not represented faithfully:

- `Rumen fluid` is a 400 ml addition to a 1000 ml final recipe, but the generated record stores it as `400 G_PER_L`.
- `Distilled water` is a 600 ml addition and is absent from the generated record.

## Findings

- `needs curation`: The 400 ml `Rumen fluid` addition is modeled as `400 G_PER_L`. That loses the source volume and treats an undefined biological fluid as a mass concentration.
- `needs curation`: The 600 ml distilled-water row is missing, even though MediaDive J135 retains it as the main-solution balance.
- `needs curation`: JCM J135 is split across two generated records. The MediaDive/JCM record is the same source medium as TOGO M126 and should merge with it once the TOGO import stops converting 90 mg, 225 mg, 225 mg, and 5 mg to gram-per-liter values.
- `pass with minor issues`: All direct chemical mass additions are correctly represented, including `K2HPO4`, `KH2PO4`, `MgSO4 x 7 H2O`, and `Indigo carmine`.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/rumen_fluid_xylan_agar.yaml`, or the MediaDive import path that creates it, rather than hand-editing `data/merge_yaml/merged/rumen_fluid_xylan_agar__21a2a89a.yaml`.
- Preserve `Rumen fluid` as a 400 ml volumetric addition instead of a `G_PER_L` ingredient.
- Reintroduce the 600 ml distilled-water row if water is within this repository's curation target for MediaDive imports.
- After the TOGO M126 and MediaDive J135 imports are repaired, merge them as source duplicates instead of leaving separate generated records for the same JCM medium.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/rumen_fluid_xylan_agar.yaml`.
- Regenerate `data/merge_yaml/merged/rumen_fluid_xylan_agar__21a2a89a.yaml` and verify that `Rumen fluid` is no longer `400 G_PER_L`.
- Verify that the regenerated J135 record still keeps `K2HPO4` and `KH2PO4` at `0.225 G_PER_L`, `MgSO4 x 7 H2O` at `0.09 G_PER_L`, and `Indigo carmine` at `0.005 G_PER_L`.
- Run an exact ignored-file-inclusive search for `mediadive.medium:J135`, `JCM_M135`, `TOGO_M126_Rumen_Fluid-Xylan-Agar`, and `rumen_fluid_xylan_agar` before deduplicating the normalized sources.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review.
