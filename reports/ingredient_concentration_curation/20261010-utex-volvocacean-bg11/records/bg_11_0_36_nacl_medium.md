# Ingredient Concentration Follow-Up

- Record: data/normalized_yaml/algae/bg_11_0_36_nacl_medium.yaml
- ID: CultureMech:000026
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 28d5909ae33d9433ef191e63d871bc967d53ad9a652c5a6fa2d96de9be7eae6d
- State: Applied locally; unresolved claims remain explicit.

| Field / ingredient | Old amount / unit / basis | Current amount / unit / basis | Status | Evidence | Calculation / action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "0.062", "unit": "MOLAR"} | {"value": "0.062", "unit": "MOLAR"} | evidence_only | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "0.062 M", "locator": "#recipe: component table and Directions"} | Retain the printed molarity; source separately states 3.6 g/L. No exact equivalence calculated. Applied and read back exactly. |
| solutions[0].concentration / BG-11 recipe base | {"value": "1000", "unit": "ML_PER_L"} | null | correct | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "through step one.", "locator": "#recipe: component table and Directions"} | Remove an unsupported carrier dose; preserve the base link and table/procedure distinction without inventing a replacement. Applied and read back exactly. |
| variant_modifications[0]; parent_media.notes / NaCl supplement | Adds 3.6 g/L NaCl to prepared BG-11 Medium. | Adds 3.6 g/L NaCl after BG-11 preparation step one, before making the liquid medium up to a final 1 L. | correct | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "3.6 g/L", "locator": "#recipe: component table and Directions"} | Source-stated mass per liter of liquid medium; no inherited stock-dose expansion. Applied and read back exactly. |
| variants[0].modifications[0:2] / optional agar and two portions | null | ["For the agar alternative, perform BG-11 preparation step one, add the formulation-specific NaCl, and make this portion up to 500 mL with dH2O.", "In another container, add 15 g agar to 500 mL dH2O. Autoclave both preparations separately, then cool them to 45-50 degrees C in a water bath."] | add | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "15 g", "locator": "#recipe: component table and Directions"} | Keep literal batch quantities and procedure; do not calculate a final-volume agar concentration. Applied and read back exactly. |
| variants[0].modifications[2] / sterile sodium thiosulfate | null | Mix sterile sodium thiosulfate into the agar preparation before combining both portions. The salt-variant page does not specify a thiosulfate dose; no amount is inferred from the linked base recipe. Mix promptly, allow to cool and refrigerate. | unsupported | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "Sodium Thiosulfate", "locator": "#recipe: component table and Directions"} | Document required addition and missing local dose. No numeric concentration added; linked-base dose not imported. Preparation requirement documented; no numeric dose added. |

## Evidence And Scope

The complete target and hash-pinned official UTEX recipe HTML were inspected. Source URLs, titles, capture hashes and access times are in ../plan-v2.json. Source type is culture_collection_page; discovery_mode is existing_record_reference. Authors, publication year and DOI are unknown, not manufactured. All changed claims have persistent source URLs and literal excerpts in YAML; additional separately located quotes and arithmetic are in evidence explanations. No PDF verification is claimed.

Null means absent or removed, not zero. Stored units retain their denominator; textual batch additions are not asserted as final-volume concentrations. Referenced parent compositions and unrelated biological/identity claims are outside this concentration review.

## Unresolved

- The salt-variant page gives no local sodium-thiosulfate dose; formulation-specific inheritance from the linked BG-11 recipe remains unresolved.
- Existing chemical/supplier mappings, salinity, roles and growth/culture-condition claims were not independently certified.
- BG-11-1 in the source title differs from BG-11 in the linked base/table; no rename, nitrogen omission or merge is inferred.

## Verification

Baseline schema/strict checks pass. Real-schema preflight, exact readback, inverse scope check and repeat no-op pass. Every added evidence snippet and separately quoted excerpt matches its pinned source. Post-edit CLI, reference and corpus results are recorded in ../post.json, ../references.json and ../corpus.json; these receipts and ../README.md, not this report's existence, determine gate status. No taxa-media associations were added.
