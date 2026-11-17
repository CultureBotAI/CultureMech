# Scientific review: CYS MEDIUM WITH MODIFIED NACL CONCENTRATION

- Review: 20261028T131937Z-culturemech-003809-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:26.083656Z
- Finished UTC: 2026-10-28T13:19:37.500253Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated four-owner CYS merge obscures a genuine 3 versus 20 g/L NaCl variant and carries seven trace-stock masses as final-medium rates. Primary sources support the unchanged main-formulation amounts with explicit final 1 L, but require separate stock stages, consistent Gelrite state and nickel-hydrate grounding. Native checks pass; source and provenance curation remains necessary.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch068 index 01
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003809 | data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml | generated | cys_medium_with_modified_nacl_concentration |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:003809 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:003809 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:003809 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:003809 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and variant boundaries

identity: concern. Targets: CultureMech:003809.

The selected modified target is identifiable, but its base/modified contributors differ scientifically. Catalogue identity supports environmental scope only; no strain growth assertion is transferred.

### Native shape and reference coverage

schema: supported. Targets: CultureMech:003809.

All four actual required checks passed; references performed 0 checks on the target. These results establish native shape only, not source correctness.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:003809.

75 current concentration fields are covered by 20 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","quantity_field_count":75,"decisions":[{"quantity_id":"q1","label":"N-Z-Case","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"N-Z-Case\",\n                        \"compound_id\": 1829,\n                        \"condition\": \"\",\n                        \"attribute\": \"Wako pure chemicals, Japan = Peptone from Caseine\",\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 3-3","quote":"NZ Case (Wako pure chemicals, Japan)=Peptone from Caseine 3.000              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 4-4","quote":"Yeast Extract                                             2.000              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Starch","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"attribute\": \"soluble\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 5-5","quote":"Soluble Starch                                            1.000              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"NaCl, modified and mislabeled base layers","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The modified target and DSM 1108a/KOMODO 1108a contributors have the supported 20 g/L modified rate. The KOMODO 1108 base contributor incorrectly carries 20 g/L despite exact DSM 1108 prescribing 3 g/L. Its legacy resolver event must not override the suffix-specific source. The true DSM 1108 owner is separately credited below.","source_stage":"Exact DSM 1108a versus DSM 1108 main formulations","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 342.231,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 6-6","quote":"NaCl                                                    20.000               g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108.bin","raw_sha256":"5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da","text_sha256":"3a71c3f45c59eec89a008c82ece3376e0350e33e672bd2a6d4032d67ad194834","accessed_at":"2026-10-28T13:11:52.569720Z","locator":"dsm1108.txt lines 6-6","quote":"NaCl                                                     3.000               g","quote_basis":"derivative text"},{"evidence_id":"api1108","reference":"https://mediadive.dsmz.de/rest/medium/1108","raw_path":"REVIEW_WORK/batch068/source01-03/api1108.bin","raw_sha256":"607e4d0b929554d98621158836103af1a47415ea55446b5d2270da2c43d00820","text_sha256":"0238e529f003ffc417e15ceefc1968edcfa5c9897024dfc015c61203f664f267","accessed_at":"2026-10-28T13:11:52.232670Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 51.3347,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","decision":"evidence_only","rationale":"Exact modified source supports 20 g/L; claim linkage is missing."},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","decision":"conflict","rationale":"Exact base source requires 3 g/L."},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","decision":"evidence_only","rationale":"Exact modified source supports 20 g/L; claim linkage is missing."},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","decision":"evidence_only","rationale":"Exact modified source supports 20 g/L; claim linkage is missing."}]},{"quantity_id":"q5","label":"NaCl, maintained DSM 1108 base","local_fields":[{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The maintained base has the supported 3 g/L. Preserve it independently of the modified 20 g/L recipe.","source_stage":"DSM 1108 base final 1 L","sources":[{"evidence_id":"dsm1108","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108.bin","raw_sha256":"5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da","text_sha256":"3a71c3f45c59eec89a008c82ece3376e0350e33e672bd2a6d4032d67ad194834","accessed_at":"2026-10-28T13:11:52.569720Z","locator":"dsm1108.txt lines 6-6","quote":"NaCl                                                     3.000               g","quote_basis":"derivative text"},{"evidence_id":"dsm1108","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108.bin","raw_sha256":"5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da","text_sha256":"3a71c3f45c59eec89a008c82ece3376e0350e33e672bd2a6d4032d67ad194834","accessed_at":"2026-10-28T13:11:52.569720Z","locator":"dsm1108.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"api1108","reference":"https://mediadive.dsmz.de/rest/medium/1108","raw_path":"REVIEW_WORK/batch068/source01-03/api1108.bin","raw_sha256":"607e4d0b929554d98621158836103af1a47415ea55446b5d2270da2c43d00820","text_sha256":"0238e529f003ffc417e15ceefc1968edcfa5c9897024dfc015c61203f664f267","accessed_at":"2026-10-28T13:11:52.232670Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 51.3347,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"MgCl2","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used. The DSM source uses the unsuffixed salt, consistent with the current salt label; its exact supplied hydrate is not independently stated and JCM hydrates are not transferred.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\": 453,\n                        \"amount\": 0.125,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.125,\n                        \"mmol_l\": 1.31289,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 7-7","quote":"MgCl2                                                     0.125              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"CaCl2","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used. The DSM source uses the unsuffixed salt, consistent with the current salt label; its exact supplied hydrate is not independently stated and JCM hydrates are not transferred.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2\",\n                        \"compound_id\": 81,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.225266,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 8-8","quote":"CaCl2                                                     0.025              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 9-9","quote":"FeSO4 x 7 H2O                                             0.010              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Gelrite","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact DSM 1108a primary lists this main-formulation mass and explicitly makes the completed medium to 1 liter; the API independently supplies the same g_l. Retain this supported rate and attach evidence. DSM 1108 is separately assessed; no water-only denominator inference is used. The named Gelrite is retained as a source-specified gelling component, not an optional omission.","source_stage":"DSM main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Gelrite\",\n                        \"compound_id\": 987,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 10-10","quote":"Gelrite                                                   8.000              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 12,\n                        \"unit\": \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\": 49.597,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 15-15","quote":"Na2MoO4 x 2 H2O                                                12.00         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"VOSO4 x H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"VOSO4 x H2O\",\n                        \"compound_id\": 988,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 16-16","quote":"VOSO4 x H2O                                                     1.00         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 25.2646,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 17-17","quote":"MnCl2 x 4 H2O                                                   5.00         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.6,\n                        \"mmol_l\": 2.08651,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 18-18","quote":"ZnSO4 x 7 H2O                                                   0.60         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"CuSO4 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 0.600755,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 19-19","quote":"CuSO4 x 5 H2O                                                   0.15         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\": 61.6148,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 20-20","quote":"CoCl2 x 6 H2O                                                   8.00         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary places this mass under seven separate trace-metal solutions and directs 100 µL of each into the medium. Its printed table gives g, with no stock final-volume denominator. The API flattened the same digits into main-solution g_l; that provider assertion conflicts with the primary stage. Neither the existing main-medium rate nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths are a different source version and are not transferred.","source_stage":"Separate DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54322,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 21-21","quote":"NiCl2 x 6 H2O                                                   0.20         g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Existing preparation and final makeup","local_fields":[{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add 100 µl each of Trace Metal solutions according to the following order:"},{"step_number":2,"action":"AUTOCLAVE","description":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter. Sterilize with and autoclave at 121°C for 15 min."}]},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add 100 µl each of Trace Metal solutions according to the following order:"},{"step_number":2,"action":"AUTOCLAVE","description":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter. Sterilize with and autoclave at 121°C for 15 min."}]}],"decision":"evidence_only","rationale":"The DSM owners preserve the 100 µL additions, pH 7.5, explicit final 1 L and121°C/15 min instructions. The merged target and both KOMODO contributors lack those steps. Preserve these actual instructions with root evidence; do not infer a stock composition denominator.","source_stage":"Primary sequence and final makeup","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the following order:","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Initial water, source-only","local_fields":[],"decision":"not_quantified","rationale":"900 mL is the primary initial solvent amount before final makeup to 1 L. It is missing as preparation context in the selected generated target; no claim that900mL is the final volume.","source_stage":"Initial solvent and later final makeup","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 11-11","quote":"H2O                                                    900.000              ml","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-23","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"pH","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ph_value","stored":7.5}],"decision":"evidence_only","rationale":"All current pH 7.5 values agree with the exact primary instruction at room temperature.","source_stage":"Final pH at stated room temperature","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 23-23","quote":"Adjust to pH 7.5 at room temperature and add water to the final volume of 1 liter.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Physical state with mandatory Gelrite","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"physical_state","stored":"LIQUID"}],"decision":"conflict","rationale":"Every layer says LIQUID while the exact recipes include8 g Gelrite per final liter with no optional qualifier. Current OLS identifies Gelrite as gellan gum/gelling agent. Curate the encoded formulation/state consistently, preserving the source inclusion; no experimental gel outcome or unprinted liquid variant is asserted.","source_stage":"Encoded source formulation","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt lines 10-10","quote":"Gelrite                                                   8.000              g","quote_basis":"derivative text"},{"evidence_id":"chebi85248","reference":"https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_85248","raw_path":"REVIEW_WORK/batch068/source01-03/chebi85248.bin","raw_sha256":"41a456ee5ecd0a2c39439a09a3da6f8e0e87a387824d5f9e9abc491319d85271","text_sha256":"910184bf8aa05a438a48feb453a6ed93771a2b662ae2c94e37c520dd7ea17dd1","accessed_at":"2026-10-28T13:11:57.581803Z","locator":"OLS canonical label","quote":"gellan gum","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml":null,"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml":null,"data/normalized_yaml/bacterial/cys_medium.yaml":null,"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:003809.

Every current primary and secondary chemical slot is compared with captured OLS and the exact packaged MIM snapshot. Nickel CHEBI:34887 is the wrong supplied hydrate; CHEBI:53542 is checked as a candidate. VOSO4 is ungrounded and its unspecified external stock basis remains unresolved. N-Z-Case brand/grade and Gelrite product specificity are not certified by a generic chemical label. Current label agreement and MIM membership do not validate concentrations. The exact MIM preferred CoCl2 x 6 H2O and NiCl2 x 6 H2O rows are REJECTED, while other label rows map the corresponding hydrates; preserve these distinct observed statuses. Current primary CHEBI form validity is assessed independently of that snapshot status. N-Z-Case remains UNMAPPED; the yeast-extract FOODON row is an optional candidate, not an automatic new assertion.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:003809.

Nine complete exact-header reports and four selected parent rows were read; all 72 historical API objects and their four whole-response hashes authenticate against current captures. The old mapping HTML is retained only as derivative history because current exact KOMODO routes/list return 403. Zero-source-check October 5 reports do not establish validity. Current merger rejects divergent formulation fields; current importer still accepts these provider-flattened primary rows, and the resolver strips suffixes.

## Findings

### f1: The merge combines distinct base and salt-modified sources

major / open / confirmed; issue key: culturemech-003809-salinity-variant-boundary.

Preserve DSM 1108 base and 1108a salt-modified identities as distinct variants. The maintained DSM base correctly has 3 g/L NaCl and the modified source 20 g/L; the KOMODO 1108 contributor incorrectly carries 20 g/L despite its base accession; its history records a DSMZ 1108 copy, while the current resolver separately shows suffix stripping. The generated four-owner merge must not imply these sources are the same formulation. Current conservative formulation matching would reject their differing encoded fields.

### f2: Seven trace-stock amounts are stored as final-medium rates

major / open / confirmed; issue key: culturemech-003809-trace-stock-stage.

Represent the seven trace solutions and their 100 µL receiving additions separately. Existing direct ingredients[8:15] and API main-solution rates flatten stock table masses into final-medium concentrations. The DSM table omits each stock preparation volume: retain that unresolved denominator, and do not substitute the separately specified JCM 618 stock formulation.

### f3: Liquid metadata conflicts with the stated Gelrite formulation

major / open / confirmed; issue key: culturemech-003809-gelrite-state.

Reconcile physical_state with the mandatory Gelrite-containing source formulation. Preserve 8 g/L Gelrite and do not silently remove it to create a liquid recipe. The discrepancy is representation-level; no growth or gel-performance claim is inferred.

### f4: Nickel hexahydrate is grounded to the anhydrous salt

major / open / confirmed; issue key: culturemech-003809-nickel-hydrate.

The exact source and local name specify NiCl2·6H2O, while primary and secondary slots use CHEBI:34887 nickel dichloride. Current CHEBI:53542 is the explicit hexahydrate and is a source-consistent curation candidate. Correct identity and label only after reconciling the separate stock-stage error; do not use anhydrous molecular weight to convert the amount. Other captured hydrate terms are retained; unsuffixed DSM magnesium/calcium salts are not automatically replaced by JCM hydrates.

### f5: Source claims and append-only event context are incomplete

minor / open / confirmed; issue key: culturemech-003809-claim-and-event-provenance.

Attach literal primary evidence to maintained ingredients and root evidence for stocks/preparation. Retain all original events, including malformed KOMODO timestamps and naive resolver timestamps, byte-for-byte; append only verified context in a new event. Preserve the current source-duplicate/salinity relationships as bounded assertions and repair the incorrect merged interpretation. The old current-byte-matching API reports are derivative support, not a recovered live KOMODO catalog.

## Recommended Actions And Acceptance Checks

### a1

Preserve DSM 1108 base and 1108a salt-modified identities as distinct variants. The maintained DSM base correctly has 3 g/L NaCl and the modified source 20 g/L; the KOMODO 1108 contributor incorrectly carries 20 g/L despite its base accession; its history records a DSMZ 1108 copy, while the current resolver separately shows suffix stripping. The generated four-owner merge must not imply these sources are the same formulation. Current conservative formulation matching would reject their differing encoded fields.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Represent the seven trace solutions and their 100 µL receiving additions separately. Existing direct ingredients[8:15] and API main-solution rates flatten stock table masses into final-medium concentrations. The DSM table omits each stock preparation volume: retain that unresolved denominator, and do not substitute the separately specified JCM 618 stock formulation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Reconcile physical_state with the mandatory Gelrite-containing source formulation. Preserve 8 g/L Gelrite and do not silently remove it to create a liquid recipe. The discrepancy is representation-level; no growth or gel-performance claim is inferred.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The exact source and local name specify NiCl2·6H2O, while primary and secondary slots use CHEBI:34887 nickel dichloride. Current CHEBI:53542 is the explicit hexahydrate and is a source-consistent curation candidate. Correct identity and label only after reconciling the separate stock-stage error; do not use anhydrous molecular weight to convert the amount. Other captured hydrate terms are retained; unsuffixed DSM magnesium/calcium salts are not automatically replaced by JCM hydrates.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Attach literal primary evidence to maintained ingredients and root evidence for stocks/preparation. Retain all original events, including malformed KOMODO timestamps and naive resolver timestamps, byte-for-byte; append only verified context in a new event. Preserve the current source-duplicate/salinity relationships as bounded assertions and repair the incorrect merged interpretation. The old current-byte-matching API reports are derivative support, not a recovered live KOMODO catalog.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm1108 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf; REVIEW_WORK/batch068/source01-03/dsm1108.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| dsm1108a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf; REVIEW_WORK/batch068/source01-03/dsm1108a.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| api1108 | https://mediadive.dsmz.de/rest/medium/1108; REVIEW_WORK/batch068/source01-03/api1108.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| api1108a | https://mediadive.dsmz.de/rest/medium/1108a; REVIEW_WORK/batch068/source01-03/api1108a.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| komodo1108 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1108; REVIEW_WORK/batch068/source01-03/komodo1108.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| komodo1108a | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1108a; REVIEW_WORK/batch068/source01-03/komodo1108a.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch068/source01-03/komodoList.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| identityDSM45223 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-45223; REVIEW_WORK/batch068/source01-03/identityDSM45223.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; REVIEW_WORK/batch068/source01-03/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; REVIEW_WORK/batch068/source01-03/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi85248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_85248; REVIEW_WORK/batch068/source01-03/chebi85248.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| target | data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-3 | data/normalized_yaml/bacterial/cys_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-4 | data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cys_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cys_medium_with_modified_nacl_concentration.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-25 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1108_CYS_MEDIUM.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch068/record01/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch068/record01/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch068/record01/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser keeps only primary compounds and separately preserves referenced stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v enums without independently establishing the basis; the action classifier tests temperature before cool. Current behavior is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver._build_dsmz_index, extract_dsmz_id, merge_composition | context_only | DSMZCompositionResolver.extract_dsmz_id and _build_dsmz_index strip variant suffixes; merge_composition copies ingredients/solutions and physical state but does not copy preparation_steps. This current mechanism can erase a suffix boundary; the observed old event is retained as historical evidence, not reproduced. |
| history-auth | REVIEW_WORK/batch068/record01/historical-source-authentication.json; Complete artifact | supports | All 72 selected historical source objects match current original API bytes and exact locators; the four original source hashes equal the current captures. This authenticates content, not old retrieval or current KOMODO catalog availability. |
| internal-links | REVIEW_WORK/batch068/record01/internal-reference-identity.json; Complete artifact | supports | Exact linked paths and IDs exist; relationship science is independently assessed. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28017; REVIEW_WORK/batch068/source01-03/chebi28017.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; REVIEW_WORK/batch068/source01-03/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi6636 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_6636; REVIEW_WORK/batch068/source01-03/chebi6636.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_3312; REVIEW_WORK/batch068/source01-03/chebi3312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; REVIEW_WORK/batch068/source01-03/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; REVIEW_WORK/batch068/source01-03/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; REVIEW_WORK/batch068/source01-03/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; REVIEW_WORK/batch068/source01-03/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; REVIEW_WORK/batch068/source01-03/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; REVIEW_WORK/batch068/source01-03/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| quantities | REVIEW_WORK/batch068/record01/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch068/record01/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch068/record01/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch068/record01/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch068/record01/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch068/record01/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch068/record01/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch068/record01/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch068/record01/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch068/record01/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch068/record01/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Partial completion: the exact KOMODO 1108/1108a and MediaList routes returned 403; original catalog raw is not recovered by current API byte equality.
- The primary DSM trace tables omit stock solvent/final volumes. Only receiving additions are explicit; no final trace rate is calculated.
- DSM 1108/1108a and JCM 618/619 must remain source-version specific; hydrated JCM salts and stock-strength details are not inherited into this DSM review.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T131937Z-culturemech-003809-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CYS MEDIUM WITH MODIFIED NACL CONCENTRATION'
started_at: '2026-10-28T13:11:26.083656Z'
finished_at: '2026-10-28T13:19:37.500253Z'
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
summary: The generated four-owner CYS merge obscures a genuine 3 versus 20 g/L NaCl
  variant and carries seven trace-stock masses as final-medium rates. Primary sources
  support the unchanged main-formulation amounts with explicit final 1 L, but require
  separate stock stages, consistent Gelrite state and nickel-hydrate grounding. Native
  checks pass; source and provenance curation remains necessary.
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
  - path: data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    sha256: 5999c2570770933b1d858487b2f9f008596d1de4229068ed4bc745a8081933db
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    sha256: 3e1a03dc3f03812f0b362b9b375384e05324f5ce0dfdf6d2c75652685bc0e084
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    sha256: 44e7ddcea566894563ba464a6a72a0c5797c355a75997a4a7f60a09ab8b8b426
    role: context
  - path: data/normalized_yaml/bacterial/cys_medium.yaml
    sha256: 94ddfab33d080478882d36a9d3d2ecfb168810a692c90a1392d180be720e709f
    role: context
  - path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    sha256: f3a488a1c3a76b39b68b2e0fb3ac18d79531607a5f5bdf245e85b9cbd85b666a
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cys_medium.yaml.md
    sha256: 4c8ab7152308d5a64b895de07d61c29f418f445087bcaf80d7c2049519c1fbb4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cys_medium_with_modified_nacl_concentration.yaml.md
    sha256: ab0b33dded3febe735cb9ddbc79d572a441d06969234a4dc33652d74584716e9
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
    sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1108_CYS_MEDIUM.yaml.md
    sha256: fc9148bf96fd0bebb4e6baafa6ffefc067392fb5096d0efd050962791b3b6b03
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml.md
    sha256: d9638c0fc08c6d3d8ac04689499415c123740c51fc57a355ec193b77f99d6847
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.md
    sha256: 12ef9fef922d0b9d4eef91c25621f50b2f21170a87c965fa192a397dc1ddebbc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.md
    sha256: 43e9584bc2c44a5d01d78242f774c8eb9abc936e7081438443468ebab78bcf33
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.md
    sha256: 8d2a77a2643e02a346601d7102d9f29acb3b18b12fabb066f2cc08f4a222ec8d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium.md
    sha256: 54107026c96782d9d1fc10625b2d61dda188649635e6a93be4d7b72df39f91e2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.md
    sha256: 1b3f6245ea53604465a16aad58a86480e4dd3abdb23466f5f608631a98acd7f1
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
  selection: Authoritative batch068 index 01
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003809
targets:
- target_id: CultureMech:003809
  path: data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
  label: cys_medium_with_modified_nacl_concentration
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:003809
  command: just validate-schema data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
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
  - CultureMech:003809
  command: just validate-strict data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    --out REVIEW_WORK/batch068/record01/strict.tsv --workers 1 --quiet
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
  - CultureMech:003809
  command: just validate-terms data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
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
  - CultureMech:003809
  command: just validate-references data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm1108
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf
  accessed_at: '2026-10-28T13:11:52.569720Z'
  locator: REVIEW_WORK/batch068/source01-03/dsm1108.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da
- evidence_id: dsm1108a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf
  accessed_at: '2026-10-28T13:11:52.563984Z'
  locator: REVIEW_WORK/batch068/source01-03/dsm1108a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd
- evidence_id: api1108
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1108
  accessed_at: '2026-10-28T13:11:52.232670Z'
  locator: REVIEW_WORK/batch068/source01-03/api1108.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 607e4d0b929554d98621158836103af1a47415ea55446b5d2270da2c43d00820
- evidence_id: api1108a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1108a
  accessed_at: '2026-10-28T13:11:52.366058Z'
  locator: REVIEW_WORK/batch068/source01-03/api1108a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993
- evidence_id: komodo1108
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1108
  accessed_at: '2026-10-28T13:11:51.853218Z'
  locator: REVIEW_WORK/batch068/source01-03/komodo1108.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 55a55cc2485c6bbc47bffc5d51c05f2be106b3d8f4096c12810fed4a8a232260
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1108;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo1108a
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1108a
  accessed_at: '2026-10-28T13:11:52.274096Z'
  locator: REVIEW_WORK/batch068/source01-03/komodo1108a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: c12a59b80f3b7f2671717c75daf2cde04e7cb44cc4d9bc49bbd5817e3ccce08f
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1108a;
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
- evidence_id: identityDSM45223
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-45223
  accessed_at: '2026-10-28T13:11:55.258995Z'
  locator: REVIEW_WORK/batch068/source01-03/identityDSM45223.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: a6d19b7f5c9e25c6ede28b1e6e8f7dedffa1370e87adad25c2a4a44c39ebcd0d
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  accessed_at: '2026-10-28T13:11:56.960579Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  accessed_at: '2026-10-28T13:11:56.609061Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi85248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_85248
  accessed_at: '2026-10-28T13:11:57.581803Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi85248.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 41a456ee5ecd0a2c39439a09a3da6f8e0e87a387824d5f9e9abc491319d85271
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.005559Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 5999c2570770933b1d858487b2f9f008596d1de4229068ed4bc745a8081933db
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.005714Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 3e1a03dc3f03812f0b362b9b375384e05324f5ce0dfdf6d2c75652685bc0e084
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.005736Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.006025Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:17:37.006047Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:17:37.006068Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.006089Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 44e7ddcea566894563ba464a6a72a0c5797c355a75997a4a7f60a09ab8b8b426
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/cys_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.006108Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 94ddfab33d080478882d36a9d3d2ecfb168810a692c90a1392d180be720e709f
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:17:37.006125Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: f3a488a1c3a76b39b68b2e0fb3ac18d79531607a5f5bdf245e85b9cbd85b666a
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:17:37.006145Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cys_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.012088Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 4c8ab7152308d5a64b895de07d61c29f418f445087bcaf80d7c2049519c1fbb4
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cys_medium_with_modified_nacl_concentration.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.012142Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ab0b33dded3febe735cb9ddbc79d572a441d06969234a4dc33652d74584716e9
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:17:37.012170Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1108_CYS_MEDIUM.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016253Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: fc9148bf96fd0bebb4e6baafa6ffefc067392fb5096d0efd050962791b3b6b03
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016315Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d9638c0fc08c6d3d8ac04689499415c123740c51fc57a355ec193b77f99d6847
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016345Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 12ef9fef922d0b9d4eef91c25621f50b2f21170a87c965fa192a397dc1ddebbc
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016373Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 43e9584bc2c44a5d01d78242f774c8eb9abc936e7081438443468ebab78bcf33
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016395Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8d2a77a2643e02a346601d7102d9f29acb3b18b12fabb066f2cc08f4a222ec8d
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016416Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 54107026c96782d9d1fc10625b2d61dda188649635e6a93be4d7b72df39f91e2
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.md
  locator: Complete report
  accessed_at: '2026-10-28T13:17:37.016439Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 1b3f6245ea53604465a16aad58a86480e4dd3abdb23466f5f608631a98acd7f1
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/historical-reading.json
  accessed_at: '2026-10-28T13:17:37.016468Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 778ba11481e57cbee4a82ad9356f38c0c13b9fa2c3eff8a8e9387e3ada3e5f2e
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:17:37.016763Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 217316c02a946bc4366463aa17304f79b80ea31bdbbf938eede6478c20547aa3
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/complete-document-reader.json
  accessed_at: '2026-10-28T13:17:37.017000Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 66d776a4fa15fdaea96edf21ab3ae6ca3268770c8939e638051a4b18ce96b696
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:17:37.017168Z'
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
  accessed_at: '2026-10-28T13:17:37.017205Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver._build_dsmz_index, extract_dsmz_id, merge_composition
  accessed_at: '2026-10-28T13:17:37.017230Z'
  support: context_only
  summary: DSMZCompositionResolver.extract_dsmz_id and _build_dsmz_index strip variant
    suffixes; merge_composition copies ingredients/solutions and physical state but
    does not copy preparation_steps. This current mechanism can erase a suffix boundary;
    the observed old event is retained as historical evidence, not reproduced.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/historical-source-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T13:17:37.017255Z'
  support: supports
  summary: All 72 selected historical source objects match current original API bytes
    and exact locators; the four original source hashes equal the current captures.
    This authenticates content, not old retrieval or current KOMODO catalog availability.
  snapshot_sha256: 9548ebaefb8a46e588d04aa6e2e4dfad7792665e921cd535f64e5afff3ddaeef
- evidence_id: internal-links
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/internal-reference-identity.json
  locator: Complete artifact
  accessed_at: '2026-10-28T13:17:37.017494Z'
  support: supports
  summary: Exact linked paths and IDs exist; relationship science is independently
    assessed.
  snapshot_sha256: 3afcb3d68128ef9d559c1b8ee186e50733c7d7fb816b622cae88233ec091fdcd
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28017
  accessed_at: '2026-10-28T13:11:56.351368Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi28017.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 97d3317b987b817f798f2968ae77d2d550be0f98d072c054f7effa98c58f9d1a
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  accessed_at: '2026-10-28T13:11:55.982175Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi6636
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_6636
  accessed_at: '2026-10-28T13:11:57.184926Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi6636.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 85b420116c39ebdcb2a0605d308118dfb2cd534bead2ccc09bdaeb4649fd0195
- evidence_id: chebi3312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_3312
  accessed_at: '2026-10-28T13:11:56.575320Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi3312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 76bdc025d30f15d533c0352d0584f76ec02f6904ab57a13277a2d87ae1189a47
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  accessed_at: '2026-10-28T13:11:57.905294Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  accessed_at: '2026-10-28T13:11:57.255273Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  accessed_at: '2026-10-28T13:11:58.198058Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  accessed_at: '2026-10-28T13:11:56.238355Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  accessed_at: '2026-10-28T13:11:55.965879Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi31440.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  accessed_at: '2026-10-28T13:11:56.849008Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130398Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 8673c0fd0987d3850d9cd80027343bbb9f77c8715fab457156be556775c15b87
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130458Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 5118bcfe522b2576b337d1dad10cadb26a855001bf7f7955d617eaf247f8dc7d
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130545Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 481da5ad4a8b9f8bffd360c34a7e73ade2633126f6f7f492917e6f2f98e5f32a
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130609Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 598f7f96296bd3ddf0805a7b879d8e87d0be328f1ff0e945607a6fad30fce375
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130673Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 6f6d6c7014109678807dafe7079eba4e91c54d7ad381dd788ee8f1f1cec6d2fc
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130695Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 2ea37b8d2094c5ef466ae1f5217c3de43a4a8c16de47acab139a8577ad4dacb5
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch068/record01/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:17:37.130719Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record01/validate-schema.json
  accessed_at: '2026-10-28T13:11:27.215649Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 7954520f57718a2dfa2a9811d23f8e5c92fe75dd5e14410224b1e06699759a4a
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record01/validate-strict.json
  accessed_at: '2026-10-28T13:11:28.168833Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 972fc1c6d9b4f1c168aaa6204e99cec39f74c3d28e8f49727276bb7066a25c09
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record01/validate-terms.json
  accessed_at: '2026-10-28T13:11:29.656925Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0bbe45a32fb29064256a9200775921a0d3de6c1150d07a5b5750a4dc81ea242d
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch068/record01/validate-references.json
  accessed_at: '2026-10-28T13:11:30.459640Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: d7f251c7a93ed3b70c50a4aa0bb1ee168bb3bec76faf9ad043fb04dbdfd4448e
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and variant boundaries
  outcome: concern
  summary: The selected modified target is identifiable, but its base/modified contributors
    differ scientifically. Catalogue identity supports environmental scope only; no
    strain growth assertion is transferred.
  target_ids:
  - CultureMech:003809
  evidence_ids:
  - dsm1108
  - dsm1108a
  - identityDSM45223
  - internal-links
- assessment_id: schema
  area: schema
  topic: Native shape and reference coverage
  outcome: supported
  summary: All four actual required checks passed; references performed 0 checks on
    the target. These results establish native shape only, not source correctness.
  target_ids:
  - CultureMech:003809
  evidence_ids:
  - target
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 75 current concentration fields are covered by 20 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:003809
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","quantity_field_count":75,"decisions":[{"quantity_id":"q1","label":"N-Z-Case","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used.","source_stage":"DSM main formulation,
    explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"N-Z-Case\",\n                        \"compound_id\":
    1829,\n                        \"condition\": \"\",\n                        \"attribute\":
    \"Wako pure chemicals, Japan = Peptone from Caseine\",\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 3-3","quote":"NZ Case (Wako pure chemicals, Japan)=Peptone from Caseine
    3.000              g","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used.","source_stage":"DSM main formulation,
    explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 4-4","quote":"Yeast Extract                                             2.000              g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q3","label":"Starch","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used.","source_stage":"DSM main formulation,
    explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Starch\",\n                        \"compound_id\":
    199,\n                        \"attribute\": \"soluble\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 5-5","quote":"Soluble Starch                                            1.000              g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q4","label":"NaCl, modified and mislabeled base layers","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    modified target and DSM 1108a/KOMODO 1108a contributors have the supported 20
    g/L modified rate. The KOMODO 1108 base contributor incorrectly carries 20 g/L
    despite exact DSM 1108 prescribing 3 g/L. Its legacy resolver event must not override
    the suffix-specific source. The true DSM 1108 owner is separately credited below.","source_stage":"Exact
    DSM 1108a versus DSM 1108 main formulations","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    342.231,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 6-6","quote":"NaCl                                                    20.000               g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108.bin","raw_sha256":"5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da","text_sha256":"3a71c3f45c59eec89a008c82ece3376e0350e33e672bd2a6d4032d67ad194834","accessed_at":"2026-10-28T13:11:52.569720Z","locator":"dsm1108.txt
    lines 6-6","quote":"NaCl                                                     3.000               g","quote_basis":"derivative
    text"},{"evidence_id":"api1108","reference":"https://mediadive.dsmz.de/rest/medium/1108","raw_path":"REVIEW_WORK/batch068/source01-03/api1108.bin","raw_sha256":"607e4d0b929554d98621158836103af1a47415ea55446b5d2270da2c43d00820","text_sha256":"0238e529f003ffc417e15ceefc1968edcfa5c9897024dfc015c61203f664f267","accessed_at":"2026-10-28T13:11:52.232670Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    51.3347,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","decision":"evidence_only","rationale":"Exact
    modified source supports 20 g/L; claim linkage is missing."},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","decision":"conflict","rationale":"Exact
    base source requires 3 g/L."},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","decision":"evidence_only","rationale":"Exact
    modified source supports 20 g/L; claim linkage is missing."},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","decision":"evidence_only","rationale":"Exact
    modified source supports 20 g/L; claim linkage is missing."}]},{"quantity_id":"q5","label":"NaCl,
    maintained DSM 1108 base","local_fields":[{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    maintained base has the supported 3 g/L. Preserve it independently of the modified
    20 g/L recipe.","source_stage":"DSM 1108 base final 1 L","sources":[{"evidence_id":"dsm1108","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108.bin","raw_sha256":"5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da","text_sha256":"3a71c3f45c59eec89a008c82ece3376e0350e33e672bd2a6d4032d67ad194834","accessed_at":"2026-10-28T13:11:52.569720Z","locator":"dsm1108.txt
    lines 6-6","quote":"NaCl                                                     3.000               g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108.bin","raw_sha256":"5e6638f6b394f5e680c1cb2e9f516a3552c6b0e0603807c06b0dc654634a16da","text_sha256":"3a71c3f45c59eec89a008c82ece3376e0350e33e672bd2a6d4032d67ad194834","accessed_at":"2026-10-28T13:11:52.569720Z","locator":"dsm1108.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"api1108","reference":"https://mediadive.dsmz.de/rest/medium/1108","raw_path":"REVIEW_WORK/batch068/source01-03/api1108.bin","raw_sha256":"607e4d0b929554d98621158836103af1a47415ea55446b5d2270da2c43d00820","text_sha256":"0238e529f003ffc417e15ceefc1968edcfa5c9897024dfc015c61203f664f267","accessed_at":"2026-10-28T13:11:52.232670Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    51.3347,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"MgCl2","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used. The DSM source uses the unsuffixed
    salt, consistent with the current salt label; its exact supplied hydrate is not
    independently stated and JCM hydrates are not transferred.","source_stage":"DSM
    main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\":
    453,\n                        \"amount\": 0.125,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.125,\n                        \"mmol_l\":
    1.31289,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 7-7","quote":"MgCl2                                                     0.125              g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q7","label":"CaCl2","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used. The DSM source uses the unsuffixed
    salt, consistent with the current salt label; its exact supplied hydrate is not
    independently stated and JCM hydrates are not transferred.","source_stage":"DSM
    main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2\",\n                        \"compound_id\":
    81,\n                        \"amount\": 0.025,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\":
    0.225266,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 8-8","quote":"CaCl2                                                     0.025              g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q8","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used.","source_stage":"DSM main formulation,
    explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 9-9","quote":"FeSO4 x 7 H2O                                             0.010              g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q9","label":"Gelrite","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[7].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact DSM 1108a primary lists this main-formulation mass and explicitly makes
    the completed medium to 1 liter; the API independently supplies the same g_l.
    Retain this supported rate and attach evidence. DSM 1108 is separately assessed;
    no water-only denominator inference is used. The named Gelrite is retained as
    a source-specified gelling component, not an optional omission.","source_stage":"DSM
    main formulation, explicit final 1 L","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Gelrite\",\n                        \"compound_id\":
    987,\n                        \"amount\": 8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 8,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 10-10","quote":"Gelrite                                                   8.000              g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q10","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[8].concentration","stored":{"value":"12","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 12,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\":
    49.597,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 15-15","quote":"Na2MoO4 x 2 H2O                                                12.00         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"VOSO4
    x H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"VOSO4 x H2O\",\n                        \"compound_id\":
    988,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 16-16","quote":"VOSO4 x H2O                                                     1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[10].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    25.2646,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 17-17","quote":"MnCl2 x 4 H2O                                                   5.00         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"ZnSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.6","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.6,\n                        \"mmol_l\":
    2.08651,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 18-18","quote":"ZnSO4 x 7 H2O                                                   0.60         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"CuSO4
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.15","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\":
    0.600755,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 19-19","quote":"CuSO4 x 5 H2O                                                   0.15         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[13].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\":
    61.6148,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 20-20","quote":"CoCl2 x 6 H2O                                                   8.00         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary places this mass under seven separate trace-metal solutions and directs
    100 µL of each into the medium. Its printed table gives g, with no stock final-volume
    denominator. The API flattened the same digits into main-solution g_l; that provider
    assertion conflicts with the primary stage. Neither the existing main-medium rate
    nor an invented stock g/L/final diluted rate is endorsed. JCM 618 stock strengths
    are a different source version and are not transferred.","source_stage":"Separate
    DSM trace stock, unresolved stock preparation volume","sources":[{"evidence_id":"api1108a","reference":"https://mediadive.dsmz.de/rest/medium/1108a","raw_path":"REVIEW_WORK/batch068/source01-03/api1108a.bin","raw_sha256":"c8bf03950c5154b98b92678fd5be7f1fa26f1455ea7dc951d0f8dda6b3d91993","text_sha256":"fffeed0ecfecb02e4a224fed1ecac8331b21b16b2ae27495ef54111b91eef624","accessed_at":"2026-10-28T13:11:52.366058Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.54322,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 21-21","quote":"NiCl2 x 6 H2O                                                   0.20         g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Existing
    preparation and final makeup","local_fields":[{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add
    100 µl each of Trace Metal solutions according to the following order:"},{"step_number":2,"action":"AUTOCLAVE","description":"Adjust
    to pH 7.5 at room temperature and add water to the final volume of 1 liter. Sterilize
    with and autoclave at 121°C for 15 min."}]},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add
    100 µl each of Trace Metal solutions according to the following order:"},{"step_number":2,"action":"AUTOCLAVE","description":"Adjust
    to pH 7.5 at room temperature and add water to the final volume of 1 liter. Sterilize
    with and autoclave at 121°C for 15 min."}]}],"decision":"evidence_only","rationale":"The
    DSM owners preserve the 100 µL additions, pH 7.5, explicit final 1 L and121°C/15
    min instructions. The merged target and both KOMODO contributors lack those steps.
    Preserve these actual instructions with root evidence; do not infer a stock composition
    denominator.","source_stage":"Primary sequence and final makeup","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 13-13","quote":"Add 100 µl each of Trace Metal solutions according to the
    following order:","quote_basis":"derivative text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-24","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.\nSterilize with and autoclave at 121°C for 15 min.","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"Initial water, source-only","local_fields":[],"decision":"not_quantified","rationale":"900
    mL is the primary initial solvent amount before final makeup to 1 L. It is missing
    as preparation context in the selected generated target; no claim that900mL is
    the final volume.","source_stage":"Initial solvent and later final makeup","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 11-11","quote":"H2O                                                    900.000              ml","quote_basis":"derivative
    text"},{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-23","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"pH","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"ph_value","stored":7.5}],"decision":"evidence_only","rationale":"All
    current pH 7.5 values agree with the exact primary instruction at room temperature.","source_stage":"Final
    pH at stated room temperature","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 23-23","quote":"Adjust to pH 7.5 at room temperature and add water to the
    final volume of 1 liter.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Physical
    state with mandatory Gelrite","local_fields":[{"path":"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/cys_medium.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml","field_path":"physical_state","stored":"LIQUID"}],"decision":"conflict","rationale":"Every
    layer says LIQUID while the exact recipes include8 g Gelrite per final liter with
    no optional qualifier. Current OLS identifies Gelrite as gellan gum/gelling agent.
    Curate the encoded formulation/state consistently, preserving the source inclusion;
    no experimental gel outcome or unprinted liquid variant is asserted.","source_stage":"Encoded
    source formulation","sources":[{"evidence_id":"dsm1108a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1108a.pdf","raw_path":"REVIEW_WORK/batch068/source01-03/dsm1108a.bin","raw_sha256":"55331a0821189c67ce4554941616fa33890a14cb1de8a4b0f3fa9eedf5b0d0dd","text_sha256":"f82872a62d71a884118b76647c84a9eac92ce89620c13d3ba4578aa6198fca5c","accessed_at":"2026-10-28T13:11:52.563984Z","locator":"dsm1108a.txt
    lines 10-10","quote":"Gelrite                                                   8.000              g","quote_basis":"derivative
    text"},{"evidence_id":"chebi85248","reference":"https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_85248","raw_path":"REVIEW_WORK/batch068/source01-03/chebi85248.bin","raw_sha256":"41a456ee5ecd0a2c39439a09a3da6f8e0e87a387824d5f9e9abc491319d85271","text_sha256":"910184bf8aa05a438a48feb453a6ed93771a2b662ae2c94e37c520dd7ea17dd1","accessed_at":"2026-10-28T13:11:57.581803Z","locator":"OLS
    canonical label","quote":"gellan gum","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml":null,"data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml":null,"data/normalized_yaml/bacterial/cys_medium.yaml":null,"data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every current primary and secondary chemical slot is compared with captured
    OLS and the exact packaged MIM snapshot. Nickel CHEBI:34887 is the wrong supplied
    hydrate; CHEBI:53542 is checked as a candidate. VOSO4 is ungrounded and its unspecified
    external stock basis remains unresolved. N-Z-Case brand/grade and Gelrite product
    specificity are not certified by a generic chemical label. Current label agreement
    and MIM membership do not validate concentrations. The exact MIM preferred CoCl2
    x 6 H2O and NiCl2 x 6 H2O rows are REJECTED, while other label rows map the corresponding
    hydrates; preserve these distinct observed statuses. Current primary CHEBI form
    validity is assessed independently of that snapshot status. N-Z-Case remains UNMAPPED;
    the yeast-extract FOODON row is an optional candidate, not an automatic new assertion.
  target_ids:
  - CultureMech:003809
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Nine complete exact-header reports and four selected parent rows were read;
    all 72 historical API objects and their four whole-response hashes authenticate
    against current captures. The old mapping HTML is retained only as derivative
    history because current exact KOMODO routes/list return 403. Zero-source-check
    October 5 reports do not establish validity. Current merger rejects divergent
    formulation fields; current importer still accepts these provider-flattened primary
    rows, and the resolver strips suffixes.
  target_ids:
  - CultureMech:003809
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-003809-salinity-variant-boundary
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The merge combines distinct base and salt-modified sources
  description: Preserve DSM 1108 base and 1108a salt-modified identities as distinct
    variants. The maintained DSM base correctly has 3 g/L NaCl and the modified source
    20 g/L; the KOMODO 1108 contributor incorrectly carries 20 g/L despite its base
    accession; its history records a DSMZ 1108 copy, while the current resolver separately
    shows suffix stripping. The generated four-owner merge must not imply these sources
    are the same formulation. Current conservative formulation matching would reject
    their differing encoded fields.
  target_ids:
  - CultureMech:003809
  field_paths:
  - merged_from
  - synonyms
  - data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml::ingredients[3].concentration
  evidence_ids:
  - dsm1108
  - dsm1108a
  - api1108
  - api1108a
  - writer-resolver
  - writer-formulation
  rule_id: review-yaml-record/salinity-variant-boundary
  native_severity: P2
  normalization_reason: 'Custom scientific rule: a material source identity, stage,
    supplied-form or formulation-state contradiction is normalized as major (native
    priority P2), without pretending that a numbered native existence/category rule
    tests it.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-003809-trace-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Seven trace-stock amounts are stored as final-medium rates
  description: 'Represent the seven trace solutions and their 100 µL receiving additions
    separately. Existing direct ingredients[8:15] and API main-solution rates flatten
    stock table masses into final-medium concentrations. The DSM table omits each
    stock preparation volume: retain that unresolved denominator, and do not substitute
    the separately specified JCM 618 stock formulation.'
  target_ids:
  - CultureMech:003809
  field_paths:
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - solutions
  - preparation_steps
  - evidence
  evidence_ids:
  - dsm1108a
  - api1108a
  - writer-mediadive
  rule_id: review-yaml-record/trace-stock-stage
  native_severity: P2
  normalization_reason: 'Custom scientific rule: a material source identity, stage,
    supplied-form or formulation-state contradiction is normalized as major (native
    priority P2), without pretending that a numbered native existence/category rule
    tests it.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-003809-gelrite-state
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Liquid metadata conflicts with the stated Gelrite formulation
  description: Reconcile physical_state with the mandatory Gelrite-containing source
    formulation. Preserve 8 g/L Gelrite and do not silently remove it to create a
    liquid recipe. The discrepancy is representation-level; no growth or gel-performance
    claim is inferred.
  target_ids:
  - CultureMech:003809
  field_paths:
  - physical_state
  - ingredients[7]
  evidence_ids:
  - dsm1108a
  - api1108a
  rule_id: review-yaml-record/gelrite-state
  native_severity: P2
  normalization_reason: 'Custom scientific rule: a material source identity, stage,
    supplied-form or formulation-state contradiction is normalized as major (native
    priority P2), without pretending that a numbered native existence/category rule
    tests it.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-003809-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to the anhydrous salt
  description: The exact source and local name specify NiCl2·6H2O, while primary and
    secondary slots use CHEBI:34887 nickel dichloride. Current CHEBI:53542 is the
    explicit hexahydrate and is a source-consistent curation candidate. Correct identity
    and label only after reconciling the separate stock-stage error; do not use anhydrous
    molecular weight to convert the amount. Other captured hydrate terms are retained;
    unsuffixed DSM magnesium/calcium salts are not automatically replaced by JCM hydrates.
  target_ids:
  - CultureMech:003809
  field_paths:
  - ingredients[14].term
  - ingredients[14].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm1108a
  - chebi34887
  - chebi53542
  rule_id: review-yaml-record/nickel-hydrate
  native_severity: P2
  normalization_reason: 'Custom scientific rule: a material source identity, stage,
    supplied-form or formulation-state contradiction is normalized as major (native
    priority P2), without pretending that a numbered native existence/category rule
    tests it.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-003809-claim-and-event-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source claims and append-only event context are incomplete
  description: Attach literal primary evidence to maintained ingredients and root
    evidence for stocks/preparation. Retain all original events, including malformed
    KOMODO timestamps and naive resolver timestamps, byte-for-byte; append only verified
    context in a new event. Preserve the current source-duplicate/salinity relationships
    as bounded assertions and repair the incorrect merged interpretation. The old
    current-byte-matching API reports are derivative support, not a recovered live
    KOMODO catalog.
  target_ids:
  - CultureMech:003809
  field_paths:
  - evidence
  - references
  - preparation_steps
  - curation_history
  evidence_ids:
  - history-auth
  - writer-resolver
  - komodoList
  rule_id: review-yaml-record/claim-and-event-provenance
  native_severity: P3
  normalization_reason: Custom event/claim-provenance rule normalized minor (native
    priority P3); exact amounts and source-stage issues are separately major.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Preserve DSM 1108 base and 1108a salt-modified identities as distinct
    variants. The maintained DSM base correctly has 3 g/L NaCl and the modified source
    20 g/L; the KOMODO 1108 contributor incorrectly carries 20 g/L despite its base
    accession; its history records a DSMZ 1108 copy, while the current resolver separately
    shows suffix stripping. The generated four-owner merge must not imply these sources
    are the same formulation. Current conservative formulation matching would reject
    their differing encoded fields.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003809
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
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
  description: 'Represent the seven trace solutions and their 100 µL receiving additions
    separately. Existing direct ingredients[8:15] and API main-solution rates flatten
    stock table masses into final-medium concentrations. The DSM table omits each
    stock preparation volume: retain that unresolved denominator, and do not substitute
    the separately specified JCM 618 stock formulation.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003809
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
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
  description: Reconcile physical_state with the mandatory Gelrite-containing source
    formulation. Preserve 8 g/L Gelrite and do not silently remove it to create a
    liquid recipe. The discrepancy is representation-level; no growth or gel-performance
    claim is inferred.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003809
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
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
  description: The exact source and local name specify NiCl2·6H2O, while primary and
    secondary slots use CHEBI:34887 nickel dichloride. Current CHEBI:53542 is the
    explicit hexahydrate and is a source-consistent curation candidate. Correct identity
    and label only after reconciling the separate stock-stage error; do not use anhydrous
    molecular weight to convert the amount. Other captured hydrate terms are retained;
    unsuffixed DSM magnesium/calcium salts are not automatically replaced by JCM hydrates.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003809
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: Attach literal primary evidence to maintained ingredients and root
    evidence for stocks/preparation. Retain all original events, including malformed
    KOMODO timestamps and naive resolver timestamps, byte-for-byte; append only verified
    context in a new event. Preserve the current source-duplicate/salinity relationships
    as bounded assertions and repair the incorrect merged interpretation. The old
    current-byte-matching API reports are derivative support, not a recovered live
    KOMODO catalog.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003809
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml
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
- 'Partial completion: the exact KOMODO 1108/1108a and MediaList routes returned 403;
  original catalog raw is not recovered by current API byte equality.'
- The primary DSM trace tables omit stock solvent/final volumes. Only receiving additions
  are explicit; no final trace rate is calculated.
- DSM 1108/1108a and JCM 618/619 must remain source-version specific; hydrated JCM
  salts and stock-strength details are not inherited into this DSM review.
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
