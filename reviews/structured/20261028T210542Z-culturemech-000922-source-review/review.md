# Scientific review: DESULFOSOMA MEDIUM

- Review: 20261028T210542Z-culturemech-000922-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:57:35.444984Z
- Finished UTC: 2026-10-28T21:05:42.571532Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The 15 main rates and retained main method/pH are positively supported. SL-10 stock placement and step scope, two supplied-form identities, and missing claim/link metadata need curation; quantities were not silently normalized.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch078 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000922 | data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml | generated | desulfosoma_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:000922 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:000922 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:000922 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:000922 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source identity

identity: supported. Targets: CultureMech:000922.

The generated target and sole maintained DSM 1456 owner correspond to the fresh primary and provider. No neighboring record is used as a formulation donor.

### Complex liquid classification

consistency: supported. Targets: CultureMech:000922.

COMPLEX/UNDEFINED and LIQUID fit the printed yeast extract and Trypticase peptone formulation. No strain-growth claim is inferred.

### Original diagnostics

schema: supported. Targets: CultureMech:000922.

The original four canonical diagnostics exited 0. Zero reference checks are not evidence verification.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:000922.

48 current concentration fields are covered by 30 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b078-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","quantity_field_count":48,"decisions":[{"quantity_id":"q1","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 3-3","quote":"K2HPO4                                                     0.30         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 4-4","quote":"KH2PO4                                                     0.30         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 5-5","quote":"NaCl                                                       1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 6-6","quote":"NH4Cl                                                      1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 7-7","quote":"KCl                                                        0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 8-8","quote":"CaCl2 x 2 H2O                                              0.10         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 9-9","quote":"MgCl2 x 6 H2O                                              0.50         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.45938,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.8","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 10-10","quote":"Na2SO4                                                     2.80         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 2.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.8,\n                        \"mmol_l\": 19.7128,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 11-11","quote":"Yeast extract (OXOID)                                      1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Trypticase peptone","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 12-12","quote":"Trypticase peptone (BD BBL)                                1.00         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists. The explicit 0.1% w/v stock and 0.5 ml addition support 0.0005 g; supplied sodium-salt identity is assessed separately.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 14-14","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 15-15","quote":"Na2CO3                                                     1.50         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 14.1525,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Na-pyruvate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 16-16","quote":"Na-pyruvate                                                2.50         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 22.7182,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 17-17","quote":"L-Cysteine HCl x H2O                                       0.50         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.8468,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider object explicitly reports this g/L rate and the primary prints its corresponding amount. Credit that source normalization without silently dividing by provider volume metadata 1001 ml or asserting measured final volume from listed water. No attached local concentration claim currently exists.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 18-18","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.08175,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies 10 ml of HCl labelled 25%, and the provider reports g_l 2.5. The primary does not specify percentage basis or density, so the mass conversion is not independently justified. Preserve native volume/label, resolve the basis and relocate this component under SL-10.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 33-33","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 34-34","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 35-35","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 36-36","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 37-37","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 38-38","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 39-39","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 40-40","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The unchanged numeric rate is supported for SL-10, whose primary explicitly makes the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium role; retain the stock rate under its named solution and restore the 1 ml receiving addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 41-41","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"SL-10 receiving addition","local_fields":[],"decision":"correct","rationale":"Represent the printed 1 ml stock addition as a batch volume, with its explicit separate SL-10 preparation. Do not infer a per-litre dose solely from the input-water value.","source_stage":"Main solution receives SL-10","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 13-13","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Source water input 0","local_fields":[],"decision":"evidence_only","rationale":"Retain the printed water amount in its exact stage. The main water input does not establish measured final volume; SL-10 has a distinct explicit final makeup statement.","source_stage":"Main water","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 19-19","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[16]","quote":"{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Source water input 1","local_fields":[],"decision":"evidence_only","rationale":"Retain the printed water amount in its exact stage. The main water input does not establish measured final volume; SL-10 has a distinct explicit final makeup statement.","source_stage":"SL-10 water","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 42-42","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q28","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients except carbonate, pyruvate, cysteine and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate (sterilized by filtration), cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary."}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients except carbonate, pyruvate, cysteine and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate (sterilized by filtration), cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary."}}],"decision":"evidence_only","rationale":"Credit the full retained method: 80% N2/20% CO2, 30–45 minutes, separate sterilizations and stock atmospheres. These instructions already survive in both documents; no absent-method finding is made.","source_stage":"Main preparation","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 21-27","quote":"Dissolve ingredients except carbonate, pyruvate, cysteine and sulfide, then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense\nmedium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials\nand autoclave. Add pyruvate (sterilized by filtration), cysteine and sulfide from sterile\nanoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic\nstock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of\ncomplete medium to 7.0 - 7.2, if necessary.","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients except carbonate, pyruvate, cysteine and sulfide, then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate (sterilized by filtration), cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Retained final pH range","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}}],"decision":"evidence_only","rationale":"The retained 7.0–7.2 range is explicitly printed for the complete medium. Preserve it unchanged and attach scoped evidence.","source_stage":"Final medium","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 26-27","quote":"stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of\ncomplete medium to 7.0 - 7.2, if necessary.","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.medium","quote":"{\n            \"id\": 1456,\n            \"name\": \"DESULFOSOMA MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7.2,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf\"\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"SL-10 makeup step","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The unchanged dissolution text and 1000 ml makeup are supported for SL-10. Their unqualified placement as a main preparation step needs explicit stock scoping, without changing the text or amount.","source_stage":"SL-10 preparation","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfosoma_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:000922.

Every asserted ontology slot and exact current MIM row was checked. L-cysteine hydrochloride monohydrate, sodium pyruvate and the other specified salt hydrates agree with the current scientific objects. Nickel hexahydrate and sodium resazurin have the distinct form problems reported above. Local NiCl2 x 6 H2O preferred-spelling rows are REJECTED; the differently spelled Nickel (II) chloride hexahydrate counterpart is MAPPED. Exact mapping status is not supplied-form validation. Unlinked yeast/peptone have current packaged preferred-term candidates, not asserted ontology claims.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:000922.

All three complete reports and the selected historical parent were read. The current API 1456 raw digest equals the historical digest; current owner bytes match the unchanged before/after hashes. Exact source objects are separately authenticated, while null prior concentration snippets remain unverified. The prior blanket stock-topology flag does not erase fresh positive support for the 15 main rates. Current importer source-step flattening and bare ml normalization remain bounded current-code observations, not reconstructed historical execution.

## Findings

### f1: Restore the SL-10 stock boundary

major / open / confirmed; issue key: culturemech-000922-sl10-stage.

The 15 main ingredient rates have direct provider support and remain unchanged. The nine SL-10 components are flattened at stock strength into main ingredients; restore the named stock and printed 1 ml receiving addition. Its explicit 1000 ml makeup supports solid-component stock rates. Preserve HCl 25% as a native volume/label until its mass basis is resolved.

### f2: Scope the retained SL-10 preparation step

major / open / confirmed; issue key: culturemech-000922-stock-step-scope.

Both documents preserve the complete main preparation and correct final pH range. Their second preparation step is the separately supported SL-10 dissolution and makeup method, but it is unqualified at the main level. Preserve its text under an explicit SL-10 stock container.

### f3: Reconcile the nickel hexahydrate identity

major / open / confirmed; issue key: culturemech-000922-nickel-hydrate.

The exact preferred term and source specify nickel chloride hexahydrate, while primary and secondary CHEBI:34887 slots represent anhydrous nickel dichloride. Current CHEBI:53542 explicitly contains six waters. Correct supplied-form identity independently of the unchanged stock amount.

### f4: Resolve sodium resazurin supplied form

major / open / confirmed; issue key: culturemech-000922-resazurin-sodium-form.

The source and preferred term name sodium resazurin, but the asserted CHEBI:8806 describes neutral resazurin. Resolve the salt identity without replacing it with a guessed concept or changing the supported native stock addition.

### f5: Attach scoped claims and complete supported ingredient links

minor / open / confirmed; issue key: culturemech-000922-claim-and-link-completeness.

No local concentration claim is attached. Add exact source-stage evidence for supported unchanged main rates and corrected stock placement. Yeast extract and Trypticase peptone also lack primary/secondary links despite exact packaged preferred-term mappings; assess those current candidates with the printed product scope, without inventing a chemical formula for these complex ingredients.

## Recommended Actions And Acceptance Checks

### a1

The 15 main ingredient rates have direct provider support and remain unchanged. The nine SL-10 components are flattened at stock strength into main ingredients; restore the named stock and printed 1 ml receiving addition. Its explicit 1000 ml makeup supports solid-component stock rates. Preserve HCl 25% as a native volume/label until its mass basis is resolved.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Both documents preserve the complete main preparation and correct final pH range. Their second preparation step is the separately supported SL-10 dissolution and makeup method, but it is unqualified at the main level. Preserve its text under an explicit SL-10 stock container.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The exact preferred term and source specify nickel chloride hexahydrate, while primary and secondary CHEBI:34887 slots represent anhydrous nickel dichloride. Current CHEBI:53542 explicitly contains six waters. Correct supplied-form identity independently of the unchanged stock amount.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The source and preferred term name sodium resazurin, but the asserted CHEBI:8806 describes neutral resazurin. Resolve the salt identity without replacing it with a guessed concept or changing the supported native stock addition.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

No local concentration claim is attached. Add exact source-stage evidence for supported unchanged main rates and corrected stock placement. Yeast extract and Trypticase peptone also lack primary/secondary links despite exact packaged preferred-term mappings; assess those current candidates with the printed product scope, without inventing a chemical formula for these complex ingredients.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm1456 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf; REVIEW_WORK/batch078/source07-08-10/dsm1456.json; exact original raw/text/hash/time metadata | context_only | Exact selected primary; whole recipe and embedded stock sections retain their own stages. |
| api1456 | https://mediadive.dsmz.de/rest/medium/1456; REVIEW_WORK/batch078/source07-08-10/api1456.json; exact original raw/text/hash/time metadata | context_only | Exact current selected provider recipe, retaining explicit stage-specific rates. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch078/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfosoma_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/desulfosoma_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSOMA_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosoma_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch078/record08/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch078/record08/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch078/record08/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch078/record08/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| historical-parent-authentication | REVIEW_WORK/batch078/record08/historical-parent-authentication.json; Exact selected parent row; literal and raw digest checks separate | context_only | Current raw content matching is independent of original retrieval provenance; null snippets remain null. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; REVIEW_WORK/batch078/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch078/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch078/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch078/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch078/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch078/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch078/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch078/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch078/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; REVIEW_WORK/batch078/source07-08-10/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; REVIEW_WORK/batch078/source07-08-10/chebi50144.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; REVIEW_WORK/batch078/source07-08-10/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch078/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; REVIEW_WORK/batch078/source07-08-10/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch078/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch078/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch078/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch078/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch078/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch078/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch078/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch078/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch078/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch078/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch078/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch078/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch078/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch078/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch078/record08/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims in this scoped sidecar; historical object joins are separate evidence. |
| check-schema | REVIEW_WORK/batch078/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch078/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch078/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch078/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The provider records volume 1001 ml while its main g_l values use the printed nominal litre amounts. Preserve explicit provider rates and the metadata discrepancy; no measured final-volume normalization is inferred.
- HCl 25% has no explicit primary percentage basis or density. No active salt-form replacement is inferred from synonym matching alone.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T210542Z-culturemech-000922-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOSOMA MEDIUM'
started_at: '2026-10-28T20:57:35.444984Z'
finished_at: '2026-10-28T21:05:42.571532Z'
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
summary: The 15 main rates and retained main method/pH are positively supported. SL-10
  stock placement and step scope, two supplied-form identities, and missing claim/link
  metadata need curation; quantities were not silently normalized.
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
  - path: data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml
    sha256: 973b9c107aa8e17af89c8dc6e940915cabedbf15eeae2356f33f00111aa802c7
    role: target
  - path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
    sha256: 0a433f1a84d2a5b87cb85f97c74cd227b96e2cf442a0fdfbede7dd141b4ff11b
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/desulfosoma_medium.yaml.md
    sha256: 1e784512b5eb218ea27cb58bed5962e71b7ad8fb93f692f392c9cfc13a94a032
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSOMA_MEDIUM.md
    sha256: e6bbdc11efb7e3d36b0d716ba632793e6816cd827d2510746f9577f80cdae487
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosoma_medium.md
    sha256: cb05b432078d68b97be76041e02ba1dc9a0386d69f2fb574424df53ff3840419
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
  - path: scripts/fetch_komodo_base_volumes.py
    sha256: 9dad49c380422b2e7d3f40b4ff713d59360d22f6eec9b55068e050099cb9cffa
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
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
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  selection: Authoritative batch078 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000922
targets:
- target_id: CultureMech:000922
  path: data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml
  label: desulfosoma_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
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
  - CultureMech:000922
  command: just validate-schema data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml
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
  - CultureMech:000922
  command: just validate-strict data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml --out
    REVIEW_WORK/batch078/record08/strict.tsv --workers 1 --quiet
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
  - CultureMech:000922
  command: just validate-terms data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml
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
  - CultureMech:000922
  command: just validate-references data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm1456
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf
  accessed_at: '2026-10-28T20:57:52.047869Z'
  locator: REVIEW_WORK/batch078/source07-08-10/dsm1456.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected primary; whole recipe and embedded stock sections retain
    their own stages.
  snapshot_sha256: 5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811
- evidence_id: api1456
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1456
  accessed_at: '2026-10-28T20:57:51.390708Z'
  locator: REVIEW_WORK/batch078/source07-08-10/api1456.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current selected provider recipe, retaining explicit stage-specific
    rates.
  snapshot_sha256: 794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T20:57:55.582950Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:05:42.482570Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 973b9c107aa8e17af89c8dc6e940915cabedbf15eeae2356f33f00111aa802c7
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:05:42.482763Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 0a433f1a84d2a5b87cb85f97c74cd227b96e2cf442a0fdfbede7dd141b4ff11b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T21:05:42.482794Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T21:05:42.483105Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T21:05:42.483130Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T21:05:42.483152Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:05:42.483178Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/desulfosoma_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T21:05:42.488873Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1e784512b5eb218ea27cb58bed5962e71b7ad8fb93f692f392c9cfc13a94a032
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSOMA_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T21:05:42.488937Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: e6bbdc11efb7e3d36b0d716ba632793e6816cd827d2510746f9577f80cdae487
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosoma_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T21:05:42.488968Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: cb05b432078d68b97be76041e02ba1dc9a0386d69f2fb574424df53ff3840419
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/historical-reading.json
  accessed_at: '2026-10-28T21:05:42.493057Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: d367c8615afc6a1377c3eedfbe63783c85a3d448a021fa7f1007fdec9fe6d205
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:05:42.493099Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: efca0686761e4d67418f5b9d3327ebe823517c3618843e933f6bacd752736166
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/complete-document-reader.json
  accessed_at: '2026-10-28T21:05:42.493141Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 3b6aca60733f18ac52058d5c3948684c93dca496f738ef84cec52e91aed1860a
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T21:05:42.493172Z'
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
  accessed_at: '2026-10-28T21:05:42.493206Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch078/record08/historical-current-object-joins.json
  accessed_at: '2026-10-28T21:05:42.493230Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 945a36a418d5d24afd779f4fdc1e83caf3053f299532cebdadef6cf3d31b4cab
- evidence_id: historical-parent-authentication
  kind: prior_review
  reference: REVIEW_WORK/batch078/record08/historical-parent-authentication.json
  accessed_at: '2026-10-28T21:05:42.493280Z'
  locator: Exact selected parent row; literal and raw digest checks separate
  support: context_only
  summary: Current raw content matching is independent of original retrieval provenance;
    null snippets remain null.
  snapshot_sha256: 9a9fe3a318d7ed2c3254d94aa24e8724e32e2ef0be26dbb7d29b1bcdf1b3856e
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  accessed_at: '2026-10-28T20:57:52.741596Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T20:57:55.820751Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T20:57:53.394246Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T20:57:53.788390Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T20:57:54.528493Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T20:57:56.790414Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T20:57:57.069072Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T20:57:54.037990Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T20:57:57.653392Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  accessed_at: '2026-10-28T20:57:53.407299Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi29377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  accessed_at: '2026-10-28T20:57:55.240291Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi50144.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  accessed_at: '2026-10-28T20:57:58.143428Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi91248.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T20:57:56.416990Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  accessed_at: '2026-10-28T20:57:53.185663Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi17883.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  accessed_at: '2026-10-28T20:57:57.016466Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T20:57:55.211394Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  accessed_at: '2026-10-28T20:57:57.543008Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T20:57:54.626226Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T20:57:55.246687Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T20:57:57.074069Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T20:57:54.649502Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T20:57:56.189397Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.570708Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: c5f99959691e3ae159c123eeecc902b0a51da61eaa01dadc02c41637a2805164
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.570771Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: ff0ad060e44152e8369c7531deaf9e642ef07e9ae92ef14120b47b25f873679d
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.570874Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 312ef0d5058791ea568691e9c3804cb5e518c1ebf2dec640c7721085b9a88af7
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.570918Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 47c59c17e25d740be958d0c60c033d69f621e8a22c9b454edc810a89c5487f6a
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.570961Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 9136825f6e37d84ed18dd21f6cfca4e43a3125980f5df462ac44991d9b9b8128
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.570986Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 3a9c415db820f6b7ba412e51f334f7dddcd1f67314a227a41dbe1ba4f4ec5e6f
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch078/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:05:42.571006Z'
  support: context_only
  summary: No attached claims in this scoped sidecar; historical object joins are
    separate evidence.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch078/record08/schema-result.json
  accessed_at: '2026-10-28T20:57:36.539096Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 6035418d0e21a6690b94962e89eeb82d2343957823f2b538ee602b719e9324e7
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch078/record08/strict-result.json
  accessed_at: '2026-10-28T20:57:37.478774Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 10d3b8598b78bd723dc1c404b886e80706f7651423ec8fa8ed25ddd233df528a
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch078/record08/terms-result.json
  accessed_at: '2026-10-28T20:57:38.512644Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0f2616e249afe19e9aaffe85bf7dc92de53df0d7339712dd5c3433bf4ad96928
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch078/record08/references-result.json
  accessed_at: '2026-10-28T20:57:39.227811Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: b3cc16b3695b3a552ed75f92eae7d0d5b0fe4695f51ffaeb46ca7d69f72e8ed2
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source identity
  outcome: supported
  summary: The generated target and sole maintained DSM 1456 owner correspond to the
    fresh primary and provider. No neighboring record is used as a formulation donor.
  target_ids:
  - CultureMech:000922
  evidence_ids:
  - target
  - owner
  - dsm1456
  - api1456
- assessment_id: classification
  area: consistency
  topic: Complex liquid classification
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID fit the printed yeast extract and Trypticase
    peptone formulation. No strain-growth claim is inferred.
  target_ids:
  - CultureMech:000922
  evidence_ids:
  - target
  - owner
  - dsm1456
  - api1456
- assessment_id: schema
  area: schema
  topic: Original diagnostics
  outcome: supported
  summary: The original four canonical diagnostics exited 0. Zero reference checks
    are not evidence verification.
  target_ids:
  - CultureMech:000922
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 48 current concentration fields are covered by 30 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:000922
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b078-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","quantity_field_count":48,"decisions":[{"quantity_id":"q1","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 3-3","quote":"K2HPO4                                                     0.30         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.7224,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 4-4","quote":"KH2PO4                                                     0.30         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    2.2045,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 5-5","quote":"NaCl                                                       1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 6-6","quote":"NH4Cl                                                      1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 7-7","quote":"KCl                                                        0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    1.34138,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 8-8","quote":"CaCl2 x 2 H2O                                              0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 9-9","quote":"MgCl2 x 6 H2O                                              0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.45938,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.8","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 10-10","quote":"Na2SO4                                                     2.80         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 2.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.8,\n                        \"mmol_l\":
    19.7128,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 11-11","quote":"Yeast extract (OXOID)                                      1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Trypticase peptone","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 12-12","quote":"Trypticase peptone (BD BBL)                                1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists. The
    explicit 0.1% w/v stock and 0.5 ml addition support 0.0005 g; supplied sodium-salt
    identity is assessed separately.","source_stage":"Main solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 14-14","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 15-15","quote":"Na2CO3                                                     1.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    14.1525,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"Na-pyruvate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 16-16","quote":"Na-pyruvate                                                2.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\":
    113,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    22.7182,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 17-17","quote":"L-Cysteine HCl x H2O                                       0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.8468,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider object explicitly reports this g/L rate and the primary
    prints its corresponding amount. Credit that source normalization without silently
    dividing by provider volume metadata 1001 ml or asserting measured final volume
    from listed water. No attached local concentration claim currently exists.","source_stage":"Main
    solution","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 18-18","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.08175,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies 10 ml of HCl labelled 25%, and the provider reports g_l 2.5.
    The primary does not specify percentage basis or density, so the mass conversion
    is not independently justified. Preserve native volume/label, resolve the basis
    and relocate this component under SL-10.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 33-33","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 34-34","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 35-35","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 36-36","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 37-37","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q21","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 38-38","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q22","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 39-39","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 40-40","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    unchanged numeric rate is supported for SL-10, whose primary explicitly makes
    the stock up to 1000 ml. Its root ingredient placement falsely gives a main-medium
    role; retain the stock rate under its named solution and restore the 1 ml receiving
    addition.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 41-41","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q25","label":"SL-10 receiving addition","local_fields":[],"decision":"correct","rationale":"Represent
    the printed 1 ml stock addition as a batch volume, with its explicit separate
    SL-10 preparation. Do not infer a per-litre dose solely from the input-water value.","source_stage":"Main
    solution receives SL-10","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 13-13","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"Source water input 0","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the printed water amount in its exact stage. The main water input does not establish
    measured final volume; SL-10 has a distinct explicit final makeup statement.","source_stage":"Main
    water","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 19-19","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].recipe[16]","quote":"{\n                        \"recipe_order\":
    17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Source water input 1","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the printed water amount in its exact stage. The main water input does not establish
    measured final volume; SL-10 has a distinct explicit final makeup statement.","source_stage":"SL-10
    water","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 42-42","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q28","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients except carbonate, pyruvate, cysteine and sulfide, then sparge medium
    with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense
    medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Add pyruvate (sterilized by filtration), cysteine and sulfide from
    sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a
    sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior
    to use adjust pH of complete medium to 7.0 - 7.2, if necessary."}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients except carbonate, pyruvate, cysteine and sulfide, then sparge medium
    with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense
    medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Add pyruvate (sterilized by filtration), cysteine and sulfide from
    sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a
    sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Prior
    to use adjust pH of complete medium to 7.0 - 7.2, if necessary."}}],"decision":"evidence_only","rationale":"Credit
    the full retained method: 80% N2/20% CO2, 30–45 minutes, separate sterilizations
    and stock atmospheres. These instructions already survive in both documents; no
    absent-method finding is made.","source_stage":"Main preparation","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 21-27","quote":"Dissolve ingredients except carbonate, pyruvate, cysteine
    and sulfide, then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 -
    45 min to make it anoxic. Dispense\nmedium under the same gas atmosphere into
    anoxic Hungate-type tubes or serum vials\nand autoclave. Add pyruvate (sterilized
    by filtration), cysteine and sulfide from sterile\nanoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic\nstock solution prepared
    under 80% N2 and 20% CO2 gas mixture. Prior to use adjust pH of\ncomplete medium
    to 7.0 - 7.2, if necessary.","quote_basis":"derivative text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients except carbonate, pyruvate, cysteine and sulfide, then
    sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.
    Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or
    serum vials and autoclave. Add pyruvate (sterilized by filtration), cysteine and
    sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate
    from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.
    Prior to use adjust pH of complete medium to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"Retained final pH range","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"ph_range","stored":{"min":7.0,"max":7.2}}],"decision":"evidence_only","rationale":"The
    retained 7.0–7.2 range is explicitly printed for the complete medium. Preserve
    it unchanged and attach scoped evidence.","source_stage":"Final medium","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 26-27","quote":"stock solution prepared under 80% N2 and 20% CO2 gas mixture.
    Prior to use adjust pH of\ncomplete medium to 7.0 - 7.2, if necessary.","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.medium","quote":"{\n            \"id\":
    1456,\n            \"name\": \"DESULFOSOMA MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7.2,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf\"\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"SL-10 makeup step","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/desulfosoma_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The unchanged
    dissolution text and 1000 ml makeup are supported for SL-10. Their unqualified
    placement as a main preparation step needs explicit stock scoping, without changing
    the text or amount.","source_stage":"SL-10 preparation","sources":[{"evidence_id":"dsm1456","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1456.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm1456.raw","raw_sha256":"5b6d65f494ec44eabc8537ef20e59cc7108cf169d79120b80717cbcaa2ef6811","text_sha256":"91944b86faaa3a86418ff6c8788abe04815fe861a3dfd946a20f5f497fa06ea9","accessed_at":"2026-10-28T20:57:52.047869Z","locator":"dsm1456.txt
    lines 44-45","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api1456","reference":"https://mediadive.dsmz.de/rest/medium/1456","raw_path":"REVIEW_WORK/batch078/source07-08-10/api1456.raw","raw_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","text_sha256":"794047ecc0a491f31754d24ab59eaf56ee5c095a169777c5f5b3bc3327e4ab97","accessed_at":"2026-10-28T20:57:51.390708Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfosoma_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every asserted ontology slot and exact current MIM row was checked. L-cysteine
    hydrochloride monohydrate, sodium pyruvate and the other specified salt hydrates
    agree with the current scientific objects. Nickel hexahydrate and sodium resazurin
    have the distinct form problems reported above. Local NiCl2 x 6 H2O preferred-spelling
    rows are REJECTED; the differently spelled Nickel (II) chloride hexahydrate counterpart
    is MAPPED. Exact mapping status is not supplied-form validation. Unlinked yeast/peptone
    have current packaged preferred-term candidates, not asserted ontology claims.
  target_ids:
  - CultureMech:000922
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All three complete reports and the selected historical parent were read.
    The current API 1456 raw digest equals the historical digest; current owner bytes
    match the unchanged before/after hashes. Exact source objects are separately authenticated,
    while null prior concentration snippets remain unverified. The prior blanket stock-topology
    flag does not erase fresh positive support for the 15 main rates. Current importer
    source-step flattening and bare ml normalization remain bounded current-code observations,
    not reconstructed historical execution.
  target_ids:
  - CultureMech:000922
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - historical-object-joins
  - writer-mediadive
  - writer-formulation
  - writer-merger
  - historical-selected-parent-rows
  - historical-parent-authentication
findings:
- finding_id: f1
  issue_key: culturemech-000922-sl10-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore the SL-10 stock boundary
  description: The 15 main ingredient rates have direct provider support and remain
    unchanged. The nine SL-10 components are flattened at stock strength into main
    ingredients; restore the named stock and printed 1 ml receiving addition. Its
    explicit 1000 ml makeup supports solid-component stock rates. Preserve HCl 25%
    as a native volume/label until its mass basis is resolved.
  target_ids:
  - CultureMech:000922
  field_paths:
  - ingredients[15]
  - ingredients[16]
  - ingredients[17]
  - ingredients[18]
  - ingredients[19]
  - ingredients[20]
  - ingredients[21]
  - ingredients[22]
  - ingredients[23]
  - solutions
  evidence_ids:
  - dsm1456
  - api1456
  - quantities
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-000922-stock-step-scope
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Scope the retained SL-10 preparation step
  description: Both documents preserve the complete main preparation and correct final
    pH range. Their second preparation step is the separately supported SL-10 dissolution
    and makeup method, but it is unqualified at the main level. Preserve its text
    under an explicit SL-10 stock container.
  target_ids:
  - CultureMech:000922
  field_paths:
  - preparation_steps[1]
  - data/normalized_yaml/bacterial/desulfosoma_medium.yaml::preparation_steps[1]
  evidence_ids:
  - dsm1456
  - api1456
  - target
  - owner
  - writer-mediadive
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-000922-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the nickel hexahydrate identity
  description: The exact preferred term and source specify nickel chloride hexahydrate,
    while primary and secondary CHEBI:34887 slots represent anhydrous nickel dichloride.
    Current CHEBI:53542 explicitly contains six waters. Correct supplied-form identity
    independently of the unchanged stock amount.
  target_ids:
  - CultureMech:000922
  field_paths:
  - data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml::ingredients[22].term
  - data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml::ingredients[22].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/desulfosoma_medium.yaml::ingredients[22].term
  - data/normalized_yaml/bacterial/desulfosoma_medium.yaml::ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm1456
  - api1456
  - chebi34887
  - chebi53542
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-000922-resazurin-sodium-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve sodium resazurin supplied form
  description: The source and preferred term name sodium resazurin, but the asserted
    CHEBI:8806 describes neutral resazurin. Resolve the salt identity without replacing
    it with a guessed concept or changing the supported native stock addition.
  target_ids:
  - CultureMech:000922
  field_paths:
  - data/merge_yaml/merged/DESULFOSOMA_MEDIUM.yaml::ingredients[10].term
  - data/normalized_yaml/bacterial/desulfosoma_medium.yaml::ingredients[10].term
  evidence_ids:
  - dsm1456
  - api1456
  - chebi8806
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-000922-claim-and-link-completeness
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach scoped claims and complete supported ingredient links
  description: No local concentration claim is attached. Add exact source-stage evidence
    for supported unchanged main rates and corrected stock placement. Yeast extract
    and Trypticase peptone also lack primary/secondary links despite exact packaged
    preferred-term mappings; assess those current candidates with the printed product
    scope, without inventing a chemical formula for these complex ingredients.
  target_ids:
  - CultureMech:000922
  field_paths:
  - ingredients
  - data/normalized_yaml/bacterial/desulfosoma_medium.yaml::ingredients[8]
  - data/normalized_yaml/bacterial/desulfosoma_medium.yaml::ingredients[9]
  evidence_ids:
  - old-claims
  - quantities
  - groundings
  - mim
  - dsm1456
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: The 15 main ingredient rates have direct provider support and remain
    unchanged. The nine SL-10 components are flattened at stock strength into main
    ingredients; restore the named stock and printed 1 ml receiving addition. Its
    explicit 1000 ml makeup supports solid-component stock rates. Preserve HCl 25%
    as a native volume/label until its mass basis is resolved.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000922
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
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
  description: Both documents preserve the complete main preparation and correct final
    pH range. Their second preparation step is the separately supported SL-10 dissolution
    and makeup method, but it is unqualified at the main level. Preserve its text
    under an explicit SL-10 stock container.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000922
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
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
  description: The exact preferred term and source specify nickel chloride hexahydrate,
    while primary and secondary CHEBI:34887 slots represent anhydrous nickel dichloride.
    Current CHEBI:53542 explicitly contains six waters. Correct supplied-form identity
    independently of the unchanged stock amount.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000922
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
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
  description: The source and preferred term name sodium resazurin, but the asserted
    CHEBI:8806 describes neutral resazurin. Resolve the salt identity without replacing
    it with a guessed concept or changing the supported native stock addition.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000922
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
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
  description: No local concentration claim is attached. Add exact source-stage evidence
    for supported unchanged main rates and corrected stock placement. Yeast extract
    and Trypticase peptone also lack primary/secondary links despite exact packaged
    preferred-term mappings; assess those current candidates with the printed product
    scope, without inventing a chemical formula for these complex ingredients.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000922
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosoma_medium.yaml
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
- The provider records volume 1001 ml while its main g_l values use the printed nominal
  litre amounts. Preserve explicit provider rates and the metadata discrepancy; no
  measured final-volume normalization is inferred.
- HCl 25% has no explicit primary percentage basis or density. No active salt-form
  replacement is inferred from synonym matching alone.
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
