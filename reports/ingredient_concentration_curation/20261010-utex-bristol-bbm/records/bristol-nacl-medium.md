# UTEX Bristol/BBM Ingredient Review

- Record: data/normalized_yaml/algae/bristol_nacl_medium.yaml
- ID: CultureMech:000036
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 90b6fe3bd4e9a91861ab5647c5c4ba089e98447f3c8f6c129091ee70e7d79dbc
- Result SHA256: bdc6486c55ab2b7e87c06c6bf40928b6e6831565b194682b38314a9c38c4cb4f

## Source And Scope

The [source ledger](../source-review.json) pins nine official UTEX pages, five linked PDFs (seven visually inspected pages), and the BBM study full text from Europe PMC. Capture hashes and exact snippets are rechecked before application. Bibliographies contain source type, discovery mode, access date, title and authors; unknown recipe publication years are not replaced by website copyright dates.

Every stored ingredient or stock concentration is listed below. Stock composition, stock addition and final-medium amounts remain distinct. Fixed water amounts are removed where the source only specifies final make-up; no replacement number is guessed. The Bristol-NaCl base is an unfinished preparation, not a completed-medium aliquot. Optional agar formulations are outside these liquid records.

| Field / ingredient | Before | Applied amount | Status | PURL / exact snippet / locator / calculation / action |
| --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"unit": "MOLAR", "value": "0.062"} | {"unit": "MOLAR", "value": "0.062"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[0].concentration: source-reported concentration for the added NaCl row, separately listed as 3.6 g/L. Do not represent this as total NaCl including the Bristol base or independently re-convert rounded molarity. This evidence also supports root notes about adding salt before final make-up.", "locator": "Directions 1-2 and recipe table", "reference": "https://utex.org/products/bristol-nacl-medium", "snippet": "0.062 M"} |
| solutions[0].concentration / Bristol Medium | {"unit": "ML_PER_L", "value": "1000"} | omitted; preparation notes retained | correct | {"action_taken": "removed unsupported quantity; retained node and notes", "explanation": "solutions[0].concentration: Directions stop Bristol preparation before its final volume adjustment, add NaCl, then make the child up to one litre. The table one-litre Bristol row defines recipe scale, not an aliquot of completed parent medium. Remove the unsupported working-dose assertion; retain the parent reference with explicit preparation-stage notes. This is not a replacement numeric amount. The same evidence supports solution label/notes and parent/variant descriptions.", "locator": "Directions 1-2 and recipe table", "reference": "https://utex.org/products/bristol-nacl-medium", "snippet": "Prepare Bristol Medium through step one."} |

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
