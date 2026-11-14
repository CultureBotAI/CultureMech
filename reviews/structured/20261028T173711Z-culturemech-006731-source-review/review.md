# Scientific review: DENITROVIBRIO MEDIUM

- Review: 20261028T173711Z-culturemech-006731-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T17:18:18.316625Z
- Finished UTC: 2026-10-28T17:37:11.298087Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM881 supplies exact batch quantities and provider-declared main rates, but stock components remain incompletely nested and the generated record predates its owners’ five-component repairs. Current primary pH/anoxic preparation conflicts with KOMODO-derived metadata, and sodium-resazurin/nickel identities require correction. Correct owner preparation and nested rates are credited; no measured final volume is inferred. Four original canonical checks passed, while direct KOMODO verification remains partial.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch073 index 02
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006731 | data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml | generated | denitrovibrio_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:006731 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:006731 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:006731 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:006731 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### DSM881 and historical KOMODO mapping

identity: unknown. Targets: CultureMech:006731.

The current primary and provider agree on DSM881. The historical KOMODO mapping reports a different pH range and the exact current accession/catalogue routes return 403; direct KOMODO version verification remains incomplete. Neighboring TOGO names found in old reports are not current merge owners or evidence substitutes.

### Defined liquid and atmosphere discrepancy

scope: concern. Targets: CultureMech:006731.

The chemically specified recipe and absence of agar support defined liquid scope. The Aerobic: Yes note conflicts with explicit anoxic preparation; no strain cultivation or temperature inference is made.

### Declared provider main rates and corrected stock scope

evidence: concern. Targets: CultureMech:006731.

Twelve unchanged main rates match current explicit provider g_l; they are credited on that provider basis, not as independently measured primary final concentrations. Existing five-component nesting is credited, and source-only volumes, pH and every preparation control are inventoried separately.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:006731.

97 current concentration fields are covered by 41 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b073-quantity-inventory-v1","target":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","quantity_field_count":97,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 3-3","quote":"Na2SO4                                                     0.02         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\": 0.140384,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 4-4","quote":"KH2PO4                                                     1.00         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 7.32637,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 5-5","quote":"NH4Cl                                                      0.25         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\": 4.65979,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"19.9402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"19.9402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"19.9402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 6-6","quote":"NaCl                                                      20.00         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.9402,\n                        \"mmol_l\": 341.208,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.99103","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.99103","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.99103","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 7-7","quote":"MgCl2 x 6 H2O                                              3.00         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\": 14.7122,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 8-8","quote":"KCl                                                        0.50         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 6.68685,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.149551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.149551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.149551","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 9-9","quote":"CaCl2 x 2 H2O                                              0.15         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q8","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.63509","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.63509","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.63509","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 10-10","quote":"Na-acetate                                                 1.64         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 1.64,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.63509,\n                        \"mmol_l\": 19.932,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q9","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration. The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution; the stock strength and receiving volume are retained separately from the provider rate and the incorrect neutral ontology identity.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 13-13","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration. The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution; the stock strength and receiving volume are retained separately from the provider rate and the incorrect neutral ontology identity."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration. The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution; the stock strength and receiving volume are retained separately from the provider rate and the incorrect neutral ontology identity."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration. The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution; the stock strength and receiving volume are retained separately from the provider rate and the incorrect neutral ontology identity."}]},{"quantity_id":"q10","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 14-14","quote":"Na2CO3                                                     1.00         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 9.40681,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q11","label":"Na2-fumarate","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6.38086","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6.38086","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6.38086","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 15-15","quote":"Na2-fumarate                                               6.40         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\": 276,\n                        \"amount\": 6.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.38086,\n                        \"mmol_l\": 39.8714,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q12","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration.","source_stage":"main declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 17-17","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 2.07553,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The current provider explicitly declares this main-stage g_l, matching every stored value; retain that declared normalization basis with exact evidence. Its 1003 ml volume is computational metadata, whereas the primary lists batch quantities and 1000 ml water input without an explicit measured final volume. Do not replace the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q13","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction. The source gives 10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not independently derived from an invented w/v assumption.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 32-32","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction. The source gives 10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not independently derived from an invented w/v assumption."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction. The source gives 10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not independently derived from an invented w/v assumption."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction. The source gives 10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not independently derived from an invented w/v assumption."}]},{"quantity_id":"q14","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 33-33","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The correct stock-rate digits are flattened at main scope; move this occurrence into its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].composition[0].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].composition[0].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."}]},{"quantity_id":"q15","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 34-34","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q16","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 35-35","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q17","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 36-36","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q18","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 37-37","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q19","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 38-38","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q20","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 39-39","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q21","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 40-40","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source identifies this as an SL-10 stock component, with explicit final stock makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q22","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 57-57","quote":"NaOH                                        0.50    g","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q23","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 58-58","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q24","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 59-59","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q25","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 64-64","quote":"Vitamin B12                               100.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The correct stock-rate digits are flattened at main scope; move this occurrence into its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[0].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[0].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."}]},{"quantity_id":"q26","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.08","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.08","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.08","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 65-65","quote":"p-Aminobenzoic acid                        80.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q27","label":"D-(+)-biotin","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 66-66","quote":"D-(+)-biotin                               20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q28","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 67-67","quote":"Nicotinic acid                            200.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The correct stock-rate digits are flattened at main scope; move this occurrence into its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[1].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[1].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."}]},{"quantity_id":"q29","label":"Calcium pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 68-68","quote":"Calcium pantothenate                      100.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q30","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[2].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[2].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 69-69","quote":"Pyridoxine hydrochloride                  300.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The correct stock-rate digits are flattened at main scope; move this occurrence into its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[2].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[2].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."}]},{"quantity_id":"q31","label":"Thiamine-HCl x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The primary supplies this stock batch mass with 1000 ml water input; its final stock volume is not explicitly stated, while the provider separately declares the stored g_l. It is not an undiluted main-medium rate. Credit an existing nested stock occurrence where present, retain its declared stock basis and attach evidence; move remaining direct occurrences into the exact source stock. Each receiving stock volume is a separate source batch instruction.","source_stage":"seven-vitamin stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 70-70","quote":"Thiamine-HCl x 2 H2O                      200.00   mg","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The correct stock-rate digits are flattened at main scope; move this occurrence into its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[3].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[3].concentration","decision":"evidence_only","rationale":"This correctly nested stock rate matches the explicit provider stock g_l; retain its stock stage and attach exact evidence. Primary final volume is explicit for SL-10, but the vitamin stock lists only water input."}]},{"quantity_id":"q32","label":"SL-10 receiving basis","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].preparation_notes","stored":"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].preparation_notes","stored":"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."}],"decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components.","source_stage":"receiving dose and retained notes","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0]","quote":"{\n                \"id\": 1822,\n                \"name\": \"Main sol. 881\",\n                \"volume\": 1003,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\": 0.140384,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 7.32637,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\": 4.65979,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.9402,\n                        \"mmol_l\": 341.208,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\": 14.7122,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 6.68685,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 1.64,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.63509,\n                        \"mmol_l\": 19.932,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 9.40681,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\": 276,\n                        \"amount\": 6.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.38086,\n                        \"mmol_l\": 39.8714,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 14,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 2.07553,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }\n                ],\n                \"equipment\": {\n                    \"1507\": \"Autoclave\",\n                    \"2302\": \"Hungate tubes\",\n                    \"3328\": \"Filter\",\n                    \"4462\": \"Gassing station\"\n                }\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].concentration","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].concentration","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].preparation_notes","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].preparation_notes","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."}]},{"quantity_id":"q33","label":"Seven vitamins receiving basis","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].preparation_notes","stored":"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].preparation_notes","stored":"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."}],"decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components.","source_stage":"receiving dose and retained notes","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0]","quote":"{\n                \"id\": 1822,\n                \"name\": \"Main sol. 881\",\n                \"volume\": 1003,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\": 0.140384,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 7.32637,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\": 4.65979,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.9402,\n                        \"mmol_l\": 341.208,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\": 14.7122,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 6.68685,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 1.64,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.63509,\n                        \"mmol_l\": 19.932,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 9.40681,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\": 276,\n                        \"amount\": 6.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.38086,\n                        \"mmol_l\": 39.8714,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 14,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 2.07553,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }\n                ],\n                \"equipment\": {\n                    \"1507\": \"Autoclave\",\n                    \"2302\": \"Hungate tubes\",\n                    \"3328\": \"Filter\",\n                    \"4462\": \"Gassing station\"\n                }\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].concentration","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].concentration","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].preparation_notes","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].preparation_notes","decision":"unsupported","rationale":"The primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing ML_PER_L and notes assert that additional basis without primary support; provider main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch addition and stock water/makeup facts, but qualify the receiving denominator. This does not negate the five correctly nested stock components."}]},{"quantity_id":"q34","label":"Selenite-tungstate receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The omitted third stock is supplied at 1 ml per source batch. Preserve this receiving addition separately from its three stock constituents; do not silently convert it to 1 ml per final litre.","source_stage":"source-only receiving dose","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact water input; no primary final-volume claim is implied.","source_stage":"source-only volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 18-18","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"SL-10 water and final makeup","local_fields":[],"decision":"evidence_only","rationale":"The source lists 990 ml water, then explicitly makes up SL-10 to 1000 ml; preserve both the solvent input and final makeup.","source_stage":"source-only volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 41-41","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Selenite-tungstate water","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact water input; no primary final-volume claim is implied.","source_stage":"source-only volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 60-60","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Vitamin water","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact water input; no primary final-volume claim is implied.","source_stage":"source-only volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 71-71","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Main pH, gas and staged preparation","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","stored":{"min":6.8,"max":7.2}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","stored":{"min":6.8,"max":7.2}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."}}],"decision":"mixed","rationale":"The current primary and DSM owner agree on final pH 7.0–7.2; generated/KOMODO 6.8–7.2 and Aerobic: Yes conflict with the current source. Credit the complete DSM owner paragraph, including 80/20 N2/CO2, 30–45 min, later 100% N2 stocks, carbonate atmosphere and vitamin filtration. Split distinct processes instead of treating the entire mixed paragraph as one AUTOCLAVE action. Generated/KOMODO preparation is missing.","source_stage":"main preparation","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 20-26","quote":"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80%\nN2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. Adjust pH of\ncomplete medium to 7.0 - 7.2, if necessary.","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","decision":"conflict","rationale":"The stored lower pH limit differs from the current primary; retain historical variant evidence and reconcile it explicitly."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","decision":"conflict","rationale":"The stored lower pH limit differs from the current primary; retain historical variant evidence and reconcile it explicitly."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"Correct current primary pH and full preparation text are credited; attach evidence and split the mixed actions."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"Correct current primary pH and full preparation text are credited; attach evidence and split the mixed actions."}]},{"quantity_id":"q40","label":"Retained SL-10 preparation placement","local_fields":[{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The text correctly preserves FeCl2 dissolution in HCl, subsequent additions and final stock makeup. Its unqualified main preparation placement is wrong; preserve the supported text with the SL-10 stock rather than apply its makeup to the medium.","source_stage":"stock preparation placement","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The text correctly preserves FeCl2 dissolution in HCl, subsequent additions and final stock makeup. Its unqualified main preparation placement is wrong; preserve the supported text with the SL-10 stock rather than apply its makeup to the medium."}]},{"quantity_id":"q41","label":"Unspecified late stock strengths and sterilization controls","local_fields":[],"decision":"not_quantified","rationale":"The primary names late fumarate, sulfide and carbonate stocks and their gas atmospheres but does not give their concentrations or aliquot volumes; it gives no autoclave temperature/duration. Preserve these explicit limits rather than invent operational values.","source_stage":"source-only missing quantities","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt lines 20-26","quote":"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80%\nN2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. Adjust pH of\ncomplete medium to 7.0 - 7.2, if necessary.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:006731.

Fresh OLS canonical objects and exact packaged MIM rows were checked for every primary/secondary assertion. Nickel hydration and sodium-resazurin salt state are confirmed mismatches. Other named hydrates and hydrochlorides remain compatible; generic vitamin B12 is not narrowed to a specific vitamer. The source says calcium pantothenate without stereochemistry, while CHEBI:31345 specifies D-pantothenate: that specificity remains unverified, not silently endorsed or declared certainly wrong. Existing MIM sodium-resazurin synonyms mapped to neutral resazurin do not override the supplied salt chemistry.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:006731.

All five report bodies, current target/contributor histories and two exact parent plan rows were read. Earlier blanket topology and pH conflicts are not treated as fresh execution or as proof that every provider rate is wrong. The August five-component repairs are present in maintained owners but absent from the older generated target. Current parser, resolver, nesting and conservative merger bodies were separately inspected; the current nesting early-return prevents automatic completion of already-partly-nested records. No attached claim exists.

## Findings

### f1: Complete the source stocks while crediting the five nested components

major / open / confirmed; issue key: culturemech-006731-incomplete-stock-topology.

The generated record keeps all nineteen stock components at main strength. Both contributors correctly nest FeCl2 and four vitamins, but leave the other fourteen stock components direct, omit the selenite-tungstate stock descriptor and assert an unsupported per-final-litre receiving basis. Preserve the source batch additions, explicit SL-10 final makeup and provider-declared stock rates. The primary water input does not prove the main final volume; no automatic replay of the current nesting script can repair a record that already has solutions.

### f2: Reconcile pH and anoxic preparation before regenerating

major / open / confirmed; issue key: culturemech-006731-preparation-ph-and-stale-output.

The DSM contributor preserves current pH 7.0–7.2 and the main staged preparation. Generated/KOMODO pH 6.8–7.2 and Aerobic: Yes conflict with the current primary; their preparation is absent. Preserve source/version distinctions rather than overwrite old history. Split the retained mixed-process paragraph and move SL-10 preparation into stock scope. Reconcile both maintained inputs before using the conservative merger, which currently rejects their different pH/preparation/notes.

### f3: Correct sodium-resazurin and nickel hydrate assertions

major / open / confirmed; issue key: culturemech-006731-supplied-sodium-and-nickel-forms.

The source names sodium resazurin, but the primary CHEBI:8806 term is neutral resazurin. Nickel is explicitly NiCl2·6H2O, while both local slots use anhydrous CHEBI:34887. Verify an exact sodium-salt identity and canonical label without transferring a speculative candidate; CHEBI:53542 is the current OLS hexahydrate candidate, although the exact MIM preferred spelling 'NiCl2 x 6 H2O' is REJECTED (row 6703), while 'Nickel (II) chloride hexahydrate' is MAPPED (row 6668). Preserve the amount and stage decisions separately.

### f4: Attach exact source claims and preserve original events

minor / open / confirmed; issue key: culturemech-006731-quantity-evidence-and-event-metadata.

No scoped quantity claims are attached. Current equal provider snippets/digests can authenticate content, not the original access event. Retain all original historical reports and malformed or timezone-naive import/resolver timestamps; append verified context if recovered. Historical ingredient-signature equality does not prove present complete formulation equivalence.

## Recommended Actions And Acceptance Checks

### a1

The generated record keeps all nineteen stock components at main strength. Both contributors correctly nest FeCl2 and four vitamins, but leave the other fourteen stock components direct, omit the selenite-tungstate stock descriptor and assert an unsupported per-final-litre receiving basis. Preserve the source batch additions, explicit SL-10 final makeup and provider-declared stock rates. The primary water input does not prove the main final volume; no automatic replay of the current nesting script can repair a record that already has solutions.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The DSM contributor preserves current pH 7.0–7.2 and the main staged preparation. Generated/KOMODO pH 6.8–7.2 and Aerobic: Yes conflict with the current primary; their preparation is absent. Preserve source/version distinctions rather than overwrite old history. Split the retained mixed-process paragraph and move SL-10 preparation into stock scope. Reconcile both maintained inputs before using the conservative merger, which currently rejects their different pH/preparation/notes.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source names sodium resazurin, but the primary CHEBI:8806 term is neutral resazurin. Nickel is explicitly NiCl2·6H2O, while both local slots use anhydrous CHEBI:34887. Verify an exact sodium-salt identity and canonical label without transferring a speculative candidate; CHEBI:53542 is the current OLS hexahydrate candidate, although the exact MIM preferred spelling 'NiCl2 x 6 H2O' is REJECTED (row 6703), while 'Nickel (II) chloride hexahydrate' is MAPPED (row 6668). Preserve the amount and stage decisions separately.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

No scoped quantity claims are attached. Current equal provider snippets/digests can authenticate content, not the original access event. Retain all original historical reports and malformed or timezone-naive import/resolver timestamps; append verified context if recovered. Historical ingredient-signature equality does not prove present complete formulation equivalence.

- Retain every original event/report byte-for-byte; append only independently verified correction context.
- Attach exact source-stage claims and preserve direct KOMODO access limits; do not certify full equivalence from old ingredient-signature notes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz881 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf; REVIEW_WORK/batch073/source01-03-supplement/dsmz881.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api881 | https://mediadive.dsmz.de/rest/medium/881; REVIEW_WORK/batch073/source01-03-supplement/api881.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo881 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=881; REVIEW_WORK/batch073/source01-03-supplement/komodo881.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch073/source01-03-supplement/komodoList.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| identityDenitrovibrio | https://lpsn.dsmz.de/genus/denitrovibrio; REVIEW_WORK/batch073/source01-03-supplement/identityDenitrovibrio.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch073/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/denitrovibrio_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-17 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/denitrovibrio_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DENITROVIBRIO_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/denitrovibrio_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch073/record02/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch073/record02/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch073/record02/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _parse_api_solutions; _normalize_unit; _parse_preparation_steps; _classify_preparation_action | context_only | Current _parse_api_composition reads primary-solution compounds and explicit g_l, while stock additions and water are skipped. _parse_api_solutions keeps stock references but maps bare ml to ML_PER_L without proving the receiving basis. _parse_preparation_steps collects all solution steps at main scope; the classifier chooses AUTOCLAVE before filtration in a mixed paragraph. These are current observations, not authenticated historical execution. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.extract_dsmz_id; merge_composition | context_only | Current merge_composition copies ingredients/solutions and only a missing scalar ph_value; it does not copy ph_range or preparation_steps. Existing copy history is distinct from proof that the current body produced the old output. |
| writer-nesting | scripts/apply_cocktail_nesting.py; match_components; match_stock_signature; plan_record; apply_plan | context_only | The current plan_record returns early when any solutions already exist, so it cannot complete this partly repaired record by automatic replay. Component and full-signature matching plus apply_plan were read; the historical event separately records the actual five-component repair. |
| writer-legacy | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | The current secondary-link migration retains existing CHEBI identity and label; it does not independently verify supplied salt/hydrate. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch073/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch073/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch073/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch073/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch073/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch073/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch073/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch073/source01-03-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch073/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch073/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi115156 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:115156; REVIEW_WORK/batch073/source01-03-supplement/chebi115156.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch073/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch073/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch073/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch073/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch073/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch073/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch073/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch073/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch073/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch073/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch073/source01-03-supplement/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; REVIEW_WORK/batch073/source01-03-supplement/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; REVIEW_WORK/batch073/source01-03-supplement/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch073/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch073/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch073/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch073/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch073/source01-03-supplement/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch073/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:132751; REVIEW_WORK/batch073/source01-03-supplement/chebi132751.json; exact original raw/text/hash/time metadata | context_only | Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch073/record02/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch073/record02/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch073/record02/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch073/record02/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch073/record02/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch073/record02/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch073/record02/existing-claim-authentication.json; Complete sidecar | context_only | No attached source claims exist in the scoped target/owners, so this empty artifact records absence of claims to authenticate. Historical report snippets are authenticated separately in historical-source-joins.json. |
| check-schema | REVIEW_WORK/batch073/record02/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch073/record02/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch073/record02/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch073/record02/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |
| historical-joins | REVIEW_WORK/batch073/record02/historical-source-joins.json; Complete rows: original report path/line/literal, decoded object and exact current raw-object/digest joins | supports | 80 exact historical report JSON objects match current captured raw objects and recorded raw hashes. This authenticates their content, not the historical access event; it is separate from the empty local attached-claim artifact. |

## Limits And Additional Notes

- Exact KOMODO catalogue/accession routes returned 403; current primary/provider are available but complete accession-version verification remains partial.
- Provider main volume 1003 ml and explicit g_l describe its normalization; the primary lists 1000 ml water and stock additions without an independently measured final volume.
- HCl 25% lacks an explicit percent basis; no 7.7 M statement from another medium is transferred.
- Calcium-pantothenate stereochemistry and the exact replacement sodium-resazurin identifier require bounded follow-up; no unverified replacement ID is proposed.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T173711Z-culturemech-006731-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DENITROVIBRIO MEDIUM'
started_at: '2026-10-28T17:18:18.316625Z'
finished_at: '2026-10-28T17:37:11.298087Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, exact
    captured sources, fresh scoped primary sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: DSM881 supplies exact batch quantities and provider-declared main rates,
  but stock components remain incompletely nested and the generated record predates
  its owners’ five-component repairs. Current primary pH/anoxic preparation conflicts
  with KOMODO-derived metadata, and sodium-resazurin/nickel identities require correction.
  Correct owner preparation and nested rates are credited; no measured final volume
  is inferred. Four original canonical checks passed, while direct KOMODO verification
  remains partial.
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
  - path: data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml
    sha256: 946ad945e0152dbd444072af042f847b4fcc45989f226e517f036dd06b3570b5
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    sha256: 745833161857bd776b8f8992a142b17e5968808159946267e027e1634f21869c
    role: context
  - path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    sha256: 604460625e4ed386ca31dfe578a68f50ffae895260cb6be32518fdf97110eef9
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
    sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml.md
    sha256: fe3592754ba72ab7a745ad219a023f8f6b872aaec1ccd1671f1b58af1175603f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/denitrovibrio_medium.yaml.md
    sha256: 3ea8382c4d89f286b7657937ef8d631262791deb3fc1694ee7ba9cbbd65bd5b4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DENITROVIBRIO_MEDIUM.md
    sha256: 372fe42653eb0ec39a23ac59296bb3c6b40dc958c94cb89871d71de4fd390196
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.md
    sha256: 8bbe2ffcfa9fbf32d312274846b1fe6d412e5e100bce84e32138424669e1e523
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/denitrovibrio_medium.md
    sha256: a9ccd74105f45a24c4d8fbf55c6baae38ca6dcc8f65963fbdf4d5c8fda855386
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
  selection: Authoritative batch073 index 02
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006731
targets:
- target_id: CultureMech:006731
  path: data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml
  label: denitrovibrio_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:006731
  command: just validate-schema data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml
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
  - CultureMech:006731
  command: just validate-strict data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml --out
    REVIEW_WORK/batch073/record02/strict.tsv --workers 1 --quiet
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
  - CultureMech:006731
  command: just validate-terms data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml
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
  - CultureMech:006731
  command: just validate-references data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz881
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf
  accessed_at: '2026-10-28T17:18:41.814458Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/dsmz881.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1
- evidence_id: api881
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/881
  accessed_at: '2026-10-28T17:18:41.668004Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/api881.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637
- evidence_id: komodo881
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=881
  accessed_at: '2026-10-28T17:18:41.560736Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/komodo881.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d9336c52d8e572552a1c5a918586d60789651ed24db7d4a92b911b32b645743f
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=881;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T17:18:42.006890Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/komodoList.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0aa29786ed8d7727e17b91a27348b4bc8857db8048028c9f5509462a4e9b6fde
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: identityDenitrovibrio
  kind: primary_source
  reference: https://lpsn.dsmz.de/genus/denitrovibrio
  accessed_at: '2026-10-28T17:18:42.761827Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/identityDenitrovibrio.json;
    exact original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 351d0a8a2c7ceed4bfcf05aea9478c0aaaf0b449b549d516ac4f8890d661935f
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T17:18:47.912524Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:30:15.914297Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 946ad945e0152dbd444072af042f847b4fcc45989f226e517f036dd06b3570b5
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:30:15.914458Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 745833161857bd776b8f8992a142b17e5968808159946267e027e1634f21869c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T17:30:15.914486Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T17:30:15.914800Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T17:30:15.914822Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T17:30:15.914843Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:30:15.914867Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 604460625e4ed386ca31dfe578a68f50ffae895260cb6be32518fdf97110eef9
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:30:15.914891Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T17:30:15.922608Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: fe3592754ba72ab7a745ad219a023f8f6b872aaec1ccd1671f1b58af1175603f
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:30:15.922676Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/denitrovibrio_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T17:30:15.929336Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 3ea8382c4d89f286b7657937ef8d631262791deb3fc1694ee7ba9cbbd65bd5b4
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DENITROVIBRIO_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:30:15.929418Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 372fe42653eb0ec39a23ac59296bb3c6b40dc958c94cb89871d71de4fd390196
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:30:15.929457Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8bbe2ffcfa9fbf32d312274846b1fe6d412e5e100bce84e32138424669e1e523
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/denitrovibrio_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T17:30:15.929490Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a9ccd74105f45a24c4d8fbf55c6baae38ca6dcc8f65963fbdf4d5c8fda855386
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/historical-reading.json
  accessed_at: '2026-10-28T17:30:15.929529Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: d7cded1bec0cd8854f136c1792090046305fefe3bf120437c4e152e2808f6707
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:30:15.929833Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: a127652a054836fd43f2442ba3e20083e0814b373b3da4d3da52a1e53158b725
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/complete-document-reader.json
  accessed_at: '2026-10-28T17:30:15.930081Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 587cc4db7faea039ec49997ccb54c3814f7887244056a4ccd36beaa0b2797d55
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _parse_api_solutions; _normalize_unit; _parse_preparation_steps;
    _classify_preparation_action
  accessed_at: '2026-10-28T17:30:15.930291Z'
  support: context_only
  summary: Current _parse_api_composition reads primary-solution compounds and explicit
    g_l, while stock additions and water are skipped. _parse_api_solutions keeps stock
    references but maps bare ml to ML_PER_L without proving the receiving basis. _parse_preparation_steps
    collects all solution steps at main scope; the classifier chooses AUTOCLAVE before
    filtration in a mixed paragraph. These are current observations, not authenticated
    historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T17:30:15.930333Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.extract_dsmz_id; merge_composition
  accessed_at: '2026-10-28T17:30:15.930365Z'
  support: context_only
  summary: Current merge_composition copies ingredients/solutions and only a missing
    scalar ph_value; it does not copy ph_range or preparation_steps. Existing copy
    history is distinct from proof that the current body produced the old output.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-nesting
  kind: record_content
  reference: scripts/apply_cocktail_nesting.py
  locator: match_components; match_stock_signature; plan_record; apply_plan
  accessed_at: '2026-10-28T17:30:15.930394Z'
  support: context_only
  summary: The current plan_record returns early when any solutions already exist,
    so it cannot complete this partly repaired record by automatic replay. Component
    and full-signature matching plus apply_plan were read; the historical event separately
    records the actual five-component repair.
  snapshot_sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
- evidence_id: writer-legacy
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T17:30:15.930430Z'
  support: context_only
  summary: The current secondary-link migration retains existing CHEBI identity and
    label; it does not independently verify supplied salt/hydrate.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T17:18:46.683882Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T17:18:48.081700Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T17:18:46.091135Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T17:18:45.317823Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T17:18:49.335920Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T17:18:46.857755Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T17:18:48.758685Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T17:18:47.056015Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi32954.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T17:18:49.503828Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T17:18:45.502809Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi115156
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:115156
  accessed_at: '2026-10-28T17:18:43.078175Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi115156.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bef4d7b112e4b6be8f75e737b1b1921ab0e8951095bba276c87d534b62d0f8c7
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T17:18:48.704391Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T17:18:45.200931Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T17:18:48.900929Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T17:18:47.548828Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T17:18:49.350897Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T17:18:47.284939Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T17:18:47.653323Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T17:18:49.143844Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T17:18:47.464840Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T17:18:48.270582Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  accessed_at: '2026-10-28T17:18:46.937845Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi32145.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  accessed_at: '2026-10-28T17:18:43.384182Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi131361.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  accessed_at: '2026-10-28T17:18:48.152765Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi63939.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T17:18:44.900665Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T17:18:45.836506Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T17:18:44.055068Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T17:18:43.831290Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T17:18:46.179612Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi31345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T17:18:45.913701Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:132751
  accessed_at: '2026-10-28T17:18:43.672578Z'
  locator: REVIEW_WORK/batch073/source01-03-supplement/chebi132751.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch073 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1d5eefc753b4fbbffd69d169aa7ca7be16df737b6c8c0e1833917806ac0607e5
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.117850Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 8c6fa7f4163e7c2750aaa0c1aea052cbeaf93b75c06705e6338bedc8132be6cc
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.117959Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 14b7067d1465525d978779acbbeed3b108dcc1bafcef705b928f824a67fec42d
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.118114Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: cdd4d32c196b779463f544b40317e157e6a3eb867eb4699db35e50abd5e5f7ff
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.118190Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 22f0086bcf148b780b8e0b0199cb44c1a61cb7d94ecf929845b90b002ad5414f
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.118259Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: dd0658622dc43a9ccb3a57bfd3a984c3b4422e5099e846d17a46b8c0b4d58f5f
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.118282Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: f0f2c94d754f5bc4cfb111c60e01c7d803ac78107e534f1bad5164899359a8f6
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:30:16.118301Z'
  support: context_only
  summary: No attached source claims exist in the scoped target/owners, so this empty
    artifact records absence of claims to authenticate. Historical report snippets
    are authenticated separately in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch073/record02/validate-schema.json
  accessed_at: '2026-10-28T17:18:19.523253Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 9bf4e9e6124ccae44fd27f80bbf3fcfb6455e8727d1f6b7eff1cda52e4ee9e3d
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch073/record02/validate-strict.json
  accessed_at: '2026-10-28T17:18:20.472162Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: ae398da6931eec08ccd62494a1864f94ed681c14892935be9710a612bb39701b
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch073/record02/validate-terms.json
  accessed_at: '2026-10-28T17:18:21.616968Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: ab30f207960a40ff112b49b05e7517040ab760d806430faeea3875a4d83b79ca
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch073/record02/validate-references.json
  accessed_at: '2026-10-28T17:18:22.374076Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 299628a4c62b14da8f45b84d803a5218a494b0afe3cfd7ecbed1dfc5be9b4a62
- evidence_id: historical-joins
  kind: record_content
  reference: REVIEW_WORK/batch073/record02/historical-source-joins.json
  locator: 'Complete rows: original report path/line/literal, decoded object and exact
    current raw-object/digest joins'
  accessed_at: '2026-10-28T17:37:11.298029Z'
  support: supports
  summary: 80 exact historical report JSON objects match current captured raw objects
    and recorded raw hashes. This authenticates their content, not the historical
    access event; it is separate from the empty local attached-claim artifact.
  snapshot_sha256: 83fc229c09f91aabdead6b21fe0b1ef811da21f4c4656d28890e00e7b26d85a7
assessments:
- assessment_id: identity
  area: identity
  topic: DSM881 and historical KOMODO mapping
  outcome: unknown
  summary: The current primary and provider agree on DSM881. The historical KOMODO
    mapping reports a different pH range and the exact current accession/catalogue
    routes return 403; direct KOMODO version verification remains incomplete. Neighboring
    TOGO names found in old reports are not current merge owners or evidence substitutes.
  target_ids:
  - CultureMech:006731
  evidence_ids:
  - dsmz881
  - api881
  - komodo881
  - komodoList
  - identityDenitrovibrio
- assessment_id: classification
  area: scope
  topic: Defined liquid and atmosphere discrepancy
  outcome: concern
  summary: 'The chemically specified recipe and absence of agar support defined liquid
    scope. The Aerobic: Yes note conflicts with explicit anoxic preparation; no strain
    cultivation or temperature inference is made.'
  target_ids:
  - CultureMech:006731
  evidence_ids:
  - dsmz881
  - target
- assessment_id: evidence
  area: evidence
  topic: Declared provider main rates and corrected stock scope
  outcome: concern
  summary: Twelve unchanged main rates match current explicit provider g_l; they are
    credited on that provider basis, not as independently measured primary final concentrations.
    Existing five-component nesting is credited, and source-only volumes, pH and every
    preparation control are inventoried separately.
  target_ids:
  - CultureMech:006731
  evidence_ids:
  - quantities
  - dsmz881
  - api881
  - old-claims
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 97 current concentration fields are covered by 41 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:006731
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b073-quantity-inventory-v1","target":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","quantity_field_count":97,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 3-3","quote":"Na2SO4                                                     0.02         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\":
    0.140384,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 4-4","quote":"KH2PO4                                                     1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    7.32637,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 5-5","quote":"NH4Cl                                                      0.25         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\":
    4.65979,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"19.9402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"19.9402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"19.9402","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 6-6","quote":"NaCl                                                      20.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 19.9402,\n                        \"mmol_l\":
    341.208,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q5","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.99103","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.99103","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.99103","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 7-7","quote":"MgCl2 x 6 H2O                                              3.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\":
    14.7122,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 8-8","quote":"KCl                                                        0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    6.68685,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q7","label":"CaCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.149551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.149551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.149551","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 9-9","quote":"CaCl2 x 2 H2O                                              0.15         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\":
    1.01725,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q8","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.63509","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.63509","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.63509","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 10-10","quote":"Na-acetate                                                 1.64         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 1.64,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.63509,\n                        \"mmol_l\":
    19.932,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q9","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.
    The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution;
    the stock strength and receiving volume are retained separately from the provider
    rate and the incorrect neutral ontology identity.","source_stage":"main declared
    provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 13-13","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.
    The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution;
    the stock strength and receiving volume are retained separately from the provider
    rate and the incorrect neutral ontology identity."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.
    The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution;
    the stock strength and receiving volume are retained separately from the provider
    rate and the incorrect neutral ontology identity."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.
    The primary specifically supplies 0.50 ml of 0.1% w/v sodium-resazurin solution;
    the stock strength and receiving volume are retained separately from the provider
    rate and the incorrect neutral ontology identity."}]},{"quantity_id":"q10","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 14-14","quote":"Na2CO3                                                     1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    9.40681,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q11","label":"Na2-fumarate","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6.38086","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6.38086","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6.38086","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 15-15","quote":"Na2-fumarate                                               6.40         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\":
    276,\n                        \"amount\": 6.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6.38086,\n                        \"mmol_l\":
    39.8714,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q12","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration.","source_stage":"main
    declared provider rate","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 17-17","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    2.07553,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The
    current provider explicitly declares this main-stage g_l, matching every stored
    value; retain that declared normalization basis with exact evidence. Its 1003
    ml volume is computational metadata, whereas the primary lists batch quantities
    and 1000 ml water input without an explicit measured final volume. Do not replace
    the source mass by the rate or infer an independently measured final concentration."}]},{"quantity_id":"q13","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction. The source gives
    10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not
    independently derived from an invented w/v assumption.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 32-32","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction. The source gives
    10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not
    independently derived from an invented w/v assumption."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction. The source gives
    10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not
    independently derived from an invented w/v assumption."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction. The source gives
    10 ml HCl at 25%; it does not specify the percent basis. Provider 2.5 g_l is not
    independently derived from an invented w/v assumption."}]},{"quantity_id":"q14","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 33-33","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    correct stock-rate digits are flattened at main scope; move this occurrence into
    its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].composition[0].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].composition[0].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."}]},{"quantity_id":"q15","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 34-34","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q16","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 35-35","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q17","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 36-36","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q18","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 37-37","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q19","label":"CuCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 38-38","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q20","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 39-39","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q21","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 40-40","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source identifies this as an SL-10 stock component, with explicit final stock
    makeup to 1000 ml. It is not an undiluted main-medium rate. Credit an existing
    nested stock occurrence where present, retain its declared stock basis and attach
    evidence; move remaining direct occurrences into the exact source stock. Each
    receiving stock volume is a separate source batch instruction."}]},{"quantity_id":"q22","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"selenite-tungstate
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 57-57","quote":"NaOH                                        0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."}]},{"quantity_id":"q23","label":"Na2SeO3
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"selenite-tungstate
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 58-58","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."}]},{"quantity_id":"q24","label":"Na2WO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"selenite-tungstate
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 59-59","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."}]},{"quantity_id":"q25","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 64-64","quote":"Vitamin B12                               100.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    correct stock-rate digits are flattened at main scope; move this occurrence into
    its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[0].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[0].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."}]},{"quantity_id":"q26","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.08","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.08","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.08","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 65-65","quote":"p-Aminobenzoic acid                        80.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."}]},{"quantity_id":"q27","label":"D-(+)-biotin","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 66-66","quote":"D-(+)-biotin                               20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."}]},{"quantity_id":"q28","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 67-67","quote":"Nicotinic acid                            200.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    correct stock-rate digits are flattened at main scope; move this occurrence into
    its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[1].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[1].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."}]},{"quantity_id":"q29","label":"Calcium
    pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 68-68","quote":"Calcium pantothenate                      100.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction."}]},{"quantity_id":"q30","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[2].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[2].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 69-69","quote":"Pyridoxine hydrochloride                  300.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    correct stock-rate digits are flattened at main scope; move this occurrence into
    its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[2].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[2].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."}]},{"quantity_id":"q31","label":"Thiamine-HCl
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    primary supplies this stock batch mass with 1000 ml water input; its final stock
    volume is not explicitly stated, while the provider separately declares the stored
    g_l. It is not an undiluted main-medium rate. Credit an existing nested stock
    occurrence where present, retain its declared stock basis and attach evidence;
    move remaining direct occurrences into the exact source stock. Each receiving
    stock volume is a separate source batch instruction.","source_stage":"seven-vitamin
    stock","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 70-70","quote":"Thiamine-HCl x 2 H2O                      200.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    correct stock-rate digits are flattened at main scope; move this occurrence into
    its source stock without treating the undiluted rate as final medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].composition[3].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].composition[3].concentration","decision":"evidence_only","rationale":"This
    correctly nested stock rate matches the explicit provider stock g_l; retain its
    stock stage and attach exact evidence. Primary final volume is explicit for SL-10,
    but the vitamin stock lists only water input."}]},{"quantity_id":"q32","label":"SL-10
    receiving basis","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].preparation_notes","stored":"Stock
    prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume
    from MediaDive (#150)."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].preparation_notes","stored":"Stock
    prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume
    from MediaDive (#150)."}],"decision":"unsupported","rationale":"The primary supplies
    1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing
    ML_PER_L and notes assert that additional basis without primary support; provider
    main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch
    addition and stock water/makeup facts, but qualify the receiving denominator.
    This does not negate the five correctly nested stock components.","source_stage":"receiving
    dose and retained notes","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 11-11","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0]","quote":"{\n                \"id\":
    1822,\n                \"name\": \"Main sol. 881\",\n                \"volume\":
    1003,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\":
    0.140384,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    7.32637,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\":
    4.65979,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 19.9402,\n                        \"mmol_l\":
    341.208,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\":
    14.7122,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    6.68685,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\":
    1.01725,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 1.64,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.63509,\n                        \"mmol_l\":
    19.932,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    9.40681,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\":
    276,\n                        \"amount\": 6.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6.38086,\n                        \"mmol_l\":
    39.8714,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    14,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    2.07553,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Dissolve all ingredients
    except carbonate, fumarate, vitamins and sulfide, then sparge medium with 80%
    N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration.
    Adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"1507\": \"Autoclave\",\n                    \"2302\":
    \"Hungate tubes\",\n                    \"3328\": \"Filter\",\n                    \"4462\":
    \"Gassing station\"\n                }\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].concentration","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].concentration","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[0].preparation_notes","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[0].preparation_notes","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."}]},{"quantity_id":"q33","label":"Seven
    vitamins receiving basis","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].preparation_notes","stored":"Stock
    prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume
    from MediaDive (#150)."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].preparation_notes","stored":"Stock
    prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume
    from MediaDive (#150)."}],"decision":"unsupported","rationale":"The primary supplies
    1 ml per listed recipe batch, not an explicitly final one-litre medium. Existing
    ML_PER_L and notes assert that additional basis without primary support; provider
    main volume is 1003 ml. Retain the supported stock identity, source 1 ml batch
    addition and stock water/makeup facts, but qualify the receiving denominator.
    This does not negate the five correctly nested stock components.","source_stage":"receiving
    dose and retained notes","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 16-16","quote":"Seven vitamins solution                                    1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0]","quote":"{\n                \"id\":
    1822,\n                \"name\": \"Main sol. 881\",\n                \"volume\":
    1003,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\":
    0.140384,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    7.32637,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\":
    4.65979,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 19.9402,\n                        \"mmol_l\":
    341.208,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\":
    14.7122,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    6.68685,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\":
    1.01725,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 1.64,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.63509,\n                        \"mmol_l\":
    19.932,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    9.40681,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\":
    276,\n                        \"amount\": 6.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6.38086,\n                        \"mmol_l\":
    39.8714,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    14,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    2.07553,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Dissolve all ingredients
    except carbonate, fumarate, vitamins and sulfide, then sparge medium with 80%
    N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add fumarate, vitamins and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration.
    Adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"1507\": \"Autoclave\",\n                    \"2302\":
    \"Hungate tubes\",\n                    \"3328\": \"Filter\",\n                    \"4462\":
    \"Gassing station\"\n                }\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].concentration","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].concentration","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"solutions[1].preparation_notes","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"solutions[1].preparation_notes","decision":"unsupported","rationale":"The
    primary supplies 1 ml per listed recipe batch, not an explicitly final one-litre
    medium. Existing ML_PER_L and notes assert that additional basis without primary
    support; provider main volume is 1003 ml. Retain the supported stock identity,
    source 1 ml batch addition and stock water/makeup facts, but qualify the receiving
    denominator. This does not negate the five correctly nested stock components."}]},{"quantity_id":"q34","label":"Selenite-tungstate
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The
    omitted third stock is supplied at 1 ml per source batch. Preserve this receiving
    addition separately from its three stock constituents; do not silently convert
    it to 1 ml per final litre.","source_stage":"source-only receiving dose","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 12-12","quote":"Selenite-tungstate solution                                1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact water input; no primary final-volume claim is implied.","source_stage":"source-only
    volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 18-18","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"SL-10 water and
    final makeup","local_fields":[],"decision":"evidence_only","rationale":"The source
    lists 990 ml water, then explicitly makes up SL-10 to 1000 ml; preserve both the
    solvent input and final makeup.","source_stage":"source-only volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 41-41","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Selenite-tungstate
    water","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact
    water input; no primary final-volume claim is implied.","source_stage":"source-only
    volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 60-60","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Vitamin water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact water input; no primary final-volume claim is implied.","source_stage":"source-only
    volume","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 71-71","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Main pH, gas and
    staged preparation","local_fields":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","stored":{"min":6.8,"max":7.2}},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","stored":{"min":6.8,"max":7.2}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    all ingredients except carbonate, fumarate, vitamins and sulfide, then sparge
    medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock
    solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock
    solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be
    sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary."}}],"decision":"mixed","rationale":"The
    current primary and DSM owner agree on final pH 7.0–7.2; generated/KOMODO 6.8–7.2
    and Aerobic: Yes conflict with the current source. Credit the complete DSM owner
    paragraph, including 80/20 N2/CO2, 30–45 min, later 100% N2 stocks, carbonate
    atmosphere and vitamin filtration. Split distinct processes instead of treating
    the entire mixed paragraph as one AUTOCLAVE action. Generated/KOMODO preparation
    is missing.","source_stage":"main preparation","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 20-26","quote":"Dissolve all ingredients except carbonate, fumarate, vitamins
    and sulfide, then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 -
    45 min to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic
    Hungate-type tubes or serum vials and\nautoclave. Add fumarate, vitamins and sulfide
    from sterile anoxic stock solutions prepared\nunder 100% N2 gas and carbonate
    from a sterile anoxic stock solution prepared under 80%\nN2 and 20% CO2 gas atmosphere.
    Vitamins should be sterilized by filtration. Adjust pH of\ncomplete medium to
    7.0 - 7.2, if necessary.","quote_basis":"derivative text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve all ingredients except carbonate, fumarate, vitamins and sulfide, then
    sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add fumarate, vitamins and sulfide from sterile anoxic stock
    solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock
    solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be
    sterilized by filtration. Adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","decision":"conflict","rationale":"The
    stored lower pH limit differs from the current primary; retain historical variant
    evidence and reconcile it explicitly."},{"path":"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml","field_path":"ph_range","decision":"conflict","rationale":"The
    stored lower pH limit differs from the current primary; retain historical variant
    evidence and reconcile it explicitly."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"Correct
    current primary pH and full preparation text are credited; attach evidence and
    split the mixed actions."},{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"Correct
    current primary pH and full preparation text are credited; attach evidence and
    split the mixed actions."}]},{"quantity_id":"q40","label":"Retained SL-10 preparation
    placement","local_fields":[{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The text
    correctly preserves FeCl2 dissolution in HCl, subsequent additions and final stock
    makeup. Its unqualified main preparation placement is wrong; preserve the supported
    text with the SL-10 stock rather than apply its makeup to the medium.","source_stage":"stock
    preparation placement","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api881","reference":"https://mediadive.dsmz.de/rest/medium/881","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/api881.bin","raw_sha256":"9f9aa0680b589abdbaa727157d6953b5fd3359b4a765f049cc23eb1626da2637","text_sha256":"0f7db5020ec8a809dd00aa223f7f009711af5ed7a901f60eb0d1c54bfa4447d6","accessed_at":"2026-10-28T17:18:41.668004Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    text correctly preserves FeCl2 dissolution in HCl, subsequent additions and final
    stock makeup. Its unqualified main preparation placement is wrong; preserve the
    supported text with the SL-10 stock rather than apply its makeup to the medium."}]},{"quantity_id":"q41","label":"Unspecified
    late stock strengths and sterilization controls","local_fields":[],"decision":"not_quantified","rationale":"The
    primary names late fumarate, sulfide and carbonate stocks and their gas atmospheres
    but does not give their concentrations or aliquot volumes; it gives no autoclave
    temperature/duration. Preserve these explicit limits rather than invent operational
    values.","source_stage":"source-only missing quantities","sources":[{"evidence_id":"dsmz881","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium881.pdf","raw_path":"REVIEW_WORK/batch073/source01-03-supplement/dsmz881.bin","raw_sha256":"08eec330ace3dc3bc01984c14b288ffc8a05af3dd90312ee9977cd0fad39c9e1","text_sha256":"16573734bf54c8e5df18b7a89056126d8b7e817d805ecc81f2304e50fec83863","accessed_at":"2026-10-28T17:18:41.814458Z","locator":"dsmz881.txt
    lines 20-26","quote":"Dissolve all ingredients except carbonate, fumarate, vitamins
    and sulfide, then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 -
    45 min to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic
    Hungate-type tubes or serum vials and\nautoclave. Add fumarate, vitamins and sulfide
    from sterile anoxic stock solutions prepared\nunder 100% N2 gas and carbonate
    from a sterile anoxic stock solution prepared under 80%\nN2 and 20% CO2 gas atmosphere.
    Vitamins should be sterilized by filtration. Adjust pH of\ncomplete medium to
    7.0 - 7.2, if necessary.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DENITROVIBRIO_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/denitrovibrio_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: 'Fresh OLS canonical objects and exact packaged MIM rows were checked for
    every primary/secondary assertion. Nickel hydration and sodium-resazurin salt
    state are confirmed mismatches. Other named hydrates and hydrochlorides remain
    compatible; generic vitamin B12 is not narrowed to a specific vitamer. The source
    says calcium pantothenate without stereochemistry, while CHEBI:31345 specifies
    D-pantothenate: that specificity remains unverified, not silently endorsed or
    declared certainly wrong. Existing MIM sodium-resazurin synonyms mapped to neutral
    resazurin do not override the supplied salt chemistry.'
  target_ids:
  - CultureMech:006731
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All five report bodies, current target/contributor histories and two exact
    parent plan rows were read. Earlier blanket topology and pH conflicts are not
    treated as fresh execution or as proof that every provider rate is wrong. The
    August five-component repairs are present in maintained owners but absent from
    the older generated target. Current parser, resolver, nesting and conservative
    merger bodies were separately inspected; the current nesting early-return prevents
    automatic completion of already-partly-nested records. No attached claim exists.
  target_ids:
  - CultureMech:006731
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-joins
findings:
- finding_id: f1
  issue_key: culturemech-006731-incomplete-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Complete the source stocks while crediting the five nested components
  description: The generated record keeps all nineteen stock components at main strength.
    Both contributors correctly nest FeCl2 and four vitamins, but leave the other
    fourteen stock components direct, omit the selenite-tungstate stock descriptor
    and assert an unsupported per-final-litre receiving basis. Preserve the source
    batch additions, explicit SL-10 final makeup and provider-declared stock rates.
    The primary water input does not prove the main final volume; no automatic replay
    of the current nesting script can repair a record that already has solutions.
  target_ids:
  - CultureMech:006731
  field_paths:
  - ingredients
  - solutions
  - evidence
  evidence_ids:
  - dsmz881
  - api881
  - quantities
  - writer-nesting
  - writer-mediadive
  rule_id: review-yaml-record/custom-incomplete-stock-topology
  native_severity: P2
  normalization_reason: 'Custom quantity rule: material stage, preparation or supplied-form
    defect; native shape checks are not scientific proof.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-006731-preparation-ph-and-stale-output
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile pH and anoxic preparation before regenerating
  description: 'The DSM contributor preserves current pH 7.0–7.2 and the main staged
    preparation. Generated/KOMODO pH 6.8–7.2 and Aerobic: Yes conflict with the current
    primary; their preparation is absent. Preserve source/version distinctions rather
    than overwrite old history. Split the retained mixed-process paragraph and move
    SL-10 preparation into stock scope. Reconcile both maintained inputs before using
    the conservative merger, which currently rejects their different pH/preparation/notes.'
  target_ids:
  - CultureMech:006731
  field_paths:
  - ph_range
  - notes
  - preparation_steps
  - data/normalized_yaml/bacterial/denitrovibrio_medium.yaml::preparation_steps
  evidence_ids:
  - dsmz881
  - api881
  - writer-resolver
  - writer-merger
  - writer-formulation
  rule_id: review-yaml-record/custom-preparation-ph-and-stale-output
  native_severity: P2
  normalization_reason: 'Custom completeness rule: material stage, preparation or
    supplied-form defect; native shape checks are not scientific proof.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-006731-supplied-sodium-and-nickel-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct sodium-resazurin and nickel hydrate assertions
  description: The source names sodium resazurin, but the primary CHEBI:8806 term
    is neutral resazurin. Nickel is explicitly NiCl2·6H2O, while both local slots
    use anhydrous CHEBI:34887. Verify an exact sodium-salt identity and canonical
    label without transferring a speculative candidate; CHEBI:53542 is the current
    OLS hexahydrate candidate, although the exact MIM preferred spelling 'NiCl2 x
    6 H2O' is REJECTED (row 6703), while 'Nickel (II) chloride hexahydrate' is MAPPED
    (row 6668). Preserve the amount and stage decisions separately.
  target_ids:
  - CultureMech:006731
  field_paths:
  - ingredients[8].term
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz881
  - api881
  - groundings
  - mim
  - chebi53542
  rule_id: review-yaml-record/custom-supplied-sodium-and-nickel-forms
  native_severity: P2
  normalization_reason: 'Custom grounding rule: material stage, preparation or supplied-form
    defect; native shape checks are not scientific proof.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-006731-quantity-evidence-and-event-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attach exact source claims and preserve original events
  description: No scoped quantity claims are attached. Current equal provider snippets/digests
    can authenticate content, not the original access event. Retain all original historical
    reports and malformed or timezone-naive import/resolver timestamps; append verified
    context if recovered. Historical ingredient-signature equality does not prove
    present complete formulation equivalence.
  target_ids:
  - CultureMech:006731
  field_paths:
  - ingredients[*].evidence
  - evidence
  - curation_history
  - parent_media
  - variant_modifications
  evidence_ids:
  - old-reports
  - old-claims
  - history
  - komodo881
  - komodoList
  - historical-joins
  rule_id: review-yaml-record/custom-quantity-evidence-and-event-metadata
  native_severity: P3
  normalization_reason: 'Custom provenance rule: bounded missing claim linkage and
    original-event metadata; preserve append-only provenance.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: The generated record keeps all nineteen stock components at main strength.
    Both contributors correctly nest FeCl2 and four vitamins, but leave the other
    fourteen stock components direct, omit the selenite-tungstate stock descriptor
    and assert an unsupported per-final-litre receiving basis. Preserve the source
    batch additions, explicit SL-10 final makeup and provider-declared stock rates.
    The primary water input does not prove the main final volume; no automatic replay
    of the current nesting script can repair a record that already has solutions.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006731
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: 'The DSM contributor preserves current pH 7.0–7.2 and the main staged
    preparation. Generated/KOMODO pH 6.8–7.2 and Aerobic: Yes conflict with the current
    primary; their preparation is absent. Preserve source/version distinctions rather
    than overwrite old history. Split the retained mixed-process paragraph and move
    SL-10 preparation into stock scope. Reconcile both maintained inputs before using
    the conservative merger, which currently rejects their different pH/preparation/notes.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006731
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: The source names sodium resazurin, but the primary CHEBI:8806 term
    is neutral resazurin. Nickel is explicitly NiCl2·6H2O, while both local slots
    use anhydrous CHEBI:34887. Verify an exact sodium-salt identity and canonical
    label without transferring a speculative candidate; CHEBI:53542 is the current
    OLS hexahydrate candidate, although the exact MIM preferred spelling 'NiCl2 x
    6 H2O' is REJECTED (row 6703), while 'Nickel (II) chloride hexahydrate' is MAPPED
    (row 6668). Preserve the amount and stage decisions separately.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006731
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
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
  description: No scoped quantity claims are attached. Current equal provider snippets/digests
    can authenticate content, not the original access event. Retain all original historical
    reports and malformed or timezone-naive import/resolver timestamps; append verified
    context if recovered. Historical ingredient-signature equality does not prove
    present complete formulation equivalence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006731
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/denitrovibrio_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Retain every original event/report byte-for-byte; append only independently verified
    correction context.
  - Attach exact source-stage claims and preserve direct KOMODO access limits; do
    not certify full equivalence from old ingredient-signature notes.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Exact KOMODO catalogue/accession routes returned 403; current primary/provider are
  available but complete accession-version verification remains partial.
- Provider main volume 1003 ml and explicit g_l describe its normalization; the primary
  lists 1000 ml water and stock additions without an independently measured final
  volume.
- HCl 25% lacks an explicit percent basis; no 7.7 M statement from another medium
  is transferred.
- Calcium-pantothenate stereochemistry and the exact replacement sodium-resazurin
  identifier require bounded follow-up; no unverified replacement ID is proposed.
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
