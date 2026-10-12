# UTEX Ingredient Concentration Preview

- Record: data/normalized_yaml/algae/Malt_Medium.yaml
- ID: CultureMech:000175
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: ec1cd464850a1c7eff6e1c8cb8ecac5919216619d9e829597de3041174ee85cd
- Proposed SHA256: ccd72158dddffb1f292d7cede17497b34ce47c56f4e12a60b981b3b873a55ff6
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed value / unit / basis | Status | Source, snippet, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Malt extract | {"value": "67.2", "unit": "G_PER_L"} | {"value": "67.2", "unit": "G_PER_L", "per_volume": "per liter of starting dH2O before malt extract addition"} | correct | {"reference": "https://utex.org/products/malt-medium", "snippet": "33.6 g/500 mL dH2O", "basis_snippet": "For 500 mL Total", "component_snippet": "Malt extract(Sigma M-0383)", "source_amount": "33.6 g/500 mL dH2O", "locator": "#recipe, composition table and Directions", "calculation": "33.6 g / 0.500 L starting water = 67.2 g per liter of starting water. The heading says 500 mL total but no final makeup instruction is given; final concentration remains unresolved."} | Retain the numeric value with exact source evidence and any explicitly stated preparation basis. Preview only; authoritative YAML unchanged. |
| variants[0].modifications / agar | null | ["Add 7.5 g agar to the source batch starting with 500 mL dH2O; do not mix. This is an input dose, not a measured final-volume concentration."] | add | {"reference": "https://utex.org/products/malt-medium", "snippet": "For 1.5% agar medium add 7.5 g of agar into the flask; do not mix.", "basis_snippet": "For 500 mL Total", "component_snippet": null, "source_amount": null, "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Preserve as an inline optional formulation, not a liquid-parent ingredient. Preview only; authoritative YAML unchanged. |

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
