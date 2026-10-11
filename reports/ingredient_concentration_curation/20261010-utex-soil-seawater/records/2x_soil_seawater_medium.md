# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/2x_soil_seawater_medium.yaml
- ID: CultureMech:000016
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 7d8c38a83e3e6f1452567b49cd9a41417f91b0f4a49a481d110c7691eee9cacd
- Applied SHA256: 43ec2016d58cd4d42d56ff7085963a1df186b1ab9aee264e4cc380a67af298a4
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Green House Soil | ingredients[0].concentration | {"value": "25", "unit": "ML_PER_L"} | {"value": "25", "unit": "ML_PER_L", "per_volume": "per liter of Supplemented Seawater before soil addition"} | correct | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "5 mL/200 mL of Supplemented Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "5 mL soil / 0.2 L Supplemented Seawater = 25 mL per liter of carrier."} | Applied exact reviewed proposal. Retain the soil input-volume ratio with an explicit Supplemented Seawater basis; do not infer the final volume after soil addition. |
| ingredients[1].concentration / CaCO3 | ingredients[1].concentration | {"value": "0.05", "unit": "MILLIMOLAR"} | {"value": "0.05", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "0.05 mM", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Retain the directly printed rounded 0.05 mM, explicitly as a source assertion. The exact source mass dose is 1 mg/200 mL carrier; no independent mass-to-molar or measured-final-volume conversion is certified. |
| solutions[0].concentration / Supplemented Seawater | solutions[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. The source supplies 200 mL carrier before soil addition. Remove the unsupported per-final-liter fraction and retain the literal batch input. |
| solutions[0].composition[0].concentration / Pasteurized Seawater | solutions[0].composition[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "900 mL", "basis_snippet": "Bring total volume to 1 L with Pasteurized Seawater.", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Retain approximate 900 mL initial seawater and makeup to 1 L stock. The exact total seawater volume is not specified. |
| solutions[0].composition[1].concentration / NaCl | solutions[0].composition[1].concentration | {"value": "23", "unit": "G_PER_L"} | {"value": "23", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "23 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Retain the explicit stock g/L amount. The source footnote scopes printed molarity to this stock; no receiving-medium molarity is calculated. |
| solutions[0].composition[2].concentration / MgCl2 x 6 H2O | solutions[0].composition[2].concentration | {"value": "5", "unit": "G_PER_L"} | {"value": "5", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "5 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Retain the explicit stock g/L amount. The source footnote scopes printed molarity to this stock; no receiving-medium molarity is calculated. |
| solutions[0].composition[3].concentration / Na2SO4 | solutions[0].composition[3].concentration | {"value": "4", "unit": "G_PER_L"} | {"value": "4", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "4 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 4; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Applied exact reviewed proposal. Retain the explicit stock g/L amount. The source footnote scopes printed molarity to this stock; no receiving-medium molarity is calculated. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/2x_soil_seawater_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/2x_soil_seawater_medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
