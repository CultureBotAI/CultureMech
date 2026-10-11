# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/soil_seawater_medium.yaml
- ID: CultureMech:000221
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: c4346d171d8587f36b9645fd5badf8968d8fdb18d14f42e579b3caba33e4a964
- Proposed SHA256: 7f96da69c2c4704e84710195d4ebf793ac99c6d7dbc387c09d60994ed7240ed8
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Green House Soil | ingredients[0].notes | {"value": "variable", "unit": "VARIABLE"} | null | schema_gap | {"reference": "https://utex.org/products/soil-plus-seawater-medium", "snippet": "1 tsp/200 mL of Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | The source specifies a fixed teaspoon dose, not a variable quantity. Remove the misleading VARIABLE concentration and retain the exact dose in notes and evidence; teaspoon size and soil density are not established. Not applied. |
| ingredients[2].concentration / CaCO3 | variants[0].modifications | {"value": "0.005", "unit": "G_PER_L"} | ["Optionally add 1 mg calcium carbonate (Fisher C 64) to the source 200 mL recipe before steaming."] | correct | {"reference": "https://utex.org/products/soil-plus-seawater-medium", "snippet": "1 mg/200 mL of Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No new concentration inferred; the source-literal amount belongs only to the optional formulation."} | Move optional calcium carbonate out of mandatory parent composition into an evidence-backed inline variant. Preserve the literal 1 mg recipe dose, supplier/identity provenance and printed rounded 0.05 mM as a source annotation; do not assert universal carbonate addition. Not applied. |
| ingredients[1].concentration / Pasteurized Seawater | ingredients[1].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/soil-plus-seawater-medium", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Remove the unsupported per-final-liter seawater fraction; preserve the 200 mL carrier input before adding soil and optional carbonate. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v2/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
