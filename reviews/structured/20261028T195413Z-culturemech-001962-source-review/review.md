# Scientific review: DESULFOHALOTOMACULUM MEDIUM

- Review: 20261028T195413Z-culturemech-001962-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T19:38:37.844618Z
- Finished UTC: 2026-10-28T19:54:13.965544Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM815 retains supported main provider rates and substantial preparation text, but nine SL-11 stock strengths and its preparation are misplaced at the main level. Restore source stock scope and evidence, correct sodium-resazurin and nickel supplied-form grounding, and preserve the distinction between main input water and explicit stock final make-up.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch076 index 03
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001962 | data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml | generated | desulfohalotomaculum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001962 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001962 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001962 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001962 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSM815 primary and maintained contributor

identity: supported. Targets: CultureMech:001962.

The selected generated record has one maintained DSM815 contributor and its scientific fields match that owner. The full current one-page DSM815 primary and API agree on formulation identity. DSM815a and other variants are outside this review; the medium name does not supply strain-growth evidence.

### Complex liquid representation

representation: supported. Targets: CultureMech:001962.

Yeast extract supports the complex/undefined classification. Iron powder or nails are supplied solids in a liquid medium, not a solidifying gel or evidence that the medium physical_state should be SOLID.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001962.

46 current concentration fields are covered by 30 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","quantity_field_count":46,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 3-3","quote":"Na2SO4                                                   3.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 21.1208,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q2","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 4-4","quote":"CaCl2 x 2 H2O                                            6.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 40.8122,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q3","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"40","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"40","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 5-5","quote":"NaCl                                                    40.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 40,\n                        \"unit\": \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\": 684.463,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 6-6","quote":"KCl                                                      2.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 26.8276,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 7-7","quote":"NH4Cl                                                    0.30        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 5.60852,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q6","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 8-8","quote":"KH2PO4                                                   0.20        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.46967,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q7","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 9-9","quote":"MgCl2 x 6 H2O                                            8.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\": 39.3501,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q8","label":"SrCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 10-10","quote":"SrCl2 x 6 H2O                                            0.10        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"SrCl2 x 6 H2O\",\n                        \"compound_id\": 176,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.37507,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q9","label":"MOPS","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 12-12","quote":"MOPS                                                     3.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"MOPS\",\n                        \"compound_id\": 351,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 14.3362,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q10","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 13-13","quote":"Yeast extract                                            1.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone."}]},{"quantity_id":"q11","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary gives 0.5 ml of an explicit 0.1% w/v sodium-resazurin stock, equivalent to 0.5 mg in the batch. API explicitly reports g_l=0.0005 and the local number agrees with that nominal rate. Retain the stock form/dose and distinguish this from measured final-medium concentration; source input water and API volume 1001 ml do not independently establish a final-volume conversion. The sodium-salt grounding issue is separate.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 14-14","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The primary gives 0.5 ml of an explicit 0.1% w/v sodium-resazurin stock, equivalent to 0.5 mg in the batch. API explicitly reports g_l=0.0005 and the local number agrees with that nominal rate. Retain the stock form/dose and distinguish this from measured final-medium concentration; source input water and API volume 1001 ml do not independently establish a final-volume conversion. The sodium-salt grounding issue is separate."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The primary gives 0.5 ml of an explicit 0.1% w/v sodium-resazurin stock, equivalent to 0.5 mg in the batch. API explicitly reports g_l=0.0005 and the local number agrees with that nominal rate. Retain the stock form/dose and distinguish this from measured final-medium concentration; source input water and API volume 1001 ml do not independently establish a final-volume conversion. The sodium-salt grounding issue is separate."}]},{"quantity_id":"q12","label":"Iron powder","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. Primary also specifies iron powder or nails and a separate 1–2 g per-vessel instruction. Preserve both source controls and the nail alternative; absent vessel fill volume does not justify deriving a unique g/L from the vessel instruction.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 15-15","quote":"Iron powder (or nails)                                 100.00        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Iron powder\",\n                        \"compound_id\": 760,\n                        \"attribute\": \"or nails\",\n                        \"amount\": 100,\n                        \"unit\": \"g\",\n                        \"g_l\": 100,\n                        \"mmol_l\": 1790.67,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. Primary also specifies iron powder or nails and a separate 1–2 g per-vessel instruction. Preserve both source controls and the nail alternative; absent vessel fill volume does not justify deriving a unique g/L from the vessel instruction."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. Primary also specifies iron powder or nails and a separate 1–2 g per-vessel instruction. Preserve both source controls and the nail alternative; absent vessel fill volume does not justify deriving a unique g/L from the vessel instruction."}]},{"quantity_id":"q13","label":"Na-L-lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.6","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. The retained main preparation explicitly adds this compound from a separately prepared sterile anoxic stock; its stock concentration/volume is not supplied and must not be invented.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 16-16","quote":"Na-L-lactate                                             3.60        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na-L-lactate\",\n                        \"compound_id\": 265,\n                        \"amount\": 3.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.6,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. The retained main preparation explicitly adds this compound from a separately prepared sterile anoxic stock; its stock concentration/volume is not supplied and must not be invented."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. The retained main preparation explicitly adds this compound from a separately prepared sterile anoxic stock; its stock concentration/volume is not supplied and must not be invented."}]},{"quantity_id":"q14","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. The retained main preparation explicitly adds this compound from a separately prepared sterile anoxic stock; its stock concentration/volume is not supplied and must not be invented.","source_stage":"Main formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 17-17","quote":"Na2CO3                                                   0.50        g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 4.71751,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. The retained main preparation explicitly adds this compound from a separately prepared sterile anoxic stock; its stock concentration/volume is not supplied and must not be invented."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The local scalar and G_PER_L unit match the exact provider g_l assertion. The primary independently gives the batch mass. Credit this nominal provider rate while preserving its distinction from primary measured final volume: API declares volume 1001 ml but reports the nominal rates without dividing these masses by 1.001; the primary lists 1000 ml input water and no explicit final make-up. No numeric replacement is justified from those facts alone. The retained main preparation explicitly adds this compound from a separately prepared sterile anoxic stock; its stock concentration/volume is not supplied and must not be invented."}]},{"quantity_id":"q15","label":"Na2-EDTA x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 32-32","quote":"Na2-EDTA x 2 H2O                                         5.20       g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q16","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 33-33","quote":"FeCl2 x 4 H2O                                            1.50       g","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q17","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 34-34","quote":"ZnCl2                                                   70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q18","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 35-35","quote":"MnCl2 x 4 H2O                                          100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q19","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 36-36","quote":"H3BO3                                                    6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q20","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 37-37","quote":"CoCl2 x 6 H2O                                          190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q21","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 38-38","quote":"CuCl2 x 2 H2O                                            2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q22","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 39-39","quote":"NiCl2 x 6 H2O                                           24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q23","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11 stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 40-40","quote":"Na2MoO4 x 2 H2O                                         36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by its exact batch amount and final make-up, agreeing with provider stock g_l. That does not support its current main-ingredient placement. Restore the SL-11 stock and separate primary 1 ml batch receiving dose; do not treat the stock strength as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q24","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"The primary includes 1000 ml distilled water, omitted locally. Preserve this solvent input in source-scoped preparation; it is not a measured final-volume statement.","source_stage":"Source-only main batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 18-18","quote":"Distilled water                                       1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q25","label":"SL-11 receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The primary adds 1 ml SL-11 to the stated batch. Restore this separate dose and its embedded stock definition; a per-litre receiving basis is not independently supplied.","source_stage":"Source-only stock receiving dose","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q26","label":"Sodium-resazurin stock dose and strength","local_fields":[],"decision":"evidence_only","rationale":"Preserve the exact 0.5 ml stock addition and explicit 0.1% w/v strength. Their product is a 0.5 mg batch amount. Retaining the provider nominal g_l does not replace the source stock representation or prove final-volume measurement.","source_stage":"Source-only dye stock","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 14-14","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q27","label":"SL-11 water and final make-up","local_fields":[],"decision":"evidence_only","rationale":"The table lists 1000 ml water, while the preparation explicitly starts in 800 ml and brings final volume to 1000 ml. Preserve the final-make-up instruction as the stock denominator, rather than add 1000 ml after the initial 800 ml.","source_stage":"Source-only stock final-volume control","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 41-41","quote":"Distilled water                                       1000.00      ml","quote_basis":"derivative text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Retained final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"The retained pH 7.2 agrees with the exact main preparation. It must remain distinct from preliminary main pH6 and stock adjustments pH 7 then 6.","source_stage":"Final main-medium pH","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105\\u00b0C. Before use add lactate from a sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The retained pH 7.2 agrees with the exact main preparation. It must remain distinct from preliminary main pH6 and stock adjustments pH 7 then 6."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The retained pH 7.2 agrees with the exact main preparation. It must remain distinct from preliminary main pH6 and stock adjustments pH 7 then 6."}]},{"quantity_id":"q29","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from a sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2."}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from a sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2."}}],"decision":"evidence_only","rationale":"The existing text and AUTOCLAVE classification preserve the primary main procedure, including pH 6, 100% N2 for 30–45 min, vessel iron 1–2 g or nail, 105°C for 30 min, later lactate/carbonate additions and pH 7.2. Keep that exact context and gas distinction. Do not infer unspecified stock strengths or vessel fill volume.","source_stage":"Retained main preparation","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing 1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105\\u00b0C. Before use add lactate from a sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing text and AUTOCLAVE classification preserve the primary main procedure, including pH 6, 100% N2 for 30–45 min, vessel iron 1–2 g or nail, 105°C for 30 min, later lactate/carbonate additions and pH 7.2. Keep that exact context and gas distinction. Do not infer unspecified stock strengths or vessel fill volume."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing text and AUTOCLAVE classification preserve the primary main procedure, including pH 6, 100% N2 for 30–45 min, vessel iron 1–2 g or nail, 105°C for 30 min, later lactate/carbonate additions and pH 7.2. Keep that exact context and gas distinction. Do not infer unspecified stock strengths or vessel fill volume."}]},{"quantity_id":"q30","label":"Retained SL-11 preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."}}],"decision":"correct","rationale":"The words and ADJUST_PH action are source-supported, including 800 ml starting water, pH 7 with 2 N NaOH, addition order, final pH 6 and 1000 ml make-up. Correct the current root sequence placement by binding it only to SL-11; it must not reset the final medium pH 7.2 or volume.","source_stage":"SL-11 preparation only","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The words and ADJUST_PH action are source-supported, including 800 ml starting water, pH 7 with 2 N NaOH, addition order, final pH 6 and 1000 ml make-up. Correct the current root sequence placement by binding it only to SL-11; it must not reset the final medium pH 7.2 or volume."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The words and ADJUST_PH action are source-supported, including 800 ml starting water, pH 7 with 2 N NaOH, addition order, final pH 6 and 1000 ml make-up. Correct the current root sequence placement by binding it only to SL-11; it must not reset the final medium pH 7.2 or volume."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:001962.

All 22 asserted chemical objects and exact current MIM rows are assessed. Confirmed mismatches are neutral resazurin versus the source sodium salt, and anhydrous nickel versus the specified hexahydrate. L-sodium lactate, elemental iron, disodium EDTA dihydrate and the other explicit hydrates are supported by current scientific ontology objects. MOPS is returned as a broad named buffer class without a supplied formula; no stronger structural claim is made. Rejected lexical rows for iron powder, EDTA or cobalt coexist with mapped equivalent names and do not negate the matching chemical form. Broad catalogue synonyms are not chemically certified; optional yeast identifiers are not endorsed.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:001962.

All three full historical reports were read. The October7 parent has 23 local unresolved concentration claims and 28 exact source recipe/step objects; current API raw digest matches its recorded digest. This authenticates content, not the old retrieval event or writer execution. The old blanket stock-topology conflict does not negate the fourteen explicit main provider rates; the nine stock placements remain wrong. Target and owner scientific fields are equal. Current singleton merger preserves owner content and current MediaDive composition behavior is improved, while preparation concatenation still loses stage labels.

## Findings

### f1: Nine SL-11 stock strengths are flattened into the main formulation

major / open / confirmed; issue key: culturemech-001962-stock-stage.

Restore the nine SL-11 components, its explicit 1000 ml final make-up and separate 1 ml batch dose. Their stock strengths are supported; their root final-medium placement is not. Preserve the main nominal provider rates and input-water distinction, and represent the sodium-resazurin stock dose/strength explicitly. Current composition parsing now excludes this stock reference and dye stock, so it should not recreate historical flattening; review bare-ml normalization before regeneration.

### f2: Two chemical assertions do not match the supplied forms

major / open / confirmed; issue key: culturemech-001962-supplied-forms.

Sodium resazurin is linked to neutral CHEBI:8806, whose formula lacks the sodium counterion; resolve an exact sodium-salt identifier and label rather than accept the broad catalogue synonym. Nickel hexahydrate is linked to anhydrous CHEBI:34887 in both primary and secondary slots; candidate CHEBI:53542 matches the source hydrate. Preserve all source amounts and source stages. MIM Nickel (II) chloride hexahydrate is a mapped preferred row 6668, while NiCl2 x 6 H2O is rejected preferred row 6703 and mapped synonym 6704; no whole-identifier rejection is implied.

### f3: SL-11 preparation is presented as a main-medium step

major / open / confirmed; issue key: culturemech-001962-stock-preparation.

Retain the supported stock preparation text and ADJUST_PH action, but move its field scope to SL-11. The stock pH 7 then 6 and 1000 ml final volume must not override the main pH 7.2 or invent a main final volume. Current preparation collection concatenates steps from all solution sections without stage labels; preserve those labels in generated representation.

### f4: Supported assertions lack attached claim evidence

minor / open / confirmed; issue key: culturemech-001962-claim-evidence.

Attach exact ingredient evidence for chemical quantities and root evidence with field/stage scope for stock doses, water, pH and preparation. No attached claims currently exist. Historical raw-byte matches are separate from attached evidence and original retrieval-event verification. Do not create nonexistent evidence fields on concentration or solution descriptors.

## Recommended Actions And Acceptance Checks

### a1

Restore the nine SL-11 components, its explicit 1000 ml final make-up and separate 1 ml batch dose. Their stock strengths are supported; their root final-medium placement is not. Preserve the main nominal provider rates and input-water distinction, and represent the sodium-resazurin stock dose/strength explicitly. Current composition parsing now excludes this stock reference and dye stock, so it should not recreate historical flattening; review bare-ml normalization before regeneration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Sodium resazurin is linked to neutral CHEBI:8806, whose formula lacks the sodium counterion; resolve an exact sodium-salt identifier and label rather than accept the broad catalogue synonym. Nickel hexahydrate is linked to anhydrous CHEBI:34887 in both primary and secondary slots; candidate CHEBI:53542 matches the source hydrate. Preserve all source amounts and source stages. MIM Nickel (II) chloride hexahydrate is a mapped preferred row 6668, while NiCl2 x 6 H2O is rejected preferred row 6703 and mapped synonym 6704; no whole-identifier rejection is implied.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Retain the supported stock preparation text and ADJUST_PH action, but move its field scope to SL-11. The stock pH 7 then 6 and 1000 ml final volume must not override the main pH 7.2 or invent a main final volume. Current preparation collection concatenates steps from all solution sections without stage labels; preserve those labels in generated representation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Attach exact ingredient evidence for chemical quantities and root evidence with field/stage scope for stock doses, water, pH and preparation. No attached claims currently exist. Historical raw-byte matches are separate from attached evidence and original retrieval-event verification. Do not create nonexistent evidence fields on concentration or solution descriptors.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz815 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf; REVIEW_WORK/batch076/source01-03-supplement/dsmz815.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api815 | https://mediadive.dsmz.de/rest/medium/815; REVIEW_WORK/batch076/source01-03-supplement/api815.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch076/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-16 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfohalotomaculum_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfohalotomaculum_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch076/record03/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch076/record03/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch076/record03/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps; _classify_preparation_action | context_only | The current API composition parser reads only the first solution recipe, excludes explicit solution references and ml rows carrying percent attributes, and prefers supplied g_l for other compounds. It skips water. _parse_api_solutions now preserves the SL-11 and resazurin stock references/doses, but normalizes bare ml to ML_PER_L without proving receiving volume. _parse_preparation_steps still concatenates all solution-stage steps without labels. These current improvements and limits do not authenticate the historical execution. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| selected-parent-authentication | REVIEW_WORK/batch076/record03/selected-parent-authentication.json; Complete artifact | context_only | All 23 old local fields and 28 exact current source objects joined to the historical selected parent. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch076/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch076/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch076/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch076/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch076/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch076/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch076/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi36385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:36385; REVIEW_WORK/batch076/source01-03-supplement/chebi36385.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi39074 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:39074; REVIEW_WORK/batch076/source01-03-supplement/chebi39074.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch076/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi82664 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:82664; REVIEW_WORK/batch076/source01-03-supplement/chebi82664.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi232798 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:232798; REVIEW_WORK/batch076/source01-03-supplement/chebi232798.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch076/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758; REVIEW_WORK/batch076/source01-03-supplement/chebi64758.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch076/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch076/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch076/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch076/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch076/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch076/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch076/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch076/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch076/record03/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch076/record03/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch076/record03/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch076/record03/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch076/record03/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch076/record03/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch076/record03/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch076/record03/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch076/record03/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch076/record03/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch076/record03/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch076/record03/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Only the SL-11 definition printed within DSM815 is used. The other formulation of parent medium 722 and DSM815a are excluded.
- The exact primary gives an explicit final volume only for SL-11. Main API volume 1001 ml and nominal g_l values are recorded separately; unused provider mmol_l conversions are not validated.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T195413Z-culturemech-001962-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOHALOTOMACULUM MEDIUM'
started_at: '2026-10-28T19:38:37.844618Z'
finished_at: '2026-10-28T19:54:13.965544Z'
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
summary: DSM815 retains supported main provider rates and substantial preparation
  text, but nine SL-11 stock strengths and its preparation are misplaced at the main
  level. Restore source stock scope and evidence, correct sodium-resazurin and nickel
  supplied-form grounding, and preserve the distinction between main input water and
  explicit stock final make-up.
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
  - path: data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
    sha256: abda6fa75a7dd91dc1cede7130f914e82aabbeadae359edf05942d63ffdcd328
    role: target
  - path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    sha256: c731fe7b4a8233373f0d5ea5da0f452803204b2809e9a3aa20caaa53be30464c
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfohalotomaculum_medium.yaml.md
    sha256: 3dcd75e1e978d029f36930fd3a05da390cdd6b3535766e69f6965d37bd6be9cb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.md
    sha256: 292fd03bb6023cd31864a15dd511f3b0b1621daba028721d29b71668ce8405f4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfohalotomaculum_medium.md
    sha256: 581c8eced8584d02b44f7f1e40f18f22c05b3ff66fd401374ad5474d13ca1cbd
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
  selection: Authoritative batch076 index 03
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001962
targets:
- target_id: CultureMech:001962
  path: data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
  label: desulfohalotomaculum_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001962
  command: just validate-schema data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
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
  - CultureMech:001962
  command: just validate-strict data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
    --out REVIEW_WORK/batch076/record03/strict.tsv --workers 1 --quiet
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
  - CultureMech:001962
  command: just validate-terms data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
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
  - CultureMech:001962
  command: just validate-references data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz815
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf
  accessed_at: '2026-10-28T19:39:10.150713Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/dsmz815.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d
- evidence_id: api815
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/815
  accessed_at: '2026-10-28T19:39:09.826827Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/api815.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T19:39:16.621013Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:53:34.604274Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: abda6fa75a7dd91dc1cede7130f914e82aabbeadae359edf05942d63ffdcd328
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:53:34.604415Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: c731fe7b4a8233373f0d5ea5da0f452803204b2809e9a3aa20caaa53be30464c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T19:53:34.604439Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T19:53:34.604747Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T19:53:34.604770Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T19:53:34.604791Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-16
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:53:34.604815Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfohalotomaculum_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:53:34.611511Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 3dcd75e1e978d029f36930fd3a05da390cdd6b3535766e69f6965d37bd6be9cb
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T19:53:34.611574Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 292fd03bb6023cd31864a15dd511f3b0b1621daba028721d29b71668ce8405f4
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfohalotomaculum_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:53:34.611603Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 581c8eced8584d02b44f7f1e40f18f22c05b3ff66fd401374ad5474d13ca1cbd
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/historical-reading.json
  accessed_at: '2026-10-28T19:53:34.611633Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 45281813dd29d4feea43c097f751058c29508c2e542c0207877b4c422d233332
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:53:34.611873Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 67e5067b0d8e098d8b9e0e74339367c6be4b90f345d7686b0314fa001d9bf03f
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/complete-document-reader.json
  accessed_at: '2026-10-28T19:53:34.612049Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: dac582f910f67bd6ca836e84e795860fd72d1975204c6d8ad9b27a6c2773a54e
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _api_stock_name; _parse_api_solutions;
    _normalize_unit; _parse_preparation_steps; _classify_preparation_action
  accessed_at: '2026-10-28T19:53:34.612205Z'
  support: context_only
  summary: The current API composition parser reads only the first solution recipe,
    excludes explicit solution references and ml rows carrying percent attributes,
    and prefers supplied g_l for other compounds. It skips water. _parse_api_solutions
    now preserves the SL-11 and resazurin stock references/doses, but normalizes bare
    ml to ML_PER_L without proving receiving volume. _parse_preparation_steps still
    concatenates all solution-stage steps without labels. These current improvements
    and limits do not authenticate the historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T19:53:34.612243Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: selected-parent-authentication
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/selected-parent-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T19:53:34.654969Z'
  support: context_only
  summary: All 23 old local fields and 28 exact current source objects joined to the
    historical selected parent.
  snapshot_sha256: 0a56da616b49e2ac25056a2f7690372944f0cad163d3ac5a72b3ccd2d5ae0519
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T19:39:14.734019Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T19:39:17.787202Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T19:39:12.979419Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T19:39:14.820100Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T19:39:13.848048Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T19:39:16.885926Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T19:39:18.118804Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi36385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:36385
  accessed_at: '2026-10-28T19:39:15.643147Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi36385.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 8593f1fca0faaa416e71c19974851d342dfe12bc8c19ee6e34ddc78e8bbc5583
- evidence_id: chebi39074
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:39074
  accessed_at: '2026-10-28T19:39:15.964988Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi39074.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ed129ea75a8e240eb53c047abc3f1af870d2434f97e65bce7b362fc45cfc659a
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T19:39:18.393979Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi82664
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:82664
  accessed_at: '2026-10-28T19:39:17.496828Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi82664.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9315542331d2d51842c785d977d76f12f6acd775fe818c8abbfd6e129a2c823e
- evidence_id: chebi232798
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:232798
  accessed_at: '2026-10-28T19:39:12.911302Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi232798.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e4ec30f25cb150a18cf079d820943cdc9f6b849b2fae5b6448d6cad204994a4c
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T19:39:13.524629Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758
  accessed_at: '2026-10-28T19:39:16.909099Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi64758.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 326b128326745296132512f9e618ef60c9c3230252a9dac3a75db92f8caa3156
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T19:39:17.804695Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T19:39:16.274339Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T19:39:18.375094Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T19:39:15.045270Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T19:39:16.572787Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T19:39:18.069295Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T19:39:15.418119Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T19:39:17.178522Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:54:13.965544Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 74738149eaa60eb017e25699f16cc614166233cb828e949b8f8c43cb2b37f387
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:53:34.742877Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 81b326c5fb338846ca7dafa59b16dd4289b5c76e3ed50a6a717408a8b2c52e69
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:53:34.742979Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 3f1af63e1a1006b9185d22dda6088945968f817791259ec96c6aef96eb8801ce
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:53:34.743031Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 41fb62a84ba918a94a3b089e73d79c03e9c504279ec90443bbf5dbaa1a9ea089
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:53:34.743073Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: e2ad0d0c8cf16d18f22fe930d7b5d0e6f8c9fcee99caa5e77b3f63f21b5c5b98
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:53:34.743093Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 7d3ecab1367f00a9b14ae69c7335c3a10e005e26555f1920d14a42e3bb9562e0
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:53:34.743112Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch076/record03/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T19:53:34.743130Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: 1d74ac9465ae2943b4a9a4e0f861dbdf00e7154d467ffa4c3a00c29fd2489afb
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch076/record03/validate-schema.json
  accessed_at: '2026-10-28T19:38:38.905499Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 8e24e4727395536f810526dec1ebb942d55700f93d9d1f2c84b9e7ad0d9fa7dc
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch076/record03/validate-strict.json
  accessed_at: '2026-10-28T19:38:39.859838Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e99ca386a07e2d5aaff105e6757a7216cef9405d640f4db5509d7ada1628b9bd
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch076/record03/validate-terms.json
  accessed_at: '2026-10-28T19:38:40.893997Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c2e0042b5b8b30d63012e30bd35e0ad1b72d022ec3bd7af8a703da7c044aa95c
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch076/record03/validate-references.json
  accessed_at: '2026-10-28T19:38:41.619135Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 407fc9137c7aeeaa2879c0e90448f5f27ddb6c0b4171c6ec73df5c077a688528
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSM815 primary and maintained contributor
  outcome: supported
  summary: The selected generated record has one maintained DSM815 contributor and
    its scientific fields match that owner. The full current one-page DSM815 primary
    and API agree on formulation identity. DSM815a and other variants are outside
    this review; the medium name does not supply strain-growth evidence.
  target_ids:
  - CultureMech:001962
  evidence_ids:
  - target
  - owner
  - dsmz815
  - api815
- assessment_id: classification
  area: representation
  topic: Complex liquid representation
  outcome: supported
  summary: Yeast extract supports the complex/undefined classification. Iron powder
    or nails are supplied solids in a liquid medium, not a solidifying gel or evidence
    that the medium physical_state should be SOLID.
  target_ids:
  - CultureMech:001962
  evidence_ids:
  - target
  - dsmz815
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 46 current concentration fields are covered by 30 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001962
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","quantity_field_count":46,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 3-3","quote":"Na2SO4                                                   3.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    21.1208,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q2","label":"CaCl2 x
    2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 4-4","quote":"CaCl2 x 2 H2O                                            6.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\":
    40.8122,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q3","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"40","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"40","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 5-5","quote":"NaCl                                                    40.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 40,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\":
    684.463,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 6-6","quote":"KCl                                                      2.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    26.8276,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 7-7","quote":"NH4Cl                                                    0.30        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    5.60852,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q6","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 8-8","quote":"KH2PO4                                                   0.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.46967,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q7","label":"MgCl2 x
    6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 9-9","quote":"MgCl2 x 6 H2O                                            8.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\":
    39.3501,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q8","label":"SrCl2 x
    6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 10-10","quote":"SrCl2 x 6 H2O                                            0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"SrCl2 x 6 H2O\",\n                        \"compound_id\":
    176,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.37507,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q9","label":"MOPS","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 12-12","quote":"MOPS                                                     3.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"MOPS\",\n                        \"compound_id\":
    351,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    14.3362,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q10","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone.","source_stage":"Main formulation; explicit
    provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 13-13","quote":"Yeast extract                                            1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone."}]},{"quantity_id":"q11","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary gives 0.5 ml of an explicit 0.1% w/v sodium-resazurin stock, equivalent
    to 0.5 mg in the batch. API explicitly reports g_l=0.0005 and the local number
    agrees with that nominal rate. Retain the stock form/dose and distinguish this
    from measured final-medium concentration; source input water and API volume 1001
    ml do not independently establish a final-volume conversion. The sodium-salt grounding
    issue is separate.","source_stage":"Main formulation; explicit provider nominal
    g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 14-14","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    primary gives 0.5 ml of an explicit 0.1% w/v sodium-resazurin stock, equivalent
    to 0.5 mg in the batch. API explicitly reports g_l=0.0005 and the local number
    agrees with that nominal rate. Retain the stock form/dose and distinguish this
    from measured final-medium concentration; source input water and API volume 1001
    ml do not independently establish a final-volume conversion. The sodium-salt grounding
    issue is separate."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    primary gives 0.5 ml of an explicit 0.1% w/v sodium-resazurin stock, equivalent
    to 0.5 mg in the batch. API explicitly reports g_l=0.0005 and the local number
    agrees with that nominal rate. Retain the stock form/dose and distinguish this
    from measured final-medium concentration; source input water and API volume 1001
    ml do not independently establish a final-volume conversion. The sodium-salt grounding
    issue is separate."}]},{"quantity_id":"q12","label":"Iron powder","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. Primary also specifies iron powder or nails
    and a separate 1–2 g per-vessel instruction. Preserve both source controls and
    the nail alternative; absent vessel fill volume does not justify deriving a unique
    g/L from the vessel instruction.","source_stage":"Main formulation; explicit provider
    nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 15-15","quote":"Iron powder (or nails)                                 100.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Iron powder\",\n                        \"compound_id\":
    760,\n                        \"attribute\": \"or nails\",\n                        \"amount\":
    100,\n                        \"unit\": \"g\",\n                        \"g_l\":
    100,\n                        \"mmol_l\": 1790.67,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate,
    adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min
    to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave
    for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. Primary also specifies iron powder or nails
    and a separate 1–2 g per-vessel instruction. Preserve both source controls and
    the nail alternative; absent vessel fill volume does not justify deriving a unique
    g/L from the vessel instruction."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. Primary also specifies iron powder or nails
    and a separate 1–2 g per-vessel instruction. Preserve both source controls and
    the nail alternative; absent vessel fill volume does not justify deriving a unique
    g/L from the vessel instruction."}]},{"quantity_id":"q13","label":"Na-L-lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.6","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. The retained main preparation explicitly
    adds this compound from a separately prepared sterile anoxic stock; its stock
    concentration/volume is not supplied and must not be invented.","source_stage":"Main
    formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 16-16","quote":"Na-L-lactate                                             3.60        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na-L-lactate\",\n                        \"compound_id\":
    265,\n                        \"amount\": 3.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.6,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate,
    adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min
    to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave
    for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. The retained main preparation explicitly
    adds this compound from a separately prepared sterile anoxic stock; its stock
    concentration/volume is not supplied and must not be invented."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. The retained main preparation explicitly
    adds this compound from a separately prepared sterile anoxic stock; its stock
    concentration/volume is not supplied and must not be invented."}]},{"quantity_id":"q14","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. The retained main preparation explicitly
    adds this compound from a separately prepared sterile anoxic stock; its stock
    concentration/volume is not supplied and must not be invented.","source_stage":"Main
    formulation; explicit provider nominal g_l, primary batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 17-17","quote":"Na2CO3                                                   0.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    4.71751,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate,
    adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min
    to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave
    for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. The retained main preparation explicitly
    adds this compound from a separately prepared sterile anoxic stock; its stock
    concentration/volume is not supplied and must not be invented."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The
    local scalar and G_PER_L unit match the exact provider g_l assertion. The primary
    independently gives the batch mass. Credit this nominal provider rate while preserving
    its distinction from primary measured final volume: API declares volume 1001 ml
    but reports the nominal rates without dividing these masses by 1.001; the primary
    lists 1000 ml input water and no explicit final make-up. No numeric replacement
    is justified from those facts alone. The retained main preparation explicitly
    adds this compound from a separately prepared sterile anoxic stock; its stock
    concentration/volume is not supplied and must not be invented."}]},{"quantity_id":"q15","label":"Na2-EDTA
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 32-32","quote":"Na2-EDTA x 2 H2O                                         5.20       g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q16","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 33-33","quote":"FeCl2 x 4 H2O                                            1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q17","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 34-34","quote":"ZnCl2                                                   70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q18","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 35-35","quote":"MnCl2 x 4 H2O                                          100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q19","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 36-36","quote":"H3BO3                                                    6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q20","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 37-37","quote":"CoCl2 x 6 H2O                                          190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q21","label":"CuCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 38-38","quote":"CuCl2 x 2 H2O                                            2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q22","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 39-39","quote":"NiCl2 x 6 H2O                                           24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q23","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent.","source_stage":"SL-11
    stock with explicit 1000 ml final make-up","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 40-40","quote":"Na2MoO4 x 2 H2O                                         36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    primary explicitly brings SL-11 to 1000 ml, so this stock g/L is supported by
    its exact batch amount and final make-up, agreeing with provider stock g_l. That
    does not support its current main-ingredient placement. Restore the SL-11 stock
    and separate primary 1 ml batch receiving dose; do not treat the stock strength
    as a final-medium concentration. Chemical-form verification is independent."}]},{"quantity_id":"q24","label":"Main
    water input","local_fields":[],"decision":"evidence_only","rationale":"The primary
    includes 1000 ml distilled water, omitted locally. Preserve this solvent input
    in source-scoped preparation; it is not a measured final-volume statement.","source_stage":"Source-only
    main batch input","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 18-18","quote":"Distilled water                                       1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q25","label":"SL-11 receiving
    dose","local_fields":[],"decision":"evidence_only","rationale":"The primary adds
    1 ml SL-11 to the stated batch. Restore this separate dose and its embedded stock
    definition; a per-litre receiving basis is not independently supplied.","source_stage":"Source-only
    stock receiving dose","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 11-11","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q26","label":"Sodium-resazurin
    stock dose and strength","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the exact 0.5 ml stock addition and explicit 0.1% w/v strength. Their product
    is a 0.5 mg batch amount. Retaining the provider nominal g_l does not replace
    the source stock representation or prove final-volume measurement.","source_stage":"Source-only
    dye stock","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 14-14","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q27","label":"SL-11 water and
    final make-up","local_fields":[],"decision":"evidence_only","rationale":"The table
    lists 1000 ml water, while the preparation explicitly starts in 800 ml and brings
    final volume to 1000 ml. Preserve the final-make-up instruction as the stock denominator,
    rather than add 1000 ml after the initial 800 ml.","source_stage":"Source-only
    stock final-volume control","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 41-41","quote":"Distilled water                                       1000.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Retained final
    pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"The
    retained pH 7.2 agrees with the exact main preparation. It must remain distinct
    from preliminary main pH6 and stock adjustments pH 7 then 6.","source_stage":"Final
    main-medium pH","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate,
    adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min
    to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave
    for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with
    NaOH and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense
    medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    containing 1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105\\u00b0C.
    Before use add lactate from a sterile anoxic stock solutions prepared under 100%
    N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas atmosphere. Final medium pH should be 7.2.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    retained pH 7.2 agrees with the exact main preparation. It must remain distinct
    from preliminary main pH6 and stock adjustments pH 7 then 6."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    retained pH 7.2 agrees with the exact main preparation. It must remain distinct
    from preliminary main pH6 and stock adjustments pH 7 then 6."}]},{"quantity_id":"q29","label":"Retained
    main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and
    sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing
    1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use
    add lactate from a sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2
    gas atmosphere. Final medium pH should be 7.2."}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients except iron, lactate and carbonate, adjust pH to 6.0 with NaOH and
    sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing
    1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105°C. Before use
    add lactate from a sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2
    gas atmosphere. Final medium pH should be 7.2."}}],"decision":"evidence_only","rationale":"The
    existing text and AUTOCLAVE classification preserve the primary main procedure,
    including pH 6, 100% N2 for 30–45 min, vessel iron 1–2 g or nail, 105°C for 30
    min, later lactate/carbonate additions and pH 7.2. Keep that exact context and
    gas distinction. Do not infer unspecified stock strengths or vessel fill volume.","source_stage":"Retained
    main preparation","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 20-26","quote":"Dissolve ingredients except iron, lactate and carbonate,
    adjust pH to 6.0 with NaOH and\nsparge medium with 100% N2 gas for 30 - 45 min
    to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials containing 1 -\n2 g iron powder or an iron nail. Autoclave
    for 30 min at 105°C. Before use add lactate from\na sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate from a sterile\nanoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium\npH should be 7.2.","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except iron, lactate and carbonate, adjust pH to 6.0 with
    NaOH and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense
    medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    containing 1 - 2 g iron powder or an iron nail. Autoclave for 30 min at 105\\u00b0C.
    Before use add lactate from a sterile anoxic stock solutions prepared under 100%
    N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas atmosphere. Final medium pH should be 7.2.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing text and AUTOCLAVE classification preserve the primary main procedure,
    including pH 6, 100% N2 for 30–45 min, vessel iron 1–2 g or nail, 105°C for 30
    min, later lactate/carbonate additions and pH 7.2. Keep that exact context and
    gas distinction. Do not infer unspecified stock strengths or vessel fill volume."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing text and AUTOCLAVE classification preserve the primary main procedure,
    including pH 6, 100% N2 for 30–45 min, vessel iron 1–2 g or nail, 105°C for 30
    min, later lactate/carbonate additions and pH 7.2. Keep that exact context and
    gas distinction. Do not infer unspecified stock strengths or vessel fill volume."}]},{"quantity_id":"q30","label":"Retained
    SL-11 preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous
    chloride. After ferrous chloride has dissolved add other compounds. Finally adjust
    pH to 6.0 and bring volume to 1000 ml."}},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous
    chloride. After ferrous chloride has dissolved add other compounds. Finally adjust
    pH to 6.0 and bring volume to 1000 ml."}}],"decision":"correct","rationale":"The
    words and ADJUST_PH action are source-supported, including 800 ml starting water,
    pH 7 with 2 N NaOH, addition order, final pH 6 and 1000 ml make-up. Correct the
    current root sequence placement by binding it only to SL-11; it must not reset
    the final medium pH 7.2 or volume.","source_stage":"SL-11 preparation only","sources":[{"evidence_id":"dsmz815","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815.pdf","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/dsmz815.bin","raw_sha256":"7e534dbe42588e038cdbb1070530cf89cdf6bbcb205c2ef6289b30dcb0c16c2d","text_sha256":"266cae9e4c5d9a2854e5c9844834af93690577d24b2e0eac767f7380ec333014","accessed_at":"2026-10-28T19:39:10.150713Z","locator":"dsmz815.txt
    lines 43-45","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api815","reference":"https://mediadive.dsmz.de/rest/medium/815","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/api815.bin","raw_sha256":"75df1ad19cd640d9f831ce251a1a4c147c4c8e1c8c8bc9ccf1b132463b544d87","text_sha256":"6d23d93242112f7420cb63a53ab66c23bbf6048fd998cda7376158b19764ceb9","accessed_at":"2026-10-28T19:39:09.826827Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    words and ADJUST_PH action are source-supported, including 800 ml starting water,
    pH 7 with 2 N NaOH, addition order, final pH 6 and 1000 ml make-up. Correct the
    current root sequence placement by binding it only to SL-11; it must not reset
    the final medium pH 7.2 or volume."},{"path":"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    words and ADJUST_PH action are source-supported, including 800 ml starting water,
    pH 7 with 2 N NaOH, addition order, final pH 6 and 1000 ml make-up. Correct the
    current root sequence placement by binding it only to SL-11; it must not reset
    the final medium pH 7.2 or volume."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOHALOTOMACULUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All 22 asserted chemical objects and exact current MIM rows are assessed.
    Confirmed mismatches are neutral resazurin versus the source sodium salt, and
    anhydrous nickel versus the specified hexahydrate. L-sodium lactate, elemental
    iron, disodium EDTA dihydrate and the other explicit hydrates are supported by
    current scientific ontology objects. MOPS is returned as a broad named buffer
    class without a supplied formula; no stronger structural claim is made. Rejected
    lexical rows for iron powder, EDTA or cobalt coexist with mapped equivalent names
    and do not negate the matching chemical form. Broad catalogue synonyms are not
    chemically certified; optional yeast identifiers are not endorsed.
  target_ids:
  - CultureMech:001962
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All three full historical reports were read. The October7 parent has 23
    local unresolved concentration claims and 28 exact source recipe/step objects;
    current API raw digest matches its recorded digest. This authenticates content,
    not the old retrieval event or writer execution. The old blanket stock-topology
    conflict does not negate the fourteen explicit main provider rates; the nine stock
    placements remain wrong. Target and owner scientific fields are equal. Current
    singleton merger preserves owner content and current MediaDive composition behavior
    is improved, while preparation concatenation still loses stage labels.
  target_ids:
  - CultureMech:001962
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-source-joins
  - historical-reading
  - historical-selected-parent-rows
  - writer-mediadive
  - selected-parent-authentication
findings:
- finding_id: f1
  issue_key: culturemech-001962-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Nine SL-11 stock strengths are flattened into the main formulation
  description: Restore the nine SL-11 components, its explicit 1000 ml final make-up
    and separate 1 ml batch dose. Their stock strengths are supported; their root
    final-medium placement is not. Preserve the main nominal provider rates and input-water
    distinction, and represent the sodium-resazurin stock dose/strength explicitly.
    Current composition parsing now excludes this stock reference and dye stock, so
    it should not recreate historical flattening; review bare-ml normalization before
    regeneration.
  target_ids:
  - CultureMech:001962
  field_paths:
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[21].concentration
  - ingredients[22].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz815
  - api815
  - quantities
  - writer-mediadive
  rule_id: custom/stock-stage-and-basis
  native_severity: P2
  normalization_reason: Exact source-specific stock-stage-and-basis issue; normalized
    major without redefining a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current primary composition, stock-dose and preparation writer
- finding_id: f2
  issue_key: culturemech-001962-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two chemical assertions do not match the supplied forms
  description: Sodium resazurin is linked to neutral CHEBI:8806, whose formula lacks
    the sodium counterion; resolve an exact sodium-salt identifier and label rather
    than accept the broad catalogue synonym. Nickel hexahydrate is linked to anhydrous
    CHEBI:34887 in both primary and secondary slots; candidate CHEBI:53542 matches
    the source hydrate. Preserve all source amounts and source stages. MIM Nickel
    (II) chloride hexahydrate is a mapped preferred row 6668, while NiCl2 x 6 H2O
    is rejected preferred row 6703 and mapped synonym 6704; no whole-identifier rejection
    is implied.
  target_ids:
  - CultureMech:001962
  field_paths:
  - ingredients[10].term
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz815
  - api815
  - groundings
  - mim
  - chebi53542
  rule_id: custom/supplied-form-identity
  native_severity: P2
  normalization_reason: Exact source-specific supplied-form-identity issue; normalized
    major without redefining a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001962-stock-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SL-11 preparation is presented as a main-medium step
  description: Retain the supported stock preparation text and ADJUST_PH action, but
    move its field scope to SL-11. The stock pH 7 then 6 and 1000 ml final volume
    must not override the main pH 7.2 or invent a main final volume. Current preparation
    collection concatenates steps from all solution sections without stage labels;
    preserve those labels in generated representation.
  target_ids:
  - CultureMech:001962
  field_paths:
  - preparation_steps[1]
  - ph_value
  evidence_ids:
  - dsmz815
  - api815
  - writer-mediadive
  - quantities
  rule_id: custom/preparation-stage-placement
  native_severity: P2
  normalization_reason: Exact source-specific preparation-stage-placement issue; normalized
    major without redefining a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current primary composition, stock-dose and preparation writer
- finding_id: f4
  issue_key: culturemech-001962-claim-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Supported assertions lack attached claim evidence
  description: Attach exact ingredient evidence for chemical quantities and root evidence
    with field/stage scope for stock doses, water, pH and preparation. No attached
    claims currently exist. Historical raw-byte matches are separate from attached
    evidence and original retrieval-event verification. Do not create nonexistent
    evidence fields on concentration or solution descriptors.
  target_ids:
  - CultureMech:001962
  field_paths:
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - dsmz815
  - api815
  - old-claims
  - historical-source-joins
  rule_id: custom/claim-evidence-completeness
  native_severity: P3
  normalization_reason: Exact source-specific claim-evidence-completeness issue; normalized
    minor without redefining a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Restore the nine SL-11 components, its explicit 1000 ml final make-up
    and separate 1 ml batch dose. Their stock strengths are supported; their root
    final-medium placement is not. Preserve the main nominal provider rates and input-water
    distinction, and represent the sodium-resazurin stock dose/strength explicitly.
    Current composition parsing now excludes this stock reference and dye stock, so
    it should not recreate historical flattening; review bare-ml normalization before
    regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001962
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current primary composition, stock-dose and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Sodium resazurin is linked to neutral CHEBI:8806, whose formula lacks
    the sodium counterion; resolve an exact sodium-salt identifier and label rather
    than accept the broad catalogue synonym. Nickel hexahydrate is linked to anhydrous
    CHEBI:34887 in both primary and secondary slots; candidate CHEBI:53542 matches
    the source hydrate. Preserve all source amounts and source stages. MIM Nickel
    (II) chloride hexahydrate is a mapped preferred row 6668, while NiCl2 x 6 H2O
    is rejected preferred row 6703 and mapped synonym 6704; no whole-identifier rejection
    is implied.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001962
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
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
  description: Retain the supported stock preparation text and ADJUST_PH action, but
    move its field scope to SL-11. The stock pH 7 then 6 and 1000 ml final volume
    must not override the main pH 7.2 or invent a main final volume. Current preparation
    collection concatenates steps from all solution sections without stage labels;
    preserve those labels in generated representation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001962
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current primary composition, stock-dose and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: Attach exact ingredient evidence for chemical quantities and root evidence
    with field/stage scope for stock doses, water, pH and preparation. No attached
    claims currently exist. Historical raw-byte matches are separate from attached
    evidence and original retrieval-event verification. Do not create nonexistent
    evidence fields on concentration or solution descriptors.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001962
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfohalotomaculum_medium.yaml
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
- Only the SL-11 definition printed within DSM815 is used. The other formulation of
  parent medium 722 and DSM815a are excluded.
- The exact primary gives an explicit final volume only for SL-11. Main API volume
  1001 ml and nominal g_l values are recorded separately; unused provider mmol_l conversions
  are not validated.
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
