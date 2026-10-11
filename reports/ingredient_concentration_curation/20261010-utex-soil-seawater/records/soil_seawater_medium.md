# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/soil_seawater_medium.yaml
- ID: CultureMech:000221
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: c4346d171d8587f36b9645fd5badf8968d8fdb18d14f42e579b3caba33e4a964
- Applied SHA256: 7f96da69c2c4704e84710195d4ebf793ac99c6d7dbc387c09d60994ed7240ed8
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Green House Soil | ingredients[0].notes | {"value": "variable", "unit": "VARIABLE"} | null | schema_gap | {"reference": "https://utex.org/products/soil-plus-seawater-medium", "snippet": "1 tsp/200 mL of Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. The source specifies a fixed teaspoon dose, not a variable quantity. Remove the misleading VARIABLE concentration and retain the exact dose in notes and evidence; teaspoon size and soil density are not established. |
| ingredients[2].concentration / CaCO3 | variants[0].modifications | {"value": "0.005", "unit": "G_PER_L"} | ["Optionally add 1 mg calcium carbonate (Fisher C 64) to the source 200 mL recipe before steaming."] | correct | {"reference": "https://utex.org/products/soil-plus-seawater-medium", "snippet": "1 mg/200 mL of Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No new concentration inferred; the source-literal amount belongs only to the optional formulation."} | Applied exact reviewed proposal. Move optional calcium carbonate out of mandatory parent composition into an evidence-backed inline variant. Preserve the literal 1 mg recipe dose, supplier/identity provenance and printed rounded 0.05 mM as a source annotation; do not assert universal carbonate addition. |
| ingredients[1].concentration / Pasteurized Seawater | ingredients[1].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/soil-plus-seawater-medium", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Remove the unsupported per-final-liter seawater fraction; preserve the 200 mL carrier input before adding soil and optional carbonate. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/soil_seawater_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/soil_seawater_medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
