# YAML Record Review: defined_minimal_medium__39c2e76f

- Repository: CultureMech
- Record: `data/merge_yaml/merged/defined_minimal_medium__39c2e76f.yaml`
- Started UTC: 2026-09-22T16:44:31Z
- Finished UTC: 2026-09-22T16:44:31Z
- Verdict: needs curation

## Target

Generated bacterial `defined_minimal_medium` merge record for TOGO M3200 and TOGO M3201.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M3200 and preserves that primary `media_term`, while the merge audit records both `TOGO_M3200_Defined_minimal_medium` and `TOGO_M3201_Defined_minimal_medium`.

The merge identity is too coarse. M3200 and M3201 share the same base defined-minimal-medium text, but M3201 additionally describes N2O emission culture conditions produced by omitting CuSO4 from the trace elements solution. That copper-free variant should not be silently merged into the parent copper-containing formula.

Most chemical groundings are plausible for the printed abbreviations, but the generated record omits CuSO4 entirely even though the source trace stock gives 6.4 mmol/liter CuSO4. The TOGO component payload also shows a CaCl2 component backed by a Copper(II) sulfate GMO label, so CaCl2 and CuSO4 need source-level reconciliation instead of trusting the imported component row.

## Evidence

The TOGO API comment contains exact final concentrations: 29 mmol/liter Na2HPO4, 11 mmol/liter KH2PO4, 10 mmol/liter NH4Cl, 0.4 mmol/liter MgSO4, 30 mmol/liter sodium succinate, 20 mmol/liter NaNO3 or 3 mmol/liter NaNO2, and 2 ml/liter Vishniac and Santer trace elements solution.

The same comment gives the trace stock itself: 130 mmol/liter EDTA, 7.64 mmol/liter ZnSO4, 25 mmol/liter MnCl2, 18.5 mmol/liter FeSO4, 0.89 mmol/liter `(NH4)6Mo7O24`, 6.4 mmol/liter CuSO4, 6.72 mmol/liter CoCl2, and 37.4 mmol/liter CaCl2.

None of those numeric concentrations are represented. KH2PO4, NH4Cl, NaNO3, Na2HPO4, sodium succinate, MgSO4, NaNO2, CaCl2, CoCl2, FeSO4, MnCl2, ZnSO4, `(NH4)6Mo7O24`, and EDTA all carry the schema default `variable` / `VARIABLE`, and the only `solutions` entry has an empty `composition` plus a `VARIABLE` dose.

The source text says 20 mmol/liter NaNO3 **or** 3 mmol/liter NaNO2. The generated ingredient list includes both nitrogen oxides as simultaneous top-level ingredients, losing the variant relationship.

## Completeness

The record is incomplete for quantitative reuse because every source concentration other than water has been defaulted to `VARIABLE`.

The Vishniac and Santer trace elements solution should be a complete stock solution, not an empty solution placeholder plus free top-level trace salts.

`medium_type: COMPLEX` and `composition_type: UNDEFINED` are unsupported by the parsed ingredients and source text; the source describes a chemically defined formula and a fully specified trace stock.

The merged file is stale relative to the 2026-09-02 duplicate-water repair already present on both normalized TOGO inputs: generated distilled water is still `2.0 G_PER_L` with `[Merged 2 duplicates: 1.0, 1.0]`, while each normalized source has been repaired back to 1 liter.

## Findings

- Needs curation: all final-medium molar concentrations and the 2 ml/liter trace-solution dose were lost and defaulted to `VARIABLE`.
- Needs curation: the trace stock is empty, its eight source molar concentrations are also defaulted to `VARIABLE`, and CuSO4 is absent.
- Needs curation: mutually exclusive NaNO3 and NaNO2 alternatives are modeled as simultaneous ingredients.
- Needs curation: M3201's copper-free N2O condition is merged into the parent M3200 recipe with no representation of CuSO4 omission.
- Needs curation: generated distilled water is stale at 2 l/L relative to the repaired normalized inputs.
- Needs curation: `COMPLEX` / `UNDEFINED` classification is contradicted by a chemically defined source formula.

## Recommended Edits

- Backfill `data/normalized_yaml/bacterial/TOGO_M3200_Defined_minimal_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M3201_Defined_minimal_medium.yaml` from the TOGO comment rather than relying only on parsed component rows.
- Represent the NaNO3 and NaNO2 formulas as alternatives or sibling media variants so one generated recipe does not contain both.
- Model the Vishniac and Santer trace elements solution as a stock with EDTA, ZnSO4, MnCl2, FeSO4, `(NH4)6Mo7O24`, CuSO4, CoCl2, and CaCl2, and dose it into the final medium at 2 ml/liter.
- Preserve the M3201 copper-free N2O condition explicitly, likely as a variant that omits CuSO4 from that trace solution.
- Regenerate `data/merge_yaml/merged/defined_minimal_medium__39c2e76f.yaml` so the September duplicate-water repair flows into merged output.
- Reclassify the curated result as defined rather than complex/undefined.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm generated water is 1 l/L, not 2 l/L.
- Confirm CuSO4 is present in the standard stock and intentionally absent only in the copper-free N2O variant.
- Confirm NaNO3 and NaNO2 no longer appear as simultaneous required ingredients in the same recipe.

## Additional Notes

M3200 and M3201 were verified through `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid`.
