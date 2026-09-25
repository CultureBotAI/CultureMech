# YAML Record Review: saccharolobus_mt_4_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/saccharolobus_mt_4_medium.yaml`
- Started UTC: `2026-09-25T03:36:44Z`
- Finished UTC: `2026-09-25T03:36:44Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `saccharolobus_mt_4_medium`, a single-source merge of `data/normalized_yaml/archaea/saccharolobus_mt_4_medium.yaml`.

The record represents DSMZ/MediaDive Medium `182a`, `SACCHAROLOBUS (MT-4) MEDIUM`. The direct parent ingredients and pH are mostly correct, but the SL-10 trace element stock is flattened into the parent formula.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated identity is correctly grounded to `mediadive.medium:182a`, and no false duplicate merge was found for this generated YAML.

## Evidence

DSMZ Medium 182a lists 2 g Yeast extract, 3.10 g `KH2PO4`, 2.50 g `(NH4)2SO4`, 0.20 g `MgSO4 x 7 H2O`, 0.25 g `CaCl2 x 2 H2O`, 1 ml Trace element solution SL-10, and 1000 ml distilled water. It says to adjust pH at room temperature to 3.5 with 10 N `H2SO4` before autoclaving.

DSMZ defines Trace element solution SL-10 as a 1 L stock containing 10 ml 25% `HCl`, 1.50 g `FeCl2 x 4 H2O`, 70 mg `ZnCl2`, 100 mg `MnCl2 x 4 H2O`, 6 mg `H3BO3`, 190 mg `CoCl2 x 6 H2O`, 2 mg `CuCl2 x 2 H2O`, 24 mg `NiCl2 x 6 H2O`, 36 mg `Na2MoO4 x 2 H2O`, and 990 ml distilled water. Its preparation step dissolves `FeCl2` in HCl, dilutes in water, adds and dissolves the other salts, and makes the stock up to 1000 ml.

## Completeness

The generated record preserves pH 3.5, all five direct gram-scale parent ingredients, and both DSMZ preparation notes.

It loses or corrupts these details:

- The 1 ml/L SL-10 aliquot is absent.
- Every SL-10 stock component is flattened into the parent at full 1 L stock concentration.
- The parent 1000 ml distilled water and SL-10 990 ml distilled water rows are absent.
- The generated `HCl` row is the 25% SL-10 stock component, not a direct parent ingredient.

## Findings

- `needs curation`: Trace element solution SL-10 was flattened into the parent formula. DSMZ calls for 1 ml/L SL-10, but the generated record emits HCl and every SL-10 trace metal as direct parent ingredients at the stock concentrations.
- `needs curation`: Both water rows are missing: the 1000 ml parent distilled water and the 990 ml SL-10 distilled water.
- `needs curation`: The generated record has no structural way to connect the SL-10 preparation step to the SL-10 ingredients; after flattening, the step reads as if it applies to the final Saccharolobus medium.
- `pass with minor issues`: `NiCl2 x 6 H2O` is grounded to CHEBI:34887, `nickel dichloride`; that identifier is too broad for a hexahydrate-labeled row and should either use a hydrate-specific term if one exists or be left ungrounded.
- `pass with minor issues`: The DSMZ 182a identity, pH 3.5, and direct parent amounts for yeast extract, phosphate, ammonium sulfate, magnesium sulfate, and calcium chloride are otherwise correct.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/saccharolobus_mt_4_medium.yaml`; fix `data/normalized_yaml/archaea/saccharolobus_mt_4_medium.yaml`, then rerun the merge.
- Preserve Trace element solution SL-10 as a nested stock with a 1 ml parent aliquot.
- Scope `HCl`, `FeCl2 x 4 H2O`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O` under SL-10.
- Restore parent distilled water and SL-10 distilled water in their source scopes.
- Attach the dissolve-FeCl2-in-HCl preparation step to SL-10, not to the final parent medium.
- Correct or remove the `NiCl2 x 6 H2O` grounding to anhydrous nickel dichloride.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/archaea/saccharolobus_mt_4_medium.yaml`.
- Regenerate `data/merge_yaml/merged/saccharolobus_mt_4_medium.yaml` and verify that SL-10 survives as a 1 ml/L aliquot.
- Verify that no SL-10 trace-metal row is emitted as a direct parent ingredient.
- Verify that parent and SL-10 water rows are scoped separately.
- Run an exact ignored-file-inclusive search for `mediadive.medium:182a` and `saccharolobus_mt_4_medium` before changing duplicate links.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. This is a narrow stock-scope defect; the generated direct parent salts are not themselves off by factors of 1000.
