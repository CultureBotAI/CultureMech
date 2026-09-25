# YAML Record Review: modified_nms_medium_4

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_nms_medium_4.yaml
- Started UTC: 2026-09-24T12:40:24Z
- Finished UTC: 2026-09-24T12:41:07Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:015872`, `modified_nms_medium_4`, generated from `data/normalized_yaml/bacterial/JCM_J1465_MODIFIED_NMS_MEDIUM_4.yaml`.
- The record represents JCM `GRMD=1465`, named `MODIFIED NMS MEDIUM-4`.
- The generated record was compared with the primary JCM `GRMD=1465` recipe.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` exited 0 with no diagnostics.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- JCM `GRMD=1465` identifies Modified NMS Medium-4 and the generated record points to that source.
- A gitignore-independent exact search for the JCM medium identifier found one maintained YAML record, `data/normalized_yaml/bacterial/JCM_J1465_MODIFIED_NMS_MEDIUM_4.yaml`, plus this generated record and index metadata.
- Several stock-solution salts are incompletely or loosely grounded: Na2HPO4 x 12 H2O lacks a primary `term`, CoCl2 x 6 H2O and NiCl2 x 6 H2O are linked to non-hydrate chloride labels, and MnCl2 x 4 H2O lacks an ontology grounding.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists a basal medium containing 1.0 g KNO3, 1.0 g MgSO4 x 7 H2O, 0.2 g CaCl2 x 2 H2O, 3.8 mg Fe(III)-EDTA, 0.26 mg Na2MoO4 x 2 H2O, 0.72 g Na2HPO4 x 12 H2O, 0.26 g KH2PO4, 1.0 ml Trace element solution, and 1.0 L distilled water.
- JCM's Trace element solution is a separate stock containing CuSO4 x 5 H2O, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, H3BO2, CoCl2 x 6 H2O, EDTA x 2Na, MnCl2 x 4 H2O, NiCl2 x 6 H2O, and 1.0 L distilled water.
- JCM instructs mixing and autoclaving the basal medium, distributing it into serum bottles with at least 80 percent gas phase by volume, and replacing the gas phase with an 82:18 air-methane gas mixture.

## Completeness

- The basal salts, phosphate pair, Fe(III)-EDTA, Na2MoO4 x 2 H2O, and gas-exchange instruction are present.
- The 1.0 ml Trace element solution addition is present, but the trace stock components are also flattened into the top-level ingredient list.
- The basal 1.0 L distilled water and the trace-stock 1.0 L distilled water rows collapsed to one `1.0` `ML_PER_L` row, so the recipe has a milliliter-per-liter value where the JCM source has liters of solvent in two different scopes.
- The trace stock has no `solutions` subrecord that keeps CuSO4 x 5 H2O, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, H3BO2, CoCl2 x 6 H2O, EDTA x 2Na, MnCl2 x 4 H2O, NiCl2 x 6 H2O, and its water under the stock recipe.

## Findings

- Blocker: Trace element solution stock members are flattened into final top-level ingredients at their 1 L stock concentrations even though JCM adds only 1.0 ml of that stock to the basal medium. For example, the generated recipe lists 0.2 g/L CuSO4 x 5 H2O, 0.5 g/L FeSO4 x 7 H2O, and 0.4 g/L ZnSO4 x 7 H2O as final-medium rows.
- Blocker: the 1.0 L distilled water rows from the basal medium and trace stock were both imported as `1.0` `ML_PER_L`; the deduplication pass then removed one identical malformed water row, masking one stock-scope solvent row while retaining the wrong unit.
- Major: the generated record simultaneously retains `Trace element solution (see below)` as a 1.0 ml/L addition and flattens the solution's internal components, so consumers cannot distinguish the actual stock addition from the stock formula.
- Minor: several hydrated salts need grounding cleanup after the solution hierarchy is fixed: Na2HPO4 x 12 H2O lacks a primary `term`, CoCl2 x 6 H2O and NiCl2 x 6 H2O are linked to non-hydrate salts, and MnCl2 x 4 H2O is ungrounded.

## Recommended Edits

- Preserve the JCM Trace element solution as a nested stock recipe, with its members and 1.0 L distilled water scoped under the stock.
- Keep the main 1.0 ml/L Trace element solution addition as the top-level row and do not also flatten its stock members into final ingredients.
- Correct the basal distilled water row to preserve the source 1.0 L volume.
- Add primary ontology grounding for the hydrated phosphate, cobalt, manganese, and nickel salts after the record structure is corrected.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting direct JCM solution handling.
- Recompare the regenerated record against JCM `GRMD=1465`, especially the 1.0 ml Trace element solution addition, the trace stock contents, both 1.0 L water rows, and the 82:18 air-methane instruction.
- Confirm that generated YAML still has exactly one JCM `GRMD=1465` record after regeneration.

## Additional Notes

None found.
