# Fresh scientific review: Bacillus Tusciae Medium

- Review: 20261028T040638Z-b054-record08
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:00:29.835081Z
- Finished UTC: 2026-10-28T04:06:38.627877Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM 369 hierarchy is identifiable, but preparation overrides, mg units, water stages, SL-6 containment and hydrate groundings need correction. Current owner water/Mg repairs and exact authenticated standalone-stock quantity evidence are credited; generated content remains stale.

## Scope And Provenance

Complete generated target and exact maintained owner; scoped dependencies expressly identified; current primary and ontology evidence separately captured.

Selection: Actual batch054 selection index08; fresh review after lost historical bundles, not reconstruction.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008975 | data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml | generated | bacillus_tusciae_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:008975 | Actual exit 0; original full streams and times retained. |
| Canonical strict | passed | True | CultureMech:008975 | Actual exit 0; original full streams and times retained. |
| Canonical terms | passed | True | CultureMech:008975 | Actual exit 0; original full streams and times retained. |
| Canonical references | passed | True | CultureMech:008975 | Actual exit 0; original full streams and times retained. |

## Scientific And Domain Assessments

### DSM 369 linked-source hierarchy

identity: supported. Targets: CultureMech:008975.

Exact target/owner identity is TOGO 2392/DSM 369. DSM 2912 identifies Kyrpidia tusciae, formerly Bacillus tusciae, riskgroup 1. The medium name is historical nomenclature, not a reason to rename or import unrelated strain claims.

### Every local quantity and scoped source condition

quantity: concern. Targets: CultureMech:008975.

41 exact local concentration fields covered by 33 stage-specific decisions; unchanged source-matched masses are retained with their denominator limits.

{"schema":"fresh-b054-scoped-quantity-inventory-v1","target":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","quantity_field_count":41,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1000.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"Restore distinct main and SL-6 water additions. The owner already repaired the duplicate sum from 2000 to1000, but both layers still use mass-concentration units. Each source water row is1000 mL in its own batch; do not sum or infer density.","source_stage":"main water","source_amount":1000,"source_unit":"mL","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 14-14","quote":"Distilled water                                               1000.00      ml"}]},{"quantity_id":"q2","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric mass and supplied salt match the primary batch table. Retain the mass, but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main batch","source_amount":"0.2","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 8-8","quote":"MgSO4 x 7 H2O                                                    0.20       g"}]},{"quantity_id":"q3","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric mass and supplied salt match the primary batch table. Retain the mass, but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main batch","source_amount":"0.01","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 9-9","quote":"CaCl2 x 2 H2O                                                    0.01       g"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric mass and supplied salt match the primary batch table. Retain the mass, but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main batch","source_amount":"1.5","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 5-5","quote":"KH2PO4                                                           1.50       g"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric mass and supplied salt match the primary batch table. Retain the mass, but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main batch","source_amount":"1","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 6-6","quote":"NH4Cl                                                            1.00       g"}]},{"quantity_id":"q6","label":"MnSO4 x H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric mass and supplied salt match the primary batch table. Retain the mass, but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main batch","source_amount":"0.01","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 7-7","quote":"MnSO4 x H2O                                                      0.01       g"}]},{"quantity_id":"q7","label":"Ferric ammonium citrate","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies 5 mg, whereas both local layers encode 5 G_PER_L. Correct the 1000-fold mg-versus-g transcription while separately preserving the listed-batch basis; do not assert 0.005 g/L as a measured final-medium rate.","source_stage":"main batch","source_amount":5,"source_unit":"mg","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 10-10","quote":"Ferric ammonium citrate                                          5.00      mg"}]},{"quantity_id":"q8","label":"Na2HPO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric mass and supplied salt match the primary batch table. Retain the mass, but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main batch","source_amount":"4.5","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 4-4","quote":"Na2HPO4 x 2 H2O                                                  4.50       g"}]},{"quantity_id":"q9","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.03","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 32-32","quote":"Na2MoO4 x 2 H2O                                              0.03        g"}]},{"quantity_id":"q10","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.3","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 28-28","quote":"H3BO3                                                        0.30        g"}]},{"quantity_id":"q11","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.03","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 27-27","quote":"MnCl2 x 4 H2O                                                0.03        g"}]},{"quantity_id":"q12","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.2","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 29-29","quote":"CoCl2 x 6 H2O                                                0.20        g"}]},{"quantity_id":"q13","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.02","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 31-31","quote":"NiCl2 x 6 H2O                                                0.02        g"}]},{"quantity_id":"q14","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.1","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 26-26","quote":"ZnSO4 x 7 H2O                                                0.10        g"}]},{"quantity_id":"q15","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the SL-6 stock and must not appear as an undiluted main-medium concentration. Retain exact stock batch mass and separately link the 3 mL stock addition; provider-declared stock g/L is independently supported only in solution 25.","source_stage":"SL-6 stock","source_amount":"0.01","source_unit":"g","denominator":"listed 1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt lines 30-30","quote":"CuCl2 x 2 H2O                                                0.01        g"}]},{"quantity_id":"q16","label":"SL-6 receiving dose","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"Replace mass-concentration encoding with the literal 3 mL stock addition per stated batch; distinguish this dose from stock composition and from a measured final-litre rate.","source_stage":"main receiving dose","source_amount":3,"source_unit":"mL","denominator":"listed 1000 mL main water","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 11-12","quote":"Trace element solution SL-6                                      3.00      ml\n(see medium 27)"}]},{"quantity_id":"q17","label":"Standalone SL-6 ZnSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.1,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\": 35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\": \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.347752,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q18","label":"Standalone SL-6 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[1].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.03,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.151588,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q19","label":"Standalone SL-6 H3BO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[2].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.3,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[2]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.3,\n                \"unit\": \"g\",\n                \"g_l\": 0.3,\n                \"mmol_l\": 4.85123,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q20","label":"Standalone SL-6 CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.2,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[3]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.54037,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q21","label":"Standalone SL-6 CuCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[4].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.01,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[4]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\": \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0586569,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q22","label":"Standalone SL-6 NiCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[5].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.02,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[5]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\": \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.154322,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q23","label":"Standalone SL-6 Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[6].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current exact provider bytes authenticate the attached claim and provider-declared stock g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone SL-6","source_amount":0.03,"source_unit":"g","denominator":"provider-declared stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[6]","quote":"{\n                \"recipe_order\": 7,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.123993,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q24","label":"Standalone SL-6 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[7].concentration","stored":{"value":"1","unit":"L"}}],"decision":"evidence_only","rationale":"Current provider 1000 mL water supports the existing 1 L batch-volume conversion; no percent or density inference.","source_stage":"standalone SL-6","source_amount":1000,"source_unit":"ml","denominator":"stock batch water","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[7]","quote":"{\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }"}]},{"quantity_id":"q25","label":"Standalone stale placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Variable placeholder is not an actual ingredient. Current complete composition supports removing the stale placeholder and reassessing incomplete_composition flag, without inventing a quantity.","source_stage":"representation","source_amount":null,"source_unit":null,"denominator":null,"sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","text_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"solution25.txt lines 5-8","quote":"\"id\": 25,\n        \"name\": \"Trace element solution SL-6\",\n        \"volume\": 1000,\n        \"recipe\": ["}]},{"quantity_id":"q26","label":"Final medium pH","local_fields":[],"decision":"add","rationale":"Use the 369 override 4.0; TOGO meta.ph7.1 reflects the parent and must not replace the explicit override.","source_stage":"369 preparation","source_amount":4.0,"source_unit":"pH","denominator":null,"sources":[{"evidence_id":"dsm369","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf","raw_sha256":"cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade","text_sha256":"fdd76ede31e2e67d8fe56b24a75ee4e2c09b67936cd7074ce13f49cc45691536","locator":"dsm369.txt lines 4-4","quote":"Adjust medium 261 to pH 4.0."}]},{"quantity_id":"q27","label":"Incubation temperature","local_fields":[],"decision":"add","rationale":"369 overrides the 261/26065 °C condition with 50 °C; do not retain both as equivalent conditions.","source_stage":"369 incubation","source_amount":50,"source_unit":"degC","denominator":null,"sources":[{"evidence_id":"dsm369","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf","raw_sha256":"cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade","text_sha256":"fdd76ede31e2e67d8fe56b24a75ee4e2c09b67936cd7074ce13f49cc45691536","locator":"dsm369.txt lines 5-5","quote":"Incubate at 50C without agitation under 5% O2, 10% CO2, 45% H2 (v/v)."}]},{"quantity_id":"q28","label":"Gas fractions and no agitation","local_fields":[],"decision":"add","rationale":"Retain 5% O2, 10% CO2, 45% H2(v/v) and no agitation. Fractions total 60%; missing balance is unstated and must remain unresolved, never filled with guessed nitrogen/air.","source_stage":"369 incubation","source_amount":"5/10/45","source_unit":"percent v/v","denominator":"gas total incomplete","sources":[{"evidence_id":"dsm369","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf","raw_sha256":"cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade","text_sha256":"fdd76ede31e2e67d8fe56b24a75ee4e2c09b67936cd7074ce13f49cc45691536","locator":"dsm369.txt lines 5-5","quote":"Incubate at 50C without agitation under 5% O2, 10% CO2, 45% H2 (v/v)."}]},{"quantity_id":"q29","label":"Pyruvate exclusion","local_fields":[],"decision":"not_quantified","rationale":"261 explicitly excludes 260 pyruvate. Retain its absence; do not import the parent 1.50 g row.","source_stage":"261 override","source_amount":null,"source_unit":null,"denominator":null,"sources":[{"evidence_id":"dsm261","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium261.pdf","raw_sha256":"abea799d50da431e0446e012179e4ef6144c6f239cc8db830e33abafbcf33596","text_sha256":"01c1b230c54f9270f8d70a3a65fe0557c62dfe64bee2ff64a7731d738b0d1753","locator":"dsm261.txt lines 5-6","quote":"Use medium 260 without pyruvate. Incubate at 65C without agitation under 5% (v/v)\nO2, 10% CO2, 45% H2."}]},{"quantity_id":"q30","label":"Parent pH and temperature","local_fields":[],"decision":"conflict","rationale":"Parent pH7.1 and 65 °C are superseded by369, not alternative targets. Other uncontradicted preparation steps remain scoped to the inherited base.","source_stage":"parent override","source_amount":null,"source_unit":null,"denominator":null,"sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 16-18","quote":"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in\nErlenmeyer flasks and sterilize for 15 minutes at 121C. Incubate without agitation at\n65C."}]},{"quantity_id":"q31","label":"Optional agar","local_fields":[],"decision":"add","rationale":"15 g agar is an optional solid variant. Do not make it mandatory or silently change the selected liquid recipe.","source_stage":"optional solid variant","source_amount":15,"source_unit":"g","denominator":"listed batch","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 16-16","quote":"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in"}]},{"quantity_id":"q32","label":"Dispensed volume","local_fields":[],"decision":"add","rationale":"Preserve 30–50 mL distribution into Erlenmeyer flasks as an inherited preparation instruction, not the final batch denominator.","source_stage":"dispensing","source_amount":"30–50","source_unit":"mL","denominator":null,"sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 16-17","quote":"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in 30 - 50 ml amounts in\nErlenmeyer flasks and sterilize for 15 minutes at 121C. Incubate without agitation at"}]},{"quantity_id":"q33","label":"Sterilization","local_fields":[],"decision":"add","rationale":"Retain 15 minutes at121 °C from the inherited base; do not transfer DSM 27 main-medium sterilization or illumination protocol.","source_stage":"sterilization","source_amount":"15 at121","source_unit":"min/degC","denominator":null,"sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt lines 17-17","quote":"Erlenmeyer flasks and sterilize for 15 minutes at 121C. Incubate without agitation at"}]}],"limits":["A listed water amount is not an explicit measured final volume. Stock-local amounts are not receiving-medium rates.","Source-only rows/conditions are explicit; no density assumptions or invented missing gas balance."]}

### Chemical identity, canonical labels and packaged MIM

grounding: concern. Targets: CultureMech:008975.

All asserted CHEBI objects were retrieved directly and exact labels compared; supplied-form exceptions are described individually. Packaged MIM membership or label agreement alone is not chemical verification.

### Category, composition and physical-state scope

representation: concern. Targets: CultureMech:008975.

Bacterial/liquid scope is consistent with the selected optional-agar-free variant. Ferric ammonium citrate is an indefinite mixture, so do not force chemically defined classification solely from named salts. DSM 27 bulk formulation and phototrophic conditions are excluded.

### Current repairs and historical review limits

provenance: supported. Targets: CultureMech:008975.

Complete current target/owner history and selected September report were read. Existing repair credit is retained; current writer bodies describe current behavior only. No lost 451–520 bundle is reconstructed or backdated.

## Findings

### f1: The369 override and source-stage preparation are missing

major / open / confirmed; issue key: b054-08-f1.

Preserve pH4.0, 50 °C and the quoted no-agitation/gas condition from 369, pyruvate exclusion from 261, and the scoped inherited base preparation. The gas fractions total 60%; no unstated balance may be inferred. TOGO metadata 7.1 is a parent conflict, not an alternative authoritative pH.

### f2: SL-6 stock components were flattened into main ingredients

major / open / confirmed; issue key: b054-08-f2.

Seven trace salts appear at stock strength as main ingredients while solutions[0] also adds SL-6 using 3 G_PER_L. Represent the 3 mL batch dose separately and keep stock components in the linked/nested stock, with no unsupported receiving-medium concentration.

### f3: Ferric ammonium citrate has a mg-to-g transcription error

major / open / confirmed; issue key: b054-08-f3.

Both local layers encode 5 G_PER_L while DSM 260 and TOGO specify 5 mg per batch. Correct the mass scale and retain denominator uncertainty separately; an exact final-volume rate is not established.

### f4: Water units and generated duplicate state remain wrong

major / open / confirmed; issue key: b054-08-f4.

The owner already collapsed identical duplicate water to1000, but the generated target retains 2000. Neither G_PER_L value represents the separate 1000 mL main and stock water doses. Preserve repair credit, restore stage-local volumes and regenerate.

### f5: Magnesium secondary and nickel primary/secondary terms do not match hydrates

major / open / confirmed; issue key: b054-08-f5.

Primary Mg heptahydrate 31795 is already repaired; secondary 32599 is still generic. Ni hexahydrate is linked to anhydrous 34887 in both main layers and dependency composition[5].chebi_term. OLS53542 verifies the hexahydrate candidate. Co53503 is chemically correct despite a REJECTED preferred-label row coexisting with a MAPPED alias in the packaged CSV.

### f6: Source-matched batch masses and stock representation need bounded evidence

major / open / confirmed; issue key: b054-08-f6.

The remaining main masses match DSM 260, but current G_PER_L units lack an explicit final-volume basis. Solution 25 rates are provider-declared and can be retained within that stock; the current returned raw matches all eight attached claim hashes/snippets. Its old access timestamp is still a historical claim.

### f7: The standalone complete stock still carries placeholder/flag and unvetted provider molarity

minor / open / confirmed; issue key: b054-08-f7.

Solution 25 composition is now complete, yet ingredients[0] says See source for composition and incomplete_composition remains. Provider Co/Ni mmol_l values use anhydrous mass scales inconsistent with named hexahydrates; do not promote these contextual numbers into the local stock. Existing g_l quantities remain independently supported.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained source for: The369 override and source-stage preparation are missing. Preserve pH4.0, 50 °C and the quoted no-agitation/gas condition from 369, pyruvate exclusion from 261, and the scoped inherited base preparation. The gas fractions total 60%; no unstated balance may be inferred. TOGO metadata 7.1 is a parent conflict, not an alternative authoritative pH.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a2

Correct the maintained source for: SL-6 stock components were flattened into main ingredients. Seven trace salts appear at stock strength as main ingredients while solutions[0] also adds SL-6 using 3 G_PER_L. Represent the 3 mL batch dose separately and keep stock components in the linked/nested stock, with no unsupported receiving-medium concentration.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a3

Correct the maintained source for: Ferric ammonium citrate has a mg-to-g transcription error. Both local layers encode 5 G_PER_L while DSM 260 and TOGO specify 5 mg per batch. Correct the mass scale and retain denominator uncertainty separately; an exact final-volume rate is not established.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a4

Correct the maintained source for: Water units and generated duplicate state remain wrong. The owner already collapsed identical duplicate water to1000, but the generated target retains 2000. Neither G_PER_L value represents the separate 1000 mL main and stock water doses. Preserve repair credit, restore stage-local volumes and regenerate.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a5

Correct the maintained source for: Magnesium secondary and nickel primary/secondary terms do not match hydrates. Primary Mg heptahydrate 31795 is already repaired; secondary 32599 is still generic. Ni hexahydrate is linked to anhydrous 34887 in both main layers and dependency composition[5].chebi_term. OLS53542 verifies the hexahydrate candidate. Co53503 is chemically correct despite a REJECTED preferred-label row coexisting with a MAPPED alias in the packaged CSV.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a6

Correct the maintained source for: Source-matched batch masses and stock representation need bounded evidence. The remaining main masses match DSM 260, but current G_PER_L units lack an explicit final-volume basis. Solution 25 rates are provider-declared and can be retained within that stock; the current returned raw matches all eight attached claim hashes/snippets. Its old access timestamp is still a historical claim.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a7

Correct the maintained source for: The standalone complete stock still carries placeholder/flag and unvetted provider molarity. Solution 25 composition is now complete, yet ingredients[0] says See source for composition and incomplete_composition remains. Provider Co/Ni mmol_l values use anhydrous mass scales inconsistent with named hexahydrates; do not promote these contextual numbers into the local stock. Existing g_l quantities remain independently supported.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togo2392 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2392; Exact raw and derivative text at sources/togo2392.raw and .txt; metadata togo2392.json | context_only | Exact linked TOGO provider transcription, not automatic override of primary |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31604; Exact raw and derivative text at sources/chebi31604.raw and .txt; metadata chebi31604.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91258; Exact raw and derivative text at sources/chebi91258.raw and .txt; metadata chebi91258.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; Exact raw and derivative text at sources/chebi15377.raw and .txt; metadata chebi15377.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; Exact raw and derivative text at sources/chebi31795.raw and .txt; metadata chebi31795.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; Exact raw and derivative text at sources/chebi86158.raw and .txt; metadata chebi86158.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; Exact raw and derivative text at sources/chebi86318.raw and .txt; metadata chebi86318.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364; Exact raw and derivative text at sources/chebi86364.raw and .txt; metadata chebi86364.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32599; Exact raw and derivative text at sources/chebi32599.raw and .txt; metadata chebi32599.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; Exact raw and derivative text at sources/chebi86368.raw and .txt; metadata chebi86368.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; Exact raw and derivative text at sources/chebi75213.raw and .txt; metadata chebi75213.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; Exact raw and derivative text at sources/chebi63036.raw and .txt; metadata chebi63036.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| dsm2912 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-2912; Exact raw and derivative text at sources/dsm2912.raw and .txt; metadata dsm2912.json | context_only | Identity and risk group only; exact catalogue association separate from record evidence |
| dsm369 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf; Exact raw and derivative text at sources/dsm369.raw and .txt; metadata dsm369.json | context_only | 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers |
| dsm27 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf; Exact raw and derivative text at sources/dsm27.raw and .txt; metadata dsm27.json | context_only | 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers |
| dsm261 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium261.pdf; Exact raw and derivative text at sources/dsm261.raw and .txt; metadata dsm261.json | context_only | 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers |
| solution25 | https://mediadive.dsmz.de/rest/solution/25; Exact raw and derivative text at sources/solution25.raw and .txt; metadata solution25.json | context_only | Provider stock composition/IDs and declared rates; no receiving-medium transfer |
| dsm260 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf; Exact raw and derivative text at sources/dsm260.raw and .txt; metadata dsm260.json | context_only | 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; Exact raw and derivative text at sources/chebi31206.raw and .txt; metadata chebi31206.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; Exact raw and derivative text at sources/chebi32312.raw and .txt; metadata chebi32312.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; Exact raw and derivative text at sources/chebi53542.raw and .txt; metadata chebi53542.json | context_only | Candidate nickel hexahydrate identity only; not concentration or preparation evidence |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; Exact raw and derivative text at sources/chebi53503.raw and .txt; metadata chebi53503.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; Exact raw and derivative text at sources/chebi34887.raw and .txt; metadata chebi34887.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; Exact raw and derivative text at sources/chebi33118.raw and .txt; metadata chebi33118.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| current | data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml; full target and owner; exact byte hashes in native source.inputs | context_only | Current target and exact maintained owner, including complete history and evidence. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; all9077rows; source commit/hash in adjacent metadata | context_only | Packaged MIM CSV only, exact row and key joins; MAPPED and REJECTED entries distinguished. No assertion about current remote release. |
| importer | src/culturemech/import/togo_importer.py; _ingredient_from_item; _extract_primary_components; _solution_from_item; _parse_unit; _convert_to_culturemech | context_only | Current TOGO importer preserves recognized primary sections and separate stocks, but bare g/ml values still map to per-litre enums and fallback/default paths exist. Current code is not proof of historical execution. |
| merger | src/culturemech/merge/formulation.py; formulation_content and merge_formulation_evidence; inspected merger.merge_group | context_only | Current formulation comparison requires exact scientific-field equality and merger rejects incompatible multi-source formulations; singleton publication still needs regeneration after owner changes. |
| prior | reports/yaml_record_review/20260921T180956Z-Bacillus_Tusciae_Medium.md; full report; exact target path in header | context_only | Fully read September narrative review of this exact target; derivative historical opinion only. Its command successes are not reused and its final-volume/merge inferences are independently reassessed. |
| sl6-owner | data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml; composition[0:8], all evidence and history; ingredients[0] placeholder | context_only | Complete current standalone solution 25, all eight composition claims, provider IDs, history, stale placeholder and quality flag; no main-medium conditions transfer. |
| water-repair | scripts/repair_merged_duplicates.py; repair_ingredient, repair_record | context_only | Current duplicate repair collapses only identical numeric parts and preserves a new history event; it does not authenticate volume units or stock separation. |
| mg-repair | scripts/migrate_mgso4_heptahydrate_term.py; iter_ingredients and main | context_only | Current MgSO4-heptahydrate writer changes primary term only when the supplied name explicitly denotes seven waters; secondary slots are outside that writer. |
| quantity-sidecar | REVIEW_WORK/batch054/record08/quantity-inventory.json; All decisions and exact local/source locators | supports | Complete scoped quantity decisions, including unchanged and unsupported claims. |
| grounding-sidecar | REVIEW_WORK/batch054/record08/grounding-inventory.json; slots, ontology_objects and exact CSV row pool | supports | Exact returned OLS objects and all asserted chemical slots, with literal label correspondence separate from supplied-form decisions. |
| check-schema | REVIEW_WORK/batch054/record08/schema-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh schema canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |
| check-strict | REVIEW_WORK/batch054/record08/strict-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh strict canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |
| check-terms | REVIEW_WORK/batch054/record08/terms-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh terms canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |
| check-references | REVIEW_WORK/batch054/record08/references-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh references canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |

## Limits And Additional Notes

- DSM 27 is read fully but only its SL-6 subsection applies. Parent medium 27 ingredients, light regime and receiving dose do not transfer.
- SL-6 current same-byte raw authenticates all eight attached claims. The current retrieval does not independently verify their historical access timestamp.
- No final-medium molarity is calculated. Provider Co/Ni mmol_l values are suspect hydrate conversions; no unsupported replacement claim is silently adopted.
- The September report is derivative historical context; its old validations and source access times are not used as current verification.
- Packaged MIM CSV observations apply only to commit 6643131b0f12ab40b66f98135245fca04027e0e9; no global absence or live MIM claim.
- No experiment, growth optimization or universal strain applicability is inferred; catalog identity examples are not automatically inserted as target_organisms.
- Canonical reference validation inspected zero references in the generated target; scientific source authentication is supplied separately here.
- Source recipes list batch amounts unless an explicit concentration/final-volume statement is quoted. No silent normalization based solely on listed water.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T040638Z-b054-record08
kind: record
repository: CultureBotAI/CultureMech
title: 'Fresh scientific review: Bacillus Tusciae Medium'
started_at: '2026-10-28T04:00:29.835081Z'
finished_at: '2026-10-28T04:06:38.627877Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Fresh review of maintained records not authored or modified
    by this reviewer; old narrative reports treated only as derivative context.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: DSM 369 hierarchy is identifiable, but preparation overrides, mg units, water
  stages, SL-6 containment and hydrate groundings need correction. Current owner water/Mg
  repairs and exact authenticated standalone-stock quantity evidence are credited;
  generated content remains stale.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
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
  - path: data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
    sha256: 884c31c753abfa7fd5de117460964a7bff945de2d887273de1c5635685393599
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    sha256: 1ca9739b4db881def3d566ed3c0a4b1ad3f72391ab01e69a0ae697584241260a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    sha256: bcf1021fe1ddfe3465a791093ff7f36ad1dbf687017dd085638e82026174c9ce
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
  - path: reports/yaml_record_review/20260921T180956Z-Bacillus_Tusciae_Medium.md
    sha256: 7f1886ea8458132239c129dafe0afd10dc2da63bfaf78ff89ac71025d90d7b07
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
scope:
  description: Complete generated target and exact maintained owner; scoped dependencies
    expressly identified; current primary and ontology evidence separately captured.
  selection: Actual batch054 selection index08; fresh review after lost historical
    bundles, not reconstruction.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008975
targets:
- target_id: CultureMech:008975
  path: data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
  label: bacillus_tusciae_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  ownership_note: Exact single maintained owner from current identity and merged_from;
    generated target must be regenerated after owner curation.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008975
  command: just validate-schema data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008975
  command: just validate-strict data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
    --out REVIEW_WORK/batch054/record08/strict.tsv --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008975
  command: just validate-terms data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008975
  command: just validate-references data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togo2392
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2392
  locator: Exact raw and derivative text at sources/togo2392.raw and .txt; metadata
    togo2392.json
  accessed_at: '2026-10-28T04:01:22.470638Z'
  support: context_only
  summary: Exact linked TOGO provider transcription, not automatic override of primary
  snapshot_sha256: 78bc93d959831e2a7ba144b3bd52afea5c135cce0b91a537698f36125b492034
- evidence_id: chebi31604
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31604
  locator: Exact raw and derivative text at sources/chebi31604.raw and .txt; metadata
    chebi31604.json
  accessed_at: '2026-10-28T04:01:28.735964Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 9ac454bf22a0708ecbcc45cfd84abffb1d2b6531edec2a1197e082d34ba51bc9
- evidence_id: chebi91258
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91258
  locator: Exact raw and derivative text at sources/chebi91258.raw and .txt; metadata
    chebi91258.json
  accessed_at: '2026-10-28T04:01:32.356780Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: e14e1a91519d14765d91d25ca145a56376d176814c62df304f78116dd4ad9278
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  locator: Exact raw and derivative text at sources/chebi15377.raw and .txt; metadata
    chebi15377.json
  accessed_at: '2026-10-28T04:01:28.539162Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  locator: Exact raw and derivative text at sources/chebi31795.raw and .txt; metadata
    chebi31795.json
  accessed_at: '2026-10-28T04:01:29.329736Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  locator: Exact raw and derivative text at sources/chebi86158.raw and .txt; metadata
    chebi86158.json
  accessed_at: '2026-10-28T04:01:31.204462Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  locator: Exact raw and derivative text at sources/chebi86318.raw and .txt; metadata
    chebi86318.json
  accessed_at: '2026-10-28T04:01:31.627204Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364
  locator: Exact raw and derivative text at sources/chebi86364.raw and .txt; metadata
    chebi86364.json
  accessed_at: '2026-10-28T04:01:31.749829Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 6e685ea7654bc1f4e16b3e3a05d73d8541e84cddcc28de59c4ae57ac288a1505
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32599
  locator: Exact raw and derivative text at sources/chebi32599.raw and .txt; metadata
    chebi32599.json
  accessed_at: '2026-10-28T04:01:29.650478Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: c8381bae86c49daf20fe2a395973680caf47e14623523c0b3c8695aff7dd8f1c
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  locator: Exact raw and derivative text at sources/chebi86368.raw and .txt; metadata
    chebi86368.json
  accessed_at: '2026-10-28T04:01:31.976048Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  locator: Exact raw and derivative text at sources/chebi75213.raw and .txt; metadata
    chebi75213.json
  accessed_at: '2026-10-28T04:01:30.984275Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  locator: Exact raw and derivative text at sources/chebi63036.raw and .txt; metadata
    chebi63036.json
  accessed_at: '2026-10-28T04:01:30.901923Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: dsm2912
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-2912
  locator: Exact raw and derivative text at sources/dsm2912.raw and .txt; metadata
    dsm2912.json
  accessed_at: '2026-10-28T04:01:24.880226Z'
  support: context_only
  summary: Identity and risk group only; exact catalogue association separate from
    record evidence
  snapshot_sha256: c65a12444b92abcf52f5f4526c751797d52a55afd5f1945875bf4ded6c273ec2
- evidence_id: dsm369
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf
  locator: Exact raw and derivative text at sources/dsm369.raw and .txt; metadata
    dsm369.json
  accessed_at: '2026-10-28T04:01:23.399207Z'
  support: context_only
  summary: 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers
  snapshot_sha256: cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade
- evidence_id: dsm27
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf
  locator: Exact raw and derivative text at sources/dsm27.raw and .txt; metadata dsm27.json
  accessed_at: '2026-10-28T04:01:24.462819Z'
  support: context_only
  summary: 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers
  snapshot_sha256: e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9
- evidence_id: dsm261
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium261.pdf
  locator: Exact raw and derivative text at sources/dsm261.raw and .txt; metadata
    dsm261.json
  accessed_at: '2026-10-28T04:01:23.650519Z'
  support: context_only
  summary: 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers
  snapshot_sha256: abea799d50da431e0446e012179e4ef6144c6f239cc8db830e33abafbcf33596
- evidence_id: solution25
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/25
  locator: Exact raw and derivative text at sources/solution25.raw and .txt; metadata
    solution25.json
  accessed_at: '2026-10-28T04:01:25.044227Z'
  support: context_only
  summary: Provider stock composition/IDs and declared rates; no receiving-medium
    transfer
  snapshot_sha256: eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c
- evidence_id: dsm260
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf
  locator: Exact raw and derivative text at sources/dsm260.raw and .txt; metadata
    dsm260.json
  accessed_at: '2026-10-28T04:01:24.152383Z'
  support: context_only
  summary: 369 overrides 261;261 excludes 260 pyruvate;27 only SL6 subsection transfers
  snapshot_sha256: ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  locator: Exact raw and derivative text at sources/chebi31206.raw and .txt; metadata
    chebi31206.json
  accessed_at: '2026-10-28T04:01:28.685278Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  locator: Exact raw and derivative text at sources/chebi32312.raw and .txt; metadata
    chebi32312.json
  accessed_at: '2026-10-28T04:01:29.562773Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  locator: Exact raw and derivative text at sources/chebi53542.raw and .txt; metadata
    chebi53542.json
  accessed_at: '2026-10-28T04:05:04.124481Z'
  support: context_only
  summary: Candidate nickel hexahydrate identity only; not concentration or preparation
    evidence
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  locator: Exact raw and derivative text at sources/chebi53503.raw and .txt; metadata
    chebi53503.json
  accessed_at: '2026-10-28T04:01:30.491812Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  locator: Exact raw and derivative text at sources/chebi34887.raw and .txt; metadata
    chebi34887.json
  accessed_at: '2026-10-28T04:01:30.286732Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  locator: Exact raw and derivative text at sources/chebi33118.raw and .txt; metadata
    chebi33118.json
  accessed_at: '2026-10-28T04:01:30.230350Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: current
  kind: record_content
  reference: data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
  locator: full target and owner; exact byte hashes in native source.inputs
  accessed_at: '2026-10-28T04:06:38.508739Z'
  support: context_only
  summary: Current target and exact maintained owner, including complete history and
    evidence.
  snapshot_sha256: 884c31c753abfa7fd5de117460964a7bff945de2d887273de1c5635685393599
- evidence_id: mim
  kind: database
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: all9077rows; source commit/hash in adjacent metadata
  accessed_at: '2026-10-28T04:06:38.508898Z'
  support: context_only
  summary: Packaged MIM CSV only, exact row and key joins; MAPPED and REJECTED entries
    distinguished. No assertion about current remote release.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _extract_primary_components; _solution_from_item;
    _parse_unit; _convert_to_culturemech
  accessed_at: '2026-10-28T04:06:38.509285Z'
  support: context_only
  summary: Current TOGO importer preserves recognized primary sections and separate
    stocks, but bare g/ml values still map to per-litre enums and fallback/default
    paths exist. Current code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: merger
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content and merge_formulation_evidence; inspected merger.merge_group
  accessed_at: '2026-10-28T04:06:38.509332Z'
  support: context_only
  summary: Current formulation comparison requires exact scientific-field equality
    and merger rejects incompatible multi-source formulations; singleton publication
    still needs regeneration after owner changes.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: prior
  kind: prior_review
  reference: reports/yaml_record_review/20260921T180956Z-Bacillus_Tusciae_Medium.md
  locator: full report; exact target path in header
  accessed_at: '2026-10-28T04:06:38.509362Z'
  support: context_only
  summary: Fully read September narrative review of this exact target; derivative
    historical opinion only. Its command successes are not reused and its final-volume/merge
    inferences are independently reassessed.
  snapshot_sha256: 7f1886ea8458132239c129dafe0afd10dc2da63bfaf78ff89ac71025d90d7b07
- evidence_id: sl6-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
  locator: composition[0:8], all evidence and history; ingredients[0] placeholder
  accessed_at: '2026-10-28T04:06:38.515061Z'
  support: context_only
  summary: Complete current standalone solution 25, all eight composition claims,
    provider IDs, history, stale placeholder and quality flag; no main-medium conditions
    transfer.
  snapshot_sha256: bcf1021fe1ddfe3465a791093ff7f36ad1dbf687017dd085638e82026174c9ce
- evidence_id: water-repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient, repair_record
  accessed_at: '2026-10-28T04:06:38.515111Z'
  support: context_only
  summary: Current duplicate repair collapses only identical numeric parts and preserves
    a new history event; it does not authenticate volume units or stock separation.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: mg-repair
  kind: record_content
  reference: scripts/migrate_mgso4_heptahydrate_term.py
  locator: iter_ingredients and main
  accessed_at: '2026-10-28T04:06:38.515526Z'
  support: context_only
  summary: Current MgSO4-heptahydrate writer changes primary term only when the supplied
    name explicitly denotes seven waters; secondary slots are outside that writer.
  snapshot_sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
- evidence_id: quantity-sidecar
  kind: record_content
  reference: REVIEW_WORK/batch054/record08/quantity-inventory.json
  locator: All decisions and exact local/source locators
  accessed_at: '2026-10-28T04:06:38.626868Z'
  support: supports
  summary: Complete scoped quantity decisions, including unchanged and unsupported
    claims.
  snapshot_sha256: 87a854b46d458b1945c53ed162da9ddc78e6fbe105c35cee9f7f87ac6c2b2405
- evidence_id: grounding-sidecar
  kind: authority
  reference: REVIEW_WORK/batch054/record08/grounding-inventory.json
  locator: slots, ontology_objects and exact CSV row pool
  accessed_at: '2026-10-28T04:06:38.626929Z'
  support: supports
  summary: Exact returned OLS objects and all asserted chemical slots, with literal
    label correspondence separate from supplied-form decisions.
  snapshot_sha256: 1e5e36e3255590d120fd0bf1da2c396727dcfd9b0272a304de24d73fa6bef9df
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch054/record08/schema-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:31.170339Z'
  support: supports
  summary: Actual fresh schema canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 0b9ed1f1ebdb40f851207a15065dca74710d756d45105f38fe49134c5c68c11e
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch054/record08/strict-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:32.332802Z'
  support: supports
  summary: Actual fresh strict canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 05ef1c3ec0e8cfbfa1ab784ef563494d4ed0a94348ee45a81537d4a8bf7245ff
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch054/record08/terms-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:33.639654Z'
  support: supports
  summary: Actual fresh terms canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 4daca76bac366844b5c9381625ebd8d334716d39595e1f3d12212bbc65217845
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch054/record08/references-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:34.582459Z'
  support: supports
  summary: Actual fresh references canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: e101123d7dd473248617c9f6c20ce5fc7818d13915e92bd8e248fd0765d34097
assessments:
- assessment_id: identity
  area: identity
  topic: DSM 369 linked-source hierarchy
  outcome: supported
  summary: Exact target/owner identity is TOGO 2392/DSM 369. DSM 2912 identifies Kyrpidia
    tusciae, formerly Bacillus tusciae, riskgroup 1. The medium name is historical
    nomenclature, not a reason to rename or import unrelated strain claims.
  target_ids:
  - CultureMech:008975
  evidence_ids:
  - dsm369
  - dsm2912
  - togo2392
- assessment_id: quantities
  area: quantity
  topic: Every local quantity and scoped source condition
  outcome: concern
  summary: 41 exact local concentration fields covered by 33 stage-specific decisions;
    unchanged source-matched masses are retained with their denominator limits.
  target_ids:
  - CultureMech:008975
  evidence_ids:
  - quantity-sidecar
  details: '{"schema":"fresh-b054-scoped-quantity-inventory-v1","target":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","quantity_field_count":41,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1000.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"Restore
    distinct main and SL-6 water additions. The owner already repaired the duplicate
    sum from 2000 to1000, but both layers still use mass-concentration units. Each
    source water row is1000 mL in its own batch; do not sum or infer density.","source_stage":"main
    water","source_amount":1000,"source_unit":"mL","denominator":"listed 1000 mL water
    in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 14-14","quote":"Distilled water                                               1000.00      ml"}]},{"quantity_id":"q2","label":"MgSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric mass and supplied salt match the primary batch table. Retain the mass,
    but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main
    batch","source_amount":"0.2","source_unit":"g","denominator":"listed 1000 mL water
    in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 8-8","quote":"MgSO4 x 7 H2O                                                    0.20       g"}]},{"quantity_id":"q3","label":"CaCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric mass and supplied salt match the primary batch table. Retain the mass,
    but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main
    batch","source_amount":"0.01","source_unit":"g","denominator":"listed 1000 mL
    water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 9-9","quote":"CaCl2 x 2 H2O                                                    0.01       g"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric mass and supplied salt match the primary batch table. Retain the mass,
    but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main
    batch","source_amount":"1.5","source_unit":"g","denominator":"listed 1000 mL water
    in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 5-5","quote":"KH2PO4                                                           1.50       g"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric mass and supplied salt match the primary batch table. Retain the mass,
    but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main
    batch","source_amount":"1","source_unit":"g","denominator":"listed 1000 mL water
    in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 6-6","quote":"NH4Cl                                                            1.00       g"}]},{"quantity_id":"q6","label":"MnSO4
    x H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric mass and supplied salt match the primary batch table. Retain the mass,
    but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main
    batch","source_amount":"0.01","source_unit":"g","denominator":"listed 1000 mL
    water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 7-7","quote":"MnSO4 x H2O                                                      0.01       g"}]},{"quantity_id":"q7","label":"Ferric
    ammonium citrate","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies 5 mg, whereas both local layers encode 5 G_PER_L. Correct the 1000-fold
    mg-versus-g transcription while separately preserving the listed-batch basis;
    do not assert 0.005 g/L as a measured final-medium rate.","source_stage":"main
    batch","source_amount":5,"source_unit":"mg","denominator":"listed 1000 mL water
    in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 10-10","quote":"Ferric ammonium citrate                                          5.00      mg"}]},{"quantity_id":"q8","label":"Na2HPO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric mass and supplied salt match the primary batch table. Retain the mass,
    but no explicit final-volume statement authenticates the current G_PER_L denominator.","source_stage":"main
    batch","source_amount":"4.5","source_unit":"g","denominator":"listed 1000 mL water
    in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 4-4","quote":"Na2HPO4 x 2 H2O                                                  4.50       g"}]},{"quantity_id":"q9","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.03","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 32-32","quote":"Na2MoO4 x 2 H2O                                              0.03        g"}]},{"quantity_id":"q10","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.3","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 28-28","quote":"H3BO3                                                        0.30        g"}]},{"quantity_id":"q11","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.03","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 27-27","quote":"MnCl2 x 4 H2O                                                0.03        g"}]},{"quantity_id":"q12","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.2","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 29-29","quote":"CoCl2 x 6 H2O                                                0.20        g"}]},{"quantity_id":"q13","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.02","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 31-31","quote":"NiCl2 x 6 H2O                                                0.02        g"}]},{"quantity_id":"q14","label":"ZnSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.1","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 26-26","quote":"ZnSO4 x 7 H2O                                                0.10        g"}]},{"quantity_id":"q15","label":"CuCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the SL-6 stock and must not appear as an undiluted main-medium
    concentration. Retain exact stock batch mass and separately link the 3 mL stock
    addition; provider-declared stock g/L is independently supported only in solution
    25.","source_stage":"SL-6 stock","source_amount":"0.01","source_unit":"g","denominator":"listed
    1000 mL water in the corresponding batch; final volume unspecified","sources":[{"evidence_id":"dsm27","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf","raw_sha256":"e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9","text_sha256":"36a388c134963116d05f85b4221bf3c0b1ff2adffe75c227c69dc0c5ea77f7e8","locator":"dsm27.txt
    lines 30-30","quote":"CuCl2 x 2 H2O                                                0.01        g"}]},{"quantity_id":"q16","label":"SL-6
    receiving dose","local_fields":[{"path":"data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"Replace
    mass-concentration encoding with the literal 3 mL stock addition per stated batch;
    distinguish this dose from stock composition and from a measured final-litre rate.","source_stage":"main
    receiving dose","source_amount":3,"source_unit":"mL","denominator":"listed 1000
    mL main water","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 11-12","quote":"Trace element solution SL-6                                      3.00      ml\n(see
    medium 27)"}]},{"quantity_id":"q17","label":"Standalone SL-6 ZnSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.1,"source_unit":"g","denominator":"provider-declared stock
    g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\":
    35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.347752,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q18","label":"Standalone SL-6 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[1].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.03,"source_unit":"g","denominator":"provider-declared
    stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.151588,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q19","label":"Standalone SL-6 H3BO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[2].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.3,"source_unit":"g","denominator":"provider-declared stock
    g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[2]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.3,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.3,\n                \"mmol_l\": 4.85123,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q20","label":"Standalone SL-6 CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.2,"source_unit":"g","denominator":"provider-declared stock
    g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[3]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.54037,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q21","label":"Standalone SL-6 CuCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[4].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.01,"source_unit":"g","denominator":"provider-declared
    stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[4]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\":
    39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0586569,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q22","label":"Standalone SL-6 NiCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[5].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.02,"source_unit":"g","denominator":"provider-declared
    stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[5]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.154322,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q23","label":"Standalone SL-6 Na2MoO4 x 2
    H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[6].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Current
    exact provider bytes authenticate the attached claim and provider-declared stock
    g_l; this is not a receiving-medium rate or measured final volume.","source_stage":"standalone
    SL-6","source_amount":0.03,"source_unit":"g","denominator":"provider-declared
    stock g_l","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[6]","quote":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.123993,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q24","label":"Standalone SL-6 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"composition[7].concentration","stored":{"value":"1","unit":"L"}}],"decision":"evidence_only","rationale":"Current
    provider 1000 mL water supports the existing 1 L batch-volume conversion; no percent
    or density inference.","source_stage":"standalone SL-6","source_amount":1000,"source_unit":"ml","denominator":"stock
    batch water","sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"$.data.recipe[7]","quote":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }"}]},{"quantity_id":"q25","label":"Standalone stale placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Variable
    placeholder is not an actual ingredient. Current complete composition supports
    removing the stale placeholder and reassessing incomplete_composition flag, without
    inventing a quantity.","source_stage":"representation","source_amount":null,"source_unit":null,"denominator":null,"sources":[{"evidence_id":"solution25","source_url":"https://mediadive.dsmz.de/rest/solution/25","raw_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","text_sha256":"eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c","locator":"solution25.txt
    lines 5-8","quote":"\"id\": 25,\n        \"name\": \"Trace element solution SL-6\",\n        \"volume\":
    1000,\n        \"recipe\": ["}]},{"quantity_id":"q26","label":"Final medium pH","local_fields":[],"decision":"add","rationale":"Use
    the 369 override 4.0; TOGO meta.ph7.1 reflects the parent and must not replace
    the explicit override.","source_stage":"369 preparation","source_amount":4.0,"source_unit":"pH","denominator":null,"sources":[{"evidence_id":"dsm369","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf","raw_sha256":"cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade","text_sha256":"fdd76ede31e2e67d8fe56b24a75ee4e2c09b67936cd7074ce13f49cc45691536","locator":"dsm369.txt
    lines 4-4","quote":"Adjust medium 261 to pH 4.0."}]},{"quantity_id":"q27","label":"Incubation
    temperature","local_fields":[],"decision":"add","rationale":"369 overrides the
    261/26065 °C condition with 50 °C; do not retain both as equivalent conditions.","source_stage":"369
    incubation","source_amount":50,"source_unit":"degC","denominator":null,"sources":[{"evidence_id":"dsm369","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf","raw_sha256":"cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade","text_sha256":"fdd76ede31e2e67d8fe56b24a75ee4e2c09b67936cd7074ce13f49cc45691536","locator":"dsm369.txt
    lines 5-5","quote":"Incubate at 50C without agitation under 5% O2, 10% CO2, 45%
    H2 (v/v)."}]},{"quantity_id":"q28","label":"Gas fractions and no agitation","local_fields":[],"decision":"add","rationale":"Retain
    5% O2, 10% CO2, 45% H2(v/v) and no agitation. Fractions total 60%; missing balance
    is unstated and must remain unresolved, never filled with guessed nitrogen/air.","source_stage":"369
    incubation","source_amount":"5/10/45","source_unit":"percent v/v","denominator":"gas
    total incomplete","sources":[{"evidence_id":"dsm369","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf","raw_sha256":"cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade","text_sha256":"fdd76ede31e2e67d8fe56b24a75ee4e2c09b67936cd7074ce13f49cc45691536","locator":"dsm369.txt
    lines 5-5","quote":"Incubate at 50C without agitation under 5% O2, 10% CO2, 45%
    H2 (v/v)."}]},{"quantity_id":"q29","label":"Pyruvate exclusion","local_fields":[],"decision":"not_quantified","rationale":"261
    explicitly excludes 260 pyruvate. Retain its absence; do not import the parent
    1.50 g row.","source_stage":"261 override","source_amount":null,"source_unit":null,"denominator":null,"sources":[{"evidence_id":"dsm261","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium261.pdf","raw_sha256":"abea799d50da431e0446e012179e4ef6144c6f239cc8db830e33abafbcf33596","text_sha256":"01c1b230c54f9270f8d70a3a65fe0557c62dfe64bee2ff64a7731d738b0d1753","locator":"dsm261.txt
    lines 5-6","quote":"Use medium 260 without pyruvate. Incubate at 65C without
    agitation under 5% (v/v)\nO2, 10% CO2, 45% H2."}]},{"quantity_id":"q30","label":"Parent
    pH and temperature","local_fields":[],"decision":"conflict","rationale":"Parent
    pH7.1 and 65 °C are superseded by369, not alternative targets. Other uncontradicted
    preparation steps remain scoped to the inherited base.","source_stage":"parent
    override","source_amount":null,"source_unit":null,"denominator":null,"sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 16-18","quote":"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in
    30 - 50 ml amounts in\nErlenmeyer flasks and sterilize for 15 minutes at 121C.
    Incubate without agitation at\n65C."}]},{"quantity_id":"q31","label":"Optional
    agar","local_fields":[],"decision":"add","rationale":"15 g agar is an optional
    solid variant. Do not make it mandatory or silently change the selected liquid
    recipe.","source_stage":"optional solid variant","source_amount":15,"source_unit":"g","denominator":"listed
    batch","sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 16-16","quote":"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in
    30 - 50 ml amounts in"}]},{"quantity_id":"q32","label":"Dispensed volume","local_fields":[],"decision":"add","rationale":"Preserve
    30–50 mL distribution into Erlenmeyer flasks as an inherited preparation instruction,
    not the final batch denominator.","source_stage":"dispensing","source_amount":"30–50","source_unit":"mL","denominator":null,"sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 16-17","quote":"Adjust pH to 7.1. Agar if necessary 15.0 g. Distribute in
    30 - 50 ml amounts in\nErlenmeyer flasks and sterilize for 15 minutes at 121C.
    Incubate without agitation at"}]},{"quantity_id":"q33","label":"Sterilization","local_fields":[],"decision":"add","rationale":"Retain
    15 minutes at121 °C from the inherited base; do not transfer DSM 27 main-medium
    sterilization or illumination protocol.","source_stage":"sterilization","source_amount":"15
    at121","source_unit":"min/degC","denominator":null,"sources":[{"evidence_id":"dsm260","source_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf","raw_sha256":"ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291","text_sha256":"881f590b26a9d46297c3679f293829be7699719ab637132e8a9b3201b58cb7a5","locator":"dsm260.txt
    lines 17-17","quote":"Erlenmeyer flasks and sterilize for 15 minutes at 121C.
    Incubate without agitation at"}]}],"limits":["A listed water amount is not an
    explicit measured final volume. Stock-local amounts are not receiving-medium rates.","Source-only
    rows/conditions are explicit; no density assumptions or invented missing gas balance."]}'
- assessment_id: grounding
  area: grounding
  topic: Chemical identity, canonical labels and packaged MIM
  outcome: concern
  summary: All asserted CHEBI objects were retrieved directly and exact labels compared;
    supplied-form exceptions are described individually. Packaged MIM membership or
    label agreement alone is not chemical verification.
  target_ids:
  - CultureMech:008975
  evidence_ids:
  - grounding-sidecar
  - mim
- assessment_id: classification
  area: representation
  topic: Category, composition and physical-state scope
  outcome: concern
  summary: Bacterial/liquid scope is consistent with the selected optional-agar-free
    variant. Ferric ammonium citrate is an indefinite mixture, so do not force chemically
    defined classification solely from named salts. DSM 27 bulk formulation and phototrophic
    conditions are excluded.
  target_ids:
  - CultureMech:008975
  evidence_ids:
  - current
  - dsm369
- assessment_id: history
  area: provenance
  topic: Current repairs and historical review limits
  outcome: supported
  summary: Complete current target/owner history and selected September report were
    read. Existing repair credit is retained; current writer bodies describe current
    behavior only. No lost 451–520 bundle is reconstructed or backdated.
  target_ids:
  - CultureMech:008975
  evidence_ids:
  - prior
  - current
  - importer
  - merger
findings:
- finding_id: f1
  issue_key: b054-08-f1
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The369 override and source-stage preparation are missing
  description: Preserve pH4.0, 50 °C and the quoted no-agitation/gas condition from
    369, pyruvate exclusion from 261, and the scoped inherited base preparation. The
    gas fractions total 60%; no unstated balance may be inferred. TOGO metadata 7.1
    is a parent conflict, not an alternative authoritative pH.
  target_ids:
  - CultureMech:008975
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - dsm369
  - dsm261
  - dsm260
  - togo2392
  rule_id: review-yaml-record/source-supported-completeness
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: b054-08-f2
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: SL-6 stock components were flattened into main ingredients
  description: Seven trace salts appear at stock strength as main ingredients while
    solutions[0] also adds SL-6 using 3 G_PER_L. Represent the 3 mL batch dose separately
    and keep stock components in the linked/nested stock, with no unsupported receiving-medium
    concentration.
  target_ids:
  - CultureMech:008975
  field_paths:
  - ingredients[8]
  - ingredients[9]
  - ingredients[10]
  - ingredients[11]
  - ingredients[12]
  - ingredients[13]
  - ingredients[14]
  - solutions[0]
  evidence_ids:
  - dsm260
  - dsm27
  - solution25
  - togo2392
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: b054-08-f3
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Ferric ammonium citrate has a mg-to-g transcription error
  description: Both local layers encode 5 G_PER_L while DSM 260 and TOGO specify 5
    mg per batch. Correct the mass scale and retain denominator uncertainty separately;
    an exact final-volume rate is not established.
  target_ids:
  - CultureMech:008975
  field_paths:
  - ingredients[6].concentration
  evidence_ids:
  - dsm260
  - togo2392
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: b054-08-f4
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water units and generated duplicate state remain wrong
  description: The owner already collapsed identical duplicate water to1000, but the
    generated target retains 2000. Neither G_PER_L value represents the separate 1000
    mL main and stock water doses. Preserve repair credit, restore stage-local volumes
    and regenerate.
  target_ids:
  - CultureMech:008975
  field_paths:
  - ingredients[0]
  evidence_ids:
  - current
  - water-repair
  - dsm260
  - dsm27
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: b054-08-f5
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Magnesium secondary and nickel primary/secondary terms do not match hydrates
  description: Primary Mg heptahydrate 31795 is already repaired; secondary 32599
    is still generic. Ni hexahydrate is linked to anhydrous 34887 in both main layers
    and dependency composition[5].chebi_term. OLS53542 verifies the hexahydrate candidate.
    Co53503 is chemically correct despite a REJECTED preferred-label row coexisting
    with a MAPPED alias in the packaged CSV.
  target_ids:
  - CultureMech:008975
  field_paths:
  - ingredients[1].mediaingredientmech_chebi_term
  - ingredients[12].term
  - ingredients[12].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml::composition[5].chebi_term
  evidence_ids:
  - chebi31795
  - chebi32599
  - chebi34887
  - chebi53542
  - chebi53503
  - mim
  - mg-repair
  - sl6-owner
  rule_id: review-recipes/ID-form-correspondence
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped SL-6 dependency; composition/evidence only
- finding_id: f6
  issue_key: b054-08-f6
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source-matched batch masses and stock representation need bounded evidence
  description: The remaining main masses match DSM 260, but current G_PER_L units
    lack an explicit final-volume basis. Solution 25 rates are provider-declared and
    can be retained within that stock; the current returned raw matches all eight
    attached claim hashes/snippets. Its old access timestamp is still a historical
    claim.
  target_ids:
  - CultureMech:008975
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsm260
  - solution25
  - sl6-owner
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
- finding_id: f7
  issue_key: b054-08-f7
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: The standalone complete stock still carries placeholder/flag and unvetted
    provider molarity
  description: Solution 25 composition is now complete, yet ingredients[0] says See
    source for composition and incomplete_composition remains. Provider Co/Ni mmol_l
    values use anhydrous mass scales inconsistent with named hexahydrates; do not
    promote these contextual numbers into the local stock. Existing g_l quantities
    remain independently supported.
  target_ids:
  - CultureMech:008975
  field_paths:
  - solutions[0]
  - data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml::data_quality_flags
  evidence_ids:
  - sl6-owner
  - solution25
  - chebi53503
  - chebi34887
  - chebi53542
  rule_id: review-yaml-record/stage-and-variant-scope
  native_severity: P3
  normalization_reason: Provenance or representational completeness issue with bounded
    impact.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped SL-6 dependency; composition/evidence only
actions:
- action_id: a1
  description: 'Correct the maintained source for: The369 override and source-stage
    preparation are missing. Preserve pH4.0, 50 °C and the quoted no-agitation/gas
    condition from 369, pyruvate exclusion from 261, and the scoped inherited base
    preparation. The gas fractions total 60%; no unstated balance may be inferred.
    TOGO metadata 7.1 is a parent conflict, not an alternative authoritative pH.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a2
  description: 'Correct the maintained source for: SL-6 stock components were flattened
    into main ingredients. Seven trace salts appear at stock strength as main ingredients
    while solutions[0] also adds SL-6 using 3 G_PER_L. Represent the 3 mL batch dose
    separately and keep stock components in the linked/nested stock, with no unsupported
    receiving-medium concentration.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a3
  description: 'Correct the maintained source for: Ferric ammonium citrate has a mg-to-g
    transcription error. Both local layers encode 5 G_PER_L while DSM 260 and TOGO
    specify 5 mg per batch. Correct the mass scale and retain denominator uncertainty
    separately; an exact final-volume rate is not established.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a4
  description: 'Correct the maintained source for: Water units and generated duplicate
    state remain wrong. The owner already collapsed identical duplicate water to1000,
    but the generated target retains 2000. Neither G_PER_L value represents the separate
    1000 mL main and stock water doses. Preserve repair credit, restore stage-local
    volumes and regenerate.'
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a5
  description: 'Correct the maintained source for: Magnesium secondary and nickel
    primary/secondary terms do not match hydrates. Primary Mg heptahydrate 31795 is
    already repaired; secondary 32599 is still generic. Ni hexahydrate is linked to
    anhydrous 34887 in both main layers and dependency composition[5].chebi_term.
    OLS53542 verifies the hexahydrate candidate. Co53503 is chemically correct despite
    a REJECTED preferred-label row coexisting with a MAPPED alias in the packaged
    CSV.'
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped SL-6 dependency; composition/evidence only
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a6
  description: 'Correct the maintained source for: Source-matched batch masses and
    stock representation need bounded evidence. The remaining main masses match DSM
    260, but current G_PER_L units lack an explicit final-volume basis. Solution 25
    rates are provider-declared and can be retained within that stock; the current
    returned raw matches all eight attached claim hashes/snippets. Its old access
    timestamp is still a historical claim.'
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a7
  description: 'Correct the maintained source for: The standalone complete stock still
    carries placeholder/flag and unvetted provider molarity. Solution 25 composition
    is now complete, yet ingredients[0] says See source for composition and incomplete_composition
    remains. Provider Co/Ni mmol_l values use anhydrous mass scales inconsistent with
    named hexahydrates; do not promote these contextual numbers into the local stock.
    Existing g_l quantities remain independently supported.'
  finding_ids:
  - f7
  target_ids:
  - CultureMech:008975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    role: scoped SL-6 dependency; composition/evidence only
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
limitations:
- DSM 27 is read fully but only its SL-6 subsection applies. Parent medium 27 ingredients,
  light regime and receiving dose do not transfer.
- SL-6 current same-byte raw authenticates all eight attached claims. The current
  retrieval does not independently verify their historical access timestamp.
- No final-medium molarity is calculated. Provider Co/Ni mmol_l values are suspect
  hydrate conversions; no unsupported replacement claim is silently adopted.
- The September report is derivative historical context; its old validations and source
  access times are not used as current verification.
- Packaged MIM CSV observations apply only to commit 6643131b0f12ab40b66f98135245fca04027e0e9;
  no global absence or live MIM claim.
- No experiment, growth optimization or universal strain applicability is inferred;
  catalog identity examples are not automatically inserted as target_organisms.
- Canonical reference validation inspected zero references in the generated target;
  scientific source authentication is supplied separately here.
- Source recipes list batch amounts unless an explicit concentration/final-volume
  statement is quoted. No silent normalization based solely on listed water.
```
