# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml
- ID: CultureMech:000019
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 98fc2daa7e4f8fb3c3220696aff4f26c294316c72c7b99e8a9166808bd50d7c7
- Proposed SHA256: f475c2abb8d6727f39f076ade2f2cd5dfbc0f29f5b9fb6695af000ac9f168e1b
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Natural sea-salt | ingredients[0].concentration | {"value": "15", "unit": "G_PER_L"} | {"value": "15", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "15 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Retain the source-explicit 15 g/L sea-salt dose; scope to the stated recipe, without treating the input liter as an independently measured final volume. Not applied. |
| ingredients[1].concentration / Agar | ingredients[1].concentration | {"value": "15", "unit": "G_PER_L"} | {"value": "15", "unit": "G_PER_L", "per_volume": "per liter of prepared Soil+Seawater Medium before salt and agar additions"} | correct | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "Add 15 g of agar into the flask; do not mix.", "basis_snippet": "Filter 1 L of Soil+Seawater Medium to remove soil particles.", "locator": "Directions step 3 (agar addition); step 1 (prepared-medium input volume)", "calculation": "15 g agar / 1 L prepared input medium = 15 g per liter of input medium, not a newly measured final-volume concentration."} | Keep the 15 g per liter-of-prepared-medium dose with an explicit input-volume basis. Preserve the do-not-mix instruction before autoclaving. Not applied. |
| solutions[0].concentration / Soil+Seawater Medium | solutions[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "1 L", "basis_snippet": "Filter 1 L of Soil+Seawater Medium to remove soil particles.", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Remove the unsupported 1000 mL/L final-medium fraction while preserving the literal 1 L carrier input and internal medium reference. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
