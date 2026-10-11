# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/1_4_erdschreibers_medium.yaml
- ID: CultureMech:000008
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 099df487d9f9abf468f4443d41326bae186bf856a22ac02e5a2476422ea5780e
- Proposed SHA256: b72e76be2b393f21050d9ec3e7cefb19472e1a1f9c49211d4ce15dc6445375c0
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Erdschreiber's Medium | solutions[0].concentration | {"value": "250", "unit": "ML_PER_L"} | {"value": "250", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-fourth-erdschreibers-medium", "snippet": "250 mL", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "250 mL / 1 L total = 250 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "The UTEX composition table specifies 250 mL Erdschreiber's Medium and 750 mL sterile dH2O for 1 L total (1:3 by input volume), whereas its introductory prose says 1:4. Retained quantities follow the explicit table; the source ratio conflict remains unresolved."} | Retain quantity and attach exact source evidence. Not applied. |
| ingredients[0].concentration / dH2O | ingredients[0].concentration | {"value": "750", "unit": "ML_PER_L"} | {"value": "750", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-fourth-erdschreibers-medium", "snippet": "750 mL", "component_snippet": "sterile dH2O", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "750 mL / 1 L total = 750 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "The UTEX composition table specifies 250 mL Erdschreiber's Medium and 750 mL sterile dH2O for 1 L total (1:3 by input volume), whereas its introductory prose says 1:4. Retained quantities follow the explicit table; the source ratio conflict remains unresolved."} | Retain quantity and attach exact source evidence. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-six-blends-preview/mutation-preview-v1/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.

The quarter-strength source table gives 250 mL plus 750 mL (1:3); its prose says 1:4. The proposal keeps the table amounts and records the unresolved conflict.
