# Scientific review of by_medium

- Review: 20261028T041305Z-by-medium-batch054
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:00:14.824332Z
- Finished UTC: 2026-10-28T04:13:05.065648Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BY identity is supported, but the target and owner lose milligram and liquid-volume units, the SL-10 stock boundary, pH and preparation. The current local M433 dependency itself has scoped unit and hydrate problems. All selected amounts and delegated stock amounts were assessed without inventing a final-volume denominator.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch054 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009522 | data/merge_yaml/merged/BY_Medium.yaml | generated | by_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009522 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:009522 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:009522 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:009522 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### BY and its exact stock dependency

identity: supported. Targets: CultureMech:009522.

The sole maintained owner and generated target represent TOGO M3005 / JCM1330. Current primary and provider agree on the listed ingredients and preparation. The JCM 433 relationship delegates SL-10 only; its main medium and vitamin solution are not BY ingredients.

### Historical reports and present writer behavior

provenance: concern. Targets: CultureMech:009522.

Historical reports correctly raised missing preparation and unit loss, but their implied litre arithmetic is not independent final-volume evidence. Current TOGO code handles mg/ml separately and retains primary comments and stock references; the observed old output must be repaired without claiming that current code still performs the historical flattening. Current conservative merge guards should preserve the corrected scientific fields.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:009522.

All 30 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009522", "selected_concentration_field_count": 30, "selected_concentration_fields_covered": 30, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "700", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "700", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main recipe batch", "interpretation": "Both sources specify 700 ml as a liquid addition, not 700 g. Restore the volume unit without assuming density. The 700 ml water and 300 ml rumen-fluid inputs plus stock addition do not establish measured final volume.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Distilled water\n700.0\nml", "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[0].items[0]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 700,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[4]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n0.2\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[1]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"MgSO4·7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[8]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Yeast extract\n1.0\ng", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[2]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[0]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "NaCl\n1.0\ng", "quote_representation": "HTML tr[0] DOM text"}, {"locator": "$.components[0].items[3]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "CaCl2·2H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.13", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.13", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[3]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "CaCl\n2\n·2H\n2\nO\n0.13\ng", "quote_representation": "HTML tr[3] DOM text"}, {"locator": "$.components[0].items[4]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.13,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[5]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "KH\n2\nPO\n4\n1.0\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[5]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[1]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "K\n2\nHPO\n4\n0.5\ng", "quote_representation": "HTML tr[1] DOM text"}, {"locator": "$.components[0].items[6]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main recipe batch", "interpretation": "Both sources specify 1 mg resazurin, equivalent to 0.001 g per batch. The local 1 G_PER_L conflates milligrams with grams and adds an unproven final-volume denominator. Correct the source mass and basis together; the source does not specify sodium resazurin, so the neutral CHEBI:8806 form is not itself contradicted here.", "sources": [{"locator": "HTML tr[12]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Resazurin\n1.0\nmg", "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[0].items[7]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "NaHCO3", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported. Add this component after boiling and cooling under carbon dioxide, as specified by the primary preparation.", "sources": [{"locator": "HTML tr[9]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "NaHCO\n3\n5.0\ng", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[8]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[2]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "(NH\n4\n)\n2\nSO\n4\n0.25\ng", "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.components[0].items[9]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"(NH4)2SO4\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\": \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Cellobiose", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML tr[7]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Cellobiose\n5.0\ng", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[10]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"Cellobiose\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001137\",\n          \"gmo_id\": \"GMO_001137\",\n          \"label\": \"Cellobiose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Rumen fluid, clarified (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "300", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "300", "unit": "G_PER_L"}}], "decision": "correct", "stage": "main recipe batch", "interpretation": "Both sources specify 300 ml as a liquid addition, not 300 g. Restore the volume unit without assuming density. The 700 ml water and 300 ml rumen-fluid inputs plus stock addition do not establish measured final volume.", "sources": [{"locator": "HTML tr[6]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Rumen fluid, clarified (see below)\n300.0\nml", "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[11]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"Rumen fluid, clarified (see below)\",\n          \"volume\": 300,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001534\",\n          \"gmo_id\": \"GMO_001534\",\n          \"label\": \"Rumen fluid (clarified)\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "L-Cysteine·HCl·H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The primary and current TOGO agree on this mass per listed recipe batch. The stored numerical value matches that batch mass, but neither source states a measured final volume or a per-litre basis. Preserve the source batch amount and supplied form; the G_PER_L denominator remains unsupported. Add this component after boiling and cooling under carbon dioxide, as specified by the primary preparation.", "sources": [{"locator": "HTML tr[10]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "L-Cysteine·HCl·H\n2\nO\n0.5\ng", "quote_representation": "HTML tr[10] DOM text"}, {"locator": "$.components[0].items[12]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"L-Cysteine·HCl·H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001205\",\n          \"gmo_id\": \"GMO_001205\",\n          \"label\": \"L-Cysteine hydrochloride monohydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "not_quantified", "stage": "preparation atmosphere", "interpretation": "The source gas has no numeric dose. Retain that honest lack of quantification and represent the gas stream in preparation; do not replace VARIABLE with a guessed concentration.", "sources": [{"locator": "$.components[0].items[14]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"CO2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[1]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except NaHCO3 and L-Cysteine·HCl·H2O. Bring to a boil and cool under CO2 gas stream, then add NaHCO3 and L-Cysteine·HCl·H2O to the medium. Dispense the medium into suitable culture vessels under a stream of CO2, seal with butyl rubber stoppers, and autoclave.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "SL-10 working addition", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "working stock addition", "interpretation": "JCM1330 and TOGO specify 1 ml of the SL-10 stock. The local empty Unknown solution and 1 G_PER_L do not encode this volume or stock composition. Resolve only the explicitly delegated SL-10 subsection of JCM 433; no other parent-medium recipe transfers.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Trace element solution SL-10 (see Medium No.\n433\n)\n1.0\nml", "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[0].items[13]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\": \"Trace element solution SL--10 (see Medium [M433])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M433\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "SL-10 stock: HCl (25%, 7.7 M)", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 10.0 ml for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum. The HCl descriptor explicitly gives 7.7 M and bare 25%; the percentage basis is unspecified, so do not relabel it w/v or v/v.", "sources": [{"locator": "HTML tr[9]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "HCl (25%, 7.7 M)\n10.0\nml", "quote_representation": "HTML tr[9] DOM text"}]}, {"decision_id": "q17", "subject": "SL-10 stock: FeCl2·4H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 1.5 g for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum.", "sources": [{"locator": "HTML tr[10]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "FeCl\n2\n·4H\n2\nO\n1.5\ng", "quote_representation": "HTML tr[10] DOM text"}]}, {"decision_id": "q18", "subject": "SL-10 stock: ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "70", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 70.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "ZnCl\n2\n70.0\nmg", "quote_representation": "HTML tr[11] DOM text"}]}, {"decision_id": "q19", "subject": "SL-10 stock: MnCl2·4H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 100.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum.", "sources": [{"locator": "HTML tr[12]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n100.0\nmg", "quote_representation": "HTML tr[12] DOM text"}]}, {"decision_id": "q20", "subject": "SL-10 stock: H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "6", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 6.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "H\n3\nBO\n3\n6.0\nmg", "quote_representation": "HTML tr[13] DOM text"}]}, {"decision_id": "q21", "subject": "SL-10 stock: CoCl2·6H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "190", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 190.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum. The source explicitly supplies the hexahydrate, while the scoped local dependency primary CHEBI term denotes the anhydrous chloride. Resolve the supplied form; no secondary MIM slot exists for this particular dependency ingredient.", "sources": [{"locator": "HTML tr[14]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n190.0\nmg", "quote_representation": "HTML tr[14] DOM text"}]}, {"decision_id": "q22", "subject": "SL-10 stock: CuCl2·2H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 2.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum.", "sources": [{"locator": "HTML tr[15]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "CuCl\n2\n·2H\n2\nO\n2.0\nmg", "quote_representation": "HTML tr[15] DOM text"}]}, {"decision_id": "q23", "subject": "SL-10 stock: NiCl2·6H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "24", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 24.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum. The source explicitly supplies the hexahydrate, while the scoped local dependency primary CHEBI term denotes the anhydrous chloride. Resolve the supplied form; no secondary MIM slot exists for this particular dependency ingredient.", "sources": [{"locator": "HTML tr[16]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "NiCl\n2\n·6H\n2\nO\n24.0\nmg", "quote_representation": "HTML tr[16] DOM text"}]}, {"decision_id": "q24", "subject": "SL-10 stock: Na2MoO4·2H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "36", "unit": "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 36.0 mg for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum.", "sources": [{"locator": "HTML tr[17]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n36.0\nmg", "quote_representation": "HTML tr[17] DOM text"}]}, {"decision_id": "q25", "subject": "SL-10 stock: Distilled water", "local_fields": [], "decision": "add", "stage": "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies 990.0 ml for this stock batch. This is stock composition, not the receiving BY dose or final-medium concentration. The separately specified BY addition is 1 ml. The source lists water and acid inputs without an explicit measured stock final volume; do not infer final dilution from their sum. The local parent water row combines several parent sections, so it cannot stand in for this 990 ml stock-water input.", "sources": [{"locator": "HTML tr[18]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "Distilled water\n990.0\nml", "quote_representation": "HTML tr[18] DOM text"}]}, {"decision_id": "q26", "subject": "pH", "local_fields": [], "decision": "add", "stage": "main preparation", "interpretation": "The primary explicitly sets pH 7.0; both selected documents omit it. This is a preparation target, not a growth result.", "sources": [{"locator": "$.comments[0]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 7.0\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "Main preparation", "local_fields": [], "decision": "add", "stage": "main preparation", "interpretation": "Restore the explicit ordering: mix except bicarbonate and cysteine hydrochloride monohydrate, boil and cool under carbon dioxide, add those components, dispense under carbon dioxide, seal with butyl rubber stoppers and autoclave. No numeric gas dose or incubation condition is supplied.", "sources": [{"locator": "$.comments[1]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except NaHCO3 and L-Cysteine·HCl·H2O. Bring to a boil and cool under CO2 gas stream, then add NaHCO3 and L-Cysteine·HCl·H2O to the medium. Dispense the medium into suitable culture vessels under a stream of CO2, seal with butyl rubber stoppers, and autoclave.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Clarified rumen-fluid preparation", "local_fields": [], "decision": "add", "stage": "rumen stock preparation", "interpretation": "Rumen-fluid stock preparation is explicitly 120 C for 15 minutes followed by 25,000 × g for 15 minutes. Do not substitute the generic page autoclave default for this stock-specific treatment.", "sources": [{"locator": "$.comments[2]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\": 4,\n      \"comment\": \"To prepare the clarified rumen fluid, preheat rumen content at 120C for 15 min. Use the supernatant after centrifuging at 25,000 x g for 15 min.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Primary page sterilization default", "local_fields": [], "decision": "add", "stage": "main-medium sterilization", "interpretation": "The JCM1330 page default is 121 C for 15 minutes unless otherwise stated. Its main preparation says autoclave without a different numeric cycle; the explicit rumen-fluid treatment remains 120 C for 15 minutes.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330", "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71", "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b", "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject": "SL-10 dissolution order", "local_fields": [], "decision": "add", "stage": "scoped stock preparation", "interpretation": "Dissolve ferrous chloride tetrahydrate in hydrochloric acid first, then dilute with distilled water and add the remaining salts. This instruction belongs to SL-10 only. Exclude JCM 433 main solutions, vitamins and their sterilization instructions.", "sources": [{"locator": "extracted-text lines 105-109", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "Dissolve FeCl\n2\n·4H\n2\nO first in HCl. Then dilute in distilled water and add the remaining salts.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch054/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:009522.

data/merge_yaml/merged/BY_Medium.yaml: primary 11/14, secondary 10/14; data/normalized_yaml/bacterial/by_medium.yaml: primary 11/14, secondary 10/14. Counts are ingredient instances in each selected document, not chemical accuracy. Every asserted CHEBI slot has an exact current OLS label match and a current MIM identifier row; MAPPED and REJECTED alias rows remain distinct. Zero numeric legacy MediaIngredientMech identifiers occur in the complete selected documents; the history placeholder NNNNNN is not an identifier. Chemical-form findings are assessed separately. Complex mixtures are not forced to pure-compound IDs.

### Growth claims and classification

scope: supported. Targets: CultureMech:009522.

The selected source identity is a bacterial cultivation formulation; physical state and undefined complex composition are coherent. No target-organism, strain-growth or performance claim is asserted. Generic application text is not evidence of demonstrated growth; no strain extrapolation or optimization is proposed.

### Native structural checks

schema: supported. Targets: CultureMech:009522.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Resazurin milligrams were represented as grams per litre

major / open / confirmed; issue key: batch054-05-resazurin-unit.

Both selected layers store resazurin as 1 G_PER_L, whereas both current sources specify 1 mg per batch. This is a mass-unit error; a precise final concentration additionally requires a justified final-volume basis.

### f2: Liquid additions and the SL-10 stock are misrepresented

major / open / confirmed; issue key: batch054-05-liquid-stock-units.

Water 700 ml, clarified rumen fluid 300 ml and SL-10 1 ml are stored as G_PER_L. The stock is empty and named Unknown solution. Ordinary gram values match source batch masses but their per-litre denominator is also unstated.

### f3: pH and source preparation are missing

major / open / confirmed; issue key: batch054-05-missing-process.

Both selected layers omit pH 7.0, ordered bicarbonate/cysteine addition, carbon-dioxide handling, sealing, sterilization and rumen-fluid preparation. The VARIABLE gas row alone cannot represent these instructions.

### f4: The local SL-10 dependency cannot be transferred unchanged

major / open / confirmed; issue key: batch054-05-dependency-scope.

The inspected M433 parent flattens its stock milligram and acid-volume values into G_PER_L and mixes water from multiple sections. Its cobalt and nickel hexahydrate descriptors use anhydrous primary CHEBI:35696 and CHEBI:34887. These are existing primary slots only. Transfer of the whole parent would also introduce unrelated medium and vitamin components.

### f5: Source claims and one simple ingredient linkage remain absent

minor / open / confirmed; issue key: batch054-05-claim-evidence-grounding.

The selected records have no attached evidence claims or structured source references. The source-defined L-cysteine hydrochloride monohydrate has no primary or secondary grounding, unlike the intentionally undefined yeast extract and rumen fluid. A source-specific grounding review can resolve that supplied form without mapping complex mixtures to pure compounds.

## Recommended Actions And Acceptance Checks

### action1

Represent the verified 1 mg batch addition with exact source evidence and an honest denominator. Do not merely divide by 1000 while leaving an unjustified final-volume claim.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Restore liquid-volume units and a resolved, scoped SL-10 stock reference/composition; preserve batch quantities separately from working dose and final-volume claims. Avoid density assumptions and automatic normalization of listed water.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the exact source preparation, preserving the distinction between the main-medium default and the explicit rumen-stock treatment; retain the unquantified gas role without inventing a dose.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Repair or model only the authenticated SL-10 subsection before linking it to BY. Preserve stock batch units and supplied hydrates, distinguish the working 1 ml dose, and exclude all other M433 sections.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Attach claim-scoped references and source excerpts, and review a canonical term for the explicit L-cysteine hydrochloride monohydrate form with current ontology/MIM evidence before adding a mapping.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/BY_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/by_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch054/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch054/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch054/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch054/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm1330 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| togoM3005 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| jcm433 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full current JCM 433 read; ONLY Trace element solution SL-10 table and its dissolution instruction are dependencies of BY. Main medium, vitamins and main preparation excluded. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon compound with formula CO&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt; in which the carbon is attached to each oxygen atom by a double bond. A colourless, odourless gas under normal conditions, it is produced during respiration by all animals, fungi and microorganisms that depend directly or indirectly on living or decaying plants for food.']; formula ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:17057 = cellobiose; definition ['A glycosylglucose consisting of two glucose units linked via a β(1→4) bond.']; formula ['C12H22O11']; mass ['342.297']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:17754 = glycerol; definition ['A triol with a structure of propane substituted at positions 1, 2 and 3 by hydroxy groups.']; formula ['C3H8O3']; mass ['92.094']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt salt in which the cobalt metal is in the +2 oxidation state and the counter-anion is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co']; mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch054/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T012400Z-BY_Medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/by_medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BY_Medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| writer43 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer44 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer45 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer46 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch054/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The sources list batch water and other additions without an explicit measured final volume. Per-litre normalization and final stock dilution remain unsupported until that basis is established.
- Only the SL-10 subsection transfers from JCM 433; no parent main-medium, vitamin or strain-growth assertion transfers. Current packaged MIM rows establish current index support, not historical validity.
- The exact source-defined cysteine hydrochloride monohydrate is ungrounded locally; no replacement identifier is asserted without a separate exact mapping check. No literature growth-performance search was performed.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T041305Z-by-medium-batch054
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of by_medium
started_at: '2026-10-28T04:00:14.824332Z'
finished_at: '2026-10-28T04:13:05.065648Z'
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
summary: BY identity is supported, but the target and owner lose milligram and liquid-volume
  units, the SL-10 stock boundary, pH and preparation. The current local M433 dependency
  itself has scoped unit and hydrate problems. All selected amounts and delegated
  stock amounts were assessed without inventing a final-volume denominator.
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
  - path: data/merge_yaml/merged/BY_Medium.yaml
    sha256: 5366acfe7123ae55ec1950f0797c577586baed642a7aa56443319d3370a1908f
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml
    sha256: 33a016afbc69069242603dff0c39d8ac64e71684294d8279416564e597648f8c
    role: context
  - path: data/normalized_yaml/bacterial/by_medium.yaml
    sha256: 81da4d6119d4902a4262951ce87b06a5e1d706f3f2799430a8ccd500768fab2e
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BY_Medium.md
    sha256: 08e2cdefa44f695ee9eee218ae0edbace3794b25cda577a29b7f5420b4633026
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/by_medium.md
    sha256: c3d9f2ad796a2a6528f3da0abe1dc2bec9cdbc6a3d2f9c8dc42d18e45f1ebb02
    role: context
  - path: reports/yaml_record_review/20260922T012400Z-BY_Medium.md
    sha256: e0fb9415bf2fae1a88ebcb051155fa3188f3877fc55ee711fb38efb5ed458e22
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  selection: Authoritative batch054 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009522
targets:
- target_id: CultureMech:009522
  path: data/merge_yaml/merged/BY_Medium.yaml
  label: by_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009522
  command: just validate-schema data/merge_yaml/merged/BY_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009522
  command: just validate-strict data/merge_yaml/merged/BY_Medium.yaml --workers 1
    --out REVIEW_WORK/batch054/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009522
  command: just validate-terms data/merge_yaml/merged/BY_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:009522
  command: just validate-references data/merge_yaml/merged/BY_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/BY_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T04:13:04.978370Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 5366acfe7123ae55ec1950f0797c577586baed642a7aa56443319d3370a1908f
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/by_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T04:13:04.978565Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 81da4d6119d4902a4262951ce87b06a5e1d706f3f2799430a8ccd500768fab2e
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch054/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:00:16.072146Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 6efad3a3782c282fd1c2b972680579a4c80d0efd262cfb6af4f40e45ef74e03f
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch054/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:00:17.254448Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: bd2cbd48294b9e6cba3c3ef72fa5ddd34489bfd3b244a746c56953e1f7f6250c
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch054/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:00:18.510469Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 88bc9009e49766b38dcfbc7dda304b07f85b96ea9f2235ae5a25f1c9ec026ba6
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch054/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T04:00:19.348669Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: b02ec300593c52505444d37123a24592e169e6a7e0c790ec4ce6ccce7c984ab9
- evidence_id: jcm1330
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:52.466733Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: 90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71
- evidence_id: togoM3005
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:52.466892Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: 747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca
- evidence_id: jcm433
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:53.080098Z'
  support: supports
  summary: Full current JCM 433 read; ONLY Trace element solution SL-10 table and
    its dissolution instruction are dependencies of BY. Main medium, vitamins and
    main preparation excluded.
  snapshot_sha256: bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:53.186252Z'
  support: supports
  summary: OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition
    ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula
    ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:53.186663Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:53.186809Z'
  support: supports
  summary: OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic
    acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy
    group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:53.186973Z'
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
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:53.282589Z'
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
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:54.055560Z'
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
- evidence_id: chebi17057
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:54.412241Z'
  support: supports
  summary: OLS current exact CHEBI:17057 = cellobiose; definition ['A glycosylglucose
    consisting of two glucose units linked via a β(1→4) bond.']; formula ['C12H22O11'];
    mass ['342.297']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:54.514004Z'
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
- evidence_id: chebi17754
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:54.716774Z'
  support: supports
  summary: OLS current exact CHEBI:17754 = glycerol; definition ['A triol with a structure
    of propane substituted at positions 1, 2 and 3 by hydroxy groups.']; formula ['C3H8O3'];
    mass ['92.094']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 0231975176416cbaad3ad04c9efeedbe9bef0b826645e592a4a2f511e8d1db95
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:54.951475Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.005769Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.376105Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.379115Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.387177Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.535483Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.812742Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:55.874809Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:56.150601Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:56.150779Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:56.253154Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:56.357700Z'
  support: supports
  summary: OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt
    salt in which the cobalt metal is in the +2 oxidation state and the counter-anion
    is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co'];
    mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:56.663683Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:56.972329Z'
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
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.124876Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.268327Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.281378Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.352285Z'
  support: supports
  summary: OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O'];
    mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.451919Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.584538Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T04:00:57.928903Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch054/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T04:13:04.993213Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 6114d249ab86ec7ed7c87669f4c2e756cbd7f9620208631783d6fd1f8400a0e4
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T012400Z-BY_Medium.md
  locator: entire report
  accessed_at: '2026-10-28T04:13:04.993263Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: e0fb9415bf2fae1a88ebcb051155fa3188f3877fc55ee711fb38efb5ed458e22
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/by_medium.md
  locator: entire report
  accessed_at: '2026-10-28T04:13:04.993296Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: c3d9f2ad796a2a6528f3da0abe1dc2bec9cdbc6a3d2f9c8dc42d18e45f1ebb02
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BY_Medium.md
  locator: entire report
  accessed_at: '2026-10-28T04:13:04.993322Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 08e2cdefa44f695ee9eee218ae0edbace3794b25cda577a29b7f5420b4633026
- evidence_id: writer43
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:13:04.993363Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer44
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:13:04.993386Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer45
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:13:04.993408Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer46
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T04:13:04.993437Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch054/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T04:13:05.065488Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: e7db13b4e27e1b443623911c2af9d82d7324be198e8b794a64973810cc8506ad
assessments:
- assessment_id: a1
  area: identity
  topic: BY and its exact stock dependency
  outcome: supported
  summary: The sole maintained owner and generated target represent TOGO M3005 / JCM1330.
    Current primary and provider agree on the listed ingredients and preparation.
    The JCM 433 relationship delegates SL-10 only; its main medium and vitamin solution
    are not BY ingredients.
  target_ids:
  - CultureMech:009522
  evidence_ids:
  - local0
  - local1
  - jcm1330
  - togoM3005
  - jcm433
- assessment_id: a2
  area: provenance
  topic: Historical reports and present writer behavior
  outcome: concern
  summary: Historical reports correctly raised missing preparation and unit loss,
    but their implied litre arithmetic is not independent final-volume evidence. Current
    TOGO code handles mg/ml separately and retains primary comments and stock references;
    the observed old output must be repaired without claiming that current code still
    performs the historical flattening. Current conservative merge guards should preserve
    the corrected scientific fields.
  target_ids:
  - CultureMech:009522
  evidence_ids:
  - history0
  - history1
  - history2
  - local1
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 30 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:009522
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009522",
    "selected_concentration_field_count": 30, "selected_concentration_fields_covered":
    30, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "700", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "700", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main recipe batch", "interpretation":
    "Both sources specify 700 ml as a liquid addition, not 700 g. Restore the volume
    unit without assuming density. The 700 ml water and 300 ml rumen-fluid inputs
    plus stock addition do not establish measured final volume.", "sources": [{"locator":
    "HTML tr[13]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Distilled
    water\n700.0\nml", "quote_representation": "HTML tr[13] DOM text"}, {"locator":
    "$.components[0].items[0]", "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 700,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgSO4·7H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[4]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n0.2\ng",
    "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[1]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgSO4·7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[2].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[8]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Yeast extract\n1.0\ng",
    "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[2]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[3].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[0]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "NaCl\n1.0\ng",
    "quote_representation": "HTML tr[0] DOM text"}, {"locator": "$.components[0].items[3]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
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
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "CaCl2·2H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[4].concentration",
    "original": {"value": "0.13", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.13", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[3]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "CaCl\n2\n·2H\n2\nO\n0.13\ng",
    "quote_representation": "HTML tr[3] DOM text"}, {"locator": "$.components[0].items[4]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"CaCl2·2H2O\",\n          \"volume\": 0.13,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[5].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[5]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "KH\n2\nPO\n4\n1.0\ng",
    "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[5]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q7", "subject": "K2HPO4", "local_fields": [{"record_path":
    "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[6].concentration",
    "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[1]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "K\n2\nHPO\n4\n0.5\ng",
    "quote_representation": "HTML tr[1] DOM text"}, {"locator": "$.components[0].items[6]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject":
    "Resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main recipe batch", "interpretation":
    "Both sources specify 1 mg resazurin, equivalent to 0.001 g per batch. The local
    1 G_PER_L conflates milligrams with grams and adds an unproven final-volume denominator.
    Correct the source mass and basis together; the source does not specify sodium
    resazurin, so the neutral CHEBI:8806 form is not itself contradicted here.", "sources":
    [{"locator": "HTML tr[12]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Resazurin\n1.0\nmg",
    "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[0].items[7]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "NaHCO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[8].concentration",
    "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported. Add this component after boiling
    and cooling under carbon dioxide, as specified by the primary preparation.", "sources":
    [{"locator": "HTML tr[9]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "NaHCO\n3\n5.0\ng",
    "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[8]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\":
    \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q10", "subject": "(NH4)2SO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[9].concentration",
    "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[2]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "(NH\n4\n)\n2\nSO\n4\n0.25\ng",
    "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.components[0].items[9]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\":
    \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "Cellobiose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path": "ingredients[10].concentration",
    "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "main recipe batch", "interpretation":
    "The primary and current TOGO agree on this mass per listed recipe batch. The
    stored numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported.", "sources": [{"locator": "HTML
    tr[7]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Cellobiose\n5.0\ng",
    "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[10]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"Cellobiose\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001137\",\n          \"gmo_id\": \"GMO_001137\",\n          \"label\":
    \"Cellobiose\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "Rumen fluid, clarified
    (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "300", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "300", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "main recipe batch", "interpretation":
    "Both sources specify 300 ml as a liquid addition, not 300 g. Restore the volume
    unit without assuming density. The 700 ml water and 300 ml rumen-fluid inputs
    plus stock addition do not establish measured final volume.", "sources": [{"locator":
    "HTML tr[6]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Rumen fluid,
    clarified (see below)\n300.0\nml", "quote_representation": "HTML tr[6] DOM text"},
    {"locator": "$.components[0].items[11]", "source_key": "togoM3005", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005", "source_raw_sha256":
    "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "source_text_sha256":
    "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca", "accessed_at":
    "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"Rumen fluid, clarified (see below)\",\n          \"volume\": 300,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001534\",\n          \"gmo_id\":
    \"GMO_001534\",\n          \"label\": \"Rumen fluid (clarified)\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "L-Cysteine·HCl·H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "main recipe batch", "interpretation": "The
    primary and current TOGO agree on this mass per listed recipe batch. The stored
    numerical value matches that batch mass, but neither source states a measured
    final volume or a per-litre basis. Preserve the source batch amount and supplied
    form; the G_PER_L denominator remains unsupported. Add this component after boiling
    and cooling under carbon dioxide, as specified by the primary preparation.", "sources":
    [{"locator": "HTML tr[10]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "L-Cysteine·HCl·H\n2\nO\n0.5\ng",
    "quote_representation": "HTML tr[10] DOM text"}, {"locator": "$.components[0].items[12]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"L-Cysteine·HCl·H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001205\",\n          \"gmo_id\": \"GMO_001205\",\n          \"label\":
    \"L-Cysteine hydrochloride monohydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q14", "subject": "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "not_quantified", "stage": "preparation atmosphere",
    "interpretation": "The source gas has no numeric dose. Retain that honest lack
    of quantification and represent the gas stream in preparation; do not replace
    VARIABLE with a guessed concentration.", "sources": [{"locator": "$.components[0].items[14]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"CO2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[1]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except NaHCO3 and L-Cysteine·HCl·H2O.
    Bring to a boil and cool under CO2 gas stream, then add NaHCO3 and L-Cysteine·HCl·H2O
    to the medium. Dispense the medium into suitable culture vessels under a stream
    of CO2, seal with butyl rubber stoppers, and autoclave.\"\n    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "SL-10 working addition",
    "local_fields": [{"record_path": "data/merge_yaml/merged/BY_Medium.yaml", "field_path":
    "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/by_medium.yaml", "field_path":
    "solutions[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}],
    "decision": "correct", "stage": "working stock addition", "interpretation": "JCM1330
    and TOGO specify 1 ml of the SL-10 stock. The local empty Unknown solution and
    1 G_PER_L do not encode this volume or stock composition. Resolve only the explicitly
    delegated SL-10 subsection of JCM 433; no other parent-medium recipe transfers.",
    "sources": [{"locator": "HTML tr[11]", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Trace element
    solution SL-10 (see Medium No.\n433\n)\n1.0\nml", "quote_representation": "HTML
    tr[11] DOM text"}, {"locator": "$.components[0].items[13]", "source_key": "togoM3005",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n          \"component_name\":
    \"Trace element solution SL--10 (see Medium [M433])\",\n          \"volume\":
    1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M433\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q16", "subject": "SL-10 stock: HCl (25%, 7.7 M)", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 10.0 ml for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum. The HCl descriptor explicitly gives 7.7 M and bare 25%; the percentage
    basis is unspecified, so do not relabel it w/v or v/v.", "sources": [{"locator":
    "HTML tr[9]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b",
    "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33",
    "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "HCl (25%,
    7.7 M)\n10.0\nml", "quote_representation": "HTML tr[9] DOM text"}]}, {"decision_id":
    "q17", "subject": "SL-10 stock: FeCl2·4H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 1.5 g for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum.", "sources": [{"locator": "HTML tr[10]", "source_key": "jcm433",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "FeCl\n2\n·4H\n2\nO\n1.5\ng",
    "quote_representation": "HTML tr[10] DOM text"}]}, {"decision_id": "q18", "subject":
    "SL-10 stock: ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "70", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 70.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm433",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "ZnCl\n2\n70.0\nmg", "quote_representation":
    "HTML tr[11] DOM text"}]}, {"decision_id": "q19", "subject": "SL-10 stock: MnCl2·4H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 100.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum.", "sources": [{"locator": "HTML tr[12]", "source_key": "jcm433",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n100.0\nmg",
    "quote_representation": "HTML tr[12] DOM text"}]}, {"decision_id": "q20", "subject":
    "SL-10 stock: H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 6.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm433",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "H\n3\nBO\n3\n6.0\nmg", "quote_representation":
    "HTML tr[13] DOM text"}]}, {"decision_id": "q21", "subject": "SL-10 stock: CoCl2·6H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "190", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 190.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum. The source explicitly supplies the hexahydrate, while the scoped
    local dependency primary CHEBI term denotes the anhydrous chloride. Resolve the
    supplied form; no secondary MIM slot exists for this particular dependency ingredient.",
    "sources": [{"locator": "HTML tr[14]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b",
    "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33",
    "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "CoCl\n2\n·6H\n2\nO\n190.0\nmg",
    "quote_representation": "HTML tr[14] DOM text"}]}, {"decision_id": "q22", "subject":
    "SL-10 stock: CuCl2·2H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 2.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum.", "sources": [{"locator": "HTML tr[15]", "source_key": "jcm433",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "CuCl\n2\n·2H\n2\nO\n2.0\nmg",
    "quote_representation": "HTML tr[15] DOM text"}]}, {"decision_id": "q23", "subject":
    "SL-10 stock: NiCl2·6H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "24", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 24.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum. The source explicitly supplies the hexahydrate, while the scoped
    local dependency primary CHEBI term denotes the anhydrous chloride. Resolve the
    supplied form; no secondary MIM slot exists for this particular dependency ingredient.",
    "sources": [{"locator": "HTML tr[16]", "source_key": "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b",
    "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33",
    "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "NiCl\n2\n·6H\n2\nO\n24.0\nmg",
    "quote_representation": "HTML tr[16] DOM text"}]}, {"decision_id": "q24", "subject":
    "SL-10 stock: Na2MoO4·2H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "36", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "scoped dependency stock batch",
    "interpretation": "The scoped SL-10 table specifies 36.0 mg for this stock batch.
    This is stock composition, not the receiving BY dose or final-medium concentration.
    The separately specified BY addition is 1 ml. The source lists water and acid
    inputs without an explicit measured stock final volume; do not infer final dilution
    from their sum.", "sources": [{"locator": "HTML tr[17]", "source_key": "jcm433",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n36.0\nmg",
    "quote_representation": "HTML tr[17] DOM text"}]}, {"decision_id": "q25", "subject":
    "SL-10 stock: Distilled water", "local_fields": [], "decision": "add", "stage":
    "scoped dependency stock batch", "interpretation": "The scoped SL-10 table specifies
    990.0 ml for this stock batch. This is stock composition, not the receiving BY
    dose or final-medium concentration. The separately specified BY addition is 1
    ml. The source lists water and acid inputs without an explicit measured stock
    final volume; do not infer final dilution from their sum. The local parent water
    row combines several parent sections, so it cannot stand in for this 990 ml stock-water
    input.", "sources": [{"locator": "HTML tr[18]", "source_key": "jcm433", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_raw_sha256":
    "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "source_text_sha256":
    "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33", "accessed_at":
    "2026-10-28T04:00:53.080098Z", "exact_source_quote": "Distilled water\n990.0\nml",
    "quote_representation": "HTML tr[18] DOM text"}]}, {"decision_id": "q26", "subject":
    "pH", "local_fields": [], "decision": "add", "stage": "main preparation", "interpretation":
    "The primary explicitly sets pH 7.0; both selected documents omit it. This is
    a preparation target, not a growth result.", "sources": [{"locator": "$.comments[0]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Adjust pH to 7.0\"\n    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q27", "subject": "Main preparation", "local_fields":
    [], "decision": "add", "stage": "main preparation", "interpretation": "Restore
    the explicit ordering: mix except bicarbonate and cysteine hydrochloride monohydrate,
    boil and cool under carbon dioxide, add those components, dispense under carbon
    dioxide, seal with butyl rubber stoppers and autoclave. No numeric gas dose or
    incubation condition is supplied.", "sources": [{"locator": "$.comments[1]", "source_key":
    "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except NaHCO3 and L-Cysteine·HCl·H2O.
    Bring to a boil and cool under CO2 gas stream, then add NaHCO3 and L-Cysteine·HCl·H2O
    to the medium. Dispense the medium into suitable culture vessels under a stream
    of CO2, seal with butyl rubber stoppers, and autoclave.\"\n    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Clarified rumen-fluid
    preparation", "local_fields": [], "decision": "add", "stage": "rumen stock preparation",
    "interpretation": "Rumen-fluid stock preparation is explicitly 120 C for 15 minutes
    followed by 25,000 × g for 15 minutes. Do not substitute the generic page autoclave
    default for this stock-specific treatment.", "sources": [{"locator": "$.comments[2]",
    "source_key": "togoM3005", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3005",
    "source_raw_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "source_text_sha256": "747f25acbb097d1f0bbc6fff8ae2eec622b1e0342928753cbe0d509b3e1ee1ca",
    "accessed_at": "2026-10-28T04:00:52.466892Z", "exact_source_quote": "{\n      \"paragraph_index\":
    4,\n      \"comment\": \"To prepare the clarified rumen fluid, preheat rumen content
    at 120C for 15 min. Use the supernatant after centrifuging at 25,000 x g for 15
    min.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q29", "subject": "Primary page sterilization default", "local_fields": [], "decision":
    "add", "stage": "main-medium sterilization", "interpretation": "The JCM1330 page
    default is 121 C for 15 minutes unless otherwise stated. Its main preparation
    says autoclave without a different numeric cycle; the explicit rumen-fluid treatment
    remains 120 C for 15 minutes.", "sources": [{"locator": "extracted-text lines
    4-4", "source_key": "jcm1330", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1330",
    "source_raw_sha256": "90bfdb8afca472ccdfd33767a1e9f1b3bb16ad9dafd256fe8b1b59dd53d7db71",
    "source_text_sha256": "424e97fb45f45bb23c9d8c0d95c96bd1c7850565227e450eaf220dcac6fc4c1b",
    "accessed_at": "2026-10-28T04:00:52.466733Z", "exact_source_quote": "Unless otherwise
    stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q30", "subject": "SL-10 dissolution
    order", "local_fields": [], "decision": "add", "stage": "scoped stock preparation",
    "interpretation": "Dissolve ferrous chloride tetrahydrate in hydrochloric acid
    first, then dilute with distilled water and add the remaining salts. This instruction
    belongs to SL-10 only. Exclude JCM 433 main solutions, vitamins and their sterilization
    instructions.", "sources": [{"locator": "extracted-text lines 105-109", "source_key":
    "jcm433", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_raw_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b",
    "source_text_sha256": "2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33",
    "accessed_at": "2026-10-28T04:00:53.080098Z", "exact_source_quote": "Dissolve
    FeCl\n2\n·4H\n2\nO first in HCl. Then dilute in distilled water and add the remaining
    salts.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch054/record05/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/BY_Medium.yaml: primary 11/14, secondary 10/14;
    data/normalized_yaml/bacterial/by_medium.yaml: primary 11/14, secondary 10/14.
    Counts are ingredient instances in each selected document, not chemical accuracy.
    Every asserted CHEBI slot has an exact current OLS label match and a current MIM
    identifier row; MAPPED and REJECTED alias rows remain distinct. Zero numeric legacy
    MediaIngredientMech identifiers occur in the complete selected documents; the
    history placeholder NNNNNN is not an identifier. Chemical-form findings are assessed
    separately. Complex mixtures are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:009522
  evidence_ids:
  - grounding
- assessment_id: a5
  area: scope
  topic: Growth claims and classification
  outcome: supported
  summary: The selected source identity is a bacterial cultivation formulation; physical
    state and undefined complex composition are coherent. No target-organism, strain-growth
    or performance claim is asserted. Generic application text is not evidence of
    demonstrated growth; no strain extrapolation or optimization is proposed.
  target_ids:
  - CultureMech:009522
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
  - CultureMech:009522
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: batch054-05-resazurin-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Resazurin milligrams were represented as grams per litre
  description: Both selected layers store resazurin as 1 G_PER_L, whereas both current
    sources specify 1 mg per batch. This is a mass-unit error; a precise final concentration
    additionally requires a justified final-volume basis.
  target_ids:
  - CultureMech:009522
  field_paths:
  - ingredients[7].concentration
  evidence_ids:
  - jcm1330
  - togoM3005
  rule_id: source-specific-formulation-fidelity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
    role: maintained normalized contributor
  native_severity: P2
  normalization_reason: P2 is normalized to major because the source milligram amount
    is represented with a gram unit, independently of the unresolved final-volume
    basis.
- finding_id: f2
  issue_key: batch054-05-liquid-stock-units
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Liquid additions and the SL-10 stock are misrepresented
  description: Water 700 ml, clarified rumen fluid 300 ml and SL-10 1 ml are stored
    as G_PER_L. The stock is empty and named Unknown solution. Ordinary gram values
    match source batch masses but their per-litre denominator is also unstated.
  target_ids:
  - CultureMech:009522
  field_paths:
  - ingredients[0].concentration
  - ingredients[11].concentration
  - solutions[0]
  - ingredients[*].concentration
  evidence_ids:
  - jcm1330
  - togoM3005
  - jcm433
  rule_id: source-specific-formulation-fidelity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
    role: maintained normalized contributor
  native_severity: P2
  normalization_reason: P2 is normalized to major because liquid additions and a required
    stock are represented as mass concentrations with an empty stock composition.
- finding_id: f3
  issue_key: batch054-05-missing-process
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: pH and source preparation are missing
  description: Both selected layers omit pH 7.0, ordered bicarbonate/cysteine addition,
    carbon-dioxide handling, sealing, sterilization and rumen-fluid preparation. The
    VARIABLE gas row alone cannot represent these instructions.
  target_ids:
  - CultureMech:009522
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[13]
  evidence_ids:
  - jcm1330
  - togoM3005
  rule_id: source-specific-formulation-fidelity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
    role: maintained normalized contributor
  native_severity: P3
  normalization_reason: P3 preparation and pH omissions are normalized to major here
    because the complete source-specific anoxic preparation sequence is missing, rather
    than only an optional descriptive step.
- finding_id: f4
  issue_key: batch054-05-dependency-scope
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: The local SL-10 dependency cannot be transferred unchanged
  description: The inspected M433 parent flattens its stock milligram and acid-volume
    values into G_PER_L and mixes water from multiple sections. Its cobalt and nickel
    hexahydrate descriptors use anhydrous primary CHEBI:35696 and CHEBI:34887. These
    are existing primary slots only. Transfer of the whole parent would also introduce
    unrelated medium and vitamin components.
  target_ids:
  - CultureMech:009522
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[6:15].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[9].term
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[10].term
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::solutions[2].composition
  evidence_ids:
  - jcm433
  - grounding
  - chebi35696
  - chebi34887
  rule_id: source-specific-formulation-fidelity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml
    role: scoped SL-10 dependency only; not a maintained owner of the complete BY
      recipe
  native_severity: P2
  normalization_reason: P2 is normalized to major because existing dependency quantities
    and asserted salt forms conflict with the scoped SL-10 source and cannot support
    unchanged reuse.
- finding_id: f5
  issue_key: batch054-05-claim-evidence-grounding
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source claims and one simple ingredient linkage remain absent
  description: The selected records have no attached evidence claims or structured
    source references. The source-defined L-cysteine hydrochloride monohydrate has
    no primary or secondary grounding, unlike the intentionally undefined yeast extract
    and rumen fluid. A source-specific grounding review can resolve that supplied
    form without mapping complex mixtures to pure compounds.
  target_ids:
  - CultureMech:009522
  field_paths:
  - references
  - ingredients[*].evidence
  - ingredients[12]
  evidence_ids:
  - grounding
  - jcm1330
  - validate-references
  rule_id: source-specific-formulation-fidelity
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
    role: maintained normalized contributor
  native_severity: P3
  normalization_reason: P3 is normalized to minor because missing attached source
    evidence and an ungrounded simple supplied ingredient limit completeness without
    contradicting an existing identifier.
actions:
- action_id: action1
  description: Represent the verified 1 mg batch addition with exact source evidence
    and an honest denominator. Do not merely divide by 1000 while leaving an unjustified
    final-volume claim.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009522
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
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
  description: Restore liquid-volume units and a resolved, scoped SL-10 stock reference/composition;
    preserve batch quantities separately from working dose and final-volume claims.
    Avoid density assumptions and automatic normalization of listed water.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009522
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
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
  description: Add the exact source preparation, preserving the distinction between
    the main-medium default and the explicit rumen-stock treatment; retain the unquantified
    gas role without inventing a dose.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009522
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
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
  description: Repair or model only the authenticated SL-10 subsection before linking
    it to BY. Preserve stock batch units and supplied hydrates, distinguish the working
    1 ml dose, and exclude all other M433 sections.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009522
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml
    role: scoped SL-10 dependency only; not a maintained owner of the complete BY
      recipe
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Attach claim-scoped references and source excerpts, and review a canonical
    term for the explicit L-cysteine hydrochloride monohydrate form with current ontology/MIM
    evidence before adding a mapping.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009522
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/by_medium.yaml
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
- The sources list batch water and other additions without an explicit measured final
  volume. Per-litre normalization and final stock dilution remain unsupported until
  that basis is established.
- Only the SL-10 subsection transfers from JCM 433; no parent main-medium, vitamin
  or strain-growth assertion transfers. Current packaged MIM rows establish current
  index support, not historical validity.
- The exact source-defined cysteine hydrochloride monohydrate is ungrounded locally;
  no replacement identifier is asserted without a separate exact mapping check. No
  literature growth-performance search was performed.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
