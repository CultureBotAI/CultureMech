# YAML Record Review: rumen_fluid_glucose_cellobiose_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar.yaml`
- Started UTC: `2026-09-25T03:06:10Z`
- Finished UTC: `2026-09-25T03:06:10Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `rumen_fluid_glucose_cellobiose_agar`, a single-source merge of `data/normalized_yaml/bacterial/TOGO_M125_Rumen_Fluid-Glucose-Cellobiose_Agar.yaml`.

The target represents TOGO M125, `Rumen Fluid-Glucose-Cellobiose Agar`, imported from JCM M134. The high-level source identity and `SOLID_AGAR` physical state are plausible, but the imported ingredients flatten source solution aliquots, convert milliliter aliquots to grams per liter, and promote two 248 mg carbohydrate additions to `248 G_PER_L`.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M125 is the right identity for this generated record: the live TOGO payload identifies `http://togomedium.org/medium/M125`, name `Rumen Fluid-Glucose-Cellobiose Agar`, `original_media_id` `JCM_M134`, and source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=134`.

The original JCM `GRMD=134` URL currently returns "Nothing found.", so TOGO's retained structured payload is the available source of record. TOGO preserves one main solution and a nested `Salt solution`; the generated YAML does not preserve that boundary.

An ignored-file-inclusive filename search found a separate sibling, `data/normalized_yaml/bacterial/rumen_fluid_glucose_cellobiose_agar.yaml`, and a separate generated record, `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar__677afe49.yaml`. This TOGO M125 import should be reconciled with that sibling only after both generated records are reviewed against their sources.

## Evidence

The TOGO M125 main solution lists 4 ml `1% Resazurin solution`, 0.2 ml `0.1% Vitamin K1`, 10 ml `1% Hemin solution`, 200 ml distilled water, 1 g `(NH4)2SO4`, 248 mg `Cellobiose`, 300 ml `Rumen fluid`, 248 mg `Glucose`, 0.5 g `Soluble starch`, 20 g `Bacto agar (BD-Difco)`, 0.5 g `L--Cysteine x HCl x H2O`, and 500 ml `Salt solution (see below)`.

The nested `Salt solution` is a 1 L stock of 0.2 g `MgSO4 x 7 H2O`, 2 g `NaCl`, 0.2 g `CaCl2 x 2 H2O`, 1 g `KH2PO4`, 1 g `K2HPO4`, 10 g `NaHCO3`, and distilled water.

## Completeness

The generated YAML has the right source medium and retains the agar and most ingredient labels, but it loses or corrupts several source amounts:

- `1% Resazurin solution`, `1% Hemin solution`, and `Salt solution (see below)` survive only as empty `solutions` entries with `4 G_PER_L`, `10 G_PER_L`, and `500 G_PER_L`.
- The 0.2 ml `0.1% Vitamin K1` solution is represented as `0.2 G_PER_L`.
- The 300 ml `Rumen fluid` volume is represented as `300 G_PER_L`.
- The two 248 mg carbohydrate additions are represented as `248 G_PER_L` each.
- The 1 L Salt solution water was merged with the 200 ml main-solution water into `Distilled water` `201.0 G_PER_L`.
- The salt stock components are hoisted into the parent at stock strength.

## Findings

- `needs curation`: `Cellobiose` and `Glucose` have a 1000x unit slip. TOGO lists both source amounts as 248 mg, but the generated record has `248 G_PER_L` for each.
- `needs curation`: Three liquid aliquots were serialized as mass concentrations. TOGO lists 4 ml `1% Resazurin solution`, 10 ml `1% Hemin solution`, and 500 ml `Salt solution (see below)`; the generated `solutions` entries are empty and carry `G_PER_L` values equal to those source milliliter amounts.
- `needs curation`: The Vitamin K1 aliquot was also mis-modeled. TOGO lists 0.2 ml of a 0.1% Vitamin K1 solution, while the generated ingredient row reports `0.2 G_PER_L`.
- `needs curation`: The 300 ml undefined `Rumen fluid` addition was flattened to `300 G_PER_L`. This is a volumetric biological-fluid addition, not 300 g/L of a chemically defined compound.
- `needs curation`: The Salt solution stock was flattened into the parent without its 500 ml dilution context. The generated `MgSO4 x 7 H2O`, `NaCl`, `CaCl2 x 2 H2O`, `KH2PO4`, `K2HPO4`, and `NaHCO3` rows are stock-strength concentrations from the 1 L Salt solution, and the stock water was incorrectly merged into the parent water row.
- `pass with minor issues`: The medium identity, agar amount, ammonium sulfate amount, soluble starch amount, cysteine amount, and hydrated salt groundings are otherwise plausible relative to the TOGO M125 payload.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M125_Rumen_Fluid-Glucose-Cellobiose_Agar.yaml`, or the TOGO import logic that creates it, rather than hand-editing `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar.yaml`.
- Convert the 248 mg `Cellobiose` and 248 mg `Glucose` source masses to 0.248 g-scale final concentrations, or preserve the original source amounts if the schema can represent source mass directly.
- Preserve `1% Resazurin solution`, `0.1% Vitamin K1`, `1% Hemin solution`, `Rumen fluid`, and `Salt solution` as volumetric main-solution additions instead of converting their milliliter amounts to `G_PER_L`.
- Preserve `Salt solution` as a nested 1 L stock and keep its 500 ml parent aliquot; do not merge its water or stock-strength salts into the parent ingredient list.
- After TOGO M125 is fixed, rerun the merge and compare the result with `rumen_fluid_glucose_cellobiose_agar__677afe49` for a true duplicate or variant relationship.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M125_Rumen_Fluid-Glucose-Cellobiose_Agar.yaml`.
- Regenerate `data/merge_yaml/merged/rumen_fluid_glucose_cellobiose_agar.yaml` and verify that neither `Cellobiose` nor `Glucose` remains at `248 G_PER_L`.
- Verify that the regenerated record has no empty `solutions` entries for Resazurin solution, Hemin solution, or Salt solution.
- Verify that no parent ingredient retains the stock-strength salt rows `0.2 G_PER_L`, `2 G_PER_L`, `0.2 G_PER_L`, `1 G_PER_L`, `1 G_PER_L`, and `10 G_PER_L` from the 1 L Salt solution.
- Run an exact ignored-file-inclusive search for `TOGO_M125_Rumen_Fluid-Glucose-Cellobiose_Agar` and `rumen_fluid_glucose_cellobiose_agar` before merging or deleting duplicate normalized sources.

## Additional Notes

The TOGO M125 payload does not include preparation comments or a pH value, so neither absence was treated as a generated-record defect. The absence of `target_organisms` was also not treated as a defect for this generated record review.
