# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/Polytomella_Medium.yaml
- ID: CultureMech:000186
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 675df02f1e1d671655287d9de0ebc4de067cc1cb72def9685e6d84bff4299819
- Proposed SHA256: cd5850bc7d73a9623af6cda491368aaa6a0c823f0d8c44322e465a739436234a
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / dH2O | ingredients[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "Bring total volume to 1 L with dH2O.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Remove the unsupported final-fraction slot while retaining the source preparation input in notes. Not applied. |
| ingredients[1].concentration / Yeast extract | ingredients[1].concentration | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "1 g/L", "component_snippet": "Yeast extract(Bacto, Difco)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| ingredients[2].concentration / Tryptone | ingredients[2].concentration | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "1 g/L", "component_snippet": "Tryptone(Sigma T 9410)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| ingredients[3].concentration / Sodium acetate | ingredients[3].concentration | {"value": "24.4", "unit": "MILLIMOLAR"} | {"value": "24.4", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "24.4 mM", "component_snippet": "Sodium acetate(Fisher BP 333)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| variants[0].modifications / agar | variants[0].modifications | null | ["After making up the liquid recipe to 1 L, add 15 g agar; do not mix."] | add | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "For 1.5% agar medium add 15 grams of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Preserve as an inline optional formulation, not a liquid-parent ingredient. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
