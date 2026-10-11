# UTEX Ingredient Concentration Preview

- Record: data/normalized_yaml/algae/Trebouxia_Medium.yaml
- ID: CultureMech:000234
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 428d227f59192ed58fb087ee1586587197bffdc21f1190b5143be5bcdf42effa
- Proposed SHA256: b5d933b4953f956ce390dbebe1991f5e8d4c96032a6a8dfdf2fda2bdc7083efe
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed value / unit / basis | Status | Source, snippet, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Proteose Peptone | {"value": "10", "unit": "G_PER_L"} | {"value": "10", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "10 g/L", "basis_snippet": "For 1 L Total", "component_snippet": "Proteose Peptone(BD 211684)", "source_amount": "10 g/L", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| ingredients[1].concentration / Glucose | {"value": "0.11", "unit": "MOLAR"} | {"value": "0.11", "unit": "MOLAR"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "0.11 M", "basis_snippet": "For 1 L Total", "component_snippet": "Glucose(BACTO-dextrose or Sigma D 9634)", "source_amount": "20 g/L", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| solutions[0].concentration / Bristol Medium | {"value": "825", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "Bring total volume to 1 L with the Bristol Medium saved from step 1.", "basis_snippet": "Transfer approximately 825 mL to a 2-L Erlenmeyer flask.", "component_snippet": null, "source_amount": null, "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Remove the unsupported final-fraction slot while retaining the source preparation input in notes. Preview only; authoritative YAML unchanged. |
| solutions[1].concentration / Soilwater: GR+ Medium | {"value": "140", "unit": "ML_PER_L"} | {"value": "140", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "140 mL/L", "basis_snippet": "For 1 L Total", "component_snippet": "Soilwater: GR+ Medium", "source_amount": "140 mL/L", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| variants[0].modifications / agar | null | ["After making up the liquid recipe to 1 L with Bristol Medium, add 15 g agar; do not mix."] | add | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "For 1.5% (w/v) agar medium: add 15 g of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "component_snippet": null, "source_amount": null, "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Preserve as an inline optional formulation, not a liquid-parent ingredient. Preview only; authoritative YAML unchanged. |

## Provenance

The proposal links every changed concentration or preparation-dose assertion to the inspected UTEX source URL and a literal excerpt. Titles, source_type=culture_collection_page, discovery_mode=existing_record_reference and access date 2026-10-10 are preserved in proposed bibliography entries. Named authors, publication year and DOI are unknown; no substitutes are fabricated.

Exact source tables, capture hashes, original and proposed YAML, and calculations are pinned by the batch plan. HTML was inspected; linked PDFs are not claimed to have been checked.

## Verification

Both baseline and proposed schema/strict CLI checks pass for this record. Across five records, all twenty commands pass, seventeen retained numeric fields match the source projection and 82 altered amount/unit/basis, unsupported-slot, agar, snippet, identity, history or unrelated-claim mutants are rejected.

The inverse comparison preserves all prior identifiers, descriptors, culture conditions, preparation steps and history except the explicitly proposed notes, bibliography, evidence, quantity slots and optional variants. No guarded application, installed-code regression or post-edit validation is claimed.

## Unresolved Scope

Malt final volume remains unresolved. Liver-extract strength is an input before heating and filtration, not a measured filtrate strength. Trebouxia total Bristol Medium input and water makeup volumes remain unspecified. These limitations apply only to the relevant record.

Printed molarities are retained as source assertions, not independently recalculated from certified supplier forms. Existing ontology mappings, ingredient roles, growth conditions and linked-medium compositions are unchanged and not newly certified. No taxa-media associations are added. This preview adds zero canonical coverage and zero authoritative edits.

This v2 proposal changes only the prospective curation-history claim metadata: preview-only state remains in reports, not in future applied history. Scientific content is identical to v1. The v2 guard passes 78 tests and a real-schema dry run with zero changed and five pending records. All five proposal pages retain seventeen quantities, two bases and four optional variants in HTML content checks, without browser visual verification.
