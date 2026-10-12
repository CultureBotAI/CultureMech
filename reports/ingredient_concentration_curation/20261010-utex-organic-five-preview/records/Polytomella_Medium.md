# UTEX Ingredient Concentration Preview

- Record: data/normalized_yaml/algae/Polytomella_Medium.yaml
- ID: CultureMech:000186
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 675df02f1e1d671655287d9de0ebc4de067cc1cb72def9685e6d84bff4299819
- Proposed SHA256: aed27722b73d677002370710daba931afc7304861e1b86e0e40853e8b6216852
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed value / unit / basis | Status | Source, snippet, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / dH2O | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "Bring total volume to 1 L with dH 2 O.", "basis_snippet": "For 1 L Total", "component_snippet": null, "source_amount": null, "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Remove the unsupported final-fraction slot while retaining the source preparation input in notes. Preview only; authoritative YAML unchanged. |
| ingredients[1].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "1 g/L", "basis_snippet": "For 1 L Total", "component_snippet": "Yeast extract(Bacto, Difco)", "source_amount": "1 g/L", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| ingredients[2].concentration / Tryptone | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "1 g/L", "basis_snippet": "For 1 L Total", "component_snippet": "Tryptone(Sigma T 9410)", "source_amount": "1 g/L", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| ingredients[3].concentration / Sodium acetate | {"value": "24.4", "unit": "MILLIMOLAR"} | {"value": "24.4", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "24.4 mM", "basis_snippet": "For 1 L Total", "component_snippet": "Sodium acetate(Fisher BP 333)", "source_amount": "2 g/L", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| variants[0].modifications / agar | null | ["After making up the liquid recipe to 1 L, add 15 g agar; do not mix."] | add | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "For 1.5% agar medium add 15 grams of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "component_snippet": null, "source_amount": null, "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Preserve as an inline optional formulation, not a liquid-parent ingredient. Preview only; authoritative YAML unchanged. |

## Provenance

The proposal links every changed concentration or preparation-dose assertion to the inspected UTEX source URL and a literal excerpt. Titles, source_type=culture_collection_page, discovery_mode=existing_record_reference and access date 2026-10-10 are preserved in proposed bibliography entries. Named authors, publication year and DOI are unknown; no substitutes are fabricated.

Exact source tables, capture hashes, original and proposed YAML, and calculations are pinned by the batch plan. HTML was inspected; linked PDFs are not claimed to have been checked.

## Verification

Both baseline and proposed schema/strict CLI checks pass for this record. Across five records, all twenty commands pass, seventeen retained numeric fields match the source projection and 82 altered amount/unit/basis, unsupported-slot, agar, snippet, identity, history or unrelated-claim mutants are rejected.

The inverse comparison preserves all prior identifiers, descriptors, culture conditions, preparation steps and history except the explicitly proposed notes, bibliography, evidence, quantity slots and optional variants. No guarded application, installed-code regression or post-edit validation is claimed.

## Unresolved Scope

Malt final volume remains unresolved. Liver-extract strength is an input before heating and filtration, not a measured filtrate strength. Trebouxia total Bristol Medium input and water makeup volumes remain unspecified. These limitations apply only to the relevant record.

Printed molarities are retained as source assertions, not independently recalculated from certified supplier forms. Existing ontology mappings, ingredient roles, growth conditions and linked-medium compositions are unchanged and not newly certified. No taxa-media associations are added. This preview adds zero canonical coverage and zero authoritative edits.
