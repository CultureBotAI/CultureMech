# Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/Malt_Medium.yaml
- ID: CultureMech:000175
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: ec1cd464850a1c7eff6e1c8cb8ecac5919216619d9e829597de3041174ee85cd
- Proposed SHA256: ccd72158dddffb1f292d7cede17497b34ce47c56f4e12a60b981b3b873a55ff6
- State: Preview only; authoritative YAML unchanged.
- Proposal: reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/plan.json
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old amount / unit / basis | Proposed amount / unit / basis | Status | Source evidence, locator and calculation | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Malt extract | ingredients[0].concentration | {"value": "67.2", "unit": "G_PER_L"} | {"value": "67.2", "unit": "G_PER_L", "per_volume": "per liter of starting dH2O before malt extract addition"} | correct | {"reference": "https://utex.org/products/malt-medium", "snippet": "33.6 g/500 mL dH2O", "component_snippet": "Malt extract(Sigma M-0383)", "basis_snippet": "For 500 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "33.6 g / 0.500 L starting water = 67.2 g per liter of starting water. The heading says 500 mL total but no final makeup instruction is given; final concentration remains unresolved."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Not applied. |
| variants[0].modifications / agar | variants[0].modifications | null | ["Add 7.5 g agar to the source batch starting with 500 mL dH2O; do not mix. This is an input dose, not a measured final-volume concentration."] | add | {"reference": "https://utex.org/products/malt-medium", "snippet": "For 1.5% agar medium add 7.5 g of agar into the flask; do not mix.", "basis_snippet": "For 500 mL Total", "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Preserve as an inline optional formulation, not a liquid-parent ingredient. Not applied. |

## Provenance

Source URLs identify the exact UTEX recipe pages inspected. Proposed bibliography entries retain source title, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This batch relies on HTML, not claimed inspection of linked PDFs.

## Validation

All four baseline/proposal schema and strict CLI checks pass for this record. The cohort guard passes isolated regression tests and a real-schema dry run with zero writes. Exact snippet and title checks pass against captured canonical recipe HTML. Rendering retains the reviewed quantities, bases and optional variants in HTML DOM checks; no browser visual check is claimed.

Receipts: `reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/mutation-preview-v3/guard-preview/validation.json`, `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/capture-validation.json`, and `reports/ingredient_concentration_curation/20261010-next-utex-integration-preview/v2/render-preview.json`.

All 18 proposal reference CLI commands pass against freshly retrieved public UTEX pages: 69 snippet and 21 title checks, with zero invalid checks. Receipt: `reports/ingredient_concentration_curation/20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json`. Earlier sandbox connection failures remain separately recorded. This record has not been applied or post-edit validated.

## Remaining Scope

No taxa-media association is added. Unrelated growth, organism, role, salinity, ontology and culture-condition assertions are unchanged and not newly certified. Named source conflicts, nonnumeric input doses and preparation-volume limits remain explicit. Guarded application, installed-code regression, canonical reporting and corpus/derived-output checks are still required. The all-record review is incomplete.
