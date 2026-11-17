# Scientific review of catonella_ureilytica_medium

- Review: 20261028T075141Z-catonella-ureilytica-medium-batch060
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:42:09.413870Z
- Finished UTC: 2026-10-28T07:51:41.013978Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM 489 identity is supported, but water and resazurin units are wrong, preparation gases are misplaced, and pH/preparation/evidence are missing. Six other declared solute rates and all asserted chemical forms are credited; the magnesium secondary link is incomplete.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch060 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009878 | data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml | generated | catonella_ureilytica_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009878 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:009878 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:009878 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:009878 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact TOGO M490 and JCM 489 identity

identity: supported. Targets: CultureMech:009878.

The source link and current JCM title exactly establish the selected complex liquid medium. The name alone is not a verified strain or growth outcome. No organism or taxonomic relabelling is proposed.

### Historical reports and current writer behavior

provenance: concern. Targets: CultureMech:009878.

All three historical reports were read. The September unit/preparation findings are reproduced from current sources; its proposed duplicate merge with a separate J489 owner remains outside this selected-owner scope and is not automatically accepted. Current TOGO parsing preserves mg, L and comments; those historical losses do not prove the current paths are broken. The current _extract_ph reads root ph, whereas the captured payload uses meta.ph, so that exact pH lookup still needs review. Current gas-item conversion still emits variable ingredients and needs a scoped review. Current merger requires exact compatible scientific content.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:009878.

All 20 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009878", "selected_concentration_field_count": 20, "selected_concentration_fields_covered": 20, "decisions": [{"decision_id": "q1", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate; source batch mass", "interpretation": "The official JCM table gives 5 g; current API J489 explicitly declares 5 g/L and matches the existing rate. Credit this provider basis, not a measured final volume inferred from 1 L water. The original mass and supplied form are retained; urea is added later from a separately sterilized stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[1]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Yeast extract\n5.0\ng", "quote_representation": "HTML tr[1] DOM text"}, {"locator": "$.components[0].items[1]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate; source batch mass", "interpretation": "The official JCM table gives 1.1 g; current API J489 explicitly declares 1.1 g/L and matches the existing rate. Credit this provider basis, not a measured final volume inferred from 1 L water. The original mass and supplied form are retained; urea is added later from a separately sterilized stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 1.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\": 5.41064,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "MgCl\n2\n·6H\n2\nO\n1.10\ng", "quote_representation": "HTML tr[3] DOM text"}, {"locator": "$.components[0].items[3]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 1.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Na2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate; source batch mass", "interpretation": "The official JCM table gives 5 g; current API J489 explicitly declares 5 g/L and matches the existing rate. Credit this provider basis, not a measured final volume inferred from 1 L water. The original mass and supplied form are retained; urea is added later from a separately sterilized stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 35.2214,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Na\n2\nHPO\n4\n5.0\ng", "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.components[0].items[4]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Na2HPO4\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001069\",\n          \"gmo_id\": \"GMO_001069\",\n          \"label\": \"Disodium phosphate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "Casitone", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate; source batch mass", "interpretation": "The official JCM table gives 20 g; current API J489 explicitly declares 20 g/L and matches the existing rate. Credit this provider basis, not a measured final volume inferred from 1 L water. The original mass and supplied form are retained; urea is added later from a separately sterilized stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Casitone (BD-Difco)\n20.0\ng", "quote_representation": "HTML tr[0] DOM text"}, {"locator": "$.components[0].items[5]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Casitone (BD-Difco)\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001104\",\n          \"gmo_id\": \"GMO_001104\",\n          \"label\": \"Bacto &amp;trade; Casitone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "Sodium thioglycolate", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate; source batch mass", "interpretation": "The official JCM table gives 0.75 g; current API J489 explicitly declares 0.75 g/L and matches the existing rate. Credit this provider basis, not a measured final volume inferred from 1 L water. The original mass and supplied form are retained; urea is added later from a separately sterilized stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sodium thioglycolate\",\n                        \"compound_id\": 1644,\n                        \"amount\": 0.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.75,\n                        \"mmol_l\": 6.57318,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[5]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Sodium thioglycolate\n0.75\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[6]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Sodium thioglycolate\",\n          \"volume\": 0.75,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001132\",\n          \"gmo_id\": \"GMO_001132\",\n          \"label\": \"Sodium thioglycolate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Urea", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate; source batch mass", "interpretation": "The official JCM table gives 1 g; current API J489 explicitly declares 1 g/L and matches the existing rate. Credit this provider basis, not a measured final volume inferred from 1 L water. The original mass and supplied form are retained; urea is added later from a separately sterilized stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Urea\",\n                        \"compound_id\": 339,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 16.6511,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[4]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Urea\n1.0\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[7]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Urea\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001133\",\n          \"gmo_id\": \"GMO_001133\",\n          \"label\": \"Urea\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Distilled water", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "absolute preparation solvent input", "interpretation": "Both sources give 1 L (1000 ml) water. Local 1 G_PER_L is a volume-to-mass category error. Preserve 1 L as an absolute preparation input, not a nutrient mass or an assumed final-medium rate. Added urea stock solvent is unspecified.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[7]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[0]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "indicator mass and explicit provider-normalized rate", "interpretation": "JCM and TOGO give 0.5 mg, while API declares 0.0005 g/L. The existing 0.5 G_PER_L is 1000 times the explicit provider rate. Preserve 0.5 mg batch mass and, if retaining provider normalization, 0.0005 G_PER_L (equivalently 0.5 MG_PER_L). No sodium-salt substitution is justified: the sources say resazurin without that qualifier.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0005,\n                        \"mmol_l\": 0.0021816,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[6]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Resazurin\n0.5\nmg", "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[2]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "conflict", "stage": "preparation atmosphere, not a dissolved-medium concentration", "interpretation": "The source specifies N2:CO2 4:1 by volume during cooling and dispensing, and N2 for urea-stock storage. These are stage-specific gas conditions, not unquantified dissolved final ingredients. Retain gas identities and exact stage/ratio in preparation; do not infer dissolved amounts, flow rate or pressure.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\": \"Mix components except urea and sodium thioglycolate, bring to a boil for a few seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add sodium thioglycolate, dispense the medium into culture vessels under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add 10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to the medium and adjust pH to 7.4.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[8]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Nitrogen gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "conflict", "stage": "preparation atmosphere, not a dissolved-medium concentration", "interpretation": "The source specifies N2:CO2 4:1 by volume during cooling and dispensing, and N2 for urea-stock storage. These are stage-specific gas conditions, not unquantified dissolved final ingredients. Retain gas identities and exact stage/ratio in preparation; do not infer dissolved amounts, flow rate or pressure.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\": \"Mix components except urea and sodium thioglycolate, bring to a boil for a few seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add sodium thioglycolate, dispense the medium into culture vessels under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add 10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to the medium and adjust pH to 7.4.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[9]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Urea stock and later addition", "local_fields": [], "decision": "unsupported", "stage": "separate filter-sterilized stock after cooling", "interpretation": "The source explicitly calls for 10% urea solution, filter sterilization and N2 storage, but does not state the percentage basis or added stock volume. Preserve the quoted 10% and later-addition instruction in preparation while leaving a quantitative stock concentration/dose unresolved. Do not assume w/v or calculate a 10 ml dose.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\": \"Mix components except urea and sodium thioglycolate, bring to a boil for a few seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add sodium thioglycolate, dispense the medium into culture vessels under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add 10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to the medium and adjust pH to 7.4.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Gas ratio, cooling, sealing and pH", "local_fields": [], "decision": "evidence_only", "stage": "ordered source preparation stages", "interpretation": "Retain the brief boil, room-temperature cooling, N2:CO2 4:1 v/v atmosphere, later thioglycolate, sealed butyl-stopper vessels, autoclaving, later urea addition and pH 7.4. There is no numeric room temperature, boiling time, gas pressure or flow to invent.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\": \"Mix components except urea and sodium thioglycolate, bring to a boil for a few seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add sodium thioglycolate, dispense the medium into culture vessels under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add 10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to the medium and adjust pH to 7.4.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[0]", "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components except urea and sodium thioglycolate, bring to a boil for a few seconds and cool to room temperature under a N2--CO2 (4:1, v/v) gasmixture. Add sodium thioglycolate, dispense the medium into culture vessels under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add 10% urea solution (filter--sterilized and stored under a N2 gas atmosphere) to the medium and adjust pH to 7.4.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "JCM sterilization default", "local_fields": [], "decision": "evidence_only", "stage": "source-wide default for the autoclaved main stage", "interpretation": "JCM specifies 121°C for 15 min unless otherwise stated. Apply this only to the source autoclave stage; the explicitly filter-sterilized urea stock is an exception.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch060/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:009878.

data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml: primary 8/10, secondary 5/10; data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml: primary 8/10, secondary 5/10. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:009878.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:009878.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Water and resazurin have incorrect units

major / open / confirmed; issue key: culturemech-009878-water-and-resazurin-source-unit-errors.

Both selected layers encode 1 L water as 1 G_PER_L and 0.5 mg resazurin as 0.5 G_PER_L. These are direct source-unit errors, independently supported by JCM, TOGO and API J489. The other six nongaseous solute rates match the explicit API basis.

### f2: Preparation atmospheres became variable final ingredients

major / open / confirmed; issue key: culturemech-009878-preparation-gases-as-final-ingredients.

CO2 and N2 are source preparation and stock-storage atmospheres. Their variable ingredient rows obscure the specified gas mixture and stages. Current TOGO _ingredient_from_item deliberately emits VARIABLE gas entries, so this remaining scope behavior warrants review even though current unit/comment handling is improved.

### f3: The complete source preparation and pH are missing

major / open / confirmed; issue key: culturemech-009878-missing-preparation-ph-and-evidence.

Neither selected layer retains pH 7.4, the ordered gas/sterilization/addition procedure or claim-level evidence. The unresolved urea percentage basis and stock volume must stay unresolved; the primary source still supports the explicit stages.

### f4: The correct magnesium hexahydrate primary lacks its secondary link

minor / open / confirmed; issue key: culturemech-009878-missing-magnesium-hexahydrate-secondary-link.

MgCl2·6H2O is correctly grounded to CHEBI:86345 in the primary slot, and its exact current OLS formula and MIM rows agree. The secondary slot is absent. This is incomplete linkage, not a wrong salt or amount. Other asserted primary and secondary IDs have correct labels; no numeric legacy IDs occur.

## Recommended Actions And Acceptance Checks

### action1

Repair the maintained water representation as an absolute preparation volume and the resazurin rate using the exact source mass and provider basis. Preserve other supported amounts and avoid claiming measured final volume.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Represent the gas identities, ratio and stages in preparation metadata rather than implying an unspecified final dissolved dose. Review the current gas-item conversion independently of the already corrected unit parser.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the source-supported preparation and pH to the maintained owner, with root evidence scoped to each stage and ingredient evidence for each amount. Preserve the literal 10% stock as unconverted source prose. Append current verified curation history only when changes are actually made.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Add only the verified same-form secondary correspondence after reviewing current MIM evidence; preserve the correct primary, hydrate and amount.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch060/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch060/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch060/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch060/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm489 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current official JCM page read, including the main and embedded stock tables, preparation and source-specific defaults. The page-wide default remains scoped to that source; named stock sections are separate from main-medium preparation. |
| togoM490 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16199 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16199 = urea; definition ['A carbonyl group with two C-bound amine groups. The commercially available fertilizer has an analysis of 46-0-0 (N-P2O5-K2O).']; formula ['CH4N2O']; mass ['60.056']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon compound with formula CO&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt; in which the carbon is attached to each oxygen atom by a double bond. A colourless, odourless gas under normal conditions, it is produced during respiration by all animals, fungi and microorganisms that depend directly or indirectly on living or decaying plants for food.']; formula ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34683 = disodium hydrogenphosphate; definition []; formula ['HO4P.2Na']; mass ['141.958']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86481 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86481 = sodium thioglycolate; definition ['An organic sodium salt having thioglycolate(1−) as the counterion.']; formula ['C2H3O2S.Na']; mass ['114.101']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| apiJ489 | https://mediadive.dsmz.de/rest/medium/J489; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| grounding | REVIEW_WORK/batch060/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T043637Z-CATONELLA_UREILYTICA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch060/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer22 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace deprecated secondary MIM links or authenticate quantities. |
| writer23 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components preserves primary versus nested sections, _parse_unit distinguishes mg/ml/L, and _extract_preparation_steps retains comments. However _extract_ph reads a root ph value while this captured M490 payload stores meta.ph; that shape can still lose pH. Gas items are retained as VARIABLE ingredients and require stage review. Current code does not prove historical execution. |
| writer24 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer25 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer26 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch060/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The bare 10% urea stock has no specified percentage basis or dose. Listed water is an absolute input, not proof of measured final volume.
- The separately named J489 normalized counterpart in an old report was not reassessed here; no automatic duplicate merge or transfer of its claims is proposed.
- Collection formulation instructions do not establish a named strain, measured growth outcome or culture optimization.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T075141Z-catonella-ureilytica-medium-batch060
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of catonella_ureilytica_medium
started_at: '2026-10-28T07:42:09.413870Z'
finished_at: '2026-10-28T07:51:41.013978Z'
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
summary: The exact JCM 489 identity is supported, but water and resazurin units are
  wrong, preparation gases are misplaced, and pH/preparation/evidence are missing.
  Six other declared solute rates and all asserted chemical forms are credited; the
  magnesium secondary link is incomplete.
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
  - path: data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
    sha256: c687836dcea0dd8d44593e083131e7d92a97675efd5935d9e93ab0bc4d354764
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
    sha256: b0a391449a9c744986cab4087a0b13e30e4352ed9f530394e61c62e6c9fde8b5
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.md
    sha256: c74208aa8d5e311a3e8f9d19cfc6488aaec86106dff8dc599f20cc0c6ba31227
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.md
    sha256: c2a462a8895d3a55d792be2094bdac32fc6aafa83eb1820557f50845484bbdf8
    role: context
  - path: reports/yaml_record_review/20260922T043637Z-CATONELLA_UREILYTICA_MEDIUM.md
    sha256: eb1c7e1cbb207d3dd29a50a6e47baa7c45cdf2633a596abbfacbf91d2f333c6c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
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
  selection: Authoritative batch060 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009878
targets:
- target_id: CultureMech:009878
  path: data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
  label: catonella_ureilytica_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009878
  command: just validate-schema data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009878
  command: just validate-strict data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch060/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009878
  command: just validate-terms data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:009878
  command: just validate-references data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:48:31.618462Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: c687836dcea0dd8d44593e083131e7d92a97675efd5935d9e93ab0bc4d354764
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:48:31.618597Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: b0a391449a9c744986cab4087a0b13e30e4352ed9f530394e61c62e6c9fde8b5
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:10.508192Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 90a6627dd6c26361ac9faeeca060ddacef6cd1cec35d1868d8342782428a835c
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:11.443250Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: f3966332dd9c7e29d5ea47f10f16cc998cef1e0e9028227b04de4145e7829685
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:12.941287Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 5526623a68e7b5de7794d7b920e4c5bf04964a1d85b2bad88f40124af5fc28be
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch060/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:13.720770Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 7bed90f284dea2d1877b3b0a0a302055c873cfdaf1c45311e1f6ab78dd758f45
- evidence_id: jcm489
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:04.348129Z'
  support: supports
  summary: Complete current official JCM page read, including the main and embedded
    stock tables, preparation and source-specific defaults. The page-wide default
    remains scoped to that source; named stock sections are separate from main-medium
    preparation.
  snapshot_sha256: 8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958
- evidence_id: togoM490
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:04.348384Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: 125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:04.348480Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16199
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:04.348543Z'
  support: supports
  summary: OLS current exact CHEBI:16199 = urea; definition ['A carbonyl group with
    two C-bound amine groups. The commercially available fertilizer has an analysis
    of 46-0-0 (N-P2O5-K2O).']; formula ['CH4N2O']; mass ['60.056']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5298ca6b7d402b8a6e2091f03adf139a2d777c9614d760976b3953bc88bd862e
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:04.348586Z'
  support: supports
  summary: OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon
    compound with formula CO<small><sub>2</sub></small> in which the carbon is attached
    to each oxygen atom by a double bond. A colourless, odourless gas under normal
    conditions, it is produced during respiration by all animals, fungi and microorganisms
    that depend directly or indirectly on living or decaying plants for food.']; formula
    ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:04.348621Z'
  support: supports
  summary: OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule
    consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:05.120761Z'
  support: supports
  summary: OLS current exact CHEBI:34683 = disodium hydrogenphosphate; definition
    []; formula ['HO4P.2Na']; mass ['141.958']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:05.339301Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86481
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:05.347703Z'
  support: supports
  summary: OLS current exact CHEBI:86481 = sodium thioglycolate; definition ['An organic
    sodium salt having thioglycolate(1−) as the counterion.']; formula ['C2H3O2S.Na'];
    mass ['114.101']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 444afd61f333b50a1be0a902c67c78c7b97483187e4fb554b6f7deeb009cd966
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:05.376560Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: apiJ489
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J489
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:45:48.296539Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch060/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T07:48:31.621054Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 741f680364b2539ea5688d7c42e075cc25c18cdddedc7849de08697e0207c4a6
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T043637Z-CATONELLA_UREILYTICA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:48:31.621370Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: eb1c7e1cbb207d3dd29a50a6e47baa7c45cdf2633a596abbfacbf91d2f333c6c
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:48:31.621390Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: c2a462a8895d3a55d792be2094bdac32fc6aafa83eb1820557f50845484bbdf8
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:48:31.621408Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: c74208aa8d5e311a3e8f9d19cfc6488aaec86106dff8dc599f20cc0c6ba31227
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch060/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T07:48:31.621426Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 5b190f14cee0083ab5920d62e42533ad73867e373b588df13afa1349d1b81df4
- evidence_id: writer22
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:48:31.621446Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace deprecated secondary MIM links
    or authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer23
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:48:31.621474Z'
  support: context_only
  summary: Current _extract_primary_components preserves primary versus nested sections,
    _parse_unit distinguishes mg/ml/L, and _extract_preparation_steps retains comments.
    However _extract_ph reads a root ph value while this captured M490 payload stores
    meta.ph; that shape can still lose pH. Gas items are retained as VARIABLE ingredients
    and require stage review. Current code does not prove historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer24
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:48:31.621490Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer25
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:48:31.621508Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer26
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:48:31.621527Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch060/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T07:48:31.625247Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: d0b446346ebde56e7c784ed660869ded4c2a436dd60c5dca0c369b0799ac8353
assessments:
- assessment_id: a1
  area: identity
  topic: Exact TOGO M490 and JCM 489 identity
  outcome: supported
  summary: The source link and current JCM title exactly establish the selected complex
    liquid medium. The name alone is not a verified strain or growth outcome. No organism
    or taxonomic relabelling is proposed.
  target_ids:
  - CultureMech:009878
  evidence_ids:
  - jcm489
  - togoM490
  - apiJ489
- assessment_id: a2
  area: provenance
  topic: Historical reports and current writer behavior
  outcome: concern
  summary: All three historical reports were read. The September unit/preparation
    findings are reproduced from current sources; its proposed duplicate merge with
    a separate J489 owner remains outside this selected-owner scope and is not automatically
    accepted. Current TOGO parsing preserves mg, L and comments; those historical
    losses do not prove the current paths are broken. The current _extract_ph reads
    root ph, whereas the captured payload uses meta.ph, so that exact pH lookup still
    needs review. Current gas-item conversion still emits variable ingredients and
    needs a scoped review. Current merger requires exact compatible scientific content.
  target_ids:
  - CultureMech:009878
  evidence_ids:
  - history-auth
  - writer22
  - writer23
  - writer24
  - writer25
  - writer26
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 20 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:009878
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009878",
    "selected_concentration_field_count": 20, "selected_concentration_fields_covered":
    20, "decisions": [{"decision_id": "q1", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate;
    source batch mass", "interpretation": "The official JCM table gives 5 g; current
    API J489 explicitly declares 5 g/L and matches the existing rate. Credit this
    provider basis, not a measured final volume inferred from 1 L water. The original
    mass and supplied form are retained; urea is added later from a separately sterilized
    stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "HTML tr[1]", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489",
    "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958",
    "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f",
    "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Yeast extract\n5.0\ng",
    "quote_representation": "HTML tr[1] DOM text"}, {"locator": "$.components[0].items[1]",
    "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "1.1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate;
    source batch mass", "interpretation": "The official JCM table gives 1.1 g; current
    API J489 explicitly declares 1.1 g/L and matches the existing rate. Credit this
    provider basis, not a measured final volume inferred from 1 L water. The original
    mass and supplied form are retained; urea is added later from a separately sterilized
    stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 1.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\":
    5.41064,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "MgCl\n2\n·6H\n2\nO\n1.10\ng",
    "quote_representation": "HTML tr[3] DOM text"}, {"locator": "$.components[0].items[3]",
    "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 1.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q3", "subject": "Na2HPO4", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate;
    source batch mass", "interpretation": "The official JCM table gives 5 g; current
    API J489 explicitly declares 5 g/L and matches the existing rate. Credit this
    provider basis, not a measured final volume inferred from 1 L water. The original
    mass and supplied form are retained; urea is added later from a separately sterilized
    stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\":
    233,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    35.2214,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Na\n2\nHPO\n4\n5.0\ng",
    "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.components[0].items[4]",
    "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2HPO4\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001069\",\n          \"gmo_id\": \"GMO_001069\",\n          \"label\":
    \"Disodium phosphate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject":
    "Casitone", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate;
    source batch mass", "interpretation": "The official JCM table gives 20 g; current
    API J489 explicitly declares 20 g/L and matches the existing rate. Credit this
    provider basis, not a measured final volume inferred from 1 L water. The original
    mass and supplied form are retained; urea is added later from a separately sterilized
    stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\":
    84,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    20,\n                        \"unit\": \"g\",\n                        \"g_l\":
    20,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Casitone (BD-Difco)\n20.0\ng",
    "quote_representation": "HTML tr[0] DOM text"}, {"locator": "$.components[0].items[5]",
    "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Casitone (BD-Difco)\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001104\",\n          \"gmo_id\": \"GMO_001104\",\n          \"label\":
    \"Bacto &trade; Casitone\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject":
    "Sodium thioglycolate", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate;
    source batch mass", "interpretation": "The official JCM table gives 0.75 g; current
    API J489 explicitly declares 0.75 g/L and matches the existing rate. Credit this
    provider basis, not a measured final volume inferred from 1 L water. The original
    mass and supplied form are retained; urea is added later from a separately sterilized
    stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Sodium thioglycolate\",\n                        \"compound_id\":
    1644,\n                        \"amount\": 0.75,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.75,\n                        \"mmol_l\":
    6.57318,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[5]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Sodium thioglycolate\n0.75\ng",
    "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[6]",
    "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Sodium thioglycolate\",\n          \"volume\": 0.75,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001132\",\n          \"gmo_id\": \"GMO_001132\",\n          \"label\":
    \"Sodium thioglycolate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject":
    "Urea", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "declared main-medium rate;
    source batch mass", "interpretation": "The official JCM table gives 1 g; current
    API J489 explicitly declares 1 g/L and matches the existing rate. Credit this
    provider basis, not a measured final volume inferred from 1 L water. The original
    mass and supplied form are retained; urea is added later from a separately sterilized
    stock, and thioglycolate follows cooling.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Urea\",\n                        \"compound_id\":
    339,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    16.6511,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[4]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Urea\n1.0\ng", "quote_representation":
    "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[7]", "source_key":
    "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Urea\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001133\",\n          \"gmo_id\": \"GMO_001133\",\n          \"label\":
    \"Urea\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject":
    "Distilled water", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "absolute preparation solvent input",
    "interpretation": "Both sources give 1 L (1000 ml) water. Local 1 G_PER_L is a
    volume-to-mass category error. Preserve 1 L as an absolute preparation input,
    not a nutrient mass or an assumed final-medium rate. Added urea stock solvent
    is unspecified.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key":
    "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256":
    "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256":
    "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at":
    "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[7]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[0]",
    "source_key": "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "Resazurin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "indicator mass and explicit provider-normalized
    rate", "interpretation": "JCM and TOGO give 0.5 mg, while API declares 0.0005
    g/L. The existing 0.5 G_PER_L is 1000 times the explicit provider rate. Preserve
    0.5 mg batch mass and, if retaining provider normalization, 0.0005 G_PER_L (equivalently
    0.5 MG_PER_L). No sodium-salt substitution is justified: the sources say resazurin
    without that qualifier.", "sources": [{"locator": "$.data.solutions[0].recipe[6]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0005,\n                        \"mmol_l\":
    0.0021816,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[6]", "source_key": "jcm489", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489", "source_raw_sha256":
    "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958", "source_text_sha256":
    "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f", "accessed_at":
    "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Resazurin\n0.5\nmg", "quote_representation":
    "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[2]", "source_key":
    "togoM490", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "Carbon dioxide gas", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "variable", "unit": "VARIABLE"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "conflict", "stage": "preparation atmosphere,
    not a dissolved-medium concentration", "interpretation": "The source specifies
    N2:CO2 4:1 by volume during cooling and dispensing, and N2 for urea-stock storage.
    These are stage-specific gas conditions, not unquantified dissolved final ingredients.
    Retain gas identities and exact stage/ratio in preparation; do not infer dissolved
    amounts, flow rate or pressure.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix components except urea and sodium thioglycolate, bring to a boil for a few
    seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add
    sodium thioglycolate, dispense the medium into culture vessels under the same
    gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add
    10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to
    the medium and adjust pH to 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[8]", "source_key": "togoM490",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q10", "subject": "Nitrogen gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "conflict", "stage": "preparation atmosphere,
    not a dissolved-medium concentration", "interpretation": "The source specifies
    N2:CO2 4:1 by volume during cooling and dispensing, and N2 for urea-stock storage.
    These are stage-specific gas conditions, not unquantified dissolved final ingredients.
    Retain gas identities and exact stage/ratio in preparation; do not infer dissolved
    amounts, flow rate or pressure.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix components except urea and sodium thioglycolate, bring to a boil for a few
    seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add
    sodium thioglycolate, dispense the medium into culture vessels under the same
    gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add
    10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to
    the medium and adjust pH to 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[9]", "source_key": "togoM490",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490",
    "source_raw_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "source_text_sha256": "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a",
    "accessed_at": "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n          \"component_name\":
    \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q11", "subject": "Urea stock and later addition", "local_fields": [], "decision":
    "unsupported", "stage": "separate filter-sterilized stock after cooling", "interpretation":
    "The source explicitly calls for 10% urea solution, filter sterilization and N2
    storage, but does not state the percentage basis or added stock volume. Preserve
    the quoted 10% and later-addition instruction in preparation while leaving a quantitative
    stock concentration/dose unresolved. Do not assume w/v or calculate a 10 ml dose.",
    "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ489",
    "reference": "https://mediadive.dsmz.de/rest/medium/J489", "source_raw_sha256":
    "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "source_text_sha256":
    "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0", "accessed_at":
    "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix components except urea and sodium thioglycolate, bring to a boil for a few
    seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add
    sodium thioglycolate, dispense the medium into culture vessels under the same
    gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add
    10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to
    the medium and adjust pH to 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "Gas ratio, cooling, sealing
    and pH", "local_fields": [], "decision": "evidence_only", "stage": "ordered source
    preparation stages", "interpretation": "Retain the brief boil, room-temperature
    cooling, N2:CO2 4:1 v/v atmosphere, later thioglycolate, sealed butyl-stopper
    vessels, autoclaving, later urea addition and pH 7.4. There is no numeric room
    temperature, boiling time, gas pressure or flow to invent.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "apiJ489", "reference": "https://mediadive.dsmz.de/rest/medium/J489",
    "source_raw_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "source_text_sha256": "c29284bc0dcaef0ecaf86a8ec1a474e528b1a3856ae57287bedacfecb03ec8d0",
    "accessed_at": "2026-10-28T07:45:48.296539Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix components except urea and sodium thioglycolate, bring to a boil for a few
    seconds and cool to room temperature under a N2-CO2 (4:1, v/v) gas mixture. Add
    sodium thioglycolate, dispense the medium into culture vessels under the same
    gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add
    10% urea solution (filter-sterilized and stored under a N2 gas atmosphere) to
    the medium and adjust pH to 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.comments[0]", "source_key": "togoM490", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M490", "source_raw_sha256":
    "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "source_text_sha256":
    "125cce9019d02567e6258c3c7f4771e2b5ece06843fae2895efd29f565ad1f7a", "accessed_at":
    "2026-10-28T07:43:04.348384Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components except urea and sodium thioglycolate,
    bring to a boil for a few seconds and cool to room temperature under a N2--CO2
    (4:1, v/v) gasmixture. Add sodium thioglycolate, dispense the medium into culture
    vessels under the same gas mixture, seal with butyl rubber stoppers and autoclave.
    After cooling, add 10% urea solution (filter--sterilized and stored under a N2
    gas atmosphere) to the medium and adjust pH to 7.4.\"\n    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "JCM sterilization default",
    "local_fields": [], "decision": "evidence_only", "stage": "source-wide default
    for the autoclaved main stage", "interpretation": "JCM specifies 121°C for 15
    min unless otherwise stated. Apply this only to the source autoclave stage; the
    explicitly filter-sterilized urea stock is an exception.", "sources": [{"locator":
    "extracted-text lines 4-4", "source_key": "jcm489", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=489",
    "source_raw_sha256": "8cb44860cc2c35e94b7d510a60be0c7a3eaf21f8ccb7a860a019500e75bc4958",
    "source_text_sha256": "46ff06586f6540cbb2035906da03c08b4052cef5bfaf26fd9de39cff7b54018f",
    "accessed_at": "2026-10-28T07:43:04.348129Z", "exact_source_quote": "Unless otherwise
    stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation":
    "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch060/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml: primary 8/10,
    secondary 5/10; data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml:
    primary 8/10, secondary 5/10. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:009878
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
  - CultureMech:009878
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
  - CultureMech:009878
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009878-water-and-resazurin-source-unit-errors
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and resazurin have incorrect units
  description: Both selected layers encode 1 L water as 1 G_PER_L and 0.5 mg resazurin
    as 0.5 G_PER_L. These are direct source-unit errors, independently supported by
    JCM, TOGO and API J489. The other six nongaseous solute rates match the explicit
    API basis.
  target_ids:
  - CultureMech:009878
  field_paths:
  - ingredients[0].concentration
  - ingredients[2].concentration
  evidence_ids:
  - jcm489
  - togoM490
  - apiJ489
  rule_id: source-unit-and-denominator-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-009878-preparation-gases-as-final-ingredients
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Preparation atmospheres became variable final ingredients
  description: CO2 and N2 are source preparation and stock-storage atmospheres. Their
    variable ingredient rows obscure the specified gas mixture and stages. Current
    TOGO _ingredient_from_item deliberately emits VARIABLE gas entries, so this remaining
    scope behavior warrants review even though current unit/comment handling is improved.
  target_ids:
  - CultureMech:009878
  field_paths:
  - ingredients[8]
  - ingredients[9]
  - preparation_steps
  evidence_ids:
  - togoM490
  - jcm489
  - apiJ489
  rule_id: source-preparation-versus-formulation-scope
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-009878-missing-preparation-ph-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The complete source preparation and pH are missing
  description: Neither selected layer retains pH 7.4, the ordered gas/sterilization/addition
    procedure or claim-level evidence. The unresolved urea percentage basis and stock
    volume must stay unresolved; the primary source still supports the explicit stages.
  target_ids:
  - CultureMech:009878
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - jcm489
  - apiJ489
  - togoM490
  rule_id: source-preparation-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-009878-missing-magnesium-hexahydrate-secondary-link
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The correct magnesium hexahydrate primary lacks its secondary link
  description: MgCl2·6H2O is correctly grounded to CHEBI:86345 in the primary slot,
    and its exact current OLS formula and MIM rows agree. The secondary slot is absent.
    This is incomplete linkage, not a wrong salt or amount. Other asserted primary
    and secondary IDs have correct labels; no numeric legacy IDs occur.
  target_ids:
  - CultureMech:009878
  field_paths:
  - ingredients[3].mediaingredientmech_chebi_term
  evidence_ids:
  - chebi86345
  - grounding
  rule_id: P3.2
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Repair the maintained water representation as an absolute preparation
    volume and the resazurin rate using the exact source mass and provider basis.
    Preserve other supported amounts and avoid claiming measured final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009878
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
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
  description: Represent the gas identities, ratio and stages in preparation metadata
    rather than implying an unspecified final dissolved dose. Review the current gas-item
    conversion independently of the already corrected unit parser.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009878
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
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
  description: Add the source-supported preparation and pH to the maintained owner,
    with root evidence scoped to each stage and ingredient evidence for each amount.
    Preserve the literal 10% stock as unconverted source prose. Append current verified
    curation history only when changes are actually made.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009878
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
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
  description: Add only the verified same-form secondary correspondence after reviewing
    current MIM evidence; preserve the correct primary, hydrate and amount.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009878
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml
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
- The bare 10% urea stock has no specified percentage basis or dose. Listed water
  is an absolute input, not proof of measured final volume.
- The separately named J489 normalized counterpart in an old report was not reassessed
  here; no automatic duplicate merge or transfer of its claims is proposed.
- Collection formulation instructions do not establish a named strain, measured growth
  outcome or culture optimization.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
