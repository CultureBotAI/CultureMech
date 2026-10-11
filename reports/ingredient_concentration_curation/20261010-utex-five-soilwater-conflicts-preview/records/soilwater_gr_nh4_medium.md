# Soilwater Concentration Conflict Preview

- Record: data/normalized_yaml/algae/soilwater_gr_nh4_medium.yaml
- ID: CultureMech:000226
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 4eab9b70255b6a01077e5a5593afc0d9d2772ff94807b6e8d32cdba47c55bba4
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old value / unit / basis | Proposed disposition | Status | Evidence, locator and calculation | Action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NH4MgPO4 | {"value": "0.04", "unit": "MILLIMOLAR"} | Do not certify 0.04 mM or the anhydrous ontology identity. The recipe instruction/table and specified supplier differ in hydration detail; the supplier gives xH2O and an anhydrous-basis mass. Preserve the 1 mg table input and unquantified pinch instruction as separate evidence until formulation identity is resolved. | conflict | {"reference": "https://utex.org/products/soilwater-gr-plus-nh4-medium", "source_component": "NH4MgPO4(Sigma 529354)", "snippet": "1 mg", "basis_snippet": "For 200 mL Total", "locator": "#recipe, composition table and Directions", "final_concentration_snippet": "0.04 mM", "other_snippet": "Add pinch of NH 4 MgPO4 after pasteurizing.", "calculation": "Conditional diagnostic only: 1 mg / 0.200 L = 5 mg/L input. If anhydrous, 5 / 137.31 = 0.03641395382710654722889811376 mM; if hexahydrate, 5 / 245.404 = 0.02037456602174373685840491598 mM. Neither assumption is selected; final volume and dissolved recovery are not established."} | Preview finding only; authoritative YAML unchanged. |
| solutions[0].concentration / Soilwater: GR+ Medium | {"value": "1000", "unit": "ML_PER_L"} | Retain the literal 200 mL prepared-medium input, but do not assert a 1000 mL/L final fraction after supplement addition. | unsupported | {"reference": "https://utex.org/products/soilwater-gr-plus-nh4-medium", "source_component": "Soilwater: GR+ Medium", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "A named 200 mL recipe and a 200 mL starting carrier do not independently specify final volume after the supplement."} | Preview finding only; authoritative YAML unchanged. |
| variant_modifications[0] / ammonium magnesium phosphate input | Adds 1 mg NH4MgPO4 per 200 mL prepared Soilwater: GR+ Medium. | The table supports this literal input-dose text, not a verified hydrate identity or dissolved final molarity. | evidence_only | {"reference": "https://utex.org/products/soilwater-gr-plus-nh4-medium", "snippet": "1 mg", "basis_snippet": "200 mL", "locator": "#recipe, both composition rows", "calculation": "No conversion; retain table input dose."} | Preview finding only; no evidence applied to YAML. |

## Additional Findings

- The full target YAML and exact source recipe were read. Every current structured concentration and inline variant-dose text is included.
- Source links support recipe input claims, not unrelated salinity, species-growth or culture-condition claims.
- Optional vitamin B12 has no numeric dose. The GR+/NH4 introduction also places carbonate after steaming, whereas the linked GR+ source puts carbonate before steaming. Source-version and optional-formulation distinctions remain unresolved.

## Provenance And Verification

Current recipe HTML is pinned by its original source URL, captured title, access time, file hash, complete recipe text and table cells in review.json. Source type: culture collection page. Discovery: existing record reference. Named authors, publication year and DOI are unknown.

Baseline schema and strict validation pass. Those checks do not validate the scientific assertions. Every quoted recipe excerpt matches the pinned capture. Supplier/ontology observations and conditional arithmetic are documented in the batch manual-source ledger; neither hydration assumption is a recommended replacement.

No authoritative edits, canonical coverage increment, taxa-media associations or applied evidence entries. Formulation/identity decisions, guarded proposals and post-edit checks remain outstanding.
