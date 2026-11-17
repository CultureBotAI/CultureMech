# Scientific review of caldithrix_medium

- Review: 20261028T063254Z-caldithrix-medium-batch058
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:08:29.217129Z
- Finished UTC: 2026-10-28T06:32:54.285807Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Caldithrix identity is supported, but the TOGO-derived formulation loses three stock boundaries, corrupts liquid and milligram units, sums different stages, and omits preparation. Existing standalone repairs and correct chemical forms are credited; source prose and final-volume limits remain explicit.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch058 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009161 | data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml | generated | caldithrix_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009161 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:009161 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:009161 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:009161 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source identity

identity: supported. Targets: CultureMech:009161.

The TOGO M2594 identity points to DSM 946a, confirmed by current payload and primary PDF. Standalone solutions 241/5980 are bounded stock dependencies, not owners or alternate whole media.

### Historical and attached claims

evidence: concern. Targets: CultureMech:009161.

Selected target/owner have no attached scientific claims. Standalone stock repairs retain substantive quantity evidence and source hashes, and current stock bytes and rows are checked. Earlier September review identifies topology errors but its per-final-litre recommendations exceed the current final-volume evidence. Current sources govern; no historical source access or execution is recreated. Current solution241 raw SHA matches the historical 50cc42c2 digest and all 17 attached excerpts literally; current solution5980 raw matches 2fe24a83 and all 11 solution-specific excerpts. Its additional medium161 recipe-array claim is retained as separate derivative context without authenticating that whole raw payload or transferring its parent medium.

### Present writers and repair credit

provenance: supported. Targets: CultureMech:009161.

Current TOGO code preserves sections and distinguishes units; current cleanup no longer sums conflicting duplicate quantities. The magnesium primary-only repair explains its bounded scope and does not fix secondary mapping. Current conservative merging preserves scientific fields; the persisted flattening is not proof that these current writers still flatten.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:009161.

All 88 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009161", "selected_concentration_field_count": 88, "selected_concentration_fields_covered": 88, "decisions": [{"decision_id": "q1", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.33", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.33", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final rate", "interpretation": "The current primary gives 0.33 g per listed batch; the API explicitly declares g_l=0.326409 on volume 1011 ml. The local number copies the gram amount into G_PER_L and is not authenticated as a final rate. Preserve the batch mass and supplied form; do not infer measured final volume from 500 ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 2.39857,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[2]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.33", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.33", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final rate", "interpretation": "The current primary gives 0.33 g per listed batch; the API explicitly declares g_l=0.326409 on volume 1011 ml. The local number copies the gram amount into G_PER_L and is not authenticated as a final rate. Preserve the batch mass and supplied form; do not infer measured final volume from 500 ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 6.10225,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[3]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.6", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final rate", "interpretation": "The current primary gives 0.6 g per listed batch; the API explicitly declares g_l=0.593472 on volume 1011 ml. The local number copies the gram amount into G_PER_L and is not authenticated as a final rate. Preserve the batch mass and supplied form; do not infer measured final volume from 500 ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.593472,\n                        \"mmol_l\": 2.47093,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[4]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\": \"Na2S x 9 H2O\",\n          \"volume\": 0.6,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final rate", "interpretation": "The current primary gives 1 g per listed batch; the API explicitly declares g_l=0.98912 on volume 1011 ml. The local number copies the gram amount into G_PER_L and is not authenticated as a final rate. Preserve the batch mass and supplied form; do not infer measured final volume from 500 ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 9.33237,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[5]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\": \"Na2CO3\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001045\",\n          \"gmo_id\": \"GMO_001045\",\n          \"label\": \"Sodium carbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final rate", "interpretation": "The current primary gives 3 g per listed batch; the API explicitly declares g_l=2.96736 on volume 1011 ml. The local number copies the gram amount into G_PER_L and is not authenticated as a final rate. Preserve the batch mass and supplied form; do not infer measured final volume from 500 ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.96736,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[6]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract (OXOID)\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001935\",\n          \"gmo_id\": \"GMO_001935\",\n          \"label\": \"Oxoid &amp;trade; Yeast extract powder\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Sodium resazurin solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main batch liquid addition", "interpretation": "The source specifies 0.5 ml of 0.1% w/v solution, not 0.5 g/L. 0.1 g/100 ml is 0.001 g/ml, so this dose contributes 0.0005 g to the batch. That mass is not a new final concentration; preserve dose and stock strength separately.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[0]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\": \"Sodium resazurin (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001453\",\n          \"gmo_id\": \"GMO_001453\",\n          \"label\": \"Sodium resazurin solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Collapsed water", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "3500.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "3500.0", "unit": "G_PER_L"}}], "decision": "correct", "stage": "four different preparation stages", "interpretation": "3500 G_PER_L is the sum of 500 ml main water and three separate 1000 ml stock preparations. Restore each absolute liquid amount in its own context; do not add stock preparation water to the receiving medium or assert final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[15]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[10]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[10]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Synthetic seawater dose", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "500", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "500", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main batch stock addition", "interpretation": "Restore 500 ml of the separately defined 2x seawater stock. 500 G_PER_L is dimensionally wrong; neither 500 ml/L nor final concentrations are inferred without a final-medium basis.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Synthetic seawater (2 x conc.)\",\n                        \"solution_id\": 5655,\n                        \"attribute\": \"\",\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "N2", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "correct", "stage": "stage-specific gas atmospheres", "interpretation": "These are procedural gases: 80% N2/20% CO2 for main sparging and carbonate stock; 100% N2 for yeast, vitamin and sulfide stocks. Replace unqualified VARIABLE direct ingredient placement with the source stages, retaining 30–45 min sparging and no invented dissolved-gas concentration.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate, yeast extract, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are sterilized by filtration. Adjust pH of complete medium to 6.8, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "correct", "stage": "stage-specific gas atmospheres", "interpretation": "These are procedural gases: 80% N2/20% CO2 for main sparging and carbonate stock; 100% N2 for yeast, vitamin and sulfide stocks. Replace unqualified VARIABLE direct ingredient placement with the source stages, retaining 30–45 min sparging and no invented dissolved-gas concentration.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate, yeast extract, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are sterilized by filtration. Adjust pH of complete medium to 6.8, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "17.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "17.0", "unit": "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks", "interpretation": "The local sum combines 3 g in the mineral stock with 14 g in the seawater stock. Keep those source rows separate, each with its own 1000 ml preparation water and receiving doses 10 ml and 500 ml. The sum is neither a valid stock composition nor a supported direct-medium rate.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 14,\n                        \"unit\": \"g\",\n                        \"g_l\": 14,\n                        \"mmol_l\": 56.8007,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "56.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "56.4", "unit": "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks", "interpretation": "The local sum combines 1 g in the mineral stock with 55.4 g in the seawater stock. Keep those source rows separate, each with its own 1000 ml preparation water and receiving doses 10 ml and 500 ml. The sum is neither a valid stock composition nor a supported direct-medium rate.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 55.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 55.4,\n                        \"mmol_l\": 947.981,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.6", "unit": "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks", "interpretation": "The local sum combines 0.1 g in the mineral stock with 1.5 g in the seawater stock. Keep those source rows separate, each with its own 1000 ml preparation water and receiving doses 10 ml and 500 ml. The sum is neither a valid stock composition nor a supported direct-medium rate.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[7]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 10.203,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.06999999999999999", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.06999999999999999", "unit": "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks", "interpretation": "The local sum combines 0.01 g in the mineral stock with 0.06 g in the seawater stock. Keep those source rows separate, each with its own 1000 ml preparation water and receiving doses 10 ml and 500 ml. The sum is neither a valid stock composition nor a supported direct-medium rate.", "sources": [{"locator": "$.data.solutions[1].recipe[10]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[9]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.01 g; provider-declared stock rate is 0.01 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[11]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "FeSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.1 g; provider-declared stock rate is 0.1 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.03 g; provider-declared stock rate is 0.03 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[12]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "ZnSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.18 g; provider-declared stock rate is 0.18 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "CuSO4 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.01 g; provider-declared stock rate is 0.01 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.3 mg; provider-declared stock rate is 0.0003 g/L. The mg-to-g conversion is /1000; the local value is 1000-fold too large even at stock stage. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[13]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "CoSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.18 g; provider-declared stock rate is 0.18 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "AlK(SO4)2 x 12 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.02 g; provider-declared stock rate is 0.02 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[9]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "Nitrilotriacetic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 1.5 g; provider-declared stock rate is 1.5 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.4 mg; provider-declared stock rate is 0.0004 g/L. The mg-to-g conversion is /1000; the local value is 1000-fold too large even at stock stage. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[14]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "MnSO4 x H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock", "interpretation": "Source stock input is 0.5 g; provider-declared stock rate is 0.5 g/L. The local number matches the declared stock rate, but its direct-medium placement is wrong. Preserve the source stock and 10 ml receiving dose, with no inferred final-medium concentration. The source water is a preparation input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "11", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "11", "unit": "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation": "Preserve 11 g in the seawater preparation; API declared stock rate 11 g/L. The number belongs to the stock, not directly to the medium. Keep the stock water and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[4]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 11,\n                        \"unit\": \"g\",\n                        \"g_l\": 11,\n                        \"mmol_l\": 54.1064,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "1.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "1.3", "unit": "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation": "Preserve 1.3 g in the seawater preparation; API declared stock rate 1.3 g/L. The number belongs to the stock, not directly to the medium. Keep the stock water and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[6]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.3,\n                        \"mmol_l\": 17.438,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "NaBr", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation": "Preserve 0.2 g in the seawater preparation; API declared stock rate 0.2 g/L. The number belongs to the stock, not directly to the medium. Keep the stock water and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[8]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.94382,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "SrCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation": "Preserve 0.03 g in the seawater preparation; API declared stock rate 0.03 g/L. The number belongs to the stock, not directly to the medium. Keep the stock water and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"SrCl2 x 6 H2O\",\n                        \"compound_id\": 176,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.112521,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "KI", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation": "Preserve 0.1 mg in the seawater preparation; API declared stock rate 0.0001 g/L. The source uses mg, so the local numeric G_PER_L is 1000-fold too large. Keep the stock water and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KI\",\n                        \"compound_id\": 354,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 0.000385587,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "Na3-citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation": "Preserve 20 mg in the seawater preparation; API declared stock rate 0.02 g/L. The source uses mg, so the local numeric G_PER_L is 1000-fold too large. Keep the stock water and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[5]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na3-citrate\",\n                        \"compound_id\": 205,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0774987,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "20 mg equals 0.02 g in this stock; API explicitly declares 0.02 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[8]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "100 mg equals 0.1 g in this stock; API explicitly declares 0.1 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "20 mg equals 0.02 g in this stock; API explicitly declares 0.02 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[36].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[36].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "1 mg equals 0.001 g in this stock; API explicitly declares 0.001 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[7]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[37].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[37].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[38].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[38].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[5]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[39].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[39].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[9]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[40].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "ingredients[40].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation": "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the stock constituent in the receiving medium. Restore the stock with its 1 ml batch addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "Modified Wolin's mineral solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main batch stock dose", "interpretation": "The source dose is 10 ml, not g/L. Retain exact stock identity and complete composition rather than an empty Unknown solution; attach dose evidence at enclosing root scope, not an unsupported SolutionDescriptor.evidence field.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "Wolin's vitamin solution (10x)", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main batch stock dose", "interpretation": "The source dose is 1 ml, not g/L. Retain exact stock identity and complete composition rather than an empty Unknown solution; attach dose evidence at enclosing root scope, not an unsupported SolutionDescriptor.evidence field.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "KOH titrant", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "correct", "stage": "mineral stock pH adjustment", "interpretation": "KOH is an unquantified mineral-stock titrant: first pH 6.5 while dissolving NTA, then pH 7.0 after minerals. It is not a separate receiving-medium VARIABLE solution. No fixed dose or strength is supplied.", "sources": [{"locator": "$.data.solutions[1].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "Standalone Nitrilotriacetic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 1.5 g and the explicit provider stock rate 1.5 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Nitrilotriacetic acid\",\n                \"compound_id\": 189,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.84765,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q46", "subject": "Standalone MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 3 g and the explicit provider stock rate 3 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"MgSO4 x 7 H2O\",\n                \"compound_id\": 8,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"g\",\n                \"g_l\": 3,\n                \"mmol_l\": 12.1716,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject": "Standalone MnSO4 x H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.5 g and the explicit provider stock rate 0.5 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"MnSO4 x H2O\",\n                \"compound_id\": 14,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 2.9583,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q48", "subject": "Standalone NaCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 1 g and the explicit provider stock rate 1 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"NaCl\",\n                \"compound_id\": 43,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\": \"g\",\n                \"g_l\": 1,\n                \"mmol_l\": 17.1116,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject": "Standalone FeSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.1 g and the explicit provider stock rate 0.1 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"FeSO4 x 7 H2O\",\n                \"compound_id\": 12,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\": \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.359693,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject": "Standalone CoSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[5].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.18 g and the explicit provider stock rate 0.18 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoSO4 x 7 H2O\",\n                \"compound_id\": 198,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.18,\n                \"unit\": \"g\",\n                \"g_l\": 0.18,\n                \"mmol_l\": 1.16132,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q51", "subject": "Standalone CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[6].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.1 g and the explicit provider stock rate 0.1 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[6]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CaCl2 x 2 H2O\",\n                \"compound_id\": 7,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\": \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.680203,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q52", "subject": "Standalone ZnSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[7].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.18 g and the explicit provider stock rate 0.18 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[7]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\": 35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.18,\n                \"unit\": \"g\",\n                \"g_l\": 0.18,\n                \"mmol_l\": 0.625954,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q53", "subject": "Standalone CuSO4 x 5 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[8].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.01 g and the explicit provider stock rate 0.01 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[8]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"CuSO4 x 5 H2O\",\n                \"compound_id\": 121,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\": \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0400503,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject": "Standalone AlK(SO4)2 x 12 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[9].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.02 g and the explicit provider stock rate 0.02 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[9]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                \"compound_id\": 908,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\": \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0421596,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q55", "subject": "Standalone H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[10].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.01 g and the explicit provider stock rate 0.01 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[10]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 11,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\": \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.161708,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q56", "subject": "Standalone Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[11].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.01 g and the explicit provider stock rate 0.01 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[11]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 12,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\": \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0413309,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q57", "subject": "Standalone NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[12].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.03 g and the explicit provider stock rate 0.03 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[12]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 13,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.231483,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q58", "subject": "Standalone Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[13].concentration", "original": {"value": "0.0003", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.3 mg and the explicit provider stock rate 0.0003 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[13]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 14,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.0003,\n                \"mmol_l\": 0.00114062,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q59", "subject": "Standalone Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[14].concentration", "original": {"value": "0.0004", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 0.4 mg and the explicit provider stock rate 0.0004 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[14]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 15,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.0004,\n                \"mmol_l\": 0.00121267,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q60", "subject": "Standalone Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[15].concentration", "original": {"value": "1", "unit": "L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 1000 ml and the absolute water input, not final volume. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[15]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": 16,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q61", "subject": "Standalone mineral titrant and sequence", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "composition[16].notes", "original": "Source identifies this titrant and pH target but gives no fixed amount; do not infer zero or a typical concentration"}, {"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml", "field_path": "preparation_notes", "original": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}], "decision": "evidence_only", "stage": "mineral stock only", "interpretation": "Correctly retains unquantified KOH and pH 6.5 then 7.0 sequence. Preserve the existing repair; nickel grounding remains separately wrong.", "sources": [{"locator": "$.data.steps[0]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\": null,\n                \"step\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\"\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q62", "subject": "Standalone Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[0].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 20 mg and the explicit provider stock rate 0.02 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q63", "subject": "Standalone Folic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[1].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 20 mg and the explicit provider stock rate 0.02 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\": 138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q64", "subject": "Standalone Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[2].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 100 mg and the explicit provider stock rate 0.1 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q65", "subject": "Standalone Thiamine HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[3].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit provider stock rate 0.05 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q66", "subject": "Standalone Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[4].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit provider stock rate 0.05 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\": 136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q67", "subject": "Standalone Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[5].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit provider stock rate 0.05 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q68", "subject": "Standalone Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[6].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit provider stock rate 0.05 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[6]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\": 1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q69", "subject": "Standalone Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[7].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 1 mg and the explicit provider stock rate 0.001 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[7]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\": \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q70", "subject": "Standalone p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[8].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit provider stock rate 0.05 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[8]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q71", "subject": "Standalone (DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[9].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit provider stock rate 0.05 g/L. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[9]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\": 252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q72", "subject": "Standalone Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[10].concentration", "original": {"value": "1", "unit": "L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock", "interpretation": "Current maintained stock preserves 1000 ml and the absolute water input, not final volume. Credit its repair and retain existing evidence. This support does not transfer a whole parent medium, validate all ontology forms or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[10]", "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\": 11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q73", "subject": "Missing main preparation and source prose conflict", "local_fields": [], "decision": "evidence_only", "stage": "main medium controls", "interpretation": "Restore 30–45 min anoxic sparging, gas-specific sterile additions, vitamin filtration and pH 6.8. DSM PDF/API specify carbonate. TOGO table also says Na2CO3 but its comments say bicarbonate: retain this discrepancy, use the direct current DSM formulation rather than silently substituting bicarbonate. No autoclave temperature or duration is invented.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate, yeast extract, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to inoculation add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins are sterilized by filtration. Adjust pH of complete medium to 6.8, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[2]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n      \"paragraph_index\": 4,\n      \"comment\": \"Prior to inoculation add bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q74", "subject": "Separate collection strain prescription", "local_fields": [], "decision": "evidence_only", "stage": "source-specific variant only", "interpretation": "DSM 21940 prescription adds 1.50 g/L nitrate after autoclaving from an anoxic stock; retain only for that explicit variant. These are source-prescribed rates, not an experimental growth observation or the base recipe.", "sources": [{"locator": "extracted-text lines 23-24", "source_key": "dsmz946a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium946a.pdf", "source_raw_sha256": "ae69365cd94153a8ccdeaf42c5363d8151612172a80bec9ac471f375572c5752", "source_text_sha256": "314eda206bd204c9e4760a963381b77b85159b021daa08279fe5b266f592f0fe", "accessed_at": "2026-10-28T06:09:03.134228Z", "exact_source_quote": "For DSM 21940: Supplement medium after autoclaving with 1.50 g/l NaNO3 added from a\nsterile anoxic stock solution.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q75", "subject": "Separate collection strain prescription", "local_fields": [], "decision": "evidence_only", "stage": "source-specific variant only", "interpretation": "DSM 101605 prescription reduces yeast extract to 0.10 g/L and adds 2.00 g/L sodium acetate and 1.00 g/L nitrate after autoclaving from anoxic stocks; retain only for that explicit variant. These are source-prescribed rates, not an experimental growth observation or the base recipe.", "sources": [{"locator": "extracted-text lines 1-1", "source_key": "dsmz946a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium946a.pdf", "source_raw_sha256": "ae69365cd94153a8ccdeaf42c5363d8151612172a80bec9ac471f375572c5752", "source_text_sha256": "314eda206bd204c9e4760a963381b77b85159b021daa08279fe5b266f592f0fe", "accessed_at": "2026-10-28T06:09:03.134228Z", "exact_source_quote": "", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch058/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:009161.

data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml: primary 38/41, secondary 35/41; data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml: primary 38/41, secondary 35/41. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:009161.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:009161.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Three stock recipes are flattened and their units are corrupted

major / open / confirmed; issue key: culturemech-009161-stock-flattening-units-and-cross-stock-sums.

The record combines three stock preparations with the main batch: water and shared salts are summed across stages, all stock constituents become direct ingredients, 14 mg inputs retain their numbers as g/L, liquid doses become g/L, and variable gas/titrant rows lose their procedural context. Ordinary main gram inputs also lack a verified final-litre basis. Complete per-field decisions distinguish supported stock rates from mass and volume errors.

### f2: Nickel hydrate and magnesium secondary mapping remain inconsistent

major / open / confirmed; issue key: culturemech-009161-hydrate-primary-secondary-disagreement.

NiCl2 hexahydrate is linked to anhydrous CHEBI:34887 in both selected primary/secondary slots and standalone mineral chebi_term. OLS candidate CHEBI:53542 explicitly supplies the hexahydrate. MgSO4 heptahydrate primary CHEBI:31795 is correct but selected secondary CHEBI:32599 remains anhydrous/generic. Preserve correct forms and values; provider mmol_l values are not used to recertify hydrates.

### f3: Preparation, pH and claim-scoped evidence are missing

major / open / confirmed; issue key: culturemech-009161-missing-stage-specific-preparation-and-evidence.

The selected layers omit pH 6.8, the complete anoxic preparation and scoped supporting evidence. TOGO bicarbonate prose conflicts with its carbonate table and direct DSM source, so a blind comment import would perpetuate a source conflict.

## Recommended Actions And Acceptance Checks

### action1

Rebuild the maintained TOGO owner with separate seawater, mineral and vitamin stocks and absolute source doses/water. Correct mg conversions, undo cross-stock sums and retain batch-versus-final-volume uncertainty; preserve all source forms and correct standalone stock repairs.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Resolve exact supplied hydrates and synchronize only the incorrect asserted slots using verified mappings; preserve the already correct magnesium primary and source masses.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the verified main and stock preparation with exact stage-scoped root evidence; explicitly document the TOGO prose discrepancy. Preserve the source distinction between base medium and named-strain prescriptions.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch058/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch058/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch058/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch058/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz946a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium946a.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current DSMZ primary PDF text and both rendered pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api946a | https://mediadive.dsmz.de/rest/medium/946a; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| togoM2594 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| solution241 | https://mediadive.dsmz.de/rest/solution/241; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon compound with formula CO&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt; in which the carbon is attached to each oxygen atom by a double bond. A colourless, odourless gas under normal conditions, it is produced during respiration by all animals, fungi and microorganisms that depend directly or indirectly on living or decaying plants for food.']; formula ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31440 = copper(II) sulfate pentahydrate; definition ['The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid.']; formula ['Cu.5H2O.O4S']; mass ['249.684']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi36385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:36385 = strontium dichloride hexahydrate; definition []; formula ['Cl2Sr.6H2O']; mass ['266.616']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:44557 = nitrilotriacetic acid; definition []; formula ['C6H9NO6']; mass ['191.139']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53258 = sodium citrate; definition ['The trisodium salt of citric acid.']; formula ['C6H5O7.3Na']; mass ['258.069']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63004 = sodium bromide; definition ['An inorganic sodium salt having bromide as the counterion.']; formula ['Br.Na']; mass ['102.894']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W']; mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used).']; formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8346 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8346; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8346 = potassium iodide; definition ['A metal iodide salt with a K(+) counterion. It is a scavenger of hydroxyl radicals.']; formula ['I.K']; mass ['166.002']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86364 = manganese(II) sulfate monohydrate; definition ['A hydrate that is the monohydrate form of manganese(II) sulfate.']; formula ['H2O.Mn.O4S']; mass ['169.016']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86465 = potassium aluminium sulfate dodecahydrate; definition ['A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water.']; formula ['Al.12H2O.K.2O4S']; mass ['474.386']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:91244 = cobalt(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of cobalt(2+) sulfate.']; formula ['Co.7H2O.O4S']; mass ['281.101']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state), chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch058/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T023456Z-CALDITHRIX_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDITHRIX_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch058/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer56 | scripts/cleanup_media_quality.py; relevant functions named in summary | context_only | Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical quantities and flags conflicting quantities rather than summing them. The old summed sodium value is a persisted record defect; it is not evidence that the current cleanup still sums unequal stages. |
| writer57 | scripts/import_mediadive_solutions.py; relevant functions named in summary | context_only | _convert_ingredient prefers provider g_l and otherwise normalizes by declared solution volume; _convert_solution retains stock identity/composition/preparation. The unit map maps ml to percentage without a separate factor, so old liquid artifacts need source review. Current repaired stock records are assessed independently of importer defaults. |
| writer58 | scripts/migrate_mgso4_heptahydrate_term.py; relevant functions named in summary | context_only | iter_ingredients and main make a label-conditional primary-term-only 32599 to 31795 repair; secondary annotations are untouched. The current primary is credited while stale secondary linkage requires separate review. |
| writer59 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer60 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer61 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer62 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| dep63 | data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep64 | data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| quantity-inventory | REVIEW_WORK/batch058/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- No measured final medium or stock volume is inferred from listed water. Provider-declared stock rates are distinguished from final-medium concentrations and unverified mmol values.
- DSM named-strain prescriptions are not growth observations and are not silently applied to the base recipe.
- Current source bytes do not recreate historical access times or execution; unrelated standalone parent recipes are outside the receiving-medium scope.
- Standalone solution5980 also cites an older medium161 raw capture; that whole payload was not re-fetched or authenticated. Its stock table is independently supported by current solution5980 and DSM946a; the separate parent formulation does not transfer.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T063254Z-caldithrix-medium-batch058
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of caldithrix_medium
started_at: '2026-10-28T06:08:29.217129Z'
finished_at: '2026-10-28T06:32:54.285807Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Caldithrix identity is supported, but the TOGO-derived formulation loses
  three stock boundaries, corrupts liquid and milligram units, sums different stages,
  and omits preparation. Existing standalone repairs and correct chemical forms are
  credited; source prose and final-volume limits remain explicit.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
    sha256: a9b30a33300b71706085724ad293ca2a4b4da297592b10404b531b460f5a002a
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    sha256: dea10ee1e675adcb88c1f4613cd5440e2b76bca2ba7b709b8a3b3174da0210c3
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml
    sha256: 3ad6e16dcff1f675260d599c644e49992fa8d76623e0889caaba21fd1e22bfab
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
    sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDITHRIX_MEDIUM.md
    sha256: 4cea31327132efa8dbff04581e1ee3c3338c484a89543a940bdca22aeae8ef42
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.md
    sha256: 7df82a7770a57f72f24743b8d450d93be1570989c0c3670ac73ebcd6eb7fae84
    role: context
  - path: reports/yaml_record_review/20260922T023456Z-CALDITHRIX_MEDIUM.md
    sha256: 4fac294d3dc75040e7cc9fa8fd49848016ae1efff3e190e901d78ad4d7abcde4
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch058 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009161
targets:
- target_id: CultureMech:009161
  path: data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
  label: caldithrix_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009161
  command: just validate-schema data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009161
  command: just validate-strict data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch058/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009161
  command: just validate-terms data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:009161
  command: just validate-references data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T06:18:01.235252Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: a9b30a33300b71706085724ad293ca2a4b4da297592b10404b531b460f5a002a
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T06:18:01.235427Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: dea10ee1e675adcb88c1f4613cd5440e2b76bca2ba7b709b8a3b3174da0210c3
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch058/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:08:30.332594Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 536d569b46c989dfb28584cc335d4b4ee03d37316d32af39fbab0f4d7138f822
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch058/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:08:31.345770Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 74aa070cef71260d7ed93c74eb160185cc06a8845cdbc7c3ac22367949080cec
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch058/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:08:32.498190Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: d3771cae82ef7a4bb54fbd776fd8902de6a759e848891e414b88f173eb3425ec
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch058/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:08:33.344762Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 428c5fc9a88732656c9e064c6744fb7fddcf54044ab792de5578cf3fa41ef551
- evidence_id: dsmz946a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium946a.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:09:03.134228Z'
  support: supports
  summary: 'Complete current DSMZ primary PDF text and both rendered pages read: exact
    main recipe, separate stock tables, preparation and any strain-specific prescriptions.
    A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: ae69365cd94153a8ccdeaf42c5363d8151612172a80bec9ac471f375572c5752
- evidence_id: api946a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/946a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:09:03.134547Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f
- evidence_id: togoM2594
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:09:03.134627Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657
- evidence_id: solution241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:09:03.134689Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:09:03.134737Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:03.134780Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:03.815820Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:03.815991Z'
  support: supports
  summary: OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic
    acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy
    group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:03.897845Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:03.988324Z'
  support: supports
  summary: OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic
    thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the
    5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.134759Z'
  support: supports
  summary: OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon
    compound with formula CO<small><sub>2</sub></small> in which the carbon is attached
    to each oxygen atom by a double bond. A colourless, odourless gas under normal
    conditions, it is produced during respiration by all animals, fungi and microorganisms
    that depend directly or indirectly on living or decaying plants for food.']; formula
    ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.176730Z'
  support: supports
  summary: OLS current exact CHEBI:17015 = riboflavin; definition ['<small>D</small>-Ribitol
    in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.446393Z'
  support: supports
  summary: OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of
    a group of cobalamin vitamers that exhibit biological activity against vitamin
    B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.539743Z'
  support: supports
  summary: OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule
    consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.545199Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.623823Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.753367Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:04.929502Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.048019Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.148518Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.153648Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.276290Z'
  support: supports
  summary: OLS current exact CHEBI:31440 = copper(II) sulfate pentahydrate; definition
    ['The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid.'];
    formula ['Cu.5H2O.O4S']; mass ['249.684']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.351563Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.563468Z'
  support: supports
  summary: OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A
    hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn'];
    mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.645693Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.750828Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.766547Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.889221Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi36385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:05.963163Z'
  support: supports
  summary: OLS current exact CHEBI:36385 = strontium dichloride hexahydrate; definition
    []; formula ['Cl2Sr.6H2O']; mass ['266.616']; obsolete=False. Literal label is
    distinct from supplied-form equivalence.
  snapshot_sha256: a81397c907aeb36242c9f0a2aa24979df4b9aad2f624e8991ccd87a4ff9428b5
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.169663Z'
  support: supports
  summary: OLS current exact CHEBI:44557 = nitrilotriacetic acid; definition []; formula
    ['C6H9NO6']; mass ['191.139']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.243431Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi53258
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.341146Z'
  support: supports
  summary: OLS current exact CHEBI:53258 = sodium citrate; definition ['The trisodium
    salt of citric acid.']; formula ['C6H5O7.3Na']; mass ['258.069']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
- evidence_id: chebi63004
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.387276Z'
  support: supports
  summary: OLS current exact CHEBI:63004 = sodium bromide; definition ['An inorganic
    sodium salt having bromide as the counterion.']; formula ['Br.Na']; mass ['102.894'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2665f3a4301ab51b67b814a8694bc906c1a13c9b301c85a4416891d3f9412c90
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.483977Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.543910Z'
  support: supports
  summary: OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen
    peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W'];
    mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.784493Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.876727Z'
  support: supports
  summary: OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a
    source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage
    treatments; for solid-dosage treatments, the monohydrate is normally used).'];
    formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:06.932814Z'
  support: supports
  summary: OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition
    ['A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O.'];
    formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi8346
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8346
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:07.024201Z'
  support: supports
  summary: OLS current exact CHEBI:8346 = potassium iodide; definition ['A metal iodide
    salt with a K(+) counterion. It is a scavenger of hydroxyl radicals.']; formula
    ['I.K']; mass ['166.002']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 261d4862f5ae3627f515eefe14ca4f27cfed8c87604dbf8b8206b81af884631d
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:07.085930Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:07.159523Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:07.390043Z'
  support: supports
  summary: OLS current exact CHEBI:86364 = manganese(II) sulfate monohydrate; definition
    ['A hydrate that is the monohydrate form of manganese(II) sulfate.']; formula
    ['H2O.Mn.O4S']; mass ['169.016']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:07.489529Z'
  support: supports
  summary: OLS current exact CHEBI:86465 = potassium aluminium sulfate dodecahydrate;
    definition ['A hydrate resulting from the the formal combination of anhydrous
    potassium aluminium sulfate with 12 mol eq. of water.']; formula ['Al.12H2O.K.2O4S'];
    mass ['474.386']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:07.538832Z'
  support: supports
  summary: OLS current exact CHEBI:91244 = cobalt(2+) sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of cobalt(2+) sulfate.']; formula ['Co.7H2O.O4S'];
    mass ['281.101']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:09:15.730936Z'
  support: supports
  summary: OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition
    ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state),
    chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass
    ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch058/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T06:18:01.250688Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: e6badc6681990901be9a09210ab6f97469e77b249e5f838e0262e4efd2b26fdb
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T023456Z-CALDITHRIX_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:18:01.251170Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 4fac294d3dc75040e7cc9fa8fd49848016ae1efff3e190e901d78ad4d7abcde4
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:18:01.251195Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 7df82a7770a57f72f24743b8d450d93be1570989c0c3670ac73ebcd6eb7fae84
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDITHRIX_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:18:01.251221Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 4cea31327132efa8dbff04581e1ee3c3338c484a89543a940bdca22aeae8ef42
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch058/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T06:18:01.251242Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 72765f22f1787a280ac17c5af929eb312b9f4375a001e01485e739096267ac52
- evidence_id: writer56
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251267Z'
  support: context_only
  summary: Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical
    quantities and flags conflicting quantities rather than summing them. The old
    summed sodium value is a persisted record defect; it is not evidence that the
    current cleanup still sums unequal stages.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer57
  kind: record_content
  reference: scripts/import_mediadive_solutions.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251289Z'
  support: context_only
  summary: _convert_ingredient prefers provider g_l and otherwise normalizes by declared
    solution volume; _convert_solution retains stock identity/composition/preparation.
    The unit map maps ml to percentage without a separate factor, so old liquid artifacts
    need source review. Current repaired stock records are assessed independently
    of importer defaults.
  snapshot_sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
- evidence_id: writer58
  kind: record_content
  reference: scripts/migrate_mgso4_heptahydrate_term.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251308Z'
  support: context_only
  summary: iter_ingredients and main make a label-conditional primary-term-only 32599
    to 31795 repair; secondary annotations are untouched. The current primary is credited
    while stale secondary linkage requires separate review.
  snapshot_sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
- evidence_id: writer59
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251340Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer60
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251359Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer61
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251379Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:18:01.251399Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: dep63
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T06:18:01.251405Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 3ad6e16dcff1f675260d599c644e49992fa8d76623e0889caaba21fd1e22bfab
- evidence_id: dep64
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T06:18:01.251406Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch058/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T06:18:02.071495Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 9c66786dbe5226653f1634714b7ac4ee03643cdd2c52f700fd4bba72ccf06c81
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source identity
  outcome: supported
  summary: The TOGO M2594 identity points to DSM 946a, confirmed by current payload
    and primary PDF. Standalone solutions 241/5980 are bounded stock dependencies,
    not owners or alternate whole media.
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - local0
  - togoM2594
  - dsmz946a
- assessment_id: a2
  area: evidence
  topic: Historical and attached claims
  outcome: concern
  summary: Selected target/owner have no attached scientific claims. Standalone stock
    repairs retain substantive quantity evidence and source hashes, and current stock
    bytes and rows are checked. Earlier September review identifies topology errors
    but its per-final-litre recommendations exceed the current final-volume evidence.
    Current sources govern; no historical source access or execution is recreated.
    Current solution241 raw SHA matches the historical 50cc42c2 digest and all 17
    attached excerpts literally; current solution5980 raw matches 2fe24a83 and all
    11 solution-specific excerpts. Its additional medium161 recipe-array claim is
    retained as separate derivative context without authenticating that whole raw
    payload or transferring its parent medium.
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - history-auth
  - grounding
  - solution241
  - solution5980
- assessment_id: a3
  area: provenance
  topic: Present writers and repair credit
  outcome: supported
  summary: Current TOGO code preserves sections and distinguishes units; current cleanup
    no longer sums conflicting duplicate quantities. The magnesium primary-only repair
    explains its bounded scope and does not fix secondary mapping. Current conservative
    merging preserves scientific fields; the persisted flattening is not proof that
    these current writers still flatten.
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - grounding
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
  - writer61
  - writer62
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 88 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009161",
    "selected_concentration_field_count": 88, "selected_concentration_fields_covered":
    88, "decisions": [{"decision_id": "q1", "subject": "KH2PO4", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[2].concentration",
    "original": {"value": "0.33", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.33", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final
    rate", "interpretation": "The current primary gives 0.33 g per listed batch; the
    API explicitly declares g_l=0.326409 on volume 1011 ml. The local number copies
    the gram amount into G_PER_L and is not authenticated as a final rate. Preserve
    the batch mass and supplied form; do not infer measured final volume from 500
    ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    2.39857,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[2]", "source_key": "togoM2594",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594",
    "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject":
    "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.33", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.33", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final
    rate", "interpretation": "The current primary gives 0.33 g per listed batch; the
    API explicitly declares g_l=0.326409 on volume 1011 ml. The local number copies
    the gram amount into G_PER_L and is not authenticated as a final rate. Preserve
    the batch mass and supplied form; do not infer measured final volume from 500
    ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    6.10225,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[3]", "source_key": "togoM2594",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594",
    "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q3", "subject": "Na2S x 9 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "0.6", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.6", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final
    rate", "interpretation": "The current primary gives 0.6 g per listed batch; the
    API explicitly declares g_l=0.593472 on volume 1011 ml. The local number copies
    the gram amount into G_PER_L and is not authenticated as a final rate. Preserve
    the batch mass and supplied form; do not infer measured final volume from 500
    ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[8]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.593472,\n                        \"mmol_l\":
    2.47093,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[4]", "source_key": "togoM2594",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594",
    "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2S x 9 H2O\",\n          \"volume\": 0.6,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\":
    \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q4", "subject": "Na2CO3", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path": "ingredients[5].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final
    rate", "interpretation": "The current primary gives 1 g per listed batch; the
    API explicitly declares g_l=0.98912 on volume 1011 ml. The local number copies
    the gram amount into G_PER_L and is not authenticated as a final rate. Preserve
    the batch mass and supplied form; do not infer measured final volume from 500
    ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\":
    9.33237,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[5]", "source_key": "togoM2594",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594",
    "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2CO3\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001045\",\n          \"gmo_id\": \"GMO_001045\",\n          \"label\":
    \"Sodium carbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject":
    "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main batch amount versus final
    rate", "interpretation": "The current primary gives 3 g per listed batch; the
    API explicitly declares g_l=2.96736 on volume 1011 ml. The local number copies
    the gram amount into G_PER_L and is not authenticated as a final rate. Preserve
    the batch mass and supplied form; do not infer measured final volume from 500
    ml water plus 500 ml seawater and additions.", "sources": [{"locator": "$.data.solutions[0].recipe[6]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.96736,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[6]", "source_key": "togoM2594",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594",
    "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract (OXOID)\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001935\",\n          \"gmo_id\": \"GMO_001935\",\n          \"label\":
    \"Oxoid &trade; Yeast extract powder\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            },\n            {\n              \"id\":
    \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\":
    \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject":
    "Sodium resazurin solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main batch liquid addition", "interpretation":
    "The source specifies 0.5 ml of 0.1% w/v solution, not 0.5 g/L. 0.1 g/100 ml is
    0.001 g/ml, so this dose contributes 0.0005 g to the batch. That mass is not a
    new final concentration; preserve dose and stock strength separately.", "sources":
    [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api946a", "reference":
    "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "$.components[0].items[0]", "source_key": "togoM2594", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594",
    "source_raw_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "source_text_sha256": "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657",
    "accessed_at": "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n          \"component_name\":
    \"Sodium resazurin (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001453\",\n          \"gmo_id\": \"GMO_001453\",\n          \"label\":
    \"Sodium resazurin solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "Collapsed water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "3500.0", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "3500.0",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "four different preparation
    stages", "interpretation": "3500 G_PER_L is the sum of 500 ml main water and three
    separate 1000 ml stock preparations. Restore each absolute liquid amount in its
    own context; do not add stock preparation water to the receiving medium or assert
    final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 500,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[15]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[10]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[10]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "Synthetic seawater dose",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "500", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "500", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main batch stock addition", "interpretation":
    "Restore 500 ml of the separately defined 2x seawater stock. 500 G_PER_L is dimensionally
    wrong; neither 500 ml/L nor final concentrations are inferred without a final-medium
    basis.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Synthetic seawater (2 x conc.)\",\n                        \"solution_id\":
    5655,\n                        \"attribute\": \"\",\n                        \"amount\":
    500,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q9", "subject": "N2", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "correct", "stage": "stage-specific gas atmospheres",
    "interpretation": "These are procedural gases: 80% N2/20% CO2 for main sparging
    and carbonate stock; 100% N2 for yeast, vitamin and sulfide stocks. Replace unqualified
    VARIABLE direct ingredient placement with the source stages, retaining 30–45 min
    sparging and no invented dissolved-gas concentration.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients (except carbonate, yeast extract, vitamins and sulfide),
    then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Prior to inoculation add carbonate from a
    sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas. Vitamins are sterilized by filtration. Adjust pH of complete
    medium to 6.8, if necessary.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "Carbon dioxide gas",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "correct", "stage": "stage-specific gas atmospheres",
    "interpretation": "These are procedural gases: 80% N2/20% CO2 for main sparging
    and carbonate stock; 100% N2 for yeast, vitamin and sulfide stocks. Replace unqualified
    VARIABLE direct ingredient placement with the source stages, retaining 30–45 min
    sparging and no invented dissolved-gas concentration.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients (except carbonate, yeast extract, vitamins and sulfide),
    then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Prior to inoculation add carbonate from a
    sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas. Vitamins are sterilized by filtration. Adjust pH of complete
    medium to 6.8, if necessary.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "MgSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "original": {"value": "17.0", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "17.0", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks",
    "interpretation": "The local sum combines 3 g in the mineral stock with 14 g in
    the seawater stock. Keep those source rows separate, each with its own 1000 ml
    preparation water and receiving doses 10 ml and 500 ml. The sum is neither a valid
    stock composition nor a supported direct-medium rate.", "sources": [{"locator":
    "$.data.solutions[1].recipe[1]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 14,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 14,\n                        \"mmol_l\":
    56.8007,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "56.4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "56.4", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks",
    "interpretation": "The local sum combines 1 g in the mineral stock with 55.4 g
    in the seawater stock. Keep those source rows separate, each with its own 1000
    ml preparation water and receiving doses 10 ml and 500 ml. The sum is neither
    a valid stock composition nor a supported direct-medium rate.", "sources": [{"locator":
    "$.data.solutions[1].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 55.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 55.4,\n                        \"mmol_l\":
    947.981,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "CaCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "1.6", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.6", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater stocks",
    "interpretation": "The local sum combines 0.1 g in the mineral stock with 1.5
    g in the seawater stock. Keep those source rows separate, each with its own 1000
    ml preparation water and receiving doses 10 ml and 500 ml. The sum is neither
    a valid stock composition nor a supported direct-medium rate.", "sources": [{"locator":
    "$.data.solutions[1].recipe[6]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[7]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    10.203,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "0.06999999999999999",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.06999999999999999",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "distinct mineral and seawater
    stocks", "interpretation": "The local sum combines 0.01 g in the mineral stock
    with 0.06 g in the seawater stock. Keep those source rows separate, each with
    its own 1000 ml preparation water and receiving doses 10 ml and 500 ml. The sum
    is neither a valid stock composition nor a supported direct-medium rate.", "sources":
    [{"locator": "$.data.solutions[1].recipe[10]", "source_key": "api946a", "reference":
    "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[9]", "source_key":
    "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a", "source_raw_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "source_text_sha256":
    "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f", "accessed_at":
    "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.06,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\":
    0.970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.01 g; provider-declared stock rate
    is 0.01 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[11]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "FeSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.1 g; provider-declared stock rate is
    0.1 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.03 g; provider-declared stock rate
    is 0.03 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[12]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "ZnSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "0.18", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.18", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.18 g; provider-declared stock rate
    is 0.18 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[7]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "CuSO4 x 5 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.01 g; provider-declared stock rate
    is 0.01 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "Na2SeO3 x 5 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.3 mg; provider-declared stock rate
    is 0.0003 g/L. The mg-to-g conversion is /1000; the local value is 1000-fold too
    large even at stock stage. Preserve the source stock and 10 ml receiving dose,
    with no inferred final-medium concentration. The source water is a preparation
    input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[13]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject":
    "CoSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.18", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.18", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.18 g; provider-declared stock rate
    is 0.18 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "AlK(SO4)2 x 12 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.02 g; provider-declared stock rate
    is 0.02 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[9]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "Nitrilotriacetic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 1.5 g; provider-declared stock rate is
    1.5 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "Na2WO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.4", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.4 mg; provider-declared stock rate
    is 0.0004 g/L. The mg-to-g conversion is /1000; the local value is 1000-fold too
    large even at stock stage. Preserve the source stock and 10 ml receiving dose,
    with no inferred final-medium concentration. The source water is a preparation
    input, not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[14]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject":
    "MnSO4 x H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "modified Wolin mineral stock",
    "interpretation": "Source stock input is 0.5 g; provider-declared stock rate is
    0.5 g/L. The local number matches the declared stock rate, but its direct-medium
    placement is wrong. Preserve the source stock and 10 ml receiving dose, with no
    inferred final-medium concentration. The source water is a preparation input,
    not a measured final volume.", "sources": [{"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "MgCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[25].concentration", "original": {"value": "11", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "11", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation":
    "Preserve 11 g in the seawater preparation; API declared stock rate 11 g/L. The
    number belongs to the stock, not directly to the medium. Keep the stock water
    and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[4]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 11,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 11,\n                        \"mmol_l\":
    54.1064,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[26].concentration", "original": {"value": "1.3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "1.3", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation":
    "Preserve 1.3 g in the seawater preparation; API declared stock rate 1.3 g/L.
    The number belongs to the stock, not directly to the medium. Keep the stock water
    and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[6]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 1.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.3,\n                        \"mmol_l\":
    17.438,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "NaBr", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[27].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation":
    "Preserve 0.2 g in the seawater preparation; API declared stock rate 0.2 g/L.
    The number belongs to the stock, not directly to the medium. Keep the stock water
    and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[8]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\":
    353,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.94382,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "SrCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[28].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation":
    "Preserve 0.03 g in the seawater preparation; API declared stock rate 0.03 g/L.
    The number belongs to the stock, not directly to the medium. Keep the stock water
    and 500 ml receiving dose separate.", "sources": [{"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"SrCl2 x 6 H2O\",\n                        \"compound_id\":
    176,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.112521,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "KI", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[29].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation":
    "Preserve 0.1 mg in the seawater preparation; API declared stock rate 0.0001 g/L.
    The source uses mg, so the local numeric G_PER_L is 1000-fold too large. Keep
    the stock water and 500 ml receiving dose separate.", "sources": [{"locator":
    "$.data.solutions[2].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KI\",\n                        \"compound_id\":
    354,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\":
    0.000385587,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject":
    "Na3-citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "2x synthetic seawater stock", "interpretation":
    "Preserve 20 mg in the seawater preparation; API declared stock rate 0.02 g/L.
    The source uses mg, so the local numeric G_PER_L is 1000-fold too large. Keep
    the stock water and 500 ml receiving dose separate.", "sources": [{"locator":
    "$.data.solutions[2].recipe[5]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na3-citrate\",\n                        \"compound_id\":
    205,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0774987,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q32", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[31].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "20 mg equals 0.02 g in this stock; API explicitly declares 0.02 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[8]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[33].concentration", "original": {"value": "50", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[3]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q35", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "100 mg equals 0.1 g in this stock; API explicitly declares 0.1 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[35].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[35].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "20 mg equals 0.02 g in this stock; API explicitly declares 0.02 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[1]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q37", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[36].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[36].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "1 mg equals 0.001 g in this stock; API explicitly declares 0.001 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[7]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject":
    "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[37].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[37].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q39", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "ingredients[38].concentration", "original": {"value": "50", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[38].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[5]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q40", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[39].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[39].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[9]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q41", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "ingredients[40].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "ingredients[40].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "10x Wolin vitamin stock", "interpretation":
    "50 mg equals 0.05 g in this stock; API explicitly declares 0.05 g/L stock. Local
    G_PER_L retains the mg number, a 1000-fold unit error, and wrongly places the
    stock constituent in the receiving medium. Restore the stock with its 1 ml batch
    addition; no final-medium rate inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[6]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q42", "subject": "Modified Wolin''s mineral
    solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main batch stock dose", "interpretation":
    "The source dose is 10 ml, not g/L. Retain exact stock identity and complete composition
    rather than an empty Unknown solution; attach dose evidence at enclosing root
    scope, not an unsupported SolutionDescriptor.evidence field.", "sources": [{"locator":
    "$.data.solutions[0].recipe[3]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q43", "subject": "Wolin''s vitamin solution
    (10x)", "local_fields": [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main batch stock dose", "interpretation":
    "The source dose is 1 ml, not g/L. Retain exact stock identity and complete composition
    rather than an empty Unknown solution; attach dose evidence at enclosing root
    scope, not an unsupported SolutionDescriptor.evidence field.", "sources": [{"locator":
    "$.data.solutions[0].recipe[7]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q44", "subject": "KOH titrant", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml", "field_path":
    "solutions[2].concentration", "original": {"value": "variable", "unit": "VARIABLE"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "correct", "stage": "mineral stock pH adjustment",
    "interpretation": "KOH is an unquantified mineral-stock titrant: first pH 6.5
    while dissolving NTA, then pH 7.0 after minerals. It is not a separate receiving-medium
    VARIABLE solution. No fixed dose or strength is supplied.", "sources": [{"locator":
    "$.data.solutions[1].steps[0]", "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add
    minerals. Adjust final to pH 7.0 with KOH.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q45", "subject": "Standalone Nitrilotriacetic
    acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 1.5 g and the explicit
    provider stock rate 1.5 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[0]", "source_key":
    "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at":
    "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"Nitrilotriacetic acid\",\n                \"compound_id\":
    189,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.84765,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q46", "subject": "Standalone MgSO4 x 7 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[1].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 3 g and the explicit
    provider stock rate 3 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[1]", "source_key":
    "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at":
    "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"MgSO4 x 7 H2O\",\n                \"compound_id\":
    8,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"g\",\n                \"g_l\": 3,\n                \"mmol_l\": 12.1716,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q47", "subject": "Standalone MnSO4 x H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.5 g and the explicit
    provider stock rate 0.5 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[2]", "source_key":
    "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at":
    "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"MnSO4 x H2O\",\n                \"compound_id\":
    14,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 2.9583,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q48", "subject": "Standalone NaCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 1 g and the explicit
    provider stock rate 1 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[3]", "source_key":
    "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at":
    "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"NaCl\",\n                \"compound_id\":
    43,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\":
    \"g\",\n                \"g_l\": 1,\n                \"mmol_l\": 17.1116,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q49", "subject": "Standalone FeSO4 x 7 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[4].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.1 g and the explicit
    provider stock rate 0.1 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[4]", "source_key":
    "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at":
    "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"FeSO4 x 7 H2O\",\n                \"compound_id\":
    12,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.359693,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q50", "subject": "Standalone CoSO4 x 7 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[5].concentration", "original": {"value": "0.18", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.18 g and the explicit
    provider stock rate 0.18 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[5]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"CoSO4 x 7 H2O\",\n                \"compound_id\":
    198,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.18,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.18,\n                \"mmol_l\": 1.16132,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q51", "subject": "Standalone CaCl2 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[6].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.1 g and the explicit
    provider stock rate 0.1 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[6]", "source_key":
    "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241", "source_raw_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "source_text_sha256":
    "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d", "accessed_at":
    "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"CaCl2 x 2 H2O\",\n                \"compound_id\":
    7,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.1,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.680203,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q52", "subject": "Standalone ZnSO4 x 7 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[7].concentration", "original": {"value": "0.18", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.18 g and the explicit
    provider stock rate 0.18 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[7]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\":
    35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.18,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.18,\n                \"mmol_l\": 0.625954,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q53", "subject": "Standalone CuSO4 x 5 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[8].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.01 g and the explicit
    provider stock rate 0.01 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[8]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    9,\n                \"compound\": \"CuSO4 x 5 H2O\",\n                \"compound_id\":
    121,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0400503,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q54", "subject": "Standalone AlK(SO4)2 x 12 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[9].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.02 g and the explicit
    provider stock rate 0.02 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[9]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    10,\n                \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                \"compound_id\":
    908,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.02,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0421596,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q55", "subject": "Standalone H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[10].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.01 g and the explicit
    provider stock rate 0.01 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[10]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    11,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.161708,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q56", "subject": "Standalone Na2MoO4 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[11].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.01 g and the explicit
    provider stock rate 0.01 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[11]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    12,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.01,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0413309,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q57", "subject": "Standalone NiCl2 x 6 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[12].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 0.03 g and the explicit
    provider stock rate 0.03 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[12]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    13,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.231483,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q58", "subject": "Standalone Na2SeO3 x 5 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[13].concentration", "original": {"value": "0.0003",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped
    standalone stock", "interpretation": "Current maintained stock preserves 0.3 mg
    and the explicit provider stock rate 0.0003 g/L. Credit its repair and retain
    existing evidence. This support does not transfer a whole parent medium, validate
    all ontology forms or authenticate provider mmol_l.", "sources": [{"locator":
    "$.data.recipe[13]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    14,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\":
    107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.3,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.0003,\n                \"mmol_l\": 0.00114062,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q59", "subject": "Standalone Na2WO4 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[14].concentration", "original": {"value": "0.0004",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped
    standalone stock", "interpretation": "Current maintained stock preserves 0.4 mg
    and the explicit provider stock rate 0.0004 g/L. Credit its repair and retain
    existing evidence. This support does not transfer a whole parent medium, validate
    all ontology forms or authenticate provider mmol_l.", "sources": [{"locator":
    "$.data.recipe[14]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    15,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\":
    249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.0004,\n                \"mmol_l\": 0.00121267,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q60", "subject": "Standalone Distilled water", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[15].concentration", "original": {"value": "1", "unit":
    "L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock",
    "interpretation": "Current maintained stock preserves 1000 ml and the absolute
    water input, not final volume. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[15]",
    "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    16,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q61", "subject": "Standalone mineral titrant and sequence", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "composition[16].notes", "original": "Source identifies this titrant
    and pH target but gives no fixed amount; do not infer zero or a typical concentration"},
    {"record_path": "data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml",
    "field_path": "preparation_notes", "original": "First dissolve nitrilotriacetic
    acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0
    with KOH."}], "decision": "evidence_only", "stage": "mineral stock only", "interpretation":
    "Correctly retains unquantified KOH and pH 6.5 then 7.0 sequence. Preserve the
    existing repair; nickel grounding remains separately wrong.", "sources": [{"locator":
    "$.data.steps[0]", "source_key": "solution241", "reference": "https://mediadive.dsmz.de/rest/solution/241",
    "source_raw_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "source_text_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d",
    "accessed_at": "2026-10-28T06:09:03.134689Z", "exact_source_quote": "{\n                \"recipe_order\":
    null,\n                \"step\": \"First dissolve nitrilotriacetic acid and adjust
    pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\"\n            }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q62", "subject":
    "Standalone Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 20 mg and the explicit
    provider stock rate 0.02 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[0]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q63", "subject": "Standalone Folic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[1].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 20 mg and the explicit
    provider stock rate 0.02 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[1]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\":
    138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q64", "subject": "Standalone Pyridoxine hydrochloride", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 100 mg and the explicit
    provider stock rate 0.1 g/L. Credit its repair and retain existing evidence. This
    support does not transfer a whole parent medium, validate all ontology forms or
    authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[2]", "source_key":
    "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "source_raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "source_text_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "accessed_at":
    "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\":
    519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q65", "subject": "Standalone Thiamine HCl", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit
    provider stock rate 0.05 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[3]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q66", "subject": "Standalone Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[4].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit
    provider stock rate 0.05 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[4]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\":
    136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q67", "subject": "Standalone Nicotinic acid", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[5].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit
    provider stock rate 0.05 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[5]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\":
    139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q68", "subject": "Standalone Calcium D-(+)-pantothenate", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[6].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit
    provider stock rate 0.05 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[6]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\":
    1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q69", "subject": "Standalone Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[7].concentration", "original": {"value": "0.001", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 1 mg and the explicit
    provider stock rate 0.001 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[7]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\":
    18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q70", "subject": "Standalone p-Aminobenzoic acid", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[8].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit
    provider stock rate 0.05 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[8]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\":
    47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q71", "subject": "Standalone (DL)-alpha-Lipoic acid", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[9].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "separately scoped standalone
    stock", "interpretation": "Current maintained stock preserves 50 mg and the explicit
    provider stock rate 0.05 g/L. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[9]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\":
    252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q72", "subject": "Standalone Distilled water", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[10].concentration", "original": {"value": "1", "unit":
    "L"}}], "decision": "evidence_only", "stage": "separately scoped standalone stock",
    "interpretation": "Current maintained stock preserves 1000 ml and the absolute
    water input, not final volume. Credit its repair and retain existing evidence.
    This support does not transfer a whole parent medium, validate all ontology forms
    or authenticate provider mmol_l.", "sources": [{"locator": "$.data.recipe[10]",
    "source_key": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "source_raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "source_text_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    "accessed_at": "2026-10-28T06:09:03.134737Z", "exact_source_quote": "{\n                \"recipe_order\":
    11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q73", "subject": "Missing main preparation and source prose conflict", "local_fields":
    [], "decision": "evidence_only", "stage": "main medium controls", "interpretation":
    "Restore 30–45 min anoxic sparging, gas-specific sterile additions, vitamin filtration
    and pH 6.8. DSM PDF/API specify carbonate. TOGO table also says Na2CO3 but its
    comments say bicarbonate: retain this discrepancy, use the direct current DSM
    formulation rather than silently substituting bicarbonate. No autoclave temperature
    or duration is invented.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api946a", "reference": "https://mediadive.dsmz.de/rest/medium/946a",
    "source_raw_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "source_text_sha256": "80e0675dd3fa664ebaa74f9cbfaead3f2b7a03a82b41ad1598f085b180ea4e8f",
    "accessed_at": "2026-10-28T06:09:03.134547Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients (except carbonate, yeast extract, vitamins and sulfide),
    then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Prior to inoculation add carbonate from a
    sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and yeast extract, vitamins and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas. Vitamins are sterilized by filtration. Adjust pH of complete
    medium to 6.8, if necessary.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.comments[2]", "source_key": "togoM2594", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2594", "source_raw_sha256":
    "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "source_text_sha256":
    "d0a97de7dd51ab2e7159781d9014d92da297a66c31cec46209a145aee5485657", "accessed_at":
    "2026-10-28T06:09:03.134627Z", "exact_source_quote": "{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Prior to inoculation add bicarbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and yeast extract,
    vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2
    gas.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q74", "subject": "Separate collection strain prescription", "local_fields": [],
    "decision": "evidence_only", "stage": "source-specific variant only", "interpretation":
    "DSM 21940 prescription adds 1.50 g/L nitrate after autoclaving from an anoxic
    stock; retain only for that explicit variant. These are source-prescribed rates,
    not an experimental growth observation or the base recipe.", "sources": [{"locator":
    "extracted-text lines 23-24", "source_key": "dsmz946a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium946a.pdf",
    "source_raw_sha256": "ae69365cd94153a8ccdeaf42c5363d8151612172a80bec9ac471f375572c5752",
    "source_text_sha256": "314eda206bd204c9e4760a963381b77b85159b021daa08279fe5b266f592f0fe",
    "accessed_at": "2026-10-28T06:09:03.134228Z", "exact_source_quote": "For DSM 21940:
    Supplement medium after autoclaving with 1.50 g/l NaNO3 added from a\nsterile
    anoxic stock solution.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q75", "subject": "Separate collection strain prescription", "local_fields":
    [], "decision": "evidence_only", "stage": "source-specific variant only", "interpretation":
    "DSM 101605 prescription reduces yeast extract to 0.10 g/L and adds 2.00 g/L sodium
    acetate and 1.00 g/L nitrate after autoclaving from anoxic stocks; retain only
    for that explicit variant. These are source-prescribed rates, not an experimental
    growth observation or the base recipe.", "sources": [{"locator": "extracted-text
    lines 1-1", "source_key": "dsmz946a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium946a.pdf",
    "source_raw_sha256": "ae69365cd94153a8ccdeaf42c5363d8151612172a80bec9ac471f375572c5752",
    "source_text_sha256": "314eda206bd204c9e4760a963381b77b85159b021daa08279fe5b266f592f0fe",
    "accessed_at": "2026-10-28T06:09:03.134228Z", "exact_source_quote": "", "quote_representation":
    "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch058/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml: primary 38/41, secondary
    35/41; data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml: primary
    38/41, secondary 35/41. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. Zero numeric
    legacy MediaIngredientMech identifiers occur in the full selected documents; NNNNNN
    is a historical placeholder, not an ID. Complex commercial/product components
    are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - grounding
- assessment_id: a6
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - local0
- assessment_id: a7
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:009161
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009161-stock-flattening-units-and-cross-stock-sums
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Three stock recipes are flattened and their units are corrupted
  description: 'The record combines three stock preparations with the main batch:
    water and shared salts are summed across stages, all stock constituents become
    direct ingredients, 14 mg inputs retain their numbers as g/L, liquid doses become
    g/L, and variable gas/titrant rows lose their procedural context. Ordinary main
    gram inputs also lack a verified final-litre basis. Complete per-field decisions
    distinguish supported stock rates from mass and volume errors.'
  target_ids:
  - CultureMech:009161
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsmz946a
  - api946a
  - togoM2594
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-009161-hydrate-primary-secondary-disagreement
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and magnesium secondary mapping remain inconsistent
  description: NiCl2 hexahydrate is linked to anhydrous CHEBI:34887 in both selected
    primary/secondary slots and standalone mineral chebi_term. OLS candidate CHEBI:53542
    explicitly supplies the hexahydrate. MgSO4 heptahydrate primary CHEBI:31795 is
    correct but selected secondary CHEBI:32599 remains anhydrous/generic. Preserve
    correct forms and values; provider mmol_l values are not used to recertify hydrates.
  target_ids:
  - CultureMech:009161
  field_paths:
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  - ingredients[10].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml::composition[12].chebi_term
  evidence_ids:
  - grounding
  - chebi34887
  - chebi53542
  - chebi31795
  - chebi32599
  rule_id: supplied-form-primary-secondary-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml
    role: scoped mineral stock dependency; composition only
- finding_id: f3
  issue_key: culturemech-009161-missing-stage-specific-preparation-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation, pH and claim-scoped evidence are missing
  description: The selected layers omit pH 6.8, the complete anoxic preparation and
    scoped supporting evidence. TOGO bicarbonate prose conflicts with its carbonate
    table and direct DSM source, so a blind comment import would perpetuate a source
    conflict.
  target_ids:
  - CultureMech:009161
  field_paths:
  - preparation_steps
  - ph_value
  - evidence
  evidence_ids:
  - dsmz946a
  - api946a
  - togoM2594
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Rebuild the maintained TOGO owner with separate seawater, mineral and
    vitamin stocks and absolute source doses/water. Correct mg conversions, undo cross-stock
    sums and retain batch-versus-final-volume uncertainty; preserve all source forms
    and correct standalone stock repairs.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009161
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Resolve exact supplied hydrates and synchronize only the incorrect
    asserted slots using verified mappings; preserve the already correct magnesium
    primary and source masses.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009161
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml
    role: scoped mineral stock dependency; composition only
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Add the verified main and stock preparation with exact stage-scoped
    root evidence; explicitly document the TOGO prose discrepancy. Preserve the source
    distinction between base medium and named-strain prescriptions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009161
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- No measured final medium or stock volume is inferred from listed water. Provider-declared
  stock rates are distinguished from final-medium concentrations and unverified mmol
  values.
- DSM named-strain prescriptions are not growth observations and are not silently
  applied to the base recipe.
- Current source bytes do not recreate historical access times or execution; unrelated
  standalone parent recipes are outside the receiving-medium scope.
- Standalone solution5980 also cites an older medium161 raw capture; that whole payload
  was not re-fetched or authenticated. Its stock table is independently supported
  by current solution5980 and DSM946a; the separate parent formulation does not transfer.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
