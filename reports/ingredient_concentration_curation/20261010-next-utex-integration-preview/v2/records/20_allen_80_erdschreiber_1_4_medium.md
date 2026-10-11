# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/20_allen_80_erdschreiber_1_4_medium.yaml
- ID: CultureMech:000013
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 7890042606e4f7e79a28e71b7a631c17ec120c864817285fd66f18b7c20b9b60
- Proposed SHA256: 235da515815b371eeb0989fb3a71bf54edf89035eea357889fa2bdca004d68a1
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Allen Medium | solutions[0].concentration | {"value": "200", "unit": "ML_PER_L"} | {"value": "200", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/20-percent-allen-plus-80-percent-erdschreibers-medium", "snippet": "200 mL", "component_snippet": "Allen Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "200 mL / 1 L total = 200 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |
| solutions[1].concentration / Erdschreiber's Medium | solutions[1].concentration | {"value": "800", "unit": "ML_PER_L"} | {"value": "800", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/20-percent-allen-plus-80-percent-erdschreibers-medium", "snippet": "800 mL", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "800 mL / 1 L total = 800 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
