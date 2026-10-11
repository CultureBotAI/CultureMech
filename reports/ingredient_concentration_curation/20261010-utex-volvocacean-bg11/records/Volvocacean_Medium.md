# Ingredient Concentration Follow-Up

- Record: data/normalized_yaml/algae/Volvocacean_Medium.yaml
- ID: CultureMech:000236
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: b0a4159590a114e5f0a3ef38ae5998b0d480879e164b23d4c4fb5638c9261fab
- State: Applied locally; unresolved claims remain explicit.

| Field / ingredient | Old amount / unit / basis | Current amount / unit / basis | Status | Evidence | Calculation / action |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Waris Medium | {"value": "800", "unit": "ML_PER_L"} | {"value": "800", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "800 mL", "locator": "#recipe: component table and Directions"} | 800 mL / source-stated 1 L liquid blend = 800 mL/L; no stock-composition conversion. Applied and read back exactly. |
| solutions[1].concentration / Euglena Medium | {"value": "200", "unit": "ML_PER_L"} | {"value": "200", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "200 mL", "locator": "#recipe: component table and Directions"} | 200 mL / source-stated 1 L liquid blend = 200 mL/L; no stock-composition conversion. Applied and read back exactly. |
| variant_modifications[0]; parent_media.notes / prepared-medium blend | Blends 800 mL Waris Medium with 200 mL Euglena Medium per liter. | Combines 800 mL Waris Medium prepared without pH adjustment with 200 mL Euglena Medium per liter of liquid blend. | correct | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "800 mL", "locator": "#recipe: component table and Directions"} | 800 mL Waris + 200 mL Euglena forms the specified 1 L liquid blend; Waris pH is not adjusted. Applied and read back exactly. |
| preparation_steps / Waris preparation and sterilization | [{"step_number": 1, "action": "MIX", "description": "Prepare Waris Medium and Euglena Medium."}, {"step_number": 2, "action": "MIX", "description": "Combine the prepared component media."}, {"step_number": 3, "action": "STORE", "description": "Store at refrigerator temperature."}] | [{"step_number": 1, "action": "MIX", "description": "Prepare 1 L Waris Medium without pH adjustment and prepare 200 mL Euglena Medium."}, {"step_number": 2, "action": "MIX", "description": "Discard 200 mL of the Waris preparation. Combine the remaining 800 mL with the prepared 200 mL Euglena in a 2 L Erlenmeyer flask."}, {"step_number": 3, "action": "AUTOCLAVE", "description": "Cover the flask and autoclave the combined medium."}, {"step_number": 4, "action": "STORE", "description": "Store at refrigerator temperature."}] | correct | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "but do not adjust the pH.", "locator": "#recipe: component table and Directions"} | Source-specific pH omission and autoclaving restored; no numeric pH or autoclave setting inferred. Applied and read back exactly. |
| variants[0].modifications[0] / optional agar | null | After combining the 800 mL Waris and 200 mL Euglena portions, add 10.0 g agar to the flask without stirring; then cover and autoclave. | add | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "10.0 grams", "locator": "#recipe: component table and Directions"} | Literal 10.0 g batch addition; no final-volume concentration or density conversion. Applied and read back exactly. |

## Evidence And Scope

The complete target and hash-pinned official UTEX recipe HTML were inspected. Source URLs, titles, capture hashes and access times are in ../plan-v2.json. Source type is culture_collection_page; discovery_mode is existing_record_reference. Authors, publication year and DOI are unknown, not manufactured. All changed claims have persistent source URLs and literal excerpts in YAML; additional separately located quotes and arithmetic are in evidence explanations. No PDF verification is claimed.

Null means absent or removed, not zero. Stored units retain their denominator; textual batch additions are not asserted as final-volume concentrations. Referenced parent compositions and unrelated biological/identity claims are outside this concentration review.

## Unresolved

- Linked Waris and Euglena compositions, final pH, autoclave temperature/time and unrelated growth/culture conditions were not newly verified.

## Verification

Baseline schema/strict checks pass. Real-schema preflight, exact readback, inverse scope check and repeat no-op pass. Every added evidence snippet and separately quoted excerpt matches its pinned source. Post-edit CLI, reference and corpus results are recorded in ../post.json, ../references.json and ../corpus.json; these receipts and ../README.md, not this report's existence, determine gate status. No taxa-media associations were added.
