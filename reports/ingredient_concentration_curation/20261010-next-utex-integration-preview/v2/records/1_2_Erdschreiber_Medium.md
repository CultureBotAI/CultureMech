# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/1_2_Erdschreiber_Medium.yaml
- ID: CultureMech:000004
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: c4156563715931d73979f2cb762d335466290a23525c4104dc229e5d41886498
- Proposed SHA256: abace84870a563cff878c5e8c414a5f98442b5bb79620e53f14bd188ac173fb2
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Erdschreiber's Medium | solutions[0].concentration | {"value": "500", "unit": "ML_PER_L"} | {"value": "500", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-half-erdschreibers-medium", "snippet": "500 mL", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "500 mL / 1 L total = 500 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |
| ingredients[0].concentration / dH2O | ingredients[0].concentration | {"value": "500", "unit": "ML_PER_L"} | {"value": "500", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-half-erdschreibers-medium", "snippet": "500 mL", "component_snippet": "sterile dH2O", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "500 mL / 1 L total = 500 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
