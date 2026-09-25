# YAML Record Review: saccharolobus_solfataricus_medium__70d92952

- Repository: CultureMech
- Record: `data/merge_yaml/merged/saccharolobus_solfataricus_medium__70d92952.yaml`
- Started UTC: `2026-09-25T03:38:11Z`
- Finished UTC: `2026-09-25T03:38:11Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `saccharolobus_solfataricus_medium__70d92952`, a single-source merge of `data/normalized_yaml/archaea/saccharolobus_solfataricus_medium.yaml`.

The record represents DSMZ/MediaDive Medium 182, `SACCHAROLOBUS SOLFATARICUS MEDIUM`. The direct parent ingredients and pH range are mostly correct, but Allen's trace element solution is flattened into the parent formula.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated identity is correctly grounded to `mediadive.medium:182`, and no false duplicate merge was found for this generated YAML.

## Evidence

DSMZ Medium 182 lists 1 g Yeast extract, 1 g Casamino acids, 3.10 g `KH2PO4`, 2.50 g `(NH4)2SO4`, 0.20 g `MgSO4 x 7 H2O`, 0.25 g `CaCl2 x 2 H2O`, 10 ml Allen's trace element solution, and 1000 ml distilled water. It instructs users to dissolve all compounds except yeast extract and Casamino acids, adjust pH to 4.0-4.2 with 10 N `H2SO4` at room temperature, autoclave, and add yeast extract and Casamino acids from filter-sterilized stock solutions before inoculation.

DSMZ defines Allen's trace element solution as a 1 L stock containing 180 mg `MnCl2 x 4 H2O`, 450 mg `Na2B4O7 x 10 H2O`, 22 mg `ZnSO4 x 7 H2O`, 5 mg `CuCl2 x 2 H2O`, 3 mg `Na2MoO4 x 2 H2O`, 3 mg `VOSO4 x 2 H2O`, 1 mg `CoSO4 x 7 H2O`, and 1000 ml distilled water, with final stock pH adjusted to 2 using 1 N HCl. DSMZ also notes that medium for DSM 5354 should be adjusted to pH 3.5.

## Completeness

The generated record preserves pH 4.0-4.2, all six direct parent ingredient amounts, and the parent autoclave plus post-filtration-addition instruction for yeast extract and Casamino acids.

It loses or corrupts these details:

- The 10 ml/L Allen's trace element solution aliquot is absent.
- Every Allen's trace stock component is flattened into the parent at full 1 L stock concentration.
- The parent 1000 ml distilled water and Allen's trace stock 1000 ml distilled water rows are absent.
- The Allen's trace stock pH 2 adjustment is emitted as a parent preparation step.
- The DSM 5354-specific pH 3.5 note is absent.

## Findings

- `needs curation`: Allen's trace element solution was flattened into the parent formula. DSMZ calls for 10 ml/L of the stock, but the generated record emits all Allen's trace metals as direct parent ingredients at their stock concentrations.
- `needs curation`: Both water rows are missing: the 1000 ml parent distilled water and the 1000 ml Allen's trace solution distilled water.
- `needs curation`: The stock-specific instruction to adjust final solution pH to 2 with 1 N HCl is attached to the generated parent medium rather than to Allen's trace element solution.
- `needs curation`: The DSM 5354 pH 3.5 note is missing, so strain-specific acidification is not recoverable.
- `pass with minor issues`: The DSMZ 182 identity, parent pH 4.0-4.2, and direct parent amounts for yeast extract, Casamino acids, phosphate, ammonium sulfate, magnesium sulfate, and calcium chloride are otherwise correct.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/saccharolobus_solfataricus_medium__70d92952.yaml`; fix `data/normalized_yaml/archaea/saccharolobus_solfataricus_medium.yaml`, then rerun the merge.
- Preserve Allen's trace element solution as a nested stock with a 10 ml parent aliquot.
- Scope `MnCl2 x 4 H2O`, `Na2B4O7 x 10 H2O`, `ZnSO4 x 7 H2O`, `CuCl2 x 2 H2O`, `Na2MoO4 x 2 H2O`, `VOSO4 x 2 H2O`, and `CoSO4 x 7 H2O` under Allen's trace element solution.
- Restore parent distilled water and Allen's trace stock distilled water in their source scopes.
- Attach the pH 2 adjustment to the Allen's trace solution, not to the final parent medium.
- Preserve the DSM 5354-specific pH 3.5 note where the schema permits.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/archaea/saccharolobus_solfataricus_medium.yaml`.
- Regenerate `data/merge_yaml/merged/saccharolobus_solfataricus_medium__70d92952.yaml` and verify that Allen's trace element solution survives as a 10 ml/L aliquot.
- Verify that no Allen's trace-metal row is emitted as a direct parent ingredient.
- Verify that the pH 2 adjustment is attached only to Allen's trace element solution.
- Run an exact ignored-file-inclusive search for `mediadive.medium:182` and `saccharolobus_solfataricus_medium` before changing duplicate links.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. This record and `saccharolobus_mt_4_medium` exercise the same nested-stock failure with different DSMZ trace solutions.
