# YAML Record Review: defined_minimal_medium__c0e50446

- Repository: CultureMech
- Record: `data/merge_yaml/merged/defined_minimal_medium__c0e50446.yaml`
- Started UTC: 2026-09-22T16:47:13Z
- Finished UTC: 2026-09-22T16:47:13Z
- Verdict: needs curation

## Target

Generated bacterial `defined_minimal_medium` record for TOGO M3199.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M3199 through `media_term` and the `TOGO_M3199_Defined_minimal_medium` merge source.

Most ingredient groundings match the printed abbreviations, but the source trace stock includes CuSO4 and the generated record omits it entirely. The TOGO payload itself shows the trace-stock CaCl2 row with a Copper(II) sulfate GMO label, so CaCl2 and CuSO4 must be reconciled from the free-text stock formula rather than from that mislabeled parsed component.

## Evidence

The TOGO M3199 comment gives exact final-medium concentrations for Paracoccus denitrificans: 29 mmol/L Na2HPO4, 11 mmol/L KH2PO4, 10 mmol/L NH4Cl, 0.4 mmol/L MgSO4, 30 mmol/L sodium succinate, 20 mmol/L NaNO3, and 2 mL/L Vishniac and Santer trace elements solution.

The same comment gives the trace stock formula: 130 mmol/L EDTA, 7.64 mmol/L ZnSO4, 25 mmol/L MnCl2, 18.5 mmol/L FeSO4, 0.89 mmol/L `(NH4)6Mo7O24`, 6.4 mmol/L CuSO4, 6.72 mmol/L CoCl2, and 37.4 mmol/L CaCl2.

KH2PO4, NH4Cl, NaNO3, Na2HPO4, sodium succinate, MgSO4, CaCl2, CoCl2, FeSO4, MnCl2, ZnSO4, `(NH4)6Mo7O24`, and EDTA are all schema defaults of `variable` / `VARIABLE`. The only `solutions` entry has an empty `composition`, and its source 2 mL/L final-medium addition has been represented as `2 G_PER_L`.

## Completeness

The record is incomplete for quantitative reuse because every final-medium salt and every trace-stock component is variable despite exact values in the TOGO comment.

The Vishniac and Santer trace elements solution should carry the eight printed stock components, not an empty composition.

`medium_type: COMPLEX` and `composition_type: UNDEFINED` are unsupported by the parsed ingredients and source text; M3199 is chemically defined after the trace stock is expanded.

The merged file is stale relative to the 2026-09-02 duplicate-water repair already present on `data/normalized_yaml/bacterial/TOGO_M3199_Defined_minimal_medium.yaml`: generated distilled water is still `2.0 G_PER_L` with `[Merged 2 duplicates: 1.0, 1.0]`, while the normalized input has been repaired back to 1 liter.

## Findings

- Needs curation: all exact final-medium molar concentrations were lost and defaulted to `VARIABLE`.
- Needs curation: the 2 mL/L trace-solution dose was parsed with the wrong mass unit, `G_PER_L`.
- Needs curation: the trace solution is empty, its component concentrations are stored as variable top-level ingredients, and CuSO4 is missing.
- Needs curation: generated distilled water is stale at 2 l/L relative to the repaired normalized input.
- Needs curation: `COMPLEX` / `UNDEFINED` classification is contradicted by a chemically defined source formula.

## Recommended Edits

- Backfill `data/normalized_yaml/bacterial/TOGO_M3199_Defined_minimal_medium.yaml` from the TOGO free-text comment instead of relying only on parsed component rows.
- Model the Vishniac and Santer trace elements solution as a stock with EDTA, ZnSO4, MnCl2, FeSO4, `(NH4)6Mo7O24`, CuSO4, CoCl2, and CaCl2.
- Preserve the 2 mL/L stock addition using a volume-per-final-volume unit or equivalent structured representation, not `G_PER_L`.
- Restore the final-medium molar concentrations for Na2HPO4, KH2PO4, NH4Cl, MgSO4, sodium succinate, and NaNO3.
- Regenerate `data/merge_yaml/merged/defined_minimal_medium__c0e50446.yaml` so the September duplicate-water repair flows into merged output.
- Reclassify the curated result as defined rather than complex/undefined.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm generated water is 1 l/L, not 2 l/L.
- Confirm the trace solution is non-empty and retains CuSO4.
- Confirm the trace-solution final concentration no longer uses `G_PER_L` for a milliliter addition.

## Additional Notes

M3199 was verified through `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid`.
