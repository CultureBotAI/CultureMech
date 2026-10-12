# UTEX Prepared-Blend Concentration Preview

- Record: data/normalized_yaml/algae/Bold_1NV_Erdshreiber_4_1_Medium.yaml
- ID: CultureMech:000031
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 82d181fe535bab22595f3e25c29fe2b53a5df71006a9ab475adb50b0f13b9097
- Proposed SHA256: 6b3d06728869016dc4f2f8acdfa29b80b54cd6658d625059e44335fd902f927d
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed value / unit / basis | Status | Evidence, locator and calculation | Action |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Bold 1NV Medium | {"value": "800", "unit": "ML_PER_L"} | {"value": "800", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bold-1nv-erdschreibers-four-to-one-medium", "snippet": "800 mL/L", "component_snippet": "Bold 1NV Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "800 mL / 1 L total = 800 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |
| solutions[1].concentration / Erdschreiber's Medium | {"value": "200", "unit": "ML_PER_L"} | {"value": "200", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bold-1nv-erdschreibers-four-to-one-medium", "snippet": "200 mL/L", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "200 mL / 1 L total = 200 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Retain quantity and attach exact source evidence. Not applied. |

## Provenance

Exact UTEX recipe HTML was inspected, including both amount cells and the explicit one-liter total heading. The proposal records the source URL, title, culture-collection-page type, existing-record-reference discovery mode and 2026-10-10 access date. Named authors, publication year and DOI are unknown. No linked PDF inspection is claimed.

## Verification

Baseline and proposed schema/strict CLI checks pass. Across this six-record preview, 24 commands pass, all twelve amounts match the captured source table and 61 deliberately altered values, units, bases, snippets, identities, old history, unrelated claims or conflict notes are rejected. Inverse comparison preserves every existing numeric quantity and all unrelated record content.

## Unresolved Scope

No conflict was found for these two input amounts and their stated total-volume basis.

The composition and preparation of linked parent media are outside this input-dose review. Existing salinity, growth, ontology and culture-condition claims are unchanged, not newly certified. Guarded application, source-reference CLI validation, installed-code regression and post-edit checks remain outstanding. This preview adds no taxa-media associations, authoritative edits or canonical coverage.
