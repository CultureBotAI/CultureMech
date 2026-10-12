# Soilwater Concentration Conflict Preview

- Record: data/normalized_yaml/algae/Soilwater_VT_Medium.yaml
- ID: CultureMech:000231
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: da78bff0e7a4e2e40d437244abc6bd46fdfcfbdae254af1d5015b87ebf2bcbe4
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed disposition | Status | Evidence, locator and calculation | Action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Vermont Soil | {"value": "1 tsp per 200 mL", "unit": "VARIABLE"} | Retain the literal one-teaspoon preparation input in notes/evidence; do not encode it as a variable concentration or convert it to mass. A volumetric soil input does not establish final-medium volume. | schema_gap | {"reference": "https://utex.org/products/soilwater-vt-medium", "source_component": "Vermont Soil", "snippet": "1 tsp", "basis_snippet": "For 200 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "No teaspoon-to-mass or final-volume conversion is supported."} | Preview finding only; authoritative YAML unchanged. |
| ingredients[1].concentration / dH2O | {"value": "1000", "unit": "ML_PER_L"} | The source specifies a 200 mL water input mixed with soil, not an independently established 1000 mL/L final water fraction. Propose removing the unsupported fraction while preserving the literal preparation dose. | unsupported | {"reference": "https://utex.org/products/soilwater-vt-medium", "source_component": "dH2O", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "No final volume after adding soil or steaming is specified independently of the heading; do not assume water volume equals final-medium volume."} | Preview finding only; authoritative YAML unchanged. |

## Additional Findings

- The full target YAML and exact source recipe were read. Every current structured concentration and inline variant-dose text is included.
- Source links support recipe input claims, not unrelated salinity, species-growth or culture-condition claims.
- The source describes a rise to approximately 95 C in 15 minutes, then just over 98 C for three hours on each of two days. Current preparation steps omit these temperature details; no new temperature is applied.

## Provenance And Verification

Current recipe HTML is pinned by its original source URL, captured title, access time, file hash, complete recipe text and table cells in review.json. Source type: culture collection page. Discovery: existing record reference. Named authors, publication year and DOI are unknown.

Baseline schema and strict validation pass. Those checks do not validate the scientific assertions. Every quoted recipe excerpt matches the pinned capture. Supplier/ontology observations and conditional arithmetic are documented in the batch manual-source ledger; neither hydration assumption is a recommended replacement.

No authoritative edits, canonical coverage increment, taxa-media associations or applied evidence entries. Formulation/identity decisions, guarded proposals and post-edit checks remain outstanding.
