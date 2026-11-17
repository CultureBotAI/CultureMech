# Scientific review: CYTOPHAGA HUTCHINSONII medium

- Review: 20261028T132652Z-culturemech-004185-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:34.750569Z
- Finished UTC: 2026-10-28T13:26:52.250281Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The existing main rates and supplied forms are supported by exact provider evidence, including six already-authenticated owner claims. Preserve that credit. Curate the source alternatives and missing preparation/solvent context, separate the overbroad autoclave code, and regenerate without losing evidence. The inaccessible current KOMODO mapping and historical event syntax remain bounded provenance limitations.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch068 index 03
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004185 | data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml | generated | cytophaga_hutchinsonii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:004185 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:004185 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:004185 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:004185 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and maintained-owner identity

identity: concern. Targets: CultureMech:004185.

DSM160 explicitly incorporates medium67; the exact source and DSM1761 catalog identity are consistent. Two selected maintained contributors resolve, but the current KOMODO catalogue is inaccessible. The September TOGO M2337 review concerns CultureMech008924 and a different generated target; its water and state findings are not transferred here.

### Conditional physical state and complex components

representation: supported. Targets: CultureMech:004185.

Complex/undefined bacterial classification and an agarized branch are source-consistent. Casitone and yeast extract remain complex named materials without mandatory ChEBI identities. Existing conditional notes are credited; no organism growth or anaerobic requirement is inferred from the name or stale catalogue flag.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:004185.

15 current concentration fields are covered by 16 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","quantity_field_count":15,"decisions":[{"quantity_id":"q1","label":"Generated Casitone","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact provider explicitly declares this main-medium g_l rate; the primary67 table independently supports the batch mass and supplied form. Its 1000 mL water is not an explicit final-volume instruction. Retain the existing provider-basis rate and restore exact attached evidence; no numerical replacement or measured-volume claim is made.","source_stage":"Provider-declared main-medium rate, primary batch mass","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Maintained Casitone","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"verified","rationale":"Both maintained owners already attach the exact matching API ingredient object and the current response is byte-identical to their cited digest. This verifies the named provider-declared rate and source form. It does not independently recover the original access event, establish measured final volume, authenticate the old KOMODO mapping response, or validate unused API mmol_l conversions.","source_stage":"Existing attached provider concentration evidence","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Generated CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.36","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact provider explicitly declares this main-medium g_l rate; the primary67 table independently supports the batch mass and supplied form. Its 1000 mL water is not an explicit final-volume instruction. Retain the existing provider-basis rate and restore exact attached evidence; no numerical replacement or measured-volume claim is made.","source_stage":"Provider-declared main-medium rate, primary batch mass","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.36,\n                        \"mmol_l\": 9.25076,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Maintained CaCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.36","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.36","unit":"G_PER_L"}}],"decision":"verified","rationale":"Both maintained owners already attach the exact matching API ingredient object and the current response is byte-identical to their cited digest. This verifies the named provider-declared rate and source form. It does not independently recover the original access event, establish measured final volume, authenticate the old KOMODO mapping response, or validate unused API mmol_l conversions.","source_stage":"Existing attached provider concentration evidence","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.36,\n                        \"mmol_l\": 9.25076,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Generated Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact provider explicitly declares this main-medium g_l rate; the primary67 table independently supports the batch mass and supplied form. Its 1000 mL water is not an explicit final-volume instruction. Retain the existing provider-basis rate and restore exact attached evidence; no numerical replacement or measured-volume claim is made.","source_stage":"Provider-declared main-medium rate, primary batch mass","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Maintained Yeast extract","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"Both maintained owners already attach the exact matching API ingredient object and the current response is byte-identical to their cited digest. This verifies the named provider-declared rate and source form. It does not independently recover the original access event, establish measured final volume, authenticate the old KOMODO mapping response, or validate unused API mmol_l conversions.","source_stage":"Existing attached provider concentration evidence","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Agar conditional amount","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary67 table supplies 15 g agar and the API explicitly supplies g_l=15 with condition alternative. The current amount is supported on the provider basis for an agarized branch; it is excluded from the agar-free tube branch. Existing alternative notes are retained. Attach exact conditional evidence, without asserting that every source alternative is solid.","source_stage":"Agarized branch only","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"alternative\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Cellobiose conditional amount","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The API explicitly declares g_l=5 for its alternative cellobiose row; the current 5 G_PER_L is supported on that declared provider basis. The primary gives bare 0.5% with filter sterilization but does not state a percent denominator, so no independent w/v conversion or measured final-volume result is claimed. This addition belongs to the cellobiose alternative and is not required in either filter-paper alternative.","source_stage":"Cellobiose alternative; provider-declared normalization","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\": 214,\n                        \"condition\": \"alternative\",\n                        \"attribute\": \"filter-sterilized\",\n                        \"amount\": 0.5,\n                        \"unit\": \"%\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 14.6071,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"pH","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"All existing pH7.2 values agree with the explicitly incorporated primary67 instruction and API160. Preserve the values and link root evidence.","source_stage":"Inherited base-medium pH","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Adjust pH to 7.2.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Physical state","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"physical_state","stored":"SOLID_AGAR"},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"physical_state","stored":"SOLID_AGAR"},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"physical_state","stored":"SOLID_AGAR"}],"decision":"evidence_only","rationale":"SOLID_AGAR is consistent with the agarized source branch and current agar amount, so it is not automatically wrong. The same label cannot describe the explicitly agar-free tube branch. Keep the chosen formulation clear rather than converting every source alternative to one universal state.","source_stage":"Conditional agarized interpretation","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"DSM pH preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"ADJUST_PH","description":"Adjust pH to 7.2."}}],"decision":"evidence_only","rationale":"The existing ADJUST_PH description agrees exactly with the source. Generated and KOMODO copies omit this structured preparation; the pH scalar alone does not replace complete preparation context.","source_stage":"Existing supported preparation","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Adjust pH to 7.2.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"DSM alternative preparation text","local_fields":[{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"preparation_steps[1].description","stored":"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on the surface of agarized medium."}],"decision":"evidence_only","rationale":"The existing description preserves the provider alternative text, including cellobiose, agar-free portions, filter-paper length and the separate surface-paper alternative. Credit the complete literal text while assessing its single action code separately.","source_stage":"Alternative-specific preparation prose","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on the surface of agarized medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"DSM combined action code","local_fields":[{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"preparation_steps[1].action","stored":"AUTOCLAVE"}],"decision":"conflict","rationale":"AUTOCLAVE applies to the described agar-free filter-paper tube branch, not to the entire combined sentence or the filter-sterilized cellobiose addition. The current classifier tests autoclave/steam before filter and returns one code for the mixed sentence; this explains a present writer limitation without proving historical execution. Split/qualify actions by their source alternative.","source_stage":"Action scope, not a changed amount","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on the surface of agarized medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Source-only water","local_fields":[],"decision":"evidence_only","rationale":"Primary67 explicitly lists 1000 mL distilled water and API160 retains it as solvent. All three local ingredient lists omit it. Retain it as source input water; do not call it measured final volume or infer a new solute rate from it.","source_stage":"Source-only solvent input","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2 x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Source-only tube portion and paper","local_fields":[],"decision":"evidence_only","rationale":"The primary explicitly supplies 5 mL portions and 7 cm paper in the agar-free branch. These are a per-tube portion and length, not concentrations. The other paper-on-agar branch gives no piece dimensions; no missing paper mass or incubation conditions are invented.","source_stage":"Alternative-specific portion and length","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on the surface of agarized medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Source-only sterilization limits","local_fields":[],"decision":"not_quantified","rationale":"The primary says filter-sterilized for cellobiose, autoclave for the paper-tube branch and sterile paper pieces for the surface branch. It gives no temperature, duration, filter pore size or sterilization cycle. Keep these fields unresolved rather than transferring a routine default.","source_stage":"Unquantified source conditions","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1. To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium 67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe surface of agarized medium 67.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml":null,"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:004185.

All three asserted chemical IDs and canonical labels agree with current OLS: calcium chloride dihydrate (CHEBI:86158), agar (CHEBI:2509) and cellobiose (CHEBI:17057). Both primary and secondary slots preserve these forms. Current MIM preferred rows agree; optional Casitone and yeast candidate identifiers are inventory leads, not new asserted groundings or certified brand equivalents. Provider media IDs are identity identifiers, not missing MIM chemicals.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:004185.

All six included reports were read in exact scope. Sixteen historical API objects and the cited API160 digest authenticate against current raw bytes, including six attached maintained claims. The September report reviews the distinct TOGO M2337 target and its repaired liquid interpretation; its assumptions and recommended sibling collapse are not adopted. Current conservative formulation equality detects preparation differences; the old merge event is not proof that the current writer permits them.

## Findings

### f1: The generated record omits the source alternative preparation

major / open / confirmed; issue key: culturemech-004185-conditional-preparation-scope.

Restore the explicitly scoped DSM160/67 preparation and solvent context through maintained-input curation and conservative regeneration. The DSM owner retains the literal multi-alternative instruction, but its single AUTOCLAVE code overgeneralizes the paper-tube branch to the combined sentence. Represent the cellobiose and filter-paper alternatives separately, preserve the current conditional agar/cellobiose notes, and retain SOLID_AGAR only for a chosen agarized branch. Do not invent percent basis, final makeup, paper mass or sterilization settings.

### f2: Six supported owner claims are missing from the generated target

minor / open / confirmed; issue key: culturemech-004185-attached-evidence-generation.

Preserve the six exact attached API claims on the first three ingredients across both maintained owners and carry them into a compatible regenerated target. Add exact conditional evidence for agar and cellobiose and root evidence for preparation/water. Current API bytes authenticate the quoted provider rates; the primary water table does not independently establish final volume. Do not substitute a TOGO sibling or discard existing supported claims.

### f3: Historical mapping and event syntax remain bounded provenance gaps

minor / open / confirmed; issue key: culturemech-004185-event-and-mapping-provenance.

Retain the old KOMODO mapping excerpt and the malformed/naive original events byte-for-byte. Current exact KOMODO media-list and accession routes return 403, so the historical mapping retrieval and inherited Aerobic: No flag are not freshly authenticated. Append only verified corrective context if authoritative original provenance is recovered; do not overwrite original timestamps, infer anaerobic requirements or replay old commands.

## Recommended Actions And Acceptance Checks

### a1

Restore the explicitly scoped DSM160/67 preparation and solvent context through maintained-input curation and conservative regeneration. The DSM owner retains the literal multi-alternative instruction, but its single AUTOCLAVE code overgeneralizes the paper-tube branch to the combined sentence. Represent the cellobiose and filter-paper alternatives separately, preserve the current conditional agar/cellobiose notes, and retain SOLID_AGAR only for a chosen agarized branch. Do not invent percent basis, final makeup, paper mass or sterilization settings.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Preserve the six exact attached API claims on the first three ingredients across both maintained owners and carry them into a compatible regenerated target. Add exact conditional evidence for agar and cellobiose and root evidence for preparation/water. Current API bytes authenticate the quoted provider rates; the primary water table does not independently establish final volume. Do not substitute a TOGO sibling or discard existing supported claims.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Retain the old KOMODO mapping excerpt and the malformed/naive original events byte-for-byte. Current exact KOMODO media-list and accession routes return 403, so the historical mapping retrieval and inherited Aerobic: No flag are not freshly authenticated. Append only verified corrective context if authoritative original provenance is recovered; do not overwrite original timestamps, infer anaerobic requirements or replay old commands.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm160 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf; REVIEW_WORK/batch068/source01-03/dsm160.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| dsm67 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf; REVIEW_WORK/batch068/source01-03-supplement/dsm67.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| api160 | https://mediadive.dsmz.de/rest/medium/160; REVIEW_WORK/batch068/source01-03/api160.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| api67 | https://mediadive.dsmz.de/rest/medium/67; REVIEW_WORK/batch068/source01-03-supplement/api67.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| komodo160 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=160; REVIEW_WORK/batch068/source01-03/komodo160.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch068/source01-03/komodoList.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| identityDSM1761 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-1761; REVIEW_WORK/batch068/source01-03/identityDSM1761.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| target | data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/cytophaga_hutchinsonii_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/yaml_record_review/20260922T130359Z-cytophaga_hutchinsonii_medium__b6268d2c.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch068/record03/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch068/record03/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch068/record03/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser keeps only primary compounds and separately preserves referenced stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v enums without independently establishing the basis; the action classifier tests temperature before cool. Current behavior is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| history-auth | REVIEW_WORK/batch068/record03/historical-source-authentication.json; Complete artifact | supports | Six included historical reports were read in their exact headers. Sixteen historical source objects and the current API160 digest match the original cited raw bytes; the September TOGO sibling report is comparison context, not this target. |
| internal-links | REVIEW_WORK/batch068/record03/internal-reference-identity.json; Complete artifact | supports | Exact parent/child paths and IDs resolve; correspondence does not authorize transfer of a sibling variant or prove a current KOMODO table retrieval. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients, solutions and selected metadata but not preparation_steps; the maintained history records a DSM160 copy. Current code behavior is not authenticated historical execution. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; REVIEW_WORK/batch068/source01-03/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; REVIEW_WORK/batch068/source01-03/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17057; REVIEW_WORK/batch068/source01-03/chebi17057.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| quantities | REVIEW_WORK/batch068/record03/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch068/record03/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch068/record03/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch068/record03/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch068/record03/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch068/record03/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch068/record03/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch068/record03/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch068/record03/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch068/record03/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch068/record03/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Current exact KOMODO accession160 and media-list requests returned 403; the earlier mapping response hash remains an unrecovered historical observation. This identity branch makes the review partial.
- DSM160 and67 primary PDFs and both complete single-page visuals were read. DSM67 specifies input water, not final-volume makeup; DSM160 gives bare 0.5% without a mass/volume basis. Explicit API g_l values are preserved as provider-declared rates only.
- No independent validation is claimed for unused API mmol_l conversions, original retrieval timing, or the old Aerobic: No flag. No growth-condition or strain-performance inference is made.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T132652Z-culturemech-004185-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CYTOPHAGA HUTCHINSONII medium'
started_at: '2026-10-28T13:11:34.750569Z'
finished_at: '2026-10-28T13:26:52.250281Z'
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
summary: The existing main rates and supplied forms are supported by exact provider
  evidence, including six already-authenticated owner claims. Preserve that credit.
  Curate the source alternatives and missing preparation/solvent context, separate
  the overbroad autoclave code, and regenerate without losing evidence. The inaccessible
  current KOMODO mapping and historical event syntax remain bounded provenance limitations.
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
  - path: data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
    sha256: 31e047243e1d186eae85eab5ed3c63f2668976609e33ed3d649fc6735d81344b
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    sha256: e7777311c852c9ae4f263077012e8081c47d66286036a8913e44ebf1406051c6
    role: context
  - path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
    sha256: bcc04c2b48972dcd505a17acf0f85e85351b2949eaa3fa2e54a0f842c9268ab7
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/archive/media_variant_isp_cys_pfennig_methylobacterium_review.md
    sha256: ecbbbc5604eb39c8765827eccc3da4e6421cf3cfa91dfbaff72a146080f4dc77
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
    sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml.md
    sha256: d66cc6bf0cd5627ed5b97af2ce3d74e33b8f1f0226386b4cb46560b095078d8d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/cytophaga_hutchinsonii_medium.yaml.md
    sha256: f4a9438983fb56cf57d1494c6fe7519a0a4f6bd4f83b93c88d1e2ec1c33d3421
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.md
    sha256: 3237ce966605caaad4ccc733603724b2e10b1cd5bd2acf9b4f9afc43f5f2eb54
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.md
    sha256: e937e69e4000beb4081f552624fbc60af0bf84e6210decb99ad282e15085fd8c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.md
    sha256: 4e8bff299da7311b9956813bdbbf5f3024732da0a8e3f827b5eb14c796176b08
    role: context
  - path: reports/yaml_record_review/20260922T130359Z-cytophaga_hutchinsonii_medium__b6268d2c.md
    sha256: 027890942171344bd72e3926cc5db07b1d38563f0b67ea966b1bd0cd3ade6c46
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  selection: Authoritative batch068 index 03
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004185
targets:
- target_id: CultureMech:004185
  path: data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
  label: cytophaga_hutchinsonii_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:004185
  command: just validate-schema data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
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
  - CultureMech:004185
  command: just validate-strict data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
    --out REVIEW_WORK/batch068/record03/strict.tsv --workers 1 --quiet
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
  - CultureMech:004185
  command: just validate-terms data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
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
  - CultureMech:004185
  command: just validate-references data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm160
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf
  accessed_at: '2026-10-28T13:11:53.169058Z'
  locator: REVIEW_WORK/batch068/source01-03/dsm160.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5
- evidence_id: dsm67
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf
  accessed_at: '2026-10-28T13:12:44.562056Z'
  locator: REVIEW_WORK/batch068/source01-03-supplement/dsm67.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b
- evidence_id: api160
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/160
  accessed_at: '2026-10-28T13:11:52.874913Z'
  locator: REVIEW_WORK/batch068/source01-03/api160.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181
- evidence_id: api67
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/67
  accessed_at: '2026-10-28T13:12:44.225834Z'
  locator: REVIEW_WORK/batch068/source01-03-supplement/api67.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 57abca6ca0954ae731f771435c2b478df5d7e21a68a17685efbd6e4fae93fa53
- evidence_id: komodo160
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=160
  accessed_at: '2026-10-28T13:11:52.790336Z'
  locator: REVIEW_WORK/batch068/source01-03/komodo160.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: c36fb3b11c0cad5148b978bbaef61587d08cd6fec4cc0c31b951b52505227e47
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=160;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T13:11:52.731503Z'
  locator: REVIEW_WORK/batch068/source01-03/komodoList.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 59620fad80e70166fd81d71d28cff9e924386863889b5e4bcf6154015cdb4740
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: identityDSM1761
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-1761
  accessed_at: '2026-10-28T13:11:55.320922Z'
  locator: REVIEW_WORK/batch068/source01-03/identityDSM1761.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: b2da5d3fe23ce0305a925e2970696e2e9f3bdcdd4f10427e8cb301ba1838daef
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:26:10.910661Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 31e047243e1d186eae85eab5ed3c63f2668976609e33ed3d649fc6735d81344b
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:26:10.910821Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: e7777311c852c9ae4f263077012e8081c47d66286036a8913e44ebf1406051c6
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:26:10.910848Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:26:10.911137Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:26:10.911160Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:26:10.911180Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:26:10.911202Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: bcc04c2b48972dcd505a17acf0f85e85351b2949eaa3fa2e54a0f842c9268ab7
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:26:10.911225Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:26:10.916484Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d66cc6bf0cd5627ed5b97af2ce3d74e33b8f1f0226386b4cb46560b095078d8d
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:26:10.916532Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/cytophaga_hutchinsonii_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:26:10.922033Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f4a9438983fb56cf57d1494c6fe7519a0a4f6bd4f83b93c88d1e2ec1c33d3421
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T13:26:10.922096Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 3237ce966605caaad4ccc733603724b2e10b1cd5bd2acf9b4f9afc43f5f2eb54
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:26:10.922123Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e937e69e4000beb4081f552624fbc60af0bf84e6210decb99ad282e15085fd8c
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:26:10.922145Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 4e8bff299da7311b9956813bdbbf5f3024732da0a8e3f827b5eb14c796176b08
- evidence_id: report-26
  kind: prior_review
  reference: reports/yaml_record_review/20260922T130359Z-cytophaga_hutchinsonii_medium__b6268d2c.md
  locator: Complete report
  accessed_at: '2026-10-28T13:26:10.922166Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 027890942171344bd72e3926cc5db07b1d38563f0b67ea966b1bd0cd3ade6c46
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/historical-reading.json
  accessed_at: '2026-10-28T13:26:10.922195Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: e42ef41f41dd6fdb44a1f0be7c4205ee6132901202dfd42e4a84dc3caf73930d
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:26:10.922470Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: a30e066917f5177d2f3be711f605d848107b04b4cbc6259177313d6f5a6397b7
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/complete-document-reader.json
  accessed_at: '2026-10-28T13:26:10.922682Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: bf5060bca6d01b122bcab29dec89cac038b25d312bfe30a98f81291da3f861f7
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:26:10.922833Z'
  support: context_only
  summary: Current parser keeps only primary compounds and separately preserves referenced
    stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v
    enums without independently establishing the basis; the action classifier tests
    temperature before cool. Current behavior is not historical execution proof.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T13:26:10.922871Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/historical-source-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T13:26:10.922909Z'
  support: supports
  summary: Six included historical reports were read in their exact headers. Sixteen
    historical source objects and the current API160 digest match the original cited
    raw bytes; the September TOGO sibling report is comparison context, not this target.
  snapshot_sha256: 922641e090ea7b1ce60df13080e8386dd90365502c72c8950b6302e082032c5a
- evidence_id: internal-links
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/internal-reference-identity.json
  locator: Complete artifact
  accessed_at: '2026-10-28T13:26:10.923123Z'
  support: supports
  summary: Exact parent/child paths and IDs resolve; correspondence does not authorize
    transfer of a sibling variant or prove a current KOMODO table retrieval.
  snapshot_sha256: ae0dab051924bf3d49dac9ae1160bcfa4b8429bfa2a00cb6c97bbdc2907a08ac
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition
  accessed_at: '2026-10-28T13:26:10.923281Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients, solutions
    and selected metadata but not preparation_steps; the maintained history records
    a DSM160 copy. Current code behavior is not authenticated historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  accessed_at: '2026-10-28T13:11:58.560452Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  accessed_at: '2026-10-28T13:11:55.648830Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: chebi17057
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17057
  accessed_at: '2026-10-28T13:11:54.949655Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi17057.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: d8316efd6b721c17fedfab7c84433253c14c440dac0dfe410f06186f0e7664d4
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.963895Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 462f1a91e5a8f0d3c4a8f4a4479a40ea1615645ff0ad7719dc78a4b64c7cb5ad
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.963937Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: f5ba0c15f0b192b62783322d332263e927b9aad5861c0df014606b686a1222f8
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.963973Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: c572d65ac23e8f7cbc32cef4da17ea0b7223532cc4a1df314b15d20ab60b479d
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.964014Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: f3e2b988b80ff4c1feda42c80636012db04a6d5a47aa297c6ace9563492e7a1f
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.964050Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 025093c0d524273ae216c0d266cea91d18d8f1cd1435d9a152b63c53f3475875
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.964074Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: ab8e249999908873bc257aeaa064eb43c7d05152838b44eeda61ed58a5ce835b
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch068/record03/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:26:10.964093Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: b253c05cf45f611ef982f9ebdbcb91eba3727c34d957cec28292d07d356134bf
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record03/validate-schema.json
  accessed_at: '2026-10-28T13:11:35.776767Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e073f32a9c4c01690fd2d7744248bebdc6e9ba9bc46ec7aa050c20c0b87f2aae
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record03/validate-strict.json
  accessed_at: '2026-10-28T13:11:36.695886Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 087404b68a558ccd9d2f2e251f91964b13bc7f8b673d60c4708caf79ae942158
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record03/validate-terms.json
  accessed_at: '2026-10-28T13:11:37.700049Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 85588109ed5479c9cbcb20b7110939a7512b86edfb1d55e105b84c91d7f1f10c
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch068/record03/validate-references.json
  accessed_at: '2026-10-28T13:11:38.339111Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 715d24daed08d96ce0120d173950e91154e6397615fdfbe5d713ffa8240779a4
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and maintained-owner identity
  outcome: concern
  summary: DSM160 explicitly incorporates medium67; the exact source and DSM1761 catalog
    identity are consistent. Two selected maintained contributors resolve, but the
    current KOMODO catalogue is inaccessible. The September TOGO M2337 review concerns
    CultureMech008924 and a different generated target; its water and state findings
    are not transferred here.
  target_ids:
  - CultureMech:004185
  evidence_ids:
  - dsm160
  - dsm67
  - api160
  - identityDSM1761
  - komodo160
  - komodoList
  - internal-links
- assessment_id: representation
  area: representation
  topic: Conditional physical state and complex components
  outcome: supported
  summary: Complex/undefined bacterial classification and an agarized branch are source-consistent.
    Casitone and yeast extract remain complex named materials without mandatory ChEBI
    identities. Existing conditional notes are credited; no organism growth or anaerobic
    requirement is inferred from the name or stale catalogue flag.
  target_ids:
  - CultureMech:004185
  evidence_ids:
  - dsm160
  - dsm67
  - owner
  - owner-2
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 15 current concentration fields are covered by 16 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:004185
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","quantity_field_count":15,"decisions":[{"quantity_id":"q1","label":"Generated
    Casitone","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact provider explicitly declares this main-medium g_l rate; the primary67 table
    independently supports the batch mass and supplied form. Its 1000 mL water is
    not an explicit final-volume instruction. Retain the existing provider-basis rate
    and restore exact attached evidence; no numerical replacement or measured-volume
    claim is made.","source_stage":"Provider-declared main-medium rate, primary batch
    mass","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\":
    84,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Maintained
    Casitone","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"verified","rationale":"Both
    maintained owners already attach the exact matching API ingredient object and
    the current response is byte-identical to their cited digest. This verifies the
    named provider-declared rate and source form. It does not independently recover
    the original access event, establish measured final volume, authenticate the old
    KOMODO mapping response, or validate unused API mmol_l conversions.","source_stage":"Existing
    attached provider concentration evidence","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\":
    84,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Generated
    CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.36","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact provider explicitly declares this main-medium g_l rate; the primary67 table
    independently supports the batch mass and supplied form. Its 1000 mL water is
    not an explicit final-volume instruction. Retain the existing provider-basis rate
    and restore exact attached evidence; no numerical replacement or measured-volume
    claim is made.","source_stage":"Provider-declared main-medium rate, primary batch
    mass","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 1.36,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.36,\n                        \"mmol_l\":
    9.25076,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Maintained CaCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.36","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.36","unit":"G_PER_L"}}],"decision":"verified","rationale":"Both
    maintained owners already attach the exact matching API ingredient object and
    the current response is byte-identical to their cited digest. This verifies the
    named provider-declared rate and source form. It does not independently recover
    the original access event, establish measured final volume, authenticate the old
    KOMODO mapping response, or validate unused API mmol_l conversions.","source_stage":"Existing
    attached provider concentration evidence","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 1.36,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.36,\n                        \"mmol_l\":
    9.25076,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"Generated Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact provider explicitly declares this main-medium g_l rate; the primary67 table
    independently supports the batch mass and supplied form. Its 1000 mL water is
    not an explicit final-volume instruction. Retain the existing provider-basis rate
    and restore exact attached evidence; no numerical replacement or measured-volume
    claim is made.","source_stage":"Provider-declared main-medium rate, primary batch
    mass","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Maintained
    Yeast extract","local_fields":[{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"Both
    maintained owners already attach the exact matching API ingredient object and
    the current response is byte-identical to their cited digest. This verifies the
    named provider-declared rate and source form. It does not independently recover
    the original access event, establish measured final volume, authenticate the old
    KOMODO mapping response, or validate unused API mmol_l conversions.","source_stage":"Existing
    attached provider concentration evidence","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Agar
    conditional amount","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary67 table supplies 15 g agar and the API explicitly supplies g_l=15 with
    condition alternative. The current amount is supported on the provider basis for
    an agarized branch; it is excluded from the agar-free tube branch. Existing alternative
    notes are retained. Attach exact conditional evidence, without asserting that
    every source alternative is solid.","source_stage":"Agarized branch only","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"alternative\",\n                        \"amount\":
    15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Cellobiose
    conditional amount","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    API explicitly declares g_l=5 for its alternative cellobiose row; the current
    5 G_PER_L is supported on that declared provider basis. The primary gives bare
    0.5% with filter sterilization but does not state a percent denominator, so no
    independent w/v conversion or measured final-volume result is claimed. This addition
    belongs to the cellobiose alternative and is not required in either filter-paper
    alternative.","source_stage":"Cellobiose alternative; provider-declared normalization","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\":
    214,\n                        \"condition\": \"alternative\",\n                        \"attribute\":
    \"filter-sterilized\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"%\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    14.6071,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"pH","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"All
    existing pH7.2 values agree with the explicitly incorporated primary67 instruction
    and API160. Preserve the values and link root evidence.","source_stage":"Inherited
    base-medium pH","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.2.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Physical
    state","local_fields":[{"path":"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml","field_path":"physical_state","stored":"SOLID_AGAR"},{"path":"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml","field_path":"physical_state","stored":"SOLID_AGAR"},{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"physical_state","stored":"SOLID_AGAR"}],"decision":"evidence_only","rationale":"SOLID_AGAR
    is consistent with the agarized source branch and current agar amount, so it is
    not automatically wrong. The same label cannot describe the explicitly agar-free
    tube branch. Keep the chosen formulation clear rather than converting every source
    alternative to one universal state.","source_stage":"Conditional agarized interpretation","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"DSM
    pH preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"ADJUST_PH","description":"Adjust
    pH to 7.2."}}],"decision":"evidence_only","rationale":"The existing ADJUST_PH
    description agrees exactly with the source. Generated and KOMODO copies omit this
    structured preparation; the pH scalar alone does not replace complete preparation
    context.","source_stage":"Existing supported preparation","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.2.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"DSM
    alternative preparation text","local_fields":[{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"preparation_steps[1].description","stored":"To
    medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without agar)
    in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to each
    and autoclave, or place sterile pieces of filter paper on the surface of agarized
    medium."}],"decision":"evidence_only","rationale":"The existing description preserves
    the provider alternative text, including cellobiose, agar-free portions, filter-paper
    length and the separate surface-paper alternative. Credit the complete literal
    text while assessing its single action code separately.","source_stage":"Alternative-specific
    preparation prose","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without
    agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to
    each and autoclave, or place sterile pieces of filter paper on the surface of
    agarized medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"DSM
    combined action code","local_fields":[{"path":"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml","field_path":"preparation_steps[1].action","stored":"AUTOCLAVE"}],"decision":"conflict","rationale":"AUTOCLAVE
    applies to the described agar-free filter-paper tube branch, not to the entire
    combined sentence or the filter-sterilized cellobiose addition. The current classifier
    tests autoclave/steam before filter and returns one code for the mixed sentence;
    this explains a present writer limitation without proving historical execution.
    Split/qualify actions by their source alternative.","source_stage":"Action scope,
    not a changed amount","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without
    agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to
    each and autoclave, or place sterile pieces of filter paper on the surface of
    agarized medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Source-only
    water","local_fields":[],"decision":"evidence_only","rationale":"Primary67 explicitly
    lists 1000 mL distilled water and API160 retains it as solvent. All three local
    ingredient lists omit it. Retain it as source input water; do not call it measured
    final volume or infer a new solute rate from it.","source_stage":"Source-only
    solvent input","sources":[{"evidence_id":"dsm67","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium67.pdf","raw_path":"REVIEW_WORK/batch068/source01-03-supplement/dsm67.bin","raw_sha256":"970327784af828bf1bb3cf9264c9b3397c970a909a905f8d44f743821d30fd8b","text_sha256":"fe7c025d300fbaaddc1d452149195b4cfe84c9a5f89dcf5645a8faacf15bd7a6","accessed_at":"2026-10-28T13:12:44.562056Z","locator":"Complete
    primary medium67 table and pH","quote":"67. CY-AGAR\n\n\nCasitone                                    3.00    g\nCaCl2
    x 2 H2O                               1.36    g\nYeast extract                               1.00    g\nAgar                                       15.00    g\nDistilled
    water                          1000.00   ml\n\nAdjust pH to 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"Source-only tube portion and paper","local_fields":[],"decision":"evidence_only","rationale":"The
    primary explicitly supplies 5 mL portions and 7 cm paper in the agar-free branch.
    These are a per-tube portion and length, not concentrations. The other paper-on-agar
    branch gives no piece dimensions; no missing paper mass or incubation conditions
    are invented.","source_stage":"Alternative-specific portion and length","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"},{"evidence_id":"api160","reference":"https://mediadive.dsmz.de/rest/medium/160","raw_path":"REVIEW_WORK/batch068/source01-03/api160.bin","raw_sha256":"c6a847f039b60896100fa0f355b4b3a13242a6713337f16225b575e4c6166181","text_sha256":"d8c716e2fd5f37372c79ea2583e459d0645a44639cba856c57e8e6f8b91b2ff3","accessed_at":"2026-10-28T13:11:52.874913Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"To medium add 0.5% cellobiose (filter-sterilized) or distribute medium (without
    agar) in 5 ml amounts in test tubes, add a strip of filter paper (7 cm long) to
    each and autoclave, or place sterile pieces of filter paper on the surface of
    agarized medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Source-only
    sterilization limits","local_fields":[],"decision":"not_quantified","rationale":"The
    primary says filter-sterilized for cellobiose, autoclave for the paper-tube branch
    and sterile paper pieces for the surface branch. It gives no temperature, duration,
    filter pore size or sterilization cycle. Keep these fields unresolved rather than
    transferring a routine default.","source_stage":"Unquantified source conditions","sources":[{"evidence_id":"dsm160","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium160.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm160.bin","raw_sha256":"8a5d85feb5edbcb563f5a856e4c7690de92c3ca9a215f6f2f963ff0abe9e40e5","text_sha256":"7b7e69043f8defd2e026b8faaba651c2d72a4259cd0dc1ea7e48956d1c6c7567","accessed_at":"2026-10-28T13:11:53.169058Z","locator":"Complete
    primary medium160 alternatives","quote":"160. CYTOPHAGA HUTCHINSONII MEDIUM\n\n\n1.
    To medium 67 add 0.5% cellobiose (filter-sterilized)\nor\n2. Distribute medium
    67 (without agar) in 5 ml amounts in test tubes, add a strip of\nfilter paper
    (7 cm long) to each and autoclave, or place sterile pieces of filter paper on\nthe
    surface of agarized medium 67.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CYTOPHAGA_HUTCHINSONII_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml":null,"data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: 'All three asserted chemical IDs and canonical labels agree with current
    OLS: calcium chloride dihydrate (CHEBI:86158), agar (CHEBI:2509) and cellobiose
    (CHEBI:17057). Both primary and secondary slots preserve these forms. Current
    MIM preferred rows agree; optional Casitone and yeast candidate identifiers are
    inventory leads, not new asserted groundings or certified brand equivalents. Provider
    media IDs are identity identifiers, not missing MIM chemicals.'
  target_ids:
  - CultureMech:004185
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All six included reports were read in exact scope. Sixteen historical API
    objects and the cited API160 digest authenticate against current raw bytes, including
    six attached maintained claims. The September report reviews the distinct TOGO
    M2337 target and its repaired liquid interpretation; its assumptions and recommended
    sibling collapse are not adopted. Current conservative formulation equality detects
    preparation differences; the old merge event is not proof that the current writer
    permits them.
  target_ids:
  - CultureMech:004185
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-004185-conditional-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated record omits the source alternative preparation
  description: Restore the explicitly scoped DSM160/67 preparation and solvent context
    through maintained-input curation and conservative regeneration. The DSM owner
    retains the literal multi-alternative instruction, but its single AUTOCLAVE code
    overgeneralizes the paper-tube branch to the combined sentence. Represent the
    cellobiose and filter-paper alternatives separately, preserve the current conditional
    agar/cellobiose notes, and retain SOLID_AGAR only for a chosen agarized branch.
    Do not invent percent basis, final makeup, paper mass or sterilization settings.
  target_ids:
  - CultureMech:004185
  field_paths:
  - preparation_steps
  - ingredients[3].notes
  - ingredients[4].notes
  - data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml::preparation_steps[1].action
  evidence_ids:
  - dsm160
  - dsm67
  - api160
  - writer-mediadive
  - writer-resolver
  rule_id: review-yaml-record/conditional-preparation-scope
  native_severity: P2
  normalization_reason: 'Custom alternative-preparation scope rule normalized major
    (native priority P2): current amounts are retained, but omitted/overgeneralized
    handling changes source meaning.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-004185-attached-evidence-generation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Six supported owner claims are missing from the generated target
  description: Preserve the six exact attached API claims on the first three ingredients
    across both maintained owners and carry them into a compatible regenerated target.
    Add exact conditional evidence for agar and cellobiose and root evidence for preparation/water.
    Current API bytes authenticate the quoted provider rates; the primary water table
    does not independently establish final volume. Do not substitute a TOGO sibling
    or discard existing supported claims.
  target_ids:
  - CultureMech:004185
  field_paths:
  - ingredients[0].evidence
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - evidence
  - references
  evidence_ids:
  - api160
  - dsm160
  - dsm67
  - old-claims
  - writer-formulation
  - writer-merger
  rule_id: review-yaml-record/attached-evidence-generation
  native_severity: P3
  normalization_reason: 'Custom claim/event-provenance rule normalized minor (native
    priority P3): bounded support gaps without claiming a quantity or canonical-schema
    failure.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-004185-event-and-mapping-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical mapping and event syntax remain bounded provenance gaps
  description: 'Retain the old KOMODO mapping excerpt and the malformed/naive original
    events byte-for-byte. Current exact KOMODO media-list and accession routes return
    403, so the historical mapping retrieval and inherited Aerobic: No flag are not
    freshly authenticated. Append only verified corrective context if authoritative
    original provenance is recovered; do not overwrite original timestamps, infer
    anaerobic requirements or replay old commands.'
  target_ids:
  - CultureMech:004185
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml::curation_history[1].timestamp
  - notes
  - parent_media
  - variant_relationship
  evidence_ids:
  - komodo160
  - komodoList
  - history-auth
  - history
  rule_id: review-yaml-record/event-and-mapping-provenance
  native_severity: P3
  normalization_reason: 'Custom claim/event-provenance rule normalized minor (native
    priority P3): bounded support gaps without claiming a quantity or canonical-schema
    failure.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Restore the explicitly scoped DSM160/67 preparation and solvent context
    through maintained-input curation and conservative regeneration. The DSM owner
    retains the literal multi-alternative instruction, but its single AUTOCLAVE code
    overgeneralizes the paper-tube branch to the combined sentence. Represent the
    cellobiose and filter-paper alternatives separately, preserve the current conditional
    agar/cellobiose notes, and retain SOLID_AGAR only for a chosen agarized branch.
    Do not invent percent basis, final makeup, paper mass or sterilization settings.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004185
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
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
  description: Preserve the six exact attached API claims on the first three ingredients
    across both maintained owners and carry them into a compatible regenerated target.
    Add exact conditional evidence for agar and cellobiose and root evidence for preparation/water.
    Current API bytes authenticate the quoted provider rates; the primary water table
    does not independently establish final volume. Do not substitute a TOGO sibling
    or discard existing supported claims.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004185
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
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
  description: 'Retain the old KOMODO mapping excerpt and the malformed/naive original
    events byte-for-byte. Current exact KOMODO media-list and accession routes return
    403, so the historical mapping retrieval and inherited Aerobic: No flag are not
    freshly authenticated. Append only verified corrective context if authoritative
    original provenance is recovered; do not overwrite original timestamps, infer
    anaerobic requirements or replay old commands.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004185
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml
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
- Current exact KOMODO accession160 and media-list requests returned 403; the earlier
  mapping response hash remains an unrecovered historical observation. This identity
  branch makes the review partial.
- DSM160 and67 primary PDFs and both complete single-page visuals were read. DSM67
  specifies input water, not final-volume makeup; DSM160 gives bare 0.5% without a
  mass/volume basis. Explicit API g_l values are preserved as provider-declared rates
  only.
- 'No independent validation is claimed for unused API mmol_l conversions, original
  retrieval timing, or the old Aerobic: No flag. No growth-condition or strain-performance
  inference is made.'
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
