# UTEX CHEV Ingredient Amount Review

- Record: data/normalized_yaml/algae/1_2_CHEV_Diatom_Medium.yaml
- ID: CultureMech:000002
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: ef24dc9dec3f28bf9a0471df9c471b2d249e14d99ef270c57fe3ffb4796fbbed
- Result SHA256: af43ca138642a9fe29b00b3651cef22ea5a8497a42af24a018e5e23781636096

## Source And Scope

1/2 CHEV Diatom Medium; https://utex.org/products/one-half-chev-diatom-medium. Publisher: UTEX Culture Collection of Algae. Source type: culture_collection_page; discovery: existing_record_reference; accessed 2026-10-09. Named authors and web publication year: unknown. HTML SHA256: eee62aa5b3c1ea15995fa07fd949a9ee7140fcaa22d8f33f03c38d1a88028883. Linked PDF: https://web.biosci.utexas.edu/utex/Media%20PDF/one-half-chev-diatom-medium.pdf; SHA256: a2688887b18736ff195ed6abc4533803f44e71b5bdedc4a8804f4393b2a52e15. The recipe table, directions and PDF page 1 were inspected. All direct ingredient and stock-addition claims in this record are listed below. Referenced F/2 composition was not concentration-reviewed in this batch. See the [pinned source ledger](../source-review.json).

## Every Amount Claim

L values are absolute volumes of inputs, not per-liter concentrations. 15 mL is tube capacity, not evidence of the final volume. A notes-only evidence entry does not verify its retained concentration.

| Field / ingredient | Old | Applied | Status | Action | PURL, exact snippet, locator, basis and calculation |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0] / CR1 Soil | {"unit": "VARIABLE", "value": "1 cc per 15 mL tube"} | {"unit": "L", "value": "0.001"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[0].concentration and notes (CR1 Soil) in UTEX:one-half-chev-diatom-medium. Locator: recipe table, row 1, Component=CR1 Soil, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 1 cc / 1000 cc per L = 0.001 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. One cubic centimetre equals one millilitre; this is bulk soil volume, with no density, dry mass, water content or soil composition inferred. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/one-half-chev-diatom-medium", "snippet": "1 cc", "supports": "SUPPORT"} |
| ingredients[1] / MgCO3 | {"unit": "MILLIMOLAR", "value": "0.5"} | {"unit": "MILLIMOLAR", "value": "0.5"} | evidence_only | retain amount; add concentration evidence | {"explanation": "Supports ingredients[1].concentration and notes (MgCO3) in UTEX:one-half-chev-diatom-medium. Locator: recipe table, row 2, Component=MgCO 3 (MCIB CB486), Final Concentration column; Directions specify the preparation basis. Retain the directly reported Final Concentration, 0.5 mM; the Amount column separately prints 0.5 mg/12 mL. No molecular-weight, hydration, solubility, purity or final-volume calculation is asserted. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/one-half-chev-diatom-medium", "snippet": "0.5 mM", "supports": "SUPPORT"} |
| ingredients[2] / dH2O | {"unit": "ML_PER_L", "value": "958.333"} | {"unit": "L", "value": "0.0115"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[2].concentration and notes (dH2O) in UTEX:one-half-chev-diatom-medium. Locator: recipe table, row 3, Component=dH 2 O, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 11.5 mL / 1000 mL per L = 0.0115 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/one-half-chev-diatom-medium", "snippet": "11.5 mL", "supports": "SUPPORT"} |
| ingredients[3] / Pasteurized Seawater | {"unit": "ML_PER_L", "value": "41.667"} | {"unit": "L", "value": "0.0005"} | correct | correct amount and add evidence | {"explanation": "Supports ingredients[3].concentration and notes (Pasteurized Seawater) in UTEX:one-half-chev-diatom-medium. Locator: recipe table, row 4, Component=Pasteurized Seawater, Amount column; Directions specify the preparation basis. Record the source input volume per tube: 0.5 mL / 1000 mL per L = 0.0005 L. L here is an absolute ingredient input volume for one tube, not a per-liter concentration or measured final volume. The 15 mL figure is vessel capacity. Do not divide by that capacity or by a sum of liquid inputs. No density, volume-additivity or stock-composition inference. HTML table and linked PDF page 1 inspected 2026-10-09. Existing chemical mappings and growth conditions are not newly verified.", "reference": "https://utex.org/products/one-half-chev-diatom-medium", "snippet": "0.5 mL", "supports": "SUPPORT"} |

## Remaining Issues

- L quantities are absolute input volumes per single-tube preparation, not final concentrations. Vessel capacity and summed liquid inputs do not establish final volume.
- The three fixed drop counts retain unresolved legacy VARIABLE encodings; their new evidence supports notes only. No drop-volume estimate is introduced.
- Modified CHEV's 1 mg/12 mL versus 0.5 mM source discrepancy remains unresolved. Its new evidence supports the discrepancy note, not the retained molarity.
- Referenced F/2 composition, chemical mappings, preparation, growth conditions and relationships are preserved, not newly certified. No new taxa-media associations.
- Existing relationship notes that describe a 12 mL liquid fill are not evidence of a measured final volume and are not newly certified.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json) and [checkpoint](../validation.json) record gate results. Pending/failed checks are not passes. No taxa-media associations were added.
