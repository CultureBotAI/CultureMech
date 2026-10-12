# UTEX CHEV Ingredient Amount Review

- Record: data/normalized_yaml/algae/2X_CHEV_Diatom_Medium.yaml
- ID: CultureMech:000014
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 40abfa6612b9cd40ddeaeb12f8c811fb8ecc56cb18601de266f7ebd53a512080
- Result SHA256: 6252ae73d394c16c097600affc8786ac0cd43580e8a168e7e932fa00dfc71322

## Source And Scope

2X CHEV Diatom Medium; https://utex.org/products/2x-chev-diatom-medium. Publisher: UTEX Culture Collection of Algae. Source type: culture_collection_page; discovery: existing_record_reference; accessed 2026-10-09. Named authors and web publication year: unknown. HTML SHA256: 9539ca9c9a22520eec9d7b7e97eb5c4e805c91bbc084ddcd2350773302dbceeb. Linked PDF: https://web.biosci.utexas.edu/utex/Media%20PDF/2x-chev-diatom-medium.pdf; SHA256: 49dfeb5a810de4dc5b89cff1b7f6f664b5d140e8b9255db43f22cd87418cf8c1. The recipe table, directions and PDF page 1 were inspected. All direct ingredient and stock-addition claims in this record are listed below. Referenced F/2 composition was not concentration-reviewed in this batch. See the [pinned source ledger](../source-review.json).

## Every Amount Claim

L values are absolute volumes of inputs, not per-liter concentrations. 15 mL is tube capacity, not evidence of the final volume. A notes-only evidence entry does not verify its retained concentration.

| Field / ingredient | Old | Applied | Status | Action | PURL, exact snippet, locator, basis and calculation |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0] / CR1 Soil | {"unit": "VARIABLE", "value": "1 cc per 15 mL tube"} | {"unit": "L", "value": "0.001"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[0].concentration and notes (CR1 Soil) in UTEX:2x-chev-diatom-medium. Locator: recipe table, row 1, Component=CR1 Soil, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 1 cc / 1000 cc per L = 0.001 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. One cubic centimetre equals one millilitre; this is bulk soil volume, with no density, dry mass, water content or soil composition inferred. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/2x-chev-diatom-medium", "snippet": "1 cc", "supports": "SUPPORT"} |
| ingredients[1] / MgCO3 | {"unit": "MILLIMOLAR", "value": "0.5"} | {"unit": "MILLIMOLAR", "value": "0.5"} | evidence_only | retain amount; add concentration evidence | {"explanation": "Supports ingredients[1].concentration and notes (MgCO3) in UTEX:2x-chev-diatom-medium. Locator: recipe table, row 2, Component=MgCO 3 (MCIB CB486), Final Concentration column; Directions specify the preparation basis. Retain the directly reported Final Concentration, 0.5 mM; the Amount column separately prints 0.5 mg/12 mL. No molecular-weight, hydration, solubility, purity or final-volume calculation is asserted. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/2x-chev-diatom-medium", "snippet": "0.5 mM", "supports": "SUPPORT"} |
| ingredients[2] / dH2O | {"unit": "ML_PER_L", "value": "833.333"} | {"unit": "L", "value": "0.01"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[2].concentration and notes (dH2O) in UTEX:2x-chev-diatom-medium. Locator: recipe table, row 3, Component=dH 2 O, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 10 mL / 1000 mL per L = 0.01 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/2x-chev-diatom-medium", "snippet": "10 mL", "supports": "SUPPORT"} |
| ingredients[3] / Pasteurized Seawater | {"unit": "ML_PER_L", "value": "166.667"} | {"unit": "L", "value": "0.002"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[3].concentration and notes (Pasteurized Seawater) in UTEX:2x-chev-diatom-medium. Locator: recipe table, row 4, Component=Pasteurized Seawater, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 2 mL / 1000 mL per L = 0.002 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/2x-chev-diatom-medium", "snippet": "2 mL", "supports": "SUPPORT"} |

## Remaining Issues

- L quantities are absolute input volumes per single-tube preparation, not final concentrations. Vessel capacity and summed liquid inputs do not establish final volume.
- The three fixed drop counts retain unresolved legacy VARIABLE encodings; their new evidence supports notes only. No drop-volume estimate is introduced.
- Modified CHEV's 1 mg/12 mL versus 0.5 mM source discrepancy remains unresolved. Its new evidence supports the discrepancy note, not the retained molarity.
- Referenced F/2 composition, chemical mappings, preparation, growth conditions and relationships are preserved, not newly certified. No new taxa-media associations.
- Existing relationship notes that describe a 12 mL liquid fill are not evidence of a measured final volume and are not newly certified.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json) and [checkpoint](../validation.json) record gate results. Pending/failed checks are not passes. No taxa-media associations were added.
