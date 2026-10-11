# UTEX Bristol/BBM Ingredient Review

- Record: data/normalized_yaml/algae/Botryococcus_Medium.yaml
- ID: CultureMech:000035
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 4c577ead43be926fd3701e1f6990992e2e99109bb6c3fcc9f222ccae7043916a
- Result SHA256: bfc92b248ad3c780166b39dfe8bd5ad3047a5efd6e659f8f166bd8e3b956bb90

## Source And Scope

The [source ledger](../source-review.json) pins nine official UTEX pages, five linked PDFs (seven visually inspected pages), and the BBM study full text from Europe PMC. Capture hashes and exact snippets are rechecked before application. Bibliographies contain source type, discovery mode, access date, title and authors; unknown recipe publication years are not replaced by website copyright dates.

Every stored ingredient or stock concentration is listed below. Stock composition, stock addition and final-medium amounts remain distinct. Fixed water amounts are removed where the source only specifies final make-up; no replacement number is guessed. The Bristol-NaCl base is an unfinished preparation, not a completed-medium aliquot. Optional agar formulations are outside these liquid records.

| Field / ingredient | Before | Applied amount | Status | PURL / exact snippet / locator / calculation / action |
| --- | --- | --- | --- | --- |
| ingredients[0].concentration / (NH4)2HPO4 | {"unit": "MILLIMOLAR", "value": "0.151"} | {"unit": "MILLIMOLAR", "value": "0.151"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[0].concentration: source-reported final phosphate contribution, not stock strength. Table row 2 separately specifies a 2 g/100 mL stock dosed at 1 mL/L. This evidence also supports correcting root notes to distinguish those stages.", "locator": "recipe table rows 1-2 and Directions 1-3", "reference": "https://utex.org/products/botryococcus-medium", "snippet": "0.151 mM"} |
| ingredients[1].concentration / dH2O | {"unit": "ML_PER_L", "value": "59"} | omitted; preparation notes retained | correct | {"action_taken": "removed unsupported quantity; retained node and notes", "explanation": "ingredients[1].concentration: remove the unsupported fixed water input. Arithmetic 1000 - 940 - 1 = 59 assumes exactly additive solution volumes; the source instead makes up to one litre. Retain its make-up notes; this is not a replacement numeric amount.", "locator": "recipe table rows 1-2 and Directions 1-3", "reference": "https://utex.org/products/botryococcus-medium", "snippet": "Bring total volume to 1 L with dH2O."} |
| solutions[0].concentration / Bristol Medium | {"unit": "ML_PER_L", "value": "940"} | {"unit": "ML_PER_L", "value": "940"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "solutions[0].concentration: the specified 940 mL prepared Bristol input belongs to one litre final medium, so 940 mL / 1 L = 940 mL/L. Preserve the separately referenced parent formulation and do not assume undiluted parent components in this child.", "locator": "recipe table rows 1-2 and Directions 1-3", "reference": "https://utex.org/products/botryococcus-medium", "snippet": "940 mL"} |

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
