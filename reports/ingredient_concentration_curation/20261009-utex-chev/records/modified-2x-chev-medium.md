# UTEX CHEV Ingredient Amount Review

- Record: data/normalized_yaml/algae/Modified_2X_CHEV_Medium.yaml
- ID: CultureMech:000177
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: e6878b8e043ec2ccf66673bd0c1af711f48225f9c167e5be6c58c71b8684e238
- Result SHA256: e71183217f8fe1eb19e0c74bf971eb9164e7088f45c2f5ebe32c89c36becd356

## Source And Scope

Modified 2X CHEV Medium; https://utex.org/products/modified-2x-chev-medium. Publisher: UTEX Culture Collection of Algae. Source type: culture_collection_page; discovery: existing_record_reference; accessed 2026-10-09. Named authors and web publication year: unknown. HTML SHA256: dcb70eade6199673085be0e0e321f74036ce5a6881d3a6654174f85ca14be73d. Linked PDF: https://web.biosci.utexas.edu/utex/Media%20PDF/modified-2x-chev-medium.pdf; SHA256: 79036dace87ee7da9a71f463ac6ce3a4fa87b19c0605fb6956166fd1bc1c0df1. The recipe table, directions and PDF page 1 were inspected. All direct ingredient and stock-addition claims in this record are listed below. Referenced F/2 composition was not concentration-reviewed in this batch. See the [pinned source ledger](../source-review.json).

## Every Amount Claim

L values are absolute volumes of inputs, not per-liter concentrations. 15 mL is tube capacity, not evidence of the final volume. A notes-only evidence entry does not verify its retained concentration.

| Field / ingredient | Old | Applied | Status | Action | PURL, exact snippet, locator, basis and calculation |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0] / dH2O | {"unit": "ML_PER_L", "value": "800"} | {"unit": "ML_PER_L", "value": "800"} | evidence_only | retain amount; add concentration evidence | {"explanation": "Supports ingredients[0].concentration and notes (dH2O) in UTEX:modified-2x-chev-medium. Locator: recipe table, row 3, Component=Sterile dH 2 O, Amount column; Directions specify the preparation basis. The Directions heading explicitly defines a 1 L total preparation; 800 mL / 1 L = 800 mL/L. This verifies a volume of prepared input medium or water, not the F/2 formulation or organism growth. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/modified-2x-chev-medium", "snippet": "800 mL", "supports": "SUPPORT"} |
| solutions[0] / F/2 Medium | {"unit": "ML_PER_L", "value": "200"} | {"unit": "ML_PER_L", "value": "200"} | evidence_only | retain amount; add concentration evidence | {"explanation": "Supports solutions[0].concentration and notes (F/2 Medium) in UTEX:modified-2x-chev-medium. Locator: recipe table, row 1, Component=F/2 Medium, Amount column; Directions specify the preparation basis. The Directions heading explicitly defines a 1 L total preparation; 200 mL / 1 L = 200 mL/L. This verifies a volume of prepared input medium or water, not the F/2 formulation or organism growth. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/modified-2x-chev-medium", "snippet": "200 mL", "supports": "SUPPORT"} |

## Remaining Issues

- L quantities are absolute input volumes per single-tube preparation, not final concentrations. Vessel capacity and summed liquid inputs do not establish final volume.
- The three fixed drop counts retain unresolved legacy VARIABLE encodings; their new evidence supports notes only. No drop-volume estimate is introduced.
- Modified CHEV's 1 mg/12 mL versus 0.5 mM source discrepancy remains unresolved. Its new evidence supports the discrepancy note, not the retained molarity.
- Referenced F/2 composition, chemical mappings, preparation, growth conditions and relationships are preserved, not newly certified. No new taxa-media associations.
- Existing relationship notes that describe a 12 mL liquid fill are not evidence of a measured final volume and are not newly certified.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json) and [checkpoint](../validation.json) record gate results. Pending/failed checks are not passes. No taxa-media associations were added.
