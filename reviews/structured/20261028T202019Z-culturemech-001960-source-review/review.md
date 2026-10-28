# Scientific review: DESULFONATRONUM LACUSTRE MEDIUM

- Review: 20261028T202019Z-culturemech-001960-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:15:13.321875Z
- Finished UTC: 2026-10-28T20:20:19.378061Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM813b retains eleven source-supported main rates, final pH and substantial preparation, while22 stock entries and SL-10 preparation are misplaced at root. Restore stock scope, keep HCl percent basis unresolved, correct sodium-resazurin/nickel form assertions and attach exact evidence.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch077 index 02
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001960 | data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml | generated | desulfonatronum_lacustre_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001960 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001960 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001960 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001960 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSM813b generic formulation

identity: supported. Targets: CultureMech:001960.

Target and single maintained owner have identical scientific fields. Current primary and API agree on DSM813b with L-lactate and low NaCl. DSM813/813a are separate formulations. The printed DSM112796 pyruvate substitution is excluded because the selected record is the generic813b formulation; no strain-growth inference is made.

### Complex liquid formulation

representation: supported. Targets: CultureMech:001960.

Yeast extract supports the complex/undefined classification. No agar or other solidifying agent is present in the exact generic formulation.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001960.

66 current concentration fields are covered by 46 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b077-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","quantity_field_count":66,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 7-7","quote":"KH2PO4                                                     0.20         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\": 1.46527,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q2","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 8-8","quote":"MgCl2 x 6 H2O                                              0.10         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 0.490405,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 9-9","quote":"NH4Cl                                                      1.00         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 10-10","quote":"KCl                                                        0.20         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\": 2.67474,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q5","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.98504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.98504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 11-11","quote":"Na2SO4                                                     5.00         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.98504,\n                        \"mmol_l\": 35.0961,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 12-12","quote":"NaCl                                                       2.00         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.99402,\n                        \"mmol_l\": 34.1208,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q7","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 15-15","quote":"Yeast extract                                              1.00         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q8","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement. The primary0.5ml of0.1% w/v sodium-resazurin stock supplies0.5mg per batch; preserve that stock dose and strength as well as the supported normalized rate. Its sodium-salt grounding is assessed separately.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 16-16","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement. The primary0.5ml of0.1% w/v sodium-resazurin stock supplies0.5mg per batch; preserve that stock dose and strength as well as the supported normalized rate. Its sodium-salt grounding is assessed separately."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement. The primary0.5ml of0.1% w/v sodium-resazurin stock supplies0.5mg per batch; preserve that stock dose and strength as well as the supported normalized rate. Its sodium-salt grounding is assessed separately."}]},{"quantity_id":"q9","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.48953","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.48953","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 17-17","quote":"Na2CO3                                                     3.50         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 3.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.48953,\n                        \"mmol_l\": 32.9238,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q10","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 18-18","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 2.07553,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement."}]},{"quantity_id":"q11","label":"Na-L-lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement. The exact source specifies L-lactate; keep that stereochemistry and the separately filtered anoxic-stock addition. No concentration of that separate lactate stock is supplied.","source_stage":"Main medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 19-19","quote":"Na-L-lactate                                               2.00         g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na-L-lactate\",\n                        \"compound_id\": 265,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.99402,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement. The exact source specifies L-lactate; keep that stereochemistry and the separately filtered anoxic-stock addition. No concentration of that separate lactate stock is supplied."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The local G_PER_L number agrees with the exact provider main g_l and the primary batch amount on its explicitly declared final1003ml basis. Credit and retain this rate; do not replace it with the undivided per1000ml input-water amount. Source-declared final volume is not an independent measurement. The exact source specifies L-lactate; keep that stereochemistry and the separately filtered anoxic-stock addition. No concentration of that separate lactate stock is supplied."}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly reports2.5g/L, but the primary specifies10ml HCl(25%) in SL-10 and does not establish the percent basis or density needed to endorse that conversion. Preserve exact10ml and25% as source assertions; restore stock scope and do not carry2.5g/L into the final medium or silently infer w/v.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 37-37","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The provider explicitly reports2.5g/L, but the primary specifies10ml HCl(25%) in SL-10 and does not establish the percent basis or density needed to endorse that conversion. Preserve exact10ml and25% as source assertions; restore stock scope and do not carry2.5g/L into the final medium or silently infer w/v."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The provider explicitly reports2.5g/L, but the primary specifies10ml HCl(25%) in SL-10 and does not establish the percent basis or density needed to endorse that conversion. Preserve exact10ml and25% as source assertions; restore stock scope and do not carry2.5g/L into the final medium or silently infer w/v."}]},{"quantity_id":"q13","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 38-38","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 39-39","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 40-40","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 41-41","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 42-42","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 43-43","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 44-44","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 45-45","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. SL-10 has an explicit1000ml final make-up."}]},{"quantity_id":"q21","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Selenite-tungstate stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 63-63","quote":"NaOH                                        0.50    g","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q22","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Selenite-tungstate stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 64-64","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q23","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Selenite-tungstate stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 65-65","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q24","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 71-71","quote":"Biotin                                     20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q25","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 72-72","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q26","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 73-73","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q27","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 74-74","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q28","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 75-75","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q29","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 76-76","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q30","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 77-77","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q31","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 78-78","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q32","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 79-79","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q33","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 80-80","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The local scalar agrees with the exact provider stock g_l and primary mass. Credit the existing stock strength on its declared basis, but correct its unqualified main-medium placement and preserve the separate1ml receiving dose. The stock table lists1000ml water and provider declares1000ml stock volume; these remain declared input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q34","label":"SL-10 receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve the printed1ml batch dose and exact stock identity. The completed medium is explicitly1003ml; bare ml is not an unqualified ml/L dose. Do not flatten its stock components.","source_stage":"Source-only stock receiving dose","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 13-13","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q35","label":"Selenite-tungstate receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve the printed1ml batch dose and exact stock identity. The completed medium is explicitly1003ml; bare ml is not an unqualified ml/L dose. Do not flatten its stock components.","source_stage":"Source-only stock receiving dose","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 14-14","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q36","label":"Wolin10x receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve the printed1ml batch dose and exact stock identity. The completed medium is explicitly1003ml; bare ml is not an unqualified ml/L dose. Do not flatten its stock components.","source_stage":"Source-only stock receiving dose","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 20-20","quote":"Wolin's vitamin solution (10x)                             1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Sodium-resazurin dose and stock strength","local_fields":[],"decision":"evidence_only","rationale":"Preserve0.5ml of0.1% w/v sodium-resazurin stock, supplying0.5mg per batch. The main supported rate uses the declared1003ml denominator; these source stock controls remain independently visible.","source_stage":"Source-only dye stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 16-16","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q38","label":"main input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed solvent input in its exact source section. SL-10 separately states final make-up, while the final main1003ml declaration and the other stock provider volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 21-21","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"SL-10 input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed solvent input in its exact source section. SL-10 separately states final make-up, while the final main1003ml declaration and the other stock provider volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 46-46","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"selenite-tungstate input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed solvent input in its exact source section. SL-10 separately states final make-up, while the final main1003ml declaration and the other stock provider volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 66-66","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"vitamin input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed solvent input in its exact source section. SL-10 separately states final make-up, while the final main1003ml declaration and the other stock provider volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 81-81","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q42","label":"Main declared final volume","local_fields":[],"decision":"evidence_only","rationale":"The primary explicitly declares1003ml final medium volume, agreeing with the API normalization. Retain that source basis without claiming independent measurement or reconstructing a different total from omissions in the schematic table.","source_stage":"Completed medium","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q43","label":"SL-10 final make-up","local_fields":[],"decision":"evidence_only","rationale":"The source starts with acid and water inputs and explicitly makes up to1000ml. Preserve the final-volume instruction, including the page break; do not add a further litre after the listed990ml.","source_stage":"SL-10 stock final volume","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 37-37","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 46-48","quote":"Distilled water                                           990.00      ml\n\nFirst dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q44","label":"Retained final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ph_range","stored":{"min":8.8,"max":9.0}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ph_range","stored":{"min":8.8,"max":9.0}}],"decision":"evidence_only","rationale":"The exact8.8–9.0 range is supported by the primary main preparation and header. It is not transferred to a stock or the excluded DSM112796 substitution.","source_stage":"Completed-medium pH","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 3-3","quote":"Final pH: 8.8 - 9.0","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 23-27","quote":"Dissolve ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium\nwith 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and\nsulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into\nHungate-type tubes or serum vials and autoclave. Before use add lactate and vitamins\n(sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The exact8.8–9.0 range is supported by the primary main preparation and header. It is not transferred to a stock or the excluded DSM112796 substitution."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The exact8.8–9.0 range is supported by the primary main preparation and header. It is not transferred to a stock or the excluded DSM112796 substitution."}]},{"quantity_id":"q45","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium with 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add lactate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas."}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium with 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add lactate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas."}}],"decision":"evidence_only","rationale":"The existing text and AUTOCLAVE classification retain the source order,100%N2 for30–45min,pH8.8–9.0,carbonate/sulfide addition,anoxic dispensing and later filtered lactate/vitamins. Preserve this substantial existing context; no specific autoclave temperature/time or lactate-stock strength is supplied.","source_stage":"Main preparation","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 23-27","quote":"Dissolve ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium\nwith 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and\nsulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into\nHungate-type tubes or serum vials and autoclave. Before use add lactate and vitamins\n(sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium with 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add lactate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing text and AUTOCLAVE classification retain the source order,100%N2 for30–45min,pH8.8–9.0,carbonate/sulfide addition,anoxic dispensing and later filtered lactate/vitamins. Preserve this substantial existing context; no specific autoclave temperature/time or lactate-stock strength is supplied."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing text and AUTOCLAVE classification retain the source order,100%N2 for30–45min,pH8.8–9.0,carbonate/sulfide addition,anoxic dispensing and later filtered lactate/vitamins. Preserve this substantial existing context; no specific autoclave temperature/time or lactate-stock strength is supplied."}]},{"quantity_id":"q46","label":"Retained SL-10 preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The existing DISSOLVE action and complete instruction are source-supported, including the final1000ml make-up continued on page2. Correct its unqualified main-step placement by binding it to SL-10; this stock volume does not replace the main1003ml declaration.","source_stage":"SL-10 preparation","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The existing DISSOLVE action and complete instruction are source-supported, including the final1000ml make-up continued on page2. Correct its unqualified main-step placement by binding it to SL-10; this stock volume does not replace the main1003ml declaration."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The existing DISSOLVE action and complete instruction are source-supported, including the final1000ml make-up continued on page2. Correct its unqualified main-step placement by binding it to SL-10; this stock volume does not replace the main1003ml declaration."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:001960.

All asserted ontology objects were checked for current labels, formulas, hydrate and stereo scope. Catalogue synonyms and preferred rows were joined exactly; broad extra synonym mappings do not certify a different salt or hydrate. Exact rejected spellings can coexist with mapped equivalent names. Missing yeast secondary links are a bounded completeness follow-up, without inventing a new asserted identifier. The confirmed mismatches are neutral resazurin versus the named sodium salt, and anhydrous nickel versus hexahydrate. Current CHEBI:31345 synonyms and stereochemical structure support D-calcium pantothenate despite its short canonical label; sodium L-lactate is likewise specific. Generic lipoic acid16494 is compatible with the explicitly retained DL qualifier but does not independently encode a racemate. B12 remains the source-named vitamer class. No unused mmol_l conversion is certified.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:001960.

All three complete reports and the75-claim selected parent were read. Its33 unchanged local concentrations and42 source recipe/step objects join to the fresh raw API, whose digest matches the historical capture. Current evidence now credits eleven main normalized rates on the primary1003ml basis; the old blanket topology conflict is not adopted for those rates. The22 stock entries still need source-stage restoration, with acid conversion separately unresolved. Current singleton and parser behaviors are distinct from historical execution.

## Findings

### f1: Twenty-two stock entries are flattened into the main medium

major / open / confirmed; issue key: culturemech-001960-stock-stage.

Preserve the eleven main rates supported by the explicit1003ml source basis. Restore SL-10, selenite-tungstate and Wolin10x stock definitions and their separate1ml batch doses instead of interpreting the22 stock entries as final-medium concentrations. Preserve the sodium-resazurin0.1% w/v stock addition. Current composition parsing now separates these stock references, but bare-ml normalization still requires source-basis review.

### f2: The HCl mass conversion lacks a source percent basis

major / open / confirmed; issue key: culturemech-001960-acid-percent-basis.

Retain SL-10 input10ml HCl(25%) and its explicit1000ml final make-up. The provider2.5g/L number does not resolve whether25% is w/w or w/v, nor a needed density; do not endorse it as source-supported mass or final-medium concentration. Bind the exact stock dose/strength evidence without inventing a percent basis.

### f3: Sodium resazurin and nickel hydrate have mismatched assertions

major / open / confirmed; issue key: culturemech-001960-supplied-forms.

Sodium resazurin uses neutral CHEBI:8806, whose current formula lacks sodium; resolve the exact salt identifier and label without guessing. CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do not reject the whole identifier. Correct both nickel primary and secondary assertions, preserving supported source amounts and stage.

### f4: SL-10 make-up is presented as a main preparation step

major / open / confirmed; issue key: culturemech-001960-stock-preparation.

Keep the complete source-supported SL-10 DISSOLVE text, but move its scope to that stock. Its1000ml make-up must not override the main1003ml source declaration. Keep the supported main preparation and pH range. Current preparation collector still concatenates steps from all solution sections without stage labels.

### f5: The supported assertions lack attached claim evidence

minor / open / confirmed; issue key: culturemech-001960-claim-evidence.

Attach exact ingredient evidence for amounts and chemical forms, and root evidence with field/stage scope for water, receiving doses, final volume,pH and preparation. No attached claims currently exist. Historical source-byte equality is separately documented, and does not recover original access events.

## Recommended Actions And Acceptance Checks

### a1

Preserve the eleven main rates supported by the explicit1003ml source basis. Restore SL-10, selenite-tungstate and Wolin10x stock definitions and their separate1ml batch doses instead of interpreting the22 stock entries as final-medium concentrations. Preserve the sodium-resazurin0.1% w/v stock addition. Current composition parsing now separates these stock references, but bare-ml normalization still requires source-basis review.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Retain SL-10 input10ml HCl(25%) and its explicit1000ml final make-up. The provider2.5g/L number does not resolve whether25% is w/w or w/v, nor a needed density; do not endorse it as source-supported mass or final-medium concentration. Bind the exact stock dose/strength evidence without inventing a percent basis.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Sodium resazurin uses neutral CHEBI:8806, whose current formula lacks sodium; resolve the exact salt identifier and label without guessing. CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do not reject the whole identifier. Correct both nickel primary and secondary assertions, preserving supported source amounts and stage.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Keep the complete source-supported SL-10 DISSOLVE text, but move its scope to that stock. Its1000ml make-up must not override the main1003ml source declaration. Keep the supported main preparation and pH range. Current preparation collector still concatenates steps from all solution sections without stage labels.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Attach exact ingredient evidence for amounts and chemical forms, and root evidence with field/stage scope for water, receiving doses, final volume,pH and preparation. No attached claims currently exist. Historical source-byte equality is separately documented, and does not recover original access events.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz813b | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf; REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api813b | https://mediadive.dsmz.de/rest/medium/813b; REVIEW_WORK/batch077/source01-03-supplement/api813b.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch077/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-16 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_lacustre_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch077/record02/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch077/record02/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch077/record02/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_composition_ingredients; _parse_api_composition; _is_api_stock_addition; _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps; _classify_preparation_action | context_only | Current composition parsing reads the first API solution only, skips water and explicit stock or percent-bearing ml references, and prioritizes supplied g_l. Solution parsing preserves the first-section stock references but normalizes bare ml to ML_PER_L. Preparation parsing concatenates every solution step without stage labels. For all-stock primary tables, API composition returns None and PDF fallback or a placeholder remains possible; no regeneration outcome is presumed. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| full-history-pool | REVIEW_WORK/batch077/validation-authors/full-history-pool.json; Complete artifact | context_only | All thirteen reports across these three records are losslessly routed through 619 exact cells; each selected record retains its own complete report reader. No neighboring formulation transfer. |
| full-catalog | REVIEW_WORK/batch077/validation-authors/mim-full-scope.json; Complete artifact | context_only | All exact asserted identifier/ontology_id and supplied-name catalogue joins, plus candidate nickel hexahydrate; preferred-label statuses are interpreted separately from chemical identity. |
| selected-parent-authentication | REVIEW_WORK/batch077/record02/selected-parent-authentication.json; Complete artifact | context_only | Exact selected parent objects, unchanged current local fields and all literal/decoded current API claims checked separately from attached evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch077/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch077/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch077/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch077/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch077/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch077/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch077/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch077/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch077/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi232798 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:232798; REVIEW_WORK/batch077/source01-03-supplement/chebi232798.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch077/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch077/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch077/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch077/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch077/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch077/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch077/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch077/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch077/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch077/source01-03-supplement/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; REVIEW_WORK/batch077/source01-03-supplement/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; REVIEW_WORK/batch077/source01-03-supplement/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch077/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch077/source01-03-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch077/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch077/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch077/source01-03-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch077/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch077/source01-03-supplement/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch077/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch077/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch077/source01-03-supplement/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch077/record02/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch077/record02/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch077/record02/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch077/record02/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch077/record02/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch077/record02/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch077/record02/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch077/record02/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch077/record02/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch077/record02/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch077/record02/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch077/record02/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The DSM112796 substitution printed on the primary is excluded from generic813b quantity assessment; its pyruvate amount is not imported into the selected record.
- Primary1003ml is an explicit source declaration. Source water inputs, stock provider volumes and measured final volume remain distinct; no unused molar-rate assertion is validated.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T202019Z-culturemech-001960-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFONATRONUM LACUSTRE MEDIUM'
started_at: '2026-10-28T20:15:13.321875Z'
finished_at: '2026-10-28T20:20:19.378061Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, exact
    captured sources, fresh scoped primary sources and original diagnostics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: DSM813b retains eleven source-supported main rates, final pH and substantial
  preparation, while22 stock entries and SL-10 preparation are misplaced at root.
  Restore stock scope, keep HCl percent basis unresolved, correct sodium-resazurin/nickel
  form assertions and attach exact evidence.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/SKILL.md
    sha256: a67993ef11cf374ac579c53252bc603f9894ebd69cad711b11f293714c76621e
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
    sha256: e3ce277049a540011d8ca05de38b42b39247cdcf55c50e71b7c3364395f6785c
    role: target
  - path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    sha256: 286b7e433b697a5fbb3c71cd7dc4b1f6380e9613c2177a60c54f957c15853feb
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_lacustre_medium.yaml.md
    sha256: f9cf70389c17473602522de4eaf55c668d520ee8fdea2db388430c3fca093aaf
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.md
    sha256: 030fc7520b2557a4374acdb942e2bff9fc800c1b44a42caed3b084aef2b411c9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.md
    sha256: 9eadf1c9ef421255c2f025e31818e8377ae2820c9696a2b301c0656f8c5b7b09
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Whole exact target/owner with explicit scoped dependencies, current
    sources and historical claims.
  selection: Authoritative batch077 index 02
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001960
targets:
- target_id: CultureMech:001960
  path: data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
  label: desulfonatronum_lacustre_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001960
  command: just validate-schema data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001960
  command: just validate-strict data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
    --out REVIEW_WORK/batch077/record02/strict.tsv --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001960
  command: just validate-terms data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001960
  command: just validate-references data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz813b
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf
  accessed_at: '2026-10-28T20:15:33.094577Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951
- evidence_id: api813b
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/813b
  accessed_at: '2026-10-28T20:15:32.926861Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/api813b.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T20:15:38.694861Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:20:19.214502Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: e3ce277049a540011d8ca05de38b42b39247cdcf55c50e71b7c3364395f6785c
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:20:19.214678Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 286b7e433b697a5fbb3c71cd7dc4b1f6380e9613c2177a60c54f957c15853feb
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T20:20:19.214709Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T20:20:19.215016Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T20:20:19.215041Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T20:20:19.215062Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-16
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:20:19.215088Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_lacustre_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T20:20:19.221519Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f9cf70389c17473602522de4eaf55c668d520ee8fdea2db388430c3fca093aaf
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T20:20:19.221598Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 030fc7520b2557a4374acdb942e2bff9fc800c1b44a42caed3b084aef2b411c9
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T20:20:19.221628Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 9eadf1c9ef421255c2f025e31818e8377ae2820c9696a2b301c0656f8c5b7b09
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/historical-reading.json
  accessed_at: '2026-10-28T20:20:19.221660Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 081698822d0c12b28685d1c27d74490eedbcd533872e6fbdab0f07f795b3f241
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:20:19.221941Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 9c79830598ea5d6d74a80b5554bf3c90df82be6b84137a4913431b368ed43cca
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/complete-document-reader.json
  accessed_at: '2026-10-28T20:20:19.222129Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 0ba56b8f4d2f3aeb135f4cb68ca650538e1af85b956533a0c2a1130b85483093
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_composition_ingredients; _parse_api_composition; _is_api_stock_addition;
    _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps;
    _classify_preparation_action
  accessed_at: '2026-10-28T20:20:19.222296Z'
  support: context_only
  summary: Current composition parsing reads the first API solution only, skips water
    and explicit stock or percent-bearing ml references, and prioritizes supplied
    g_l. Solution parsing preserves the first-section stock references but normalizes
    bare ml to ML_PER_L. Preparation parsing concatenates every solution step without
    stage labels. For all-stock primary tables, API composition returns None and PDF
    fallback or a placeholder remains possible; no regeneration outcome is presumed.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T20:20:19.222335Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: full-history-pool
  kind: record_content
  reference: REVIEW_WORK/batch077/validation-authors/full-history-pool.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:20:19.222364Z'
  support: context_only
  summary: All thirteen reports across these three records are losslessly routed through
    619 exact cells; each selected record retains its own complete report reader.
    No neighboring formulation transfer.
  snapshot_sha256: 35d1e79d61d4d348a952a6faa00bfb1a397d30f96995ea913be0822f2024612e
- evidence_id: full-catalog
  kind: record_content
  reference: REVIEW_WORK/batch077/validation-authors/mim-full-scope.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:20:19.222452Z'
  support: context_only
  summary: All exact asserted identifier/ontology_id and supplied-name catalogue joins,
    plus candidate nickel hexahydrate; preferred-label statuses are interpreted separately
    from chemical identity.
  snapshot_sha256: 741b684f47194d97bb0a782ece7136465d7c31c2d1c94480aad6d3518ef55158
- evidence_id: selected-parent-authentication
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/selected-parent-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:20:19.267699Z'
  support: context_only
  summary: Exact selected parent objects, unchanged current local fields and all literal/decoded
    current API claims checked separately from attached evidence.
  snapshot_sha256: bc023413bf16ddef8d4a9a18f01c2fd19fee606bb2562bd41577c432d958a7c6
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T20:15:38.928795Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T20:15:40.018436Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T20:15:36.517340Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T20:15:37.461125Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T20:15:37.110930Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T20:15:35.818421Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T20:15:40.227947Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T20:15:35.931240Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T20:15:39.562551Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi232798
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:232798
  accessed_at: '2026-10-28T20:15:35.605164Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi232798.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e4ec30f25cb150a18cf079d820943cdc9f6b849b2fae5b6448d6cad204994a4c
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T20:15:35.346986Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T20:15:39.644345Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T20:15:38.325603Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T20:15:40.167533Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T20:15:37.732850Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T20:15:38.429348Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T20:15:39.888563Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T20:15:37.828199Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T20:15:39.301964Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  accessed_at: '2026-10-28T20:15:37.008413Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32145.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  accessed_at: '2026-10-28T20:15:33.939796Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi131361.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  accessed_at: '2026-10-28T20:15:39.046444Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi63939.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T20:15:34.591885Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T20:15:35.966282Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi27470.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T20:15:36.413596Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T20:15:38.248432Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T20:15:35.268960Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi17015.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T20:15:34.543633Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T20:15:36.590790Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi31345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T20:15:35.188321Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T20:15:36.260740Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T20:15:34.708700Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi16494.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.375953Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: cc1771f98d55cb40deb6fabb14b48026dd9b6716b3c7f7eeefb74a5131f7331d
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.376077Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: f2e0f9a18b4deae8bdf7cb1e8be2dba0bb051c57476d99c66c01b2bb3f553954
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.376238Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: f8051cdb98df07ea113009318f0a248b4c4253fc74aa2aedaa6af863b7cfb9b0
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.376309Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 806d6838b999a8a67bd43df1f1ce4f3f4c50e8b4dd2d8148cb13a402ead63030
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.376372Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: b693f1b9c7ceca3ade582eda5e2fd906a629a187775ad499bb8921a3a2d6059d
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.376411Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 8282f236fdf0e72f0f06c531de7e044629eb24d5d0122d2b7498fc74fe770ae7
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:20:19.376443Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch077/record02/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T20:20:19.376473Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: ce6dbe70086b8379aac4a16a6b8717aa674582b52922b5aa5bf3f8debe5feefa
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch077/record02/validate-schema.json
  accessed_at: '2026-10-28T20:15:14.348851Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 9f81b927845bb633540a9272847700c047283706104c9e1038edc887ca9c552e
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch077/record02/validate-strict.json
  accessed_at: '2026-10-28T20:15:15.283635Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 89df7cf14d805248761a94be440fa2960f9cc9b05f1540f1dfa5e5c32b2cec4b
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch077/record02/validate-terms.json
  accessed_at: '2026-10-28T20:15:16.299692Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 9f500fc9704ceb3e578bc0a07df3f13bc2369063f7e9490c8f85164d3b01bee9
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch077/record02/validate-references.json
  accessed_at: '2026-10-28T20:15:17.051483Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 7907e3a7c4ec3e6f174850a3527f44b30fa7d9a476ad2dc37d15ed5b05d779ea
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSM813b generic formulation
  outcome: supported
  summary: Target and single maintained owner have identical scientific fields. Current
    primary and API agree on DSM813b with L-lactate and low NaCl. DSM813/813a are
    separate formulations. The printed DSM112796 pyruvate substitution is excluded
    because the selected record is the generic813b formulation; no strain-growth inference
    is made.
  target_ids:
  - CultureMech:001960
  evidence_ids:
  - target
  - owner
  - dsmz813b
  - api813b
- assessment_id: classification
  area: representation
  topic: Complex liquid formulation
  outcome: supported
  summary: Yeast extract supports the complex/undefined classification. No agar or
    other solidifying agent is present in the exact generic formulation.
  target_ids:
  - CultureMech:001960
  evidence_ids:
  - target
  - dsmz813b
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 66 current concentration fields are covered by 46 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001960
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b077-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","quantity_field_count":66,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 7-7","quote":"KH2PO4                                                     0.20         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\":
    1.46527,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q2","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 8-8","quote":"MgCl2 x 6 H2O                                              0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    0.490405,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 9-9","quote":"NH4Cl                                                      1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 10-10","quote":"KCl                                                        0.20         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\":
    2.67474,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q5","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.98504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.98504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 11-11","quote":"Na2SO4                                                     5.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.98504,\n                        \"mmol_l\":
    35.0961,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 12-12","quote":"NaCl                                                       2.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.99402,\n                        \"mmol_l\":
    34.1208,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q7","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 15-15","quote":"Yeast extract                                              1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q8","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement. The primary0.5ml of0.1% w/v sodium-resazurin
    stock supplies0.5mg per batch; preserve that stock dose and strength as well as
    the supported normalized rate. Its sodium-salt grounding is assessed separately.","source_stage":"Main
    medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 16-16","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement. The primary0.5ml of0.1% w/v sodium-resazurin
    stock supplies0.5mg per batch; preserve that stock dose and strength as well as
    the supported normalized rate. Its sodium-salt grounding is assessed separately."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement. The primary0.5ml of0.1% w/v sodium-resazurin
    stock supplies0.5mg per batch; preserve that stock dose and strength as well as
    the supported normalized rate. Its sodium-salt grounding is assessed separately."}]},{"quantity_id":"q9","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.48953","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.48953","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 17-17","quote":"Na2CO3                                                     3.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 3.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.48953,\n                        \"mmol_l\":
    32.9238,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q10","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement.","source_stage":"Main medium on
    declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 18-18","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    2.07553,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement."}]},{"quantity_id":"q11","label":"Na-L-lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1.99402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement. The exact source specifies L-lactate;
    keep that stereochemistry and the separately filtered anoxic-stock addition. No
    concentration of that separate lactate stock is supplied.","source_stage":"Main
    medium on declared1003ml basis","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 19-19","quote":"Na-L-lactate                                               2.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na-L-lactate\",\n                        \"compound_id\":
    265,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.99402,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement. The exact source specifies L-lactate;
    keep that stereochemistry and the separately filtered anoxic-stock addition. No
    concentration of that separate lactate stock is supplied."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    local G_PER_L number agrees with the exact provider main g_l and the primary batch
    amount on its explicitly declared final1003ml basis. Credit and retain this rate;
    do not replace it with the undivided per1000ml input-water amount. Source-declared
    final volume is not an independent measurement. The exact source specifies L-lactate;
    keep that stereochemistry and the separately filtered anoxic-stock addition. No
    concentration of that separate lactate stock is supplied."}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly reports2.5g/L, but the primary specifies10ml HCl(25%) in SL-10
    and does not establish the percent basis or density needed to endorse that conversion.
    Preserve exact10ml and25% as source assertions; restore stock scope and do not
    carry2.5g/L into the final medium or silently infer w/v.","source_stage":"SL-10
    trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 37-37","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    provider explicitly reports2.5g/L, but the primary specifies10ml HCl(25%) in SL-10
    and does not establish the percent basis or density needed to endorse that conversion.
    Preserve exact10ml and25% as source assertions; restore stock scope and do not
    carry2.5g/L into the final medium or silently infer w/v."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    provider explicitly reports2.5g/L, but the primary specifies10ml HCl(25%) in SL-10
    and does not establish the percent basis or density needed to endorse that conversion.
    Preserve exact10ml and25% as source assertions; restore stock scope and do not
    carry2.5g/L into the final medium or silently infer w/v."}]},{"quantity_id":"q13","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 38-38","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 39-39","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 40-40","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 41-41","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 42-42","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 43-43","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 44-44","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up.","source_stage":"SL-10 trace stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 45-45","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. SL-10 has an
    explicit1000ml final make-up."}]},{"quantity_id":"q21","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Selenite-tungstate
    stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 63-63","quote":"NaOH                                        0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q22","label":"Na2SeO3
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Selenite-tungstate
    stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 64-64","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q23","label":"Na2WO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Selenite-tungstate
    stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 65-65","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q24","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 71-71","quote":"Biotin                                     20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q25","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 72-72","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q26","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 73-73","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q27","label":"Thiamine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 74-74","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q28","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 75-75","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q29","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 76-76","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q30","label":"Calcium
    D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 77-77","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q31","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 78-78","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[30].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q32","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 79-79","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[31].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q33","label":"(DL)-alpha-Lipoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up.","source_stage":"Wolin10x
    vitamin stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 80-80","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ingredients[32].concentration","decision":"correct","rationale":"The
    local scalar agrees with the exact provider stock g_l and primary mass. Credit
    the existing stock strength on its declared basis, but correct its unqualified
    main-medium placement and preserve the separate1ml receiving dose. The stock table
    lists1000ml water and provider declares1000ml stock volume; these remain declared
    input/normalization facts, not an independently measured make-up."}]},{"quantity_id":"q34","label":"SL-10
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the printed1ml batch dose and exact stock identity. The completed medium is explicitly1003ml;
    bare ml is not an unqualified ml/L dose. Do not flatten its stock components.","source_stage":"Source-only
    stock receiving dose","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 13-13","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q35","label":"Selenite-tungstate
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the printed1ml batch dose and exact stock identity. The completed medium is explicitly1003ml;
    bare ml is not an unqualified ml/L dose. Do not flatten its stock components.","source_stage":"Source-only
    stock receiving dose","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 14-14","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q36","label":"Wolin10x
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the printed1ml batch dose and exact stock identity. The completed medium is explicitly1003ml;
    bare ml is not an unqualified ml/L dose. Do not flatten its stock components.","source_stage":"Source-only
    stock receiving dose","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 20-20","quote":"Wolin''s vitamin solution (10x)                             1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Sodium-resazurin
    dose and stock strength","local_fields":[],"decision":"evidence_only","rationale":"Preserve0.5ml
    of0.1% w/v sodium-resazurin stock, supplying0.5mg per batch. The main supported
    rate uses the declared1003ml denominator; these source stock controls remain independently
    visible.","source_stage":"Source-only dye stock","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 16-16","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q38","label":"main
    input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed solvent input in its exact source section. SL-10 separately states
    final make-up, while the final main1003ml declaration and the other stock provider
    volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 21-21","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"SL-10 input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed solvent input in its exact source section. SL-10 separately states
    final make-up, while the final main1003ml declaration and the other stock provider
    volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 46-46","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"selenite-tungstate
    input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed solvent input in its exact source section. SL-10 separately states
    final make-up, while the final main1003ml declaration and the other stock provider
    volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 66-66","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"vitamin input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed solvent input in its exact source section. SL-10 separately states
    final make-up, while the final main1003ml declaration and the other stock provider
    volume fields have their own scope.","source_stage":"Source-only water","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 81-81","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q42","label":"Main declared final
    volume","local_fields":[],"decision":"evidence_only","rationale":"The primary
    explicitly declares1003ml final medium volume, agreeing with the API normalization.
    Retain that source basis without claiming independent measurement or reconstructing
    a different total from omissions in the schematic table.","source_stage":"Completed
    medium","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 4-4","quote":"Final volume: 1003 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q43","label":"SL-10
    final make-up","local_fields":[],"decision":"evidence_only","rationale":"The source
    starts with acid and water inputs and explicitly makes up to1000ml. Preserve the
    final-volume instruction, including the page break; do not add a further litre
    after the listed990ml.","source_stage":"SL-10 stock final volume","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 37-37","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 46-48","quote":"Distilled water                                           990.00      ml\n\nFirst
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q44","label":"Retained final
    pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ph_range","stored":{"min":8.8,"max":9.0}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ph_range","stored":{"min":8.8,"max":9.0}}],"decision":"evidence_only","rationale":"The
    exact8.8–9.0 range is supported by the primary main preparation and header. It
    is not transferred to a stock or the excluded DSM112796 substitution.","source_stage":"Completed-medium
    pH","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 3-3","quote":"Final pH: 8.8 - 9.0","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 23-27","quote":"Dissolve ingredients (except carbonate, sulfide, lactate,
    and vitamins) and sparge medium\nwith 100 % N2 gas for 30 - 45 min to make it
    anoxic. Add and dissolve carbonate and\nsulfide, then adjust pH to 8.8 - 9.0,
    dispense under 100% N2 gas atmosphere into\nHungate-type tubes or serum vials
    and autoclave. Before use add lactate and vitamins\n(sterilized by filtration)
    from sterile anoxic stock solutions prepared under 100% N2 gas.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    exact8.8–9.0 range is supported by the primary main preparation and header. It
    is not transferred to a stock or the excluded DSM112796 substitution."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    exact8.8–9.0 range is supported by the primary main preparation and header. It
    is not transferred to a stock or the excluded DSM112796 substitution."}]},{"quantity_id":"q45","label":"Retained
    main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium
    with 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate
    and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere
    into Hungate-type tubes or serum vials and autoclave. Before use add lactate and
    vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared
    under 100% N2 gas."}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients (except carbonate, sulfide, lactate, and vitamins) and sparge medium
    with 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate
    and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere
    into Hungate-type tubes or serum vials and autoclave. Before use add lactate and
    vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared
    under 100% N2 gas."}}],"decision":"evidence_only","rationale":"The existing text
    and AUTOCLAVE classification retain the source order,100%N2 for30–45min,pH8.8–9.0,carbonate/sulfide
    addition,anoxic dispensing and later filtered lactate/vitamins. Preserve this
    substantial existing context; no specific autoclave temperature/time or lactate-stock
    strength is supplied.","source_stage":"Main preparation","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 23-27","quote":"Dissolve ingredients (except carbonate, sulfide, lactate,
    and vitamins) and sparge medium\nwith 100 % N2 gas for 30 - 45 min to make it
    anoxic. Add and dissolve carbonate and\nsulfide, then adjust pH to 8.8 - 9.0,
    dispense under 100% N2 gas atmosphere into\nHungate-type tubes or serum vials
    and autoclave. Before use add lactate and vitamins\n(sterilized by filtration)
    from sterile anoxic stock solutions prepared under 100% N2 gas.","quote_basis":"derivative
    text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients (except carbonate, sulfide, lactate, and vitamins) and
    sparge medium with 100 % N2 gas for 30 - 45 min to make it anoxic. Add and dissolve
    carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas
    atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add
    lactate and vitamins (sterilized by filtration) from sterile anoxic stock solutions
    prepared under 100% N2 gas.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing text and AUTOCLAVE classification retain the source order,100%N2 for30–45min,pH8.8–9.0,carbonate/sulfide
    addition,anoxic dispensing and later filtered lactate/vitamins. Preserve this
    substantial existing context; no specific autoclave temperature/time or lactate-stock
    strength is supplied."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing text and AUTOCLAVE classification retain the source order,100%N2 for30–45min,pH8.8–9.0,carbonate/sulfide
    addition,anoxic dispensing and later filtered lactate/vitamins. Preserve this
    substantial existing context; no specific autoclave temperature/time or lactate-stock
    strength is supplied."}]},{"quantity_id":"q46","label":"Retained SL-10 preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The existing
    DISSOLVE action and complete instruction are source-supported, including the final1000ml
    make-up continued on page2. Correct its unqualified main-step placement by binding
    it to SL-10; this stock volume does not replace the main1003ml declaration.","source_stage":"SL-10
    preparation","sources":[{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 48-48","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally","quote_basis":"derivative text"},{"evidence_id":"dsmz813b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813b.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813b.bin","raw_sha256":"2fdf4e83bff0cc329372d9c19f91b4d093490ab86e62f1c58765ccc7a4dd8951","text_sha256":"d1c61b9d6f7a4873210823f324f44e0efa47d4c833d5bf0d8aaaf139abffd738","accessed_at":"2026-10-28T20:15:33.094577Z","locator":"dsmz813b.txt
    lines 58-58","quote":"make up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813b","reference":"https://mediadive.dsmz.de/rest/medium/813b","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813b.bin","raw_sha256":"09ac3e8cdb69be5ae75fd484325d8ad5df8c2486a3493458ae91fdb097686446","text_sha256":"f8b80e3989029ad0401f66a758ef453c84fe36f29bd90311559d93600921d598","accessed_at":"2026-10-28T20:15:32.926861Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    existing DISSOLVE action and complete instruction are source-supported, including
    the final1000ml make-up continued on page2. Correct its unqualified main-step
    placement by binding it to SL-10; this stock volume does not replace the main1003ml
    declaration."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    existing DISSOLVE action and complete instruction are source-supported, including
    the final1000ml make-up continued on page2. Correct its unqualified main-step
    placement by binding it to SL-10; this stock volume does not replace the main1003ml
    declaration."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONUM_LACUSTRE_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted ontology objects were checked for current labels, formulas,
    hydrate and stereo scope. Catalogue synonyms and preferred rows were joined exactly;
    broad extra synonym mappings do not certify a different salt or hydrate. Exact
    rejected spellings can coexist with mapped equivalent names. Missing yeast secondary
    links are a bounded completeness follow-up, without inventing a new asserted identifier.
    The confirmed mismatches are neutral resazurin versus the named sodium salt, and
    anhydrous nickel versus hexahydrate. Current CHEBI:31345 synonyms and stereochemical
    structure support D-calcium pantothenate despite its short canonical label; sodium
    L-lactate is likewise specific. Generic lipoic acid16494 is compatible with the
    explicitly retained DL qualifier but does not independently encode a racemate.
    B12 remains the source-named vitamer class. No unused mmol_l conversion is certified.
  target_ids:
  - CultureMech:001960
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All three complete reports and the75-claim selected parent were read. Its33
    unchanged local concentrations and42 source recipe/step objects join to the fresh
    raw API, whose digest matches the historical capture. Current evidence now credits
    eleven main normalized rates on the primary1003ml basis; the old blanket topology
    conflict is not adopted for those rates. The22 stock entries still need source-stage
    restoration, with acid conversion separately unresolved. Current singleton and
    parser behaviors are distinct from historical execution.
  target_ids:
  - CultureMech:001960
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-source-joins
  - historical-reading
  - historical-selected-parent-rows
  - selected-parent-authentication
  - writer-mediadive
findings:
- finding_id: f1
  issue_key: culturemech-001960-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Twenty-two stock entries are flattened into the main medium
  description: Preserve the eleven main rates supported by the explicit1003ml source
    basis. Restore SL-10, selenite-tungstate and Wolin10x stock definitions and their
    separate1ml batch doses instead of interpreting the22 stock entries as final-medium
    concentrations. Preserve the sodium-resazurin0.1% w/v stock addition. Current
    composition parsing now separates these stock references, but bare-ml normalization
    still requires source-basis review.
  target_ids:
  - CultureMech:001960
  field_paths:
  - ingredients[11:33].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz813b
  - api813b
  - quantities
  - writer-mediadive
  rule_id: custom/stock-stage
  native_severity: P2
  normalization_reason: Exact source-specific quantity issue, normalized major. This
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
- finding_id: f2
  issue_key: culturemech-001960-acid-percent-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The HCl mass conversion lacks a source percent basis
  description: Retain SL-10 input10ml HCl(25%) and its explicit1000ml final make-up.
    The provider2.5g/L number does not resolve whether25% is w/w or w/v, nor a needed
    density; do not endorse it as source-supported mass or final-medium concentration.
    Bind the exact stock dose/strength evidence without inventing a percent basis.
  target_ids:
  - CultureMech:001960
  field_paths:
  - ingredients[11].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz813b
  - api813b
  - quantities
  rule_id: custom/acid-percent-basis
  native_severity: P2
  normalization_reason: Exact source-specific quantity issue, normalized major. This
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
- finding_id: f3
  issue_key: culturemech-001960-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin and nickel hydrate have mismatched assertions
  description: Sodium resazurin uses neutral CHEBI:8806, whose current formula lacks
    sodium; resolve the exact salt identifier and label without guessing. CHEBI:34887
    is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current
    CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel
    (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and
    synonym row6704 is MAPPED. These spelling-specific statuses do not reject the
    whole identifier. Correct both nickel primary and secondary assertions, preserving
    supported source amounts and stage.
  target_ids:
  - CultureMech:001960
  field_paths:
  - ingredients[7].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz813b
  - api813b
  - groundings
  - chebi53542
  - full-catalog
  rule_id: custom/supplied-forms
  native_severity: P2
  normalization_reason: Exact source-specific grounding issue, normalized major. This
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-001960-stock-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SL-10 make-up is presented as a main preparation step
  description: Keep the complete source-supported SL-10 DISSOLVE text, but move its
    scope to that stock. Its1000ml make-up must not override the main1003ml source
    declaration. Keep the supported main preparation and pH range. Current preparation
    collector still concatenates steps from all solution sections without stage labels.
  target_ids:
  - CultureMech:001960
  field_paths:
  - preparation_steps[1]
  - ph_range
  evidence_ids:
  - dsmz813b
  - api813b
  - quantities
  - writer-mediadive
  rule_id: custom/stock-preparation
  native_severity: P2
  normalization_reason: Exact source-specific completeness issue, normalized major.
    This custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
- finding_id: f5
  issue_key: culturemech-001960-claim-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The supported assertions lack attached claim evidence
  description: Attach exact ingredient evidence for amounts and chemical forms, and
    root evidence with field/stage scope for water, receiving doses, final volume,pH
    and preparation. No attached claims currently exist. Historical source-byte equality
    is separately documented, and does not recover original access events.
  target_ids:
  - CultureMech:001960
  field_paths:
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - old-claims
  - historical-source-joins
  - selected-parent-authentication
  - dsmz813b
  - api813b
  rule_id: custom/claim-evidence
  native_severity: P3
  normalization_reason: Exact source-specific completeness issue, normalized minor.
    This custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Preserve the eleven main rates supported by the explicit1003ml source
    basis. Restore SL-10, selenite-tungstate and Wolin10x stock definitions and their
    separate1ml batch doses instead of interpreting the22 stock entries as final-medium
    concentrations. Preserve the sodium-resazurin0.1% w/v stock addition. Current
    composition parsing now separates these stock references, but bare-ml normalization
    still requires source-basis review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001960
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Retain SL-10 input10ml HCl(25%) and its explicit1000ml final make-up.
    The provider2.5g/L number does not resolve whether25% is w/w or w/v, nor a needed
    density; do not endorse it as source-supported mass or final-medium concentration.
    Bind the exact stock dose/strength evidence without inventing a percent basis.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001960
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Sodium resazurin uses neutral CHEBI:8806, whose current formula lacks
    sodium; resolve the exact salt identifier and label without guessing. CHEBI:34887
    is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current
    CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel
    (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and
    synonym row6704 is MAPPED. These spelling-specific statuses do not reject the
    whole identifier. Correct both nickel primary and secondary assertions, preserving
    supported source amounts and stage.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001960
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: Keep the complete source-supported SL-10 DISSOLVE text, but move its
    scope to that stock. Its1000ml make-up must not override the main1003ml source
    declaration. Keep the supported main preparation and pH range. Current preparation
    collector still concatenates steps from all solution sections without stage labels.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001960
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: Attach exact ingredient evidence for amounts and chemical forms, and
    root evidence with field/stage scope for water, receiving doses, final volume,pH
    and preparation. No attached claims currently exist. Historical source-byte equality
    is separately documented, and does not recover original access events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001960
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_lacustre_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- The DSM112796 substitution printed on the primary is excluded from generic813b quantity
  assessment; its pyruvate amount is not imported into the selected record.
- Primary1003ml is an explicit source declaration. Source water inputs, stock provider
  volumes and measured final volume remain distinct; no unused molar-rate assertion
  is validated.
- No strain-growth claim, optimization or experimental recommendation is inferred
  from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent
  rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed
  only on their declared normalization basis; unspecified percent bases and hydrate
  numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was
  performed by this author.
```
