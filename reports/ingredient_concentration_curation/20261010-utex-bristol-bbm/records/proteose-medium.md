# UTEX Bristol/BBM Ingredient Review

- Record: data/normalized_yaml/algae/Proteose_Medium.yaml
- ID: CultureMech:000188
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 66dfd4315618352a08b7812d6ab9de35c5448efa3e12ec9ebef4150d4bac5895
- Result SHA256: 0f2c98cb352e8e38d09e767e7c572531e80c0ba76039287382b491db75b3458a

## Source And Scope

The [source ledger](../source-review.json) pins nine official UTEX pages, five linked PDFs (seven visually inspected pages), and the BBM study full text from Europe PMC. Capture hashes and exact snippets are rechecked before application. Bibliographies contain source type, discovery mode, access date, title and authors; unknown recipe publication years are not replaced by website copyright dates.

Every stored ingredient or stock concentration is listed below. Stock composition, stock addition and final-medium amounts remain distinct. Fixed water amounts are removed where the source only specifies final make-up; no replacement number is guessed. The Bristol-NaCl base is an unfinished preparation, not a completed-medium aliquot. Optional agar formulations are outside these liquid records.

| Field / ingredient | Before | Applied amount | Status | PURL / exact snippet / locator / calculation / action |
| --- | --- | --- | --- | --- |
| ingredients[0].concentration / Proteose Peptone | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "ingredients[0].concentration: the source explicitly gives a one-litre batch, one-litre Bristol input and 1 g/L proteose peptone. For the base input, 1 L x 1000 mL/L / 1 L batch = 1000 mL/L. The optional agar preparation is not silently added to this liquid record.", "locator": "recipe table and For 1 L Total heading", "reference": "https://utex.org/products/proteose-medium", "snippet": "1 g/L"} |
| solutions[0].concentration / Bristol Medium | {"unit": "ML_PER_L", "value": "1000"} | {"unit": "ML_PER_L", "value": "1000"} | evidence_only | {"action_taken": "retained amount; added scoped source evidence", "explanation": "solutions[0].concentration: the source explicitly gives a one-litre batch, one-litre Bristol input and 1 g/L proteose peptone. For the base input, 1 L x 1000 mL/L / 1 L batch = 1000 mL/L. The optional agar preparation is not silently added to this liquid record.", "locator": "recipe table and For 1 L Total heading", "reference": "https://utex.org/products/proteose-medium", "snippet": "1 L"} |

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
