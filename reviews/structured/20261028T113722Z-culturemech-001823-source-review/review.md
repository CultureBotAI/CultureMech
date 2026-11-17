# Scientific review: COLUMBIA BLOOD AGAR

- Review: 20261028T113722Z-culturemech-001823-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T11:32:22.321109Z
- Finished UTC: 2026-10-28T11:37:22.433654Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM687 identity and maintained repair are supported, but the generated record is stale and current quantitative representations still overstate final-volume/percentage bases. All fifteen concentration fields and retained source/process assertions are reviewed; source claims, current chemical IDs and history are distinguished from schema success.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch065 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001823 | data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml | generated | columbia_blood_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001823 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001823 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001823 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001823 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSM687 identity

identity: supported. Targets: CultureMech:001823.

The primary title, provider687 medium object and both stable local identifiers agree. The base/finished-medium distinction is explicit, without borrowing DSM715 or inferring an organism-growth claim.

### Complex undefined solid medium

consistency: supported. Targets: CultureMech:001823.

COMPLEX/UNDEFINED and solid agar agree with the exact source. No named target organism is asserted, and no growth applicability is inferred from the generic medium title.

### Original native diagnostics

schema: supported. Targets: CultureMech:001823.

All four canonical commands exited zero once; strict reports zero errors and reference validation performed zero checks. These checks do not verify concentration bases or primary-source claims.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001823.

15 current concentration fields are covered by 16 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b065-quantity-inventory-v1","target":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","quantity_field_count":15,"decisions":[{"quantity_id":"q1","label":"Bacto Panton (Peptone)","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the same nominal g_l with volume=0, while API687 reports a separate prepared-base stage and later blood addition. Those fields do not establish this as the final blood-supplemented medium concentration. Preserve the supported batch mass and base identity; do not calculate a final denominator from input water or the unexplained blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 5-5","quote":"Bacto Panton (Peptone)                                            10.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Bacto Panton\",\n                        \"compound_id\": 2134,\n                        \"attribute\": \"Peptone\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Bacto Bitone (Peptone)","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the same nominal g_l with volume=0, while API687 reports a separate prepared-base stage and later blood addition. Those fields do not establish this as the final blood-supplemented medium concentration. Preserve the supported batch mass and base identity; do not calculate a final denominator from input water or the unexplained blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 6-6","quote":"Bacto Bitone (Peptone)                                            10.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Bacto Bitone\",\n                        \"compound_id\": 2135,\n                        \"attribute\": \"Peptone\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Tryptic Digest of beef heart","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[3].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the same nominal g_l with volume=0, while API687 reports a separate prepared-base stage and later blood addition. Those fields do not establish this as the final blood-supplemented medium concentration. Preserve the supported batch mass and base identity; do not calculate a final denominator from input water or the unexplained blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 7-7","quote":"Tryptic Digest of beef heart                                       3.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Tryptic Digest of beef heart\",\n                        \"compound_id\": 662,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Corn starch","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the same nominal g_l with volume=0, while API687 reports a separate prepared-base stage and later blood addition. Those fields do not establish this as the final blood-supplemented medium concentration. Preserve the supported batch mass and base identity; do not calculate a final denominator from input water or the unexplained blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 8-8","quote":"Corn starch                                                        1.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Corn starch\",\n                        \"compound_id\": 663,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[5].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the same nominal g_l with volume=0, while API687 reports a separate prepared-base stage and later blood addition. Those fields do not establish this as the final blood-supplemented medium concentration. Preserve the supported batch mass and base identity; do not calculate a final denominator from input water or the unexplained blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 9-9","quote":"NaCl                                                               5.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 85.5578,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[6].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[5].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the same nominal g_l with volume=0, while API687 reports a separate prepared-base stage and later blood addition. Those fields do not establish this as the final blood-supplemented medium concentration. Preserve the supported batch mass and base identity; do not calculate a final denominator from input water or the unexplained blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 10-10","quote":"Agar                                                              15.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Generated blood mass representation","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary states 5% sterile defibrinated blood, not 50 G_PER_L. The API derived g_l=50 documents the provider mapping but does not establish density or a percent basis. Preserve the literal percentage and unresolved basis; do not replace it with an invented mass or volume fraction.","source_stage":"Blood supplement after base cooling","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Defibrinated Blood\",\n                        \"compound_id\": 1177,\n                        \"attribute\": \"sterile\",\n                        \"amount\": 5,\n                        \"unit\": \"%\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Owner blood percentage basis","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"PERCENT_V_V"}}],"decision":"unsupported","rationale":"The owner correctly retains the source numeral and blood identity, but PERCENT_V_V is more specific than the printed bare %. Neither the inspected PDF nor API supplies an explicit v/v basis. Leave the basis unresolved and retain the existing source notes as context.","source_stage":"Blood supplement, unspecified percent basis","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Defibrinated Blood\",\n                        \"compound_id\": 1177,\n                        \"attribute\": \"sterile\",\n                        \"amount\": 5,\n                        \"unit\": \"%\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Owner input-water denominator","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1000","unit":"ML_PER_L"}}],"decision":"unsupported","rationale":"The source explicitly adds 1 L deionized water as input; it does not measure the final supplemented medium volume. The owner has restored this missing solvent, which is credited, but its ML_PER_L denominator is unverified. Preserve an input volume representation such as L rather than asserting a final-medium rate.","source_stage":"Solvent input, not measured final volume","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\": 418,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Retained owner source annotations","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[0].notes","stored":"DSMZ Medium 687 lists Bacto Panton as a peptone in the Columbia Blood Agar Base; the BD product is not reducible to one ChEBI molecule."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[1].notes","stored":"DSMZ Medium 687 lists Bacto Bitone as a peptone in the Columbia Blood Agar Base; the BD product is not reducible to one ChEBI molecule."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[2].notes","stored":"DSMZ Medium 687 lists tryptic digest of beef heart as part of the Columbia Blood Agar Base."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[3].notes","stored":"DSMZ Medium 687 lists 1 g corn starch."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[4].notes","stored":"DSMZ Medium 687 lists 5 g NaCl."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[5].notes","stored":"DSMZ Medium 687 lists 15 g agar."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[6].notes","stored":"DSMZ Medium 687 instructs suspending Columbia Blood Agar Base in 1 L deionized water."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[7].notes","stored":"DSMZ Medium 687 instructs adding 5% sterile defibrinated blood after cooling."}],"decision":"evidence_only","rationale":"These notes accurately identify the source base ingredients, printed batch masses, solvent input and literal blood percentage. They are retained textual support, distinct from the unresolved concentration enums; source/notes and a root URL are not ingredient-level EvidenceItem quotations.","source_stage":"Current owner notes","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-10","quote":"Columbia Blood Agar Base\n Bacto Panton (Peptone)                                            10.0    g\n Bacto Bitone (Peptone)                                            10.0    g\n Tryptic Digest of beef heart                                       3.0    g\n Corn starch                                                        1.0    g\n NaCl                                                               5.0    g\n Agar                                                              15.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix well.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Base mass and solvent input","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[0].description","stored":"Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to dissolve completely."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[0].description","stored":"Suspend 44 g Columbia Blood Agar Base in 1 L deionized water and heat to boiling."}],"decision":"evidence_only","rationale":"Both descriptions retain the supported source operation and its stated quantities. Preserve those statements and attach precise evidence; this does not authenticate any unstated final-volume or percent-basis conversion.","source_stage":"Existing preparation narrative","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to dissolve completely.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Sterilization duration and temperature","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[1].description","stored":"Sterilize in autoclave for 15 min at 121°C."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[1].description","stored":"Sterilize in an autoclave for 15 min at 121 C."}],"decision":"evidence_only","rationale":"Both descriptions retain the supported source operation and its stated quantities. Preserve those statements and attach precise evidence; this does not authenticate any unstated final-volume or percent-basis conversion.","source_stage":"Existing preparation narrative","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 17-17","quote":"2. Sterilize in autoclave for 15 min at 121C.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Sterilize in autoclave for 15 min at 121\\u00b0C.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Cooling and blood supplement","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].description","stored":"Cool to 45°C. Add 5% sterile defibrinated blood and mix well."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].description","stored":"Cool to 45 C, add 5% sterile defibrinated blood, and mix well."}],"decision":"evidence_only","rationale":"Both descriptions retain the supported source operation and its stated quantities. Preserve those statements and attach precise evidence; this does not authenticate any unstated final-volume or percent-basis conversion.","source_stage":"Existing preparation narrative","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\": \"Cool to 45\\u00b0C. Add 5% sterile defibrinated blood and mix well.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Generated cooling action","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].action","stored":"HEAT"}],"decision":"correct","rationale":"HEAT contradicts the retained description beginning Cool. The maintained owner already uses COOL; preserve that repair. The current importer temperature-before-cool branch explains a reproducible risk, not proof of the historical execution.","source_stage":"Action-code representation","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\": \"Cool to 45\\u00b0C. Add 5% sterile defibrinated blood and mix well.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Retained owner cooling action","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].action","stored":"COOL"}],"decision":"evidence_only","rationale":"COOL agrees with the exact current source narrative and is credited as an existing owner repair; no new temperature is inferred.","source_stage":"Maintained action code","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\": \"Cool to 45\\u00b0C. Add 5% sterile defibrinated blood and mix well.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Source base mass and provider volume sentinel","local_fields":[],"decision":"evidence_only","rationale":"The API distinguishes a 44 g base addition and a separate base composition with volume=0. The zero is a provider field, not evidence of a physically zero-volume stock and not a permissible divisor. The primary supports the six printed masses and their base context.","source_stage":"Source-only topology context","sources":[{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Columbia Blood Agar Base\",\n                        \"solution_id\": 1435,\n                        \"amount\": 44,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 4-10","quote":"Columbia Blood Agar Base\n Bacto Panton (Peptone)                                            10.0    g\n Bacto Bitone (Peptone)                                            10.0    g\n Tryptic Digest of beef heart                                       3.0    g\n Corn starch                                                        1.0    g\n NaCl                                                               5.0    g\n Agar                                                              15.0    g","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml":null,"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:001823.

Exact fresh OLS objects support the current starch, sodium chloride, agar, water and UBERON blood IDs and canonical labels. Generic starch does not certify corn origin, water does not certify deionization, and blood does not certify sterility or defibrination; those remain source annotations. Undefined peptones/digests are not forced to a single chemical ID. Current MIM linkage presence and exact snapshot membership are separate from chemical/formulation accuracy; no historical legacy-ID deprecation is newly authenticated.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:001823.

The complete three exact reports and their selected plan row were read. The current API687 digest equals the October7 cited digest and its twelve literal recipe/step objects join exactly; this authenticates content, not the old retrieval clock or execution. The September owner repair is visibly present and credited; the generated record remains older. Current guarded repair and conservative merge/importer behavior were read directly, including the append-only history issue.

## Findings

### f1: Generated record loses the maintained source repair

major / open / confirmed; issue key: culturemech-001823-generated-owner-staleness.

The exact maintained owner restores the peptone identities, source annotations, solvent input, percent wording, root reference and COOL action; the generated target still has a blood mass concentration, no solvent row and HEAT on a cooling description. Refresh only after the remaining owner basis/evidence issues are curated. Current merge_group copies singletons and the formulation matcher preserves exact scientific fields, so this is generated staleness, not a claim that the current merger still discards those repairs.

### f2: Base masses and blood percentage lack a supported final-medium basis

major / open / confirmed; issue key: culturemech-001823-base-final-volume-and-percent-basis.

Both layers encode the six base components as final G_PER_L values without a verified final supplemented volume; the API rates occur on a base object whose volume is zero. The target additionally converts a bare blood percentage to mass per litre, while the owner chooses v/v without an explicit source basis and expresses input water per final litre. Preserve the source batch, solvent and supplement stages; leave density and percentage/final-volume bases unresolved instead of inventing conversions.

### f3: Supported recipe statements lack attached literal claims

minor / open / confirmed; issue key: culturemech-001823-claim-evidence.

The owner has useful source/notes fields and a root source reference, but neither document attaches EvidenceItem snippets to the current quantity assertions. Add exact primary/API quotations with their batch and stage limits; do not mark unsupported final-medium concentrations verified. Three complete October reports are retained; equal current API bytes authenticate their twelve quoted objects without authenticating an original retrieval event.

### f4: Current repair writer can replace a prior history event

minor / open / confirmed; issue key: culturemech-001823-repair-append-only-history.

The current _append_curation_event replaces an existing entry sharing curator/action with a newly constructed fixed-timestamp event. Preserve the existing September event and make future actual changes append new truthful events instead of replacing the old event. This is a direct current-code observation, not a claim of another historical execution.

## Recommended Actions And Acceptance Checks

### a1

The exact maintained owner restores the peptone identities, source annotations, solvent input, percent wording, root reference and COOL action; the generated target still has a blood mass concentration, no solvent row and HEAT on a cooling description. Refresh only after the remaining owner basis/evidence issues are curated. Current merge_group copies singletons and the formulation matcher preserves exact scientific fields, so this is generated staleness, not a claim that the current merger still discards those repairs.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Both layers encode the six base components as final G_PER_L values without a verified final supplemented volume; the API rates occur on a base object whose volume is zero. The target additionally converts a bare blood percentage to mass per litre, while the owner chooses v/v without an explicit source basis and expresses input water per final litre. Preserve the source batch, solvent and supplement stages; leave density and percentage/final-volume bases unresolved instead of inventing conversions.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The owner has useful source/notes fields and a root source reference, but neither document attaches EvidenceItem snippets to the current quantity assertions. Add exact primary/API quotations with their batch and stage limits; do not mark unsupported final-medium concentrations verified. Three complete October reports are retained; equal current API bytes authenticate their twelve quoted objects without authenticating an original retrieval event.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Revise the named repair writer so changed repairs append a new actual-time event while unchanged reruns preserve prior events byte-for-byte.

- A changed repair retains the complete existing history and appends a new actual event.
- An unchanged rerun is a no-op; no backdated or replaced history entry.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm687 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf; REVIEW_WORK/batch065/source07-08-10/dsm687.json; exact original raw/text/hash/time metadata | context_only | 07 exact DSM687 primary recipe; ordinary source/quantity scope, no strain-growth inference. |
| api687 | https://mediadive.dsmz.de/rest/medium/687; REVIEW_WORK/batch065/source07-08-10/api687.json; exact original raw/text/hash/time metadata | context_only | 07 exact current API687 source; reused immutable sibling capture, original URL/time/raw/text preserved. |
| target | data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| writer-repair | scripts/repair_dsmz_1551_687_score15.py; _dsmz_687_ingredients, _ensure_target, repair_record, _append_curation_event | context_only | Current exact687 guarded repair preserves the revised ingredient names, water, percent wording and COOL action. _append_curation_event replaces a matching historical event using a fixed timestamp; that current behavior needs an append-only successor design, not a claim that it ran again. |
| historical-reading | REVIEW_WORK/batch065/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch065/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch065/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser keeps only primary compounds and separately preserves referenced stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v enums without independently establishing the basis; the action classifier tests temperature before cool. Current behavior is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28017; REVIEW_WORK/batch065/source07-08-10/chebi28017.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; no operational grounding assessment08. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch065/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; no operational grounding assessment08. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch065/source07-08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; no operational grounding assessment08. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch065/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; no operational grounding assessment08. |
| uberon0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON:0000178; REVIEW_WORK/batch065/source07-08-10/uberon0000178.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; no operational grounding assessment08. |
| quantities | REVIEW_WORK/batch065/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch065/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch065/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch065/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch065/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch065/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch065/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch065/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch065/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch065/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch065/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The complete one-page primary PDF was read visually and as text. It supplies no explicit final supplemented volume or percent basis; no density or normalization is guessed.
- API687 is an exact immutable same-batch shared capture from record06, with original raw/text/metadata URL and access timestamps preserved. Its role here is exact687 evidence, not a transfer from record06 DSM715.
- Ignored-inclusive report and script enumeration covered the exact target/owner names, all selected report parents and named repair writer; no global literature absence claim is made.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T113722Z-culturemech-001823-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: COLUMBIA BLOOD AGAR'
started_at: '2026-10-28T11:32:22.321109Z'
finished_at: '2026-10-28T11:37:22.433654Z'
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
summary: DSM687 identity and maintained repair are supported, but the generated record
  is stale and current quantitative representations still overstate final-volume/percentage
  bases. All fifteen concentration fields and retained source/process assertions are
  reviewed; source claims, current chemical IDs and history are distinguished from
  schema success.
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
  - path: data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml
    sha256: e1350cc74923444a91621a18e498b615f87064736649ee8ccecffd3c8d24438a
    role: target
  - path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
    sha256: 1bd1d60e982c9a02bf0cdd64ab3719ab732d02b2ffb5f6fc9042cc2e53db2acd
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml.md
    sha256: d671752223921bafdf2ac5b9fb00ab5593b4ed33f19458fbd5841e95d4349b59
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.md
    sha256: 736ca4b421de40b1435769d3d201c97f4f76bcd3bba6620e5be960637009f35c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.md
    sha256: e17314f0e04fd6f1b4dde26b9778e5c4ed48e86730564dd83e82e724eb9f9bfe
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
  - path: scripts/repair_dsmz_1551_687_score15.py
    sha256: 8d6df8debee25199456cb7b8bde62e265b78864396fe01259a924ad22a183745
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  selection: Authoritative batch065 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001823
targets:
- target_id: CultureMech:001823
  path: data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml
  label: columbia_blood_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
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
  - CultureMech:001823
  command: just validate-schema data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml
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
  - CultureMech:001823
  command: just validate-strict data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml --out
    REVIEW_WORK/batch065/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:001823
  command: just validate-terms data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml
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
  - CultureMech:001823
  command: just validate-references data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm687
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf
  accessed_at: '2026-10-28T11:33:15.730030Z'
  locator: REVIEW_WORK/batch065/source07-08-10/dsm687.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 07 exact DSM687 primary recipe; ordinary source/quantity scope, no strain-growth
    inference.
  snapshot_sha256: bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f
- evidence_id: api687
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/687
  accessed_at: '2026-10-28T11:31:04.906482Z'
  locator: REVIEW_WORK/batch065/source07-08-10/api687.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 07 exact current API687 source; reused immutable sibling capture, original
    URL/time/raw/text preserved.
  snapshot_sha256: e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml
  locator: Complete file
  accessed_at: '2026-10-28T11:37:22.388575Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: e1350cc74923444a91621a18e498b615f87064736649ee8ccecffd3c8d24438a
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
  locator: Complete file
  accessed_at: '2026-10-28T11:37:22.388761Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 1bd1d60e982c9a02bf0cdd64ab3719ab732d02b2ffb5f6fc9042cc2e53db2acd
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T11:37:22.388791Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T11:37:22.389120Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T11:37:22.389145Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T11:37:22.389167Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T11:37:22.389194Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T11:37:22.396132Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d671752223921bafdf2ac5b9fb00ab5593b4ed33f19458fbd5841e95d4349b59
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.md
  locator: Complete report
  accessed_at: '2026-10-28T11:37:22.396191Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 736ca4b421de40b1435769d3d201c97f4f76bcd3bba6620e5be960637009f35c
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.md
  locator: Complete report
  accessed_at: '2026-10-28T11:37:22.396221Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e17314f0e04fd6f1b4dde26b9778e5c4ed48e86730564dd83e82e724eb9f9bfe
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_dsmz_1551_687_score15.py
  locator: _dsmz_687_ingredients, _ensure_target, repair_record, _append_curation_event
  accessed_at: '2026-10-28T11:37:22.396248Z'
  support: context_only
  summary: Current exact687 guarded repair preserves the revised ingredient names,
    water, percent wording and COOL action. _append_curation_event replaces a matching
    historical event using a fixed timestamp; that current behavior needs an append-only
    successor design, not a claim that it ran again.
  snapshot_sha256: 8d6df8debee25199456cb7b8bde62e265b78864396fe01259a924ad22a183745
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/historical-reading.json
  accessed_at: '2026-10-28T11:37:22.396717Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 85daadde096c356afbebf66b1f4d82e07cf997a8bf2567b9c8add682f76d57c1
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T11:37:22.396759Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 8e50c563fcaebff20d97a5d4c641bf0beb31ab194d1918ce8b7436ac3644db14
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/complete-document-reader.json
  accessed_at: '2026-10-28T11:37:22.396790Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: fd430de564d6168da456860e19fbee1e4be34acca9b8d85f37aeb55db7fb04f8
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T11:37:22.396814Z'
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
  accessed_at: '2026-10-28T11:37:22.396854Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28017
  accessed_at: '2026-10-28T11:33:17.672679Z'
  locator: REVIEW_WORK/batch065/source07-08-10/chebi28017.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; no operational grounding
    assessment08.
  snapshot_sha256: 8d5cfcf42eb1f0d584069e65aa21275d1863248742e38cef6b0bbe3853db7084
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T11:33:17.179047Z'
  locator: REVIEW_WORK/batch065/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; no operational grounding
    assessment08.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T11:33:17.051262Z'
  locator: REVIEW_WORK/batch065/source07-08-10/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; no operational grounding
    assessment08.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T11:33:16.359697Z'
  locator: REVIEW_WORK/batch065/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; no operational grounding
    assessment08.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: uberon0000178
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON:0000178
  accessed_at: '2026-10-28T11:33:19.694910Z'
  locator: REVIEW_WORK/batch065/source07-08-10/uberon0000178.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; no operational grounding
    assessment08.
  snapshot_sha256: e6a51f559811919b854cc6f88e7490e3ac7dd7d2148c0d6628386f151605252d
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432490Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: f7ea95d4dd9e6af61a3543aa90bdfddb0a548ea0f0bb4819af928464c319a170
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432536Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: dfa2674edac491363876edb1f3721087063b5c1fe34dcd836c6a0038da4bacce
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432568Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: ae0537a9ff0ec0631aef332f74afba887ac1452d0a8dc935fca23ed7271b6280
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432599Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 76ee7ae30cd45905715628e6d796e1cf1257f013d16b763e7c78ad0d0aaf8dc6
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432628Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 2653ff0a6c4434feaa95ffa3e53802dbdc9ce8cb98ba670e7651d5bcf7dae40b
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432647Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 18478cf7d308edb5447ff7f076392194c04b68941246e60db854c0b6ac4b0a6d
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch065/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:37:22.432665Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch065/record07/schema-result.json
  accessed_at: '2026-10-28T11:32:23.424595Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c6b02d5edb1a00f3bbca0b31561de3f1f0dda18fe9369a08d4ba62b20625f013
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch065/record07/strict-result.json
  accessed_at: '2026-10-28T11:32:24.370845Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4926d77eb5c59473984a761045a96326e580bd7695311cf84885c6161b9727f1
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch065/record07/terms-result.json
  accessed_at: '2026-10-28T11:32:25.410954Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 69be276c892537ad3926da97cf5cef39dd2b45bcee13a8e15d1d3e84d8c6caa5
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch065/record07/references-result.json
  accessed_at: '2026-10-28T11:32:26.086949Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 2f949cf5dcdca8746bbde0ab615e6140484583e2c36076cfb48393ea0c8cc989
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSM687 identity
  outcome: supported
  summary: The primary title, provider687 medium object and both stable local identifiers
    agree. The base/finished-medium distinction is explicit, without borrowing DSM715
    or inferring an organism-growth claim.
  target_ids:
  - CultureMech:001823
  evidence_ids:
  - dsm687
  - api687
  - target
  - owner
- assessment_id: classification
  area: consistency
  topic: Complex undefined solid medium
  outcome: supported
  summary: COMPLEX/UNDEFINED and solid agar agree with the exact source. No named
    target organism is asserted, and no growth applicability is inferred from the
    generic medium title.
  target_ids:
  - CultureMech:001823
  evidence_ids:
  - dsm687
  - target
  - owner
- assessment_id: schema
  area: schema
  topic: Original native diagnostics
  outcome: supported
  summary: All four canonical commands exited zero once; strict reports zero errors
    and reference validation performed zero checks. These checks do not verify concentration
    bases or primary-source claims.
  target_ids:
  - CultureMech:001823
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 15 current concentration fields are covered by 16 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001823
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b065-quantity-inventory-v1","target":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","quantity_field_count":15,"decisions":[{"quantity_id":"q1","label":"Bacto
    Panton (Peptone)","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the
    same nominal g_l with volume=0, while API687 reports a separate prepared-base
    stage and later blood addition. Those fields do not establish this as the final
    blood-supplemented medium concentration. Preserve the supported batch mass and
    base identity; do not calculate a final denominator from input water or the unexplained
    blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented
    finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 5-5","quote":"Bacto Panton (Peptone)                                            10.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Bacto Panton\",\n                        \"compound_id\":
    2134,\n                        \"attribute\": \"Peptone\",\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    10,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"Bacto Bitone (Peptone)","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the
    same nominal g_l with volume=0, while API687 reports a separate prepared-base
    stage and later blood addition. Those fields do not establish this as the final
    blood-supplemented medium concentration. Preserve the supported batch mass and
    base identity; do not calculate a final denominator from input water or the unexplained
    blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented
    finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 6-6","quote":"Bacto Bitone (Peptone)                                            10.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Bacto Bitone\",\n                        \"compound_id\":
    2135,\n                        \"attribute\": \"Peptone\",\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    10,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Tryptic Digest of beef heart","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[3].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the
    same nominal g_l with volume=0, while API687 reports a separate prepared-base
    stage and later blood addition. Those fields do not establish this as the final
    blood-supplemented medium concentration. Preserve the supported batch mass and
    base identity; do not calculate a final denominator from input water or the unexplained
    blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented
    finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 7-7","quote":"Tryptic Digest of beef heart                                       3.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Tryptic Digest of beef heart\",\n                        \"compound_id\":
    662,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Corn
    starch","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the
    same nominal g_l with volume=0, while API687 reports a separate prepared-base
    stage and later blood addition. Those fields do not establish this as the final
    blood-supplemented medium concentration. Preserve the supported batch mass and
    base identity; do not calculate a final denominator from input water or the unexplained
    blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented
    finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 8-8","quote":"Corn starch                                                        1.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Corn starch\",\n                        \"compound_id\":
    663,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[5].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the
    same nominal g_l with volume=0, while API687 reports a separate prepared-base
    stage and later blood addition. Those fields do not establish this as the final
    blood-supplemented medium concentration. Preserve the supported batch mass and
    base identity; do not calculate a final denominator from input water or the unexplained
    blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented
    finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 9-9","quote":"NaCl                                                               5.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    85.5578,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[6].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[5].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass belongs to the Columbia Blood Agar Base batch. API1435 exposes the
    same nominal g_l with volume=0, while API687 reports a separate prepared-base
    stage and later blood addition. Those fields do not establish this as the final
    blood-supplemented medium concentration. Preserve the supported batch mass and
    base identity; do not calculate a final denominator from input water or the unexplained
    blood percentage.","source_stage":"Base formulation, distinct from blood-supplemented
    finished medium","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-4","quote":"Columbia Blood Agar Base","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 10-10","quote":"Agar                                                              15.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"Generated blood mass representation","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary states 5% sterile defibrinated blood, not 50 G_PER_L. The API derived
    g_l=50 documents the provider mapping but does not establish density or a percent
    basis. Preserve the literal percentage and unresolved basis; do not replace it
    with an invented mass or volume fraction.","source_stage":"Blood supplement after
    base cooling","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix
    well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Defibrinated Blood\",\n                        \"compound_id\":
    1177,\n                        \"attribute\": \"sterile\",\n                        \"amount\":
    5,\n                        \"unit\": \"%\",\n                        \"g_l\":
    50,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Owner blood percentage basis","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[7].concentration","stored":{"value":"5","unit":"PERCENT_V_V"}}],"decision":"unsupported","rationale":"The
    owner correctly retains the source numeral and blood identity, but PERCENT_V_V
    is more specific than the printed bare %. Neither the inspected PDF nor API supplies
    an explicit v/v basis. Leave the basis unresolved and retain the existing source
    notes as context.","source_stage":"Blood supplement, unspecified percent basis","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix
    well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Defibrinated Blood\",\n                        \"compound_id\":
    1177,\n                        \"attribute\": \"sterile\",\n                        \"amount\":
    5,\n                        \"unit\": \"%\",\n                        \"g_l\":
    50,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Owner input-water denominator","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1000","unit":"ML_PER_L"}}],"decision":"unsupported","rationale":"The
    source explicitly adds 1 L deionized water as input; it does not measure the final
    supplemented medium volume. The owner has restored this missing solvent, which
    is credited, but its ML_PER_L denominator is unverified. Preserve an input volume
    representation such as L rather than asserting a final-medium rate.","source_stage":"Solvent
    input, not measured final volume","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\":
    418,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Retained owner source annotations","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[0].notes","stored":"DSMZ
    Medium 687 lists Bacto Panton as a peptone in the Columbia Blood Agar Base; the
    BD product is not reducible to one ChEBI molecule."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[1].notes","stored":"DSMZ
    Medium 687 lists Bacto Bitone as a peptone in the Columbia Blood Agar Base; the
    BD product is not reducible to one ChEBI molecule."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[2].notes","stored":"DSMZ
    Medium 687 lists tryptic digest of beef heart as part of the Columbia Blood Agar
    Base."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[3].notes","stored":"DSMZ
    Medium 687 lists 1 g corn starch."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[4].notes","stored":"DSMZ
    Medium 687 lists 5 g NaCl."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[5].notes","stored":"DSMZ
    Medium 687 lists 15 g agar."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[6].notes","stored":"DSMZ
    Medium 687 instructs suspending Columbia Blood Agar Base in 1 L deionized water."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"ingredients[7].notes","stored":"DSMZ
    Medium 687 instructs adding 5% sterile defibrinated blood after cooling."}],"decision":"evidence_only","rationale":"These
    notes accurately identify the source base ingredients, printed batch masses, solvent
    input and literal blood percentage. They are retained textual support, distinct
    from the unresolved concentration enums; source/notes and a root URL are not ingredient-level
    EvidenceItem quotations.","source_stage":"Current owner notes","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-10","quote":"Columbia Blood Agar Base\n Bacto Panton (Peptone)                                            10.0    g\n
    Bacto Bitone (Peptone)                                            10.0    g\n
    Tryptic Digest of beef heart                                       3.0    g\n
    Corn starch                                                        1.0    g\n
    NaCl                                                               5.0    g\n
    Agar                                                              15.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix
    well.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Base mass
    and solvent input","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[0].description","stored":"Suspend
    44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling to dissolve
    completely."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[0].description","stored":"Suspend
    44 g Columbia Blood Agar Base in 1 L deionized water and heat to boiling."}],"decision":"evidence_only","rationale":"Both
    descriptions retain the supported source operation and its stated quantities.
    Preserve those statements and attach precise evidence; this does not authenticate
    any unstated final-volume or percent-basis conversion.","source_stage":"Existing
    preparation narrative","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 44 g Columbia Blood Agar Base in 1l deionized water. Heat to boiling
    to dissolve completely.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Sterilization
    duration and temperature","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[1].description","stored":"Sterilize
    in autoclave for 15 min at 121°C."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[1].description","stored":"Sterilize
    in an autoclave for 15 min at 121 C."}],"decision":"evidence_only","rationale":"Both
    descriptions retain the supported source operation and its stated quantities.
    Preserve those statements and attach precise evidence; this does not authenticate
    any unstated final-volume or percent-basis conversion.","source_stage":"Existing
    preparation narrative","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 17-17","quote":"2. Sterilize in autoclave for 15 min at 121C.","quote_basis":"derivative
    text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Sterilize in autoclave for 15 min at 121\\u00b0C.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"Cooling and blood supplement","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].description","stored":"Cool
    to 45°C. Add 5% sterile defibrinated blood and mix well."},{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].description","stored":"Cool
    to 45 C, add 5% sterile defibrinated blood, and mix well."}],"decision":"evidence_only","rationale":"Both
    descriptions retain the supported source operation and its stated quantities.
    Preserve those statements and attach precise evidence; this does not authenticate
    any unstated final-volume or percent-basis conversion.","source_stage":"Existing
    preparation narrative","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix
    well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\":
    \"Cool to 45\\u00b0C. Add 5% sterile defibrinated blood and mix well.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"Generated cooling action","local_fields":[{"path":"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].action","stored":"HEAT"}],"decision":"correct","rationale":"HEAT
    contradicts the retained description beginning Cool. The maintained owner already
    uses COOL; preserve that repair. The current importer temperature-before-cool
    branch explains a reproducible risk, not proof of the historical execution.","source_stage":"Action-code
    representation","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix
    well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\":
    \"Cool to 45\\u00b0C. Add 5% sterile defibrinated blood and mix well.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"Retained owner cooling action","local_fields":[{"path":"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml","field_path":"preparation_steps[2].action","stored":"COOL"}],"decision":"evidence_only","rationale":"COOL
    agrees with the exact current source narrative and is credited as an existing
    owner repair; no new temperature is inferred.","source_stage":"Maintained action
    code","sources":[{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 19-19","quote":"3. Cool to 45C. Add 5% sterile defibrinated blood and mix
    well.","quote_basis":"derivative text"},{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].steps[2]","quote":"{\n                        \"step\":
    \"Cool to 45\\u00b0C. Add 5% sterile defibrinated blood and mix well.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"Source base mass and provider volume sentinel","local_fields":[],"decision":"evidence_only","rationale":"The
    API distinguishes a 44 g base addition and a separate base composition with volume=0.
    The zero is a provider field, not evidence of a physically zero-volume stock and
    not a permissible divisor. The primary supports the six printed masses and their
    base context.","source_stage":"Source-only topology context","sources":[{"evidence_id":"api687","reference":"https://mediadive.dsmz.de/rest/medium/687","raw_path":"REVIEW_WORK/batch065/record06/sources/api687.raw","raw_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","text_sha256":"e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9","accessed_at":"2026-10-28T11:31:04.906482Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Columbia Blood Agar Base\",\n                        \"solution_id\":
    1435,\n                        \"amount\": 44,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 4-10","quote":"Columbia Blood Agar Base\n Bacto Panton (Peptone)                                            10.0    g\n
    Bacto Bitone (Peptone)                                            10.0    g\n
    Tryptic Digest of beef heart                                       3.0    g\n
    Corn starch                                                        1.0    g\n
    NaCl                                                               5.0    g\n
    Agar                                                              15.0    g","quote_basis":"derivative
    text"},{"evidence_id":"dsm687","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf","raw_path":"REVIEW_WORK/batch065/source07-08-10/dsm687.raw","raw_sha256":"bf4e44fb1f8b3bf9f1e5c0f8ee4337f9f68e618a14f8878ff0432eb8fb70579f","text_sha256":"e22752b854c869f1d233ff20c293790dae7c5cc95e8ae1da3c87b08fc8429651","accessed_at":"2026-10-28T11:33:15.730030Z","locator":"dsm687.txt
    lines 14-15","quote":"1. Suspend 44 g Columbia Blood Agar Base in 1l deionized
    water. Heat to boiling to\ndissolve completely.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR.yaml":null,"data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: Exact fresh OLS objects support the current starch, sodium chloride, agar,
    water and UBERON blood IDs and canonical labels. Generic starch does not certify
    corn origin, water does not certify deionization, and blood does not certify sterility
    or defibrination; those remain source annotations. Undefined peptones/digests
    are not forced to a single chemical ID. Current MIM linkage presence and exact
    snapshot membership are separate from chemical/formulation accuracy; no historical
    legacy-ID deprecation is newly authenticated.
  target_ids:
  - CultureMech:001823
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: The complete three exact reports and their selected plan row were read.
    The current API687 digest equals the October7 cited digest and its twelve literal
    recipe/step objects join exactly; this authenticates content, not the old retrieval
    clock or execution. The September owner repair is visibly present and credited;
    the generated record remains older. Current guarded repair and conservative merge/importer
    behavior were read directly, including the append-only history issue.
  target_ids:
  - CultureMech:001823
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-001823-generated-owner-staleness
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated record loses the maintained source repair
  description: The exact maintained owner restores the peptone identities, source
    annotations, solvent input, percent wording, root reference and COOL action; the
    generated target still has a blood mass concentration, no solvent row and HEAT
    on a cooling description. Refresh only after the remaining owner basis/evidence
    issues are curated. Current merge_group copies singletons and the formulation
    matcher preserves exact scientific fields, so this is generated staleness, not
    a claim that the current merger still discards those repairs.
  target_ids:
  - CultureMech:001823
  field_paths:
  - ingredients
  - preparation_steps[2].action
  - references
  - curation_history
  evidence_ids:
  - target
  - owner
  - dsm687
  - api687
  - writer-repair
  - writer-merger
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-001823-base-final-volume-and-percent-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Base masses and blood percentage lack a supported final-medium basis
  description: Both layers encode the six base components as final G_PER_L values
    without a verified final supplemented volume; the API rates occur on a base object
    whose volume is zero. The target additionally converts a bare blood percentage
    to mass per litre, while the owner chooses v/v without an explicit source basis
    and expresses input water per final litre. Preserve the source batch, solvent
    and supplement stages; leave density and percentage/final-volume bases unresolved
    instead of inventing conversions.
  target_ids:
  - CultureMech:001823
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsm687
  - api687
  - target
  - owner
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-001823-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported recipe statements lack attached literal claims
  description: The owner has useful source/notes fields and a root source reference,
    but neither document attaches EvidenceItem snippets to the current quantity assertions.
    Add exact primary/API quotations with their batch and stage limits; do not mark
    unsupported final-medium concentrations verified. Three complete October reports
    are retained; equal current API bytes authenticate their twelve quoted objects
    without authenticating an original retrieval event.
  target_ids:
  - CultureMech:001823
  field_paths:
  - ingredients
  - preparation_steps
  - evidence
  evidence_ids:
  - dsm687
  - api687
  - target
  - owner
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-001823-repair-append-only-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current repair writer can replace a prior history event
  description: The current _append_curation_event replaces an existing entry sharing
    curator/action with a newly constructed fixed-timestamp event. Preserve the existing
    September event and make future actual changes append new truthful events instead
    of replacing the old event. This is a direct current-code observation, not a claim
    of another historical execution.
  target_ids:
  - CultureMech:001823
  field_paths:
  - scripts/repair_dsmz_1551_687_score15.py::_append_curation_event
  evidence_ids:
  - writer-repair
  - owner
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_dsmz_1551_687_score15.py
    role: maintained repair writer
actions:
- action_id: a1
  description: The exact maintained owner restores the peptone identities, source
    annotations, solvent input, percent wording, root reference and COOL action; the
    generated target still has a blood mass concentration, no solvent row and HEAT
    on a cooling description. Refresh only after the remaining owner basis/evidence
    issues are curated. Current merge_group copies singletons and the formulation
    matcher preserves exact scientific fields, so this is generated staleness, not
    a claim that the current merger still discards those repairs.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001823
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
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
  description: Both layers encode the six base components as final G_PER_L values
    without a verified final supplemented volume; the API rates occur on a base object
    whose volume is zero. The target additionally converts a bare blood percentage
    to mass per litre, while the owner chooses v/v without an explicit source basis
    and expresses input water per final litre. Preserve the source batch, solvent
    and supplement stages; leave density and percentage/final-volume bases unresolved
    instead of inventing conversions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001823
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
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
  description: The owner has useful source/notes fields and a root source reference,
    but neither document attaches EvidenceItem snippets to the current quantity assertions.
    Add exact primary/API quotations with their batch and stage limits; do not mark
    unsupported final-medium concentrations verified. Three complete October reports
    are retained; equal current API bytes authenticate their twelve quoted objects
    without authenticating an original retrieval event.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001823
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml
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
  description: Revise the named repair writer so changed repairs append a new actual-time
    event while unchanged reruns preserve prior events byte-for-byte.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001823
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_dsmz_1551_687_score15.py
    role: maintained repair writer
  acceptance_checks:
  - A changed repair retains the complete existing history and appends a new actual
    event.
  - An unchanged rerun is a no-op; no backdated or replaced history entry.
  generator: scripts/repair_dsmz_1551_687_score15.py
limitations:
- The complete one-page primary PDF was read visually and as text. It supplies no
  explicit final supplemented volume or percent basis; no density or normalization
  is guessed.
- API687 is an exact immutable same-batch shared capture from record06, with original
  raw/text/metadata URL and access timestamps preserved. Its role here is exact687
  evidence, not a transfer from record06 DSM715.
- Ignored-inclusive report and script enumeration covered the exact target/owner names,
  all selected report parents and named repair writer; no global literature absence
  claim is made.
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
