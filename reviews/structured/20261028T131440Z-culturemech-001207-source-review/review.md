# Scientific review: CY S2 MEDIUM

- Review: 20261028T131440Z-culturemech-001207-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:51.014300Z
- Finished UTC: 2026-10-28T13:14:40.561970Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 172a identity and nominal provider values are supported, including eight authenticated owner claims. One major stock-stage gap and two minor input-water/generated-evidence gaps remain; all retained quantities and preparation sentences are explicitly assessed.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch068 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001207 | data/merge_yaml/merged/CY_S2_MEDIUM.yaml | generated | cy_s2_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001207 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001207 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001207 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001207 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSMZ 172a identity

identity: supported. Targets: CultureMech:001207.

The selected target is the single DSMZ 172a CY S2 owner. The neighboring historical CYTOPHAGA marine review concerns DSM172 and another KOMODO172a input; its false-merge finding is not transferred to this target. No target organism is asserted.

### Physical state, classification and scope

representation: supported. Targets: CultureMech:001207.

Complex medium with yeast extract and agar is retained; no particular strain, growth result, temperature or incubation time is inferred. Existing pH and all three preparation descriptions are credited. Native diagnostics assess shape/labels, not the source-stage defects.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001207.

22 current concentration fields are covered by 30 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","quantity_field_count":22,"decisions":[{"quantity_id":"q1","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 4-4","quote":"NH4Cl                                                            1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"NH4Cl","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 4-4","quote":"NH4Cl                                                            1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 7.34835,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 5-5","quote":"KH2PO4                                                           1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 7.34835,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 5-5","quote":"KH2PO4                                                           1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 6-6","quote":"MgSO4 x 7 H2O                                                    1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 6-6","quote":"MgSO4 x 7 H2O                                                    1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.06","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.408122,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 7-7","quote":"CaCl2 x 2 H2O                                                    0.06       g","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.06","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.408122,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 7-7","quote":"CaCl2 x 2 H2O                                                    0.06       g","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 513.347,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 8-8","quote":"NaCl                                                            30.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"NaCl","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 513.347,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 8-8","quote":"NaCl                                                            30.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"FeCl3 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00125","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 1.25,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00125,\n                        \"mmol_l\": 0.00462456,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 9-9","quote":"FeCl3 x 6 H2O                                                    1.25      mg","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00125","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 1.25,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00125,\n                        \"mmol_l\": 0.00462456,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 9-9","quote":"FeCl3 x 6 H2O                                                    1.25      mg","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 10-10","quote":"Yeast extract                                                    1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Yeast extract","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 10-10","quote":"Yeast extract                                                    1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.97327,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 11-11","quote":"Agar                                                             1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"Agar","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and whole current API digest match the recorded October source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching batch input; its water row does not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.97327,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 11-11","quote":"Agar                                                             1.00       g","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Glucose","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; The API explicitly supplies this nominal g_l, consistent with the printed w/v stock strength and per-litre receiving dose. This supports the declared nominal recipe basis, not a measured final volume after additions; separate sterile stock identity/strength/dose is absent from the structured formulation.","source_stage":"post-autoclave stock-derived nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"attribute\": \"10% w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 17-17","quote":"Glucose (10% w/v)                                                 10.0     ml","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Glucose","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; The API explicitly supplies this nominal g_l, consistent with the printed w/v stock strength and per-litre receiving dose. This supports the declared nominal recipe basis, not a measured final volume after additions; separate sterile stock identity/strength/dose is absent from the structured formulation.","source_stage":"post-autoclave stock-derived nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"attribute\": \"10% w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 17-17","quote":"Glucose (10% w/v)                                                 10.0     ml","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; The API explicitly supplies this nominal g_l, consistent with the printed w/v stock strength and per-litre receiving dose. This supports the declared nominal recipe basis, not a measured final volume after additions; separate sterile stock identity/strength/dose is absent from the structured formulation.","source_stage":"post-autoclave stock-derived nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"5% w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 5.95188,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 18-18","quote":"NaHCO3 (5% w/v)                                                   10.0     ml","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"NaHCO3","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; The API explicitly supplies this nominal g_l, consistent with the printed w/v stock strength and per-litre receiving dose. This supports the declared nominal recipe basis, not a measured final volume after additions; separate sterile stock identity/strength/dose is absent from the structured formulation.","source_stage":"post-autoclave stock-derived nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"5% w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 5.95188,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 18-18","quote":"NaHCO3 (5% w/v)                                                   10.0     ml","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; The API explicitly supplies this nominal g_l, consistent with the printed w/v stock strength and per-litre receiving dose. This supports the declared nominal recipe basis, not a measured final volume after additions; separate sterile stock identity/strength/dose is absent from the structured formulation.","source_stage":"post-autoclave stock-derived nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"3% w/v\",\n                        \"amount\": 3.3,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.099,\n                        \"mmol_l\": 0.412187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 19-19","quote":"Na2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Na2S x 9 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current field lacks an attached exact supporting claim; The API explicitly supplies this nominal g_l, consistent with the printed w/v stock strength and per-litre receiving dose. This supports the declared nominal recipe basis, not a measured final volume after additions; separate sterile stock identity/strength/dose is absent from the structured formulation.","source_stage":"post-autoclave stock-derived nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"3% w/v\",\n                        \"amount\": 3.3,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.099,\n                        \"mmol_l\": 0.412187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 19-19","quote":"Na2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"Distilled-water input","local_fields":[],"decision":"evidence_only","rationale":"The source explicitly lists 1000 ml input water; no local water field or explicit final make-up exists. Retain as input volume, not 1000 g/L and not proof of final volume.","source_stage":"main solvent input","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 12-12","quote":"Distilled water                                               1000.00      ml","quote_basis":"derivative text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Glucose separate stock strength and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The printed 10% w/v stock and 10 ml/L receiving dose are explicit; preserve both, with post-autoclave separate-sterile context. Do not equate stock strength to final-medium concentration or infer an additive final volume.","source_stage":"source-only separately sterilized supplement","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 15-19","quote":"After autoclaving, add from separate sterile solutions per liter medium:\n\nGlucose (10% w/v)                                                 10.0     ml\nNaHCO3 (5% w/v)                                                   10.0     ml\nNa2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"attribute\": \"10% w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"NaHCO3 separate stock strength and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The printed 5% w/v stock and 10 ml/L receiving dose are explicit; preserve both, with post-autoclave separate-sterile context. Do not equate stock strength to final-medium concentration or infer an additive final volume.","source_stage":"source-only separately sterilized supplement","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 15-19","quote":"After autoclaving, add from separate sterile solutions per liter medium:\n\nGlucose (10% w/v)                                                 10.0     ml\nNaHCO3 (5% w/v)                                                   10.0     ml\nNa2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"5% w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 5.95188,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Na2S nonahydrate separate stock strength and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The printed 3% w/v stock and 3.3 ml/L receiving dose are explicit; preserve both, with post-autoclave separate-sterile context. Do not equate stock strength to final-medium concentration or infer an additive final volume.","source_stage":"source-only separately sterilized supplement","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 15-19","quote":"After autoclaving, add from separate sterile solutions per liter medium:\n\nGlucose (10% w/v)                                                 10.0     ml\nNaHCO3 (5% w/v)                                                   10.0     ml\nNa2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"3% w/v\",\n                        \"amount\": 3.3,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.099,\n                        \"mmol_l\": 0.412187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"pH 7.0","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ph_value","stored":7.0}],"decision":"evidence_only","rationale":"Both local values agree with the source and retained preparation description; no attached field-level source claim exists.","source_stage":"before autoclaving","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 14-14","quote":"Adjust pH to 7.0 and autoclave.","quote_basis":"derivative text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.medium","quote":"{\n            \"id\": \"172a\",\n            \"name\": \"CY S2 MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf\"\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Retained preparation step 1","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Adjust pH to 7.0 and autoclave."}},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Adjust pH to 7.0 and autoclave."}}],"decision":"evidence_only","rationale":"The complete source sentence is retained in both documents. Preserve its ordering and qualifiers; autoclave temperature/duration are not supplied, and 10 ml is vessel size rather than a measured fill or final batch volume.","source_stage":"preparation / source-only numeric qualifiers","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 10,\n                        \"step\": \"Adjust pH to 7.0 and autoclave.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 14-14","quote":"Adjust pH to 7.0 and autoclave.","quote_basis":"derivative text"}]},{"quantity_id":"q29","label":"Retained preparation step 2","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"After autoclaving, add from separate sterile solutions per liter medium:"}},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"After autoclaving, add from separate sterile solutions per liter medium:"}}],"decision":"evidence_only","rationale":"The complete source sentence is retained in both documents. Preserve its ordering and qualifiers; autoclave temperature/duration are not supplied, and 10 ml is vessel size rather than a measured fill or final batch volume.","source_stage":"preparation / source-only numeric qualifiers","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"recipe_order\": 10,\n                        \"step\": \"After autoclaving, add from separate sterile solutions per liter medium: \"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 15-15","quote":"After autoclaving, add from separate sterile solutions per liter medium:","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"Retained preparation step 3","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"Aseptically fill sterile 10-ml screwcap tubes almost completely with the medium. Make stab inoculation."}},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"Aseptically fill sterile 10-ml screwcap tubes almost completely with the medium. Make stab inoculation."}}],"decision":"evidence_only","rationale":"The complete source sentence is retained in both documents. Preserve its ordering and qualifiers; autoclave temperature/duration are not supplied, and 10 ml is vessel size rather than a measured fill or final batch volume.","source_stage":"preparation / source-only numeric qualifiers","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\": \"Aseptically fill sterile 10-ml screwcap tubes almost completely with the medium. Make stab inoculation.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt lines 21-22","quote":"Aseptically fill sterile 10-ml screwcap tubes almost completely with the medium. Make\nstab inoculation.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CY_S2_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/cy_s2_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:001207.

All 40 current chemical slots have fresh exact OLS objects. Source salts/hydrates agree with the asserted formulas, including calcium dihydrate, magnesium heptahydrate, ferric hexahydrate and sodium sulfide nonahydrate. Generic glucose remains generic; yeast extract has no invented compound ID. Each document has 10 secondary links among 11 ingredient instances; all 20 existing secondary slots match current identifiers and labels. Current MIM membership is distinct from source-form verification.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:001207.

The eight owner claims retain exact current raw-byte and literal correspondence; original October access times are not re-created. October5 reports were incomplete; October7 supplied main-recipe evidence and explicitly deferred stock attributes. The full neighboring September cytophaga report is comparison-only, not an assessment of this selected record. Current importer and conservative merger improvements are credited.

## Findings

### f1: Separate stock strength and receiving dose are not represented

major / open / confirmed; issue key: culturemech-001207-stock-stage.

The last three ingredients retain nominal provider g/L but lose the separate glucose, bicarbonate and sulfide stock strengths and receiving doses. The retained preparation sentence correctly says to add separate sterile solutions after autoclaving; credit that text. Represent the three source stocks and their explicit w/v strengths/doses without duplicating the nominal ingredient amount or inventing final volume. Current MediaDive _is_api_stock_addition and _parse_api_solutions already distinguish percent-stock additions, so this target/owner state is not proof that present code still flattens them.

### f2: Explicit input water is absent

minor / open / confirmed; issue key: culturemech-001207-missing-input-water.

Preserve the source distilled-water input as volume/preparation context. The source lists 1000 ml water but does not state measured final make-up after solids and supplements. Current MediaDive composition parsing skips water; any repair must retain its input-stage meaning rather than convert it to a mass concentration.

### f3: Generated target omits existing exact owner evidence

minor / open / confirmed; issue key: culturemech-001207-generated-evidence.

The owner has eight attached main-recipe claims whose literal snippets and entire API digest match the fresh response. The generated target omits these claims and the later curation/reference provenance. Preserve the existing repair and append any new source-stage assessment; regenerate through the current singleton/evidence-preserving path.

## Recommended Actions And Acceptance Checks

### a1

The last three ingredients retain nominal provider g/L but lose the separate glucose, bicarbonate and sulfide stock strengths and receiving doses. The retained preparation sentence correctly says to add separate sterile solutions after autoclaving; credit that text. Represent the three source stocks and their explicit w/v strengths/doses without duplicating the nominal ingredient amount or inventing final volume. Current MediaDive _is_api_stock_addition and _parse_api_solutions already distinguish percent-stock additions, so this target/owner state is not proof that present code still flattens them.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Preserve the source distilled-water input as volume/preparation context. The source lists 1000 ml water but does not state measured final make-up after solids and supplements. Current MediaDive composition parsing skips water; any repair must retain its input-stage meaning rather than convert it to a mass concentration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The owner has eight attached main-recipe claims whose literal snippets and entire API digest match the fresh response. The generated target omits these claims and the later curation/reference provenance. Preserve the existing repair and append any new source-stage assessment; regenerate through the current singleton/evidence-preserving path.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm172a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf; REVIEW_WORK/batch068/source07-08-10/dsm172a.json; exact original raw/text/hash/time metadata | context_only | Exact declared DSMZ primary for ordinary record07/08; source-specific organism context screened before assessment. |
| api172a | https://mediadive.dsmz.de/rest/medium/172a; REVIEW_WORK/batch068/source07-08-10/api172a.json; exact original raw/text/hash/time metadata | context_only | Exact declared provider counterpart; preserve source version, stages and explicit provider basis. |
| target | data/merge_yaml/merged/CY_S2_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/cy_s2_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/cy_s2_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CY_S2_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cy_s2_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/yaml_record_review/20260922T130947Z-cytophaga_marine_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch068/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch068/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch068/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch068/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch068/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch068/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; REVIEW_WORK/batch068/source07-08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch068/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch068/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254; REVIEW_WORK/batch068/source07-08-10/chebi86254.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch068/source07-08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17234; REVIEW_WORK/batch068/source07-08-10/chebi17234.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch068/source07-08-10/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch068/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| quantities | REVIEW_WORK/batch068/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch068/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch068/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch068/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch068/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch068/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch068/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch068/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch068/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch068/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch068/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T131440Z-culturemech-001207-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CY S2 MEDIUM'
started_at: '2026-10-28T13:11:51.014300Z'
finished_at: '2026-10-28T13:14:40.561970Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: DSMZ 172a identity and nominal provider values are supported, including eight
  authenticated owner claims. One major stock-stage gap and two minor input-water/generated-evidence
  gaps remain; all retained quantities and preparation sentences are explicitly assessed.
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
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CY_S2_MEDIUM.yaml
    sha256: c7375bfab1cb8d13ecfa54cf07c72bc29cb5985636dc871438e287e6fe47210b
    role: target
  - path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    sha256: 496158fae04a08be15696c576cecb45d6bb97e12434d9a244cc3d0f0588fc7ec
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/cy_s2_medium.yaml.md
    sha256: cc2e852c91851ad4179882212a9de2d20cfc05f5b410a55521bd115bb3343c6a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CY_S2_MEDIUM.md
    sha256: b0ae6724c5dd9e466a620e02cf612901848bb1ed53221ae12afc2739ea0ecf5d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cy_s2_medium.md
    sha256: 780288442063e1b2e3685da64626518536055153874fadf7502b35db3b8301bf
    role: context
  - path: reports/yaml_record_review/20260922T130947Z-cytophaga_marine_medium.md
    sha256: a288c605114a1a7ac9b8bae4e6b75423fc2faf4f959670022dc7cd589db0a52f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
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
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  selection: Authoritative batch068 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001207
targets:
- target_id: CultureMech:001207
  path: data/merge_yaml/merged/CY_S2_MEDIUM.yaml
  label: cy_s2_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001207
  command: just validate-schema data/merge_yaml/merged/CY_S2_MEDIUM.yaml
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
  - CultureMech:001207
  command: just validate-strict data/merge_yaml/merged/CY_S2_MEDIUM.yaml --out REVIEW_WORK/batch068/record07/strict.tsv
    --workers 1 --quiet
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
  - CultureMech:001207
  command: just validate-terms data/merge_yaml/merged/CY_S2_MEDIUM.yaml
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
  - CultureMech:001207
  command: just validate-references data/merge_yaml/merged/CY_S2_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm172a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf
  accessed_at: '2026-10-28T13:11:52.563986Z'
  locator: REVIEW_WORK/batch068/source07-08-10/dsm172a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact declared DSMZ primary for ordinary record07/08; source-specific organism
    context screened before assessment.
  snapshot_sha256: 4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240
- evidence_id: api172a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/172a
  accessed_at: '2026-10-28T13:11:52.231416Z'
  locator: REVIEW_WORK/batch068/source07-08-10/api172a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact declared provider counterpart; preserve source version, stages and
    explicit provider basis.
  snapshot_sha256: 3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CY_S2_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:14:40.503947Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: c7375bfab1cb8d13ecfa54cf07c72bc29cb5985636dc871438e287e6fe47210b
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cy_s2_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:14:40.504128Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 496158fae04a08be15696c576cecb45d6bb97e12434d9a244cc3d0f0588fc7ec
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:14:40.504161Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:14:40.504447Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:14:40.504471Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:14:40.504495Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:14:40.504520Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/cy_s2_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:14:40.510059Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: cc2e852c91851ad4179882212a9de2d20cfc05f5b410a55521bd115bb3343c6a
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CY_S2_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T13:14:40.510120Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b0ae6724c5dd9e466a620e02cf612901848bb1ed53221ae12afc2739ea0ecf5d
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cy_s2_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:14:40.510149Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 780288442063e1b2e3685da64626518536055153874fadf7502b35db3b8301bf
- evidence_id: report-21
  kind: prior_review
  reference: reports/yaml_record_review/20260922T130947Z-cytophaga_marine_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:14:40.510173Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a288c605114a1a7ac9b8bae4e6b75423fc2faf4f959670022dc7cd589db0a52f
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/historical-reading.json
  accessed_at: '2026-10-28T13:14:40.511280Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 135fc4b4b8c62989ad4fa121baa82e7228c8d92de8ec60d86e18c320163fa7e2
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:14:40.511320Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 6b5cb2a9d645d1c3ff7f048dcb53146724e1b71145db6a2ae59b67d1fe9b11bf
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/complete-document-reader.json
  accessed_at: '2026-10-28T13:14:40.511355Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: a52d63e1a76020741f402cb2f805b8b3a5f642a77402a3070b7f40a063a81647
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:14:40.511384Z'
  support: context_only
  summary: Current parser excludes percent-stock additions from primary ingredients,
    preserves referenced stock amounts/attributes separately and prioritizes explicit
    provider g_l. It skips source water; bare units alone do not establish a final-volume
    basis. Current code is not historical execution proof.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T13:14:40.511417Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch068/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T13:14:40.511440Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: cf4b1788c364d98627febb2732491e1d8f18709b9ba2c6a7b22d6ebb6e68fa91
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T13:11:53.777948Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T13:11:54.486969Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  accessed_at: '2026-10-28T13:11:53.837767Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi31795.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T13:11:55.863492Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T13:11:53.288008Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254
  accessed_at: '2026-10-28T13:11:55.052357Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi86254.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: b3a79ee6d9359b7b827f6f87134bc166d84d3948ec20c54965c6e706aecde3a4
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T13:11:53.355997Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17234
  accessed_at: '2026-10-28T13:11:53.285250Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi17234.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 91e3580b7a2c3718d25272b7ac62fe34badfa75bf58b16dd6ba08dfca987b859
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T13:11:53.886343Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T13:11:54.565471Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561233Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 0f42df7c3ec256fc3cd8ce8a20041f58111debb2996d1acfb81dbd9342a81490
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561291Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 4d82cc62997eadd278b02ff474f13c18fad2f7b00cc193ea5ad315b3c8cb26ab
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561352Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 9cc5891809dac4c050670a892a8a1cc3590b1166015d96900bc86e6d5574471f
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561390Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: aecdca2e880f15a82782208fbedaba558a37ca5a89e82363be570e9d88a40841
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561427Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: f1b550b5ad7845acf7a238766afd14468def183b9c3a1ac00b92a68c77cdb3fa
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561446Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: fb253fc05932517ea4f23a8139eff2c6bcb7f551f4cd84b79214df97c6dfa680
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch068/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:14:40.561464Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: fb65d33520979e5f71de0e57104255bbed11372b81fa4d2b1ffec05ba582615e
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record07/schema-result.json
  accessed_at: '2026-10-28T13:11:52.124306Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 258c77719175297e9f2e4793a78c7f9a01975be70217edf5f80ff889de998982
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record07/strict-result.json
  accessed_at: '2026-10-28T13:11:53.085896Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: ad3fe7cc4b4e9702612c4f4d68f95b3f1cd64d00d72ec94e1f73341cffa60cdb
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record07/terms-result.json
  accessed_at: '2026-10-28T13:11:54.125659Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 2cc1a4c6ba2badff3f55baa4a43ce00b7ceeeac7239ee8d4c3cc7784f6d34a2a
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch068/record07/references-result.json
  accessed_at: '2026-10-28T13:11:54.806978Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: c99ca4e38fcd9b0d7059372573883e6d890502b779d7be366031c830707d9cea
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSMZ 172a identity
  outcome: supported
  summary: The selected target is the single DSMZ 172a CY S2 owner. The neighboring
    historical CYTOPHAGA marine review concerns DSM172 and another KOMODO172a input;
    its false-merge finding is not transferred to this target. No target organism
    is asserted.
  target_ids:
  - CultureMech:001207
  evidence_ids:
  - target
  - owner
  - dsm172a
  - api172a
  - historical-reading
- assessment_id: representation
  area: representation
  topic: Physical state, classification and scope
  outcome: supported
  summary: Complex medium with yeast extract and agar is retained; no particular strain,
    growth result, temperature or incubation time is inferred. Existing pH and all
    three preparation descriptions are credited. Native diagnostics assess shape/labels,
    not the source-stage defects.
  target_ids:
  - CultureMech:001207
  evidence_ids:
  - target
  - owner
  - dsm172a
  - api172a
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 22 current concentration fields are covered by 30 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001207
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","quantity_field_count":22,"decisions":[{"quantity_id":"q1","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 4-4","quote":"NH4Cl                                                            1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q2","label":"NH4Cl","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 4-4","quote":"NH4Cl                                                            1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q3","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    7.34835,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 5-5","quote":"KH2PO4                                                           1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    7.34835,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 5-5","quote":"KH2PO4                                                           1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q5","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.05719,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 6-6","quote":"MgSO4 x 7 H2O                                                    1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q6","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.05719,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 6-6","quote":"MgSO4 x 7 H2O                                                    1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.06","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.06,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\":
    0.408122,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 7-7","quote":"CaCl2 x 2 H2O                                                    0.06       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q8","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.06","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.06,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\":
    0.408122,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 7-7","quote":"CaCl2 x 2 H2O                                                    0.06       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q9","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    513.347,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 8-8","quote":"NaCl                                                            30.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q10","label":"NaCl","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    513.347,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 8-8","quote":"NaCl                                                            30.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q11","label":"FeCl3 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00125","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\":
    82,\n                        \"amount\": 1.25,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00125,\n                        \"mmol_l\":
    0.00462456,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 9-9","quote":"FeCl3 x 6 H2O                                                    1.25      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q12","label":"FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.00125","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\":
    82,\n                        \"amount\": 1.25,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00125,\n                        \"mmol_l\":
    0.00462456,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 9-9","quote":"FeCl3 x 6 H2O                                                    1.25      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q13","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 10-10","quote":"Yeast extract                                                    1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q14","label":"Yeast extract","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 10-10","quote":"Yeast extract                                                    1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q15","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; the API explicitly supplies
    this main-recipe g_l. The PDF lists the matching batch input; its water row does
    not independently establish measured final volume.","source_stage":"main recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    2.97327,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 11-11","quote":"Agar                                                             1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q16","label":"Agar","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and whole current API digest match the recorded October
    source; the API explicitly supplies this main-recipe g_l. The PDF lists the matching
    batch input; its water row does not independently establish measured final volume.","source_stage":"main
    recipe","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    2.97327,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 11-11","quote":"Agar                                                             1.00       g","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"Glucose","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; The API explicitly supplies
    this nominal g_l, consistent with the printed w/v stock strength and per-litre
    receiving dose. This supports the declared nominal recipe basis, not a measured
    final volume after additions; separate sterile stock identity/strength/dose is
    absent from the structured formulation.","source_stage":"post-autoclave stock-derived
    nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"attribute\": \"10% w/v\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 17-17","quote":"Glucose (10% w/v)                                                 10.0     ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"Glucose","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; The API explicitly supplies
    this nominal g_l, consistent with the printed w/v stock strength and per-litre
    receiving dose. This supports the declared nominal recipe basis, not a measured
    final volume after additions; separate sterile stock identity/strength/dose is
    absent from the structured formulation.","source_stage":"post-autoclave stock-derived
    nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"attribute\": \"10% w/v\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 17-17","quote":"Glucose (10% w/v)                                                 10.0     ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; The API explicitly supplies
    this nominal g_l, consistent with the printed w/v stock strength and per-litre
    receiving dose. This supports the declared nominal recipe basis, not a measured
    final volume after additions; separate sterile stock identity/strength/dose is
    absent from the structured formulation.","source_stage":"post-autoclave stock-derived
    nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"5% w/v\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 5.95188,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 18-18","quote":"NaHCO3 (5% w/v)                                                   10.0     ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q20","label":"NaHCO3","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; The API explicitly supplies
    this nominal g_l, consistent with the printed w/v stock strength and per-litre
    receiving dose. This supports the declared nominal recipe basis, not a measured
    final volume after additions; separate sterile stock identity/strength/dose is
    absent from the structured formulation.","source_stage":"post-autoclave stock-derived
    nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"5% w/v\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 5.95188,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 18-18","quote":"NaHCO3 (5% w/v)                                                   10.0     ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q21","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; The API explicitly supplies
    this nominal g_l, consistent with the printed w/v stock strength and per-litre
    receiving dose. This supports the declared nominal recipe basis, not a measured
    final volume after additions; separate sterile stock identity/strength/dose is
    absent from the structured formulation.","source_stage":"post-autoclave stock-derived
    nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"3% w/v\",\n                        \"amount\":
    3.3,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.099,\n                        \"mmol_l\": 0.412187,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 19-19","quote":"Na2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q22","label":"Na2S x 9 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current field lacks an attached exact supporting claim; The API explicitly supplies
    this nominal g_l, consistent with the printed w/v stock strength and per-litre
    receiving dose. This supports the declared nominal recipe basis, not a measured
    final volume after additions; separate sterile stock identity/strength/dose is
    absent from the structured formulation.","source_stage":"post-autoclave stock-derived
    nominal recipe rate","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"3% w/v\",\n                        \"amount\":
    3.3,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.099,\n                        \"mmol_l\": 0.412187,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 19-19","quote":"Na2S x 9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q23","label":"Distilled-water input","local_fields":[],"decision":"evidence_only","rationale":"The
    source explicitly lists 1000 ml input water; no local water field or explicit
    final make-up exists. Retain as input volume, not 1000 g/L and not proof of final
    volume.","source_stage":"main solvent input","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 12-12","quote":"Distilled water                                               1000.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"Glucose separate stock strength and receiving
    dose","local_fields":[],"decision":"evidence_only","rationale":"The printed 10%
    w/v stock and 10 ml/L receiving dose are explicit; preserve both, with post-autoclave
    separate-sterile context. Do not equate stock strength to final-medium concentration
    or infer an additive final volume.","source_stage":"source-only separately sterilized
    supplement","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 15-19","quote":"After autoclaving, add from separate sterile solutions per
    liter medium:\n\nGlucose (10% w/v)                                                 10.0     ml\nNaHCO3
    (5% w/v)                                                   10.0     ml\nNa2S x
    9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative
    text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"attribute\": \"10% w/v\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"NaHCO3
    separate stock strength and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The
    printed 5% w/v stock and 10 ml/L receiving dose are explicit; preserve both, with
    post-autoclave separate-sterile context. Do not equate stock strength to final-medium
    concentration or infer an additive final volume.","source_stage":"source-only
    separately sterilized supplement","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 15-19","quote":"After autoclaving, add from separate sterile solutions per
    liter medium:\n\nGlucose (10% w/v)                                                 10.0     ml\nNaHCO3
    (5% w/v)                                                   10.0     ml\nNa2S x
    9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative
    text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"5% w/v\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 5.95188,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Na2S
    nonahydrate separate stock strength and receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The
    printed 3% w/v stock and 3.3 ml/L receiving dose are explicit; preserve both,
    with post-autoclave separate-sterile context. Do not equate stock strength to
    final-medium concentration or infer an additive final volume.","source_stage":"source-only
    separately sterilized supplement","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 15-19","quote":"After autoclaving, add from separate sterile solutions per
    liter medium:\n\nGlucose (10% w/v)                                                 10.0     ml\nNaHCO3
    (5% w/v)                                                   10.0     ml\nNa2S x
    9 H2O (3% w/v)                                              3.3     ml","quote_basis":"derivative
    text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"3% w/v\",\n                        \"amount\":
    3.3,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.099,\n                        \"mmol_l\": 0.412187,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"pH
    7.0","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"ph_value","stored":7.0}],"decision":"evidence_only","rationale":"Both
    local values agree with the source and retained preparation description; no attached
    field-level source claim exists.","source_stage":"before autoclaving","sources":[{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 14-14","quote":"Adjust pH to 7.0 and autoclave.","quote_basis":"derivative
    text"},{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.medium","quote":"{\n            \"id\":
    \"172a\",\n            \"name\": \"CY S2 MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf\"\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Retained preparation step 1","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Adjust
    pH to 7.0 and autoclave."}},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Adjust
    pH to 7.0 and autoclave."}}],"decision":"evidence_only","rationale":"The complete
    source sentence is retained in both documents. Preserve its ordering and qualifiers;
    autoclave temperature/duration are not supplied, and 10 ml is vessel size rather
    than a measured fill or final batch volume.","source_stage":"preparation / source-only
    numeric qualifiers","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"step\": \"Adjust pH to 7.0 and autoclave.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 14-14","quote":"Adjust pH to 7.0 and autoclave.","quote_basis":"derivative
    text"}]},{"quantity_id":"q29","label":"Retained preparation step 2","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"After
    autoclaving, add from separate sterile solutions per liter medium:"}},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"After
    autoclaving, add from separate sterile solutions per liter medium:"}}],"decision":"evidence_only","rationale":"The
    complete source sentence is retained in both documents. Preserve its ordering
    and qualifiers; autoclave temperature/duration are not supplied, and 10 ml is
    vessel size rather than a measured fill or final batch volume.","source_stage":"preparation
    / source-only numeric qualifiers","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"step\": \"After autoclaving, add from separate
    sterile solutions per liter medium: \"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 15-15","quote":"After autoclaving, add from separate sterile solutions per
    liter medium:","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"Retained
    preparation step 3","local_fields":[{"path":"data/merge_yaml/merged/CY_S2_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"Aseptically
    fill sterile 10-ml screwcap tubes almost completely with the medium. Make stab
    inoculation."}},{"path":"data/normalized_yaml/bacterial/cy_s2_medium.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"Aseptically
    fill sterile 10-ml screwcap tubes almost completely with the medium. Make stab
    inoculation."}}],"decision":"evidence_only","rationale":"The complete source sentence
    is retained in both documents. Preserve its ordering and qualifiers; autoclave
    temperature/duration are not supplied, and 10 ml is vessel size rather than a
    measured fill or final batch volume.","source_stage":"preparation / source-only
    numeric qualifiers","sources":[{"evidence_id":"api172a","reference":"https://mediadive.dsmz.de/rest/medium/172a","raw_path":"REVIEW_WORK/batch068/source07-08-10/api172a.raw","raw_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","text_sha256":"3b00e137d1becf5285a42d8e52507db9591828f301b415291d319b417f46e216","accessed_at":"2026-10-28T13:11:52.231416Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\":
    \"Aseptically fill sterile 10-ml screwcap tubes almost completely with the medium.
    Make stab inoculation.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm172a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium172a.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm172a.raw","raw_sha256":"4e89c745d8ce6bb1f606ffb6457f02fb820838ec3640446a70ab62f5a2627240","text_sha256":"180cd960510da5049b785a60056d33a7b4b9dd026f9c162427df6ecafca43fe7","accessed_at":"2026-10-28T13:11:52.563986Z","locator":"dsm172a.txt
    lines 21-22","quote":"Aseptically fill sterile 10-ml screwcap tubes almost completely
    with the medium. Make\nstab inoculation.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CY_S2_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/cy_s2_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: All 40 current chemical slots have fresh exact OLS objects. Source salts/hydrates
    agree with the asserted formulas, including calcium dihydrate, magnesium heptahydrate,
    ferric hexahydrate and sodium sulfide nonahydrate. Generic glucose remains generic;
    yeast extract has no invented compound ID. Each document has 10 secondary links
    among 11 ingredient instances; all 20 existing secondary slots match current identifiers
    and labels. Current MIM membership is distinct from source-form verification.
  target_ids:
  - CultureMech:001207
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: The eight owner claims retain exact current raw-byte and literal correspondence;
    original October access times are not re-created. October5 reports were incomplete;
    October7 supplied main-recipe evidence and explicitly deferred stock attributes.
    The full neighboring September cytophaga report is comparison-only, not an assessment
    of this selected record. Current importer and conservative merger improvements
    are credited.
  target_ids:
  - CultureMech:001207
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-001207-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate stock strength and receiving dose are not represented
  description: The last three ingredients retain nominal provider g/L but lose the
    separate glucose, bicarbonate and sulfide stock strengths and receiving doses.
    The retained preparation sentence correctly says to add separate sterile solutions
    after autoclaving; credit that text. Represent the three source stocks and their
    explicit w/v strengths/doses without duplicating the nominal ingredient amount
    or inventing final volume. Current MediaDive _is_api_stock_addition and _parse_api_solutions
    already distinguish percent-stock additions, so this target/owner state is not
    proof that present code still flattens them.
  target_ids:
  - CultureMech:001207
  field_paths:
  - ingredients[8]
  - ingredients[9]
  - ingredients[10]
  - solutions
  - preparation_steps[1]
  evidence_ids:
  - target
  - owner
  - dsm172a
  - api172a
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-001207-missing-input-water
  category: quantity
  severity: minor
  status: open
  certainty: confirmed
  title: Explicit input water is absent
  description: Preserve the source distilled-water input as volume/preparation context.
    The source lists 1000 ml water but does not state measured final make-up after
    solids and supplements. Current MediaDive composition parsing skips water; any
    repair must retain its input-stage meaning rather than convert it to a mass concentration.
  target_ids:
  - CultureMech:001207
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - dsm172a
  - api172a
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-001207-generated-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Generated target omits existing exact owner evidence
  description: The owner has eight attached main-recipe claims whose literal snippets
    and entire API digest match the fresh response. The generated target omits these
    claims and the later curation/reference provenance. Preserve the existing repair
    and append any new source-stage assessment; regenerate through the current singleton/evidence-preserving
    path.
  target_ids:
  - CultureMech:001207
  field_paths:
  - ingredients
  - references
  - curation_history
  evidence_ids:
  - target
  - owner
  - api172a
  - old-claims
  - writer-merger
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: The last three ingredients retain nominal provider g/L but lose the
    separate glucose, bicarbonate and sulfide stock strengths and receiving doses.
    The retained preparation sentence correctly says to add separate sterile solutions
    after autoclaving; credit that text. Represent the three source stocks and their
    explicit w/v strengths/doses without duplicating the nominal ingredient amount
    or inventing final volume. Current MediaDive _is_api_stock_addition and _parse_api_solutions
    already distinguish percent-stock additions, so this target/owner state is not
    proof that present code still flattens them.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001207
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Preserve the source distilled-water input as volume/preparation context.
    The source lists 1000 ml water but does not state measured final make-up after
    solids and supplements. Current MediaDive composition parsing skips water; any
    repair must retain its input-stage meaning rather than convert it to a mass concentration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001207
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: The owner has eight attached main-recipe claims whose literal snippets
    and entire API digest match the fresh response. The generated target omits these
    claims and the later curation/reference provenance. Preserve the existing repair
    and append any new source-stage assessment; regenerate through the current singleton/evidence-preserving
    path.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001207
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_s2_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
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
