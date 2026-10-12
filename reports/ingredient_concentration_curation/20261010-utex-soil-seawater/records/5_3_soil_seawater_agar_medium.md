# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml
- ID: CultureMech:000019
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 98fc2daa7e4f8fb3c3220696aff4f26c294316c72c7b99e8a9166808bd50d7c7
- Applied SHA256: f475c2abb8d6727f39f076ade2f2cd5dfbc0f29f5b9fb6695af000ac9f168e1b
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Natural sea-salt | ingredients[0].concentration | {"value": "15", "unit": "G_PER_L"} | {"value": "15", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "15 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Retain the source-explicit 15 g/L sea-salt dose; scope to the stated recipe, without treating the input liter as an independently measured final volume. |
| ingredients[1].concentration / Agar | ingredients[1].concentration | {"value": "15", "unit": "G_PER_L"} | {"value": "15", "unit": "G_PER_L", "per_volume": "per liter of prepared Soil+Seawater Medium before salt and agar additions"} | correct | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "Add 15 g of agar into the flask; do not mix.", "basis_snippet": "Filter 1 L of Soil+Seawater Medium to remove soil particles.", "locator": "Directions step 3 (agar addition); step 1 (prepared-medium input volume)", "calculation": "15 g agar / 1 L prepared input medium = 15 g per liter of input medium, not a newly measured final-volume concentration."} | Applied exact reviewed proposal. Keep the 15 g per liter-of-prepared-medium dose with an explicit input-volume basis. Preserve the do-not-mix instruction before autoclaving. |
| solutions[0].concentration / Soil+Seawater Medium | solutions[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "1 L", "basis_snippet": "Filter 1 L of Soil+Seawater Medium to remove soil particles.", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Remove the unsupported 1000 mL/L final-medium fraction while preserving the literal 1 L carrier input and internal medium reference. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
