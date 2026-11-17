# Scientific review of caproiciproducens_medium

- Review: 20261028T065529Z-caproiciproducens-medium-batch059
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:48:44.450101Z
- Finished UTC: 2026-10-28T06:55:29.698342Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact source accession is supported, with a current title difference. Base provider rates are retained; water and five liquid doses have wrong units, preparation is missing, and cobalt hexahydrate is mapped to the anhydrous form.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch059 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007902 | data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml | generated | caproiciproducens_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007902 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:007902 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:007902 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:007902 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact accession with source-name distinction

identity: supported. Targets: CultureMech:007902.

TOGO M1364 explicitly points to JCM 1268; current JCM and MediaDive corroborate the same recipe despite differing current names. No named strain, taxonomic synonym or growth outcome is inferred from the title.

### Earlier reports and final-volume limits

evidence: concern. Targets: CultureMech:007902.

All three historical reports were read in full. Their water/dose/preparation concerns are supported, but the September assertion that summed input volumes establish final volume is not adopted as physical proof. Current API independently supplies the matching base g_l values. No claim-level source evidence is attached in the selected documents.

### Current writer responsibilities

provenance: supported. Targets: CultureMech:007902.

Current TOGO extraction preserves main paragraphs, stock descriptors and preparation comments; its bare-unit/percent mapping still needs source-basis review. The solution migration copies prior concentrations without validating their semantics. Correct magnesium primary/secondary mappings are credited. Present code and recorded history do not prove a particular historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:007902.

All 32 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007902", "selected_concentration_field_count": 32, "selected_concentration_fields_covered": 32, "decisions": [{"decision_id": "q1", "subject": "Base preparation water", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "645", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "645", "unit": "G_PER_L"}}], "decision": "correct", "stage": "basal solvent", "interpretation": "645 ml is the absolute source water input, not 645 g/L. The five later liquid additions total 355 ml; their sum with water is 1000 ml of listed inputs, not proof of measured final volume after dissolving solutes.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 645,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[9]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 645,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[9]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "Distilled water\n645.0\nml", "quote_representation": "HTML tr[9] DOM text"}]}, {"decision_id": "q2", "subject": "MgSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.1 g/L matching the local rate. API source amount is 0.1 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[1]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"MgSO4·7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[4]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n0.1\ng", "quote_representation": "HTML tr[4] DOM text"}]}, {"decision_id": "q3", "subject": "CaCl2·2H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.01 g/L matching the local rate. API source amount is 0.01 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[2]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0680203,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[6]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "CaCl\n2\n·2H\n2\nO\n0.01\ng", "quote_representation": "HTML tr[6] DOM text"}]}, {"decision_id": "q4", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.5 g/L matching the local rate. API source amount is 0.5 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[3]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.67415,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "KH\n2\nPO\n4\n0.5\ng", "quote_representation": "HTML tr[2] DOM text"}]}, {"decision_id": "q5", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 1 g/L matching the local rate. API source amount is 1 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[4]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[1]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "K\n2\nHPO\n4\n1.0\ng", "quote_representation": "HTML tr[1] DOM text"}]}, {"decision_id": "q6", "subject": "FeSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.015", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.015", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.015 g/L matching the local rate. API source amount is 0.015 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[5]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"FeSO4·7H2O\",\n          \"volume\": 0.015,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.015,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.015,\n                        \"mmol_l\": 0.0539539,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "FeSO\n4\n·7H\n2\nO\n0.015\ng", "quote_representation": "HTML tr[3] DOM text"}]}, {"decision_id": "q7", "subject": "CoCl2·6H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.002 g/L matching the local rate. API source amount is 2 mg. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[6]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 0.002,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[8]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0154037,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[8]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n0.002\ng", "quote_representation": "HTML tr[8] DOM text"}]}, {"decision_id": "q8", "subject": "ZnSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.002 g/L matching the local rate. API source amount is 2 mg. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[7]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"ZnSO4·7H2O\",\n          \"volume\": 0.002,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00695505,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[7]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "ZnSO\n4\n·7H\n2\nO\n0.002\ng", "quote_representation": "HTML tr[7] DOM text"}]}, {"decision_id": "q9", "subject": "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 2 g/L matching the local rate. API source amount is 2 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. The stated supplied form remains significant; cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[8]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"(NH4)2SO4\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\": \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 15.1355,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "(NH\n4\n)\n2\nSO\n4\n2.0\ng", "quote_representation": "HTML tr[0] DOM text"}]}, {"decision_id": "q10", "subject": "MnSO4·xH2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API explicitly declares 0.01 g/L matching the local rate. API source amount is 0.01 g. Preserve the explicit provider normalization without claiming that summing liquid inputs proves a measured final denominator. Mn sulfate has unspecified x/n hydration; no exact molecular weight or hydrate is inferred.", "sources": [{"locator": "$.components[0].items[9]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"MnSO4·xH2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[5]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "MnSO\n4\n·xH\n2\nO\n0.01\ng", "quote_representation": "HTML tr[5] DOM text"}]}, {"decision_id": "q11", "subject": "Nitrogen", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "correct", "stage": "basal sterilization atmosphere", "interpretation": "The source assigns N2 to the autoclave atmosphere. It gives no dissolved-gas mass or concentration; preserve atmospheric context instead of a generic variable ingredient.", "sources": [{"locator": "$.components[0].items[10]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[0]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly and adjust pH to 6.5. Autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved):\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "10% Yeast extract solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling stock addition", "interpretation": "Restore 100 ml absolute dose rather than the same number in G_PER_L. Keep source stock strength separate from working dose, correct the Unknown solution placeholder, and preserve unresolved stock-preparation details. The bare 10% basis is unspecified; do not assume w/v, w/w or v/v or derive grams.", "sources": [{"locator": "$.components[1].items[0]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"10% Yeast extract solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001292\",\n          \"gmo_id\": \"GMO_001292\",\n          \"label\": \"Yeast extract solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"10%\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[10]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "10% Yeast extract solution\n100.0\nml", "quote_representation": "HTML tr[10] DOM text"}]}, {"decision_id": "q13", "subject": "1.0 M Sodium acetate solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling stock addition", "interpretation": "Restore 20 ml absolute dose rather than the same number in G_PER_L. Keep source stock strength separate from working dose, correct the Unknown solution placeholder, and preserve unresolved stock-preparation details. The 1.0 M stock supplies 0.02 mol to the batch; this is moles per batch, not a final molarity.", "sources": [{"locator": "$.components[1].items[1]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"1.0 M Sodium acetate solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001415\",\n          \"gmo_id\": \"GMO_001415\",\n          \"label\": \"Sodium acetate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[13]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\": 731,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[13]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "1.0 M Sodium acetate solution\n20.0\nml", "quote_representation": "HTML tr[13] DOM text"}]}, {"decision_id": "q14", "subject": "1.0 M Glucose solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling stock addition", "interpretation": "Restore 100 ml absolute dose rather than the same number in G_PER_L. Keep source stock strength separate from working dose, correct the Unknown solution placeholder, and preserve unresolved stock-preparation details. The 1.0 M stock supplies 0.1 mol to the batch; this is moles per batch, not a final molarity.", "sources": [{"locator": "$.components[1].items[2]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"1.0 M Glucose solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001465\",\n          \"gmo_id\": \"GMO_001465\",\n          \"label\": \"Glucose solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[12]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[12]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "1.0 M Glucose solution\n100.0\nml", "quote_representation": "HTML tr[12] DOM text"}]}, {"decision_id": "q15", "subject": "1.0 M sodium butyrate solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[3].concentration", "original": {"value": "35", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "solutions[3].concentration", "original": {"value": "35", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling stock addition", "interpretation": "Restore 35 ml absolute dose rather than the same number in G_PER_L. Keep source stock strength separate from working dose, correct the Unknown solution placeholder, and preserve unresolved stock-preparation details. The 1.0 M stock supplies 0.035 mol to the batch; this is moles per batch, not a final molarity.", "sources": [{"locator": "$.components[1].items[3]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"1.0 M sodium butyrate solution\",\n          \"volume\": 35,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001473\",\n          \"gmo_id\": \"GMO_001473\",\n          \"label\": \"Sodium butyrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[14]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Sodium butyrate\",\n                        \"compound_id\": 1750,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\": 35,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[14]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "1.0 M sodium butyrate solution\n35.0\nml", "quote_representation": "HTML tr[14] DOM text"}]}, {"decision_id": "q16", "subject": "10% Tryptone solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[4].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml", "field_path": "solutions[4].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling stock addition", "interpretation": "Restore 100 ml absolute dose rather than the same number in G_PER_L. Keep source stock strength separate from working dose, correct the Unknown solution placeholder, and preserve unresolved stock-preparation details. The bare 10% basis is unspecified; do not assume w/v, w/w or v/v or derive grams.", "sources": [{"locator": "$.components[1].items[4]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\": \"10% Tryptone solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001737\",\n          \"gmo_id\": \"GMO_001737\",\n          \"label\": \"Bacto &amp;trade; Tryptone solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"10%\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[11]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "10% Tryptone solution\n100.0\nml", "quote_representation": "HTML tr[11] DOM text"}]}, {"decision_id": "q17", "subject": "Main pH and preparation sequence", "local_fields": [], "decision": "evidence_only", "stage": "basal and later sterile stages", "interpretation": "The source prescribes pH 6.5, N2 autoclaving, cooling, then aseptic anaerobic addition of the separately autoclaved solutions. Preserve sequence and source scope; no cooling endpoint or stock-preparation recipe is invented.", "sources": [{"locator": "$.comments[0]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly and adjust pH to 6.5. Autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved):\"\n    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"step\": \"Mix components thoroughly and adjust pH to 6.5. Autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved): \"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "Source default sterilization", "local_fields": [], "decision": "evidence_only", "stage": "JCM source-wide default", "interpretation": "Retain JCM default121°C15 min unless otherwise stated, separately from the exact N2 and post-cooling instructions. Do not apply it to an unrelated medium.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "Subculture preheating", "local_fields": [], "decision": "evidence_only", "stage": "source-prescribed pre-use condition", "interpretation": "The current JCM and TOGO comment specifies preheating medium to 37°C for subculturing. This is not a general optimum growth temperature or a strain-specific experimental result.", "sources": [{"locator": "$.comments[1]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n      \"paragraph_index\": 4,\n      \"comment\": \"Comment: For subculturing, preheat the medium to 37C.\"\n    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 89-89", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "Comment: For subculturing, preheat the medium to 37C.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch059/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:007902.

data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml: primary 10/11, secondary 7/11; data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml: primary 10/11, secondary 7/11. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:007902.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:007902.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Water and five stock doses are recorded as mass concentrations

major / open / confirmed; issue key: culturemech-007902-absolute-water-and-stock-dose-units.

645 ml base water and five later additions of 100,20,100,35,100 ml are encoded as G_PER_L. Stock compositions are empty and names use Unknown solution despite meaningful preferred terms. Current API explicitly supports the nine base-compound rates; those values need no numerical correction. The three 1.0 M strengths and two bare 10% labels must remain separate from dose and final concentration.

### f2: pH and stage-specific preparation are missing

major / open / confirmed; issue key: culturemech-007902-missing-ph-and-staged-anaerobic-preparation.

Both selected layers omit pH 6.5 and all preparation. N2 remains a variable ingredient rather than an autoclave atmosphere. The sources state cooling before anaerobic aseptic stock additions and a separate 37°C preheating note; the JCM default sterilization is also available.

### f3: Cobalt hexahydrate uses an anhydrous primary term

major / open / confirmed; issue key: culturemech-007902-cobalt-hexahydrate-primary-form.

The source and local label explicitly name CoCl2·6H2O, but primary CHEBI:35696 is cobalt dichloride with formula 2Cl.Co. Current OLS CHEBI:53503 explicitly represents the hexahydrate. There is no cobalt secondary assertion to correct. Correct magnesium, calcium, iron and zinc hydrate groundings are retained; unspecified MnSO4·xH2O should remain unresolved rather than forced to a specific hydrate.

### f4: The current JCM title differs from the imported source name

minor / open / confirmed; issue key: culturemech-007902-source-name-version-provenance.

The exact JCM 1268 accession now says CAPROICIBACTERIUM MEDIUM, while TOGO M1364 and current MediaDive J1268 retain CAPROICIPRODUCENS MEDIUM. Formulation rows and source links correspond; this is a naming/version distinction, not proof the target denotes a different recipe.

## Recommended Actions And Acceptance Checks

### action1

Represent source water and absolute stock additions in their preparation stages, preserve known molar strengths and unresolved percent basis, and replace placeholders with exact source labels. Attach stock-dose evidence to enclosing root evidence with the full solution field path; do not invent an evidence slot on SolutionDescriptor.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Add the exact source preparation with root evidence scoped to pH, gas, sterilization, cooling/addition order and subculture preheat. Retain unquantified details as unresolved instead of supplying standard assumptions.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the cobalt supplied form using the verified hexahydrate correspondence without changing supported source mass. Independently verify any newly proposed secondary linkage. Do not adopt provider mmol_l based on anhydrous cobalt mass.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Preserve source accession and imported name, document the current title with capture date, and verify any biological synonym claim separately. Keep original history unchanged and append actual corrective context only when curated.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch059/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch059/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch059/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch059/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm1268 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current official JCM page read, including the main and embedded stock tables, preparation and source-specific defaults. The page-wide default remains scoped to that source; named stock sections are separate from main-medium preparation. |
| togoM1364 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt salt in which the cobalt metal is in the +2 oxidation state and the counter-anion is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co']; mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used).']; formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| apiJ1268 | https://mediadive.dsmz.de/rest/medium/J1268; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| grounding | REVIEW_WORK/batch059/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T033913Z-CAPROICIPRODUCENS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch059/record05/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer26 | scripts/migrate_mgso4_heptahydrate_term.py; relevant functions named in summary | context_only | iter_ingredients and main make a label-conditional primary-term-only 32599 to 31795 repair; secondary annotations are untouched. The current magnesium primary and secondary are both correct here; this writer alone does not authenticate other forms or amounts. |
| writer27 | scripts/migrate_solutions_from_ingredients.py; relevant functions named in summary | context_only | Current _resolve_solution copies an existing concentration unchanged into a referenced or empty stock descriptor; _migrate_media_file moves matched names into solutions and appends history. It does not validate dose units, populate missing source composition or prove historical execution. |
| writer28 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer29 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer30 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer31 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch059/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- No measured final volume is inferred from 645+355 ml of listed liquid inputs. Base provider g_l is explicitly labeled normalization, not physical volume proof.
- The two 10% stock labels do not state percent basis, and stock preparation recipes are not supplied. No grams or final concentrations are invented.
- Current naming differences are not evidence of organism taxonomy or experimentally observed growth; source-specific preparation guidance is not optimization.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T065529Z-caproiciproducens-medium-batch059
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of caproiciproducens_medium
started_at: '2026-10-28T06:48:44.450101Z'
finished_at: '2026-10-28T06:55:29.698342Z'
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
summary: The exact source accession is supported, with a current title difference.
  Base provider rates are retained; water and five liquid doses have wrong units,
  preparation is missing, and cobalt hexahydrate is mapped to the anhydrous form.
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
  - path: data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
    sha256: 49afb6a301ea749ab0ac3ab23ee06dd8b92ac168609bb5d110ce0c81a3514a0d
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
    sha256: ba065c89fc0b0b913015cf069b0cbfe7eb42352b8e96ea87514f0f0fbbc92108
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.md
    sha256: 4ca57ac1f5ec66b1215ed65404f7e4d66611b926ca292338d603ed692f4b35d8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.md
    sha256: 6e8429a4bc5750659500383b4e65735c9130c3747337987d264b902c43e6b1a5
    role: context
  - path: reports/yaml_record_review/20260922T033913Z-CAPROICIPRODUCENS_MEDIUM.md
    sha256: 5d77f896727b26bbb8d7f35f3703521b8935dc9691512af55c26b2bb55616f45
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
  selection: Authoritative batch059 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007902
targets:
- target_id: CultureMech:007902
  path: data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
  label: caproiciproducens_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007902
  command: just validate-schema data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007902
  command: just validate-strict data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch059/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007902
  command: just validate-terms data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:007902
  command: just validate-references data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T06:55:29.688781Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 49afb6a301ea749ab0ac3ab23ee06dd8b92ac168609bb5d110ce0c81a3514a0d
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T06:55:29.688955Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: ba065c89fc0b0b913015cf069b0cbfe7eb42352b8e96ea87514f0f0fbbc92108
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:45.534891Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 9512cef69c41062fda392e7726e5f9c64aa2caa72927d8a72259a5dc060de6f4
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:46.535796Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 026b93ed01f36258bba77ea4aa405b8a5616edbe03f65c93278ae419c9eb800b
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:47.638082Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 2eeaa16998d31283993896f3ed202f92d1c65870870210ac8f7c93d2c47b124f
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch059/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:48.351117Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 533d7a0e4d4f82001feeec41e4653ddf2c0c6f4bae0650f21aba1c3cc9b6aa2d
- evidence_id: jcm1268
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:24.427953Z'
  support: supports
  summary: Complete current official JCM page read, including the main and embedded
    stock tables, preparation and source-specific defaults. The page-wide default
    remains scoped to that source; named stock sections are separate from main-medium
    preparation.
  snapshot_sha256: 2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3
- evidence_id: togoM1364
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:24.485672Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:24.529738Z'
  support: supports
  summary: OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition
    ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula
    ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:24.530183Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:24.556332Z'
  support: supports
  summary: OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule
    consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:24.579360Z'
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
  accessed_at: '2026-10-28T06:49:24.992236Z'
  support: supports
  summary: OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A
    hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn'];
    mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:25.141505Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:25.149679Z'
  support: supports
  summary: OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt
    salt in which the cobalt metal is in the +2 oxidation state and the counter-anion
    is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co'];
    mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:25.163177Z'
  support: supports
  summary: OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic
    sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia.
    A high-melting (decomposes above 280°C) white solid which is very soluble in water
    (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as
    a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:25.193117Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:25.249096Z'
  support: supports
  summary: OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a
    source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage
    treatments; for solid-dosage treatments, the monohydrate is normally used).'];
    formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:25.595972Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:27.997179Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: apiJ1268
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1268
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:53:29.708702Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch059/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T06:55:29.691398Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 82d8363f0235d1ffa3842a77bafea7f2f067b1abbc36855125859cfd1ce6a795
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T033913Z-CAPROICIPRODUCENS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:55:29.691736Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 5d77f896727b26bbb8d7f35f3703521b8935dc9691512af55c26b2bb55616f45
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:55:29.691757Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 6e8429a4bc5750659500383b4e65735c9130c3747337987d264b902c43e6b1a5
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:55:29.691778Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 4ca57ac1f5ec66b1215ed65404f7e4d66611b926ca292338d603ed692f4b35d8
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch059/record05/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T06:55:29.691797Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 28cd77d3a2f843beeb36f66f347103e468b99049490702932162775a93f58829
- evidence_id: writer26
  kind: record_content
  reference: scripts/migrate_mgso4_heptahydrate_term.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:55:29.691815Z'
  support: context_only
  summary: iter_ingredients and main make a label-conditional primary-term-only 32599
    to 31795 repair; secondary annotations are untouched. The current magnesium primary
    and secondary are both correct here; this writer alone does not authenticate other
    forms or amounts.
  snapshot_sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
- evidence_id: writer27
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:55:29.691834Z'
  support: context_only
  summary: Current _resolve_solution copies an existing concentration unchanged into
    a referenced or empty stock descriptor; _migrate_media_file moves matched names
    into solutions and appends history. It does not validate dose units, populate
    missing source composition or prove historical execution.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer28
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:55:29.691862Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer29
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:55:29.691878Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer30
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:55:29.691896Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer31
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:55:29.691914Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch059/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T06:55:29.698142Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 3a60246cb5a4f20408860efa9c6e92a9b77ef004b95cf1f5ba10b3813409978f
assessments:
- assessment_id: a1
  area: identity
  topic: Exact accession with source-name distinction
  outcome: supported
  summary: TOGO M1364 explicitly points to JCM 1268; current JCM and MediaDive corroborate
    the same recipe despite differing current names. No named strain, taxonomic synonym
    or growth outcome is inferred from the title.
  target_ids:
  - CultureMech:007902
  evidence_ids:
  - jcm1268
  - apiJ1268
  - togoM1364
- assessment_id: a2
  area: evidence
  topic: Earlier reports and final-volume limits
  outcome: concern
  summary: All three historical reports were read in full. Their water/dose/preparation
    concerns are supported, but the September assertion that summed input volumes
    establish final volume is not adopted as physical proof. Current API independently
    supplies the matching base g_l values. No claim-level source evidence is attached
    in the selected documents.
  target_ids:
  - CultureMech:007902
  evidence_ids:
  - history-auth
  - jcm1268
  - apiJ1268
- assessment_id: a3
  area: provenance
  topic: Current writer responsibilities
  outcome: supported
  summary: Current TOGO extraction preserves main paragraphs, stock descriptors and
    preparation comments; its bare-unit/percent mapping still needs source-basis review.
    The solution migration copies prior concentrations without validating their semantics.
    Correct magnesium primary/secondary mappings are credited. Present code and recorded
    history do not prove a particular historical execution.
  target_ids:
  - CultureMech:007902
  evidence_ids:
  - local0
  - writer26
  - writer27
  - writer28
  - writer29
  - writer30
  - writer31
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 32 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:007902
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007902",
    "selected_concentration_field_count": 32, "selected_concentration_fields_covered":
    32, "decisions": [{"decision_id": "q1", "subject": "Base preparation water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "645", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "645", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "basal solvent", "interpretation":
    "645 ml is the absolute source water input, not 645 g/L. The five later liquid
    additions total 355 ml; their sum with water is 1000 ml of listed inputs, not
    proof of measured final volume after dissolving solutes.", "sources": [{"locator":
    "$.components[0].items[0]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 645,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[9]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 645,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[9]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "Distilled water\n645.0\nml",
    "quote_representation": "HTML tr[9] DOM text"}]}, {"decision_id": "q2", "subject":
    "MgSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.1 g/L matching the local rate. API source amount is 0.1
    g. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. The stated supplied form remains
    significant; cobalt mapping is assessed separately.", "sources": [{"locator":
    "$.components[0].items[1]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgSO4·7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.405719,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[4]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n0.1\ng",
    "quote_representation": "HTML tr[4] DOM text"}]}, {"decision_id": "q3", "subject":
    "CaCl2·2H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.01 g/L matching the local rate. API source amount is 0.01
    g. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. The stated supplied form remains
    significant; cobalt mapping is assessed separately.", "sources": [{"locator":
    "$.components[0].items[2]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"CaCl2·2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0680203,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[6]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "CaCl\n2\n·2H\n2\nO\n0.01\ng",
    "quote_representation": "HTML tr[6] DOM text"}]}, {"decision_id": "q4", "subject":
    "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.5 g/L matching the local rate. API source amount is 0.5
    g. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. The stated supplied form remains
    significant; cobalt mapping is assessed separately.", "sources": [{"locator":
    "$.components[0].items[3]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268",
    "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    3.67415,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "KH\n2\nPO\n4\n0.5\ng", "quote_representation":
    "HTML tr[2] DOM text"}]}, {"decision_id": "q5", "subject": "K2HPO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 1 g/L matching the local rate. API source amount is 1 g. Preserve
    the explicit provider normalization without claiming that summing liquid inputs
    proves a measured final denominator. The stated supplied form remains significant;
    cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[4]",
    "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.74132,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[1]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "K\n2\nHPO\n4\n1.0\ng", "quote_representation":
    "HTML tr[1] DOM text"}]}, {"decision_id": "q6", "subject": "FeSO4·7H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.015", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.015", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.015 g/L matching the local rate. API source amount is 0.015
    g. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. The stated supplied form remains
    significant; cobalt mapping is assessed separately.", "sources": [{"locator":
    "$.components[0].items[5]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"FeSO4·7H2O\",\n          \"volume\": 0.015,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key":
    "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.015,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.015,\n                        \"mmol_l\":
    0.0539539,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "FeSO\n4\n·7H\n2\nO\n0.015\ng",
    "quote_representation": "HTML tr[3] DOM text"}]}, {"decision_id": "q7", "subject":
    "CoCl2·6H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.002", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.002", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.002 g/L matching the local rate. API source amount is 2
    mg. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. The stated supplied form remains
    significant; cobalt mapping is assessed separately.", "sources": [{"locator":
    "$.components[0].items[6]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"CoCl2·6H2O\",\n          \"volume\": 0.002,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[8]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0154037,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[8]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n0.002\ng",
    "quote_representation": "HTML tr[8] DOM text"}]}, {"decision_id": "q8", "subject":
    "ZnSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.002", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.002", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.002 g/L matching the local rate. API source amount is 2
    mg. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. The stated supplied form remains
    significant; cobalt mapping is assessed separately.", "sources": [{"locator":
    "$.components[0].items[7]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"ZnSO4·7H2O\",\n          \"volume\": 0.002,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key":
    "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00695505,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[7]", "source_key":
    "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "ZnSO\n4\n·7H\n2\nO\n0.002\ng",
    "quote_representation": "HTML tr[7] DOM text"}]}, {"decision_id": "q9", "subject":
    "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 2 g/L matching the local rate. API source amount is 2 g. Preserve
    the explicit provider normalization without claiming that summing liquid inputs
    proves a measured final denominator. The stated supplied form remains significant;
    cobalt mapping is assessed separately.", "sources": [{"locator": "$.components[0].items[8]",
    "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\":
    \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    15.1355,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm1268", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "(NH\n4\n)\n2\nSO\n4\n2.0\ng",
    "quote_representation": "HTML tr[0] DOM text"}]}, {"decision_id": "q10", "subject":
    "MnSO4·xH2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and provider-declared
    rate", "interpretation": "JCM and TOGO preserve this batch mass, and current API
    explicitly declares 0.01 g/L matching the local rate. API source amount is 0.01
    g. Preserve the explicit provider normalization without claiming that summing
    liquid inputs proves a measured final denominator. Mn sulfate has unspecified
    x/n hydration; no exact molecular weight or hydrate is inferred.", "sources":
    [{"locator": "$.components[0].items[9]", "source_key": "togoM1364", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364", "source_raw_sha256":
    "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "source_text_sha256":
    "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5", "accessed_at":
    "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"MnSO4·xH2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\":
    \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\":
    1000,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[5]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "MnSO\n4\n·xH\n2\nO\n0.01\ng",
    "quote_representation": "HTML tr[5] DOM text"}]}, {"decision_id": "q11", "subject":
    "Nitrogen", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "correct", "stage": "basal sterilization atmosphere",
    "interpretation": "The source assigns N2 to the autoclave atmosphere. It gives
    no dissolved-gas mass or concentration; preserve atmospheric context instead of
    a generic variable ingredient.", "sources": [{"locator": "$.components[0].items[10]",
    "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[0]",
    "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly and adjust pH to 6.5. Autoclave
    under a N2 atmosphere. After cooling, aseptically and anaerobically add the following
    solutions (autoclaved):\"\n    }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q12", "subject": "10% Yeast extract solution", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path":
    "solutions[0].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling
    stock addition", "interpretation": "Restore 100 ml absolute dose rather than the
    same number in G_PER_L. Keep source stock strength separate from working dose,
    correct the Unknown solution placeholder, and preserve unresolved stock-preparation
    details. The bare 10% basis is unspecified; do not assume w/v, w/w or v/v or derive
    grams.", "sources": [{"locator": "$.components[1].items[0]", "source_key": "togoM1364",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"10% Yeast extract solution\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001292\",\n          \"gmo_id\": \"GMO_001292\",\n          \"label\":
    \"Yeast extract solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key":
    "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"10%\",\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[10]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "10% Yeast
    extract solution\n100.0\nml", "quote_representation": "HTML tr[10] DOM text"}]},
    {"decision_id": "q13", "subject": "1.0 M Sodium acetate solution", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path":
    "solutions[1].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling
    stock addition", "interpretation": "Restore 20 ml absolute dose rather than the
    same number in G_PER_L. Keep source stock strength separate from working dose,
    correct the Unknown solution placeholder, and preserve unresolved stock-preparation
    details. The 1.0 M stock supplies 0.02 mol to the batch; this is moles per batch,
    not a final molarity.", "sources": [{"locator": "$.components[1].items[1]", "source_key":
    "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"1.0 M Sodium acetate solution\",\n          \"volume\": 20,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001415\",\n          \"gmo_id\": \"GMO_001415\",\n          \"label\":
    \"Sodium acetate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\":
    \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[13]", "source_key": "apiJ1268",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\":
    731,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[13]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "1.0 M Sodium
    acetate solution\n20.0\nml", "quote_representation": "HTML tr[13] DOM text"}]},
    {"decision_id": "q14", "subject": "1.0 M Glucose solution", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[2].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling
    stock addition", "interpretation": "Restore 100 ml absolute dose rather than the
    same number in G_PER_L. Keep source stock strength separate from working dose,
    correct the Unknown solution placeholder, and preserve unresolved stock-preparation
    details. The 1.0 M stock supplies 0.1 mol to the batch; this is moles per batch,
    not a final molarity.", "sources": [{"locator": "$.components[1].items[2]", "source_key":
    "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"1.0 M Glucose solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\":
    1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001465\",\n          \"gmo_id\":
    \"GMO_001465\",\n          \"label\": \"Glucose solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[12]", "source_key":
    "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "source_text_sha256":
    "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9", "accessed_at":
    "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[12]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "1.0 M Glucose
    solution\n100.0\nml", "quote_representation": "HTML tr[12] DOM text"}]}, {"decision_id":
    "q15", "subject": "1.0 M sodium butyrate solution", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[3].concentration",
    "original": {"value": "35", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "solutions[3].concentration", "original": {"value": "35", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling
    stock addition", "interpretation": "Restore 35 ml absolute dose rather than the
    same number in G_PER_L. Keep source stock strength separate from working dose,
    correct the Unknown solution placeholder, and preserve unresolved stock-preparation
    details. The 1.0 M stock supplies 0.035 mol to the batch; this is moles per batch,
    not a final molarity.", "sources": [{"locator": "$.components[1].items[3]", "source_key":
    "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"1.0 M sodium butyrate solution\",\n          \"volume\": 35,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001473\",\n          \"gmo_id\": \"GMO_001473\",\n          \"label\":
    \"Sodium butyrate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[14]",
    "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268",
    "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Sodium butyrate\",\n                        \"compound_id\":
    1750,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\":
    35,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[14]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "1.0 M sodium
    butyrate solution\n35.0\nml", "quote_representation": "HTML tr[14] DOM text"}]},
    {"decision_id": "q16", "subject": "10% Tryptone solution", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml", "field_path": "solutions[4].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml",
    "field_path": "solutions[4].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separately prepared post-cooling
    stock addition", "interpretation": "Restore 100 ml absolute dose rather than the
    same number in G_PER_L. Keep source stock strength separate from working dose,
    correct the Unknown solution placeholder, and preserve unresolved stock-preparation
    details. The bare 10% basis is unspecified; do not assume w/v, w/w or v/v or derive
    grams.", "sources": [{"locator": "$.components[1].items[4]", "source_key": "togoM1364",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n          \"component_name\":
    \"10% Tryptone solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\":
    10,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001737\",\n          \"gmo_id\":
    \"GMO_001737\",\n          \"label\": \"Bacto &trade; Tryptone solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]",
    "source_key": "apiJ1268", "reference": "https://mediadive.dsmz.de/rest/medium/J1268",
    "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\":
    71,\n                        \"attribute\": \"10%\",\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[11]", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "10% Tryptone
    solution\n100.0\nml", "quote_representation": "HTML tr[11] DOM text"}]}, {"decision_id":
    "q17", "subject": "Main pH and preparation sequence", "local_fields": [], "decision":
    "evidence_only", "stage": "basal and later sterile stages", "interpretation":
    "The source prescribes pH 6.5, N2 autoclaving, cooling, then aseptic anaerobic
    addition of the separately autoclaved solutions. Preserve sequence and source
    scope; no cooling endpoint or stock-preparation recipe is invented.", "sources":
    [{"locator": "$.comments[0]", "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly and adjust pH to 6.5. Autoclave
    under a N2 atmosphere. After cooling, aseptically and anaerobically add the following
    solutions (autoclaved):\"\n    }", "quote_representation": "raw JSON object"},
    {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1268", "reference":
    "https://mediadive.dsmz.de/rest/medium/J1268", "source_raw_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "source_text_sha256": "0825598490494bdd2b33c03a80e8bf6ced2ab9c429ca2eff585d9004b4216ee9",
    "accessed_at": "2026-10-28T06:53:29.708702Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"step\": \"Mix components thoroughly and adjust
    pH to 6.5. Autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically
    add the following solutions (autoclaved): \"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "Source default sterilization",
    "local_fields": [], "decision": "evidence_only", "stage": "JCM source-wide default",
    "interpretation": "Retain JCM default121°C15 min unless otherwise stated, separately
    from the exact N2 and post-cooling instructions. Do not apply it to an unrelated
    medium.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "jcm1268",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268", "source_raw_sha256":
    "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3", "source_text_sha256":
    "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514", "accessed_at":
    "2026-10-28T06:49:24.427953Z", "exact_source_quote": "Unless otherwise stated,
    sterilize media by autoclaving at 121°C for 15 min.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q19", "subject": "Subculture preheating",
    "local_fields": [], "decision": "evidence_only", "stage": "source-prescribed pre-use
    condition", "interpretation": "The current JCM and TOGO comment specifies preheating
    medium to 37°C for subculturing. This is not a general optimum growth temperature
    or a strain-specific experimental result.", "sources": [{"locator": "$.comments[1]",
    "source_key": "togoM1364", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1364",
    "source_raw_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "source_text_sha256": "a90725d5e248f08815184ceca772b1dfd52199084e742ccff4645aa9cc8916d5",
    "accessed_at": "2026-10-28T06:49:24.485672Z", "exact_source_quote": "{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Comment: For subculturing, preheat the medium to 37C.\"\n    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    89-89", "source_key": "jcm1268", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1268",
    "source_raw_sha256": "2114b023e459fdbf58372a6c1dc3ccb08e9d7add3f43039477d5bf02c9e428a3",
    "source_text_sha256": "f50073a4441dd5ea3da812592fef50693fb4814b5e1c8520250959dc0b185514",
    "accessed_at": "2026-10-28T06:49:24.427953Z", "exact_source_quote": "Comment:
    For subculturing, preheat the medium to 37C.", "quote_representation": "captured
    extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch059/record05/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CAPROICIPRODUCENS_MEDIUM.yaml: primary 10/11, secondary
    7/11; data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml:
    primary 10/11, secondary 7/11. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:007902
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
  - CultureMech:007902
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
  - CultureMech:007902
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-007902-absolute-water-and-stock-dose-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and five stock doses are recorded as mass concentrations
  description: 645 ml base water and five later additions of 100,20,100,35,100 ml
    are encoded as G_PER_L. Stock compositions are empty and names use Unknown solution
    despite meaningful preferred terms. Current API explicitly supports the nine base-compound
    rates; those values need no numerical correction. The three 1.0 M strengths and
    two bare 10% labels must remain separate from dose and final concentration.
  target_ids:
  - CultureMech:007902
  field_paths:
  - ingredients[0].concentration
  - solutions
  evidence_ids:
  - jcm1268
  - togoM1364
  - apiJ1268
  rule_id: source-quantity-stage-and-unit-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-007902-missing-ph-and-staged-anaerobic-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: pH and stage-specific preparation are missing
  description: Both selected layers omit pH 6.5 and all preparation. N2 remains a
    variable ingredient rather than an autoclave atmosphere. The sources state cooling
    before anaerobic aseptic stock additions and a separate 37°C preheating note;
    the JCM default sterilization is also available.
  target_ids:
  - CultureMech:007902
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[10]
  - evidence
  evidence_ids:
  - jcm1268
  - togoM1364
  - apiJ1268
  rule_id: source-preparation-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-007902-cobalt-hexahydrate-primary-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Cobalt hexahydrate uses an anhydrous primary term
  description: The source and local label explicitly name CoCl2·6H2O, but primary
    CHEBI:35696 is cobalt dichloride with formula 2Cl.Co. Current OLS CHEBI:53503
    explicitly represents the hexahydrate. There is no cobalt secondary assertion
    to correct. Correct magnesium, calcium, iron and zinc hydrate groundings are retained;
    unspecified MnSO4·xH2O should remain unresolved rather than forced to a specific
    hydrate.
  target_ids:
  - CultureMech:007902
  field_paths:
  - ingredients[6].term
  evidence_ids:
  - grounding
  - chebi35696
  - chebi53503
  - jcm1268
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-007902-source-name-version-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The current JCM title differs from the imported source name
  description: The exact JCM 1268 accession now says CAPROICIBACTERIUM MEDIUM, while
    TOGO M1364 and current MediaDive J1268 retain CAPROICIPRODUCENS MEDIUM. Formulation
    rows and source links correspond; this is a naming/version distinction, not proof
    the target denotes a different recipe.
  target_ids:
  - CultureMech:007902
  field_paths:
  - name
  - original_name
  - media_term
  - notes
  evidence_ids:
  - jcm1268
  - togoM1364
  - apiJ1268
  rule_id: source-version-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Represent source water and absolute stock additions in their preparation
    stages, preserve known molar strengths and unresolved percent basis, and replace
    placeholders with exact source labels. Attach stock-dose evidence to enclosing
    root evidence with the full solution field path; do not invent an evidence slot
    on SolutionDescriptor.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007902
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
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
  description: Add the exact source preparation with root evidence scoped to pH, gas,
    sterilization, cooling/addition order and subculture preheat. Retain unquantified
    details as unresolved instead of supplying standard assumptions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007902
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
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
  description: Resolve the cobalt supplied form using the verified hexahydrate correspondence
    without changing supported source mass. Independently verify any newly proposed
    secondary linkage. Do not adopt provider mmol_l based on anhydrous cobalt mass.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007902
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
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
  description: Preserve source accession and imported name, document the current title
    with capture date, and verify any biological synonym claim separately. Keep original
    history unchanged and append actual corrective context only when curated.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007902
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1364_Caproiciproducens_Medium.yaml
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
- No measured final volume is inferred from 645+355 ml of listed liquid inputs. Base
  provider g_l is explicitly labeled normalization, not physical volume proof.
- The two 10% stock labels do not state percent basis, and stock preparation recipes
  are not supplied. No grams or final concentrations are invented.
- Current naming differences are not evidence of organism taxonomy or experimentally
  observed growth; source-specific preparation guidance is not optimization.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
