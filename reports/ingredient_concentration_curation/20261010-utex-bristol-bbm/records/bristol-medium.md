# UTEX Bristol/BBM Ingredient Review

- Record: data/normalized_yaml/algae/Bristol_Medium.yaml
- ID: CultureMech:000037
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 4d00769fe831cf963257aca23c9ebefc013791f4de2c530f7ff53209808cba04
- Result SHA256: 90791360e88ab690d6c3d7a363d302a8f819d9226eb7cbfe8f259ee25b6e681d

## Source And Scope

The [source ledger](../source-review.json) pins nine official UTEX pages, five linked PDFs (seven visually inspected pages), and the BBM study full text from Europe PMC. Capture hashes and exact snippets are rechecked before application. Bibliographies contain source type, discovery mode, access date, title and authors; unknown recipe publication years are not replaced by website copyright dates.

Every stored ingredient or stock concentration is listed below. Stock composition, stock addition and final-medium amounts remain distinct. Fixed water amounts are removed where the source only specifies final make-up; no replacement number is guessed. The Bristol-NaCl base is an unfinished preparation, not a completed-medium aliquot. Optional agar formulations are outside these liquid records.

| Field / ingredient | Before | Applied amount | Status | PURL / exact snippet / locator / calculation / action |
| --- | --- | --- | --- | --- |
| ingredients[0].concentration / dH2O | {"unit": "ML_PER_L", "value": "1000"} | omitted; preparation notes retained | correct | {"action_taken": "removed unsupported quantity; retained node and notes", "explanation": "ingredients[0].concentration: the source specifies make-up to the final medium or stock volume, not a fixed water input. Remove the unsupported 1000 mL/L assertion while retaining the water node and preparation notes. This is not a replacement numeric amount.", "locator": "Directions make-up step", "reference": "https://utex.org/products/bristol-medium", "snippet": "total volume to 1 L"} |
| ingredients[1].concentration / NaNO3 | {"unit": "MILLIMOLAR", "value": "2.94"} | {"unit": "MILLIMOLAR", "value": "2.94"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[1].concentration: Exact final molarity in the named row; stock input is separate and not independently re-expanded. The source table labels this cell Final Concentration; keep the source molarity and hydrate form without importing stock composition as a direct amount.", "locator": "recipe table, row 1, Final Concentration", "reference": "https://utex.org/products/bristol-medium", "snippet": "2.94 mM"} |
| ingredients[2].concentration / CaCl2 x 2 H2O | {"unit": "MILLIMOLAR", "value": "0.17"} | {"unit": "MILLIMOLAR", "value": "0.17"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[2].concentration: Exact final molarity in the named row; stock input is separate and not independently re-expanded. The source table labels this cell Final Concentration; keep the source molarity and hydrate form without importing stock composition as a direct amount.", "locator": "recipe table, row 2, Final Concentration", "reference": "https://utex.org/products/bristol-medium", "snippet": "0.17 mM"} |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"unit": "MILLIMOLAR", "value": "0.3"} | {"unit": "MILLIMOLAR", "value": "0.3"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[3].concentration: Exact final molarity in the named row; stock input is separate and not independently re-expanded. The source table labels this cell Final Concentration; keep the source molarity and hydrate form without importing stock composition as a direct amount.", "locator": "recipe table, row 3, Final Concentration", "reference": "https://utex.org/products/bristol-medium", "snippet": "0.3 mM"} |
| ingredients[4].concentration / K2HPO4 | {"unit": "MILLIMOLAR", "value": "0.43"} | {"unit": "MILLIMOLAR", "value": "0.43"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[4].concentration: Exact final molarity in the named row; stock input is separate and not independently re-expanded. The source table labels this cell Final Concentration; keep the source molarity and hydrate form without importing stock composition as a direct amount.", "locator": "recipe table, row 4, Final Concentration", "reference": "https://utex.org/products/bristol-medium", "snippet": "0.43 mM"} |
| ingredients[5].concentration / KH2PO4 | {"unit": "MILLIMOLAR", "value": "1.29"} | {"unit": "MILLIMOLAR", "value": "1.29"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[5].concentration: Exact final molarity in the named row; stock input is separate and not independently re-expanded. The source table labels this cell Final Concentration; keep the source molarity and hydrate form without importing stock composition as a direct amount.", "locator": "recipe table, row 5, Final Concentration", "reference": "https://utex.org/products/bristol-medium", "snippet": "1.29 mM"} |
| ingredients[6].concentration / NaCl | {"unit": "MILLIMOLAR", "value": "0.43"} | {"unit": "MILLIMOLAR", "value": "0.43"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[6].concentration: Exact final molarity in the named row; stock input is separate and not independently re-expanded. The source table labels this cell Final Concentration; keep the source molarity and hydrate form without importing stock composition as a direct amount.", "locator": "recipe table, row 6, Final Concentration", "reference": "https://utex.org/products/bristol-medium", "snippet": "0.43 mM"} |

## Narrative And Relationship Claims

| Field | Before | Applied text | Status | Source / snippet / locator / reasoning / action |
| --- | --- | --- | --- | --- |
| variant_children[3].notes | Adds 3.6 g/L NaCl to prepared Bristol Medium. | Bristol-NaCl uses this mineral preparation only through step one; it adds 3.6 g NaCl before making the child up to 1 L, not to a litre of completed Bristol Medium. | correct | {"action_taken": "corrected text and added scoped evidence", "explanation": "Reciprocal stage correction; no parent ingredient amount changed by the child recipe.", "locator": "Bristol-NaCl Directions 1-2 and table", "reference": "https://utex.org/products/bristol-nacl-medium", "snippet": "Prepare Bristol Medium through step one."} |

## Other Evidenced Changes

The [guarded plan](../plan.json) records every exact old/new operation, including stock-stage notes, the Botryococcus liquid-stock mixing action, reciprocal Bristol-NaCl relationship notes and discrete estradiol treatments. The study NH4Cl value remains 4.5 ppm in the pre-experiment stock culture; ppm basis and culture working volume are not inferred. Prior history and unrelated organism/growth/role claims are preserved.

## Remaining Issues

- The BBM trace source prints MnCl with tetrahydrate; its intended chemical identity and the existing MnCl2 amount remain unverified. Added node evidence supports only that source-spelling conflict.
- BBM trace concentration columns and stock-page parenthetical micromolar values conflict with explicit stock preparation amounts. Preserve inspected Amount-per-litre stock recipes, not those incompatible columns; no new final-medium conversions.
- The BBM iron stock does not specify acid strength. No density, purity or molarity is assumed.
- The BBM study cites Stein 1973; exact equivalence with the current UTEX parent is unverified. NH4Cl ppm basis and culture working volume remain unspecified; no numerical conversion or aliquot inference.
- Bristol-NaCl uses an unfinished parent preparation; its table one-litre row is not certified as a working dose of completed Bristol. The reference and explicit stage notes are retained without a fabricated dose.
- Optional agar formulations are not silently added to these liquid records. No new taxa-media associations, IDs or growth/role assertions are curated.
- Supplier-catalog identities, generic incubation/light claims and unrelated preexisting organism evidence are not blanket-certified by this ingredient review.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json), [merge retention](../reconcile-retention.json) and [checkpoint](../validation.json) record actual outcomes when present. Pending or failed gates are not passes; report presence is not complete concentration verification. No taxa-media associations added.
