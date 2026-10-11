# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/2x_soil_seawater_medium.yaml
- ID: CultureMech:000016
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 7d8c38a83e3e6f1452567b49cd9a41417f91b0f4a49a481d110c7691eee9cacd
- Proposed SHA256: 43ec2016d58cd4d42d56ff7085963a1df186b1ab9aee264e4cc380a67af298a4
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Green House Soil | ingredients[0].concentration | {"value": "25", "unit": "ML_PER_L"} | {"value": "25", "unit": "ML_PER_L", "per_volume": "per liter of Supplemented Seawater before soil addition"} | correct | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "5 mL/200 mL of Supplemented Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "5 mL soil / 0.2 L Supplemented Seawater = 25 mL per liter of carrier."} | Retain the soil input-volume ratio with an explicit Supplemented Seawater basis; do not infer the final volume after soil addition. Not applied. |
| ingredients[1].concentration / CaCO3 | ingredients[1].concentration | {"value": "0.05", "unit": "MILLIMOLAR"} | {"value": "0.05", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "0.05 mM", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Retain the directly printed rounded 0.05 mM, explicitly as a source assertion. The exact source mass dose is 1 mg/200 mL carrier; no independent mass-to-molar or measured-final-volume conversion is certified. Not applied. |
| solutions[0].concentration / Supplemented Seawater | solutions[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No numerical conversion applied"} | The source supplies 200 mL carrier before soil addition. Remove the unsupported per-final-liter fraction and retain the literal batch input. Not applied. |
| solutions[0].composition[0].concentration / Pasteurized Seawater | solutions[0].composition[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "900 mL", "basis_snippet": "Bring total volume to 1 L with Pasteurized Seawater.", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Retain approximate 900 mL initial seawater and makeup to 1 L stock. The exact total seawater volume is not specified. Not applied. |
| solutions[0].composition[1].concentration / NaCl | solutions[0].composition[1].concentration | {"value": "23", "unit": "G_PER_L"} | {"value": "23", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "23 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Retain the explicit stock g/L amount. The source footnote scopes printed molarity to this stock; no receiving-medium molarity is calculated. Not applied. |
| solutions[0].composition[2].concentration / MgCl2 x 6 H2O | solutions[0].composition[2].concentration | {"value": "5", "unit": "G_PER_L"} | {"value": "5", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "5 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Retain the explicit stock g/L amount. The source footnote scopes printed molarity to this stock; no receiving-medium molarity is calculated. Not applied. |
| solutions[0].composition[3].concentration / Na2SO4 | solutions[0].composition[3].concentration | {"value": "4", "unit": "G_PER_L"} | {"value": "4", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "4 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 4; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Retain the explicit stock g/L amount. The source footnote scopes printed molarity to this stock; no receiving-medium molarity is calculated. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
