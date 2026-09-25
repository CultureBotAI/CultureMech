# YAML Record Review: 3n_bbm_v_recipe_for_customer_orders

- Repository: CultureMech
- Record: data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml
- Started UTC: 2026-09-21T06:59:20Z
- Finished UTC: 2026-09-21T07:00:28Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml`.
- Stable identifier: `CultureMech:000322`.
- MediaDive identity asserted by the record: `mediadive.medium:C15`, `3N-BBM+V recipe for customer orders`.
- The generated record was merged from `3n_bbm_v.yaml` and `3n_bbm_v_recipe_for_customer_orders.yaml` on fingerprint `018962bbf493a61fc9aa477ded032fd59ba9b0d98f0d769c006ce538acb2d793`.
- Current authoritative owners: `data/normalized_yaml/bacterial/3n_bbm_v.yaml` and `data/normalized_yaml/bacterial/3n_bbm_v_recipe_for_customer_orders.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The MediaDive identity is coherent: the record has `mediadive.medium:C15`, original name `3N-BBM+V recipe for customer orders`, and the expected normalized owner `data/normalized_yaml/bacterial/3n_bbm_v_recipe_for_customer_orders.yaml`.
- The source URL imported into the record, `https://www.ccap.ac.uk/wp-content/uploads/MR_3N_BBM_V_customerorders.pdf`, now returns HTTP 404.
- DSMZ/BacMedia still serves a `text/c15` rendering for `C15: 3N-BBM+V recipe for customer orders`, and a sibling `text/c14` rendering for the C14 parent.
- A gitignore-independent exact search for `mediadive.medium:C15` found only this normalized owner, this generated record, and the media content manifest.
- A gitignore-independent exact search for `MR_3N_BBM_V_customerorders` found only this normalized owner and this generated record.

## Evidence

- The C15 source text lists the main solution with 10 ml `NaNO3 (7.5 g/l stock solution)`, 1 ml each of `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`, `K2HPO4 x 3 H2O`, `KH2PO4`, and `NaCl` stock solutions, 6 ml of `Trace Elements (PIV)`, 1 ml each of vitamin B1 and B12 solutions, and 15 g agar for solid medium.
- The C15 source keeps the same PIV trace-element subrecipe as C14: 0.75 g `Na2-EDTA`, 0.097 g `FeCl3 x 6 H2O`, 0.041 g `MnCl2 x 4 H2O`, 0.005 g `ZnCl2`, 0.002 g `CoCl2 x 6 H2O`, and 0.004 g `Na2 MoO4 x 2 H2O`.
- The C15 source keeps the same vitamin subrecipes as C14: 0.12 g thiamine hydrochloride for vitamin B1 and 0.1 g cyanocobalamine for vitamin B12, with the B12 stock diluted 1:100 before sterile filtration.
- Relative to C14, the C15 customer-order recipe changes the main-solution addition for `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`, `K2HPO4 x 3 H2O`, `KH2PO4`, and `NaCl` from 10 ml to 1 ml while leaving the `NaNO3` addition at 10 ml.

## Completeness

- The record has the source's 15 named rows, so it is count-complete at the flattened ingredient-list level.
- The representation is not semantically complete because every nested stock recipe is flattened into direct `G_PER_L` ingredient concentrations.
- The generated target also loses the C15-specific concentrations. It records `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`, `K2HPO4 x 3 H2O`, `KH2PO4`, and `NaCl` with the C14 parent values, even though the C15 normalized owner records the lower customer-order values for those rows.

## Findings

- BLOCKER: `data/merge_yaml/merged/3n_bbm_v_recipe_for_customer_orders.yaml` merged the C14 parent into the C15 child and emitted C14 values for the five salt/phosphate rows that distinguish C15. The output is identified as `CultureMech:000322` / MediaDive C15 but its ingredient table is no longer the C15 formulation.
- BLOCKER: the normalized C14 and C15 records were correctly linked as `CONCENTRATION_VARIANT` records but should not be merged as duplicate recipes. The merge obliterates the child-side concentration changes it is supposed to preserve.
- MAJOR: the imported C15 owner still encodes stock-solution volumes and stock-solution recipes as direct `G_PER_L` ingredient rows. For example, the source's 1 ml stock additions became 1 g/L rows, while PIV trace components and vitamins are stored at stock concentrations rather than final-medium concentrations.
- MAJOR: `preparation_steps` contain duplicated and reordered nested-subrecipe steps. The PIV autoclave instruction appears twice, and the PIV addition-order instruction follows vitamin filtration in the generated order.
- MINOR: the imported CCAP PDF URL for the C15 customer-order recipe is stale and returns 404.

## Recommended Edits

- Prevent `data/normalized_yaml/bacterial/3n_bbm_v.yaml` and `data/normalized_yaml/bacterial/3n_bbm_v_recipe_for_customer_orders.yaml` from merging. Keep the existing `CONCENTRATION_VARIANT` relationship, but emit C14 and C15 as two separate generated records.
- Re-model the C15 recipe so millilitre rows are stock-solution additions rather than direct g/L solute concentrations.
- If the schema cannot express nested stocks directly, convert each source stock ingredient into its final concentration in the C15 main litre while documenting the stock-solution calculation in notes or preparation metadata.
- De-duplicate and order preparation steps by subrecipe so the PIV addition-order and PIV autoclave instructions remain scoped to `Trace Elements (PIV)`, the thiamine and cyanocobalamine filtration steps remain scoped to their vitamin solutions, and final autoclaving remains scoped to the main solution.
- Replace the stale CCAP PDF URL with a working source URL or add a MediaDive/DSMZ evidence URL for C15.

## Follow-up Checks

- Regenerate merged YAML and confirm that the C15 target is generated from only `3n_bbm_v_recipe_for_customer_orders.yaml`.
- Confirm that regenerated C15 keeps the lower customer-order values for the five rows that differ from C14.
- Re-run schema, strict, reference, and term validation on both regenerated C14 and C15.
- Search all generated records for the merge fingerprint `018962bbf493a61fc9aa477ded032fd59ba9b0d98f0d769c006ce538acb2d793`; after repair, no generated output should still merge the parent and child under that fingerprint.

## Additional Notes

- The C15 source confirms the intended `CONCENTRATION_VARIANT` relationship: C15 is not a spelling duplicate of C14.
