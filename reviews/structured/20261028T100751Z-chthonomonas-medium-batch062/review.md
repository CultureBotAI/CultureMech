# Scientific review of chthonomonas_medium

- Review: 20261028T100751Z-chthonomonas-medium-batch062
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:29:43.990561Z
- Finished UTC: 2026-10-28T10:07:51.445652Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The medium identity and source batch inputs are recoverable, but stock flattening, mass/volume errors, incompatible same-name stock links and omitted preparation prevent faithful representation. Existing owner water repair and 18 authenticated dependency claims are retained and credited.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch062 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008921 | data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml | generated | chthonomonas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008921 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:008921 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:008921 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:008921 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact primary and stock identities

identity: concern. Targets: CultureMech:008921.

TOGO M2334 explicitly names DSM 1291. Main identity is secure; same-name linked stocks 5191 and 4611 are not compositionally equivalent to embedded 1474 and 1038. Both independent dependency evidence sets are preserved.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:008921.

Two exact selected historical reports record zero source checks and are derivative only. The owner equal-water-sum repair is credited; generated target remains stale. All 18 attached dependency claims have exact current raw digest and literal quote matches, with receiving-medium equivalence explicitly excluded. Current conservative merging preserves scientific fields and rejects incompatible formulations. The inspected TOGO importer, solution migrator and duplicate/default writers are described separately by exact file and function; current behavior does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:008921.

All 52 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008921", "selected_concentration_field_count": 52, "selected_concentration_fields_covered": 52, "decisions": [{"decision_id": "q1", "subject": "Main water versus collapsed stock waters", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3000.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1000.0", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "main water and two separately prepared stock solvents", "interpretation": "The source has three separate 1000 ml water rows, one per recipe section. Generated 3000 G_PER_L sums them and changes volume to mass. The owner correctly collapsed the old numerical sum to 1000, but still asserts G_PER_L and omits the stock-water separation. Preserve absolute water inputs without density or final-volume inference.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.components[1].items[0]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.components[2].items[0]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus unresolved per-litre basis", "interpretation": "The same digits are supported as gram inputs in the primary and TOGO and as declared API g_l values. However API volume is 1002 ml while its g_l values retain the gram numerals, and the primary lists 1000 ml water plus additions without explicit final make-up. Preserve the input mass; neither divide by 1002 nor certify G_PER_L without a source basis. This is unresolved normalization, not evidence that the batch mass itself is wrong.", "sources": [{"locator": "$.components[0].items[1]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.45", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.45", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus unresolved per-litre basis", "interpretation": "The same digits are supported as gram inputs in the primary and TOGO and as declared API g_l values. However API volume is 1002 ml while its g_l values retain the gram numerals, and the primary lists 1000 ml water plus additions without explicit final make-up. Preserve the input mass; neither divide by 1002 nor certify G_PER_L without a source basis. This is unresolved normalization, not evidence that the batch mass itself is wrong.", "sources": [{"locator": "$.components[0].items[2]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.45,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.45,\n                        \"mmol_l\": 2.58359,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus unresolved per-litre basis", "interpretation": "The same digits are supported as gram inputs in the primary and TOGO and as declared API g_l values. However API volume is 1002 ml while its g_l values retain the gram numerals, and the primary lists 1000 ml water plus additions without explicit final make-up. Preserve the input mass; neither divide by 1002 nor certify G_PER_L without a source basis. This is unresolved normalization, not evidence that the batch mass itself is wrong.", "sources": [{"locator": "$.components[0].items[3]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"MgCl2 x 6 H2O\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.91877,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "4", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus unresolved per-litre basis", "interpretation": "The same digits are supported as gram inputs in the primary and TOGO and as declared API g_l values. However API volume is 1002 ml while its g_l values retain the gram numerals, and the primary lists 1000 ml water plus additions without explicit final make-up. Preserve the input mass; neither divide by 1002 nor certify G_PER_L without a source basis. This is unresolved normalization, not evidence that the batch mass itself is wrong.", "sources": [{"locator": "$.components[0].items[4]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"(NH4)2SO4\",\n          \"volume\": 4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\": \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 30.2709,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Gellan Gum (Phytagel)", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus unresolved per-litre basis", "interpretation": "The same digits are supported as gram inputs in the primary and TOGO and as declared API g_l values. However API volume is 1002 ml while its g_l values retain the gram numerals, and the primary lists 1000 ml water plus additions without explicit final make-up. Preserve the input mass; neither divide by 1002 nor certify G_PER_L without a source basis. This is unresolved normalization, not evidence that the batch mass itself is wrong.", "sources": [{"locator": "$.components[0].items[6]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Gellan Gum (Phytagel)\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001250\",\n          \"gmo_id\": \"GMO_001250\",\n          \"label\": \"Gellan gum\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\": \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Gellan Gum\",\n                        \"compound_id\": 1158,\n                        \"attribute\": \"Phytagel\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "36", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "36", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 36 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[1]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "6", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 6 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[2]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 100 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[3]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"MnCl2 x 4 H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "190", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "190", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 190 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[4]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"CoCl2 x 6 H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "24", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "24", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 24 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[5]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"NiCl2 x 6 H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 2 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[6]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"CuCl2 x 2 H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "70", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "70", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 70 mg in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[7]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 1.5 g in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[8]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"FeCl2 x 4 H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened into main medium", "interpretation": "The source specifies 5.2 g in the named SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied form and convert mg to g only within that stock if representing G_PER_L. The current main placement is wrong even for gram rows whose digits match stock strength; the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator": "$.components[1].items[9]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Na2-EDTA x 2 H2O\",\n          \"volume\": 5.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001148\",\n          \"gmo_id\": \"GMO_001148\",\n          \"label\": \"Disodium EDTA dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "conflict", "stage": "SL11 titrant stock versus main ingredient", "interpretation": "VARIABLE does not invent a dose, but this sodium hydroxide belongs to SL11 preparation as a 2 N titrant to pH 7 before final pH 6 and make-up. It is not a quantified main-medium ingredient. Retain the absent dose as unresolved while preserving the source titrant strength and stage.", "sources": [{"locator": "$.components[1].items[10]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"NaOH\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].steps[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "80", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "80", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 80 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[1]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 80,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 100 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[2]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[4]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "300", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "300", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 300 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[3]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Pyridoxine hydrochloride\",\n          \"volume\": 300,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[5]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 100 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[4]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "200", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "200", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 200 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[5]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "200", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "200", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 200 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[6]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Thiamine-HCl x 2 H2O\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001278\",\n          \"gmo_id\": \"GMO_001278\",\n          \"label\": \"Thiamine hydrochloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[6]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "D(+)-Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component", "interpretation": "The source gives 20 mg in a separately prepared stock with 1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs and source-declared stock basis separately from the 1 ml receiving dose; do not infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[7]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"D(+)-Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001939\",\n          \"gmo_id\": \"GMO_001939\",\n          \"label\": \"D(+)-Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "CaCl2 x 2 H2O solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "0.15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "0.15", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "source liquid addition", "interpretation": "The source gives an absolute volume addition in ml, not G_PER_L. Both primary PDF and API literally print 0.15 ml CaCl2 dihydrate, while TOGO calls it a solution. Its stock strength is not supplied; do not silently change ml to g or invent calcium concentration.", "sources": [{"locator": "$.components[0].items[5]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"CaCl2 x 2 H2O solution\",\n          \"volume\": 0.15,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001228\",\n          \"gmo_id\": \"GMO_001228\",\n          \"label\": \"Calcium chloride dihydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Trace element solution SL-11", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "source liquid addition", "interpretation": "The source gives an absolute volume addition in ml, not G_PER_L. The current linked stock is not the stock printed in DSM 1291: API 1291 explicitly identifies 1474 for SL11 and 1038 for seven vitamins. Keep dose separate from stock identity and the unresolved final-litre denominator.", "sources": [{"locator": "$.components[0].items[7]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Trace element solution SL-11\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2334\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "Seven vitamins solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "source liquid addition", "interpretation": "The source gives an absolute volume addition in ml, not G_PER_L. The current linked stock is not the stock printed in DSM 1291: API 1291 explicitly identifies 1474 for SL11 and 1038 for seven vitamins. Keep dose separate from stock identity and the unresolved final-litre denominator.", "sources": [{"locator": "$.components[0].items[8]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\": \"Seven vitamins solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2334\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "solution5191 Na2-EDTA", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[0].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\": \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "solution5191 FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[1].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "solution5191 ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[2].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "solution5191 MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[3].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "solution5191 H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[4].concentration", "original": {"value": "6", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "solution5191 CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[5].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "solution5191 CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[6].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[6]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "solution5191 NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[7].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[7]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "solution5191 Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[8].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[8]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "solution5191 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "composition[9].concentration", "original": {"value": "1", "unit": "L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[9]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "solution5191 placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "legacy schema placeholder", "interpretation": "The source already supplies the full composition. The extra See source for composition VARIABLE row and incomplete_composition flag are inherited structural placeholders, not additional chemical ingredients or evidence that the stock table is absent.", "sources": [{"locator": "$.data", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n        \"id\": 5191,\n        \"name\": \"Trace element solution SL-11\",\n        \"volume\": 1000,\n        \"recipe\": [\n            {\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\": \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\": null,\n                \"step\": \"Adjust pH to 6.0.\"\n            }\n        ],\n        \"equipment\": []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "solution4611 Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[0].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.0368895,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "solution4611 p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[1].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "solution4611 D-(+)-biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[2].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"D-(+)-biotin\",\n                \"compound_id\": 1359,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0409316,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "solution4611 Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[3].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.812282,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "solution4611 Calcium pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[4].concentration", "original": {"value": "0.025", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Calcium pantothenate\",\n                \"compound_id\": 518,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.025,\n                \"mmol_l\": 0.0524659,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "solution4611 Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[5].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.25,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "solution4611 Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[6].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[6]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\": 77,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "solution4611 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "composition[7].concentration", "original": {"value": "0.2", "unit": "L"}}], "decision": "verified", "stage": "separately authenticated stock dependency", "interpretation": "Existing attached exact snippets and cited raw hash match the current response. The stored provider concentration or corrected absolute water input is credited within this stock only. It does not establish compatibility with the selected medium; preserve this evidence and do not rewrite the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[7]", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q46", "subject": "solution4611 placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "legacy schema placeholder", "interpretation": "The source already supplies the full composition. The extra See source for composition VARIABLE row and incomplete_composition flag are inherited structural placeholders, not additional chemical ingredients or evidence that the stock table is absent.", "sources": [{"locator": "$.data", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n        \"id\": 4611,\n        \"name\": \"Seven vitamins solution\",\n        \"volume\": 200,\n        \"recipe\": [\n            {\n                \"recipe_order\": 1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.0368895,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"D-(+)-biotin\",\n                \"compound_id\": 1359,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0409316,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.812282,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\": \"Calcium pantothenate\",\n                \"compound_id\": 518,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.025,\n                \"mmol_l\": 0.0524659,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.25,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\": \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\": 77,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [],\n        \"equipment\": []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject": "SL11 incompatible dependency identity", "local_fields": [], "decision": "evidence_only", "stage": "source-only stock identity reconciliation", "interpretation": "Selected DSM 1291 uses dihydrate EDTA and 6 mg boric acid per stock batch, with final make-up to 1000 ml. Linked 5191 instead says Na2-EDTA and 6 g boric acid, with only pH 6 instruction. Both raw sources are authentic; the selected link must be reconciled rather than treating the name as proof of equality.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.recipe[0]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\": \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.recipe[4]", "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q48", "subject": "Seven-vitamin incompatible dependency", "local_fields": [], "decision": "evidence_only", "stage": "source-only stock identity reconciliation", "interpretation": "All seven component concentrations in linked 4611 differ from the embedded 1038 stock, and its water input is 200 ml rather than 1000 ml. The link cannot be accepted by name alone; retain both separately authenticated formulations.", "sources": [{"locator": "$.data.solutions[2]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                \"id\": 1038,\n                \"name\": \"Seven vitamins solution\",\n                \"volume\": 1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ]\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data", "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n        \"id\": 4611,\n        \"name\": \"Seven vitamins solution\",\n        \"volume\": 200,\n        \"recipe\": [\n            {\n                \"recipe_order\": 1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.0368895,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"D-(+)-biotin\",\n                \"compound_id\": 1359,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0409316,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.812282,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\": \"Calcium pantothenate\",\n                \"compound_id\": 518,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.025,\n                \"mmol_l\": 0.0524659,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.25,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\": \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\": 77,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [],\n        \"equipment\": []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject": "Main preparation and source controls", "local_fields": [], "decision": "evidence_only", "stage": "source-only main preparation", "interpretation": "Preserve gellan dissolution, pH 5.0–5.3, air atmosphere and 30% vessel fill. Magnesium chloride, yeast extract and vitamins are added as sterile stocks after autoclaving; vitamins are filtered. Shaking is a source suggestion, not an independently measured growth claim. These instructions are missing from both selected layers.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\": \"Add gellan gum and boil to dissolve. Then add the remaining ingredients (except magnesium chloride, yeast extract and vitamins), adjust the pH value to 5.0 to 5.3 and fill the medium under an air atmosphere into tubes of the Hungate type or similar vials up to 30% their volume. After autoclaving add magnesium chloride, yeast extract and vitamins from steril stock solutions. Vitamins should be sterilized by filtration.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\": \"Note: Incubation with shaking may improve cell yield.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject": "Stock preparation controls", "local_fields": [], "decision": "evidence_only", "stage": "source-only SL11 preparation", "interpretation": "Retain 800 ml initial water,2 N NaOH to pH 7, order of ferrous chloride addition, final pH 6 and make-up to 1000 ml in the SL11 subsection. This explicit final-volume instruction does not apply to the main medium or the vitamin stock.", "sources": [{"locator": "$.data.solutions[1].steps[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch062/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:008921.

data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml: primary 21/23, secondary 21/23; data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml: primary 21/23, secondary 21/23. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:008921.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:008921.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Stock inputs and liquid additions are represented as main-medium mass concentrations

major / open / confirmed; issue key: culturemech-008921-stock-units-and-water-staleness.

Milligram stock rows retain their numerals as G_PER_L, gram stock rows remain flat, and three liquid additions have mass units. Generated water still sums three independent solvent rows; the owner numerical repair is credited but its unit and stage remain wrong. Five ordinary main masses have correct batch digits but unresolved per-litre basis.

### f2: The named stock links point to different formulations

major / open / confirmed; issue key: culturemech-008921-incompatible-same-name-stock-links.

SL11 link 5191 differs in EDTA form, boric acid 6 g versus 6 mg and preparation. Seven-vitamin link 4611 differs in all seven component strengths. Their 18 attached claims match their own current raw bytes and must not be overwritten simply to fit DSM 1291.

### f3: Source preparation and quantitative evidence are missing

major / open / confirmed; issue key: culturemech-008921-missing-preparation-and-evidence.

Both layers lack pH 5.0–5.3, staged sterilization and addition instructions, air and fill controls, and claim-level evidence. Current TOGO writer can preserve nested sections, ml/mg units and comments; the historical flattened output does not prove that its current implementation still loses them.

### f4: Nickel hexahydrate is linked to anhydrous nickel dichloride

major / open / confirmed; issue key: culturemech-008921-nickel-hydrate-grounding.

Selected nickel rows name the hexahydrate but both term slots point to CHEBI:34887. The same form mismatch occurs in the separately inspected 5191 dependency chebi_term. Other supplied hydrates are credited. Generic calcium pantothenate and D-biotin retain their exact source labels; no unsupported stereochemical replacement is proposed.

### f5: Stock placeholders obscure populated source tables

minor / open / confirmed; issue key: culturemech-008921-placeholder-stock-metadata.

Both linked stock records contain a full composition but also retain See source for composition and incomplete_composition placeholders. The selected solutions have meaningful preferred terms alongside Unknown solution names. These are structural remnants, not evidence that the authenticated stock recipes are absent.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the main recipe and two stock sections using exact source units, preserve the existing numerical duplicate repair, keep absolute liquid additions and document denominator limits. Do not invent calcium-stock strength or convert listed water into final volume.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Reconcile the receiving record links against exact embedded stock 1474/1038 identities and complete compositions. Preserve linked 5191/4611 as separate source formulations and retain their authenticated evidence; no automatic whole-stock substitution.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the source-supported preparation to its correct main or stock stage and attach scoped evidence. Preserve unresolved calcium strength and physical-state interpretation; gellan content alone is not an explicit source state designation. Regenerate from repaired maintained inputs.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve the exact nickel hydrate mapping independently in the selected owner and dependency, preserving all authentic quantities and evidence. If no verified mapping is available retain a precise source form with explicit unresolved grounding.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

After preserving the actual stock identities, review placeholder names, rows and flags against the complete composition and append a verified cleanup event. Do not remove or relabel historical evidence.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch062/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch062/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch062/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch062/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz1291 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1291.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api1291 | https://mediadive.dsmz.de/rest/medium/1291; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| togoM2334 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| solution5191 | https://mediadive.dsmz.de/rest/solution/5191; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| solution4611 | https://mediadive.dsmz.de/rest/solution/4611; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O']; mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:64734 = EDTA disodium salt (anhydrous); definition ['An organic sodium salt that is the anhydrous form of the disodium salt of ethylenediaminetetraacetic acid (EDTA).']; formula ['C10H14N2O8.2Na']; mass ['336.208']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na']; mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch062/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHTHONOMONAS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch062/record05/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer37 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace legacy secondary MIM links or authenticate quantities. |
| writer38 | scripts/cleanup_media_quality.py; relevant functions named in summary | context_only | Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical quantities and flags conflicting quantities rather than summing them. Persisted old duplicate sums require independent source review; they do not establish that this current implementation still sums unequal stages. |
| writer39 | scripts/migrate_solutions_from_ingredients.py; relevant functions named in summary | context_only | Current _resolve_solution and _migrate_media_file identify stock references and move descriptors into solutions while preserving their stored concentration. Copying a malformed G_PER_L value does not validate its source dose or hydrate, and a current named reference does not prove stock equivalence. |
| writer40 | scripts/repair_merged_duplicates.py; relevant functions named in summary | context_only | Full repair_ingredient/repair_record read: only identical merged parts are collapsed; unequal groups remain for source review. Any current repaired equal duplicate is credited separately; collapsing a sum does not authenticate units or stages. Current code is not proof of the historical run. |
| writer41 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer42 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer43 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer44 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| writer45 | src/culturemech/validation/schema_defaulter.py; relevant functions named in summary | context_only | Full apply_defaults/_fix_ingredient/_fix_solution read. The defaulter inserts VARIABLE concentrations and Unknown solution names to satisfy structure. These defaults are not evidence for a source dose, composition or final volume; copied historical default events remain contextual. |
| dep46 | data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep47 | data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| quantity-inventory | REVIEW_WORK/batch062/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Calcium dihydrate is printed as 0.15 ml with no strength; neither a mass replacement nor a final calcium concentration is established.
- API 1291 declares 1002 ml yet keeps main g_l values equal to gram inputs. The primary provides water inputs rather than explicit final medium volume. No unsupported normalization is introduced.
- Generic source pantothenate does not independently select a stereoisomer. Current MIM joins and exact OLS labels are separate from supplied-form equivalence; all selected numeric legacy MIM counts are zero.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T100751Z-chthonomonas-medium-batch062
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of chthonomonas_medium
started_at: '2026-10-28T09:29:43.990561Z'
finished_at: '2026-10-28T10:07:51.445652Z'
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
summary: The medium identity and source batch inputs are recoverable, but stock flattening,
  mass/volume errors, incompatible same-name stock links and omitted preparation prevent
  faithful representation. Existing owner water repair and 18 authenticated dependency
  claims are retained and credited.
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
  - path: data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml
    sha256: 61245d8c4109eb281ecfcc664e64a4a5c0cc2d085ad9427b4fb8b1a8b52e23a4
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    sha256: 37ffd7b8c130ffae9cd73bda4bc3e3c3ee432ccf94c3724cd4469a6f36321ea2
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml
    sha256: 18bae91fce8a0cdccc3fc6a2d67c3bc915498198c11f03e36b16ef5867c700f0
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    sha256: 815892ebecf9cc2d1aa27e305c6ff73f6ab4183707b143e17f7f7e5c7e09ff0e
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHTHONOMONAS_MEDIUM.md
    sha256: 1729529df7beb8145da213330c6fb52ae2f57c9949a7952aeec64cb3afe52608
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.md
    sha256: 91aa3a87c719b14278579b2a9e0bdacdb15eb546a66e5cd672d250c9639552c9
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch062 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008921
targets:
- target_id: CultureMech:008921
  path: data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml
  label: chthonomonas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008921
  command: just validate-schema data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008921
  command: just validate-strict data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch062/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008921
  command: just validate-terms data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:008921
  command: just validate-references data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T09:40:29.395182Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 61245d8c4109eb281ecfcc664e64a4a5c0cc2d085ad9427b4fb8b1a8b52e23a4
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T09:40:29.395357Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 37ffd7b8c130ffae9cd73bda4bc3e3c3ee432ccf94c3724cd4469a6f36321ea2
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:45.010102Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: b448a9d82c052685d33e563957604451beba7d7efa32fdf84289cac59852ea78
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:45.969078Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 32a63a3db93e2496e486fe3c859ad3231bb0e54935aa97dbc42b956f5516a578
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:46.969580Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 65ef128c473062d6abf452e8bba3461f34c3ac79bddc7dd9ed8e22723d441223
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch062/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:47.684488Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 0d7ecb51ce082dbb77e1cd39add7bc2967799f5eed9873416799bb12f022bdce
- evidence_id: dsmz1291
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1291.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:22.181282Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 57711f54b6294a83522dc37b9810329e76d455d39555bc436b1c97a4827b6a65
- evidence_id: api1291
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1291
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:22.072396Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9
- evidence_id: togoM2334
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:22.000487Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: 2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e
- evidence_id: solution5191
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5191
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:21.988198Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0
- evidence_id: solution4611
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4611
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:21.986065Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:19.397533Z'
  support: supports
  summary: OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition
    ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula
    ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.742590Z'
  support: supports
  summary: OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition
    ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O'];
    mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:19.130156Z'
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
  accessed_at: '2026-10-28T09:30:21.409645Z'
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
  accessed_at: '2026-10-28T09:30:21.398530Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.385686Z'
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
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.350111Z'
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
  accessed_at: '2026-10-28T09:30:21.196677Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.904169Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.775577Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:17.947089Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.775488Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.726940Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.691698Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.519639Z'
  support: supports
  summary: OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic
    sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia.
    A high-melting (decomposes above 280°C) white solid which is very soluble in water
    (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as
    a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.211234Z'
  support: supports
  summary: OLS current exact CHEBI:64734 = EDTA disodium salt (anhydrous); definition
    ['An organic sodium salt that is the anhydrous form of the disodium salt of ethylenediaminetetraacetic
    acid (EDTA).']; formula ['C10H14N2O8.2Na']; mass ['336.208']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 95b7557b1867dcce37a69714dbad0a6a6a6c11c66dde39c6793a2307a7fb0e1c
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.171246Z'
  support: supports
  summary: OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition
    ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na'];
    mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 5432921ff4fea3479e93ce6392a2654e3d5560255beb96022793102e776d9647
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:17.036791Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.118004Z'
  support: supports
  summary: OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O'];
    mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.049072Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:15.999491Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.009797Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch062/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T09:40:29.401278Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: fee3f48aaa5d742597e2426dc3150c5d38555eb9160653db87498278775d3605
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:40:29.401587Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 91aa3a87c719b14278579b2a9e0bdacdb15eb546a66e5cd672d250c9639552c9
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHTHONOMONAS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:40:29.401610Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 1729529df7beb8145da213330c6fb52ae2f57c9949a7952aeec64cb3afe52608
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch062/record05/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T09:40:29.401628Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: b73e22233ba322f4b8e12374b5e132e69e6aa11e9c99ca0786ecc3acae21a9e1
- evidence_id: writer37
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401648Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace legacy secondary MIM links or
    authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer38
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401667Z'
  support: context_only
  summary: Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical
    quantities and flags conflicting quantities rather than summing them. Persisted
    old duplicate sums require independent source review; they do not establish that
    this current implementation still sums unequal stages.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer39
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401687Z'
  support: context_only
  summary: Current _resolve_solution and _migrate_media_file identify stock references
    and move descriptors into solutions while preserving their stored concentration.
    Copying a malformed G_PER_L value does not validate its source dose or hydrate,
    and a current named reference does not prove stock equivalence.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer40
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401703Z'
  support: context_only
  summary: 'Full repair_ingredient/repair_record read: only identical merged parts
    are collapsed; unequal groups remain for source review. Any current repaired equal
    duplicate is credited separately; collapsing a sum does not authenticate units
    or stages. Current code is not proof of the historical run.'
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer41
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401731Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer42
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401748Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer43
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401766Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer44
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401785Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer45
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:40:29.401803Z'
  support: context_only
  summary: Full apply_defaults/_fix_ingredient/_fix_solution read. The defaulter inserts
    VARIABLE concentrations and Unknown solution names to satisfy structure. These
    defaults are not evidence for a source dose, composition or final volume; copied
    historical default events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: dep46
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T09:40:29.401907Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 18bae91fce8a0cdccc3fc6a2d67c3bc915498198c11f03e36b16ef5867c700f0
- evidence_id: dep47
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T09:40:29.401908Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 815892ebecf9cc2d1aa27e305c6ff73f6ab4183707b143e17f7f7e5c7e09ff0e
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch062/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T09:40:29.425559Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: bd2493caa02e3610c30b03819dea74e05b2ae7bbaca6bbb6fca2de9a9e253255
assessments:
- assessment_id: a1
  area: identity
  topic: Exact primary and stock identities
  outcome: concern
  summary: TOGO M2334 explicitly names DSM 1291. Main identity is secure; same-name
    linked stocks 5191 and 4611 are not compositionally equivalent to embedded 1474
    and 1038. Both independent dependency evidence sets are preserved.
  target_ids:
  - CultureMech:008921
  evidence_ids:
  - togoM2334
  - dsmz1291
  - api1291
  - solution5191
  - solution4611
- assessment_id: a2
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Two exact selected historical reports record zero source checks and are
    derivative only. The owner equal-water-sum repair is credited; generated target
    remains stale. All 18 attached dependency claims have exact current raw digest
    and literal quote matches, with receiving-medium equivalence explicitly excluded.
    Current conservative merging preserves scientific fields and rejects incompatible
    formulations. The inspected TOGO importer, solution migrator and duplicate/default
    writers are described separately by exact file and function; current behavior
    does not prove historical execution.
  target_ids:
  - CultureMech:008921
  evidence_ids:
  - history-auth
  - writer37
  - writer38
  - writer39
  - writer40
  - writer41
  - writer42
  - writer43
  - writer44
  - writer45
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 52 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:008921
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008921",
    "selected_concentration_field_count": 52, "selected_concentration_fields_covered":
    52, "decisions": [{"decision_id": "q1", "subject": "Main water versus collapsed
    stock waters", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3000.0",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1000.0",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "main water and two separately
    prepared stock solvents", "interpretation": "The source has three separate 1000
    ml water rows, one per recipe section. Generated 3000 G_PER_L sums them and changes
    volume to mass. The owner correctly collapsed the old numerical sum to 1000, but
    still asserts G_PER_L and omits the stock-water separation. Preserve absolute
    water inputs without density or final-volume inference.", "sources": [{"locator":
    "$.components[0].items[0]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.components[1].items[0]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.components[2].items[0]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus
    unresolved per-litre basis", "interpretation": "The same digits are supported
    as gram inputs in the primary and TOGO and as declared API g_l values. However
    API volume is 1002 ml while its g_l values retain the gram numerals, and the primary
    lists 1000 ml water plus additions without explicit final make-up. Preserve the
    input mass; neither divide by 1002 nor certify G_PER_L without a source basis.
    This is unresolved normalization, not evidence that the batch mass itself is wrong.",
    "sources": [{"locator": "$.components[0].items[1]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q3", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.45", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.45", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus
    unresolved per-litre basis", "interpretation": "The same digits are supported
    as gram inputs in the primary and TOGO and as declared API g_l values. However
    API volume is 1002 ml while its g_l values retain the gram numerals, and the primary
    lists 1000 ml water plus additions without explicit final make-up. Preserve the
    input mass; neither divide by 1002 nor certify G_PER_L without a source basis.
    This is unresolved normalization, not evidence that the batch mass itself is wrong.",
    "sources": [{"locator": "$.components[0].items[2]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.45,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.45,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.45,\n                        \"mmol_l\":
    2.58359,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "MgCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus
    unresolved per-litre basis", "interpretation": "The same digits are supported
    as gram inputs in the primary and TOGO and as declared API g_l values. However
    API volume is 1002 ml while its g_l values retain the gram numerals, and the primary
    lists 1000 ml water plus additions without explicit final make-up. Preserve the
    input mass; neither divide by 1002 nor certify G_PER_L without a source basis.
    This is unresolved normalization, not evidence that the batch mass itself is wrong.",
    "sources": [{"locator": "$.components[0].items[3]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgCl2 x 6 H2O\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.91877,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "(NH4)2SO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "4", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus
    unresolved per-litre basis", "interpretation": "The same digits are supported
    as gram inputs in the primary and TOGO and as declared API g_l values. However
    API volume is 1002 ml while its g_l values retain the gram numerals, and the primary
    lists 1000 ml water plus additions without explicit final make-up. Preserve the
    input mass; neither divide by 1002 nor certify G_PER_L without a source basis.
    This is unresolved normalization, not evidence that the batch mass itself is wrong.",
    "sources": [{"locator": "$.components[0].items[4]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\":
    \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\":
    30.2709,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "Gellan Gum (Phytagel)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "ordinary main batch mass versus
    unresolved per-litre basis", "interpretation": "The same digits are supported
    as gram inputs in the primary and TOGO and as declared API g_l values. However
    API volume is 1002 ml while its g_l values retain the gram numerals, and the primary
    lists 1000 ml water plus additions without explicit final make-up. Preserve the
    input mass; neither divide by 1002 nor certify G_PER_L without a source basis.
    This is unresolved normalization, not evidence that the batch mass itself is wrong.",
    "sources": [{"locator": "$.components[0].items[6]", "source_key": "togoM2334",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Gellan Gum (Phytagel)\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001250\",\n          \"gmo_id\": \"GMO_001250\",\n          \"label\":
    \"Gellan gum\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\":
    \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Gellan Gum\",\n                        \"compound_id\":
    1158,\n                        \"attribute\": \"Phytagel\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "36", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "36", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 36 mg in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[1]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2MoO4 x 2 H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "6", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 6 mg in the named SL11
    stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied
    form and convert mg to g only within that stock if representing G_PER_L. The current
    main placement is wrong even for gram rows whose digits match stock strength;
    the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator":
    "$.components[1].items[2]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\":
    \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 100 mg in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[3]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"MnCl2 x 4 H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "original": {"value": "190", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "190", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 190 mg in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[4]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"CoCl2 x 6 H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "original": {"value": "24", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "24", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 24 mg in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[5]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"NiCl2 x 6 H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\":
    \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 2 mg in the named SL11
    stock, whose preparation explicitly brings volume to 1000 ml. Preserve this supplied
    form and convert mg to g only within that stock if representing G_PER_L. The current
    main placement is wrong even for gram rows whose digits match stock strength;
    the stock is separately dosed 1 ml per listed medium batch.", "sources": [{"locator":
    "$.components[1].items[6]", "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"CuCl2 x 2 H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\":
    \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "70", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "70", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 70 mg in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[7]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\":
    \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 1.5 g in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[8]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"FeCl2 x 4 H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\":
    \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2-EDTA x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL11 stock component flattened
    into main medium", "interpretation": "The source specifies 5.2 g in the named
    SL11 stock, whose preparation explicitly brings volume to 1000 ml. Preserve this
    supplied form and convert mg to g only within that stock if representing G_PER_L.
    The current main placement is wrong even for gram rows whose digits match stock
    strength; the stock is separately dosed 1 ml per listed medium batch.", "sources":
    [{"locator": "$.components[1].items[9]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2-EDTA x 2 H2O\",\n          \"volume\": 5.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001148\",\n          \"gmo_id\": \"GMO_001148\",\n          \"label\":
    \"Disodium EDTA dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "NaOH", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "variable", "unit": "VARIABLE"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "conflict", "stage": "SL11 titrant stock versus
    main ingredient", "interpretation": "VARIABLE does not invent a dose, but this
    sodium hydroxide belongs to SL11 preparation as a 2 N titrant to pH 7 before final
    pH 6 and make-up. It is not a quantified main-medium ingredient. Retain the absent
    dose as unresolved while preserving the source titrant strength and stage.", "sources":
    [{"locator": "$.components[1].items[10]", "source_key": "togoM2334", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334", "source_raw_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "source_text_sha256":
    "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e", "accessed_at":
    "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaOH\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"N\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\":
    \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].steps[0]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "80", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "80", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 80 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[1]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 80,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 100 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[2]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Calcium pantothenate\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\":
    \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[4]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "300", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "300", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 300 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[3]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Pyridoxine hydrochloride\",\n          \"volume\": 300,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\":
    \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[5]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 100 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[4]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "200", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 200 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[5]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[3]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "Thiamine-HCl x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 200 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[6]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Thiamine-HCl x 2 H2O\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001278\",\n          \"gmo_id\": \"GMO_001278\",\n          \"label\":
    \"Thiamine hydrochloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[6]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "D(+)-Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "seven-vitamin stock batch component",
    "interpretation": "The source gives 20 mg in a separately prepared stock with
    1000 ml listed water, not that numeral in G_PER_L of the medium. Preserve mg inputs
    and source-declared stock basis separately from the 1 ml receiving dose; do not
    infer measured final medium volume.", "sources": [{"locator": "$.components[2].items[7]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"D(+)-Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001939\",\n          \"gmo_id\": \"GMO_001939\",\n          \"label\":
    \"D(+)-Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[2]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "CaCl2 x 2 H2O solution",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "0.15", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "0.15", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "source liquid addition", "interpretation":
    "The source gives an absolute volume addition in ml, not G_PER_L. Both primary
    PDF and API literally print 0.15 ml CaCl2 dihydrate, while TOGO calls it a solution.
    Its stock strength is not supplied; do not silently change ml to g or invent calcium
    concentration.", "sources": [{"locator": "$.components[0].items[5]", "source_key":
    "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"CaCl2 x 2 H2O solution\",\n          \"volume\": 0.15,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001228\",\n          \"gmo_id\":
    \"GMO_001228\",\n          \"label\": \"Calcium chloride dihydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "api1291",
    "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Trace element solution
    SL-11", "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "source liquid addition", "interpretation":
    "The source gives an absolute volume addition in ml, not G_PER_L. The current
    linked stock is not the stock printed in DSM 1291: API 1291 explicitly identifies
    1474 for SL11 and 1038 for seven vitamins. Keep dose separate from stock identity
    and the unresolved final-litre denominator.", "sources": [{"locator": "$.components[0].items[7]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Trace element solution SL-11\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2334\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"},
    {"locator": "$.data.solutions[0].recipe[4]", "source_key": "api1291", "reference":
    "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "Seven vitamins solution",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "source liquid addition", "interpretation":
    "The source gives an absolute volume addition in ml, not G_PER_L. The current
    linked stock is not the stock printed in DSM 1291: API 1291 explicitly identifies
    1474 for SL11 and 1038 for seven vitamins. Keep dose separate from stock identity
    and the unresolved final-litre denominator.", "sources": [{"locator": "$.components[0].items[8]",
    "source_key": "togoM2334", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2334",
    "source_raw_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "source_text_sha256": "2fd7b6c9796bdb39805dd37d0710aa31e89b326fc66ddbfcaa5d1ffe8257177e",
    "accessed_at": "2026-10-28T09:30:22.000487Z", "exact_source_quote": "{\n          \"component_name\":
    \"Seven vitamins solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2334\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "solution5191 Na2-EDTA",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[0]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\":
    \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q28", "subject": "solution5191 FeCl2 x 4 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[1].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[1]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\":
    260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q29", "subject": "solution5191 ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[2]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\":
    64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q30", "subject": "solution5191 MnCl2 x 4 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[3]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q31", "subject": "solution5191 H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[4].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[4]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q32", "subject": "solution5191 CoCl2 x 6 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[5].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[5]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q33", "subject": "solution5191 CuCl2 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[6].concentration", "original": {"value": "0.002", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[6]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\":
    39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q34", "subject": "solution5191 NiCl2 x 6 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[7].concentration", "original": {"value": "0.024", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[7]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q35", "subject": "solution5191 Na2MoO4 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[8].concentration", "original": {"value": "0.036", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[8]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q36", "subject": "solution5191 Distilled water", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "composition[9].concentration", "original": {"value": "1", "unit":
    "L"}}], "decision": "verified", "stage": "separately authenticated stock dependency",
    "interpretation": "Existing attached exact snippets and cited raw hash match the
    current response. The stored provider concentration or corrected absolute water
    input is credited within this stock only. It does not establish compatibility
    with the selected medium; preserve this evidence and do not rewrite the separate
    stock merely to force a match.", "sources": [{"locator": "$.data.recipe[9]", "source_key":
    "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256":
    "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256":
    "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at":
    "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q37", "subject": "solution5191 placeholder", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "legacy schema placeholder",
    "interpretation": "The source already supplies the full composition. The extra
    See source for composition VARIABLE row and incomplete_composition flag are inherited
    structural placeholders, not additional chemical ingredients or evidence that
    the stock table is absent.", "sources": [{"locator": "$.data", "source_key": "solution5191",
    "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256":
    "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256":
    "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at":
    "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n        \"id\": 5191,\n        \"name\":
    \"Trace element solution SL-11\",\n        \"volume\": 1000,\n        \"recipe\":
    [\n            {\n                \"recipe_order\": 1,\n                \"compound\":
    \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\":
    \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\":
    \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\":
    \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\":
    \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\":
    \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\":
    \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 9,\n                \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 10,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\":
    null,\n                \"step\": \"Adjust pH to 6.0.\"\n            }\n        ],\n        \"equipment\":
    []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38",
    "subject": "solution4611 Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[0]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\":
    18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.0368895,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q39", "subject": "solution4611 p-Aminobenzoic acid", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[1].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[1]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\":
    47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q40", "subject": "solution4611 D-(+)-biotin", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[2]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"D-(+)-biotin\",\n                \"compound_id\":
    1359,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0409316,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q41", "subject": "solution4611 Nicotinic acid", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[3]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\":
    139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.812282,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q42", "subject": "solution4611 Calcium pantothenate", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[4].concentration", "original": {"value": "0.025", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[4]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"Calcium pantothenate\",\n                \"compound_id\":
    518,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.025,\n                \"mmol_l\": 0.0524659,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q43", "subject": "solution4611 Pyridoxine hydrochloride", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[5].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[5]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\":
    519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.25,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q44", "subject": "solution4611 Thiamine-HCl x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[6].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "separately authenticated stock
    dependency", "interpretation": "Existing attached exact snippets and cited raw
    hash match the current response. The stored provider concentration or corrected
    absolute water input is credited within this stock only. It does not establish
    compatibility with the selected medium; preserve this evidence and do not rewrite
    the separate stock merely to force a match.", "sources": [{"locator": "$.data.recipe[6]",
    "source_key": "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611",
    "source_raw_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "source_text_sha256": "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270",
    "accessed_at": "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\":
    77,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q45", "subject": "solution4611 Distilled water", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "composition[7].concentration", "original": {"value": "0.2", "unit":
    "L"}}], "decision": "verified", "stage": "separately authenticated stock dependency",
    "interpretation": "Existing attached exact snippets and cited raw hash match the
    current response. The stored provider concentration or corrected absolute water
    input is credited within this stock only. It does not establish compatibility
    with the selected medium; preserve this evidence and do not rewrite the separate
    stock merely to force a match.", "sources": [{"locator": "$.data.recipe[7]", "source_key":
    "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256":
    "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256":
    "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at":
    "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q46", "subject": "solution4611 placeholder", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "legacy schema placeholder",
    "interpretation": "The source already supplies the full composition. The extra
    See source for composition VARIABLE row and incomplete_composition flag are inherited
    structural placeholders, not additional chemical ingredients or evidence that
    the stock table is absent.", "sources": [{"locator": "$.data", "source_key": "solution4611",
    "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256":
    "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256":
    "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at":
    "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n        \"id\": 4611,\n        \"name\":
    \"Seven vitamins solution\",\n        \"volume\": 200,\n        \"recipe\": [\n            {\n                \"recipe_order\":
    1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\":
    18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.0368895,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\":
    \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"D-(+)-biotin\",\n                \"compound_id\": 1359,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0409316,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.812282,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\":
    \"Calcium pantothenate\",\n                \"compound_id\": 518,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.025,\n                \"mmol_l\": 0.0524659,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\":
    \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.25,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\":
    \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\": 77,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [],\n        \"equipment\": []\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject":
    "SL11 incompatible dependency identity", "local_fields": [], "decision": "evidence_only",
    "stage": "source-only stock identity reconciliation", "interpretation": "Selected
    DSM 1291 uses dihydrate EDTA and 6 mg boric acid per stock batch, with final make-up
    to 1000 ml. Linked 5191 instead says Na2-EDTA and 6 g boric acid, with only pH
    6 instruction. Both raw sources are authentic; the selected link must be reconciled
    rather than treating the name as proof of equality.", "sources": [{"locator":
    "$.data.solutions[1].recipe[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key":
    "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "source_text_sha256":
    "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9", "accessed_at":
    "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.recipe[0]", "source_key": "solution5191",
    "reference": "https://mediadive.dsmz.de/rest/solution/5191", "source_raw_sha256":
    "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "source_text_sha256":
    "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0", "accessed_at":
    "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\":
    \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.recipe[4]",
    "source_key": "solution5191", "reference": "https://mediadive.dsmz.de/rest/solution/5191",
    "source_raw_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "source_text_sha256": "a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0",
    "accessed_at": "2026-10-28T09:30:21.988198Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q48", "subject": "Seven-vitamin incompatible dependency", "local_fields": [],
    "decision": "evidence_only", "stage": "source-only stock identity reconciliation",
    "interpretation": "All seven component concentrations in linked 4611 differ from
    the embedded 1038 stock, and its water input is 200 ml rather than 1000 ml. The
    link cannot be accepted by name alone; retain both separately authenticated formulations.",
    "sources": [{"locator": "$.data.solutions[2]", "source_key": "api1291", "reference":
    "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                \"id\":
    1038,\n                \"name\": \"Seven vitamins solution\",\n                \"volume\":
    1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ]\n            }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data", "source_key":
    "solution4611", "reference": "https://mediadive.dsmz.de/rest/solution/4611", "source_raw_sha256":
    "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "source_text_sha256":
    "66c691667610d8dd1f3fda2765389dc7aa068a108fccd4af97489b332849b270", "accessed_at":
    "2026-10-28T09:30:21.986065Z", "exact_source_quote": "{\n        \"id\": 4611,\n        \"name\":
    \"Seven vitamins solution\",\n        \"volume\": 200,\n        \"recipe\": [\n            {\n                \"recipe_order\":
    1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\":
    18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.0368895,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\":
    \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"D-(+)-biotin\",\n                \"compound_id\": 1359,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.01,\n                \"mmol_l\": 0.0409316,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.812282,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\":
    \"Calcium pantothenate\",\n                \"compound_id\": 518,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.025,\n                \"mmol_l\": 0.0524659,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\":
    \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.25,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\":
    \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\": 77,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [],\n        \"equipment\": []\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject":
    "Main preparation and source controls", "local_fields": [], "decision": "evidence_only",
    "stage": "source-only main preparation", "interpretation": "Preserve gellan dissolution,
    pH 5.0–5.3, air atmosphere and 30% vessel fill. Magnesium chloride, yeast extract
    and vitamins are added as sterile stocks after autoclaving; vitamins are filtered.
    Shaking is a source suggestion, not an independently measured growth claim. These
    instructions are missing from both selected layers.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\":
    \"Add gellan gum and boil to dissolve. Then add the remaining ingredients (except
    magnesium chloride, yeast extract and vitamins), adjust the pH value to 5.0 to
    5.3 and fill the medium under an air atmosphere into tubes of the Hungate type
    or similar vials up to 30% their volume. After autoclaving add magnesium chloride,
    yeast extract and vitamins from steril stock solutions. Vitamins should be sterilized
    by filtration.\"\n                    }", "quote_representation": "raw JSON object"},
    {"locator": "$.data.solutions[0].steps[1]", "source_key": "api1291", "reference":
    "https://mediadive.dsmz.de/rest/medium/1291", "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: Incubation with shaking may improve cell yield.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject":
    "Stock preparation controls", "local_fields": [], "decision": "evidence_only",
    "stage": "source-only SL11 preparation", "interpretation": "Retain 800 ml initial
    water,2 N NaOH to pH 7, order of ferrous chloride addition, final pH 6 and make-up
    to 1000 ml in the SL11 subsection. This explicit final-volume instruction does
    not apply to the main medium or the vitamin stock.", "sources": [{"locator": "$.data.solutions[1].steps[0]",
    "source_key": "api1291", "reference": "https://mediadive.dsmz.de/rest/medium/1291",
    "source_raw_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "source_text_sha256": "564fe0e68d75ec8a1422916957389f6c775a32e419859152c1457b928e3fbdd9",
    "accessed_at": "2026-10-28T09:30:22.072396Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch062/record05/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml: primary 21/23, secondary
    21/23; data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml: primary
    21/23, secondary 21/23. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric
    legacy MediaIngredientMech mentions occur across the complete selected documents,
    with exact locators in the inventory; NNNNNN is a historical placeholder, not
    an ID. Complex commercial/product components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:008921
  evidence_ids:
  - grounding
- assessment_id: a5
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:008921
  evidence_ids:
  - local0
- assessment_id: a6
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:008921
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-008921-stock-units-and-water-staleness
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock inputs and liquid additions are represented as main-medium mass concentrations
  description: Milligram stock rows retain their numerals as G_PER_L, gram stock rows
    remain flat, and three liquid additions have mass units. Generated water still
    sums three independent solvent rows; the owner numerical repair is credited but
    its unit and stage remain wrong. Five ordinary main masses have correct batch
    digits but unresolved per-litre basis.
  target_ids:
  - CultureMech:008921
  field_paths:
  - ingredients
  - solutions
  - ingredients[0].concentration
  evidence_ids:
  - togoM2334
  - dsmz1291
  - api1291
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-008921-incompatible-same-name-stock-links
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The named stock links point to different formulations
  description: SL11 link 5191 differs in EDTA form, boric acid 6 g versus 6 mg and
    preparation. Seven-vitamin link 4611 differs in all seven component strengths.
    Their 18 attached claims match their own current raw bytes and must not be overwritten
    simply to fit DSM 1291.
  target_ids:
  - CultureMech:008921
  field_paths:
  - solutions[1].term
  - solutions[2].term
  evidence_ids:
  - api1291
  - solution5191
  - solution4611
  rule_id: review-yaml-record/stock-source-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the asserted stock-source
    equivalence conflicts with the exact primary stock recipes; this custom rule does
    not claim native P2.1 invalid-ID semantics.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-008921-missing-preparation-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and quantitative evidence are missing
  description: Both layers lack pH 5.0–5.3, staged sterilization and addition instructions,
    air and fill controls, and claim-level evidence. Current TOGO writer can preserve
    nested sections, ml/mg units and comments; the historical flattened output does
    not prove that its current implementation still loses them.
  target_ids:
  - CultureMech:008921
  field_paths:
  - ph_range
  - preparation_steps
  - evidence
  - solutions
  evidence_ids:
  - dsmz1291
  - togoM2334
  - api1291
  rule_id: review-yaml-record/preparation-and-atmosphere-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major under this custom rule because omitted
    source pH, staged preparation, and air-and-fill context materially reduce preparation
    fidelity; this is not attributed to the native concentration-mismatch rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-008921-nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is linked to anhydrous nickel dichloride
  description: Selected nickel rows name the hexahydrate but both term slots point
    to CHEBI:34887. The same form mismatch occurs in the separately inspected 5191
    dependency chebi_term. Other supplied hydrates are credited. Generic calcium pantothenate
    and D-biotin retain their exact source labels; no unsupported stereochemical replacement
    is proposed.
  target_ids:
  - CultureMech:008921
  field_paths:
  - ingredients[10].term
  - ingredients[10].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::composition[7].chebi_term
  evidence_ids:
  - chebi34887
  - grounding
  - dsmz1291
  - solution5191
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the asserted nickel dichloride
    identifiers do not represent the explicitly supplied nickel chloride hexahydrate;
    this custom rule does not claim native P2.1 invalid-ID semantics.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: separately scoped linked SL11 stock chemical-form dependency
- finding_id: f5
  issue_key: culturemech-008921-placeholder-stock-metadata
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Stock placeholders obscure populated source tables
  description: Both linked stock records contain a full composition but also retain
    See source for composition and incomplete_composition placeholders. The selected
    solutions have meaningful preferred terms alongside Unknown solution names. These
    are structural remnants, not evidence that the authenticated stock recipes are
    absent.
  target_ids:
  - CultureMech:008921
  field_paths:
  - solutions[0].name
  - solutions[1].name
  - solutions[2].name
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml::data_quality_flags
  evidence_ids:
  - solution5191
  - solution4611
  rule_id: P3.1
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: separately scoped stock placeholder metadata
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml
    role: separately scoped stock placeholder metadata
actions:
- action_id: action1
  description: Reconstruct the main recipe and two stock sections using exact source
    units, preserve the existing numerical duplicate repair, keep absolute liquid
    additions and document denominator limits. Do not invent calcium-stock strength
    or convert listed water into final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008921
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
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
  description: Reconcile the receiving record links against exact embedded stock 1474/1038
    identities and complete compositions. Preserve linked 5191/4611 as separate source
    formulations and retain their authenticated evidence; no automatic whole-stock
    substitution.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008921
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Add the source-supported preparation to its correct main or stock stage
    and attach scoped evidence. Preserve unresolved calcium strength and physical-state
    interpretation; gellan content alone is not an explicit source state designation.
    Regenerate from repaired maintained inputs.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008921
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Resolve the exact nickel hydrate mapping independently in the selected
    owner and dependency, preserving all authentic quantities and evidence. If no
    verified mapping is available retain a precise source form with explicit unresolved
    grounding.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008921
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: separately scoped linked SL11 stock chemical-form dependency
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: After preserving the actual stock identities, review placeholder names,
    rows and flags against the complete composition and append a verified cleanup
    event. Do not remove or relabel historical evidence.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008921
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2334_Chthonomonas_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: separately scoped stock placeholder metadata
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4611_Seven_vitamins_solution.yaml
    role: separately scoped stock placeholder metadata
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- Calcium dihydrate is printed as 0.15 ml with no strength; neither a mass replacement
  nor a final calcium concentration is established.
- API 1291 declares 1002 ml yet keeps main g_l values equal to gram inputs. The primary
  provides water inputs rather than explicit final medium volume. No unsupported normalization
  is introduced.
- Generic source pantothenate does not independently select a stereoisomer. Current
  MIM joins and exact OLS labels are separate from supplied-form equivalence; all
  selected numeric legacy MIM counts are zero.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
