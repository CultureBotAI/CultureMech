# UTEX CHEV Ingredient Amount Review

- Record: data/normalized_yaml/algae/Modified_CHEV_Medium.yaml
- ID: CultureMech:000180
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: c3f788517bc714a548aabefbb6d4fea5282423881a834227c0b1e84aa2215e4d
- Result SHA256: 7f675c453a766a34c871343eb79df4f95668789e523795007c49cf702adece43

## Source And Scope

Modified CHEV Medium; https://utex.org/products/modified-chev-medium. Publisher: UTEX Culture Collection of Algae. Source type: culture_collection_page; discovery: existing_record_reference; accessed 2026-10-09. Named authors and web publication year: unknown. HTML SHA256: 39ab61e63d4552b3bc14acd743d553d8cff8fc9c883e1ab9ff80d5d0cfb3e66b. Linked PDF: https://web.biosci.utexas.edu/utex/Media%20PDF/modified-chev-medium.pdf; SHA256: b86906131583f168f29e072d97145bb6e460d4d2cd2649b157d54d6b41c447bd. The recipe table, directions and PDF page 1 were inspected. All direct ingredient and stock-addition claims in this record are listed below. Referenced F/2 composition was not concentration-reviewed in this batch. See the [pinned source ledger](../source-review.json).

## Every Amount Claim

L values are absolute volumes of inputs, not per-liter concentrations. 15 mL is tube capacity, not evidence of the final volume. A notes-only evidence entry does not verify its retained concentration.

| Field / ingredient | Old | Applied | Status | Action | PURL, exact snippet, locator, basis and calculation |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0] / CR1 Soil | {"unit": "VARIABLE", "value": "1 cc per 15 mL tube"} | {"unit": "L", "value": "0.001"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[0].concentration and notes (CR1 Soil) in UTEX:modified-chev-medium. Locator: recipe table, row 1, Component=CR1 Soil, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 1 cc / 1000 cc per L = 0.001 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. One cubic centimetre equals one millilitre; this is bulk soil volume, with no density, dry mass, water content or soil composition inferred. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/modified-chev-medium", "snippet": "1 cc", "supports": "SUPPORT"} |
| ingredients[1] / MgCO3 | {"unit": "MILLIMOLAR", "value": "0.5"} | {"unit": "MILLIMOLAR", "value": "0.5"} | conflict | retain unverified encoding/amount; clarify notes with notes-only evidence | {"explanation": "Supports ingredients[1].notes only; retained concentration remains unverified (MgCO3) in UTEX:modified-chev-medium. Locator: recipe table, row 2, Component=MgCO 3 (MCIB CB486), Amount column; Directions specify the preparation basis. The modified recipe doubles the printed MgCO3 mass relative to the other inspected CHEV pages while retaining the same printed molarity. The PDF confirms this source discrepancy. Neither column is selected as a corrected amount, and no mass/molar conversion is applied. This evidence supports the discrepancy note only, not the retained concentration. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/modified-chev-medium", "snippet": "1 mg/12 mL", "supports": "SUPPORT"} |
| ingredients[2] / dH2O | {"unit": "VARIABLE", "value": "11 mL per 15 mL tube"} | {"unit": "L", "value": "0.011"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[2].concentration and notes (dH2O) in UTEX:modified-chev-medium. Locator: recipe table, row 3, Component=dH 2 O, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 11 mL / 1000 mL per L = 0.011 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/modified-chev-medium", "snippet": "11 mL", "supports": "SUPPORT"} |
| solutions[0] / F/2 Medium | {"unit": "VARIABLE", "value": "1 mL per 15 mL tube"} | {"unit": "L", "value": "0.001"} | correct | correct amount and add evidence | {"explanation": "Supports solutions[0].concentration and notes (F/2 Medium) in UTEX:modified-chev-medium. Locator: recipe table, row 4, Component=F/2 Medium, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 1 mL / 1000 mL per L = 0.001 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/modified-chev-medium", "snippet": "1 mL", "supports": "SUPPORT"} |

## Remaining Issues

- L quantities are absolute input volumes per single-tube preparation, not final concentrations. Vessel capacity and summed liquid inputs do not establish final volume.
- The three fixed drop counts retain unresolved legacy VARIABLE encodings; their new evidence supports notes only. No drop-volume estimate is introduced.
- Modified CHEV's 1 mg/12 mL versus 0.5 mM source discrepancy remains unresolved. Its new evidence supports the discrepancy note, not the retained molarity.
- Referenced F/2 composition, chemical mappings, preparation, growth conditions and relationships are preserved, not newly certified. No new taxa-media associations.
- Existing relationship notes that describe a 12 mL liquid fill are not evidence of a measured final volume and are not newly certified.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json) and [checkpoint](../validation.json) record gate results. Pending/failed checks are not passes. No taxa-media associations were added.
