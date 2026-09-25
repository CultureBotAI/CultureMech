# YAML Record Review: rumen_fluid_glucose_cellobiose_agar__677afe49

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar__677afe49.yaml`
- Started UTC: `2026-09-25T03:07:14Z`
- Finished UTC: `2026-09-25T03:07:14Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `rumen_fluid_glucose_cellobiose_agar__677afe49`, a single-source merge of `data/normalized_yaml/bacterial/rumen_fluid_glucose_cellobiose_agar.yaml`.

The target represents the MediaDive/JCM J134 record for `RUMEN FLUID-GLUCOSE-CELLOBIOSE AGAR`. It is the same JCM medium also represented by TOGO M125, but it did not merge with the TOGO import because the two import paths produced different fingerprints.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The identity is correct: the live MediaDive REST endpoint for J134 reports source `JCM`, name `RUMEN FLUID-GLUCOSE-CELLOBIOSE AGAR`, and link `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=134`. The live JCM page currently returns "Nothing found.", so MediaDive and TOGO are the available structured representations of this JCM recipe.

This generated record should be reconciled with `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar.yaml`, the TOGO M125 import of the same `original_media_id` `JCM_M134`. The two records differ because the MediaDive path converts some source masses to final `g_l` concentrations while the TOGO path carries several source amounts literally.

## Evidence

The MediaDive J134 main solution has final volume 1014 ml and includes 248 mg glucose, 248 mg cellobiose, 0.5 g soluble starch, 1 g `(NH4)2SO4`, 4 ml `1%` Resazurin, 200 ml distilled water, 500 ml Salt solution, 300 ml Rumen fluid, 0.5 g `L-Cysteine HCl x H2O`, 10 ml `1%` Hemin, 0.2 ml `0.1%` Vitamin K1, and 20 g agar.

The referenced Salt solution is a 1 L stock containing 0.2 g `CaCl2 x 2 H2O`, 0.2 g `MgSO4 x 7 H2O`, 1 g `K2HPO4`, 1 g `KH2PO4`, 10 g `NaHCO3`, 2 g `NaCl`, and 1000 ml distilled water.

## Completeness

The generated record correctly uses MediaDive's `g_l` conversions for direct mass additions: glucose and cellobiose at `0.244576 G_PER_L`, starch and cysteine at `0.493097 G_PER_L`, ammonium sulfate at `0.986193 G_PER_L`, and agar at `19.7239 G_PER_L`.

It loses the remaining structure:

- The 200 ml main-solution water and 1 L Salt solution water are absent.
- The Salt solution 500 ml aliquot is absent as a solution relationship.
- The 300 ml Rumen fluid aliquot is serialized as `300 G_PER_L`.
- The 4 ml Resazurin, 10 ml Hemin, and 0.2 ml Vitamin K1 aliquots are serialized as `4 G_PER_L`, `10 G_PER_L`, and `0.2 G_PER_L`.
- Salt solution components are hoisted into the parent at stock strength.

## Findings

- `needs curation`: The direct MediaDive import flattened `Salt solution` into final ingredients without applying its 500 ml aliquot or preserving the stock boundary. The generated `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`, `K2HPO4`, `KH2PO4`, `NaHCO3`, and `NaCl` rows are the 1 L salt-stock concentrations, not final parent-medium concentrations.
- `needs curation`: Milliliter aliquots were modeled as grams per liter. Resazurin, Hemin, Vitamin K1, and Rumen fluid are all source-volume additions in MediaDive J134, but the generated target stores them as `G_PER_L` parent ingredients.
- `needs curation`: The water rows were dropped. MediaDive J134 explicitly retains 200 ml distilled water in the main solution and 1000 ml distilled water in the Salt solution stock, but neither scope is represented in the generated YAML.
- `needs curation`: The J134 recipe is split into two generated records. This MediaDive record and TOGO M125 share the JCM `GRMD=134` source identity and should converge after the TOGO milligram and solution-flattening issues are repaired.
- `pass with minor issues`: The direct mass rows from the main solution are correctly normalized against the 1014 ml final volume; unlike the TOGO import, this record does not inflate the 248 mg glucose and cellobiose source masses by 1000x.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/rumen_fluid_glucose_cellobiose_agar.yaml`, or the MediaDive import path that creates it, rather than hand-editing `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar__677afe49.yaml`.
- Preserve `Salt solution` as a nested 1 L stock and retain the parent 500 ml aliquot.
- Preserve `Rumen fluid`, 1% Resazurin, 1% Hemin, and 0.1% Vitamin K1 as volumetric or percentage solution additions; do not convert their milliliter aliquots to grams per liter.
- Reintroduce the main and stock distilled-water rows in their correct scopes if water is within this repository's curation target for MediaDive imports.
- After the MediaDive J134 and TOGO M125 imports are repaired, merge them as source duplicates instead of leaving separate generated records for the same JCM medium.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/rumen_fluid_glucose_cellobiose_agar.yaml`.
- Regenerate `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar__677afe49.yaml` and verify that `Resazurin` `4 G_PER_L`, `Hemin` `10 G_PER_L`, `Vitamin K1` `0.2 G_PER_L`, and `Rumen fluid` `300 G_PER_L` are gone.
- Verify that stock-strength `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`, `K2HPO4`, `KH2PO4`, `NaHCO3`, and `NaCl` rows are no longer direct parent ingredients.
- Run an exact ignored-file-inclusive search for `mediadive.medium:J134`, `JCM_M134`, `TOGO_M125_Rumen_Fluid-Glucose-Cellobiose_Agar`, and `rumen_fluid_glucose_cellobiose_agar` before deduplicating the normalized sources.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. The JCM source currently being inaccessible does not block curation because both MediaDive and TOGO expose structured J134 data.
