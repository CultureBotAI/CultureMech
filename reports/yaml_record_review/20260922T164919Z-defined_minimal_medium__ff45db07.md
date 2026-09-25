# YAML Record Review: defined_minimal_medium__ff45db07

- Repository: CultureMech
- Record: `data/merge_yaml/merged/defined_minimal_medium__ff45db07.yaml`
- Started UTC: 2026-09-22T16:49:19Z
- Finished UTC: 2026-09-22T16:49:19Z
- Verdict: needs curation

## Target

Generated bacterial `defined_minimal_medium` record for TOGO M3202.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M3202 through `media_term` and the `TOGO_M3202_Defined_minimal_medium` merge source.

Most ingredient groundings match their printed formulas. CuSO4 is present and grounded to copper(II) sulfate, but CaCl2 is absent even though the source trace-stock formula includes 37.4 mmol/liter CaCl2.

`N2` is correctly grounded to dinitrogen, but it is a sparging gas and an anoxic cultivation condition in the source, not a defined ingredient at a variable mass concentration.

## Evidence

The TOGO M3202 comment gives exact final-medium concentrations: 29 mmol/liter Na2HPO4, 11 mmol/liter KH2PO4, 10 mmol/liter NH4Cl, 0.4 mmol/liter MgSO4, 30 mmol/liter sodium succinate, 20 mmol/liter NaNO3 or 3 mmol/liter NaNO2, and 2 ml/liter Vishniac and Santer trace elements solution.

The same comment gives the trace stock formula: 130 mmol/liter EDTA, 7.64 mmol/liter ZnSO4, 25 mmol/liter MnCl2, 18.5 mmol/liter FeSO4, 0.89 mmol/liter `(NH4)6Mo7O24`, 6.4 mmol/liter CuSO4, 6.72 mmol/liter CoCl2, and 37.4 mmol/liter CaCl2.

The source also states that anaerobic batch cultures were sparged with N2 for 10 minutes to impose an anoxic environment and were incubated statically at 30 C. The generated record stores `N2` as a normal top-level ingredient with `variable` / `VARIABLE`.

KH2PO4, NH4Cl, NaNO3, Na2HPO4, sodium succinate, MgSO4, NaNO2, N2, CuSO4, CoCl2, FeSO4, MnCl2, ZnSO4, `(NH4)6Mo7O24`, and EDTA all have schema-default `variable` concentrations. The `Vishniac and Santer trace elements solution` entry is empty and also variable.

## Completeness

The record is incomplete for quantitative reuse because every exact final-medium and trace-stock amount from the source comment has been defaulted to `VARIABLE`.

The source's NaNO3 and NaNO2 alternatives are encoded together as simultaneous top-level ingredients.

The stock solution should include CaCl2 and all other trace components under `solutions[].composition`; its current composition is empty.

`medium_type: COMPLEX` and `composition_type: UNDEFINED` are unsupported by the parsed ingredients and source text; the source formula is chemically defined after the trace stock is expanded.

The merged file is stale relative to the 2026-09-02 duplicate-water repair already present on `data/normalized_yaml/bacterial/TOGO_M3202_Defined_minimal_medium.yaml`: generated distilled water is still `2.0 G_PER_L` with `[Merged 2 duplicates: 1.0, 1.0]`, while the normalized input has been repaired back to 1 liter.

## Findings

- Needs curation: all exact final-medium molar concentrations and the 2 ml/liter trace-stock addition were lost and defaulted to `VARIABLE`.
- Needs curation: the trace solution is empty, its component concentrations are stored as variable top-level ingredients, and CaCl2 is missing.
- Needs curation: mutually exclusive NaNO3 and NaNO2 alternatives are modeled as simultaneous ingredients.
- Needs curation: N2 sparging is modeled as a variable ingredient instead of a 10-minute anoxic sparge.
- Needs curation: generated distilled water is stale at 2 l/L relative to the repaired normalized input.
- Needs curation: `COMPLEX` / `UNDEFINED` classification is contradicted by a chemically defined source formula.

## Recommended Edits

- Backfill `data/normalized_yaml/bacterial/TOGO_M3202_Defined_minimal_medium.yaml` from the TOGO free-text comment.
- Represent the NaNO3 and NaNO2 formulas as alternatives or sibling media variants.
- Model the Vishniac and Santer trace elements solution as a stock with EDTA, ZnSO4, MnCl2, FeSO4, `(NH4)6Mo7O24`, CuSO4, CoCl2, and CaCl2, and dose it into the final medium at 2 ml/liter.
- Move `N2` out of `ingredients` into a preparation or cultivation-condition representation for the 10-minute sparge.
- Preserve static 30 C anaerobic batch incubation as source-backed growth-condition evidence if this record is expected to capture cultivation conditions.
- Regenerate `data/merge_yaml/merged/defined_minimal_medium__ff45db07.yaml` so the September duplicate-water repair flows into merged output.
- Reclassify the curated result as defined rather than complex/undefined.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm generated water is 1 l/L, not 2 l/L.
- Confirm CaCl2 is present in the trace stock.
- Confirm NaNO3 and NaNO2 no longer appear as simultaneous required ingredients in the same recipe.
- Confirm N2 is no longer a variable concentration row in `ingredients`.

## Additional Notes

M3202 was verified through `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid`.
