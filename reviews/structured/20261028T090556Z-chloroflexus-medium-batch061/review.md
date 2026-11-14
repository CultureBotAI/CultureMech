# Scientific review of chloroflexus_medium

- Review: 20261028T090556Z-chloroflexus-medium-batch061
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:33:19.353227Z
- Finished UTC: 2026-10-28T09:05:56.998451Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1268/JCM 1183 identity is supported, but the maintained and generated formulation requires stage reconstruction: water was summed across stocks, vitamin milligrams became flat grams-per-litre values, and five liquid stock doses retain mass units. Preparation, pH and exact chemical-form support also need curation. Correct current writer protections and the dependency water repair are credited.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch061 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007800 | data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml | generated | chloroflexus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007800 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:007800 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:007800 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:007800 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact TOGO and JCM identities

identity: supported. Targets: CultureMech:007800.

The maintained owner and single-source target consistently identify TOGO M1268 from JCM 1183. Both current sources agree on that identity. M305 is a trace-stock dependency, not a second owner or a replacement basal medium.

### Preparation and stock structure

completeness: concern. Targets: CultureMech:007800.

Five named solution descriptors retain useful identity leads but have placeholder names, empty compositions and mass-unit dose errors. Main pH 7.5 and post-autoclave stock preparation are absent. The current TOGO importer already distinguishes primary/nested sections and preserves comments, so persisted flattening is not attributed to an unchanged current importer.

### All histories and historical reports

provenance: concern. Targets: CultureMech:007800.

The September review and two zero-source October reports were read fully. Their recipe/stock concerns are independently confirmed, but the September statement of a final 1 L preparation is narrowed to listed water: later stocks and current API normalization do not establish a measured final volume. No historical raw capture was recovered from these reports. Existing migration, duplicate-repair and grounding events remain unchanged; current code is not proof of past execution.

### Source formulation versus organism growth

evidence: unknown. Targets: CultureMech:007800.

Current collection and database sources establish a formulation and preparation, but no strain-specific experimental growth claim was independently verified. Generic cultivation application text is retained without inventing taxa or performance metrics.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:007800.

All 46 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007800", "selected_concentration_field_count": 46, "selected_concentration_fields_covered": 46, "decisions": [{"decision_id": "q1", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[4]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "NaCl\n0.5\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[4]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 8.53871,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[0]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "KH\n2\nPO\n4\n0.5\ng", "quote_representation": "HTML tr[0] DOM text"}, {"locator": "$.components[0].items[5]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 3.66681,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[1]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "NH\n4\nCl\n0.5\ng", "quote_representation": "HTML tr[1] DOM text"}, {"locator": "$.components[0].items[6]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 9.32888,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "MgCl2・6H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[2]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "MgCl\n2\n·6H\n2\nO\n0.3\ng", "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.components[0].items[7]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\": 1.47268,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[3]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "KCl\n0.5\ng", "quote_representation": "HTML tr[3] DOM text"}, {"locator": "$.components[0].items[8]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 6.69352,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "HEPES", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[7]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "HEPES\n3.0\ng", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[9]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"HEPES\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001142\",\n          \"gmo_id\": \"GMO_001142\",\n          \"label\": \"HEPES\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"HEPES\",\n                        \"compound_id\": 371,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.99401,\n                        \"mmol_l\": 12.5635,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Yeast extract (BD-Difco)", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[6]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Yeast extract (BD-Difco)\n1.0\ng", "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[10]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Na2S2O3・5H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume basis unresolved", "interpretation": "The same numeric mass is supported in grams for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L asserts an additional denominator not established by the 1 L water input plus later stocks. API J1183 reports different g_l values on declared 1002 ml metadata; this is an attributed provider basis, not a measured final volume. Preserve the absolute source amount and resolve representation without inventing a final-rate replacement.", "sources": [{"locator": "HTML tr[5]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Na\n2\nS\n2\nO\n3\n·5H\n2\nO\n0.1\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[11]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Na2S2O3・5H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001041\",\n          \"gmo_id\": \"GMO_001041\",\n          \"label\": \"Sodium thiosulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 0.402119,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Water combined across stages", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "101.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "101.0", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Basal water versus vitamin-stock water", "interpretation": "The source has 1 L basal water and 100 ml vitamin-stock water; only 1 ml of the vitamin stock is added. The persisted 101 G_PER_L is a sum of incompatible magnitudes and stages, not a supported water amount. Separate source inputs; do not replace it by an assumed 1.1 L or final-medium mass.", "sources": [{"locator": "HTML tr[10]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[10] DOM text"}, {"locator": "HTML tr[20]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Distilled water\n100.0\nml", "quote_representation": "HTML tr[20] DOM text"}, {"locator": "$.components[0].items[3]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.components[1].items[0]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 2 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Biotin\n2.0\nmg", "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[1].items[1]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 5 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[19]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "p\n-Aminobenzoic acid\n5.0\nmg", "quote_representation": "HTML tr[19] DOM text"}, {"locator": "$.components[1].items[2]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Thiamine・HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 5 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[14]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Thiamine·HCl\n5.0\nmg", "quote_representation": "HTML tr[14] DOM text"}, {"locator": "$.components[1].items[3]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "Pyridoxine・HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 10 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Pyridoxine·HCl\n10.0\nmg", "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[1].items[4]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 2 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[12]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Folic acid\n2.0\nmg", "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[1].items[5]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 0.5 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[18]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Vitamin B\n12\n0.5\nmg", "quote_representation": "HTML tr[18] DOM text"}, {"locator": "$.components[1].items[6]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 5 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[15]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Riboflavin\n5.0\nmg", "quote_representation": "HTML tr[15] DOM text"}, {"locator": "$.components[1].items[7]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 5 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[16]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Nicotinic acid\n5.0\nmg", "quote_representation": "HTML tr[16] DOM text"}, {"locator": "$.components[1].items[8]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "DL-Calcium pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition", "interpretation": "The source amount 5 is in milligrams in the separate stock with 100 ml water. The stored identical number in G_PER_L is both a unit and stage error. API stock g_l is separately attributed; it must not become the receiving-medium concentration. Preserve the exact supplied form and 1 ml stock dose; no physical final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator": "HTML tr[17]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "DL-Calcium pantothenate\n5.0\nmg", "quote_representation": "HTML tr[17] DOM text"}, {"locator": "$.components[1].items[9]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"DL-Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001936\",\n          \"gmo_id\": \"GMO_001936\",\n          \"label\": \"DL-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\": 1720,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.104932,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "Bicarbonate stock: 10 ml, 3%", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Post-autoclave receiving dose and separate stock strength", "interpretation": "The stored scalar is a liquid addition in ml, not G_PER_L. Preserve the stock percentage separately with its source-unspecified basis; do not silently assume w/v or calculate final masses. Sulfide and calcium stocks are autoclaved; bicarbonate is filter-sterilized. These additions follow basal autoclaving.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"NaHCO3 solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 3,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\": \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of 5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized). Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "Calcium chloride dihydrate stock: 1 ml, 5%", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Post-autoclave receiving dose and separate stock strength", "interpretation": "The stored scalar is a liquid addition in ml, not G_PER_L. Preserve the stock percentage separately with its source-unspecified basis; do not silently assume w/v or calculate final masses. Sulfide and calcium stocks are autoclaved; bicarbonate is filter-sterilized. These additions follow basal autoclaving.", "sources": [{"locator": "$.components[0].items[1]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"CaCl2・2H2O solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001228\",\n          \"gmo_id\": \"GMO_001228\",\n          \"label\": \"Calcium chloride dihydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\": \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of 5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized). Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "Sulfide nonahydrate stock: 1 ml, 5%", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Post-autoclave receiving dose and separate stock strength", "interpretation": "The stored scalar is a liquid addition in ml, not G_PER_L. Preserve the stock percentage separately with its source-unspecified basis; do not silently assume w/v or calculate final masses. Sulfide and calcium stocks are autoclaved; bicarbonate is filter-sterilized. These additions follow basal autoclaving.", "sources": [{"locator": "$.components[0].items[2]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Na2S・9H2O solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\": \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of 5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized). Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "Trace-vitamin dose", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "solutions[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "solutions[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving batch addition", "interpretation": "The source specifies 1 ml, not 1 G_PER_L. The vitamin stock is defined below JCM 1183; the trace stock is the explicitly named subsection of JCM 310/M305. Neither dose licenses transfer of an entire parent medium, nor does listed basal water establish a final ml/L denominator.", "sources": [{"locator": "HTML tr[8]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Trace vitamins solution (see below)\n1.0\nml", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[12]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Trace vitamins solution (see below)\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1268\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "Trace-element dose", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "solutions[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml", "field_path": "solutions[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Receiving batch addition", "interpretation": "The source specifies 1 ml, not 1 G_PER_L. The vitamin stock is defined below JCM 1183; the trace stock is the explicitly named subsection of JCM 310/M305. Neither dose licenses transfer of an entire parent medium, nor does listed basal water establish a final ml/L denominator.", "sources": [{"locator": "HTML tr[9]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Trace elements solution (see Medium No.\n310\n)\n1.0\nml", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[13]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\": \"Trace elements solution (see Medium [M305])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M305\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Basal sterilization and later pH", "local_fields": [], "decision": "evidence_only", "stage": "Source-only preparation", "interpretation": "JCM 1183 page default is 121 C for 15 min unless otherwise stated. Its explicit prose requires later stock additions with their separate sterilization and adjustment to pH 7.5. Retain this source-scoped default; do not import unrelated JCM 310 parent conditions.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\": \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of 5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized). Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Na2MoO4・2H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[14]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n0.03\ng", "quote_representation": "HTML tr[14] DOM text"}, {"locator": "$.components[1].items[1]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[6]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "H3BO3 in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[16]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "H\n3\nBO\n3\n0.3\ng", "quote_representation": "HTML tr[16] DOM text"}, {"locator": "$.components[1].items[2]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[8]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "FeSO4・7H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[9]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "FeSO\n4\n·7H\n2\nO\n2.0\ng", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[1].items[3]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "MnCl2・4H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n0.03\ng", "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[1].items[4]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "CoCl2・6H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[12]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n0.2\ng", "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[1].items[5]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[4]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "NiCl2・6H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "NiCl\n2\n·6H\n2\nO\n0.02\ng", "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[1].items[6]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[5]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "ZnSO4・7H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[10]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "ZnSO\n4\n·7H\n2\nO\n0.1\ng", "quote_representation": "HTML tr[10] DOM text"}, {"locator": "$.components[1].items[7]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "CuCl2・2H2O in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[15]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "CuCl\n2\n·2H\n2\nO\n0.01\ng", "quote_representation": "HTML tr[15] DOM text"}, {"locator": "$.components[1].items[8]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[7]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "EDTA in scoped M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent basal medium or receiving final rate", "interpretation": "The amount belongs to the trace stock with 1 L listed water. The local dependency flattens it into parent ingredients; retain this amount/form under the stock. API J1183 explicitly gives stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni supplied hexahydrates require separate primary-term repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML tr[8]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "EDTA\n5.0\ng", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[1].items[9]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"EDTA\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001237\",\n          \"gmo_id\": \"GMO_001237\",\n          \"label\": \"EDTA\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "M305 water already duplicate-collapsed", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.0", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Two distinct source water stages", "interpretation": "Credit the historical equal-duplicate collapse from 2 to 1, but the source still gives 1 L basal water and separately 1 L trace-stock water, not 1 G_PER_L. Only the trace-stock water transfers here. Preserve the repair history while reconstructing stage and unit; do not transfer the entire parent water recipe.", "sources": [{"locator": "HTML tr[7]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "HTML tr[17]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[17] DOM text"}, {"locator": "$.components[0].items[2]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.components[1].items[0]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "Trace-stock HCl and pH 3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Stock adjustment, quantity unspecified", "interpretation": "The source says adjust the trace stock to pH 3 with HCl, with no acid dose or molarity. The existing variable placeholder truthfully avoids a fabricated amount but needs this stock-specific pH context. This is not the receiving medium pH 7.5.", "sources": [{"locator": "extracted-text lines 114-114", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Adjust pH to 3 with HCl.", "quote_representation": "captured extracted text"}, {"locator": "$.components[1].items[10]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305", "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff", "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\": \"HCl\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].steps[0]", "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 3 with HCl.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "Excluded M305 basal ingredients and additions", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "solutions[1].concentration", "original": {"value": "7.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "not_assessed", "stage": "Explicit dependency boundary", "interpretation": "These NaCl/phosphate/carbonate basal fields and the 20% magnesium, 2 M KSCN and parent trace-dose stubs belong to the distinct M305/JCM 310 receiving medium. They are inventoried unchanged for boundary clarity and are not assessed or proposed for transfer into JCM 1183.", "sources": []}], "local_field_census_reference": "REVIEW_WORK/batch061/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:007800.

data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml: primary 17/18, secondary 13/18; data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml: primary 17/18, secondary 13/18. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:007800.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:007800.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Water and vitamin amounts lose units and stock stages

major / open / confirmed; issue key: culturemech-007800-water-vitamin-and-denominator-stages.

The water row sums 1 L basal and 100 ml vitamin-stock inputs as 101 G_PER_L. Nine stock milligram values are stored unchanged as top-level G_PER_L. Eight basal numbers match source grams but lack an explicit final-volume basis. API J1183 uses a declared 1002 ml normalization, which is not silently substituted for the primary source.

### f2: Five liquid stock additions retain mass units and empty compositions

major / open / confirmed; issue key: culturemech-007800-stock-dose-units-and-empty-composition.

The five solution scalars are receiving volumes in ml, not grams per litre. Bicarbonate is 10 ml of a 3% stock; calcium and sulfide each use 1 ml of a 5% stock; vitamin and trace stocks each use 1 ml. Bare percent bases remain unspecified. Named preferred terms already provide identities, despite the generic Unknown solution names.

### f3: Source preparation and receiving pH are absent

major / open / confirmed; issue key: culturemech-007800-missing-stage-preparation-and-ph.

Both selected layers omit main pH 7.5, basal autoclaving and post-autoclave additions. The source differentiates autoclaved sulfide/calcium stocks from filter-sterilized bicarbonate. Trace-stock pH 3 belongs only to JCM 310, not the receiving medium. Evidence for preparation and solution doses must use supported root-level scope, not nonexistent solution/preparation evidence slots.

### f4: DL pantothenate and dependency hydrates differ from asserted chemical structures

major / open / confirmed; issue key: culturemech-007800-supplied-stereochemistry-and-dependency-hydrates.

The source explicitly names DL-calcium pantothenate, while CHEBI:31345 has D-form synonyms and stereospecific InChI/SMILES in the current OLS response. Both selected primary and secondary slots assert that ID. The scoped dependency separately names cobalt and nickel hexahydrates but asserts anhydrous CHEBI:35696 and :34887 in primary slots only. Literal label checks do not establish these supplied-form correspondences.

### f5: Referenced trace stock cannot be replaced by the full flattened parent record

major / open / confirmed; issue key: culturemech-007800-trace-dependency-boundary.

M305 contains an unrelated basal medium plus flattened trace ingredients and three other stock stubs. Only its JCM 310 trace subsection supports the receiving stock. Its repaired equal water duplicate is credited, but its mass-unit water and flat composition still need source-scoped reconstruction.

### f6: HEPES secondary linkage has no current exact MIM row

minor / open / confirmed; issue key: culturemech-007800-hepes-current-secondary-coverage.

Both selected layers assert CHEBI:46756 as primary and secondary HEPES. Current OLS confirms the literal label but returns no formula or definition; the packaged MIM CSV has zero exact identifier rows. This is a current secondary-coverage gap, not proof that the ontology term or historical mapping was invalid.

## Recommended Actions And Acceptance Checks

### action1

Restore source-scoped basal amounts, separate water stages and the complete nine-component vitamin stock. Preserve the BD-Difco qualifier and supplied hydrates. Resolve denominator representation explicitly; do not sum stock water into the medium or manufacture final-rate conversions.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Correct each dose to its explicit source batch-volume representation, preserve stock percentages with honest basis limits, and reconstruct source-supported composition or scoped references. Do not encode a liquid dose as a solute mass or infer percentage basis from current importer defaults.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the exact source-scoped preparation and pH with claim-specific root evidence. Preserve distinct stock sterilization and receiving stages; review current importer meta.ph handling and the retained comments before regeneration.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve the explicitly racemic supplied form and exact cobalt/nickel hydrates against authoritative ontology and current MIM records. Preserve source masses and scoped stock membership; retain precise unresolved labels if no verified identifier is available. Do not invent secondary links or alter the formula to fit an existing ID.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Use only the verified trace subsection, including exact hydrates, stock water and pH 3/HCl adjustment. Preserve M305 historical repairs and do not transfer its basal carbonate, thiocyanate, magnesium solution, parent doses or parent preparation into JCM 1183.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action6

Retain the correct source HEPES name and independently verify current MIM linkage support. Record unresolved current coverage explicitly rather than substituting an unverified identifier.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch061/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch061/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch061/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch061/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm1183 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current official JCM page read, including the main and embedded stock tables, preparation and source-specific defaults. The page-wide default remains scoped to that source; named stock sections are separate from main-medium preparation. |
| togoM1268 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| jcm310 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full source read for identity and boundaries; only the explicitly linked trace-elements subsection, its water and pH 3/HCl instruction support the receiving JCM 1183 stock. The parent basal salts, KSCN and MgCl2 additions and parent-specific preparation do not transfer. |
| togoM305 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full source read for identity and boundaries; only the explicitly linked trace-elements subsection, its water and pH 3/HCl instruction support the receiving JCM 1183 stock. The parent basal salts, KSCN and MgCl2 additions and parent-specific preparation do not transfer. |
| apiJ1183 | https://mediadive.dsmz.de/rest/medium/J1183; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32150 = sodium thiosulfate pentahydrate; definition ['A hydrate consisting of sodium thiosulfate with 5 mol eq. of water.']; formula ['5H2O.2Na.O3S2']; mass ['248.186']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt salt in which the cobalt metal is in the +2 oxidation state and the counter-anion is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co']; mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi46756 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:46756 = HEPES; definition []; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_4735; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:4735 = ethylenediaminetetraacetic acid; definition []; formula ['C10H16N2O8']; mass ['292.244']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used).']; formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch061/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T071125Z-CHLOROFLEXUS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch061/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer46 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace legacy secondary MIM links or authenticate quantities. |
| writer47 | scripts/cleanup_media_quality.py; relevant functions named in summary | context_only | Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical values and flags unequal values rather than summing them. The persisted 101 water value combines source amounts from different units and stages; it does not show that current cleanup still sums unequal stages. |
| writer48 | scripts/migrate_solutions_from_ingredients.py; relevant functions named in summary | context_only | Current _resolve_solution and _migrate_media_file identify stock references and move descriptors into solutions while preserving their stored concentration. Copying a malformed G_PER_L value does not validate its source dose or hydrate, and a current named reference does not prove stock equivalence. |
| writer49 | scripts/repair_merged_duplicates.py; relevant functions named in summary | context_only | Current repair_ingredient/repair_record only collapse identical historical merged parts and recurse into nested composition. The dependency already retains a corrected equal water duplicate, but this does not establish its scientific water unit; the selected unequal 1 plus 100 sum remains outside the automatic repair. Current code is not proof of past execution. |
| writer50 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus referenced stock sections, _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. _local_batch_volume_ml declines unmatched stock bases; _extract_ph reads top-level ph, whereas this current payload stores meta.ph. Bare g/ml still map to per-litre enums and bare percent to PERCENT_W_V, requiring source-basis review. Current fixed code is not proof of historical flattening. |
| writer51 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer52 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer53 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| dep54 | data/normalized_yaml/bacterial/togo_medium_m305.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| quantity-inventory | REVIEW_WORK/batch061/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Primary sources list absolute water inputs and later additions, not a measured final medium volume. API normalization is separately attributed and is not silently treated as physical final volume.
- Bare 3% and 5% stock strengths have no explicit percentage basis in the retrieved primary source. No implied solute masses or final concentrations are supplied.
- JCM 310/M305 contributes only the trace-elements subsection, its water and stock pH adjustment. Its unrelated basal medium, receiving doses and other stock recipes are outside scientific assessment.
- Current MIM rows are from packaged metadata commit 6643131b0f12ab40b66f98135245fca04027e0e9; current exact negatives do not establish historical invalidity.
- No experimental strain-specific growth claim was verified. All three historical reports were read, but their assertions do not authenticate historical raw payloads or executions.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T090556Z-chloroflexus-medium-batch061
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of chloroflexus_medium
started_at: '2026-10-28T08:33:19.353227Z'
finished_at: '2026-10-28T09:05:56.998451Z'
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
summary: 'TOGO M1268/JCM 1183 identity is supported, but the maintained and generated
  formulation requires stage reconstruction: water was summed across stocks, vitamin
  milligrams became flat grams-per-litre values, and five liquid stock doses retain
  mass units. Preparation, pH and exact chemical-form support also need curation.
  Correct current writer protections and the dependency water repair are credited.'
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
  - path: data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
    sha256: 8664bf41a69df59c8fd1a5c2460e3924da6b8bc9a8d9db6a4b469ca31a823410
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    sha256: 1a75d8b66828e9af4c18f5b3125e203a86c4bade9e144fd4168337e1f1f66516
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m305.yaml
    sha256: 36741d6102c5a2446f11a903a75c8300711f04457ed5be336e384258e635e88b
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.md
    sha256: 50e6db67df080e00dd9feca8cc01a329d672aee453aa4574561fd729976c02c6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.md
    sha256: f10da18e2ec5546de85301df3c176c77c4d741cbf37c59c2c2dd957ed4f432c4
    role: context
  - path: reports/yaml_record_review/20260922T071125Z-CHLOROFLEXUS_MEDIUM.md
    sha256: 4aebea0b8aa2001de80d47a494fc02b4ccbb3082f5cc87ffa681334eed984c26
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
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch061 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007800
targets:
- target_id: CultureMech:007800
  path: data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
  label: chloroflexus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007800
  command: just validate-schema data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007800
  command: just validate-strict data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch061/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007800
  command: just validate-terms data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:007800
  command: just validate-references data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:53:46.754305Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 8664bf41a69df59c8fd1a5c2460e3924da6b8bc9a8d9db6a4b469ca31a823410
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:53:46.754454Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 1a75d8b66828e9af4c18f5b3125e203a86c4bade9e144fd4168337e1f1f66516
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:20.364389Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: d19f4089d43177088fd4ae847c26bfd8afda9c63e9bb3aaba974bf9ead185e74
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:21.276357Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: d7499e4399ea37ba6d48f967d583db1d35c1237fdce83bc8ae909ceed0bf971c
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:22.274094Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 98bfa64af65e9f4372c42168d1b9dcf5a9542061395fd1ef1400abea057fbf55
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch061/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:22.969315Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 5055ea20dcdc1425570bbf0af4a06e798e6091e414481f4271cc77a168dc894f
- evidence_id: jcm1183
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:54.197433Z'
  support: supports
  summary: Complete current official JCM page read, including the main and embedded
    stock tables, preparation and source-specific defaults. The page-wide default
    remains scoped to that source; named stock sections are separate from main-medium
    preparation.
  snapshot_sha256: 5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293
- evidence_id: togoM1268
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:54.182700Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a
- evidence_id: jcm310
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:54.181666Z'
  support: supports
  summary: Full source read for identity and boundaries; only the explicitly linked
    trace-elements subsection, its water and pH 3/HCl instruction support the receiving
    JCM 1183 stock. The parent basal salts, KSCN and MgCl2 additions and parent-specific
    preparation do not transfer.
  snapshot_sha256: 021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b
- evidence_id: togoM305
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:54.151165Z'
  support: supports
  summary: Full source read for identity and boundaries; only the explicitly linked
    trace-elements subsection, its water and pH 3/HCl instruction support the receiving
    JCM 1183 stock. The parent basal salts, KSCN and MgCl2 additions and parent-specific
    preparation do not transfer.
  snapshot_sha256: 7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff
- evidence_id: apiJ1183
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1183
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:54.031836Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:53.561545Z'
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
  accessed_at: '2026-10-28T08:33:53.517891Z'
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
  accessed_at: '2026-10-28T08:33:53.502195Z'
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
  accessed_at: '2026-10-28T08:33:53.479372Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:53.441479Z'
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
  accessed_at: '2026-10-28T08:33:53.435372Z'
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
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.947761Z'
  support: supports
  summary: OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear
    parent hydride consisting of covalently bonded hydrogen and chlorine atoms.'];
    formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.909743Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.848896Z'
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
  accessed_at: '2026-10-28T08:33:52.834988Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.834752Z'
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
  accessed_at: '2026-10-28T08:33:52.766950Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.290980Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.267651Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.206443Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32150
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.170264Z'
  support: supports
  summary: OLS current exact CHEBI:32150 = sodium thiosulfate pentahydrate; definition
    ['A hydrate consisting of sodium thiosulfate with 5 mol eq. of water.']; formula
    ['5H2O.2Na.O3S2']; mass ['248.186']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:52.155309Z'
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
  accessed_at: '2026-10-28T08:33:52.152843Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.674201Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.606222Z'
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
  accessed_at: '2026-10-28T08:33:51.571085Z'
  support: supports
  summary: OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt
    salt in which the cobalt metal is in the +2 oxidation state and the counter-anion
    is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co'];
    mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi46756
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.559293Z'
  support: supports
  summary: OLS current exact CHEBI:46756 = HEPES; definition []; formula None; mass
    None; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 4270cc705078ff2f1787f98b7dbcf05c96b1eccd333801a00cff01b855298a69
- evidence_id: chebi4735
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_4735
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.534250Z'
  support: supports
  summary: OLS current exact CHEBI:4735 = ethylenediaminetetraacetic acid; definition
    []; formula ['C10H16N2O8']; mass ['292.244']; obsolete=False. Literal label is
    distinct from supplied-form equivalence.
  snapshot_sha256: ef8713e257a5e52aa813d8a43a26ed321ff04a475591ff238c00a47758f96717
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:51.533448Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:50.796117Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:50.796078Z'
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
  accessed_at: '2026-10-28T08:33:50.796023Z'
  support: supports
  summary: OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a
    source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage
    treatments; for solid-dosage treatments, the monohydrate is normally used).'];
    formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:50.795954Z'
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
  accessed_at: '2026-10-28T08:33:50.795855Z'
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
  accessed_at: '2026-10-28T08:33:50.795587Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch061/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T08:53:46.765736Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 42af034084fae014724cf1af71d6bf22081fcb777dcfd71876dba198ef54e78c
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T071125Z-CHLOROFLEXUS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:53:46.766134Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 4aebea0b8aa2001de80d47a494fc02b4ccbb3082f5cc87ffa681334eed984c26
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:53:46.766157Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: f10da18e2ec5546de85301df3c176c77c4d741cbf37c59c2c2dd957ed4f432c4
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:53:46.766180Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 50e6db67df080e00dd9feca8cc01a329d672aee453aa4574561fd729976c02c6
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch061/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T08:53:46.766199Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: f6068c0e9bd426b4ed4f3ded16c56b10d4def57b87634ed973792563960cdaef
- evidence_id: writer46
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766221Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace legacy secondary MIM links or
    authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer47
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766244Z'
  support: context_only
  summary: Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical
    values and flags unequal values rather than summing them. The persisted 101 water
    value combines source amounts from different units and stages; it does not show
    that current cleanup still sums unequal stages.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer48
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766266Z'
  support: context_only
  summary: Current _resolve_solution and _migrate_media_file identify stock references
    and move descriptors into solutions while preserving their stored concentration.
    Copying a malformed G_PER_L value does not validate its source dose or hydrate,
    and a current named reference does not prove stock equivalence.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer49
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766284Z'
  support: context_only
  summary: Current repair_ingredient/repair_record only collapse identical historical
    merged parts and recurse into nested composition. The dependency already retains
    a corrected equal water duplicate, but this does not establish its scientific
    water unit; the selected unequal 1 plus 100 sum remains outside the automatic
    repair. Current code is not proof of past execution.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer50
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766317Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    referenced stock sections, _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. _local_batch_volume_ml declines unmatched stock bases; _extract_ph
    reads top-level ph, whereas this current payload stores meta.ph. Bare g/ml still
    map to per-litre enums and bare percent to PERCENT_W_V, requiring source-basis
    review. Current fixed code is not proof of historical flattening.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer51
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766336Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer52
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766355Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer53
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:53:46.766375Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: dep54
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m305.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T08:53:46.766381Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 36741d6102c5a2446f11a903a75c8300711f04457ed5be336e384258e635e88b
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch061/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T08:53:46.896784Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: ef1b084d41b8e7b9bac2627de9e258a7d534ff9ae0630fe47a5c8b6e51c32350
assessments:
- assessment_id: a1
  area: identity
  topic: Exact TOGO and JCM identities
  outcome: supported
  summary: The maintained owner and single-source target consistently identify TOGO
    M1268 from JCM 1183. Both current sources agree on that identity. M305 is a trace-stock
    dependency, not a second owner or a replacement basal medium.
  target_ids:
  - CultureMech:007800
  evidence_ids:
  - togoM1268
  - jcm1183
  - local0
  - local1
- assessment_id: a2
  area: completeness
  topic: Preparation and stock structure
  outcome: concern
  summary: Five named solution descriptors retain useful identity leads but have placeholder
    names, empty compositions and mass-unit dose errors. Main pH 7.5 and post-autoclave
    stock preparation are absent. The current TOGO importer already distinguishes
    primary/nested sections and preserves comments, so persisted flattening is not
    attributed to an unchanged current importer.
  target_ids:
  - CultureMech:007800
  evidence_ids:
  - jcm1183
  - togoM1268
  - quantity-inventory
- assessment_id: a3
  area: provenance
  topic: All histories and historical reports
  outcome: concern
  summary: 'The September review and two zero-source October reports were read fully.
    Their recipe/stock concerns are independently confirmed, but the September statement
    of a final 1 L preparation is narrowed to listed water: later stocks and current
    API normalization do not establish a measured final volume. No historical raw
    capture was recovered from these reports. Existing migration, duplicate-repair
    and grounding events remain unchanged; current code is not proof of past execution.'
  target_ids:
  - CultureMech:007800
  evidence_ids:
  - history-auth
  - writer46
  - writer47
  - writer48
  - writer49
  - writer50
  - writer51
  - writer52
  - writer53
- assessment_id: a4
  area: evidence
  topic: Source formulation versus organism growth
  outcome: unknown
  summary: Current collection and database sources establish a formulation and preparation,
    but no strain-specific experimental growth claim was independently verified. Generic
    cultivation application text is retained without inventing taxa or performance
    metrics.
  target_ids:
  - CultureMech:007800
  evidence_ids:
  - jcm1183
  - togoM1268
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 46 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:007800
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007800",
    "selected_concentration_field_count": 46, "selected_concentration_fields_covered":
    46, "decisions": [{"decision_id": "q1", "subject": "NaCl", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[4]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "NaCl\n0.5\ng", "quote_representation":
    "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[4]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    8.53871,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[0]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "KH\n2\nPO\n4\n0.5\ng", "quote_representation":
    "HTML tr[0] DOM text"}, {"locator": "$.components[0].items[5]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    3.66681,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[1]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "NH\n4\nCl\n0.5\ng", "quote_representation":
    "HTML tr[1] DOM text"}, {"locator": "$.components[0].items[6]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    9.32888,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "MgCl2・6H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[2]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "MgCl\n2\n·6H\n2\nO\n0.3\ng",
    "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.components[0].items[7]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\":
    1.47268,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[3]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "KCl\n0.5\ng", "quote_representation":
    "HTML tr[3] DOM text"}, {"locator": "$.components[0].items[8]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    6.69352,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "HEPES", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[7]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "HEPES\n3.0\ng", "quote_representation":
    "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[9]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"HEPES\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001142\",\n          \"gmo_id\": \"GMO_001142\",\n          \"label\":
    \"HEPES\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"HEPES\",\n                        \"compound_id\":
    371,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.99401,\n                        \"mmol_l\":
    12.5635,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "Yeast extract (BD-Difco)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[6]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Yeast extract (BD-Difco)\n1.0\ng",
    "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[10]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract (BD-Difco)\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\":
    \"Bacto &trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.998004,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "Na2S2O3・5H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Basal absolute mass; final-volume
    basis unresolved", "interpretation": "The same numeric mass is supported in grams
    for the source batch, including the stated hydrate or BD-Difco grade. Local G_PER_L
    asserts an additional denominator not established by the 1 L water input plus
    later stocks. API J1183 reports different g_l values on declared 1002 ml metadata;
    this is an attributed provider basis, not a measured final volume. Preserve the
    absolute source amount and resolve representation without inventing a final-rate
    replacement.", "sources": [{"locator": "HTML tr[5]", "source_key": "jcm1183",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183", "source_raw_sha256":
    "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293", "source_text_sha256":
    "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992", "accessed_at":
    "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Na\n2\nS\n2\nO\n3\n·5H\n2\nO\n0.1\ng",
    "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[11]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2S2O3・5H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001041\",\n          \"gmo_id\": \"GMO_001041\",\n          \"label\":
    \"Sodium thiosulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\":
    65,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    0.402119,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "Water combined across
    stages", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "101.0", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "101.0", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Basal water versus vitamin-stock
    water", "interpretation": "The source has 1 L basal water and 100 ml vitamin-stock
    water; only 1 ml of the vitamin stock is added. The persisted 101 G_PER_L is a
    sum of incompatible magnitudes and stages, not a supported water amount. Separate
    source inputs; do not replace it by an assumed 1.1 L or final-medium mass.", "sources":
    [{"locator": "HTML tr[10]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Distilled
    water\n1.0\nL", "quote_representation": "HTML tr[10] DOM text"}, {"locator": "HTML
    tr[20]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Distilled
    water\n100.0\nml", "quote_representation": "HTML tr[20] DOM text"}, {"locator":
    "$.components[0].items[3]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "$.components[1].items[0]", "source_key": "togoM1268",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\":
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
    JSON object"}]}, {"decision_id": "q10", "subject": "Biotin", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration",
    "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 2 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[11]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Biotin\n2.0\nmg",
    "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[1].items[1]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 5 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[19]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "p\n-Aminobenzoic
    acid\n5.0\nmg", "quote_representation": "HTML tr[19] DOM text"}, {"locator": "$.components[1].items[2]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "Thiamine・HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 5 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[14]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Thiamine·HCl\n5.0\nmg",
    "quote_representation": "HTML tr[14] DOM text"}, {"locator": "$.components[1].items[3]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q13", "subject": "Pyridoxine・HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 10 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[13]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Pyridoxine·HCl\n10.0\nmg",
    "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[1].items[4]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\":
    \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q14", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 2 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[12]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Folic acid\n2.0\nmg",
    "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[1].items[5]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\":
    \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[1]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 0.5 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[18]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Vitamin B\n12\n0.5\nmg",
    "quote_representation": "HTML tr[18] DOM text"}, {"locator": "$.components[1].items[6]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[7]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.00368895,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject":
    "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 5 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[15]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Riboflavin\n5.0\nmg",
    "quote_representation": "HTML tr[15] DOM text"}, {"locator": "$.components[1].items[7]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\":
    \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 5 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[16]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Nicotinic
    acid\n5.0\nmg", "quote_representation": "HTML tr[16] DOM text"}, {"locator": "$.components[1].items[8]",
    "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "DL-Calcium pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-vitamin stock composition",
    "interpretation": "The source amount 5 is in milligrams in the separate stock
    with 100 ml water. The stored identical number in G_PER_L is both a unit and stage
    error. API stock g_l is separately attributed; it must not become the receiving-medium
    concentration. Preserve the exact supplied form and 1 ml stock dose; no physical
    final-volume or vitamin molecular-mass assumption is made.", "sources": [{"locator":
    "HTML tr[17]", "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "DL-Calcium
    pantothenate\n5.0\nmg", "quote_representation": "HTML tr[17] DOM text"}, {"locator":
    "$.components[1].items[9]", "source_key": "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"DL-Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001936\",\n          \"gmo_id\": \"GMO_001936\",\n          \"label\":
    \"DL-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\":
    1720,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.104932,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "Bicarbonate stock: 10
    ml, 3%", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Post-autoclave receiving dose and
    separate stock strength", "interpretation": "The stored scalar is a liquid addition
    in ml, not G_PER_L. Preserve the stock percentage separately with its source-unspecified
    basis; do not silently assume w/v or calculate final masses. Sulfide and calcium
    stocks are autoclaved; bicarbonate is filter-sterilized. These additions follow
    basal autoclaving.", "sources": [{"locator": "$.components[0].items[0]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaHCO3 solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
    3,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\":
    \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\":
    \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of
    5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized).
    Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q20", "subject": "Calcium chloride dihydrate stock:
    1 ml, 5%", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Post-autoclave receiving dose and
    separate stock strength", "interpretation": "The stored scalar is a liquid addition
    in ml, not G_PER_L. Preserve the stock percentage separately with its source-unspecified
    basis; do not silently assume w/v or calculate final masses. Sulfide and calcium
    stocks are autoclaved; bicarbonate is filter-sterilized. These additions follow
    basal autoclaving.", "sources": [{"locator": "$.components[0].items[1]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"CaCl2・2H2O solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"conc_value\":
    5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001228\",\n          \"gmo_id\":
    \"GMO_001228\",\n          \"label\": \"Calcium chloride dihydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\":
    \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of
    5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized).
    Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q21", "subject": "Sulfide nonahydrate stock: 1 ml,
    5%", "local_fields": [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Post-autoclave receiving dose and
    separate stock strength", "interpretation": "The stored scalar is a liquid addition
    in ml, not G_PER_L. Preserve the stock percentage separately with its source-unspecified
    basis; do not silently assume w/v or calculate final masses. Sulfide and calcium
    stocks are autoclaved; bicarbonate is filter-sterilized. These additions follow
    basal autoclaving.", "sources": [{"locator": "$.components[0].items[2]", "source_key":
    "togoM1268", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2S・9H2O solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"conc_value\":
    5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\":
    \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\":
    \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of
    5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized).
    Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q22", "subject": "Trace-vitamin dose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path":
    "solutions[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "solutions[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving batch addition", "interpretation":
    "The source specifies 1 ml, not 1 G_PER_L. The vitamin stock is defined below
    JCM 1183; the trace stock is the explicitly named subsection of JCM 310/M305.
    Neither dose licenses transfer of an entire parent medium, nor does listed basal
    water establish a final ml/L denominator.", "sources": [{"locator": "HTML tr[8]",
    "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Trace vitamins
    solution (see below)\n1.0\nml", "quote_representation": "HTML tr[8] DOM text"},
    {"locator": "$.components[0].items[12]", "source_key": "togoM1268", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268", "source_raw_sha256":
    "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "source_text_sha256":
    "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a", "accessed_at":
    "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Trace vitamins solution (see below)\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M1268\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q23", "subject": "Trace-element dose", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml", "field_path": "solutions[4].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml",
    "field_path": "solutions[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Receiving batch addition", "interpretation":
    "The source specifies 1 ml, not 1 G_PER_L. The vitamin stock is defined below
    JCM 1183; the trace stock is the explicitly named subsection of JCM 310/M305.
    Neither dose licenses transfer of an entire parent medium, nor does listed basal
    water establish a final ml/L denominator.", "sources": [{"locator": "HTML tr[9]",
    "source_key": "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Trace elements
    solution (see Medium No.\n310\n)\n1.0\nml", "quote_representation": "HTML tr[9]
    DOM text"}, {"locator": "$.components[0].items[13]", "source_key": "togoM1268",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1268",
    "source_raw_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "source_text_sha256": "d1cb5dedf4c52334acfbffa1d782448508aa6f70f581693150c47b509e30680a",
    "accessed_at": "2026-10-28T08:33:54.182700Z", "exact_source_quote": "{\n          \"component_name\":
    \"Trace elements solution (see Medium [M305])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M305\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q24", "subject": "Basal sterilization and later pH", "local_fields":
    [], "decision": "evidence_only", "stage": "Source-only preparation", "interpretation":
    "JCM 1183 page default is 121 C for 15 min unless otherwise stated. Its explicit
    prose requires later stock additions with their separate sterilization and adjustment
    to pH 7.5. Retain this source-scoped default; do not import unrelated JCM 310
    parent conditions.", "sources": [{"locator": "extracted-text lines 4-4", "source_key":
    "jcm1183", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1183",
    "source_raw_sha256": "5729273d6f5d28466a9af75de77ddf4b2965530d7fcc4684ed388d4d240a9293",
    "source_text_sha256": "6e09c88e03784a3e9a9c5dde8a499a513bb0bfd7a28fa141d586b17508efd992",
    "accessed_at": "2026-10-28T08:33:54.197433Z", "exact_source_quote": "Unless otherwise
    stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\":
    \"After autoclaving, add 1 ml of 5% Na2S x 9H2O solution (autoclaved), 1 ml of
    5% CaCl2 x 2H2O solution (autoclaved) and 10 ml of 3% NaHCO3 solution (filter-sterilized).
    Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q25", "subject": "Na2MoO4・2H2O in scoped M305 dependency",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[14]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n0.03\ng",
    "quote_representation": "HTML tr[14] DOM text"}, {"locator": "$.components[1].items[1]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[6]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.123993,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "H3BO3 in scoped M305
    dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[16]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "H\n3\nBO\n3\n0.3\ng", "quote_representation":
    "HTML tr[16] DOM text"}, {"locator": "$.components[1].items[2]", "source_key":
    "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[8]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    4.85123,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "FeSO4・7H2O in scoped
    M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[9]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "FeSO\n4\n·7H\n2\nO\n2.0\ng",
    "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[1].items[3]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    7.19386,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "MnCl2・4H2O in scoped
    M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n0.03\ng",
    "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[1].items[4]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q29", "subject": "CoCl2・6H2O in scoped M305 dependency", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/togo_medium_m305.yaml", "field_path": "ingredients[9].concentration",
    "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "correct", "stage":
    "Trace-element stock, not parent basal medium or receiving final rate", "interpretation":
    "The amount belongs to the trace stock with 1 L listed water. The local dependency
    flattens it into parent ingredients; retain this amount/form under the stock.
    API J1183 explicitly gives stock g_l on its declared basis, but no final-medium
    conversion is made. Co/Ni supplied hexahydrates require separate primary-term
    repair; no unasserted secondary slot is invented.", "sources": [{"locator": "HTML
    tr[12]", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310",
    "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b",
    "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b",
    "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n0.2\ng",
    "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[1].items[5]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[4]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.54037,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "NiCl2・6H2O in scoped
    M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "NiCl\n2\n·6H\n2\nO\n0.02\ng",
    "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[1].items[6]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[5]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.154322,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "ZnSO4・7H2O in scoped
    M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[10]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "ZnSO\n4\n·7H\n2\nO\n0.1\ng",
    "quote_representation": "HTML tr[10] DOM text"}, {"locator": "$.components[1].items[7]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.347752,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q32", "subject": "CuCl2・2H2O in scoped
    M305 dependency", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[15]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "CuCl\n2\n·2H\n2\nO\n0.01\ng",
    "quote_representation": "HTML tr[15] DOM text"}, {"locator": "$.components[1].items[8]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"CuCl2・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[7]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0586569,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "EDTA in scoped M305 dependency",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace-element stock, not parent
    basal medium or receiving final rate", "interpretation": "The amount belongs to
    the trace stock with 1 L listed water. The local dependency flattens it into parent
    ingredients; retain this amount/form under the stock. API J1183 explicitly gives
    stock g_l on its declared basis, but no final-medium conversion is made. Co/Ni
    supplied hexahydrates require separate primary-term repair; no unasserted secondary
    slot is invented.", "sources": [{"locator": "HTML tr[8]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "EDTA\n5.0\ng", "quote_representation":
    "HTML tr[8] DOM text"}, {"locator": "$.components[1].items[9]", "source_key":
    "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"EDTA\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001237\",\n          \"gmo_id\": \"GMO_001237\",\n          \"label\":
    \"EDTA\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "apiJ1183", "reference": "https://mediadive.dsmz.de/rest/medium/J1183",
    "source_raw_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "source_text_sha256": "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b",
    "accessed_at": "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\":
    271,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    17.1092,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "M305 water already duplicate-collapsed",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1.0", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Two distinct source water stages",
    "interpretation": "Credit the historical equal-duplicate collapse from 2 to 1,
    but the source still gives 1 L basal water and separately 1 L trace-stock water,
    not 1 G_PER_L. Only the trace-stock water transfers here. Preserve the repair
    history while reconstructing stage and unit; do not transfer the entire parent
    water recipe.", "sources": [{"locator": "HTML tr[7]", "source_key": "jcm310",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310", "source_raw_sha256":
    "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b", "source_text_sha256":
    "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b", "accessed_at":
    "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[7] DOM text"}, {"locator": "HTML tr[17]", "source_key":
    "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310",
    "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b",
    "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b",
    "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Distilled
    water\n1.0\nL", "quote_representation": "HTML tr[17] DOM text"}, {"locator": "$.components[0].items[2]",
    "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "$.components[1].items[0]", "source_key": "togoM305",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}]}, {"decision_id": "q35", "subject": "Trace-stock HCl and pH 3",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Stock adjustment,
    quantity unspecified", "interpretation": "The source says adjust the trace stock
    to pH 3 with HCl, with no acid dose or molarity. The existing variable placeholder
    truthfully avoids a fabricated amount but needs this stock-specific pH context.
    This is not the receiving medium pH 7.5.", "sources": [{"locator": "extracted-text
    lines 114-114", "source_key": "jcm310", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=310",
    "source_raw_sha256": "021460ff89bb9bdfc6dbd8c9d6ede6531057f458b2ec3001e85e44173ec7419b",
    "source_text_sha256": "8bde07bac9516465d9614e5de0ebb97454753ba2104b9c95e6783252a669a35b",
    "accessed_at": "2026-10-28T08:33:54.181666Z", "exact_source_quote": "Adjust pH
    to 3 with HCl.", "quote_representation": "captured extracted text"}, {"locator":
    "$.components[1].items[10]", "source_key": "togoM305", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M305",
    "source_raw_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "source_text_sha256": "7212b1385938bd4c5c10fef4e62d00314015bf4e42814285ac3c084314b7d4ff",
    "accessed_at": "2026-10-28T08:33:54.151165Z", "exact_source_quote": "{\n          \"component_name\":
    \"HCl\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\":
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
    JSON object"}, {"locator": "$.data.solutions[2].steps[0]", "source_key": "apiJ1183",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1183", "source_raw_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "source_text_sha256":
    "4dc4dd80f5f9f24edf2b2576fef01e8d7c55ab1f910bec39e45c90eeea05f24b", "accessed_at":
    "2026-10-28T08:33:54.031836Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 3 with HCl.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "Excluded M305 basal ingredients
    and additions", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "7.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/togo_medium_m305.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "not_assessed", "stage": "Explicit dependency boundary",
    "interpretation": "These NaCl/phosphate/carbonate basal fields and the 20% magnesium,
    2 M KSCN and parent trace-dose stubs belong to the distinct M305/JCM 310 receiving
    medium. They are inventoried unchanged for boundary clarity and are not assessed
    or proposed for transfer into JCM 1183.", "sources": []}], "local_field_census_reference":
    "REVIEW_WORK/batch061/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml: primary 17/18, secondary
    13/18; data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml: primary
    17/18, secondary 13/18. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric
    legacy MediaIngredientMech mentions occur across the complete selected documents,
    with exact locators in the inventory; NNNNNN is a historical placeholder, not
    an ID. Complex commercial/product components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:007800
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
  - CultureMech:007800
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
  - CultureMech:007800
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-007800-water-vitamin-and-denominator-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and vitamin amounts lose units and stock stages
  description: The water row sums 1 L basal and 100 ml vitamin-stock inputs as 101
    G_PER_L. Nine stock milligram values are stored unchanged as top-level G_PER_L.
    Eight basal numbers match source grams but lack an explicit final-volume basis.
    API J1183 uses a declared 1002 ml normalization, which is not silently substituted
    for the primary source.
  target_ids:
  - CultureMech:007800
  field_paths:
  - ingredients
  evidence_ids:
  - quantity-inventory
  - jcm1183
  - togoM1268
  - apiJ1183
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-007800-stock-dose-units-and-empty-composition
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Five liquid stock additions retain mass units and empty compositions
  description: The five solution scalars are receiving volumes in ml, not grams per
    litre. Bicarbonate is 10 ml of a 3% stock; calcium and sulfide each use 1 ml of
    a 5% stock; vitamin and trace stocks each use 1 ml. Bare percent bases remain
    unspecified. Named preferred terms already provide identities, despite the generic
    Unknown solution names.
  target_ids:
  - CultureMech:007800
  field_paths:
  - solutions
  evidence_ids:
  - jcm1183
  - togoM1268
  - quantity-inventory
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-007800-missing-stage-preparation-and-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and receiving pH are absent
  description: Both selected layers omit main pH 7.5, basal autoclaving and post-autoclave
    additions. The source differentiates autoclaved sulfide/calcium stocks from filter-sterilized
    bicarbonate. Trace-stock pH 3 belongs only to JCM 310, not the receiving medium.
    Evidence for preparation and solution doses must use supported root-level scope,
    not nonexistent solution/preparation evidence slots.
  target_ids:
  - CultureMech:007800
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - jcm1183
  - jcm310
  - togoM1268
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-007800-supplied-stereochemistry-and-dependency-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: DL pantothenate and dependency hydrates differ from asserted chemical structures
  description: The source explicitly names DL-calcium pantothenate, while CHEBI:31345
    has D-form synonyms and stereospecific InChI/SMILES in the current OLS response.
    Both selected primary and secondary slots assert that ID. The scoped dependency
    separately names cobalt and nickel hexahydrates but asserts anhydrous CHEBI:35696
    and :34887 in primary slots only. Literal label checks do not establish these
    supplied-form correspondences.
  target_ids:
  - CultureMech:007800
  field_paths:
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/togo_medium_m305.yaml::ingredients[9].term
  - data/normalized_yaml/bacterial/togo_medium_m305.yaml::ingredients[10].term
  evidence_ids:
  - jcm1183
  - jcm310
  - chebi31345
  - chebi35696
  - chebi34887
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m305.yaml
    role: Scoped JCM310/M305 trace-element stock dependency; unrelated parent recipe
      excluded
- finding_id: f5
  issue_key: culturemech-007800-trace-dependency-boundary
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Referenced trace stock cannot be replaced by the full flattened parent record
  description: M305 contains an unrelated basal medium plus flattened trace ingredients
    and three other stock stubs. Only its JCM 310 trace subsection supports the receiving
    stock. Its repaired equal water duplicate is credited, but its mass-unit water
    and flat composition still need source-scoped reconstruction.
  target_ids:
  - CultureMech:007800
  field_paths:
  - solutions[4].composition
  - data/normalized_yaml/bacterial/togo_medium_m305.yaml::ingredients
  - data/normalized_yaml/bacterial/togo_medium_m305.yaml::preparation_steps
  evidence_ids:
  - jcm310
  - togoM305
  - apiJ1183
  - quantity-inventory
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m305.yaml
    role: Scoped JCM310/M305 trace-element stock dependency; unrelated parent recipe
      excluded
- finding_id: f6
  issue_key: culturemech-007800-hepes-current-secondary-coverage
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: HEPES secondary linkage has no current exact MIM row
  description: Both selected layers assert CHEBI:46756 as primary and secondary HEPES.
    Current OLS confirms the literal label but returns no formula or definition; the
    packaged MIM CSV has zero exact identifier rows. This is a current secondary-coverage
    gap, not proof that the ontology term or historical mapping was invalid.
  target_ids:
  - CultureMech:007800
  field_paths:
  - ingredients[6].mediaingredientmech_chebi_term
  evidence_ids:
  - chebi46756
  - grounding
  rule_id: mediaingredientmech-exact-identifier-linkage
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Restore source-scoped basal amounts, separate water stages and the
    complete nine-component vitamin stock. Preserve the BD-Difco qualifier and supplied
    hydrates. Resolve denominator representation explicitly; do not sum stock water
    into the medium or manufacture final-rate conversions.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
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
  description: Correct each dose to its explicit source batch-volume representation,
    preserve stock percentages with honest basis limits, and reconstruct source-supported
    composition or scoped references. Do not encode a liquid dose as a solute mass
    or infer percentage basis from current importer defaults.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
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
  description: Add the exact source-scoped preparation and pH with claim-specific
    root evidence. Preserve distinct stock sterilization and receiving stages; review
    current importer meta.ph handling and the retained comments before regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
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
  description: Resolve the explicitly racemic supplied form and exact cobalt/nickel
    hydrates against authoritative ontology and current MIM records. Preserve source
    masses and scoped stock membership; retain precise unresolved labels if no verified
    identifier is available. Do not invent secondary links or alter the formula to
    fit an existing ID.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m305.yaml
    role: Scoped JCM310/M305 trace-element stock dependency; unrelated parent recipe
      excluded
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Use only the verified trace subsection, including exact hydrates, stock
    water and pH 3/HCl adjustment. Preserve M305 historical repairs and do not transfer
    its basal carbonate, thiocyanate, magnesium solution, parent doses or parent preparation
    into JCM 1183.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m305.yaml
    role: Scoped JCM310/M305 trace-element stock dependency; unrelated parent recipe
      excluded
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action6
  description: Retain the correct source HEPES name and independently verify current
    MIM linkage support. Record unresolved current coverage explicitly rather than
    substituting an unverified identifier.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:007800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml
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
- Primary sources list absolute water inputs and later additions, not a measured final
  medium volume. API normalization is separately attributed and is not silently treated
  as physical final volume.
- Bare 3% and 5% stock strengths have no explicit percentage basis in the retrieved
  primary source. No implied solute masses or final concentrations are supplied.
- JCM 310/M305 contributes only the trace-elements subsection, its water and stock
  pH adjustment. Its unrelated basal medium, receiving doses and other stock recipes
  are outside scientific assessment.
- Current MIM rows are from packaged metadata commit 6643131b0f12ab40b66f98135245fca04027e0e9;
  current exact negatives do not establish historical invalidity.
- No experimental strain-specific growth claim was verified. All three historical
  reports were read, but their assertions do not authenticate historical raw payloads
  or executions.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
