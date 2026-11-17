# Scientific review: DESULFONATRONUM ALKALITOLERANS MEDIUM

- Review: 20261028T201844Z-culturemech-000952-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:15:09.132786Z
- Finished UTC: 2026-10-28T20:18:44.464248Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM1485 preserves source stock strengths and main preparation, but all23 stock-stage values are presented as main-medium concentrations. Restore A–H assembly and trace-stock pH scope, correct nickel-hydrate grounding, and attach exact field-level evidence.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch077 index 01
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000952 | data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml | generated | desulfonatronum_alkalitolerans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:000952 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:000952 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:000952 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:000952 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSM1485 source and owner

identity: supported. Targets: CultureMech:000952.

The selected generated record has one maintained DSM1485 contributor and all scientific fields match that owner. The current two-page primary and complete API are the exact accession. Referenced media1369/385 contribute only the printed trace and SeW definitions; their other formulations are excluded.

### Complex liquid medium

representation: supported. Targets: CultureMech:000952.

Yeast extract supports complex/undefined classification; no solidifier is specified. The high_metal flag is retained as qualitative metadata, not a quantified threshold or growth claim.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:000952.

46 current concentration fields are covered by 45 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b077-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","quantity_field_count":46,"decisions":[{"quantity_id":"q1","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"6.31579","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"6.31579","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 27-27","quote":"NaCl                                                   6.00        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.31579,\n                        \"mmol_l\": 108.073,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.05263","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.05263","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 28-28","quote":"K2HPO4                                                 1.00        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.05263,\n                        \"mmol_l\": 6.04349,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q3","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"33.6842","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"33.6842","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 29-29","quote":"NaHCO3                                                32.00        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 32,\n                        \"unit\": \"g\",\n                        \"g_l\": 33.6842,\n                        \"mmol_l\": 400.969,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q4","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"11.1579","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"11.1579","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 30-30","quote":"Na2CO3                                                10.60        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 10.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 11.1579,\n                        \"mmol_l\": 105.275,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q5","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.94737","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.94737","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 31-31","quote":"Na2SO4                                                 2.80        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 2.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.94737,\n                        \"mmol_l\": 20.7503,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q6","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.210526","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.210526","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 32-32","quote":"Na-acetate                                             0.20        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210526,\n                        \"mmol_l\": 2.56634,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution A, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. Solution A has950ml input water and is dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q7","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution D, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot.","source_stage":"Solution D","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 48-48","quote":"NH4Cl                                                  0.20        g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 373.902,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution D, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution D, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."}]},{"quantity_id":"q8","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution E, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot.","source_stage":"Solution E","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 62-62","quote":"MgCl2 x 6 H2O                                 0.20    g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[5].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 98.3753,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution E, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution E, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution F, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot.","source_stage":"Solution F","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 68-68","quote":"Yeast extract                                20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[6].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution F, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution F, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."}]},{"quantity_id":"q10","label":"Na-formate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"340","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"340","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution G, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot.","source_stage":"Solution G","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 74-74","quote":"Na-formate                                    3.40    g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[7].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 3.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 340,\n                        \"mmol_l\": 4999.47,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution G, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution G, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."}]},{"quantity_id":"q11","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution H, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot.","source_stage":"Solution H","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 80-80","quote":"Na2S x 9 H2O                                  0.30    g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[8].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution H, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Solution H, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. This single-component solution has10ml input water and a separate10ml receiving dose; the printed mass belongs to that aliquot."}]},{"quantity_id":"q12","label":"EDTA","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 86-86","quote":"EDTA                                        5.00      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q13","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 87-87","quote":"FeSO4 x 7 H2O                               2.20      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.2,\n                        \"mmol_l\": 7.91324,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q14","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 88-88","quote":"ZnSO4 x 7 H2O                               0.10      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 89-89","quote":"MnCl2 x 4 H2O                               0.03      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 90-90","quote":"H3BO3                                       0.03      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.485123,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 91-91","quote":"CoCl2 x 6 H2O                               0.20      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 92-92","quote":"CuCl2 x 2 H2O                               0.03      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.175971,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 93-93","quote":"NiCl2 x 6 H2O                               0.03      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 94-94","quote":"Na2MoO4 x 2 H2O                             0.03      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Pfennig trace stock / Solution B, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q21","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Selenite-tungstate stock / Solution C","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 102-102","quote":"NaOH                                        0.50      g","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q22","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Selenite-tungstate stock / Solution C","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 103-103","quote":"Na2SeO3 x 5 H2O                             3.00     mg","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q23","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C.","source_stage":"Selenite-tungstate stock / Solution C","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 104-104","quote":"Na2WO4 x 2 H2O                              4.00     mg","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution C, and the primary batch mass agrees. Preserve that stock-stage strength as declared support, but correct its current unqualified main-ingredient placement. The primary explicitly states final medium volume1002ml; neither the source solution volume nor its g_l is already the completed-medium concentration. Restore the exact source dose and stage before any final-rate calculation. The stock table lists1000ml water and API declares stock volume1000ml; preserve that declared basis without inventing a separate measured stock make-up. Only1ml of this stock is received via B or C."}]},{"quantity_id":"q24","label":"Assembly dose Solution A","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-7","quote":"Solution A                                           950.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 3039,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q25","label":"Assembly dose Solution B","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 8-8","quote":"Solution B                                             1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 3040,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q26","label":"Assembly dose Solution C","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 9-9","quote":"Solution C                                             1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 3041,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q27","label":"Assembly dose Solution D","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 10-10","quote":"Solution D                                            10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 3042,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Assembly dose Solution E","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 11-11","quote":"Solution E                                            10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 3043,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q29","label":"Assembly dose Solution F","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 12-12","quote":"Solution F                                            10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 3044,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q30","label":"Assembly dose Solution G","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 13-13","quote":"Solution G                                            10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Solution G\",\n                        \"solution_id\": 3045,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q31","label":"Assembly dose Solution H","local_fields":[],"decision":"evidence_only","rationale":"Preserve this printed batch dose, its referenced solution and the completed1002ml declaration. Bare ml is an aliquot into this assembly, not an independently stated ml/L rate. B and C route the same1ml trace/SeW addition; their inner references are not an extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 14-14","quote":"Solution H                                            10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Solution H\",\n                        \"solution_id\": 3046,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q32","label":"Input water 1","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 33-33","quote":"Distilled water                                      950.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q33","label":"Input water 4","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 49-49","quote":"Distilled water                                       10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q34","label":"Input water 5","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 63-63","quote":"Distilled water                              10.00   ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[5].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"Input water 6","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 69-69","quote":"Distilled water                              10.00   ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[6].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"Input water 7","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 75-75","quote":"Distilled water                              10.00   ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[7].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Input water 8","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 81-81","quote":"Distilled water                              10.00   ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[8].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Input water 9","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 95-95","quote":"Distilled water                          1000.00     ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Input water 10","local_fields":[],"decision":"evidence_only","rationale":"Retain this water amount in its exact solution scope. Input water is distinct from an explicit final make-up; the completed-medium1002ml statement does not redefine each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 105-105","quote":"Distilled water                          1000.00     ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Nested stock reference 2","local_fields":[],"decision":"evidence_only","rationale":"Preserve the1ml nested stock identity under Solution B or C. The outer1ml dose and this defining inner aliquot describe the same stock path and must not be added twice.","source_stage":"Source-only nested stock identity","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 38-38","quote":"Trace elements solution (Pfennig, 1965)                 1.00      ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Trace elements solution (Pfennig, 1965)\",\n                        \"solution_id\": 2762,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"Nested stock reference 3","local_fields":[],"decision":"evidence_only","rationale":"Preserve the1ml nested stock identity under Solution B or C. The outer1ml dose and this defining inner aliquot describe the same stock path and must not be added twice.","source_stage":"Source-only nested stock identity","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 43-43","quote":"Selenite-tungstate solution                             1.00      ml","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q42","label":"Declared completed volume","local_fields":[],"decision":"evidence_only","rationale":"The primary explicitly states final volume1002ml, agreeing with the assembly doses950+1+1+5×10ml. This is source-declared final volume; it is not an independent measured-volume result.","source_stage":"Completed medium","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution H                                            10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q43","label":"Retained final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ph_range","stored":{"min":8.7,"max":9.0}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ph_range","stored":{"min":8.7,"max":9.0}}],"decision":"evidence_only","rationale":"The existing8.7–9.0 range is directly supported for the completed medium; preliminary solution A pH9.0 and trace-stock pH3.0–4.0 are separate stages.","source_stage":"Completed-medium pH","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 3-3","quote":"Final pH: 8.7 - 9.0","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 16-21","quote":"Dissolve ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 - 45\nmin to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0, dispense\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\nPrior to inoculation complete the medium by adding appropriate amounts of sterile\nsolutions B to H prepared under 100% N2 gas atmosphere. Adjust pH of the complete\nmedium to 8.7 - 9.0, if necessary.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The existing8.7–9.0 range is directly supported for the completed medium; preliminary solution A pH9.0 and trace-stock pH3.0–4.0 are separate stages."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The existing8.7–9.0 range is directly supported for the completed medium; preliminary solution A pH9.0 and trace-stock pH3.0–4.0 are separate stages."}]},{"quantity_id":"q44","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0, dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of sterile solutions B to H prepared under 100% N2 gas atmosphere. Adjust pH of the complete medium to 8.7 - 9.0, if necessary."}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0, dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of sterile solutions B to H prepared under 100% N2 gas atmosphere. Adjust pH of the complete medium to 8.7 - 9.0, if necessary."}}],"decision":"evidence_only","rationale":"The existing main text and AUTOCLAVE action preserve solution A carbonates/addition order,100%N2,30–45min,preliminarypH9,sterile B–H assembly and finalpH8.7–9.0. Retain these controls and stock identity links; no temperature or time for autoclaving is supplied.","source_stage":"Main preparation","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 16-21","quote":"Dissolve ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 - 45\nmin to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0, dispense\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\nPrior to inoculation complete the medium by adding appropriate amounts of sterile\nsolutions B to H prepared under 100% N2 gas atmosphere. Adjust pH of the complete\nmedium to 8.7 - 9.0, if necessary.","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0, dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of sterile solutions B to H prepared under 100% N2 gas atmosphere. Adjust pH of the complete medium to 8.7 - 9.0, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing main text and AUTOCLAVE action preserve solution A carbonates/addition order,100%N2,30–45min,preliminarypH9,sterile B–H assembly and finalpH8.7–9.0. Retain these controls and stock identity links; no temperature or time for autoclaving is supplied."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing main text and AUTOCLAVE action preserve solution A carbonates/addition order,100%N2,30–45min,preliminarypH9,sterile B–H assembly and finalpH8.7–9.0. Retain these controls and stock identity links; no temperature or time for autoclaving is supplied."}]},{"quantity_id":"q45","label":"Retained trace-stock pH text","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"pH 3.0-4.0"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"pH 3.0-4.0"}}],"decision":"correct","rationale":"The text pH3.0–4.0 is source-supported for Pfennig trace stock only. Correct its current main-step placement and MIX action to a stock-scoped pH control; do not lower completed-medium pH. The current classifier falls through to MIX for this bare pH phrase because it lacks an adjustment verb.","source_stage":"Pfennig trace-stock pH","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt lines 97-97","quote":"pH 3.0-4.0","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].steps[0]","quote":"{\n                        \"step\": \"pH 3.0-4.0\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The text pH3.0–4.0 is source-supported for Pfennig trace stock only. Correct its current main-step placement and MIX action to a stock-scoped pH control; do not lower completed-medium pH. The current classifier falls through to MIX for this bare pH phrase because it lacks an adjustment verb."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The text pH3.0–4.0 is source-supported for Pfennig trace stock only. Correct its current main-step placement and MIX action to a stock-scoped pH control; do not lower completed-medium pH. The current classifier falls through to MIX for this bare pH phrase because it lacks an adjustment verb."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:000952.

All asserted ontology objects were checked for current labels, formulas, hydrate and stereo scope. Catalogue synonyms and preferred rows were joined exactly; broad extra synonym mappings do not certify a different salt or hydrate. Exact rejected spellings can coexist with mapped equivalent names. Missing yeast secondary links are a bounded completeness follow-up, without inventing a new asserted identifier. Nickel is the confirmed supplied-form mismatch. EDTA acid, anhydrous sodium acetate, dipotassium hydrogen phosphate, formate and the other explicitly specified hydrates match the current scientific objects. No unused provider mmol_l conversion is certified.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:000952.

All three full reports and the selected66-claim October parent were read. Its23 old local fields and43 exact current API objects join, and the recorded raw digest equals the fresh response. The old blanket conflict correctly leaves stage remediation open, while current source evidence now credits all23 stock-stage rates. Singleton generation preserves maintained scientific content; historical import execution is not reconstructed.

## Findings

### f1: All23 stock-stage strengths are flattened into the main medium

major / open / confirmed; issue key: culturemech-000952-stock-stage.

Restore solution A and D–H, plus the B/C paths to their trace and selenite-tungstate stocks. All23 local numbers agree with exact provider stock g_l, but their current main placement loses receiving doses and the explicit1002ml completed-medium basis. Preserve supported source masses and use the complete source topology before deriving final rates. Current API parsing no longer flattens later sections, but a main table containing only references returns no API compound list, allowing PDF fallback or a placeholder; inspect that path before regeneration.

### f2: Trace-stock pH is represented as a main mixing step

major / open / confirmed; issue key: culturemech-000952-stock-preparation.

Retain the exact pH3.0–4.0 text, bind it to the Pfennig trace stock and use a stock-scoped pH action rather than MIX. Keep the supported main preparation and completed8.7–9.0 range unchanged. Current collection concatenates every solution step without labels, and the bare pH phrase falls through the classifier to MIX.

### f3: Nickel hexahydrate is asserted as anhydrous nickel dichloride

major / open / confirmed; issue key: culturemech-000952-nickel-form.

CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do not reject the whole identifier. Correct both actual asserted slots after checking the exact source form; retain its supported stock amount and stage.

### f4: Supported source claims lack attached evidence

minor / open / confirmed; issue key: culturemech-000952-claim-evidence.

Attach literal ingredient evidence for stock strengths and root evidence with exact field/stage scope for assembly doses, water, volume and pH. There are no attached claims now. Historical byte matches authenticate content separately from original retrieval events; do not create an evidence slot on concentration or solution descriptors.

## Recommended Actions And Acceptance Checks

### a1

Restore solution A and D–H, plus the B/C paths to their trace and selenite-tungstate stocks. All23 local numbers agree with exact provider stock g_l, but their current main placement loses receiving doses and the explicit1002ml completed-medium basis. Preserve supported source masses and use the complete source topology before deriving final rates. Current API parsing no longer flattens later sections, but a main table containing only references returns no API compound list, allowing PDF fallback or a placeholder; inspect that path before regeneration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Retain the exact pH3.0–4.0 text, bind it to the Pfennig trace stock and use a stock-scoped pH action rather than MIX. Keep the supported main preparation and completed8.7–9.0 range unchanged. Current collection concatenates every solution step without labels, and the bare pH phrase falls through the classifier to MIX.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do not reject the whole identifier. Correct both actual asserted slots after checking the exact source form; retain its supported stock amount and stage.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Attach literal ingredient evidence for stock strengths and root evidence with exact field/stage scope for assembly doses, water, volume and pH. There are no attached claims now. Historical byte matches authenticate content separately from original retrieval events; do not create an evidence slot on concentration or solution descriptors.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz1485 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf; REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api1485 | https://mediadive.dsmz.de/rest/medium/1485; REVIEW_WORK/batch077/source01-03-supplement/api1485.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch077/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-16 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/desulfonatronum_alkalitolerans_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch077/record01/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch077/record01/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch077/record01/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_composition_ingredients; _parse_api_composition; _is_api_stock_addition; _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps; _classify_preparation_action | context_only | Current composition parsing reads the first API solution only, skips water and explicit stock or percent-bearing ml references, and prioritizes supplied g_l. Solution parsing preserves the first-section stock references but normalizes bare ml to ML_PER_L. Preparation parsing concatenates every solution step without stage labels. For all-stock primary tables, API composition returns None and PDF fallback or a placeholder remains possible; no regeneration outcome is presumed. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| full-history-pool | REVIEW_WORK/batch077/validation-authors/full-history-pool.json; Complete artifact | context_only | All thirteen reports across these three records are losslessly routed through 619 exact cells; each selected record retains its own complete report reader. No neighboring formulation transfer. |
| full-catalog | REVIEW_WORK/batch077/validation-authors/mim-full-scope.json; Complete artifact | context_only | All exact asserted identifier/ontology_id and supplied-name catalogue joins, plus candidate nickel hexahydrate; preferred-label statuses are interpreted separately from chemical identity. |
| selected-parent-authentication | REVIEW_WORK/batch077/record01/selected-parent-authentication.json; Complete artifact | context_only | Exact selected parent objects, unchanged current local fields and all literal/decoded current API claims checked separately from attached evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch077/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch077/source01-03-supplement/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch077/source01-03-supplement/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch077/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch077/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch077/source01-03-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch077/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch077/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62965; REVIEW_WORK/batch077/source01-03-supplement/chebi62965.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch077/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:4735; REVIEW_WORK/batch077/source01-03-supplement/chebi4735.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch077/source01-03-supplement/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch077/source01-03-supplement/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch077/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch077/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch077/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch077/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch077/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch077/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch077/source01-03-supplement/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; REVIEW_WORK/batch077/source01-03-supplement/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; REVIEW_WORK/batch077/source01-03-supplement/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch077/record01/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch077/record01/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch077/record01/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch077/record01/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch077/record01/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch077/record01/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch077/record01/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch077/record01/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch077/record01/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch077/record01/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch077/record01/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch077/record01/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Scope is the exact printed DSM1485 formulation and its embedded stock definitions only. No organism-growth evidence or neighboring parent formulation is transferred.
- The primary explicitly declares1002ml final medium volume; stock table water remains an input and provider stock volumes are declared normalization bases. No molar recalculation is proposed.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T201844Z-culturemech-000952-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFONATRONUM ALKALITOLERANS MEDIUM'
started_at: '2026-10-28T20:15:09.132786Z'
finished_at: '2026-10-28T20:18:44.464248Z'
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
summary: DSM1485 preserves source stock strengths and main preparation, but all23
  stock-stage values are presented as main-medium concentrations. Restore A–H assembly
  and trace-stock pH scope, correct nickel-hydrate grounding, and attach exact field-level
  evidence.
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
  - path: data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
    sha256: 10473b7861aed1560f738f2bec0a1531125785ddf5b46a640d6e19ffe2d50a69
    role: target
  - path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
    sha256: 09fc038965ed48c39b0898a99bd2e8020cc76a64be21461a1f2cb6bd694a27c7
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/desulfonatronum_alkalitolerans_medium.yaml.md
    sha256: 5dbf23379e3b0042af31d7fb166a0417bc6d757261126ec873a2c083bba67d88
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.md
    sha256: 1f06c2ee1da2e34f5c87ef3a50ccea0d0b8660c34c6cccd84a8e3a2591febcad
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.md
    sha256: 0b7081bf1e5557b72d5bff5aaa0c7a7d67a0bdecffcfd765d867d2836c1e71bb
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
  selection: Authoritative batch077 index 01
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000952
targets:
- target_id: CultureMech:000952
  path: data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
  label: desulfonatronum_alkalitolerans_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:000952
  command: just validate-schema data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
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
  - CultureMech:000952
  command: just validate-strict data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
    --out REVIEW_WORK/batch077/record01/strict.tsv --workers 1 --quiet
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
  - CultureMech:000952
  command: just validate-terms data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
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
  - CultureMech:000952
  command: just validate-references data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz1485
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf
  accessed_at: '2026-10-28T20:15:33.090933Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c
- evidence_id: api1485
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1485
  accessed_at: '2026-10-28T20:15:32.952000Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/api1485.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258
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
  reference: data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:18:44.323005Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 10473b7861aed1560f738f2bec0a1531125785ddf5b46a640d6e19ffe2d50a69
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:18:44.323159Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 09fc038965ed48c39b0898a99bd2e8020cc76a64be21461a1f2cb6bd694a27c7
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T20:18:44.323185Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T20:18:44.323477Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T20:18:44.323499Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T20:18:44.323518Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-16
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:18:44.323541Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/desulfonatronum_alkalitolerans_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T20:18:44.329010Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 5dbf23379e3b0042af31d7fb166a0417bc6d757261126ec873a2c083bba67d88
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T20:18:44.329076Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 1f06c2ee1da2e34f5c87ef3a50ccea0d0b8660c34c6cccd84a8e3a2591febcad
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T20:18:44.329108Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 0b7081bf1e5557b72d5bff5aaa0c7a7d67a0bdecffcfd765d867d2836c1e71bb
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/historical-reading.json
  accessed_at: '2026-10-28T20:18:44.329138Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 57effb3987801d5accfd929f0d416a39abf2b57f0088f7d67a05da116892af75
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:18:44.329387Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: f133180760c999c4de07bdea2f61bfe70b1dac74b4dd8488eb84755a2b81454a
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/complete-document-reader.json
  accessed_at: '2026-10-28T20:18:44.329604Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 0520484bf22d1b629cc2e5a83371c6828b7d499ee0d3595f9167e9daaa510fe0
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_composition_ingredients; _parse_api_composition; _is_api_stock_addition;
    _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps;
    _classify_preparation_action
  accessed_at: '2026-10-28T20:18:44.329761Z'
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
  accessed_at: '2026-10-28T20:18:44.329805Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: full-history-pool
  kind: record_content
  reference: REVIEW_WORK/batch077/validation-authors/full-history-pool.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:18:44.329835Z'
  support: context_only
  summary: All thirteen reports across these three records are losslessly routed through
    619 exact cells; each selected record retains its own complete report reader.
    No neighboring formulation transfer.
  snapshot_sha256: 35d1e79d61d4d348a952a6faa00bfb1a397d30f96995ea913be0822f2024612e
- evidence_id: full-catalog
  kind: record_content
  reference: REVIEW_WORK/batch077/validation-authors/mim-full-scope.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:18:44.330065Z'
  support: context_only
  summary: All exact asserted identifier/ontology_id and supplied-name catalogue joins,
    plus candidate nickel hexahydrate; preferred-label statuses are interpreted separately
    from chemical identity.
  snapshot_sha256: 741b684f47194d97bb0a782ece7136465d7c31c2d1c94480aad6d3518ef55158
- evidence_id: selected-parent-authentication
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/selected-parent-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:18:44.373666Z'
  support: context_only
  summary: Exact selected parent objects, unchanged current local fields and all literal/decoded
    current API claims checked separately from attached evidence.
  snapshot_sha256: 31e964e769298d44af6388568a693fad068d5c60f28e020db7c57418b0cdaa5d
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
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T20:15:34.088710Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi131527.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T20:15:36.865259Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32139.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
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
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T20:15:37.622227Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32954.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
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
- evidence_id: chebi62965
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62965
  accessed_at: '2026-10-28T20:15:38.826774Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi62965.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cfd1c5de376b9874afbc0c231dfd94f0b4954f4b69c40062783876093e7f0354
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
- evidence_id: chebi4735
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:4735
  accessed_at: '2026-10-28T20:15:38.088911Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi4735.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cbb8a2d2fd80b7e771711746d09aee7aaf9a8ac2dabc853617c1c08b49db4908
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T20:15:39.423589Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi75836.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T20:15:37.216331Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32312.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
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
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462230Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 48fd1b8fe006dc1ec37f0fd41e821d5db10599250e38921f4f5a18427622b418
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462335Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 246ac4bd5236efffedd51b3af816dea6396cf05f7a19b3b333e919ee0388d0a2
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462435Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 2b872942a50f214624cbe99fe71c2c0d7f7a33e27116e6d862c1f728ae3fbce4
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462484Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 8f7688023735aabc2e13562a99b54b9a28e721fc0a7b3e6a65cff15fcae7cf2d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462531Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: e201d28ee493b4c3d712d77d6f36dda3f66c8f2c7dde38fa29fd4ac43ef2fe16
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462551Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 76e828035b92b902a598a2deb66461b9462d31d32f5566ed0f77cfef38951671
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:18:44.462569Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch077/record01/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T20:18:44.462587Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: 74657968f191f64be7935b58da8b90a1226106f9f942f34236a905804d3b1a8b
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch077/record01/validate-schema.json
  accessed_at: '2026-10-28T20:15:10.155760Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e19ae5c8d6f5d9a63acfe43132a3e4401f4e477bcb59f6ce7f6d0bba5467f28e
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch077/record01/validate-strict.json
  accessed_at: '2026-10-28T20:15:11.070971Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 98047e5683463097ba673373e8a7ff6dab5333add7ae7caf62593260b4d773c2
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch077/record01/validate-terms.json
  accessed_at: '2026-10-28T20:15:12.084044Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: cb7710ed20093f801530aa9d1eefece4eae1cf1f75d2cd2b2091b9e78c176c37
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch077/record01/validate-references.json
  accessed_at: '2026-10-28T20:15:12.806649Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 6648418fc05f5230a0c4d7950836499689a337f2dd380265723ebe9da4f3c46f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSM1485 source and owner
  outcome: supported
  summary: The selected generated record has one maintained DSM1485 contributor and
    all scientific fields match that owner. The current two-page primary and complete
    API are the exact accession. Referenced media1369/385 contribute only the printed
    trace and SeW definitions; their other formulations are excluded.
  target_ids:
  - CultureMech:000952
  evidence_ids:
  - target
  - owner
  - dsmz1485
  - api1485
- assessment_id: classification
  area: representation
  topic: Complex liquid medium
  outcome: supported
  summary: Yeast extract supports complex/undefined classification; no solidifier
    is specified. The high_metal flag is retained as qualitative metadata, not a quantified
    threshold or growth claim.
  target_ids:
  - CultureMech:000952
  evidence_ids:
  - target
  - dsmz1485
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 46 current concentration fields are covered by 45 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:000952
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b077-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","quantity_field_count":46,"decisions":[{"quantity_id":"q1","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"6.31579","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"6.31579","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 27-27","quote":"NaCl                                                   6.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6.31579,\n                        \"mmol_l\":
    108.073,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.05263","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.05263","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 28-28","quote":"K2HPO4                                                 1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.05263,\n                        \"mmol_l\":
    6.04349,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q3","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"33.6842","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"33.6842","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 29-29","quote":"NaHCO3                                                32.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 32,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 33.6842,\n                        \"mmol_l\":
    400.969,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q4","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"11.1579","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"11.1579","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 30-30","quote":"Na2CO3                                                10.60        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 10.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 11.1579,\n                        \"mmol_l\":
    105.275,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q5","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.94737","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"2.94737","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 31-31","quote":"Na2SO4                                                 2.80        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 2.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.94737,\n                        \"mmol_l\":
    20.7503,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q6","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.210526","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.210526","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 32-32","quote":"Na-acetate                                             0.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.210526,\n                        \"mmol_l\":
    2.56634,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution A, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. Solution A has950ml input water and is
    dosed as950ml into the final assembly; its provider rates use the950ml basis."}]},{"quantity_id":"q7","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution D, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot.","source_stage":"Solution D","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 48-48","quote":"NH4Cl                                                  0.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    373.902,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution D, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution D, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."}]},{"quantity_id":"q8","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution E, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot.","source_stage":"Solution E","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 62-62","quote":"MgCl2 x 6 H2O                                 0.20    g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[5].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    98.3753,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution E, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution E, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution F, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot.","source_stage":"Solution F","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 68-68","quote":"Yeast extract                                20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[6].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution F, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution F, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."}]},{"quantity_id":"q10","label":"Na-formate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"340","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"340","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution G, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot.","source_stage":"Solution G","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 74-74","quote":"Na-formate                                    3.40    g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[7].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\":
    144,\n                        \"amount\": 3.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 340,\n                        \"mmol_l\":
    4999.47,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution G, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution G, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."}]},{"quantity_id":"q11","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution H, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot.","source_stage":"Solution H","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 80-80","quote":"Na2S x 9 H2O                                  0.30    g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[8].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    124.905,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution H, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Solution H, and the primary
    batch mass agrees. Preserve that stock-stage strength as declared support, but
    correct its current unqualified main-ingredient placement. The primary explicitly
    states final medium volume1002ml; neither the source solution volume nor its g_l
    is already the completed-medium concentration. Restore the exact source dose and
    stage before any final-rate calculation. This single-component solution has10ml
    input water and a separate10ml receiving dose; the printed mass belongs to that
    aliquot."}]},{"quantity_id":"q12","label":"EDTA","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 86-86","quote":"EDTA                                        5.00      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\":
    271,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    17.1092,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q13","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 87-87","quote":"FeSO4 x 7 H2O                               2.20      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 2.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.2,\n                        \"mmol_l\":
    7.91324,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q14","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 88-88","quote":"ZnSO4 x 7 H2O                               0.10      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.347752,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 89-89","quote":"MnCl2 x 4 H2O                               0.03      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.151588,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 90-90","quote":"H3BO3                                       0.03      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.485123,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 91-91","quote":"CoCl2 x 6 H2O                               0.20      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.54037,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 92-92","quote":"CuCl2 x 2 H2O                               0.03      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.175971,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 93-93","quote":"NiCl2 x 6 H2O                               0.03      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Pfennig trace stock / Solution B","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 94-94","quote":"Na2MoO4 x 2 H2O                             0.03      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.123993,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Pfennig trace stock / Solution
    B, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q21","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Selenite-tungstate stock / Solution C","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 102-102","quote":"NaOH                                        0.50      g","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q22","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Selenite-tungstate stock / Solution C","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 103-103","quote":"Na2SeO3 x 5 H2O                             3.00     mg","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q23","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C.","source_stage":"Selenite-tungstate stock / Solution C","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 104-104","quote":"Na2WO4 x 2 H2O                              4.00     mg","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    local scalar exactly matches the provider g_l for Selenite-tungstate stock / Solution
    C, and the primary batch mass agrees. Preserve that stock-stage strength as declared
    support, but correct its current unqualified main-ingredient placement. The primary
    explicitly states final medium volume1002ml; neither the source solution volume
    nor its g_l is already the completed-medium concentration. Restore the exact source
    dose and stage before any final-rate calculation. The stock table lists1000ml
    water and API declares stock volume1000ml; preserve that declared basis without
    inventing a separate measured stock make-up. Only1ml of this stock is received
    via B or C."}]},{"quantity_id":"q24","label":"Assembly dose Solution A","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-7","quote":"Solution A                                           950.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    3039,\n                        \"amount\": 950,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q25","label":"Assembly
    dose Solution B","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 8-8","quote":"Solution B                                             1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    3040,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q26","label":"Assembly
    dose Solution C","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 9-9","quote":"Solution C                                             1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    3041,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q27","label":"Assembly
    dose Solution D","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 10-10","quote":"Solution D                                            10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    3042,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Assembly
    dose Solution E","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 11-11","quote":"Solution E                                            10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\":
    3043,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q29","label":"Assembly
    dose Solution F","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 12-12","quote":"Solution F                                            10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\":
    3044,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q30","label":"Assembly
    dose Solution G","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 13-13","quote":"Solution G                                            10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Solution G\",\n                        \"solution_id\":
    3045,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q31","label":"Assembly
    dose Solution H","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this printed batch dose, its referenced solution and the completed1002ml declaration.
    Bare ml is an aliquot into this assembly, not an independently stated ml/L rate.
    B and C route the same1ml trace/SeW addition; their inner references are not an
    extra second dose.","source_stage":"Source-only final assembly","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 14-14","quote":"Solution H                                            10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Solution H\",\n                        \"solution_id\":
    3046,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q32","label":"Input
    water 1","local_fields":[],"decision":"evidence_only","rationale":"Retain this
    water amount in its exact solution scope. Input water is distinct from an explicit
    final make-up; the completed-medium1002ml statement does not redefine each stock
    preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 33-33","quote":"Distilled water                                      950.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 950,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q33","label":"Input water 4","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 49-49","quote":"Distilled water                                       10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q34","label":"Input water 5","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 63-63","quote":"Distilled water                              10.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[5].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"Input water 6","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 69-69","quote":"Distilled water                              10.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[6].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"Input water 7","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 75-75","quote":"Distilled water                              10.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[7].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Input water 8","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 81-81","quote":"Distilled water                              10.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[8].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Input water 9","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 95-95","quote":"Distilled water                          1000.00     ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Input water 10","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this water amount in its exact solution scope. Input water is distinct from an
    explicit final make-up; the completed-medium1002ml statement does not redefine
    each stock preparation.","source_stage":"Source-only solution solvent","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 105-105","quote":"Distilled water                          1000.00     ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[10].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Nested stock reference
    2","local_fields":[],"decision":"evidence_only","rationale":"Preserve the1ml nested
    stock identity under Solution B or C. The outer1ml dose and this defining inner
    aliquot describe the same stock path and must not be added twice.","source_stage":"Source-only
    nested stock identity","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 38-38","quote":"Trace elements solution (Pfennig, 1965)                 1.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Trace elements solution (Pfennig,
    1965)\",\n                        \"solution_id\": 2762,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"Nested
    stock reference 3","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the1ml nested stock identity under Solution B or C. The outer1ml dose and this
    defining inner aliquot describe the same stock path and must not be added twice.","source_stage":"Source-only
    nested stock identity","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 43-43","quote":"Selenite-tungstate solution                             1.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q42","label":"Declared completed
    volume","local_fields":[],"decision":"evidence_only","rationale":"The primary
    explicitly states final volume1002ml, agreeing with the assembly doses950+1+1+5×10ml.
    This is source-declared final volume; it is not an independent measured-volume
    result.","source_stage":"Completed medium","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 4-4","quote":"Final volume: 1002 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 7-14","quote":"Solution A                                           950.00       ml\n   Solution
    B                                             1.00       ml\n   Solution C                                             1.00       ml\n   Solution
    D                                            10.00       ml\n   Solution E                                            10.00       ml\n   Solution
    F                                            10.00       ml\n   Solution G                                            10.00       ml\n   Solution
    H                                            10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q43","label":"Retained final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ph_range","stored":{"min":8.7,"max":9.0}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ph_range","stored":{"min":8.7,"max":9.0}}],"decision":"evidence_only","rationale":"The
    existing8.7–9.0 range is directly supported for the completed medium; preliminary
    solution A pH9.0 and trace-stock pH3.0–4.0 are separate stages.","source_stage":"Completed-medium
    pH","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 3-3","quote":"Final pH: 8.7 - 9.0","quote_basis":"derivative text"},{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 16-21","quote":"Dissolve ingredients of solution A except carbonates, sparge
    with 100% N2 gas for 30 - 45\nmin to make it anoxic, then add bicarbonate and
    carbonate, adjust pH to 9.0, dispense\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave.\nPrior to inoculation complete the medium
    by adding appropriate amounts of sterile\nsolutions B to H prepared under 100%
    N2 gas atmosphere. Adjust pH of the complete\nmedium to 8.7 - 9.0, if necessary.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    existing8.7–9.0 range is directly supported for the completed medium; preliminary
    solution A pH9.0 and trace-stock pH3.0–4.0 are separate stages."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    existing8.7–9.0 range is directly supported for the completed medium; preliminary
    solution A pH9.0 and trace-stock pH3.0–4.0 are separate stages."}]},{"quantity_id":"q44","label":"Retained
    main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 -
    45 min to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0,
    dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Prior to inoculation complete the medium by adding appropriate
    amounts of sterile solutions B to H prepared under 100% N2 gas atmosphere. Adjust
    pH of the complete medium to 8.7 - 9.0, if necessary."}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients of solution A except carbonates, sparge with 100% N2 gas for 30 -
    45 min to make it anoxic, then add bicarbonate and carbonate, adjust pH to 9.0,
    dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Prior to inoculation complete the medium by adding appropriate
    amounts of sterile solutions B to H prepared under 100% N2 gas atmosphere. Adjust
    pH of the complete medium to 8.7 - 9.0, if necessary."}}],"decision":"evidence_only","rationale":"The
    existing main text and AUTOCLAVE action preserve solution A carbonates/addition
    order,100%N2,30–45min,preliminarypH9,sterile B–H assembly and finalpH8.7–9.0.
    Retain these controls and stock identity links; no temperature or time for autoclaving
    is supplied.","source_stage":"Main preparation","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 16-21","quote":"Dissolve ingredients of solution A except carbonates, sparge
    with 100% N2 gas for 30 - 45\nmin to make it anoxic, then add bicarbonate and
    carbonate, adjust pH to 9.0, dispense\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave.\nPrior to inoculation complete the medium
    by adding appropriate amounts of sterile\nsolutions B to H prepared under 100%
    N2 gas atmosphere. Adjust pH of the complete\nmedium to 8.7 - 9.0, if necessary.","quote_basis":"derivative
    text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients of solution A except carbonates, sparge with 100% N2 gas
    for 30 - 45 min to make it anoxic, then add bicarbonate and carbonate, adjust
    pH to 9.0, dispense under same gas atmosphere into anoxic Hungate-type tubes or
    serum vials and autoclave. Prior to inoculation complete the medium by adding
    appropriate amounts of sterile solutions B to H prepared under 100% N2 gas atmosphere.
    Adjust pH of the complete medium to 8.7 - 9.0, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing main text and AUTOCLAVE action preserve solution A carbonates/addition
    order,100%N2,30–45min,preliminarypH9,sterile B–H assembly and finalpH8.7–9.0.
    Retain these controls and stock identity links; no temperature or time for autoclaving
    is supplied."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing main text and AUTOCLAVE action preserve solution A carbonates/addition
    order,100%N2,30–45min,preliminarypH9,sterile B–H assembly and finalpH8.7–9.0.
    Retain these controls and stock identity links; no temperature or time for autoclaving
    is supplied."}]},{"quantity_id":"q45","label":"Retained trace-stock pH text","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"pH
    3.0-4.0"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"pH
    3.0-4.0"}}],"decision":"correct","rationale":"The text pH3.0–4.0 is source-supported
    for Pfennig trace stock only. Correct its current main-step placement and MIX
    action to a stock-scoped pH control; do not lower completed-medium pH. The current
    classifier falls through to MIX for this bare pH phrase because it lacks an adjustment
    verb.","source_stage":"Pfennig trace-stock pH","sources":[{"evidence_id":"dsmz1485","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1485.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz1485.bin","raw_sha256":"fec925a8261f81eb504e47003d72e7fd1d1078c097f1c69a0f1b454fa189e28c","text_sha256":"978ec5a6ba5f83b44cce270ec58286fd7063f57c3d55b0ca155cfb868e2c2535","accessed_at":"2026-10-28T20:15:33.090933Z","locator":"dsmz1485.txt
    lines 97-97","quote":"pH 3.0-4.0","quote_basis":"derivative text"},{"evidence_id":"api1485","reference":"https://mediadive.dsmz.de/rest/medium/1485","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api1485.bin","raw_sha256":"75146ef7fba83990730adde985836982ce0d1f1001e175b435b0bbca218dc258","text_sha256":"05352fc3353b84d6fff7664ed9847ffb00a2abe4e87411e1ec8676375fd39b02","accessed_at":"2026-10-28T20:15:32.952000Z","locator":"data.solutions[9].steps[0]","quote":"{\n                        \"step\":
    \"pH 3.0-4.0\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    text pH3.0–4.0 is source-supported for Pfennig trace stock only. Correct its current
    main-step placement and MIX action to a stock-scoped pH control; do not lower
    completed-medium pH. The current classifier falls through to MIX for this bare
    pH phrase because it lacks an adjustment verb."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    text pH3.0–4.0 is source-supported for Pfennig trace stock only. Correct its current
    main-step placement and MIX action to a stock-scoped pH control; do not lower
    completed-medium pH. The current classifier falls through to MIX for this bare
    pH phrase because it lacks an adjustment verb."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONUM_ALKALITOLERANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml":null},"scope":"Every
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
    Nickel is the confirmed supplied-form mismatch. EDTA acid, anhydrous sodium acetate,
    dipotassium hydrogen phosphate, formate and the other explicitly specified hydrates
    match the current scientific objects. No unused provider mmol_l conversion is
    certified.
  target_ids:
  - CultureMech:000952
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All three full reports and the selected66-claim October parent were read.
    Its23 old local fields and43 exact current API objects join, and the recorded
    raw digest equals the fresh response. The old blanket conflict correctly leaves
    stage remediation open, while current source evidence now credits all23 stock-stage
    rates. Singleton generation preserves maintained scientific content; historical
    import execution is not reconstructed.
  target_ids:
  - CultureMech:000952
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
  issue_key: culturemech-000952-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: All23 stock-stage strengths are flattened into the main medium
  description: Restore solution A and D–H, plus the B/C paths to their trace and selenite-tungstate
    stocks. All23 local numbers agree with exact provider stock g_l, but their current
    main placement loses receiving doses and the explicit1002ml completed-medium basis.
    Preserve supported source masses and use the complete source topology before deriving
    final rates. Current API parsing no longer flattens later sections, but a main
    table containing only references returns no API compound list, allowing PDF fallback
    or a placeholder; inspect that path before regeneration.
  target_ids:
  - CultureMech:000952
  field_paths:
  - ingredients[*].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz1485
  - api1485
  - quantities
  - writer-mediadive
  rule_id: custom/stock-stage
  native_severity: P2
  normalization_reason: Exact source-specific quantity issue, normalized major. This
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
- finding_id: f2
  issue_key: culturemech-000952-stock-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Trace-stock pH is represented as a main mixing step
  description: Retain the exact pH3.0–4.0 text, bind it to the Pfennig trace stock
    and use a stock-scoped pH action rather than MIX. Keep the supported main preparation
    and completed8.7–9.0 range unchanged. Current collection concatenates every solution
    step without labels, and the bare pH phrase falls through the classifier to MIX.
  target_ids:
  - CultureMech:000952
  field_paths:
  - preparation_steps[1]
  - ph_range
  evidence_ids:
  - dsmz1485
  - api1485
  - quantities
  - writer-mediadive
  rule_id: custom/stock-preparation
  native_severity: P2
  normalization_reason: Exact source-specific completeness issue, normalized major.
    This custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
- finding_id: f3
  issue_key: culturemech-000952-nickel-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is asserted as anhydrous nickel dichloride
  description: CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies
    NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred
    row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O)
    is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do
    not reject the whole identifier. Correct both actual asserted slots after checking
    the exact source form; retain its supported stock amount and stage.
  target_ids:
  - CultureMech:000952
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz1485
  - api1485
  - chebi53542
  - groundings
  - mim
  - full-catalog
  rule_id: custom/nickel-form
  native_severity: P2
  normalization_reason: Exact source-specific grounding issue, normalized major. This
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-000952-claim-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Supported source claims lack attached evidence
  description: Attach literal ingredient evidence for stock strengths and root evidence
    with exact field/stage scope for assembly doses, water, volume and pH. There are
    no attached claims now. Historical byte matches authenticate content separately
    from original retrieval events; do not create an evidence slot on concentration
    or solution descriptors.
  target_ids:
  - CultureMech:000952
  field_paths:
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - old-claims
  - historical-source-joins
  - selected-parent-authentication
  - dsmz1485
  - api1485
  rule_id: custom/claim-evidence
  native_severity: P3
  normalization_reason: Exact source-specific completeness issue, normalized minor.
    This custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Restore solution A and D–H, plus the B/C paths to their trace and selenite-tungstate
    stocks. All23 local numbers agree with exact provider stock g_l, but their current
    main placement loses receiving doses and the explicit1002ml completed-medium basis.
    Preserve supported source masses and use the complete source topology before deriving
    final rates. Current API parsing no longer flattens later sections, but a main
    table containing only references returns no API compound list, allowing PDF fallback
    or a placeholder; inspect that path before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000952
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
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
  description: Retain the exact pH3.0–4.0 text, bind it to the Pfennig trace stock
    and use a stock-scoped pH action rather than MIX. Keep the supported main preparation
    and completed8.7–9.0 range unchanged. Current collection concatenates every solution
    step without labels, and the bare pH phrase falls through the classifier to MIX.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000952
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
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
  description: CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies
    NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred
    row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O)
    is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do
    not reject the whole identifier. Correct both actual asserted slots after checking
    the exact source form; retain its supported stock amount and stage.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000952
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
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
  description: Attach literal ingredient evidence for stock strengths and root evidence
    with exact field/stage scope for assembly doses, water, volume and pH. There are
    no attached claims now. Historical byte matches authenticate content separately
    from original retrieval events; do not create an evidence slot on concentration
    or solution descriptors.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000952
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_alkalitolerans_medium.yaml
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
- Scope is the exact printed DSM1485 formulation and its embedded stock definitions
  only. No organism-growth evidence or neighboring parent formulation is transferred.
- The primary explicitly declares1002ml final medium volume; stock table water remains
  an input and provider stock volumes are declared normalization bases. No molar recalculation
  is proposed.
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
