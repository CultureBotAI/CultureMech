# UTEX CHEV Ingredient Amount Review

- Record: data/normalized_yaml/algae/CHEV_Diatom_Medium.yaml
- ID: CultureMech:000151
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: fd26befe97dbecb57af0f2689ab266056d3eec18eb0610abe94402caae2ed5f1
- Result SHA256: 609605d0e755989b48f3c9b4a9ddb775c16c274d23e6eeae27260cb10e601708

## Source And Scope

CHEV Diatom Medium; https://utex.org/products/chev-diatom-medium. Publisher: UTEX Culture Collection of Algae. Source type: culture_collection_page; discovery: existing_record_reference; accessed 2026-10-09. Named authors and web publication year: unknown. HTML SHA256: 4a1c81a26b2da09df49590c111795c6e4a5eb6f357fee73253cadf7f32525c62. Linked PDF: https://web.biosci.utexas.edu/utex/Media%20PDF/chev-diatom-medium.pdf; SHA256: 62d01eeaef7e45bcfdea61c4c7b112665bb869b659d8905f7ace20cacb15b5c6. The recipe table, directions and PDF page 1 were inspected. All direct ingredient and stock-addition claims in this record are listed below. Referenced F/2 composition was not concentration-reviewed in this batch. See the [pinned source ledger](../source-review.json).

## Every Amount Claim

L values are absolute volumes of inputs, not per-liter concentrations. 15 mL is tube capacity, not evidence of the final volume. A notes-only evidence entry does not verify its retained concentration.

| Field / ingredient | Old | Applied | Status | Action | PURL, exact snippet, locator, basis and calculation |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0] / CR1 Soil | {"unit": "VARIABLE", "value": "1 cc per 15 mL tube"} | {"unit": "L", "value": "0.001"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[0].concentration and notes (CR1 Soil) in UTEX:chev-diatom-medium. Locator: recipe table, row 1, Component=CR1 Soil, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 1 cc / 1000 cc per L = 0.001 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. One cubic centimetre equals one millilitre; this is bulk soil volume, with no density, dry mass, water content or soil composition inferred. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/chev-diatom-medium", "snippet": "1 cc", "supports": "SUPPORT"} |
| ingredients[1] / MgCO3 | {"unit": "MILLIMOLAR", "value": "0.5"} | {"unit": "MILLIMOLAR", "value": "0.5"} | evidence_only | retain amount; add concentration evidence | {"explanation": "Supports ingredients[1].concentration and notes (MgCO3) in UTEX:chev-diatom-medium. Locator: recipe table, row 2, Component=MgCO 3 (MCIB CB486), Final Concentration column; Directions specify the preparation basis. Retain the directly reported Final Concentration, 0.5 mM; the Amount column separately prints 0.5 mg/12 mL. No molecular-weight, hydration, solubility, purity or final-volume calculation is asserted. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/chev-diatom-medium", "snippet": "0.5 mM", "supports": "SUPPORT"} |
| ingredients[2] / dH2O | {"unit": "ML_PER_L", "value": "916.667"} | {"unit": "L", "value": "0.011"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[2].concentration and notes (dH2O) in UTEX:chev-diatom-medium. Locator: recipe table, row 3, Component=dH 2 O, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 11 mL / 1000 mL per L = 0.011 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/chev-diatom-medium", "snippet": "11 mL", "supports": "SUPPORT"} |
| ingredients[3] / Pasteurized Seawater | {"unit": "ML_PER_L", "value": "83.333"} | {"unit": "L", "value": "0.001"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[3].concentration and notes (Pasteurized Seawater) in UTEX:chev-diatom-medium. Locator: recipe table, row 4, Component=Pasteurized Seawater, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 1 mL / 1000 mL per L = 0.001 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/chev-diatom-medium", "snippet": "1 mL", "supports": "SUPPORT"} |

## Remaining Issues

- L quantities are absolute input volumes per single-tube preparation, not final concentrations. Vessel capacity and summed liquid inputs do not establish final volume.
- The three fixed drop counts retain unresolved legacy VARIABLE encodings; their new evidence supports notes only. No drop-volume estimate is introduced.
- Modified CHEV's 1 mg/12 mL versus 0.5 mM source discrepancy remains unresolved. Its new evidence supports the discrepancy note, not the retained molarity.
- Referenced F/2 composition, chemical mappings, preparation, growth conditions and relationships are preserved, not newly certified. No new taxa-media associations.
- Existing relationship notes that describe a 12 mL liquid fill are not evidence of a measured final volume and are not newly certified.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json) and [checkpoint](../validation.json) record gate results. Pending/failed checks are not passes. No taxa-media associations were added.
