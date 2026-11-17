# Scientific review: CZAPEK Peptone AGAR

- Review: 20261028T131726Z-culturemech-006636-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:55.182624Z
- Finished UTC: 2026-10-28T13:17:26.170443Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Partial review: one major agar source-version conflict and four minor evidence/preparation, input-water, legacy secondary-link and historical timestamp issues. Every current concentration is assessed;18 owner claims retain exact current API authentication without certifying the inaccessible KOMODO event.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch068 index 08
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006636 | data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml | generated | czapek_peptone_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:006636 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:006636 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:006636 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:006636 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Two source branches and exact accession scope

identity: concern. Targets: CultureMech:006636.

The selected generated record declares the bacterial KOMODO83 and fungal DSM83 owners. Fresh DSM83 API/PDF are readable; exact historical KOMODO83 and MediaList routes return 403, leaving the original mapping event unverified. The preserved catalogue snippet supports only the historical identity claim; no unrelated 12% NaCl variant or organism growth claim is transferred.

### Classification and native structural diagnostics

representation: supported. Targets: CultureMech:006636.

Complex agar medium and existing pH metadata are retained; bacterial/fungal category labels are source classifications, not strain-growth evidence. No sterilization time/temperature or growth condition is invented from a generic medium title.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:006636.

27 current concentration fields are covered by 30 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","quantity_field_count":27,"decisions":[{"quantity_id":"q1","label":"Sucrose","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 4-4","quote":"Sucrose                                    30.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\": 108,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 87.6424,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Sucrose","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 4-4","quote":"Sucrose                                    30.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\": 108,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 87.6424,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Sucrose","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 4-4","quote":"Sucrose                                    30.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\": 108,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 87.6424,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaNO3","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 5-5","quote":"NaNO3                                       3.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 35.2962,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NaNO3","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 5-5","quote":"NaNO3                                       3.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 35.2962,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"NaNO3","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 5-5","quote":"NaNO3                                       3.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 35.2962,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 6-6","quote":"K2HPO4                                      1.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"K2HPO4","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 6-6","quote":"K2HPO4                                      1.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"K2HPO4","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 6-6","quote":"K2HPO4                                      1.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 7-7","quote":"MgSO4 x 7 H2O                               0.50    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 7-7","quote":"MgSO4 x 7 H2O                               0.50    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 7-7","quote":"MgSO4 x 7 H2O                               0.50    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 8-8","quote":"KCl                                         0.50    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 6.70691,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"KCl","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 8-8","quote":"KCl                                         0.50    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 6.70691,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"KCl","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 8-8","quote":"KCl                                         0.50    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 6.70691,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 9-9","quote":"FeSO4 x 7 H2O                               0.01    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 9-9","quote":"FeSO4 x 7 H2O                               0.01    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 9-9","quote":"FeSO4 x 7 H2O                               0.01    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 10-10","quote":"Yeast extract                               2.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Yeast extract","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 10-10","quote":"Yeast extract                               2.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Yeast extract","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 10-10","quote":"Yeast extract                               2.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Peptone","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The generated field lacks the attached claim retained by its owners. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 11-11","quote":"Peptone                                     5.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Peptone","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 11-11","quote":"Peptone                                     5.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Peptone","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing owner literal claim and current whole API digest match. The API explicitly declares this main-recipe g_l, and the primary table has the matching mass input. This verifies the provider basis, not a separately measured final-medium volume or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 11-11","quote":"Peptone                                     5.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The local20 G_PER_L and retained owner claim match current API g_l=20 and its historical whole-response digest, but the exact DSM83 PDF lists15 g agar in its batch table. Preserve both dated source versions and resolve the conflict before choosing a formulation; the PDF water input is not measured final volume.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 12-12","quote":"Agar                                       15.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Agar","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The local20 G_PER_L and retained owner claim match current API g_l=20 and its historical whole-response digest, but the exact DSM83 PDF lists15 g agar in its batch table. Preserve both dated source versions and resolve the conflict before choosing a formulation; the PDF water input is not measured final volume.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 12-12","quote":"Agar                                       15.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Agar","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The local20 G_PER_L and retained owner claim match current API g_l=20 and its historical whole-response digest, but the exact DSM83 PDF lists15 g agar in its batch table. Preserve both dated source versions and resolve the conflict before choosing a formulation; the PDF water input is not measured final volume.","source_stage":"DSM83 main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 12-12","quote":"Agar                                       15.00    g","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Source water input","local_fields":[],"decision":"evidence_only","rationale":"Both sources list 1000 ml water as batch input. No target/owner solvent field exists; retain volume or preparation context rather than infer measured final volume or a mass concentration.","source_stage":"source-only solvent input","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 13-13","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"pH 7.3","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ph_value","stored":7.3},{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ph_value","stored":7.3},{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ph_value","stored":7.3}],"decision":"evidence_only","rationale":"All three values are unchanged and supported; no field-level pH claim is attached. The fungal owner already preserves the adjustment sentence.","source_stage":"main-recipe pH","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 15-15","quote":"Adjust pH to 7.3.","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.medium","quote":"{\n            \"id\": 83,\n            \"name\": \"CZAPEK PEPTONE AGAR\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 7.3,\n            \"max_pH\": 7.3,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf\"\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Retained fungal-owner pH instruction","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"ADJUST_PH","description":"Adjust pH to 7.3."}}],"decision":"evidence_only","rationale":"The exact adjustment sentence is present in this owner and absent from the generated and bacterial records; preserve it without inventing time or temperature.","source_stage":"preparation","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt lines 15-15","quote":"Adjust pH to 7.3.","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Adjust pH to 7.3.\"\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml":null,"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml":null,"data/normalized_yaml/fungal/czapek_peptone_agar.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:006636.

Each document has seven secondary links among nine ingredients: six CHEBI-backed secondary slots and one legacy nitrate slot. The 18 CHEBI-backed secondary slots have exact current label/ID correspondence; the three legacy slots have no current exact MIM row and are excluded from that label-agreement population. All 21 primary chemical slots resolve to seven fresh exact OLS objects; the printed magnesium and iron heptahydrates agree with those formulas. Peptone and yeast extract remain mixtures without invented compound groundings. Source agar quantity disagreement is separate from correct agar identity.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:006636.

All 18 ingredient snippets retain exact current API digest matches; the catalogue claim does not because both current KOMODO routes return 403. The five complete historical reports and three selected parent objects remain derivative provenance; no original access timestamp is recovered merely from equal current bytes. Existing repairs are credited, while malformed embedded timestamps require append-only clarification.

## Findings

### f1: DSM83 PDF and API disagree on agar

major / open / confirmed; issue key: culturemech-006636-agar-source-conflict.

The current API and both maintained records encode20 g/L agar, while the exact DSM83 PDF lists15 g in the batch table. Existing owner evidence authenticates the API value, including its unchanged raw digest, but does not resolve the conflicting primary version. Retain both captures and explicit source-version provenance; do not silently replace one value or certify a measured final volume.

### f2: Generated record loses repaired evidence and preparation

minor / open / confirmed; issue key: culturemech-006636-generated-provenance.

Both owners retain nine exact API ingredient claims; all 18 snippets and their current whole-response digests match, including the agar claim that remains scientifically conflicted. The generated record loses those claims/references and omits the fungal owner pH-adjustment instruction, although ph_value 7.3 is retained. The two owner notes/preparation fields differ, so current exact-formulation merging must respect those differences instead of assuming ingredient-only equivalence. Preserve existing repairs and regenerate with the current conservative merge behavior.

### f3: Source solvent input is omitted

minor / open / confirmed; issue key: culturemech-006636-missing-input-water.

Preserve the explicit distilled-water batch input in each applicable maintained source context as volume/preparation information. Current importer skips water rows; do not infer final-volume make-up or convert water to grams per litre.

### f4: Legacy nitrate secondary identifiers lack current snapshot correspondence

minor / open / confirmed; issue key: culturemech-006636-legacy-nitrate-link.

Each document retains MediaIngredientMech:000171 on nitrate. The exact current 9077-row MIM snapshot has no matching legacy identifier; the ingredient primary CHEBI:63005 resolves to sodium nitrate and has current MIM membership. Preserve the old provenance while reconciling the secondary link against the exact current mapping. Absence from this snapshot is not an independently verified historical deprecation or wrong-primary-ID claim.

### f5: Embedded historical import timestamp is malformed

minor / open / confirmed; issue key: culturemech-006636-history-timestamp.

The generated and bacterial-owner import timestamp ends in literal .fZ, and the later resolver timestamp omits a timezone. Keep the original history as evidence; append an accurately timed clarification if its provenance can be established, rather than fabricating the original instant or silently rewriting history. Audit the responsible historical writer before claiming a live formatting defect.

## Recommended Actions And Acceptance Checks

### a1

The current API and both maintained records encode20 g/L agar, while the exact DSM83 PDF lists15 g in the batch table. Existing owner evidence authenticates the API value, including its unchanged raw digest, but does not resolve the conflicting primary version. Retain both captures and explicit source-version provenance; do not silently replace one value or certify a measured final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Both owners retain nine exact API ingredient claims; all 18 snippets and their current whole-response digests match, including the agar claim that remains scientifically conflicted. The generated record loses those claims/references and omits the fungal owner pH-adjustment instruction, although ph_value 7.3 is retained. The two owner notes/preparation fields differ, so current exact-formulation merging must respect those differences instead of assuming ingredient-only equivalence. Preserve existing repairs and regenerate with the current conservative merge behavior.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Preserve the explicit distilled-water batch input in each applicable maintained source context as volume/preparation information. Current importer skips water rows; do not infer final-volume make-up or convert water to grams per litre.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Each document retains MediaIngredientMech:000171 on nitrate. The exact current 9077-row MIM snapshot has no matching legacy identifier; the ingredient primary CHEBI:63005 resolves to sodium nitrate and has current MIM membership. Preserve the old provenance while reconciling the secondary link against the exact current mapping. Absence from this snapshot is not an independently verified historical deprecation or wrong-primary-ID claim.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The generated and bacterial-owner import timestamp ends in literal .fZ, and the later resolver timestamp omits a timezone. Keep the original history as evidence; append an accurately timed clarification if its provenance can be established, rather than fabricating the original instant or silently rewriting history. Audit the responsible historical writer before claiming a live formatting defect.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm83 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf; REVIEW_WORK/batch068/source07-08-10/dsm83.json; exact original raw/text/hash/time metadata | context_only | Exact declared DSMZ primary for ordinary record07/08; source-specific organism context screened before assessment. |
| api83 | https://mediadive.dsmz.de/rest/medium/83; REVIEW_WORK/batch068/source07-08-10/api83.json; exact original raw/text/hash/time metadata | context_only | Exact declared provider counterpart; preserve source version, stages and explicit provider basis. |
| komodo83 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=83; REVIEW_WORK/batch068/source07-08-10/komodo83.json; exact original raw/text/hash/time metadata | context_only | Exact historical MediaInfo hyperlink for KOMODO83 only; no inferred variant equivalence. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch068/source07-08-10/komodoList.json; exact original raw/text/hash/time metadata | context_only | Exact existing attached identity catalogue URL; ingredient amounts are separately assessed. |
| target | data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/czapek_peptone_agar.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/fungal/czapek_peptone_agar.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/inspected-candidate-context.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/czapek_peptone_agar.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/fungal/czapek_peptone_agar.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/czapek_peptone_agar.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/fungal/czapek_peptone_agar.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch068/record08/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch068/record08/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch068/record08/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch068/record08/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| writer-mim | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi, _rewrite_entry, migrate_file | context_only | Current _resolve_chebi preserves existing CHEBI identity, requires current membership, and _rewrite_entry replaces a legacy link only after that check; unmappable legacy links remain unchanged. This is current-code context, not proof of an earlier migration execution. |
| chebi17992 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17992; REVIEW_WORK/batch068/source07-08-10/chebi17992.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63005; REVIEW_WORK/batch068/source07-08-10/chebi63005.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch068/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; REVIEW_WORK/batch068/source07-08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch068/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch068/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch068/source07-08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| quantities | REVIEW_WORK/batch068/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch068/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch068/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch068/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch068/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch068/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch068/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch068/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch068/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch068/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch068/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Review completion is partial because the exact KOMODO branch/catalogue cannot be freshly authenticated and the primary PDF/API agar discrepancy remains unresolved.
- The nearby CZAPEK12%NaCl record is a separate uninspected variant; none of its conditions or findings are transferred.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T131726Z-culturemech-006636-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CZAPEK Peptone AGAR'
started_at: '2026-10-28T13:11:55.182624Z'
finished_at: '2026-10-28T13:17:26.170443Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Partial review: one major agar source-version conflict and four minor evidence/preparation,
  input-water, legacy secondary-link and historical timestamp issues. Every current
  concentration is assessed;18 owner claims retain exact current API authentication
  without certifying the inaccessible KOMODO event.'
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
  - path: data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml
    sha256: 899ae03c0196e9a0e17393fcd8130494fb88756ac5d322c17d7148bfedb1c5ab
    role: target
  - path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    sha256: 1ed4a6fbffb26ace3cd769d928dfda305fe5785b8e5e736a33447dd8f7e00662
    role: context
  - path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    sha256: 9a92d0332c588a19c301a582dfb38a51110238f77864dfa0fdc15a9d773de77a
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/inspected-candidate-context.json
    sha256: b7c93f3e550e036ef9c2b49f25cc543e6a38e57fc628e6eb7159b00e39d2c7fb
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json
    sha256: 7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/czapek_peptone_agar.yaml.md
    sha256: 782a4a23a7b7dc83a0bccd2bdc2da71498dd40eee35cc8f6b3d5cb97b2bf5d06
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/fungal/czapek_peptone_agar.yaml.md
    sha256: d58ef7406c5904beccfd6af76f5aa325e5e119eb4e5309497eafd75ee145ded0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.md
    sha256: 344faee81d882ea5fcdc51cdd4c8b439664ba2692d024009fb5c01cf09c90b51
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/czapek_peptone_agar.md
    sha256: d8f90c12a743b08f41a4d27ce826f14b6822588f45e16a427991a648d16ce944
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/fungal/czapek_peptone_agar.md
    sha256: 7cfe74e3911412783e73ab87d247444a242ded4f75a9022f88e5c76082699b8d
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
  selection: Authoritative batch068 index 08
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006636
targets:
- target_id: CultureMech:006636
  path: data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml
  label: czapek_peptone_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
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
  - CultureMech:006636
  command: just validate-schema data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml
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
  - CultureMech:006636
  command: just validate-strict data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml --out
    REVIEW_WORK/batch068/record08/strict.tsv --workers 1 --quiet
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
  - CultureMech:006636
  command: just validate-terms data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml
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
  - CultureMech:006636
  command: just validate-references data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm83
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf
  accessed_at: '2026-10-28T13:11:52.583990Z'
  locator: REVIEW_WORK/batch068/source07-08-10/dsm83.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact declared DSMZ primary for ordinary record07/08; source-specific organism
    context screened before assessment.
  snapshot_sha256: b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d
- evidence_id: api83
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/83
  accessed_at: '2026-10-28T13:11:52.226611Z'
  locator: REVIEW_WORK/batch068/source07-08-10/api83.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact declared provider counterpart; preserve source version, stages and
    explicit provider basis.
  snapshot_sha256: 24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c
- evidence_id: komodo83
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=83
  accessed_at: '2026-10-28T13:11:51.909241Z'
  locator: REVIEW_WORK/batch068/source07-08-10/komodo83.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical MediaInfo hyperlink for KOMODO83 only; no inferred variant
    equivalence.
  snapshot_sha256: c4e50d2839a8cf8fb961f4224b6ae1e34dc6e2c760b2e42872161462b6989b2b
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=83;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T13:11:51.967104Z'
  locator: REVIEW_WORK/batch068/source07-08-10/komodoList.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact existing attached identity catalogue URL; ingredient amounts are
    separately assessed.
  snapshot_sha256: d3dccffcd87ca24bb05200f18641aa375876498f7b307d8b520e891661a9a942
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:16:15.674755Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 899ae03c0196e9a0e17393fcd8130494fb88756ac5d322c17d7148bfedb1c5ab
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:16:15.674929Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 1ed4a6fbffb26ace3cd769d928dfda305fe5785b8e5e736a33447dd8f7e00662
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:16:15.674960Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:16:15.675260Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:16:15.675283Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:16:15.675305Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:16:15.675329Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 9a92d0332c588a19c301a582dfb38a51110238f77864dfa0fdc15a9d773de77a
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/inspected-candidate-context.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:16:15.675355Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: b7c93f3e550e036ef9c2b49f25cc543e6a38e57fc628e6eb7159b00e39d2c7fb
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:16:15.675476Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 7a936ec4bde63107f1315e9f6c4bcaa7b5c1fe6136cb23457754601dbe37e500
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/czapek_peptone_agar.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:16:15.679450Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 782a4a23a7b7dc83a0bccd2bdc2da71498dd40eee35cc8f6b3d5cb97b2bf5d06
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:16:15.679504Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/fungal/czapek_peptone_agar.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:16:15.685110Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d58ef7406c5904beccfd6af76f5aa325e5e119eb4e5309497eafd75ee145ded0
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.md
  locator: Complete report
  accessed_at: '2026-10-28T13:16:15.685176Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 344faee81d882ea5fcdc51cdd4c8b439664ba2692d024009fb5c01cf09c90b51
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/czapek_peptone_agar.md
  locator: Complete report
  accessed_at: '2026-10-28T13:16:15.685205Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d8f90c12a743b08f41a4d27ce826f14b6822588f45e16a427991a648d16ce944
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/fungal/czapek_peptone_agar.md
  locator: Complete report
  accessed_at: '2026-10-28T13:16:15.685228Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 7cfe74e3911412783e73ab87d247444a242ded4f75a9022f88e5c76082699b8d
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/historical-reading.json
  accessed_at: '2026-10-28T13:16:15.686594Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: e2a5ecb406025d00d1bcc7017e82d5aa0a02068b83cf1b111f9dfa1c402be693
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:16:15.686639Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 9f14e62602f884449f9197c6861ac77bf3643fadae230069eb0118fd0c165370
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/complete-document-reader.json
  accessed_at: '2026-10-28T13:16:15.686804Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: a7e5b6963e400f01f31585435fa3783c38a3714949795f414c56e29fb700751b
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:16:15.686842Z'
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
  accessed_at: '2026-10-28T13:16:15.686875Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch068/record08/historical-current-object-joins.json
  accessed_at: '2026-10-28T13:16:15.686898Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 1b46f735374d77efcfde7ea4b30886b36dee2561f946193c25c6d41526a0930e
- evidence_id: writer-mim
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi, _rewrite_entry, migrate_file
  accessed_at: '2026-10-28T13:16:15.686933Z'
  support: context_only
  summary: Current _resolve_chebi preserves existing CHEBI identity, requires current
    membership, and _rewrite_entry replaces a legacy link only after that check; unmappable
    legacy links remain unchanged. This is current-code context, not proof of an earlier
    migration execution.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: chebi17992
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17992
  accessed_at: '2026-10-28T13:11:53.238738Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi17992.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 2ae9545ca2aa881a60170edd0ee4843850f3864396aef39ee387b7f71e6c833d
- evidence_id: chebi63005
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63005
  accessed_at: '2026-10-28T13:11:54.341187Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi63005.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: f939d1fb0ecd70237f05d967ccb3c588813ee46c66ff74de2355aeca2bd22ebb
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T13:11:53.179234Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
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
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T13:11:54.455173Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T13:11:54.448264Z'
  locator: REVIEW_WORK/batch068/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
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
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:26.170436Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 7320c79017559631e04dca8d259d02731a4e14e523d1ad59498bc7790009601b
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:16:15.747439Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 2cf6f011ac81ec9313913f2c4bfe2269dfc8340b5d5065033234cdd9a1bf566c
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:16:15.747501Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 589b0203076c573408fc38165947e390a7989a1e75d8c04dfddf4688af163e56
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:16:15.747555Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: c9bfe6a8c61eea749a1c8b113e1f80b2b26671eb97f8925a8a785dbca733b142
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:16:15.747605Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 2c7b5f05d93e933f9e4c90bf6709d639cbac15b4e9fa13058002489e01db103b
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:16:15.747628Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: bc1589e238aea9008413bfc9aa2370163dc0d0531d61e959a9c6deed65e1b1d7
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch068/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:16:15.747648Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 2861cff684634dea5e8735833e728555232874373e6b757d2a88b9d8d8e6da59
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record08/schema-result.json
  accessed_at: '2026-10-28T13:11:56.266403Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 353c9b2ddfbdafd9f3b7dc7250d1341b3746c3e1d39c40914e5d898cbf5be68c
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record08/strict-result.json
  accessed_at: '2026-10-28T13:11:57.189965Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 154b6b84dac7cb822bef4cf1874468a51548ec75c2fcd3e9d2697443ac41daff
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record08/terms-result.json
  accessed_at: '2026-10-28T13:11:58.215485Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4d70db44f91cb8513501803523432a532c9300ed794836901f83df18a4004e26
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch068/record08/references-result.json
  accessed_at: '2026-10-28T13:11:58.866810Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 94b6498d0a7b5899fe9fa8958baef3f681818fe73366cc4b648cfe44f0d096d7
assessments:
- assessment_id: identity
  area: identity
  topic: Two source branches and exact accession scope
  outcome: concern
  summary: The selected generated record declares the bacterial KOMODO83 and fungal
    DSM83 owners. Fresh DSM83 API/PDF are readable; exact historical KOMODO83 and
    MediaList routes return 403, leaving the original mapping event unverified. The
    preserved catalogue snippet supports only the historical identity claim; no unrelated
    12% NaCl variant or organism growth claim is transferred.
  target_ids:
  - CultureMech:006636
  evidence_ids:
  - target
  - owner
  - owner-2
  - api83
  - dsm83
  - komodo83
  - komodoList
- assessment_id: representation
  area: representation
  topic: Classification and native structural diagnostics
  outcome: supported
  summary: Complex agar medium and existing pH metadata are retained; bacterial/fungal
    category labels are source classifications, not strain-growth evidence. No sterilization
    time/temperature or growth condition is invented from a generic medium title.
  target_ids:
  - CultureMech:006636
  evidence_ids:
  - target
  - owner
  - owner-2
  - dsm83
  - api83
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 27 current concentration fields are covered by 30 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:006636
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","quantity_field_count":27,"decisions":[{"quantity_id":"q1","label":"Sucrose","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 4-4","quote":"Sucrose                                    30.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\":
    108,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    87.6424,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"Sucrose","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 4-4","quote":"Sucrose                                    30.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\":
    108,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    87.6424,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Sucrose","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 4-4","quote":"Sucrose                                    30.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\":
    108,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    87.6424,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"NaNO3","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 5-5","quote":"NaNO3                                       3.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\":
    187,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    35.2962,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"NaNO3","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 5-5","quote":"NaNO3                                       3.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\":
    187,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    35.2962,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"NaNO3","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 5-5","quote":"NaNO3                                       3.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\":
    187,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    35.2962,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 6-6","quote":"K2HPO4                                      1.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.74132,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"K2HPO4","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 6-6","quote":"K2HPO4                                      1.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.74132,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"K2HPO4","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 6-6","quote":"K2HPO4                                      1.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.74132,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 7-7","quote":"MgSO4 x 7 H2O                               0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.02859,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 7-7","quote":"MgSO4 x 7 H2O                               0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.02859,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 7-7","quote":"MgSO4 x 7 H2O                               0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.02859,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 8-8","quote":"KCl                                         0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    6.70691,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"KCl","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 8-8","quote":"KCl                                         0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    6.70691,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"KCl","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 8-8","quote":"KCl                                         0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    6.70691,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 9-9","quote":"FeSO4 x 7 H2O                               0.01    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q17","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 9-9","quote":"FeSO4 x 7 H2O                               0.01    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q18","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 9-9","quote":"FeSO4 x 7 H2O                               0.01    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 10-10","quote":"Yeast extract                               2.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Yeast
    extract","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 10-10","quote":"Yeast extract                               2.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Yeast
    extract","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 10-10","quote":"Yeast extract                               2.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Peptone","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    generated field lacks the attached claim retained by its owners. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 11-11","quote":"Peptone                                     5.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\":
    1,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Peptone","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 11-11","quote":"Peptone                                     5.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\":
    1,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Peptone","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing owner literal claim and current whole API digest match. The API explicitly
    declares this main-recipe g_l, and the primary table has the matching mass input.
    This verifies the provider basis, not a separately measured final-medium volume
    or the inaccessible original KOMODO event.","source_stage":"DSM83 main recipe;
    conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 11-11","quote":"Peptone                                     5.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\":
    1,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    local20 G_PER_L and retained owner claim match current API g_l=20 and its historical
    whole-response digest, but the exact DSM83 PDF lists15 g agar in its batch table.
    Preserve both dated source versions and resolve the conflict before choosing a
    formulation; the PDF water input is not measured final volume.","source_stage":"DSM83
    main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 12-12","quote":"Agar                                       15.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Agar","local_fields":[{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    local20 G_PER_L and retained owner claim match current API g_l=20 and its historical
    whole-response digest, but the exact DSM83 PDF lists15 g agar in its batch table.
    Preserve both dated source versions and resolve the conflict before choosing a
    formulation; the PDF water input is not measured final volume.","source_stage":"DSM83
    main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 12-12","quote":"Agar                                       15.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Agar","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    local20 G_PER_L and retained owner claim match current API g_l=20 and its historical
    whole-response digest, but the exact DSM83 PDF lists15 g agar in its batch table.
    Preserve both dated source versions and resolve the conflict before choosing a
    formulation; the PDF water input is not measured final volume.","source_stage":"DSM83
    main recipe; conflicting agar versions retained","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 12-12","quote":"Agar                                       15.00    g","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Source
    water input","local_fields":[],"decision":"evidence_only","rationale":"Both sources
    list 1000 ml water as batch input. No target/owner solvent field exists; retain
    volume or preparation context rather than infer measured final volume or a mass
    concentration.","source_stage":"source-only solvent input","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 13-13","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"pH 7.3","local_fields":[{"path":"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml","field_path":"ph_value","stored":7.3},{"path":"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml","field_path":"ph_value","stored":7.3},{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"ph_value","stored":7.3}],"decision":"evidence_only","rationale":"All
    three values are unchanged and supported; no field-level pH claim is attached.
    The fungal owner already preserves the adjustment sentence.","source_stage":"main-recipe
    pH","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 15-15","quote":"Adjust pH to 7.3.","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.medium","quote":"{\n            \"id\":
    83,\n            \"name\": \"CZAPEK PEPTONE AGAR\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 7.3,\n            \"max_pH\": 7.3,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf\"\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"Retained fungal-owner pH instruction","local_fields":[{"path":"data/normalized_yaml/fungal/czapek_peptone_agar.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"ADJUST_PH","description":"Adjust
    pH to 7.3."}}],"decision":"evidence_only","rationale":"The exact adjustment sentence
    is present in this owner and absent from the generated and bacterial records;
    preserve it without inventing time or temperature.","source_stage":"preparation","sources":[{"evidence_id":"dsm83","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium83.pdf","raw_path":"REVIEW_WORK/batch068/source07-08-10/dsm83.raw","raw_sha256":"b578829e4008ff3bc7da33c8dcb4945aefb083453db0e46fe5fb42692348267d","text_sha256":"559cc2a1e9a81695e38818ba97ac9a78a53a14d35340b5ddfb4b91fdc9e6e187","accessed_at":"2026-10-28T13:11:52.583990Z","locator":"dsm83.txt
    lines 15-15","quote":"Adjust pH to 7.3.","quote_basis":"derivative text"},{"evidence_id":"api83","reference":"https://mediadive.dsmz.de/rest/medium/83","raw_path":"REVIEW_WORK/batch068/source07-08-10/api83.raw","raw_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","text_sha256":"24d56907f107106d9ffcd1c83e052a30549a6778a5086b9f7b884295afdb9f0c","accessed_at":"2026-10-28T13:11:52.226611Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.3.\"\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CZAPEK_PEPTONE_AGAR.yaml":null,"data/normalized_yaml/bacterial/czapek_peptone_agar.yaml":null,"data/normalized_yaml/fungal/czapek_peptone_agar.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: 'Each document has seven secondary links among nine ingredients: six CHEBI-backed
    secondary slots and one legacy nitrate slot. The 18 CHEBI-backed secondary slots
    have exact current label/ID correspondence; the three legacy slots have no current
    exact MIM row and are excluded from that label-agreement population. All 21 primary
    chemical slots resolve to seven fresh exact OLS objects; the printed magnesium
    and iron heptahydrates agree with those formulas. Peptone and yeast extract remain
    mixtures without invented compound groundings. Source agar quantity disagreement
    is separate from correct agar identity.'
  target_ids:
  - CultureMech:006636
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All 18 ingredient snippets retain exact current API digest matches; the
    catalogue claim does not because both current KOMODO routes return 403. The five
    complete historical reports and three selected parent objects remain derivative
    provenance; no original access timestamp is recovered merely from equal current
    bytes. Existing repairs are credited, while malformed embedded timestamps require
    append-only clarification.
  target_ids:
  - CultureMech:006636
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-006636-agar-source-conflict
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: DSM83 PDF and API disagree on agar
  description: The current API and both maintained records encode20 g/L agar, while
    the exact DSM83 PDF lists15 g in the batch table. Existing owner evidence authenticates
    the API value, including its unchanged raw digest, but does not resolve the conflicting
    primary version. Retain both captures and explicit source-version provenance;
    do not silently replace one value or certify a measured final volume.
  target_ids:
  - CultureMech:006636
  field_paths:
  - ingredients[8].concentration
  evidence_ids:
  - dsm83
  - api83
  - old-claims
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-006636-generated-provenance
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Generated record loses repaired evidence and preparation
  description: Both owners retain nine exact API ingredient claims; all 18 snippets
    and their current whole-response digests match, including the agar claim that
    remains scientifically conflicted. The generated record loses those claims/references
    and omits the fungal owner pH-adjustment instruction, although ph_value 7.3 is
    retained. The two owner notes/preparation fields differ, so current exact-formulation
    merging must respect those differences instead of assuming ingredient-only equivalence.
    Preserve existing repairs and regenerate with the current conservative merge behavior.
  target_ids:
  - CultureMech:006636
  field_paths:
  - ingredients
  - references
  - preparation_steps
  - curation_history
  evidence_ids:
  - target
  - owner
  - owner-2
  - old-claims
  - writer-formulation
  - writer-merger
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-006636-missing-input-water
  category: quantity
  severity: minor
  status: open
  certainty: confirmed
  title: Source solvent input is omitted
  description: Preserve the explicit distilled-water batch input in each applicable
    maintained source context as volume/preparation information. Current importer
    skips water rows; do not infer final-volume make-up or convert water to grams
    per litre.
  target_ids:
  - CultureMech:006636
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - dsm83
  - api83
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-006636-legacy-nitrate-link
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy nitrate secondary identifiers lack current snapshot correspondence
  description: Each document retains MediaIngredientMech:000171 on nitrate. The exact
    current 9077-row MIM snapshot has no matching legacy identifier; the ingredient
    primary CHEBI:63005 resolves to sodium nitrate and has current MIM membership.
    Preserve the old provenance while reconciling the secondary link against the exact
    current mapping. Absence from this snapshot is not an independently verified historical
    deprecation or wrong-primary-ID claim.
  target_ids:
  - CultureMech:006636
  field_paths:
  - ingredients[1].mediaingredientmech_term
  evidence_ids:
  - mim
  - mim-meta
  - chebi63005
  - writer-mim
  rule_id: review-yaml-record/grounding
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-006636-history-timestamp
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Embedded historical import timestamp is malformed
  description: The generated and bacterial-owner import timestamp ends in literal
    .fZ, and the later resolver timestamp omits a timezone. Keep the original history
    as evidence; append an accurately timed clarification if its provenance can be
    established, rather than fabricating the original instant or silently rewriting
    history. Audit the responsible historical writer before claiming a live formatting
    defect.
  target_ids:
  - CultureMech:006636
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - target
  - owner
  - history
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
actions:
- action_id: a1
  description: The current API and both maintained records encode20 g/L agar, while
    the exact DSM83 PDF lists15 g in the batch table. Existing owner evidence authenticates
    the API value, including its unchanged raw digest, but does not resolve the conflicting
    primary version. Retain both captures and explicit source-version provenance;
    do not silently replace one value or certify a measured final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
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
  description: Both owners retain nine exact API ingredient claims; all 18 snippets
    and their current whole-response digests match, including the agar claim that
    remains scientifically conflicted. The generated record loses those claims/references
    and omits the fungal owner pH-adjustment instruction, although ph_value 7.3 is
    retained. The two owner notes/preparation fields differ, so current exact-formulation
    merging must respect those differences instead of assuming ingredient-only equivalence.
    Preserve existing repairs and regenerate with the current conservative merge behavior.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
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
  description: Preserve the explicit distilled-water batch input in each applicable
    maintained source context as volume/preparation information. Current importer
    skips water rows; do not infer final-volume make-up or convert water to grams
    per litre.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: Each document retains MediaIngredientMech:000171 on nitrate. The exact
    current 9077-row MIM snapshot has no matching legacy identifier; the ingredient
    primary CHEBI:63005 resolves to sodium nitrate and has current MIM membership.
    Preserve the old provenance while reconciling the secondary link against the exact
    current mapping. Absence from this snapshot is not an independently verified historical
    deprecation or wrong-primary-ID claim.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: The generated and bacterial-owner import timestamp ends in literal
    .fZ, and the later resolver timestamp omits a timezone. Keep the original history
    as evidence; append an accurately timed clarification if its provenance can be
    established, rather than fabricating the original instant or silently rewriting
    history. Audit the responsible historical writer before claiming a live formatting
    defect.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/czapek_peptone_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/czapek_peptone_agar.yaml
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
- Review completion is partial because the exact KOMODO branch/catalogue cannot be
  freshly authenticated and the primary PDF/API agar discrepancy remains unresolved.
- The nearby CZAPEK12%NaCl record is a separate uninspected variant; none of its conditions
  or findings are transferred.
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
