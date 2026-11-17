# Scientific review: CALORAMATOR QUIMBAYENSIS MEDIUM

- Review: 20261028T061508Z-culturemech-000944-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:09:49.634622Z
- Finished UTC: 2026-10-28T06:15:08.745982Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM1477 identity and main preparation are retained. Two flattened stocks, calcium/sodium sums across different solution bases and two supplied-form identifiers require curation; every concentration and numeric preparation assertion is covered without guessed final volume.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch058 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000944 | data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml | generated | caloramator_quimbayensis_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:000944 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:000944 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:000944 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:000944 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSM1477 owner and target

identity: supported. Targets: CultureMech:000944.

Fresh PDF/API identify DSM1477. The target and its one maintained owner have identical scientific fields; merge metadata alone differs. No similarly numbered medium, organism growth or experimental optimization is inferred.

### Complex undefined liquid with retained preparation

representation: supported. Targets: CultureMech:000944.

The yeast extract makes this a complex, compositionally undefined liquid. Existing main pH and preparation are source-supported and credited, while trace-stock preparation needs a clear stock association.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:000944.

64 current concentration fields are covered by 42 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b058-quantity-inventory-v1","target":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","quantity_field_count":64,"decisions":[{"quantity_id":"q1","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 3-3","quote":"K2HPO4                                                   0.30         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\": 1.71896,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 4-4","quote":"KH2PO4                                                   0.30         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\": 2.2001,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 5-5","quote":"NH4Cl                                                    1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\": 18.6578,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.49701","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.49701","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 6-6","quote":"MgCl2 x 6 H2O                                            1.50         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49701,\n                        \"mmol_l\": 7.36342,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1998004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The encoded sum combines a provider main g/L value with the undiluted trace-stock g/L value. The units have the same dimensions but different solution bases, so this is invalid as a final-medium total. Restore the distinct main input and trace-stock component; do not calculate an unproved receiving dilution.","source_stage":"incompatible main and undiluted stock bases","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 7-7","quote":"CaCl2 x 2 H2O                                            0.10         g","quote_basis":"derivative text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 34-34","quote":"CaCl2 x 2 H2O                                            0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 0.678845,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"20.9601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"20.9601","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The encoded sum combines a provider main g/L value with the undiluted trace-stock g/L value. The units have the same dimensions but different solution bases, so this is invalid as a final-medium total. Restore the distinct main input and trace-stock component; do not calculate an unproved receiving dilution.","source_stage":"incompatible main and undiluted stock bases","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 8-8","quote":"NaCl                                                    20.00         g","quote_basis":"derivative text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 40-40","quote":"NaCl                                                     1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.9601,\n                        \"mmol_l\": 341.548,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 9-9","quote":"KCl                                                      0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 1.3387,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 11-11","quote":"Yeast extract                                            1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence. Preserve the separate 0.50 mL dose of 0.1% w/v sodium resazurin.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 12-12","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 13-13","quote":"NaHCO3                                                   0.50         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 5.94,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"D-Glucose","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.59281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.59281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares the existing g_l rate on its 1002 mL normalization basis; the primary supports the batch input. This is provider-specific rate evidence, not a measured-final-volume inference from 1000 mL water. Preserve that distinction and attach exact local evidence.","source_stage":"provider-declared main rate / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 14-14","quote":"D-Glucose                                                3.60         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 3.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.59281,\n                        \"mmol_l\": 19.9424,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"12.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"12.8","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 30-30","quote":"Nitrilotriacetic acid (NTA)                             12.80         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\": \"NTA\",\n                        \"amount\": 12.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 12.8,\n                        \"mmol_l\": 66.9666,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 31-31","quote":"FeCl2 x 4 H2O                                            1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.02988,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 32-32","quote":"MnCl2 x 4 H2O                                            0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 33-33","quote":"CoCl2 x 6 H2O                                            0.03         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231055,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 35-35","quote":"ZnCl2                                                    0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.733676,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"CuCl2","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 36-36","quote":"CuCl2                                                    0.02         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.148754,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 37-37","quote":"H3BO3                                                    0.01         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 38-38","quote":"Na2MoO4 x 2 H2O                                          0.03         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 39-39","quote":"NiCl2 x 6 H2O                                            0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.771611,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 41-41","quote":"Na2SeO3 x 5 H2O                                          0.03         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.04","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.04","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The trace stock explicitly makes up to 1000 mL, supporting its mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 42-42","quote":"Na2WO4 x 2 H2O                                           0.04         g","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.04,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\": 0.121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 60-60","quote":"Biotin                                                20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 61-61","quote":"Folic acid                                            20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 62-62","quote":"Pyridoxine hydrochloride                             100.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 63-63","quote":"Thiamine HCl                                          50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 64-64","quote":"Riboflavin                                            50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 65-65","quote":"Nicotinic acid                                        50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 66-66","quote":"Calcium D-(+)-pantothenate                            50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 67-67","quote":"Vitamin B12                                            1.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 68-68","quote":"p-Aminobenzoic acid                                   50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an undiluted stock component encoded as a direct main ingredient. Restore the separate stock and its receiving dose; the present number is not a final-medium concentration. The API explicitly declares stock g_l; the primary water input alone does not establish measured final volume. The 10x label does not supply an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 69-69","quote":"(DL)-alpha-Lipoic acid                                50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Receiving stock 7","local_fields":[],"decision":"evidence_only","rationale":"Preserve the printed 1 mL batch input and exact source stock. The main receiving denominator is not established by the stock makeup or the 10x name.","source_stage":"source-only receiving dose","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 10-10","quote":"Trace element solution                                   1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 589,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Receiving stock 12","local_fields":[],"decision":"evidence_only","rationale":"Preserve the printed 1 mL batch input and exact source stock. The main receiving denominator is not established by the stock makeup or the 10x name.","source_stage":"source-only receiving dose","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 15-15","quote":"Wolin's vitamin solution (10x)                           1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Water input, source solution 0","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact source solvent input. The trace stock separately has explicit final makeup; the main and vitamin water inputs do not justify assumed final-volume calculations.","source_stage":"source-only solvent","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 16-16","quote":"Distilled water                                       1000.00        ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Water input, source solution 1","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact source solvent input. The trace stock separately has explicit final makeup; the main and vitamin water inputs do not justify assumed final-volume calculations.","source_stage":"source-only solvent","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 43-43","quote":"Distilled water                                       1000.00        ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Water input, source solution 2","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact source solvent input. The trace stock separately has explicit final makeup; the main and vitamin water inputs do not justify assumed final-volume calculations.","source_stage":"source-only solvent","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 70-70","quote":"Distilled water                                     1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Sodium resazurin percentage and addition","local_fields":[],"decision":"evidence_only","rationale":"Both source stock strength and liquid input are explicit; keep them distinct from the provider-normalized solute rate.","source_stage":"source-only direct stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 12-12","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Retained complete-medium pH","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}}],"decision":"evidence_only","rationale":"The existing 7.0–7.2 range matches the complete-medium adjustment and is separate from trace-stock pH 6.5.","source_stage":"main pH","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 23-24","quote":"and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if\nnecessary.","quote_basis":"derivative text"}]},{"quantity_id":"q40","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve ingredients except bicarbonate, glucose and vitamins, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary."},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve ingredients except bicarbonate, glucose and vitamins, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary."}],"decision":"evidence_only","rationale":"Preserve all existing main preparation details, 100% nitrogen and separate 80/20 bicarbonate stock atmosphere, 30–45 minute sparging, selective filtration and pH stage. These are recipe instructions, not growth assertions.","source_stage":"main preparation","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 18-24","quote":"Dissolve ingredients except bicarbonate, glucose and vitamins, then sparge medium with\n100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the same gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose\nand vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under\n100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2\nand 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if\nnecessary.","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except bicarbonate, glucose and vitamins, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Trace-stock preparation","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"preparation_steps[1].description","stored":"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml."}],"decision":"correct","rationale":"The NTA dissolution in 200 mL, pH 6.5 with KOH, subsequent salts and final 1000 mL makeup are supported. Associate the instruction with the trace stock rather than an unscoped second main-medium step.","source_stage":"trace-stock preparation","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 45-45","quote":"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve","quote_basis":"derivative text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"KOH pH adjustment dose","local_fields":[],"decision":"not_quantified","rationale":"The source specifies KOH to reach the stock pH endpoint but no fixed amount. Do not infer a concentration or borrow another medium dose.","source_stage":"source-only variable adjustment","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 45-45","quote":"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve","quote_basis":"derivative text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:000944.

All asserted ontology slots and current MIM exact-key rows are joined. Nickel hexahydrate versus anhydrous CHEBI:34887 and sodium resazurin versus neutral CHEBI:8806 are confirmed mismatches; nickel has primary and secondary slots, resazurin only primary. Source-explicit calcium D-pantothenate is consistent with CHEBI:31345 stereochemistry. Lipoic-acid generic identity does not warrant narrowing the source DL wording to an R-only compound. Canonical labels are not concentration evidence.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:000944.

All four historical reports and current histories were read. Fresh API bytes equal the October source digest and all selected source objects; that authenticates content separately from original access timestamps. The September report inferred final-litre input water and underconcentration; those assumptions are not repeated. Current no-sum cleanup and stage-preserving importer are credited. There are no attached current quantity claims to mark verified.

## Findings

### f1: Two stocks are flattened into main ingredients

major / open / confirmed; issue key: culturemech-000944-flattened-stock-topology.

The target and its exact owner retain the same old flattening: twenty-one distinct stock-only rows are direct ingredients and two further stock components are absorbed into main sums. Restore trace-element and Wolin vitamin stocks with exact batch receiving doses, solvent inputs and stock preparation. Current primary-only importer already preserves stock references; do not describe it as still flattening every solution.

### f2: Calcium and sodium chloride combine different solution bases

major / open / confirmed; issue key: culturemech-000944-main-stock-sums.

The calcium value 0.1998004 g/L sums 0.0998004 main and 0.1 trace-stock g/L; sodium chloride 20.9601 sums 19.9601 main and 1 stock g/L. Same-dimensional numbers on different solution bases cannot be added as a final-medium total. Separate the exact source stages, retaining the primary 0.10 g and 20.00 g main inputs and independent stock rows. Current duplicate cleanup flags conflicting values instead of summing; this is an encoded historical defect, not evidence of current execution.

### f3: Nickel hydrate and sodium resazurin use different chemical forms

major / open / confirmed; issue key: culturemech-000944-supplied-form-identifiers.

The source and local names specify nickel chloride hexahydrate, whereas primary and secondary CHEBI:34887 denote anhydrous nickel dichloride. Fresh CHEBI:53542 independently identifies the hexahydrate candidate. Sodium resazurin has a primary CHEBI:8806 slot denoting neutral resazurin, with no sodium in its formula; there is no secondary resazurin slot to repair. Correct only the actual asserted slots and keep stock-stage work separate.

### f4: Source normalization and stock-dose evidence are incomplete

minor / open / confirmed; issue key: culturemech-000944-normalization-evidence.

Attach exact main and stock claims with their different bases. API main volume 1002 mL is a provider declaration, while the primary gives water input; neither authorizes replacing declared g_l rates by nominal-litre arithmetic. The trace stock has explicit final makeup; vitamins do not. Preserve percent basis and 10x wording without inferred receiving dilutions.

## Recommended Actions And Acceptance Checks

### a1

The target and its exact owner retain the same old flattening: twenty-one distinct stock-only rows are direct ingredients and two further stock components are absorbed into main sums. Restore trace-element and Wolin vitamin stocks with exact batch receiving doses, solvent inputs and stock preparation. Current primary-only importer already preserves stock references; do not describe it as still flattening every solution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The calcium value 0.1998004 g/L sums 0.0998004 main and 0.1 trace-stock g/L; sodium chloride 20.9601 sums 19.9601 main and 1 stock g/L. Same-dimensional numbers on different solution bases cannot be added as a final-medium total. Separate the exact source stages, retaining the primary 0.10 g and 20.00 g main inputs and independent stock rows. Current duplicate cleanup flags conflicting values instead of summing; this is an encoded historical defect, not evidence of current execution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source and local names specify nickel chloride hexahydrate, whereas primary and secondary CHEBI:34887 denote anhydrous nickel dichloride. Fresh CHEBI:53542 independently identifies the hexahydrate candidate. Sodium resazurin has a primary CHEBI:8806 slot denoting neutral resazurin, with no sodium in its formula; there is no secondary resazurin slot to repair. Correct only the actual asserted slots and keep stock-stage work separate.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Attach exact main and stock claims with their different bases. API main volume 1002 mL is a provider declaration, while the primary gives water input; neither authorizes replacing declared g_l rates by nominal-litre arithmetic. The trace stock has explicit final makeup; vitamins do not. Preserve percent basis and 10x wording without inferred receiving dilutions.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm1477 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf; REVIEW_WORK/batch058/source07-09/dsm1477.json; exact original raw/text/hash/time metadata | context_only | Exact primary medium and its printed stock/preparation subsections; named strain variations remain separate and do not establish generic growth. |
| api1477 | https://mediadive.dsmz.de/rest/medium/1477; REVIEW_WORK/batch058/source07-09/api1477.json; exact original raw/text/hash/time metadata | context_only | Exact current provider identity and declared amounts/basis; provider volume is not independently measured final volume. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch058/source07-09/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch058/source07-09/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch058/source07-09/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch058/source07-09/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch058/source07-09/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| target | data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-16 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/caloramator_quimbayensis_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caloramator_quimbayensis_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/yaml_record_review/20260922T025332Z-CALORAMATOR_QUIMBAYENSIS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit | context_only | Current parser reads only the primary recipe, separates referenced solutions and percentage/ml additions, and preserves their source attributes. It prefers explicit g_l but otherwise maps bare mass/volume units to per-litre schema units. This credits existing stage handling without certifying a source final volume or historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current duplicate cleanup collapses identical values but flags conflicting values without summing. Earlier sums require source-stage curation; do not rerun cleanup as a substitute for scientific reconciliation. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch058/source07-09/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch058/source07-09/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch058/source07-09/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch058/source07-09/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch058/source07-09/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch058/source07-09/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch058/source07-09/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch058/source07-09/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634; REVIEW_WORK/batch058/source07-09/chebi17634.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557; REVIEW_WORK/batch058/source07-09/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch058/source07-09/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch058/source07-09/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch058/source07-09/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch058/source07-09/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49553; REVIEW_WORK/batch058/source07-09/chebi49553.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch058/source07-09/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch058/source07-09/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; REVIEW_WORK/batch058/source07-09/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; REVIEW_WORK/batch058/source07-09/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch058/source07-09/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch058/source07-09/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch058/source07-09/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch058/source07-09/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch058/source07-09/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch058/source07-09/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch058/source07-09/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch058/source07-09/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| quantities | REVIEW_WORK/batch058/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch058/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch058/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch058/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch058/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch058/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch058/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch058/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch058/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch058/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch058/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Current canonical checks validate encoded structure/labels; zero reference checks do not verify external source claims.
- All primary PDF pages were read visually as well as in their complete extracted text. Current source status, retrieval times and complete raw/text bytes remain in the capture catalog.
- Provider mmol_l fields are retained as declarations, not endorsed calculations: cobalt/nickel values do not use the named hexahydrate formula masses. No molar correction or final-medium dilution is inferred.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T061508Z-culturemech-000944-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CALORAMATOR QUIMBAYENSIS MEDIUM'
started_at: '2026-10-28T06:09:49.634622Z'
finished_at: '2026-10-28T06:15:08.745982Z'
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
summary: DSM1477 identity and main preparation are retained. Two flattened stocks,
  calcium/sodium sums across different solution bases and two supplied-form identifiers
  require curation; every concentration and numeric preparation assertion is covered
  without guessed final volume.
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
  - path: data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
    sha256: cd1ab222e842b865f9977d4791360420af4652e827fc4fb948be8f26af2af31c
    role: target
  - path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
    sha256: bf9fc1e8e56211e1e6a3701e79e9b457d88671cb1b7b84c13f332f519bc5f685
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/caloramator_quimbayensis_medium.yaml.md
    sha256: 868bfb67ae800c7454eeb4e5d3f32517dbdd20580754fd741432de6767dece97
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.md
    sha256: f50caf6266b62fda8280076526a581df5e2d4c6243bdc655230bb60fae2db10f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caloramator_quimbayensis_medium.md
    sha256: 92ddda2f27fd20545b43385093a9e2b8fcb518929c9572beca6a7a2186791917
    role: context
  - path: reports/yaml_record_review/20260922T025332Z-CALORAMATOR_QUIMBAYENSIS_MEDIUM.md
    sha256: 2368e8c5a09c4ceb0a1b9cf67f56d8e18f81380de80d90f28e97d957cab151db
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
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
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Authoritative batch058 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000944
targets:
- target_id: CultureMech:000944
  path: data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
  label: caloramator_quimbayensis_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
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
  - CultureMech:000944
  command: just validate-schema data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
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
  - CultureMech:000944
  command: just validate-strict data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
    --out REVIEW_WORK/batch058/record08/strict.tsv --workers 1 --quiet
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
  - CultureMech:000944
  command: just validate-terms data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
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
  - CultureMech:000944
  command: just validate-references data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm1477
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf
  accessed_at: '2026-10-28T06:10:13.213373Z'
  locator: REVIEW_WORK/batch058/source07-09/dsm1477.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact primary medium and its printed stock/preparation subsections; named
    strain variations remain separate and do not establish generic growth.
  snapshot_sha256: d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5
- evidence_id: api1477
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1477
  accessed_at: '2026-10-28T06:10:13.046054Z'
  locator: REVIEW_WORK/batch058/source07-09/api1477.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current provider identity and declared amounts/basis; provider volume
    is not independently measured final volume.
  snapshot_sha256: 23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T06:10:16.490533Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T06:10:17.185279Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T06:10:18.847160Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T06:10:15.870210Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T06:10:14.549967Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T06:15:08.562041Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: cd1ab222e842b865f9977d4791360420af4652e827fc4fb948be8f26af2af31c
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T06:15:08.562196Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: bf9fc1e8e56211e1e6a3701e79e9b457d88671cb1b7b84c13f332f519bc5f685
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T06:15:08.562222Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T06:15:08.562550Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T06:15:08.562572Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T06:15:08.562593Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-16
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T06:15:08.562617Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/caloramator_quimbayensis_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T06:15:08.568295Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 868bfb67ae800c7454eeb4e5d3f32517dbdd20580754fd741432de6767dece97
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T06:15:08.568354Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f50caf6266b62fda8280076526a581df5e2d4c6243bdc655230bb60fae2db10f
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caloramator_quimbayensis_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T06:15:08.568384Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 92ddda2f27fd20545b43385093a9e2b8fcb518929c9572beca6a7a2186791917
- evidence_id: report-20
  kind: prior_review
  reference: reports/yaml_record_review/20260922T025332Z-CALORAMATOR_QUIMBAYENSIS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T06:15:08.568409Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2368e8c5a09c4ceb0a1b9cf67f56d8e18f81380de80d90f28e97d957cab151db
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit
  accessed_at: '2026-10-28T06:15:08.568433Z'
  support: context_only
  summary: Current parser reads only the primary recipe, separates referenced solutions
    and percentage/ml additions, and preserves their source attributes. It prefers
    explicit g_l but otherwise maps bare mass/volume units to per-litre schema units.
    This credits existing stage handling without certifying a source final volume
    or historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T06:15:08.568466Z'
  support: context_only
  summary: Current duplicate cleanup collapses identical values but flags conflicting
    values without summing. Earlier sums require source-stage curation; do not rerun
    cleanup as a substitute for scientific reconciliation.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T06:10:13.828292Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T06:10:17.662931Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T06:10:15.827429Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T06:10:18.389111Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T06:10:18.233627Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T06:10:15.215504Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T06:10:16.377374Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T06:10:15.959955Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634
  accessed_at: '2026-10-28T06:10:14.527215Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi17634.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 04060738e01fe33b9fc8e5bf54807590127ce391eb8a962d1d013002502169b2
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557
  accessed_at: '2026-10-28T06:10:16.589149Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi44557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 25e8fb689e4dfc294e2823ca36290cdce6d21ad174238e0e958ebe09d4c1262b
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T06:10:18.267374Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T06:10:18.396541Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T06:10:17.153627Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T06:10:17.045258Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi49553
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49553
  accessed_at: '2026-10-28T06:10:16.994321Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi49553.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 2d4660eb3bc066caef0e626b9b3bdf46ebaecdcf1779b4a75bfcd982f49bbc5b
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T06:10:16.436126Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T06:10:17.802299Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  accessed_at: '2026-10-28T06:10:13.825959Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi131361.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  accessed_at: '2026-10-28T06:10:17.660443Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T06:10:14.390430Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T06:10:15.256435Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T06:10:15.769055Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T06:10:17.061523Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T06:10:14.572075Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T06:10:14.077368Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T06:10:14.731572Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T06:10:15.715860Z'
  locator: REVIEW_WORK/batch058/source07-09/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744245Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: d28253309be3e0e010cd8913dafe9c9f8d9b50bb23bdf81c0a5c6959f159bbc8
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744332Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 67b58f00d07c31ee1fa67b1a19ad9b59e451983128b59defedf35d1879066d41
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744481Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: d8aa3572f66e32ab73ab2c538729787cf0166512db4423875f80b00161adc986
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744542Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: f4333046a47af7f1ba5ca1bc2891bc5d07989c7d6055065b6f5852baade05d2d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744597Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: db9a2db5f13d82c1f91decfbe4241c1671e009bf2f7cf2dabeff2315a2a79824
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744623Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: d145f3a8d01fc73d0889d51b457de3602e52bdefb506267a2f4f874309a8cef6
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch058/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T06:15:08.744644Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch058/record08/schema-result.json
  accessed_at: '2026-10-28T06:09:50.780624Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 36740ab1d0bc44fe1a6b6e5594d8dcf608e22d72e747608deeb072e50ed2266a
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch058/record08/strict-result.json
  accessed_at: '2026-10-28T06:09:51.778845Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 3ed4edb3362b51bda5b175a2db41a7e18e32211057a122f39d7cb5d06abc3927
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch058/record08/terms-result.json
  accessed_at: '2026-10-28T06:09:52.885247Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: bc2e92a51dad5138915ad4b39039f4cd7cd920a81f0c57612bd812744a3e9d64
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch058/record08/references-result.json
  accessed_at: '2026-10-28T06:09:53.685422Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: adcd4568ee64ba88ce26aec5c13fe113d874914e5298a57b596114b218201a65
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSM1477 owner and target
  outcome: supported
  summary: Fresh PDF/API identify DSM1477. The target and its one maintained owner
    have identical scientific fields; merge metadata alone differs. No similarly numbered
    medium, organism growth or experimental optimization is inferred.
  target_ids:
  - CultureMech:000944
  evidence_ids:
  - dsm1477
  - api1477
  - target
  - owner
- assessment_id: classification
  area: representation
  topic: Complex undefined liquid with retained preparation
  outcome: supported
  summary: The yeast extract makes this a complex, compositionally undefined liquid.
    Existing main pH and preparation are source-supported and credited, while trace-stock
    preparation needs a clear stock association.
  target_ids:
  - CultureMech:000944
  evidence_ids:
  - dsm1477
  - owner
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 64 current concentration fields are covered by 42 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:000944
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b058-quantity-inventory-v1","target":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","quantity_field_count":64,"decisions":[{"quantity_id":"q1","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 3-3","quote":"K2HPO4                                                   0.30         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\":
    1.71896,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.299401","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 4-4","quote":"KH2PO4                                                   0.30         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\":
    2.2001,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 5-5","quote":"NH4Cl                                                    1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\":
    18.6578,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.49701","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.49701","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 6-6","quote":"MgCl2 x 6 H2O                                            1.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49701,\n                        \"mmol_l\":
    7.36342,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1998004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    encoded sum combines a provider main g/L value with the undiluted trace-stock
    g/L value. The units have the same dimensions but different solution bases, so
    this is invalid as a final-medium total. Restore the distinct main input and trace-stock
    component; do not calculate an unproved receiving dilution.","source_stage":"incompatible
    main and undiluted stock bases","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 7-7","quote":"CaCl2 x 2 H2O                                            0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 34-34","quote":"CaCl2 x 2 H2O                                            0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    0.678845,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"20.9601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"20.9601","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    encoded sum combines a provider main g/L value with the undiluted trace-stock
    g/L value. The units have the same dimensions but different solution bases, so
    this is invalid as a final-medium total. Restore the distinct main input and trace-stock
    component; do not calculate an unproved receiving dilution.","source_stage":"incompatible
    main and undiluted stock bases","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 8-8","quote":"NaCl                                                    20.00         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 40-40","quote":"NaCl                                                     1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 19.9601,\n                        \"mmol_l\":
    341.548,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 9-9","quote":"KCl                                                      0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    1.3387,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 11-11","quote":"Yeast extract                                            1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence. Preserve the separate 0.50 mL dose of 0.1% w/v
    sodium resazurin.","source_stage":"provider-declared main rate / primary batch
    input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 12-12","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 13-13","quote":"NaHCO3                                                   0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    5.94,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"D-Glucose","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.59281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.59281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares the existing g_l rate on its 1002 mL normalization basis;
    the primary supports the batch input. This is provider-specific rate evidence,
    not a measured-final-volume inference from 1000 mL water. Preserve that distinction
    and attach exact local evidence.","source_stage":"provider-declared main rate
    / primary batch input","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 14-14","quote":"D-Glucose                                                3.60         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\":
    211,\n                        \"amount\": 3.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.59281,\n                        \"mmol_l\":
    19.9424,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"12.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"12.8","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 30-30","quote":"Nitrilotriacetic acid (NTA)                             12.80         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"attribute\": \"NTA\",\n                        \"amount\":
    12.8,\n                        \"unit\": \"g\",\n                        \"g_l\":
    12.8,\n                        \"mmol_l\": 66.9666,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 31-31","quote":"FeCl2 x 4 H2O                                            1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.02988,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 32-32","quote":"MnCl2 x 4 H2O                                            0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 33-33","quote":"CoCl2 x 6 H2O                                            0.03         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231055,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 35-35","quote":"ZnCl2                                                    0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.733676,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"CuCl2","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 36-36","quote":"CuCl2                                                    0.02         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2\",\n                        \"compound_id\":
    261,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.148754,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 37-37","quote":"H3BO3                                                    0.01         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 38-38","quote":"Na2MoO4 x 2 H2O                                          0.03         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.123993,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 39-39","quote":"NiCl2 x 6 H2O                                            0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.771611,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Na2SeO3
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 41-41","quote":"Na2SeO3 x 5 H2O                                          0.03         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Na2WO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.04","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.04","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The trace stock explicitly makes up to 1000 mL, supporting its
    mass-to-stock-g/L normalization.","source_stage":"trace-element stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 42-42","quote":"Na2WO4 x 2 H2O                                           0.04         g","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.04,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\":
    0.121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 60-60","quote":"Biotin                                                20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 61-61","quote":"Folic acid                                            20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 62-62","quote":"Pyridoxine hydrochloride                             100.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 63-63","quote":"Thiamine HCl                                          50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 64-64","quote":"Riboflavin                                            50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 65-65","quote":"Nicotinic acid                                        50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 66-66","quote":"Calcium D-(+)-pantothenate                            50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 67-67","quote":"Vitamin B12                                            1.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 68-68","quote":"p-Aminobenzoic acid                                   50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an undiluted stock component encoded as a direct main ingredient. Restore the
    separate stock and its receiving dose; the present number is not a final-medium
    concentration. The API explicitly declares stock g_l; the primary water input
    alone does not establish measured final volume. The 10x label does not supply
    an independent working dose.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 69-69","quote":"(DL)-alpha-Lipoic acid                                50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"Receiving stock 7","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the printed 1 mL batch input and exact source stock. The main receiving denominator
    is not established by the stock makeup or the 10x name.","source_stage":"source-only
    receiving dose","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 10-10","quote":"Trace element solution                                   1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\":
    589,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q34","label":"Receiving stock 12","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the printed 1 mL batch input and exact source stock. The main receiving denominator
    is not established by the stock makeup or the 10x name.","source_stage":"source-only
    receiving dose","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 15-15","quote":"Wolin''s vitamin solution (10x)                           1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q35","label":"Water input, source solution 0","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact source solvent input. The trace stock separately has explicit final
    makeup; the main and vitamin water inputs do not justify assumed final-volume
    calculations.","source_stage":"source-only solvent","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 16-16","quote":"Distilled water                                       1000.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q36","label":"Water input, source solution 1","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact source solvent input. The trace stock separately has explicit final
    makeup; the main and vitamin water inputs do not justify assumed final-volume
    calculations.","source_stage":"source-only solvent","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 43-43","quote":"Distilled water                                       1000.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q37","label":"Water input, source solution 2","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact source solvent input. The trace stock separately has explicit final
    makeup; the main and vitamin water inputs do not justify assumed final-volume
    calculations.","source_stage":"source-only solvent","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 70-70","quote":"Distilled water                                     1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q38","label":"Sodium resazurin percentage and addition","local_fields":[],"decision":"evidence_only","rationale":"Both
    source stock strength and liquid input are explicit; keep them distinct from the
    provider-normalized solute rate.","source_stage":"source-only direct stock","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 12-12","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Retained
    complete-medium pH","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}}],"decision":"evidence_only","rationale":"The
    existing 7.0–7.2 range matches the complete-medium adjustment and is separate
    from trace-stock pH 6.5.","source_stage":"main pH","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 23-24","quote":"and 20% CO2 gas mixture. Prior to use adjust pH of complete
    medium to 7.0 - 7.2, if\nnecessary.","quote_basis":"derivative text"}]},{"quantity_id":"q40","label":"Retained
    main preparation","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve
    ingredients except bicarbonate, glucose and vitamins, then sparge medium with
    100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add
    glucose and vitamins (sterilized by filtration) from sterile anoxic stock solutions
    prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete
    medium to 7.0 - 7.2, if necessary."},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve
    ingredients except bicarbonate, glucose and vitamins, then sparge medium with
    100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add
    glucose and vitamins (sterilized by filtration) from sterile anoxic stock solutions
    prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete
    medium to 7.0 - 7.2, if necessary."}],"decision":"evidence_only","rationale":"Preserve
    all existing main preparation details, 100% nitrogen and separate 80/20 bicarbonate
    stock atmosphere, 30–45 minute sparging, selective filtration and pH stage. These
    are recipe instructions, not growth assertions.","source_stage":"main preparation","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 18-24","quote":"Dissolve ingredients except bicarbonate, glucose and vitamins,
    then sparge medium with\n100% N2 gas for 30 - 45 min to make it anoxic. Dispense
    medium under the same gas\natmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add glucose\nand vitamins (sterilized by filtration) from
    sterile anoxic stock solutions prepared under\n100% N2 gas and bicarbonate from
    a sterile anoxic stock solution prepared under 80% N2\nand 20% CO2 gas mixture.
    Prior to use adjust pH of complete medium to 7.0 - 7.2, if\nnecessary.","quote_basis":"derivative
    text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except bicarbonate, glucose and vitamins, then sparge medium
    with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under the
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add glucose and vitamins (sterilized by filtration) from sterile anoxic stock
    solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock
    solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH
    of complete medium to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"Trace-stock preparation","local_fields":[{"path":"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"First
    dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then
    dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00
    ml."},{"path":"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml","field_path":"preparation_steps[1].description","stored":"First
    dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then
    dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00
    ml."}],"decision":"correct","rationale":"The NTA dissolution in 200 mL, pH 6.5
    with KOH, subsequent salts and final 1000 mL makeup are supported. Associate the
    instruction with the trace stock rather than an unscoped second main-medium step.","source_stage":"trace-stock
    preparation","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 45-45","quote":"First dissolve NTA in 200 ml of distilled water and adjust
    pH to 6.5 with KOH, then dissolve","quote_basis":"derivative text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api1477","reference":"https://mediadive.dsmz.de/rest/medium/1477","raw_path":"REVIEW_WORK/batch058/source07-09/api1477.raw","raw_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","text_sha256":"23fbb0acd66e8ec253e1a1214d75f0c0249ef8e686479c829784adc107b764e2","accessed_at":"2026-10-28T06:10:13.046054Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH,
    then dissolve mineral salts. Finally adjust pH to 6.5 with KOH and make up to
    1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"KOH
    pH adjustment dose","local_fields":[],"decision":"not_quantified","rationale":"The
    source specifies KOH to reach the stock pH endpoint but no fixed amount. Do not
    infer a concentration or borrow another medium dose.","source_stage":"source-only
    variable adjustment","sources":[{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 45-45","quote":"First dissolve NTA in 200 ml of distilled water and adjust
    pH to 6.5 with KOH, then dissolve","quote_basis":"derivative text"},{"evidence_id":"dsm1477","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1477.pdf","raw_path":"REVIEW_WORK/batch058/source07-09/dsm1477.raw","raw_sha256":"d17bd77a17d5a124a7b85e9f8ee0c759c62846c6416a11b4991546d7669a97a5","text_sha256":"eefa63c0231509a0610a6fd87c89a705d6879a5cf9237abd6c29aed2eeee56ce","accessed_at":"2026-10-28T06:10:13.213373Z","locator":"dsm1477.txt
    lines 55-55","quote":"mineral salts. Finally adjust pH to 6.5 with KOH and make
    up to 1000.00 ml.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted ontology slots and current MIM exact-key rows are joined.
    Nickel hexahydrate versus anhydrous CHEBI:34887 and sodium resazurin versus neutral
    CHEBI:8806 are confirmed mismatches; nickel has primary and secondary slots, resazurin
    only primary. Source-explicit calcium D-pantothenate is consistent with CHEBI:31345
    stereochemistry. Lipoic-acid generic identity does not warrant narrowing the source
    DL wording to an R-only compound. Canonical labels are not concentration evidence.
  target_ids:
  - CultureMech:000944
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All four historical reports and current histories were read. Fresh API
    bytes equal the October source digest and all selected source objects; that authenticates
    content separately from original access timestamps. The September report inferred
    final-litre input water and underconcentration; those assumptions are not repeated.
    Current no-sum cleanup and stage-preserving importer are credited. There are no
    attached current quantity claims to mark verified.
  target_ids:
  - CultureMech:000944
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-000944-flattened-stock-topology
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Two stocks are flattened into main ingredients
  description: 'The target and its exact owner retain the same old flattening: twenty-one
    distinct stock-only rows are direct ingredients and two further stock components
    are absorbed into main sums. Restore trace-element and Wolin vitamin stocks with
    exact batch receiving doses, solvent inputs and stock preparation. Current primary-only
    importer already preserves stock references; do not describe it as still flattening
    every solution.'
  target_ids:
  - CultureMech:000944
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[1]
  evidence_ids:
  - dsm1477
  - api1477
  - writer-mediadive
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-000944-main-stock-sums
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Calcium and sodium chloride combine different solution bases
  description: The calcium value 0.1998004 g/L sums 0.0998004 main and 0.1 trace-stock
    g/L; sodium chloride 20.9601 sums 19.9601 main and 1 stock g/L. Same-dimensional
    numbers on different solution bases cannot be added as a final-medium total. Separate
    the exact source stages, retaining the primary 0.10 g and 20.00 g main inputs
    and independent stock rows. Current duplicate cleanup flags conflicting values
    instead of summing; this is an encoded historical defect, not evidence of current
    execution.
  target_ids:
  - CultureMech:000944
  field_paths:
  - ingredients[4].concentration
  - ingredients[4].notes
  - ingredients[5].concentration
  - ingredients[5].notes
  evidence_ids:
  - dsm1477
  - api1477
  - writer-cleanup
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-000944-supplied-form-identifiers
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin use different chemical forms
  description: The source and local names specify nickel chloride hexahydrate, whereas
    primary and secondary CHEBI:34887 denote anhydrous nickel dichloride. Fresh CHEBI:53542
    independently identifies the hexahydrate candidate. Sodium resazurin has a primary
    CHEBI:8806 slot denoting neutral resazurin, with no sodium in its formula; there
    is no secondary resazurin slot to repair. Correct only the actual asserted slots
    and keep stock-stage work separate.
  target_ids:
  - CultureMech:000944
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  - ingredients[8].term
  evidence_ids:
  - dsm1477
  - api1477
  - chebi34887
  - chebi53542
  - chebi8806
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-000944-normalization-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source normalization and stock-dose evidence are incomplete
  description: Attach exact main and stock claims with their different bases. API
    main volume 1002 mL is a provider declaration, while the primary gives water input;
    neither authorizes replacing declared g_l rates by nominal-litre arithmetic. The
    trace stock has explicit final makeup; vitamins do not. Preserve percent basis
    and 10x wording without inferred receiving dilutions.
  target_ids:
  - CultureMech:000944
  field_paths:
  - ingredients
  - solutions
  - references
  evidence_ids:
  - dsm1477
  - api1477
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: 'The target and its exact owner retain the same old flattening: twenty-one
    distinct stock-only rows are direct ingredients and two further stock components
    are absorbed into main sums. Restore trace-element and Wolin vitamin stocks with
    exact batch receiving doses, solvent inputs and stock preparation. Current primary-only
    importer already preserves stock references; do not describe it as still flattening
    every solution.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000944
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
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
  description: The calcium value 0.1998004 g/L sums 0.0998004 main and 0.1 trace-stock
    g/L; sodium chloride 20.9601 sums 19.9601 main and 1 stock g/L. Same-dimensional
    numbers on different solution bases cannot be added as a final-medium total. Separate
    the exact source stages, retaining the primary 0.10 g and 20.00 g main inputs
    and independent stock rows. Current duplicate cleanup flags conflicting values
    instead of summing; this is an encoded historical defect, not evidence of current
    execution.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000944
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
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
  description: The source and local names specify nickel chloride hexahydrate, whereas
    primary and secondary CHEBI:34887 denote anhydrous nickel dichloride. Fresh CHEBI:53542
    independently identifies the hexahydrate candidate. Sodium resazurin has a primary
    CHEBI:8806 slot denoting neutral resazurin, with no sodium in its formula; there
    is no secondary resazurin slot to repair. Correct only the actual asserted slots
    and keep stock-stage work separate.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000944
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
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
  description: Attach exact main and stock claims with their different bases. API
    main volume 1002 mL is a provider declaration, while the primary gives water input;
    neither authorizes replacing declared g_l rates by nominal-litre arithmetic. The
    trace stock has explicit final makeup; vitamins do not. Preserve percent basis
    and 10x wording without inferred receiving dilutions.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000944
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml
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
- Current canonical checks validate encoded structure/labels; zero reference checks
  do not verify external source claims.
- All primary PDF pages were read visually as well as in their complete extracted
  text. Current source status, retrieval times and complete raw/text bytes remain
  in the capture catalog.
- 'Provider mmol_l fields are retained as declarations, not endorsed calculations:
  cobalt/nickel values do not use the named hexahydrate formula masses. No molar correction
  or final-medium dilution is inferred.'
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
