# UTEX Prepared-Blend Concentration Preview

- Record: data/normalized_yaml/algae/waris_soil_extract_medium.yaml
- ID: CultureMech:000241
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 4e87f3ad551f16948722c10d11907707196d581e7351589b6337809abaceaa75
- Proposed SHA256: 208d304651dc28b5a4ab7d43d2e45c80b40dabed7e0bceb121dc2cb80a53253b
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed value / unit / basis | Status | Evidence, locator and calculation | Action |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Waris Medium | {"value": "960", "unit": "ML_PER_L"} | {"value": "960", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/waris-plus-soil-extract-medium", "snippet": "960 mL", "component_snippet": "Waris Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "960 mL / 1 L total = 960 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |
| solutions[1].concentration / Soilwater: GR+ Medium | {"value": "40", "unit": "ML_PER_L"} | {"value": "40", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/waris-plus-soil-extract-medium", "snippet": "40 mL", "component_snippet": "Soilwater: GR+ Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "40 mL / 1 L total = 40 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |

## Provenance

Exact UTEX recipe HTML was inspected, including both amount cells and the explicit one-liter total heading. The proposal records the source URL, title, culture-collection-page type, existing-record-reference discovery mode and 2026-10-10 access date. Named authors, publication year and DOI are unknown. No linked PDF inspection is claimed.

## Verification

Baseline and proposed schema/strict CLI checks pass. Across this six-record preview, 24 commands pass, all twelve amounts match the captured source table and 61 deliberately altered values, units, bases, snippets, identities, old history, unrelated claims or conflict notes are rejected. Inverse comparison preserves every existing numeric quantity and all unrelated record content.

## Unresolved Scope

No conflict was found for these two input amounts and their stated total-volume basis.

The composition and preparation of linked parent media are outside this input-dose review. Existing salinity, growth, ontology and culture-condition claims are unchanged, not newly certified. Guarded application, source-reference CLI validation, installed-code regression and post-edit checks remain outstanding. This preview adds no taxa-media associations, authoritative edits or canonical coverage.
