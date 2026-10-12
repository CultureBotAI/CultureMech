# UTEX Prepared-Blend Concentration Preview

- Record: data/normalized_yaml/algae/1_4_erdschreibers_medium.yaml
- ID: CultureMech:000008
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 099df487d9f9abf468f4443d41326bae186bf856a22ac02e5a2476422ea5780e
- Proposed SHA256: b72e76be2b393f21050d9ec3e7cefb19472e1a1f9c49211d4ce15dc6445375c0
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed value / unit / basis | Status | Evidence, locator and calculation | Action |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Erdschreiber's Medium | {"value": "250", "unit": "ML_PER_L"} | {"value": "250", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-fourth-erdschreibers-medium", "snippet": "250 mL", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "250 mL / 1 L total = 250 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "The UTEX composition table specifies 250 mL Erdschreiber's Medium and 750 mL sterile dH2O for 1 L total (1:3 by input volume), whereas its introductory prose says 1:4. Retained quantities follow the explicit table; the source ratio conflict remains unresolved."} | Retain quantity and attach exact source evidence. Not applied. |
| ingredients[0].concentration / dH2O | {"value": "750", "unit": "ML_PER_L"} | {"value": "750", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-fourth-erdschreibers-medium", "snippet": "750 mL", "component_snippet": "sterile dH2O", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "750 mL / 1 L total = 750 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "The UTEX composition table specifies 250 mL Erdschreiber's Medium and 750 mL sterile dH2O for 1 L total (1:3 by input volume), whereas its introductory prose says 1:4. Retained quantities follow the explicit table; the source ratio conflict remains unresolved."} | Retain quantity and attach exact source evidence. Not applied. |

## Provenance

Exact UTEX recipe HTML was inspected, including both amount cells and the explicit one-liter total heading. The proposal records the source URL, title, culture-collection-page type, existing-record-reference discovery mode and 2026-10-10 access date. Named authors, publication year and DOI are unknown. No linked PDF inspection is claimed.

## Verification

Baseline and proposed schema/strict CLI checks pass. Across this six-record preview, 24 commands pass, all twelve amounts match the captured source table and 61 deliberately altered values, units, bases, snippets, identities, old history, unrelated claims or conflict notes are rejected. Inverse comparison preserves every existing numeric quantity and all unrelated record content.

## Unresolved Scope

The quarter-strength source prose says 1:4, while its table gives 250 mL plus 750 mL, or 1:3 by input volume. The proposal retains the table values and explicitly records this unresolved source conflict.

The composition and preparation of linked parent media are outside this input-dose review. Existing salinity, growth, ontology and culture-condition claims are unchanged, not newly certified. Guarded application, source-reference CLI validation, installed-code regression and post-edit checks remain outstanding. This preview adds no taxa-media associations, authoritative edits or canonical coverage.
