# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/Trebouxia_Medium.yaml
- ID: CultureMech:000234
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 428d227f59192ed58fb087ee1586587197bffdc21f1190b5143be5bcdf42effa
- Proposed SHA256: b5d933b4953f956ce390dbebe1991f5e8d4c96032a6a8dfdf2fda2bdc7083efe
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Proteose Peptone | ingredients[0].concentration | {"value": "10", "unit": "G_PER_L"} | {"value": "10", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "10 g/L", "component_snippet": "Proteose Peptone(BD 211684)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| ingredients[1].concentration / Glucose | ingredients[1].concentration | {"value": "0.11", "unit": "MOLAR"} | {"value": "0.11", "unit": "MOLAR"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "0.11 M", "component_snippet": "Glucose(BACTO-dextrose or Sigma D 9634)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| solutions[0].concentration / Bristol Medium | solutions[0].notes | {"value": "825", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "Bring total volume to 1 L with the Bristol Medium saved from step 1.", "basis_snippet": "Transfer approximately 825 mL to a 2-L Erlenmeyer flask.", "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Remove the unsupported final-fraction slot while retaining the source preparation input in notes. Not applied. |
| solutions[1].concentration / Soilwater: GR+ Medium | solutions[1].concentration | {"value": "140", "unit": "ML_PER_L"} | {"value": "140", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "140 mL/L", "component_snippet": "Soilwater: GR+ Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| variants[0].modifications / agar | variants[0].modifications | null | ["After making up the liquid recipe to 1 L with Bristol Medium, add 15 g agar; do not mix."] | add | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "For 1.5% (w/v) agar medium: add 15 g of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Preserve as an inline optional formulation, not a liquid-parent ingredient. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
