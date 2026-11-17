# Scientific review of desulfobacterium_naphthalenivolans_medium

- Review: 20261028T184659Z-desulfobacterium-naphthalenivolans-medium-batch074
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:09:49.387552Z
- Finished UTC: 2026-10-28T18:46:59.092780Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected formulation needs source-specific unit, stock-boundary and preparation curation. Existing repaired dependency evidence is credited; remaining scoped dependency form or unit errors are identified without transferring parent-medium recipes.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch074 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007762 | data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml | generated | desulfobacterium_naphthalenivolans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007762 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:007762 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:007762 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:007762 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### M609 vitamin reference resolves to a different stock

identity: concern. Targets: CultureMech:007762.

M609 solutions[3].term resolves to provider6241, whose three-vitamin formula differs from the eight-vitamin JCM602/TOGO609 and J1151 source stock. The standalone6241 contents and its two old claims are comparison-only, not a corrective recipe or receiving evidence.

### Historical repairs and current writer behavior

provenance: concern. Targets: CultureMech:007762.

Selected histories are derivative import/migration records and do not contain attached formulation claims. The M180 iron/trace repair is credited through exact existing excerpts and current raw digests. Historical plan rows and zero-source-check reports are retained separately; original events remain unchanged. Current import/migration and cleanup behavior is read as code, not proof of past execution.

### Exact source and target identity

identity: supported. Targets: CultureMech:007762.

The selected generated target and exact maintained TOGO contributor identify the corresponding current source accession. Similar labels and generic stock names do not establish equivalence with other maintained medium records. No organism growth claim is inferred from a recipe name.

### Classification and metadata limits

consistency: concern. Targets: CultureMech:007762.

LIQUID is consistent with the selected formulation. Current APIJ1151 explicitly reports data.medium.complex_medium: 'no', and the reviewed provider formulation specifies its chemical components; the retained COMPLEX/UNDEFINED importer defaults therefore require classification follow-up. Retain LIQUID and distinguish this provider classification from experimental growth or performance. The current JCM1151 primary page remains unavailable, so independent primary corroboration is unresolved.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:007762.

All 40 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007762", "selected_concentration_field_count": 40, "selected_concentration_fields_covered": 40, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "970", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "970", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving basal batch", "interpretation": "Source basal water is 970 ml, not 970 g/L. The provider lists nominal total volume1028 ml, but preparation stages and separately per-litre additions do not establish an independently measured final volume.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 970,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 970,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.972763,\n                        \"mmol_l\": 16.6455,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "CaCl2・2H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.15", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[2]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.145914,\n                        \"mmol_l\": 0.992514,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[3]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.194553,\n                        \"mmol_l\": 1.42963,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[4]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.243191,\n                        \"mmol_l\": 4.54647,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving basal batch", "interpretation": "The source supplies resazurin in mg per basal batch. The retained same-number G_PER_L value is not supported and is not converted through an assumed final litre. Preserve the explicit mass and stage.", "sources": [{"locator": "$.components[0].items[5]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 0.4,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000389105,\n                        \"mmol_l\": 0.00169774,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "MgCl2・6H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[6]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.389105,\n                        \"mmol_l\": 1.91392,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[7]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.486381,\n                        \"mmol_l\": 6.52423,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "1.42", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "1.42", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation": "The source supports the exact supplied compound and batch mass, but no explicit final-medium volume supports the same-number G_PER_L assertion. Preserve the batch amount; do not invent a final rate. MediaDive declares a different normalized g_l on its1028ml nominal basis; this is retained as a distinct provider claim, not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[8]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 1.42,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 1.42,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.38132,\n                        \"mmol_l\": 9.72489,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Receiving basal batch", "interpretation": "Retain the unquantified VARIABLE gas placeholder. Source names the gas and preparation controls its atmosphere; there is no fixed dissolved-gas concentration or ingredient amount to infer.", "sources": [{"locator": "$.components[0].items[12]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Nitrogen gas", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Receiving basal batch", "interpretation": "Retain the unquantified VARIABLE gas placeholder. Source names the gas and preparation controls its atmosphere; there is no fixed dissolved-gas concentration or ingredient amount to infer.", "sources": [{"locator": "$.components[0].items[13]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Naphthalene", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate naphthalene stock", "interpretation": "Source naphthalene is1.5g in a stock with100ml solvent; provider explicitly gives15g/L for this stock only. Local1.5g/L main-medium placement is wrong. Do not multiply by receiving dose without its verified denominator.", "sources": [{"locator": "$.components[3].items[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Naphthalene\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001307\",\n          \"gmo_id\": \"GMO_001307\",\n          \"label\": \"Naphthalene\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Naphthalene\",\n                        \"compound_id\": 432,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 117.032,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "2,2,4,4,6,8,8-Heptamethylnonane", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate naphthalene stock", "interpretation": "The stock solvent is100ml heptamethylnonane, not100g/L in the main medium. No density, mass fraction or final-volume equivalence is assumed.", "sources": [{"locator": "$.components[3].items[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"2,2,4,4,6,8,8-Heptamethylnonane\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002098\",\n          \"gmo_id\": \"GMO_002098\",\n          \"label\": \"Isocetane\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"2,2,4,4,6,8,8-Heptamethylnonane\",\n                        \"compound_id\": 303,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 solution (see Medium [M180])", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. Preserve the receiving-batch volume and the distinct stock identity; final-volume scaling is not established.", "sources": [{"locator": "$.components[0].items[9]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Trace element solution (see Medium [M180])", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. Preserve the receiving-batch volume and the distinct stock identity; final-volume scaling is not established.", "sources": [{"locator": "$.components[0].items[10]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "Selenite--tungstate solution (see Medium [M431])", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. Preserve the receiving-batch volume and the distinct stock identity; final-volume scaling is not established.", "sources": [{"locator": "$.components[0].items[11]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M431\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "8% NaHCO3 solution", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[3].concentration", "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[3].concentration", "original": {"value": "30", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. Preserve the receiving-batch volume and the distinct stock identity; final-volume scaling is not established. The percentage label lacks an explicit basis; retain the exact label without w/v, density or molarity inference.", "sources": [{"locator": "$.components[1].items[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components and autoclave under a N2-CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions (filter-sterilized):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "Vitamin solution (see Medium [M609])", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. Preserve the receiving-batch volume and the distinct stock identity; final-volume scaling is not established.", "sources": [{"locator": "$.components[1].items[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin solution (see Medium [M609])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M609\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components and autoclave under a N2-CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions (filter-sterilized):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "5% Na2S・9H2O solution", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[5].concentration", "original": {"value": "4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[5].concentration", "original": {"value": "4", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. The second procedure explicitly specifies these late additions per litre; keep that basis separate from the earlier batch additions. The percentage label lacks an explicit basis; retain the exact label without w/v, density or molarity inference.", "sources": [{"locator": "$.components[2].items[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 4,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\": 4,\n      \"comment\": \"Aseptically and anaerobically distribute the medium into culture vessels (e.g., 50 ml of the medium in 120 ml serum bottle) under a N2-CO2 (4:1,v/v) gas mixture, and seal with butyl rubber stoppers. Prior to use, add per liter the following solution (autoclaved and stored under a N2 atmosphere):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "1.5% Naphthalene solution (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path": "solutions[6].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml", "field_path": "solutions[6].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation": "Source specifies a liquid addition in ml, not the current same-number G_PER_L. The second procedure explicitly specifies these late additions per litre; keep that basis separate from the earlier batch additions. The percentage label lacks an explicit basis; retain the exact label without w/v, density or molarity inference.", "sources": [{"locator": "$.components[2].items[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\": \"1.5% Naphthalene solution (see below)\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1233\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\": 4,\n      \"comment\": \"Aseptically and anaerobically distribute the medium into culture vessels (e.g., 50 ml of the medium in 120 ml serum bottle) under a N2-CO2 (4:1,v/v) gas mixture, and seal with butyl rubber stoppers. Prior to use, add per liter the following solution (autoclaved and stored under a N2 atmosphere):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "Source preparation and controls 1", "local_fields": [], "decision": "add", "stage": "Source-only staged procedure", "interpretation": "Restore the exact staged preparation and its source-only numeric controls; retain gas proportions as gas-mixture specifications, vessel quantities as examples, and stock preparation separately. No transfer of a dependency parent-medium preparation.", "sources": [{"locator": "$.comments[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components and autoclave under a N2-CO2 (4:1, v/v) gas mixture. After cooling, add the following solutions (filter-sterilized):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "Source preparation and controls 2", "local_fields": [], "decision": "add", "stage": "Source-only staged procedure", "interpretation": "Restore the exact staged preparation and its source-only numeric controls; retain gas proportions as gas-mixture specifications, vessel quantities as examples, and stock preparation separately. No transfer of a dependency parent-medium preparation. This includes50ml medium/120ml vessel as an example,4:1v/v atmosphere and explicit per-litre late additions.", "sources": [{"locator": "$.comments[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\": 4,\n      \"comment\": \"Aseptically and anaerobically distribute the medium into culture vessels (e.g., 50 ml of the medium in 120 ml serum bottle) under a N2-CO2 (4:1,v/v) gas mixture, and seal with butyl rubber stoppers. Prior to use, add per liter the following solution (autoclaved and stored under a N2 atmosphere):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "M180 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].composition[0].notes", "original": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 990.0, 990.0, 1.0]\n\nSource water batch input: 990 ml = 0.99 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record."}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].composition[0].concentration", "original": {"value": "0.99", "unit": "L"}}], "decision": "verified", "stage": "Scoped M180 iron stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[1].items[1]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[18]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "Distilled water\n990.0\nml", "quote_representation": "HTML tr[18] DOM text"}]}, {"decision_id": "q24", "subject": "M180 FeCl2・4H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].composition[1].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 iron stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[1].items[2]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[17]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "FeCl\n2\n·4H\n2\nO\n1.5\ng", "quote_representation": "HTML tr[17] DOM text"}]}, {"decision_id": "q25", "subject": "M180 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[0].notes", "original": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 990.0, 990.0, 1.0]\n\nSource water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record."}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[0].concentration", "original": {"value": "1", "unit": "L"}}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[0]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[26]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[26] DOM text"}]}, {"decision_id": "q26", "subject": "M180 Na2MoO4・2H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[1].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[1]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[25]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n36.0\nmg", "quote_representation": "HTML tr[25] DOM text"}]}, {"decision_id": "q27", "subject": "M180 H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[2].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[2]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[21]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "H\n3\nBO\n3\n6.0\nmg", "quote_representation": "HTML tr[21] DOM text"}]}, {"decision_id": "q28", "subject": "M180 MnCl2・4H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[3].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[3]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[20]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n100.0\nmg", "quote_representation": "HTML tr[20] DOM text"}]}, {"decision_id": "q29", "subject": "M180 CoCl2・6H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[4].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[4]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[22]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n190.0\nmg", "quote_representation": "HTML tr[22] DOM text"}]}, {"decision_id": "q30", "subject": "M180 NiCl2・6H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[5].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[5]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[24]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "NiCl\n2\n·6H\n2\nO\n24.0\nmg", "quote_representation": "HTML tr[24] DOM text"}]}, {"decision_id": "q31", "subject": "M180 CuCl2・2H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[6].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[6]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[23]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "CuCl\n2\n·2H\n2\nO\n2.0\nmg", "quote_representation": "HTML tr[23] DOM text"}]}, {"decision_id": "q32", "subject": "M180 ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[7].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock", "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate this repaired stock field. Retain the explicit batch-water volume or source batch-mass note and absence of unsupported mass-per-litre concentration. Earlier duplicate notes are historical; parent doses and medium quantities do not transfer. Chemical supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[7]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[19]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "ZnCl\n2\n70.0\nmg", "quote_representation": "HTML tr[19] DOM text"}]}, {"decision_id": "q33", "subject": "M180 nested HCl dose and explicit strength", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].solutions[0].concentration", "original": {"value": "0.01", "unit": "L"}}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].solutions[0].notes", "original": "Source stock addition: 10 ml = 0.01 L per receiving batch, not grams per liter or a dose per final liter."}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].solutions[0].composition[0].concentration", "original": {"value": "7.7", "unit": "MOLAR"}}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].solutions[0].composition[0].notes", "original": "Role: Solvating media; Properties: Defined component, Inorganic compound, Solution\n\nExplicit HCl reagent strength 7.7 M, not a final-medium concentration. The 25% basis is unspecified; the enclosing stock holds the 10 ml batch dose."}], "decision": "verified", "stage": "FeCl2 stock nested reagent", "interpretation": "Retain0.01L HCl batch dose and7.7M reagent strength; source25% basis remains unspecified. Both attached TOGO and JCM excerpts and the separately scoped root dose excerpt authenticate the current fields. This is not receiving-medium acid molarity.", "sources": [{"locator": "$.components[1].items[0]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[16]", "source_key": "jcm187", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256": "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at": "2026-10-28T18:06:52.466627Z", "exact_source_quote": "25% HCl (7.7 M)\n10.0\nml", "quote_representation": "HTML tr[16] DOM text"}]}, {"decision_id": "q34", "subject": "M431 Se/W Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "989.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[11].notes", "original": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 1.0, 987.0, 1.0]"}], "decision": "correct", "stage": "Scoped Se/W stock", "interpretation": "Only the Se/W stock is in scope. Restore its1L water batch separately; current989g/L is a flattened sum of unrelated parent/trace/SeW volumes, not a meaningful concentration.", "sources": [{"locator": "$.components[3].items[0]", "source_key": "togo431", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431", "source_raw_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "source_text_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "accessed_at": "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[32]", "source_key": "jcm431", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256": "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at": "2026-10-28T18:10:03.362170Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[32] DOM text"}, {"locator": "$.data.solutions[4].recipe[3]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "M431 Se/W Na2SeO3・5H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[27].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped Se/W stock", "interpretation": "Only the Se/W stock is in scope. Source specifies mg of the stated hydrate, not the same-number g/L. Keep explicit stock batch mass and supplied form; no final-medium conversion.", "sources": [{"locator": "$.components[3].items[1]", "source_key": "togo431", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431", "source_raw_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "source_text_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "accessed_at": "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[30]", "source_key": "jcm431", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256": "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at": "2026-10-28T18:10:03.362170Z", "exact_source_quote": "Na\n2\nSeO\n3\n·5H\n2\nO\n6.0\nmg", "quote_representation": "HTML tr[30] DOM text"}, {"locator": "$.data.solutions[4].recipe[1]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0228125,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "M431 Se/W Na2WO4・2H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "8", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[28].notes", "original": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped Se/W stock", "interpretation": "Only the Se/W stock is in scope. Source specifies mg of the stated hydrate, not the same-number g/L. Keep explicit stock batch mass and supplied form; no final-medium conversion.", "sources": [{"locator": "$.components[3].items[2]", "source_key": "togo431", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431", "source_raw_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "source_text_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "accessed_at": "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[31]", "source_key": "jcm431", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256": "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at": "2026-10-28T18:10:03.362170Z", "exact_source_quote": "Na\n2\nWO\n4\n·2H\n2\nO\n8.0\nmg", "quote_representation": "HTML tr[31] DOM text"}, {"locator": "$.data.solutions[4].recipe[2]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 8,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.008,\n                        \"mmol_l\": 0.0242534,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "M431 Se/W NaOH", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path": "ingredients[29].notes", "original": "Properties: Defined component, Simple component, Inorganic compound"}], "decision": "correct", "stage": "Scoped Se/W stock", "interpretation": "Only the Se/W stock is in scope. Source 0.4 g NaOH is a stock batch mass; listed 1 L water alone does not prove final volume. Current MediaDive4172 separately declares 0.4 g/L for the matching stock formula, which supports the provider-normalized stock basis. The local M431 ingredient remains flattened at the parent root, so that supported stock value does not validate its present receiving-medium placement. Restore the stock boundary while retaining the source amount and provider-basis credit; do not assert a measured final volume or parent-medium equivalence.", "sources": [{"locator": "$.components[3].items[3]", "source_key": "togo431", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431", "source_raw_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "source_text_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "accessed_at": "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\": \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\": \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[29]", "source_key": "jcm431", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256": "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at": "2026-10-28T18:10:03.362170Z", "exact_source_quote": "NaOH\n0.4\ng", "quote_representation": "HTML tr[29] DOM text"}, {"locator": "$.data.solutions[4].recipe[0]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 10.0007,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "M609 vitamin Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1003.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[0].notes", "original": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 6 duplicates: 900.0, 1.0, 1.0, 50.0, 50.0, 1.0]"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Keep1L stock water separate from the flattened1003g/L aggregate of several unrelated M609 stages.", "sources": [{"locator": "$.components[7].items[0]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[8]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[35]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[35] DOM text"}]}, {"decision_id": "q39", "subject": "M609 vitamin Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[23].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[1]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[0]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[27]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Biotin\n20.0\nmg", "quote_representation": "HTML tr[27] DOM text"}]}, {"decision_id": "q40", "subject": "M609 vitamin p--Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[24].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[2]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[2]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.729182,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[29]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "p\n-Aminobenzoic acid\n100.0\nmg", "quote_representation": "HTML tr[29] DOM text"}]}, {"decision_id": "q41", "subject": "M609 vitamin Thiamine・HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "200", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[25].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[3]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[3]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[30]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Thiamine·HCl\n200.0\nmg", "quote_representation": "HTML tr[30] DOM text"}]}, {"decision_id": "q42", "subject": "M609 vitamin Pyridoxine・HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "500", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[26].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[4]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 500,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[5]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 500,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[32]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Pyridoxine·HCl\n500.0\nmg", "quote_representation": "HTML tr[32] DOM text"}]}, {"decision_id": "q43", "subject": "M609 vitamin Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[27].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[5]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[6]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[33]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Vitamin B\n1\n2\n100.0\nmg", "quote_representation": "HTML tr[33] DOM text"}]}, {"decision_id": "q44", "subject": "M609 vitamin Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[28].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[6]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[7]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.265675,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[34]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Riboflavin\n100.0\nmg", "quote_representation": "HTML tr[34] DOM text"}]}, {"decision_id": "q45", "subject": "M609 vitamin Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "200", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[29].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[7]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[1]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[28]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Nicotinic acid\n200.0\nmg", "quote_representation": "HTML tr[28] DOM text"}]}, {"decision_id": "q46", "subject": "M609 vitamin DL--Calcium pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml", "field_path": "ingredients[30].notes", "original": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component"}], "decision": "correct", "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides this vitamin in mg per separate stock batch; the same-number G_PER_L field is wrong. MediaDive4460 independently declares its normalized stock g_l, which is not a receiving-medium concentration. Preserve exact supplied form, including D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator": "$.components[7].items[8]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\": \"DL--Calcium pantothenate\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001936\",\n          \"gmo_id\": \"GMO_001936\",\n          \"label\": \"DL-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[4]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\": 1720,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209864,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[31]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "DL-Calcium pantothenate\n100.0\nmg", "quote_representation": "HTML tr[31] DOM text"}]}, {"decision_id": "q47", "subject": "M609 vitamin filtration and atmosphere", "local_fields": [], "decision": "add", "stage": "Vitamin stock-only preparation", "interpretation": "Retain filter sterilization and N2storage from the vitamin subsection only. Exclude the parent-medium70kPa overpressure, receivingdose, pH and other stock instructions.", "sources": [{"locator": "$.comments[5]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n      \"paragraph_index\": 14,\n      \"comment\": \"Filter--sterilize and store under a N2 atmosphere.\"\n    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].steps[0]", "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"step\": \"Filter-sterilize and store under a N2 atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch074/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:007762.

data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml: primary 13/13, secondary 9/13; data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml: primary 13/13, secondary 9/13. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:007762.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:007762.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Batch volumes, masses and stock stages are misrepresented

major / open / confirmed; issue key: culturemech-007762-batch-units-and-stock-boundaries.

The selected target and maintained owner preserve imported numbers but misrepresent water and liquid additions as mass concentrations. Stock-only ingredients are flattened into the main recipe where present, and mg inputs are represented by same-number g/L. Ordinary gram amounts have no verified final-volume basis; all unchanged and changed fields are enumerated in the inventory.

### f2: Source procedures and claim evidence are absent from the selected layers

major / open / confirmed; issue key: culturemech-007762-missing-staged-preparation-and-evidence.

Both selected layers lack the source staged preparation and attached formulation excerpts. Empty stock compositions and Unknown solution names obscure otherwise recoverable source stock identity. Gas placeholders are unquantified fields, while the source atmosphere, example vessel controls and sterilization sequence belong to preparation.

### f3: M180 trace-stock hydrate labels carry anhydrous identifiers

major / open / confirmed; issue key: culturemech-007762-linked-stock-hydrate-mapping.

Within the assessed M180 trace stock, cobalt chloride hexahydrate and nickel chloride hexahydrate retain anhydrous CHEBI35696 and34887. Current OLS formulas and masses omit hydrate water; native label validation and MIM mapped aliases do not prove source-form equivalence. The recent amount/preparation repair is credited and did not recertify these mappings.

### f4: Linked Se/W stock remains flattened in its parent record

major / open / confirmed; issue key: culturemech-007762-sew-stock-flattening.

The source-linked Se/W recipe is represented by empty solution composition and root ingredients with incorrect water/mg units. Only its four components and stock identity are in scope; the M431 receiving dose and unrelated parent/trace recipes are excluded.

### f5: Linked vitamin parent and provider stock are not equivalent

major / open / confirmed; issue key: culturemech-007762-vitamin-stock-identity-and-amounts.

M609 retains eight vitamin masses in wrong g/L units plus collapsed water, while its vitamin solution points to the different three-vitamin6241 formula. The exact JCM602 source and current TOGO609/MediaDive4460 establish the eight-component stock independently of that generic-name linkage. The primary JCM1151 page itself remains unavailable.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the exact source batch and stock boundaries in the maintained owner. Preserve separate dose, stock composition, source water and preparation-stage evidence; replace unsupported concentration assertions with explicit batch notes or a source-declared provider basis where justified. Regenerate the target only after maintained input corrections.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Add the exact selected-source preparation with explicit stage-scoped root evidence, and fill or resolve the source-specific stock definitions without importing dependency parent-media instructions. Preserve unquantified gas placeholders and percentages with unknown basis. Do not invent pH or controls absent from the selected source.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the exact supplied hydrate identities against authoritative ontology evidence or retain precise source labels as unresolved; preserve repaired source batch notes and all authentic attached evidence. Do not change unrelated M180 parent fields or use anhydrous molecular masses.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Restore the separate Se/W source stock with its explicit batch inputs and source-form evidence, retaining unresolved final-volume basis. Scope any edit to this stock and preserve all unrelated M431 content.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Restore the source-specific vitamin stock and correct its erroneous reference identity without rewriting standalone6241 merely to fit this receiving record. Preserve D,L-pantothenate source identity and unresolved legacy mapping; do not import parent pressure/pH/dose controls.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch074/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch074/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch074/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch074/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full parent source read as context; only the selenite-tungstate stock is assessed. Parent medium, other trace stock, receiving dose and parent preparation are excluded. |
| togo431 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full parent source read as context; only the selenite-tungstate stock is assessed. Parent medium, other trace stock, receiving dose and parent preparation are excluded. |
| jcm1151 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1151; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Exact JCM1151 page returns HTTP200 but Nothing found; no primary recipe is available from this capture. Current TOGO and MediaDive provider formulations are assessed separately. |
| togo1233 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current TOGO identity, components and comments read; exact paragraphs distinguish receiving recipe, post-sterilization additions and stock definitions. Batch inputs and bare percentages are not silently converted to final-medium rates. |
| jcm615 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=615; raw source; exact captured text/DOM/JSON locators in quantity inventory | context_only | Excluded preliminary accession lead. Actual vitamin dependency M609 identifies JCM602; no JCM615 formulation or organism claim transfers. |
| togo609 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full parent source read as context; only the eight-vitamin stock and its preparation are assessed. Parent medium, other stocks and receiving doses are excluded. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full parent source read as context. Scientific scope is only the separate FeCl2 stock including nested HCl reagent, and trace-element stock. Parent medium, receiving doses, vitamins, pH and parent preparation are excluded. |
| togo180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full parent source read as context. Scientific scope is only the separate FeCl2 stock including nested HCl reagent, and trace-element stock. Parent medium, receiving doses, vitamins, pH and parent preparation are excluded. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon compound with formula CO&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt; in which the carbon is attached to each oxygen atom by a double bond. A colourless, odourless gas under normal conditions, it is produced during respiration by all animals, fungi and microorganisms that depend directly or indirectly on living or decaying plants for food.']; formula ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26836 = sulfuric acid; definition ['A sulfur oxoacid that consists of two oxo and two hydroxy groups joined covalently to a central sulfur atom.']; formula ['H2O4S']; mass ['98.079']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33403 = elemental sulfur; definition []; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt salt in which the cobalt metal is in the +2 oxidation state and the counter-anion is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co']; mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W']; mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used).']; formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi131383 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131383; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131383 = 2,2,4,4,6,8,8-heptamethylnonane; definition ['A branched alkane that is nonane carrying seven methyl substituents at positions 2, 2, 4, 4, 6, 8 and 8.']; formula ['C16H34']; mass ['226.448']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16482 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16482; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16482 = naphthalene; definition ['An aromatic hydrocarbon comprising two fused benzene rings. It occurs in the essential oils of numerous plant species e.g. magnolia.']; formula ['C10H8']; mass ['128.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34683 = disodium hydrogenphosphate; definition []; formula ['HO4P.2Na']; mass ['141.958']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75228 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75228; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75228 = sodium lactate; definition ['An organic sodium salt having lactate as the counterion.']; formula ['C3H5O3.Na']; mass ['112.06']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| jcm602 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full parent source read as context; only the eight-vitamin stock and its preparation are assessed. Parent medium, other stocks and receiving doses are excluded. |
| apiJ1151 | https://mediadive.dsmz.de/rest/medium/J1151; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive J1151 identity, six solution tables and preparation read. Explicit g_l values and 1028ml main volume are provider normalization, not independent final-volume measurement. Separate stock concentrations and source forms do not transfer to the main medium; questionable provider mmol_l conversions are not adopted. |
| stock6241 | https://mediadive.dsmz.de/rest/solution/6241; raw source; exact captured text/DOM/JSON locators in quantity inventory | context_only | Complete standalone provider identity/composition read for comparison with M609 vitamin stock. Three-vitamin formula differs from the eight-vitamin receiving source. Standalone numeric amounts and its historical curation are context-only; no receiving formulation transfer or standalone correction is proposed. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17439 = cyanocob(III)alamin; definition ['A complex cob(III)alamin in which cobalt is positioned in the centre of a planar corrin tetrapyrrole ring and bound axially to a 5,6-dimethylbenzimidazole moiety and a cyano group. It is one of several forms of the vitamin known as vitamin B12.']; formula ['C63H88CoN14O14P']; mass ['1355.388']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch074/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected and dependency-context term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_naphthalenivolans_medium__c96254de.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobacterium_naphthalenivolans_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history8 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history9 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read. October5 zero-source-check diagnostics are historical structure only; same-label DSM or generated sibling reports are comparison-only. October8 stock reports and the exact M180 parent-plan row document source-scoped repairs. Current source/claim equality is recorded separately; historical access time, tool execution and unrelated parent-medium science are not authenticated. |
| history-auth | REVIEW_WORK/batch074/record06/historical-authentication.json; attached_claims; historical_plan_claims | supports | Every actual attached claim in the scoped dependency stock sections is reconciled with fresh captured bytes and original raw-digest assertions. Report-plan claims are separately retained as historical context; no attached claims exist on either selected layer. Current byte equality authenticates excerpts, not historical execution or dates. |
| writer70 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer71 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer72 | scripts/migrate_solutions_from_ingredients.py; _is_solution; _resolve_solution; _migrate_media_file | context_only | Current _is_solution uses name patterns, _resolve_solution keeps concentrations while creating empty reference stubs or matching a name-indexed solution, and _migrate_media_file appends those solutions and history. It does not reconstruct nested source batches or authenticate copied unit/basis. |
| writer73 | scripts/repair_jcm_stock_preparations.py; frozen; sources; Review.leaf; Review.stock; Review.stages; Review.procedures; build; process | context_only | Current frozen/sources checks a pinned context and exact J151/J187/J197 and M142/M180/M190 graphs. Review.leaf withdraws unsupported TOGO mass rates, retains explicit batch-water volumes and qualified provider stock rates; stock/stages separate additions; procedures keeps parent preparation and pH scoped. Existing annotations survive, so this repair does not recertify hydrate mappings. Only this module was read; imported shared internals and historical execution are not independently authenticated. |
| writer74 | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _extract_assembled_solutions; _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph | context_only | Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions distinguish primary sections, nested stocks and assembled solutions. _parse_unit maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices still require a verified source basis. _extract_preparation_steps retains comments. _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied object. These present behaviors neither authenticate historical execution nor prove that all source metadata survived the old import. |
| writer75 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer76 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer77 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| dep78 | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency retained as context; only the explicitly named stock subsection is assessed. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep79 | data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency retained as context; only the explicitly named stock subsection is assessed. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep80 | data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency retained as context; only the explicitly named stock subsection is assessed. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep81 | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency retained as context; only the explicitly named stock subsection is assessed. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| quantity-inventory | REVIEW_WORK/batch074/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- No independent final-medium volume, density or bare-percent basis is established; source batch inputs, provider normalization and declared receiving bases remain distinct.
- Historical report and claim-byte matches do not authenticate historical tool execution or original access time. All old events must be preserved; any future correction should append current verified context.
- All dependency parents were read as context, but only explicitly enumerated stock fields are scientifically assessed. Parent doses, other stocks, pH and organism growth do not transfer.
- Current packaged MIM snapshot 6643131b0f12ab40b66f98135245fca04027e0e9 is a present identifier/label index, not a historical-validity certificate or supplied-form authority.
- Current exact JCM1151 returned HTTP200 with Nothing found. TOGO1233 and MediaDiveJ1151 are provider evidence; no full current primary recipe was recovered. Earlier JCM615 was an excluded preliminary lead; actual vitamin dependency is JCM602.
- Standalone6241 quantities and chemical mappings are comparison-only; its formula mismatch does not authorize rewriting the standalone record.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T184659Z-desulfobacterium-naphthalenivolans-medium-batch074
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfobacterium_naphthalenivolans_medium
started_at: '2026-10-28T18:09:49.387552Z'
finished_at: '2026-10-28T18:46:59.092780Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The selected formulation needs source-specific unit, stock-boundary and preparation
  curation. Existing repaired dependency evidence is credited; remaining scoped dependency
  form or unit errors are identified without transferring parent-medium recipes.
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
  - path: data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
    sha256: c5f38262317c3b86f2343b3725c96fec1785be6db1639c8cdc128b3d425f72a0
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
    sha256: 6c099468a64a05bdf0141cfa0b24630168798251cbd771c0363353339ec8c616
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml
    sha256: 79b62853cf258e0dd9312404cdd3198140f0c6f93b0884d904594ee1aa9dce9e
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
    sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
    sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
    sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.md
    sha256: a74f52371072c37bbd775950bdb7aeeba6f24f3445607ae1c8c79428621feec2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_naphthalenivolans_medium__c96254de.md
    sha256: 0fd08b7ec7dd2be602bfa74cc56629beb01b72d931f90e30e349339406917ea2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
    sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.md
    sha256: 802c9b601e2989eb4508c9549e842517a166f1ca8f6731d22d1c07aa7571398d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
    sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.md
    sha256: fcadf8c5dbc6f249608ea11dd4468dadd0d29be90315d6d081cd0680ead30b50
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobacterium_naphthalenivolans_medium.md
    sha256: 3a85901cfdbb87aa9cb5fba63cc6420072b95d977c32156451bb2202515141e4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
    sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  selection: Authoritative batch074 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007762
targets:
- target_id: CultureMech:007762
  path: data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
  label: desulfobacterium_naphthalenivolans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007762
  command: just validate-schema data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007762
  command: just validate-strict data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch074/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007762
  command: just validate-terms data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:007762
  command: just validate-references data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T18:24:26.492980Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: c5f38262317c3b86f2343b3725c96fec1785be6db1639c8cdc128b3d425f72a0
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T18:24:26.493136Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 6c099468a64a05bdf0141cfa0b24630168798251cbd771c0363353339ec8c616
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch074/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:09:50.439438Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 3b31f7bb411f162c29cd2f5ad3326ccffbd04e2b793ae17d3863d652b0916e99
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch074/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:09:51.403913Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: ccfa6a6f7072bfc4806a597b0f56540f795b1656d3ef946c642dd46aaa3c3016
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch074/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:09:52.446469Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: d616af16dac11005cfe5fff424628cab93fddf4a2227c2518921959aad2d6a1e
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch074/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:09:53.163142Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 561a52e2244fc603bb0b2ff46550465bd6221a2e17039455457e0792ae294178
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:10:03.362170Z'
  support: supports
  summary: Full parent source read as context; only the selenite-tungstate stock is
    assessed. Parent medium, other trace stock, receiving dose and parent preparation
    are excluded.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: togo431
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:10:03.362269Z'
  support: supports
  summary: Full parent source read as context; only the selenite-tungstate stock is
    assessed. Parent medium, other trace stock, receiving dose and parent preparation
    are excluded.
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: jcm1151
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1151
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:10:04.192612Z'
  support: unknown
  summary: Exact JCM1151 page returns HTTP200 but Nothing found; no primary recipe
    is available from this capture. Current TOGO and MediaDive provider formulations
    are assessed separately.
  snapshot_sha256: 5b07c6fa3bb44f902c92fe019317211f802afdefdd9054206fe503bf091e769e
- evidence_id: togo1233
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:10:04.335196Z'
  support: supports
  summary: Complete current TOGO identity, components and comments read; exact paragraphs
    distinguish receiving recipe, post-sterilization additions and stock definitions.
    Batch inputs and bare percentages are not silently converted to final-medium rates.
  snapshot_sha256: 6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b
- evidence_id: jcm615
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=615
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:10:04.433257Z'
  support: context_only
  summary: Excluded preliminary accession lead. Actual vitamin dependency M609 identifies
    JCM602; no JCM615 formulation or organism claim transfers.
  snapshot_sha256: fd4b59f68aef7074127487586378a07c6c1c2e345b92440da1b749402f898ea4
- evidence_id: togo609
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:10:04.469853Z'
  support: supports
  summary: Full parent source read as context; only the eight-vitamin stock and its
    preparation are assessed. Parent medium, other stocks and receiving doses are
    excluded.
  snapshot_sha256: 7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:06:52.466627Z'
  support: supports
  summary: Full parent source read as context. Scientific scope is only the separate
    FeCl2 stock including nested HCl reagent, and trace-element stock. Parent medium,
    receiving doses, vitamins, pH and parent preparation are excluded.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: togo180
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:06:52.466439Z'
  support: supports
  summary: Full parent source read as context. Scientific scope is only the separate
    FeCl2 stock including nested HCl reagent, and trace-element stock. Parent medium,
    receiving doses, vitamins, pH and parent preparation are excluded.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:36.281868Z'
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
  accessed_at: '2026-10-28T18:11:36.282218Z'
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
  accessed_at: '2026-10-28T18:11:36.282283Z'
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
  accessed_at: '2026-10-28T18:11:36.282332Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.196023Z'
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
  accessed_at: '2026-10-28T18:11:37.206579Z'
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
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.209112Z'
  support: supports
  summary: OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used
    as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass
    ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.214405Z'
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
  accessed_at: '2026-10-28T18:11:37.269020Z'
  support: supports
  summary: OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule
    consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.803628Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi26836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.809436Z'
  support: supports
  summary: OLS current exact CHEBI:26836 = sulfuric acid; definition ['A sulfur oxoacid
    that consists of two oxo and two hydroxy groups joined covalently to a central
    sulfur atom.']; formula ['H2O4S']; mass ['98.079']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.890221Z'
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
  accessed_at: '2026-10-28T18:11:37.939862Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:37.989288Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:38.475033Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:38.511933Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:38.551032Z'
  support: supports
  summary: OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula
    ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:38.586772Z'
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
  accessed_at: '2026-10-28T18:11:39.044515Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.101551Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi33403
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.111804Z'
  support: supports
  summary: OLS current exact CHEBI:33403 = elemental sulfur; definition []; formula
    None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b349493be5d8cb371d1e71751510f9205880ab9d0a14f560191e05606c127a60
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.153761Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.185432Z'
  support: supports
  summary: OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt
    salt in which the cobalt metal is in the +2 oxidation state and the counter-anion
    is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co'];
    mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.656497Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.703714Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:39.705422Z'
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
  accessed_at: '2026-10-28T18:11:39.783336Z'
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
  accessed_at: '2026-10-28T18:11:39.812955Z'
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
  accessed_at: '2026-10-28T18:11:40.272762Z'
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
  accessed_at: '2026-10-28T18:11:40.284054Z'
  support: supports
  summary: OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition
    ['A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O.'];
    formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:40.327556Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:40.335104Z'
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
  accessed_at: '2026-10-28T18:11:40.394800Z'
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
  accessed_at: '2026-10-28T18:11:40.419003Z'
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
  accessed_at: '2026-10-28T18:11:40.909756Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:40.912366Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi131383
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131383
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:40.985467Z'
  support: supports
  summary: OLS current exact CHEBI:131383 = 2,2,4,4,6,8,8-heptamethylnonane; definition
    ['A branched alkane that is nonane carrying seven methyl substituents at positions
    2, 2, 4, 4, 6, 8 and 8.']; formula ['C16H34']; mass ['226.448']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 20a71e9aef2114e5d27624e98fc36dd396084bf9f7cd7c330be3a17068276ac7
- evidence_id: chebi16482
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16482
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:41.018371Z'
  support: supports
  summary: OLS current exact CHEBI:16482 = naphthalene; definition ['An aromatic hydrocarbon
    comprising two fused benzene rings. It occurs in the essential oils of numerous
    plant species e.g. magnolia.']; formula ['C10H8']; mass ['128.174']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0d4f487bf9315f5682f99005104fd6b1deaee4a8e894398675ab40d8a6f1bfa8
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:41.518447Z'
  support: supports
  summary: OLS current exact CHEBI:34683 = disodium hydrogenphosphate; definition
    []; formula ['HO4P.2Na']; mass ['141.958']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi75228
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75228
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:11:41.527753Z'
  support: supports
  summary: OLS current exact CHEBI:75228 = sodium lactate; definition ['An organic
    sodium salt having lactate as the counterion.']; formula ['C3H5O3.Na']; mass ['112.06'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 725fbc04444c481cec25519a6f632470427a7020613af93e84e05b5f23d66ccf
- evidence_id: jcm602
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:11:41.571473Z'
  support: supports
  summary: Full parent source read as context; only the eight-vitamin stock and its
    preparation are assessed. Parent medium, other stocks and receiving doses are
    excluded.
  snapshot_sha256: 57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac
- evidence_id: apiJ1151
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1151
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:11:41.586030Z'
  support: supports
  summary: Complete current MediaDive J1151 identity, six solution tables and preparation
    read. Explicit g_l values and 1028ml main volume are provider normalization, not
    independent final-volume measurement. Separate stock concentrations and source
    forms do not transfer to the main medium; questionable provider mmol_l conversions
    are not adopted.
  snapshot_sha256: 444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a
- evidence_id: stock6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:11:41.634582Z'
  support: context_only
  summary: Complete standalone provider identity/composition read for comparison with
    M609 vitamin stock. Three-vitamin formula differs from the eight-vitamin receiving
    source. Standalone numeric amounts and its historical curation are context-only;
    no receiving formulation transfer or standalone correction is proposed.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:13:23.051429Z'
  support: supports
  summary: OLS current exact CHEBI:17439 = cyanocob(III)alamin; definition ['A complex
    cob(III)alamin in which cobalt is positioned in the centre of a planar corrin
    tetrapyrrole ring and bound axially to a 5,6-dimethylbenzimidazole moiety and
    a cyano group. It is one of several forms of the vitamin known as vitamin B12.'];
    formula ['C63H88CoN14O14P']; mass ['1355.388']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch074/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T18:24:26.501571Z'
  support: supports
  summary: Complete selected and dependency-context term slots and current packaged
    MIM CSV exact-identifier joins with row locators and metadata commit; includes
    separately scoped dependency context. No fuzzy mapping or historical-validity
    inference.
  snapshot_sha256: 79ba4ca0dc8328df247158f5d4ba23dea1f7b386d34450d11c41ed83e5b8dcca
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540552Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540585Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: a74f52371072c37bbd775950bdb7aeeba6f24f3445607ae1c8c79428621feec2
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_naphthalenivolans_medium__c96254de.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540610Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: 0fd08b7ec7dd2be602bfa74cc56629beb01b72d931f90e30e349339406917ea2
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540633Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540654Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: 802c9b601e2989eb4508c9549e842517a166f1ca8f6731d22d1c07aa7571398d
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540676Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540698Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: fcadf8c5dbc6f249608ea11dd4468dadd0d29be90315d6d081cd0680ead30b50
- evidence_id: history7
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobacterium_naphthalenivolans_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540719Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: 3a85901cfdbb87aa9cb5fba63cc6420072b95d977c32156451bb2202515141e4
- evidence_id: history8
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540746Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: history9
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T18:24:26.540766Z'
  support: supports
  summary: Complete report body read. October5 zero-source-check diagnostics are historical
    structure only; same-label DSM or generated sibling reports are comparison-only.
    October8 stock reports and the exact M180 parent-plan row document source-scoped
    repairs. Current source/claim equality is recorded separately; historical access
    time, tool execution and unrelated parent-medium science are not authenticated.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch074/record06/historical-authentication.json
  locator: attached_claims; historical_plan_claims
  accessed_at: '2026-10-28T18:24:26.540810Z'
  support: supports
  summary: Every actual attached claim in the scoped dependency stock sections is
    reconciled with fresh captured bytes and original raw-digest assertions. Report-plan
    claims are separately retained as historical context; no attached claims exist
    on either selected layer. Current byte equality authenticates excerpts, not historical
    execution or dates.
  snapshot_sha256: 57c2f317f96c6417fe8e29e76732eacac3a39da8a2685b9043d1259fe3ee92ab
- evidence_id: writer70
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T18:24:26.540883Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer71
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T18:24:26.540907Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer72
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _is_solution; _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T18:24:26.540939Z'
  support: context_only
  summary: Current _is_solution uses name patterns, _resolve_solution keeps concentrations
    while creating empty reference stubs or matching a name-indexed solution, and
    _migrate_media_file appends those solutions and history. It does not reconstruct
    nested source batches or authenticate copied unit/basis.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer73
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: frozen; sources; Review.leaf; Review.stock; Review.stages; Review.procedures;
    build; process
  accessed_at: '2026-10-28T18:24:26.540971Z'
  support: context_only
  summary: Current frozen/sources checks a pinned context and exact J151/J187/J197
    and M142/M180/M190 graphs. Review.leaf withdraws unsupported TOGO mass rates,
    retains explicit batch-water volumes and qualified provider stock rates; stock/stages
    separate additions; procedures keeps parent preparation and pH scoped. Existing
    annotations survive, so this repair does not recertify hydrate mappings. Only
    this module was read; imported shared internals and historical execution are not
    independently authenticated.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: writer74
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _extract_assembled_solutions;
    _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph
  accessed_at: '2026-10-28T18:24:26.541017Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions
    distinguish primary sections, nested stocks and assembled solutions. _parse_unit
    maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices
    still require a verified source basis. _extract_preparation_steps retains comments.
    _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied
    object. These present behaviors neither authenticate historical execution nor
    prove that all source metadata survived the old import.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer75
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T18:24:26.541041Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer76
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T18:24:26.541064Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer77
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T18:24:26.541090Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: dep78
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T18:24:26.541109Z'
  support: supports
  summary: Current dependency retained as context; only the explicitly named stock
    subsection is assessed. Earlier attached evidence and history retained; unrelated
    parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dep79
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T18:24:26.541110Z'
  support: supports
  summary: Current dependency retained as context; only the explicitly named stock
    subsection is assessed. Earlier attached evidence and history retained; unrelated
    parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
- evidence_id: dep80
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T18:24:26.541111Z'
  support: supports
  summary: Current dependency retained as context; only the explicitly named stock
    subsection is assessed. Earlier attached evidence and history retained; unrelated
    parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 79b62853cf258e0dd9312404cdd3198140f0c6f93b0884d904594ee1aa9dce9e
- evidence_id: dep81
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T18:24:26.541112Z'
  support: supports
  summary: Current dependency retained as context; only the explicitly named stock
    subsection is assessed. Earlier attached evidence and history retained; unrelated
    parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch074/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T18:46:59.092780Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 9d02f906d1a29c9d8f905ace3fb56ecfb883fcf3fd963c38b84b77b7d289a3cd
assessments:
- assessment_id: a1
  area: identity
  topic: M609 vitamin reference resolves to a different stock
  outcome: concern
  summary: M609 solutions[3].term resolves to provider6241, whose three-vitamin formula
    differs from the eight-vitamin JCM602/TOGO609 and J1151 source stock. The standalone6241
    contents and its two old claims are comparison-only, not a corrective recipe or
    receiving evidence.
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - togo609
  - jcm602
  - stock6241
  - apiJ1151
- assessment_id: a2
  area: provenance
  topic: Historical repairs and current writer behavior
  outcome: concern
  summary: Selected histories are derivative import/migration records and do not contain
    attached formulation claims. The M180 iron/trace repair is credited through exact
    existing excerpts and current raw digests. Historical plan rows and zero-source-check
    reports are retained separately; original events remain unchanged. Current import/migration
    and cleanup behavior is read as code, not proof of past execution.
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - history-auth
  - writer70
  - writer71
  - writer72
  - writer73
  - writer74
  - writer75
  - writer76
  - writer77
- assessment_id: a3
  area: identity
  topic: Exact source and target identity
  outcome: supported
  summary: The selected generated target and exact maintained TOGO contributor identify
    the corresponding current source accession. Similar labels and generic stock names
    do not establish equivalence with other maintained medium records. No organism
    growth claim is inferred from a recipe name.
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - togo1233
  - jcm1151
- assessment_id: a4
  area: consistency
  topic: Classification and metadata limits
  outcome: concern
  summary: 'LIQUID is consistent with the selected formulation. Current APIJ1151 explicitly
    reports data.medium.complex_medium: ''no'', and the reviewed provider formulation
    specifies its chemical components; the retained COMPLEX/UNDEFINED importer defaults
    therefore require classification follow-up. Retain LIQUID and distinguish this
    provider classification from experimental growth or performance. The current JCM1151
    primary page remains unavailable, so independent primary corroboration is unresolved.'
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - togo1233
  - apiJ1151
  - jcm1151
  - local0
  - writer74
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 40 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007762",
    "selected_concentration_field_count": 40, "selected_concentration_fields_covered":
    40, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "970", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "970", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving basal batch", "interpretation":
    "Source basal water is 970 ml, not 970 g/L. The provider lists nominal total volume1028
    ml, but preparation stages and separately per-litre additions do not establish
    an independently measured final volume.", "sources": [{"locator": "$.components[0].items[0]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 970,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 970,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[1]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.972763,\n                        \"mmol_l\":
    16.6455,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "CaCl2・2H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.15", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.15", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[2]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ1151",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.145914,\n                        \"mmol_l\":
    0.992514,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[3]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.194553,\n                        \"mmol_l\":
    1.42963,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[4]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.243191,\n                        \"mmol_l\":
    4.54647,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "Resazurin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.4", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.4", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving basal batch", "interpretation":
    "The source supplies resazurin in mg per basal batch. The retained same-number
    G_PER_L value is not supported and is not converted through an assumed final litre.
    Preserve the explicit mass and stage.", "sources": [{"locator": "$.components[0].items[5]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 0.4,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000389105,\n                        \"mmol_l\":
    0.00169774,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject":
    "MgCl2・6H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.4", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.4", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[6]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.389105,\n                        \"mmol_l\":
    1.91392,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[7]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.486381,\n                        \"mmol_l\":
    6.52423,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "Na2SO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "1.42", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "1.42", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Receiving basal batch", "interpretation":
    "The source supports the exact supplied compound and batch mass, but no explicit
    final-medium volume supports the same-number G_PER_L assertion. Preserve the batch
    amount; do not invent a final rate. MediaDive declares a different normalized
    g_l on its1028ml nominal basis; this is retained as a distinct provider claim,
    not proof of measured final volume.", "sources": [{"locator": "$.components[0].items[8]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2SO4\",\n          \"volume\": 1.42,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\":
    \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 1.42,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.38132,\n                        \"mmol_l\":
    9.72489,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "Carbon dioxide gas",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Receiving basal
    batch", "interpretation": "Retain the unquantified VARIABLE gas placeholder. Source
    names the gas and preparation controls its atmosphere; there is no fixed dissolved-gas
    concentration or ingredient amount to infer.", "sources": [{"locator": "$.components[0].items[12]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q11", "subject": "Nitrogen gas", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Receiving basal
    batch", "interpretation": "Retain the unquantified VARIABLE gas placeholder. Source
    names the gas and preparation controls its atmosphere; there is no fixed dissolved-gas
    concentration or ingredient amount to infer.", "sources": [{"locator": "$.components[0].items[13]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q12", "subject": "Naphthalene", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate naphthalene stock", "interpretation":
    "Source naphthalene is1.5g in a stock with100ml solvent; provider explicitly gives15g/L
    for this stock only. Local1.5g/L main-medium placement is wrong. Do not multiply
    by receiving dose without its verified denominator.", "sources": [{"locator":
    "$.components[3].items[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Naphthalene\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001307\",\n          \"gmo_id\": \"GMO_001307\",\n          \"label\":
    \"Naphthalene\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key":
    "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Naphthalene\",\n                        \"compound_id\":
    432,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    117.032,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "2,2,4,4,6,8,8-Heptamethylnonane",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate naphthalene stock", "interpretation":
    "The stock solvent is100ml heptamethylnonane, not100g/L in the main medium. No
    density, mass fraction or final-volume equivalence is assumed.", "sources": [{"locator":
    "$.components[3].items[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"2,2,4,4,6,8,8-Heptamethylnonane\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002098\",\n          \"gmo_id\":
    \"GMO_002098\",\n          \"label\": \"Isocetane\",\n          \"properties\":
    [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ1151",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"2,2,4,4,6,8,8-Heptamethylnonane\",\n                        \"compound_id\":
    303,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 solution (see Medium
    [M180])", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    Preserve the receiving-batch volume and the distinct stock identity; final-volume
    scaling is not established.", "sources": [{"locator": "$.components[0].items[9]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q15", "subject": "Trace element solution (see Medium [M180])",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    Preserve the receiving-batch volume and the distinct stock identity; final-volume
    scaling is not established.", "sources": [{"locator": "$.components[0].items[10]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q16", "subject": "Selenite--tungstate solution (see Medium [M431])",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    Preserve the receiving-batch volume and the distinct stock identity; final-volume
    scaling is not established.", "sources": [{"locator": "$.components[0].items[11]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M431\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q17", "subject": "8% NaHCO3 solution", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml", "field_path":
    "solutions[3].concentration", "original": {"value": "30", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[3].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    Preserve the receiving-batch volume and the distinct stock identity; final-volume
    scaling is not established. The percentage label lacks an explicit basis; retain
    the exact label without w/v, density or molarity inference.", "sources": [{"locator":
    "$.components[1].items[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\":
    8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\":
    \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.comments[0]", "source_key":
    "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components and autoclave under a N2-CO2 (4:1, v/v)
    gas mixture. After cooling, add the following solutions (filter-sterilized):\"\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject":
    "Vitamin solution (see Medium [M609])", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "solutions[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    Preserve the receiving-batch volume and the distinct stock identity; final-volume
    scaling is not established.", "sources": [{"locator": "$.components[1].items[1]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"Vitamin solution (see Medium [M609])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M609\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"},
    {"locator": "$.comments[0]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components and autoclave under a N2-CO2 (4:1, v/v)
    gas mixture. After cooling, add the following solutions (filter-sterilized):\"\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject":
    "5% Na2S・9H2O solution", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "solutions[5].concentration", "original": {"value": "4", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[5].concentration", "original": {"value": "4", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    The second procedure explicitly specifies these late additions per litre; keep
    that basis separate from the earlier batch additions. The percentage label lacks
    an explicit basis; retain the exact label without w/v, density or molarity inference.",
    "sources": [{"locator": "$.components[2].items[0]", "source_key": "togo1233",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"5% Na2S・9H2O solution\",\n          \"volume\": 4,\n          \"unit\": \"ml\",\n          \"conc_value\":
    5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\":
    \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.comments[1]", "source_key": "togo1233", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233", "source_raw_sha256":
    "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "source_text_sha256":
    "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b", "accessed_at":
    "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Aseptically and anaerobically distribute the medium into
    culture vessels (e.g., 50 ml of the medium in 120 ml serum bottle) under a N2-CO2
    (4:1,v/v) gas mixture, and seal with butyl rubber stoppers. Prior to use, add
    per liter the following solution (autoclaved and stored under a N2 atmosphere):\"\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject":
    "1.5% Naphthalene solution (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml",
    "field_path": "solutions[6].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml",
    "field_path": "solutions[6].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving stock addition", "interpretation":
    "Source specifies a liquid addition in ml, not the current same-number G_PER_L.
    The second procedure explicitly specifies these late additions per litre; keep
    that basis separate from the earlier batch additions. The percentage label lacks
    an explicit basis; retain the exact label without w/v, density or molarity inference.",
    "sources": [{"locator": "$.components[2].items[1]", "source_key": "togo1233",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n          \"component_name\":
    \"1.5% Naphthalene solution (see below)\",\n          \"volume\": 20,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M1233\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"},
    {"locator": "$.comments[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Aseptically and anaerobically distribute the medium into
    culture vessels (e.g., 50 ml of the medium in 120 ml serum bottle) under a N2-CO2
    (4:1,v/v) gas mixture, and seal with butyl rubber stoppers. Prior to use, add
    per liter the following solution (autoclaved and stored under a N2 atmosphere):\"\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject":
    "Source preparation and controls 1", "local_fields": [], "decision": "add", "stage":
    "Source-only staged procedure", "interpretation": "Restore the exact staged preparation
    and its source-only numeric controls; retain gas proportions as gas-mixture specifications,
    vessel quantities as examples, and stock preparation separately. No transfer of
    a dependency parent-medium preparation.", "sources": [{"locator": "$.comments[0]",
    "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components and autoclave under a N2-CO2 (4:1, v/v)
    gas mixture. After cooling, add the following solutions (filter-sterilized):\"\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject":
    "Source preparation and controls 2", "local_fields": [], "decision": "add", "stage":
    "Source-only staged procedure", "interpretation": "Restore the exact staged preparation
    and its source-only numeric controls; retain gas proportions as gas-mixture specifications,
    vessel quantities as examples, and stock preparation separately. No transfer of
    a dependency parent-medium preparation. This includes50ml medium/120ml vessel
    as an example,4:1v/v atmosphere and explicit per-litre late additions.", "sources":
    [{"locator": "$.comments[1]", "source_key": "togo1233", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1233",
    "source_raw_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "source_text_sha256": "6768fd8fb716386b6ea0efc7b473513fa647f945e7639b0f00083fde9a03da9b",
    "accessed_at": "2026-10-28T18:10:04.335196Z", "exact_source_quote": "{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Aseptically and anaerobically distribute the medium into
    culture vessels (e.g., 50 ml of the medium in 120 ml serum bottle) under a N2-CO2
    (4:1,v/v) gas mixture, and seal with butyl rubber stoppers. Prior to use, add
    per liter the following solution (autoclaved and stored under a N2 atmosphere):\"\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject":
    "M180 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].composition[0].notes", "original": "Role: Solvating
    media; Properties: Inorganic compound, Defined component, Simple component [Merged
    3 duplicates: 990.0, 990.0, 1.0]\n\nSource water batch input: 990 ml = 0.99 L.
    This is not a measured final volume. Prior duplicate-collapse notes describe the
    superseded flattened record."}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].composition[0].concentration", "original": {"value":
    "0.99", "unit": "L"}}], "decision": "verified", "stage": "Scoped M180 iron stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[1].items[1]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[18]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "Distilled water\n990.0\nml",
    "quote_representation": "HTML tr[18] DOM text"}]}, {"decision_id": "q24", "subject":
    "M180 FeCl2・4H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].composition[1].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 iron stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[1].items[2]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[17]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "FeCl\n2\n·4H\n2\nO\n1.5\ng",
    "quote_representation": "HTML tr[17] DOM text"}]}, {"decision_id": "q25", "subject":
    "M180 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[0].notes", "original": "Role: Solvating
    media; Properties: Inorganic compound, Defined component, Simple component [Merged
    3 duplicates: 990.0, 990.0, 1.0]\n\nSource water batch input: 1 L = 1 L. This
    is not a measured final volume. Prior duplicate-collapse notes describe the superseded
    flattened record."}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[0].concentration", "original": {"value":
    "1", "unit": "L"}}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[0]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[26]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[26] DOM text"}]}, {"decision_id": "q26", "subject":
    "M180 Na2MoO4・2H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[1].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 36 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[1]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[25]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n36.0\nmg",
    "quote_representation": "HTML tr[25] DOM text"}]}, {"decision_id": "q27", "subject":
    "M180 H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[2].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 6 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[2]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[21]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "H\n3\nBO\n3\n6.0\nmg", "quote_representation":
    "HTML tr[21] DOM text"}]}, {"decision_id": "q28", "subject": "M180 MnCl2・4H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[3].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 100 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[3]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[20]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n100.0\nmg",
    "quote_representation": "HTML tr[20] DOM text"}]}, {"decision_id": "q29", "subject":
    "M180 CoCl2・6H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[4].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 190 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[4]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[22]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n190.0\nmg",
    "quote_representation": "HTML tr[22] DOM text"}]}, {"decision_id": "q30", "subject":
    "M180 NiCl2・6H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[5].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 24 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[5]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[24]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "NiCl\n2\n·6H\n2\nO\n24.0\nmg",
    "quote_representation": "HTML tr[24] DOM text"}]}, {"decision_id": "q31", "subject":
    "M180 CuCl2・2H2O", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[6].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[6]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[23]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "CuCl\n2\n·2H\n2\nO\n2.0\nmg",
    "quote_representation": "HTML tr[23] DOM text"}]}, {"decision_id": "q32", "subject":
    "M180 ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[7].notes", "original": "Role: Mineral
    source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 70 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}], "decision": "verified", "stage": "Scoped M180 trace stock",
    "interpretation": "Existing exact attached TOGO excerpts and raw digests authenticate
    this repaired stock field. Retain the explicit batch-water volume or source batch-mass
    note and absence of unsupported mass-per-litre concentration. Earlier duplicate
    notes are historical; parent doses and medium quantities do not transfer. Chemical
    supplied forms are assessed separately.", "sources": [{"locator": "$.components[2].items[7]",
    "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[19]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "ZnCl\n2\n70.0\nmg", "quote_representation":
    "HTML tr[19] DOM text"}]}, {"decision_id": "q33", "subject": "M180 nested HCl
    dose and explicit strength", "local_fields": [{"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].solutions[0].concentration", "original": {"value":
    "0.01", "unit": "L"}}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].solutions[0].notes", "original": "Source stock addition:
    10 ml = 0.01 L per receiving batch, not grams per liter or a dose per final liter."},
    {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].solutions[0].composition[0].concentration", "original":
    {"value": "7.7", "unit": "MOLAR"}}, {"record_path": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].solutions[0].composition[0].notes", "original": "Role:
    Solvating media; Properties: Defined component, Inorganic compound, Solution\n\nExplicit
    HCl reagent strength 7.7 M, not a final-medium concentration. The 25% basis is
    unspecified; the enclosing stock holds the 10 ml batch dose."}], "decision": "verified",
    "stage": "FeCl2 stock nested reagent", "interpretation": "Retain0.01L HCl batch
    dose and7.7M reagent strength; source25% basis remains unspecified. Both attached
    TOGO and JCM excerpts and the separately scoped root dose excerpt authenticate
    the current fields. This is not receiving-medium acid molarity.", "sources": [{"locator":
    "$.components[1].items[0]", "source_key": "togo180", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "source_text_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "accessed_at": "2026-10-28T18:06:52.466439Z", "exact_source_quote": "{\n          \"component_name\":
    \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
    25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\":
    \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "HTML tr[16]", "source_key": "jcm187", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187", "source_raw_sha256":
    "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "source_text_sha256":
    "646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f", "accessed_at":
    "2026-10-28T18:06:52.466627Z", "exact_source_quote": "25% HCl (7.7 M)\n10.0\nml",
    "quote_representation": "HTML tr[16] DOM text"}]}, {"decision_id": "q34", "subject":
    "M431 Se/W Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "989.0",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
    "field_path": "ingredients[11].notes", "original": "Role: Solvating media; Properties:
    Inorganic compound, Defined component, Simple component [Merged 3 duplicates:
    1.0, 987.0, 1.0]"}], "decision": "correct", "stage": "Scoped Se/W stock", "interpretation":
    "Only the Se/W stock is in scope. Restore its1L water batch separately; current989g/L
    is a flattened sum of unrelated parent/trace/SeW volumes, not a meaningful concentration.",
    "sources": [{"locator": "$.components[3].items[0]", "source_key": "togo431", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431", "source_raw_sha256":
    "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "source_text_sha256":
    "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "accessed_at":
    "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[32]", "source_key": "jcm431", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256":
    "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256":
    "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at":
    "2026-10-28T18:10:03.362170Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[32] DOM text"}, {"locator": "$.data.solutions[4].recipe[3]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q35", "subject": "M431 Se/W Na2SeO3・5H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
    "field_path": "ingredients[27].notes", "original": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped Se/W stock", "interpretation": "Only the Se/W stock is in scope.
    Source specifies mg of the stated hydrate, not the same-number g/L. Keep explicit
    stock batch mass and supplied form; no final-medium conversion.", "sources": [{"locator":
    "$.components[3].items[1]", "source_key": "togo431", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
    "source_raw_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570",
    "source_text_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570",
    "accessed_at": "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\":
    \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "HTML tr[30]", "source_key": "jcm431", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256":
    "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256":
    "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at":
    "2026-10-28T18:10:03.362170Z", "exact_source_quote": "Na\n2\nSeO\n3\n·5H\n2\nO\n6.0\nmg",
    "quote_representation": "HTML tr[30] DOM text"}, {"locator": "$.data.solutions[4].recipe[1]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0228125,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "M431 Se/W Na2WO4・2H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "8", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
    "field_path": "ingredients[28].notes", "original": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped Se/W stock", "interpretation": "Only the Se/W stock is in scope.
    Source specifies mg of the stated hydrate, not the same-number g/L. Keep explicit
    stock batch mass and supplied form; no final-medium conversion.", "sources": [{"locator":
    "$.components[3].items[2]", "source_key": "togo431", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
    "source_raw_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570",
    "source_text_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570",
    "accessed_at": "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\":
    \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "HTML tr[31]", "source_key": "jcm431", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431", "source_raw_sha256":
    "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50", "source_text_sha256":
    "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618", "accessed_at":
    "2026-10-28T18:10:03.362170Z", "exact_source_quote": "Na\n2\nWO\n4\n·2H\n2\nO\n8.0\nmg",
    "quote_representation": "HTML tr[31] DOM text"}, {"locator": "$.data.solutions[4].recipe[2]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 8,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.008,\n                        \"mmol_l\":
    0.0242534,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q37", "subject": "M431 Se/W NaOH", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path":
    "ingredients[29].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "field_path":
    "ingredients[29].notes", "original": "Properties: Defined component, Simple component,
    Inorganic compound"}], "decision": "correct", "stage": "Scoped Se/W stock", "interpretation":
    "Only the Se/W stock is in scope. Source 0.4 g NaOH is a stock batch mass; listed
    1 L water alone does not prove final volume. Current MediaDive4172 separately
    declares 0.4 g/L for the matching stock formula, which supports the provider-normalized
    stock basis. The local M431 ingredient remains flattened at the parent root, so
    that supported stock value does not validate its present receiving-medium placement.
    Restore the stock boundary while retaining the source amount and provider-basis
    credit; do not assert a measured final volume or parent-medium equivalence.",
    "sources": [{"locator": "$.components[3].items[3]", "source_key": "togo431", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431", "source_raw_sha256":
    "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "source_text_sha256":
    "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570", "accessed_at":
    "2026-10-28T18:10:03.362269Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\":
    \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[29]", "source_key":
    "jcm431", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
    "source_raw_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
    "source_text_sha256": "ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618",
    "accessed_at": "2026-10-28T18:10:03.362170Z", "exact_source_quote": "NaOH\n0.4\ng",
    "quote_representation": "HTML tr[29] DOM text"}, {"locator": "$.data.solutions[4].recipe[0]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\":
    10.0007,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q38", "subject": "M609 vitamin Distilled
    water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1003.0",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[0].notes", "original": "Role: Solvating media; Properties:
    Inorganic compound, Defined component, Simple component [Merged 6 duplicates:
    900.0, 1.0, 1.0, 50.0, 50.0, 1.0]"}], "decision": "correct", "stage": "Scoped
    M609 eight-vitamin stock", "interpretation": "Keep1L stock water separate from
    the flattened1003g/L aggregate of several unrelated M609 stages.", "sources":
    [{"locator": "$.components[7].items[0]", "source_key": "togo609", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609", "source_raw_sha256":
    "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "source_text_sha256":
    "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d", "accessed_at":
    "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[5].recipe[8]", "source_key": "apiJ1151",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1151", "source_raw_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "source_text_sha256":
    "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a", "accessed_at":
    "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[35]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[35] DOM text"}]}, {"decision_id": "q39", "subject":
    "M609 vitamin Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[23].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[1]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[0]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[27]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Biotin\n20.0\nmg", "quote_representation":
    "HTML tr[27] DOM text"}]}, {"decision_id": "q40", "subject": "M609 vitamin p--Aminobenzoic
    acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[24].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[2]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"p--Aminobenzoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[2]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.729182,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[29]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "p\n-Aminobenzoic acid\n100.0\nmg",
    "quote_representation": "HTML tr[29] DOM text"}]}, {"decision_id": "q41", "subject":
    "M609 vitamin Thiamine・HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[25].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[3]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 200,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[3]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[30]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602",
    "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac",
    "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d",
    "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Thiamine·HCl\n200.0\nmg",
    "quote_representation": "HTML tr[30] DOM text"}]}, {"decision_id": "q42", "subject":
    "M609 vitamin Pyridoxine・HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "500", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[26].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[4]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 500,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\":
    \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[5]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 500,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[32]", "source_key": "jcm602", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602",
    "source_raw_sha256": "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac",
    "source_text_sha256": "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d",
    "accessed_at": "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Pyridoxine·HCl\n500.0\nmg",
    "quote_representation": "HTML tr[32] DOM text"}]}, {"decision_id": "q43", "subject":
    "M609 vitamin Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[27].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[5]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
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
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[6]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[33]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Vitamin B\n1\n2\n100.0\nmg",
    "quote_representation": "HTML tr[33] DOM text"}]}, {"decision_id": "q44", "subject":
    "M609 vitamin Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[28].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[6]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\":
    \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[7]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.265675,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[34]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Riboflavin\n100.0\nmg",
    "quote_representation": "HTML tr[34] DOM text"}]}, {"decision_id": "q45", "subject":
    "M609 vitamin Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[29].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[7]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
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
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[1]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[28]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "Nicotinic acid\n200.0\nmg",
    "quote_representation": "HTML tr[28] DOM text"}]}, {"decision_id": "q46", "subject":
    "M609 vitamin DL--Calcium pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml",
    "field_path": "ingredients[30].notes", "original": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component"}], "decision": "correct",
    "stage": "Scoped M609 eight-vitamin stock", "interpretation": "Source provides
    this vitamin in mg per separate stock batch; the same-number G_PER_L field is
    wrong. MediaDive4460 independently declares its normalized stock g_l, which is
    not a receiving-medium concentration. Preserve exact supplied form, including
    D,L for calcium pantothenate; no generic-name equivalence.", "sources": [{"locator":
    "$.components[7].items[8]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n          \"component_name\":
    \"DL--Calcium pantothenate\",\n          \"volume\": 100,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001936\",\n          \"gmo_id\":
    \"GMO_001936\",\n          \"label\": \"DL-Calcium pantothenate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[4]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\":
    1720,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209864,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[31]", "source_key": "jcm602", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=602", "source_raw_sha256":
    "57f6d8c391aff519078abb7b0dc0448056c336fca2bd06bb1e460e384efec3ac", "source_text_sha256":
    "0e917eb4a032f13340617b7c3f9c8f0260c0f2c7068424a93990cb8b5ccc232d", "accessed_at":
    "2026-10-28T18:11:41.571473Z", "exact_source_quote": "DL-Calcium pantothenate\n100.0\nmg",
    "quote_representation": "HTML tr[31] DOM text"}]}, {"decision_id": "q47", "subject":
    "M609 vitamin filtration and atmosphere", "local_fields": [], "decision": "add",
    "stage": "Vitamin stock-only preparation", "interpretation": "Retain filter sterilization
    and N2storage from the vitamin subsection only. Exclude the parent-medium70kPa
    overpressure, receivingdose, pH and other stock instructions.", "sources": [{"locator":
    "$.comments[5]", "source_key": "togo609", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M609",
    "source_raw_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "source_text_sha256": "7a68ef3f4beadc929bd0e78527c5b0d991edfc08e98cf40a9a63083b99270d7d",
    "accessed_at": "2026-10-28T18:10:04.469853Z", "exact_source_quote": "{\n      \"paragraph_index\":
    14,\n      \"comment\": \"Filter--sterilize and store under a N2 atmosphere.\"\n    }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].steps[0]",
    "source_key": "apiJ1151", "reference": "https://mediadive.dsmz.de/rest/medium/J1151",
    "source_raw_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "source_text_sha256": "444bc2e01778a3fd45920e483e40ad5ec3b3def8138efb21d7f88748494c084a",
    "accessed_at": "2026-10-28T18:11:41.586030Z", "exact_source_quote": "{\n                        \"step\":
    \"Filter-sterilize and store under a N2 atmosphere.\"\n                    }",
    "quote_representation": "raw JSON object"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch074/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFOBACTERIUM_NAPHTHALENIVOLANS_MEDIUM.yaml:
    primary 13/13, secondary 9/13; data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml:
    primary 13/13, secondary 9/13. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - local0
- assessment_id: a8
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:007762
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-007762-batch-units-and-stock-boundaries
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Batch volumes, masses and stock stages are misrepresented
  description: The selected target and maintained owner preserve imported numbers
    but misrepresent water and liquid additions as mass concentrations. Stock-only
    ingredients are flattened into the main recipe where present, and mg inputs are
    represented by same-number g/L. Ordinary gram amounts have no verified final-volume
    basis; all unchanged and changed fields are enumerated in the inventory.
  target_ids:
  - CultureMech:007762
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - togo1233
  - jcm1151
  - apiJ1151
  rule_id: review-ingredient-concentrations/source-unit-and-stage-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-007762-missing-staged-preparation-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source procedures and claim evidence are absent from the selected layers
  description: Both selected layers lack the source staged preparation and attached
    formulation excerpts. Empty stock compositions and Unknown solution names obscure
    otherwise recoverable source stock identity. Gas placeholders are unquantified
    fields, while the source atmosphere, example vessel controls and sterilization
    sequence belong to preparation.
  target_ids:
  - CultureMech:007762
  field_paths:
  - preparation_steps
  - evidence
  - solutions
  evidence_ids:
  - togo1233
  - jcm1151
  rule_id: review-yaml-record/staged-preparation-and-claim-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-007762-linked-stock-hydrate-mapping
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: M180 trace-stock hydrate labels carry anhydrous identifiers
  description: Within the assessed M180 trace stock, cobalt chloride hexahydrate and
    nickel chloride hexahydrate retain anhydrous CHEBI35696 and34887. Current OLS
    formulas and masses omit hydrate water; native label validation and MIM mapped
    aliases do not prove source-form equivalence. The recent amount/preparation repair
    is credited and did not recertify these mappings.
  target_ids:
  - CultureMech:007762
  field_paths:
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - jcm187
  - togo180
  - chebi35696
  - chebi34887
  - grounding
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped iron and trace-stock dependency; parent-medium doses and formulation
      excluded
- finding_id: f4
  issue_key: culturemech-007762-sew-stock-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Linked Se/W stock remains flattened in its parent record
  description: The source-linked Se/W recipe is represented by empty solution composition
    and root ingredients with incorrect water/mg units. Only its four components and
    stock identity are in scope; the M431 receiving dose and unrelated parent/trace
    recipes are excluded.
  target_ids:
  - CultureMech:007762
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[11].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[27].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[28].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[29].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::solutions[1].composition
  evidence_ids:
  - jcm431
  - togo431
  rule_id: review-ingredient-concentrations/scoped-stock-boundary
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: selenite-tungstate stock only; parent recipe and receiving dose excluded
- finding_id: f5
  issue_key: culturemech-007762-vitamin-stock-identity-and-amounts
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Linked vitamin parent and provider stock are not equivalent
  description: M609 retains eight vitamin masses in wrong g/L units plus collapsed
    water, while its vitamin solution points to the different three-vitamin6241 formula.
    The exact JCM602 source and current TOGO609/MediaDive4460 establish the eight-component
    stock independently of that generic-name linkage. The primary JCM1151 page itself
    remains unavailable.
  target_ids:
  - CultureMech:007762
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[0].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[23].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[24].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[25].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[26].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[27].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[28].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[29].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::ingredients[30].concentration
  - data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml::solutions[3].term
  evidence_ids:
  - jcm602
  - togo609
  - stock6241
  - apiJ1151
  rule_id: review-yaml-record/source-stock-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml
    role: eight-vitamin stock only; parent medium, other stocks and receiving dose
      excluded
actions:
- action_id: action1
  description: Reconstruct the exact source batch and stock boundaries in the maintained
    owner. Preserve separate dose, stock composition, source water and preparation-stage
    evidence; replace unsupported concentration assertions with explicit batch notes
    or a source-declared provider basis where justified. Regenerate the target only
    after maintained input corrections.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007762
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
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
  description: Add the exact selected-source preparation with explicit stage-scoped
    root evidence, and fill or resolve the source-specific stock definitions without
    importing dependency parent-media instructions. Preserve unquantified gas placeholders
    and percentages with unknown basis. Do not invent pH or controls absent from the
    selected source.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007762
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1233_Desulfobacterium_Naphthalenivolans_Medium.yaml
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
  description: Resolve the exact supplied hydrate identities against authoritative
    ontology evidence or retain precise source labels as unresolved; preserve repaired
    source batch notes and all authentic attached evidence. Do not change unrelated
    M180 parent fields or use anhydrous molecular masses.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007762
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped iron and trace-stock dependency; parent-medium doses and formulation
      excluded
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Restore the separate Se/W source stock with its explicit batch inputs
    and source-form evidence, retaining unresolved final-volume basis. Scope any edit
    to this stock and preserve all unrelated M431 content.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007762
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: selenite-tungstate stock only; parent recipe and receiving dose excluded
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Restore the source-specific vitamin stock and correct its erroneous
    reference identity without rewriting standalone6241 merely to fit this receiving
    record. Preserve D,L-pantothenate source identity and unresolved legacy mapping;
    do not import parent pressure/pH/dose controls.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007762
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml
    role: eight-vitamin stock only; parent medium, other stocks and receiving dose
      excluded
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- No independent final-medium volume, density or bare-percent basis is established;
  source batch inputs, provider normalization and declared receiving bases remain
  distinct.
- Historical report and claim-byte matches do not authenticate historical tool execution
  or original access time. All old events must be preserved; any future correction
  should append current verified context.
- All dependency parents were read as context, but only explicitly enumerated stock
  fields are scientifically assessed. Parent doses, other stocks, pH and organism
  growth do not transfer.
- Current packaged MIM snapshot 6643131b0f12ab40b66f98135245fca04027e0e9 is a present
  identifier/label index, not a historical-validity certificate or supplied-form authority.
- Current exact JCM1151 returned HTTP200 with Nothing found. TOGO1233 and MediaDiveJ1151
  are provider evidence; no full current primary recipe was recovered. Earlier JCM615
  was an excluded preliminary lead; actual vitamin dependency is JCM602.
- Standalone6241 quantities and chemical mappings are comparison-only; its formula
  mismatch does not authorize rewriting the standalone record.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
