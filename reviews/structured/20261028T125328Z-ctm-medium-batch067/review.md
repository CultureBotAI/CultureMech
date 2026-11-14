# Scientific review of ctm_medium

- Review: 20261028T125328Z-ctm-medium-batch067
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:36:55.911963Z
- Finished UTC: 2026-10-28T12:53:28.395809Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

CTM identity is clear, but its basal medium, nested stocks and finishing addition were flattened. Repair source stages and units, restore the explicit preparation controls, resolve the linked Mixed-solution volume conflict, then regenerate while preserving the owner’s six later correct groundings.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch067 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007698 | data/merge_yaml/merged/CTM_MEDIUM.yaml | generated | ctm_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007698 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:007698 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:007698 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:007698 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact CTM source identity and stock graph

identity: supported. Targets: CultureMech:007698.

Selected TOGO M1173 is JCM1100. The source has a basal stage and a finishing Mixed solution, with separate named stocks. MediaDive5182 is the exact locally linked stock; the differently maintained CTM CultureMech:002279 report is comparison-only. No organism or experimental growth assertion is inferred.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:007698.

The selected owner and target have identical amounts; only six later owner primary groundings are missing from the generated target. Earlier zero-source-check reports remain incomplete leads. The exact5182 current raw matches six historical quoted objects and both attached claims, while its explicit provider-only limit and unresolved nested additions are preserved. The source instruction now makes the volume conflict actionable without pretending the old provider evidence was fabricated. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:007698.

All 128 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007698", "selected_concentration_field_count": 128, "selected_concentration_fields_covered": 128, "decisions": [{"decision_id": "q1", "subject": "Collapsed water from multiple stocks", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "625.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "625.0", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Distinct basal and stock solvent inputs", "interpretation": "625 G_PER_L aggregates mixed-unit water entries from different recipe stages and is not a real concentration. Restore the basal make-up to 1 L separately from each stock water input. The TOGO mixed-stock 19 ml is arithmetic-derived; the primary requires make-up to 30 ml and does not independently measure that solvent amount.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.components[7].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 19,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0 L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40 min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation. Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below) to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "HEPES", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "2.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "2.4", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "One-litre basal medium before Mixed solution addition", "interpretation": "The primary supports 2.4 g in a basal preparation explicitly made up to 1 L, hence 2.4 g/L at that stage. The stored direct rate lacks that stage; the final medium receives 30 ml Mixed solution afterward without an independently measured final volume. Do not adopt API g_l=85.7143 based on its incomplete 28 ml metadata.", "sources": [{"locator": "HTML tr[4]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "HEPES\n2.4\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"HEPES\",\n          \"volume\": 2.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001142\",\n          \"gmo_id\": \"GMO_001142\",\n          \"label\": \"HEPES\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"HEPES\",\n                        \"compound_id\": 371,\n                        \"amount\": 2.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 85.7143,\n                        \"mmol_l\": 359.676,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0 L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40 min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation. Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below) to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "KOH adjustment", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Basal pH adjustment", "interpretation": "The fixed dose is not stated, so VARIABLE does not contradict the source. Preserve an unquantified adjustment and separately record source 2 M reagent strength and pH 7.0; neither is represented by the placeholder itself.", "sources": [{"locator": "$.components[0].items[6]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"KOH\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0 L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40 min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation. Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below) to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "MgSO4・7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "3.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "3.75", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 (50 x stock) composition", "interpretation": "The source specifies 3.75 g in Solution 1 (50 x stock), not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=3.56803 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[5]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n3.75\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[2].items[2]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3.75,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.56803,\n                        \"mmol_l\": 14.4762,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "CaCl2・2H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1.8", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1.8", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 (50 x stock) composition", "interpretation": "The source specifies 1.8 g in Solution 1 (50 x stock), not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=1.71265 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[6]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "CaCl\n2\n·2H\n2\nO\n1.80\ng", "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[2].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 1.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.71265,\n                        \"mmol_l\": 11.6495,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Citric acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 (50 x stock) composition", "interpretation": "The source specifies 0.3 g in Solution 1 (50 x stock), not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=0.285442 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[7]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Citric acid\n0.30\ng", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[2].items[4]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Citric acid\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001112\",\n          \"gmo_id\": \"GMO_001112\",\n          \"label\": \"Citric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Citric acid\",\n                        \"compound_id\": 348,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.285442,\n                        \"mmol_l\": 1.48575,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Na2MoO4・2H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.39", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.39", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition", "interpretation": "The source specifies 0.39 g in Trace metal solution, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=0.39 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[14]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n0.39\ng", "quote_representation": "HTML tr[14] DOM text"}, {"locator": "$.components[3].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.39,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.39,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.39,\n                        \"mmol_l\": 1.6119,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.86", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.86", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition", "interpretation": "The source specifies 2.86 g in Trace metal solution, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=2.86 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[11]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "H\n3\nBO\n3\n2.86\ng", "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[3].items[2]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 2.86,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 2.86,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.86,\n                        \"mmol_l\": 46.2484,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "MnCl2・4H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "1.81", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "1.81", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition", "interpretation": "The source specifies 1.81 g in Trace metal solution, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=1.81 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[12]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n1.81\ng", "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[3].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 1.81,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 1.81,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.81,\n                        \"mmol_l\": 9.1458,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "ZnSO4・7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.222", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.222", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition", "interpretation": "The source specifies 0.222 g in Trace metal solution, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=0.222 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[13]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "ZnSO\n4\n·7H\n2\nO\n0.222\ng", "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[3].items[4]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.222,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.222,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.222,\n                        \"mmol_l\": 0.77201,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "CuSO4・5H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.079", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.079", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition", "interpretation": "The source specifies 0.079 g in Trace metal solution, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=0.079 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[15]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "CuSO\n4\n·5H\n2\nO\n0.079\ng", "quote_representation": "HTML tr[15] DOM text"}, {"locator": "$.components[3].items[5]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.079,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.079,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.079,\n                        \"mmol_l\": 0.316397,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Co(NO3)2・6H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.049", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.049", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition", "interpretation": "The source specifies 0.049 g in Trace metal solution, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=0.049 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[16]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Co(NO\n3\n)\n2\n·6H\n2\nO\n0.049\ng", "quote_representation": "HTML tr[16] DOM text"}, {"locator": "$.components[3].items[6]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Co(NO3)2・6H2O\",\n          \"volume\": 0.049,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001110\",\n          \"gmo_id\": \"GMO_001110\",\n          \"label\": \"Cobalt(II) nitrate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[5]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Co(NO3)2 x 6 H2O\",\n                        \"compound_id\": 541,\n                        \"amount\": 0.049,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.049,\n                        \"mmol_l\": 0.168365,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "15.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "15.3", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 2 composition", "interpretation": "The source specifies 15.3 g in Solution 2, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=15.3 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[18]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "K\n2\nHPO\n4\n15.3\ng", "quote_representation": "HTML tr[18] DOM text"}, {"locator": "$.components[4].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 15.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 15.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 15.3,\n                        \"mmol_l\": 87.8422,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "Ferric ammonium citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "12", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 3 composition", "interpretation": "The source specifies 12 g in Solution 3, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=12 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[20]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Ferric ammonium citrate\n12.0\ng", "quote_representation": "HTML tr[20] DOM text"}, {"locator": "$.components[5].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Ferric ammonium citrate\",\n          \"volume\": 12,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001147\",\n          \"gmo_id\": \"GMO_001147\",\n          \"label\": \"Ammonium ferric citrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[4].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Ferric ammonium citrate\",\n                        \"compound_id\": 97,\n                        \"amount\": 12,\n                        \"unit\": \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\": 45.805,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "2-Oxoglutarate", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "14.6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "14.6", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 4 composition", "interpretation": "The source specifies 14.6 g in Solution 4, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=14.6 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[22]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "2-Oxoglutarate\n14.6\ng", "quote_representation": "HTML tr[22] DOM text"}, {"locator": "$.components[6].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"2-Oxoglutarate\",\n          \"volume\": 14.6,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001861\",\n          \"gmo_id\": \"GMO_001861\",\n          \"label\": \"alpha-Ketoglutaric acid\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"2-Oxoglutarate\",\n                        \"compound_id\": 1992,\n                        \"amount\": 14.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 14.6,\n                        \"mmol_l\": 101.331,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "NaHCO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.625", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.625", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution composition", "interpretation": "The source specifies 0.625 g in Mixed solution, explicitly made up to 30 ml. Restore that stock stage; the entire 30 ml is added after preparing the basal litre. A final-medium g/L is not established by the stored direct value. The provider's separate 11 ml normalization conflicts with its own preparation instruction.", "sources": [{"locator": "HTML tr[24]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "NaHCO\n3\n0.625\ng", "quote_representation": "HTML tr[24] DOM text"}, {"locator": "$.components[7].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 0.625,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.625,\n                        \"unit\": \"g\",\n                        \"g_l\": 56.8182,\n                        \"mmol_l\": 676.351,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "Sodium thioglycolate", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.125", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.125", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution composition", "interpretation": "The source specifies 0.125 g in Mixed solution, explicitly made up to 30 ml. Restore that stock stage; the entire 30 ml is added after preparing the basal litre. A final-medium g/L is not established by the stored direct value. The provider's separate 11 ml normalization conflicts with its own preparation instruction.", "sources": [{"locator": "HTML tr[25]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Sodium thioglycolate\n0.125\ng", "quote_representation": "HTML tr[25] DOM text"}, {"locator": "$.components[7].items[2]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Sodium thioglycolate\",\n          \"volume\": 0.125,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001132\",\n          \"gmo_id\": \"GMO_001132\",\n          \"label\": \"Sodium thioglycolate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium thioglycolate\",\n                        \"compound_id\": 1644,\n                        \"amount\": 0.125,\n                        \"unit\": \"g\",\n                        \"g_l\": 11.3636,\n                        \"mmol_l\": 99.5937,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "Bacto peptone (BD--Difco)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 5 composition", "interpretation": "The source specifies 10 g in Solution 5, not as an undiluted direct main-medium rate. Restore that stock composition and its enclosing dose. Provider g_l=100 is source metadata, not an independently measured stock/final-medium volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator": "HTML tr[30]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Bacto peptone (BD-Difco)\n10.0\ng", "quote_representation": "HTML tr[30] DOM text"}, {"locator": "$.components[8].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Bacto peptone (BD--Difco)\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001089\",\n          \"gmo_id\": \"GMO_001089\",\n          \"label\": \"Bacto &amp;trade; Peptone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[7].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\": 19,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 100,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "L--Cysteine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[36]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Cysteine\n100.0\nmg", "quote_representation": "HTML tr[36] DOM text"}, {"locator": "$.components[9].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Cysteine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001318\",\n          \"gmo_id\": \"GMO_001318\",\n          \"label\": \"Cysteine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"L-Cysteine\",\n                        \"compound_id\": 671,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 2.06339,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "Glycine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[39]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Glycine\n100.0\nmg", "quote_representation": "HTML tr[39] DOM text"}, {"locator": "$.components[9].items[2]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Glycine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001559\",\n          \"gmo_id\": \"GMO_001559\",\n          \"label\": \"Glycine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[7]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Glycine\",\n                        \"compound_id\": 358,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 3.33023,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "L--Glutamic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[37]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Glutamic acid\n100.0\nmg", "quote_representation": "HTML tr[37] DOM text"}, {"locator": "$.components[9].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Glutamic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001570\",\n          \"gmo_id\": \"GMO_001570\",\n          \"label\": \"L-Glutamic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[5]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"L-Glutamic acid\",\n                        \"compound_id\": 374,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.69918,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "L--Alanine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[32]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Alanine\n100.0\nmg", "quote_representation": "HTML tr[32] DOM text"}, {"locator": "$.components[9].items[4]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Alanine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001766\",\n          \"gmo_id\": \"GMO_001766\",\n          \"label\": \"L-Alanine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"L-Alanine\",\n                        \"compound_id\": 274,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 2.80615,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "L--Arginine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[33]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Arginine\n100.0\nmg", "quote_representation": "HTML tr[33] DOM text"}, {"locator": "$.components[9].items[5]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Arginine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001767\",\n          \"gmo_id\": \"GMO_001767\",\n          \"label\": \"L-Arginine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"L-Arginine\",\n                        \"compound_id\": 1327,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.43513,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "L--Aspartic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[35]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Aspartic acid\n100.0\nmg", "quote_representation": "HTML tr[35] DOM text"}, {"locator": "$.components[9].items[6]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Aspartic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001770\",\n          \"gmo_id\": \"GMO_001770\",\n          \"label\": \"L-Aspartic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"L-Aspartic acid\",\n                        \"compound_id\": 1328,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.87829,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "L--Glutamine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[38]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Glutamine\n100.0\nmg", "quote_representation": "HTML tr[38] DOM text"}, {"locator": "$.components[9].items[7]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Glutamine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001776\",\n          \"gmo_id\": \"GMO_001776\",\n          \"label\": \"L-Glutamine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[6]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"L-Glutamine\",\n                        \"compound_id\": 134,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.71069,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "L--Isoleucine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[41]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Isoleucine\n100.0\nmg", "quote_representation": "HTML tr[41] DOM text"}, {"locator": "$.components[9].items[8]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Isoleucine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001783\",\n          \"gmo_id\": \"GMO_001783\",\n          \"label\": \"L-Isoleucine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[9]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"L-Isoleucine\",\n                        \"compound_id\": 447,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.90592,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "L--Leucine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[42]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Leucine\n100.0\nmg", "quote_representation": "HTML tr[42] DOM text"}, {"locator": "$.components[9].items[9]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Leucine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001785\",\n          \"gmo_id\": \"GMO_001785\",\n          \"label\": \"L-Leucine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[10]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"L-Leucine\",\n                        \"compound_id\": 446,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.90592,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "L--Lysine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[43]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Lysine\n100.0\nmg", "quote_representation": "HTML tr[43] DOM text"}, {"locator": "$.components[9].items[10]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Lysine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001788\",\n          \"gmo_id\": \"GMO_001788\",\n          \"label\": \"L-Lysine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[11]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"L-Lysine\",\n                        \"compound_id\": 1973,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.7101,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "L--Phenylalanine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[45]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Phenylalanine\n100.0\nmg", "quote_representation": "HTML tr[45] DOM text"}, {"locator": "$.components[9].items[11]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Phenylalanine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001794\",\n          \"gmo_id\": \"GMO_001794\",\n          \"label\": \"L-Phenylalanine \",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[13]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"L-Phenylalanine\",\n                        \"compound_id\": 1332,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.51341,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "L--Proline", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[46]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Proline\n100.0\nmg", "quote_representation": "HTML tr[46] DOM text"}, {"locator": "$.components[9].items[12]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Proline\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001797\",\n          \"gmo_id\": \"GMO_001797\",\n          \"label\": \"L-Proline\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[14]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"L-Proline\",\n                        \"compound_id\": 1130,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 2.17146,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "L--Serine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[47]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Serine\n100.0\nmg", "quote_representation": "HTML tr[47] DOM text"}, {"locator": "$.components[9].items[13]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Serine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001800\",\n          \"gmo_id\": \"GMO_001800\",\n          \"label\": \"L-Serine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[15]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"L-Serine\",\n                        \"compound_id\": 133,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 2.37891,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "L--Threonine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[48]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Threonine\n100.0\nmg", "quote_representation": "HTML tr[48] DOM text"}, {"locator": "$.components[9].items[14]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Threonine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001803\",\n          \"gmo_id\": \"GMO_001803\",\n          \"label\": \"L-Threonine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[16]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 17,\n                        \"compound\": \"L-Threonine\",\n                        \"compound_id\": 658,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 2.09872,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "L--Tryptophan", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[49]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Tryptophan\n100.0\nmg", "quote_representation": "HTML tr[49] DOM text"}, {"locator": "$.components[9].items[15]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Tryptophan\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001805\",\n          \"gmo_id\": \"GMO_001805\",\n          \"label\": \"L-Tryptophan\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[17]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 18,\n                        \"compound\": \"L-Tryptophan\",\n                        \"compound_id\": 449,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.22417,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "L--Tyrosine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[50]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Tyrosine\n100.0\nmg", "quote_representation": "HTML tr[50] DOM text"}, {"locator": "$.components[9].items[16]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Tyrosine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001808\",\n          \"gmo_id\": \"GMO_001808\",\n          \"label\": \"L-Tyrosine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[18]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 19,\n                        \"compound\": \"L-Tyrosine\",\n                        \"compound_id\": 1333,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.37977,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "L--Valine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[51]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Valine\n100.0\nmg", "quote_representation": "HTML tr[51] DOM text"}, {"locator": "$.components[9].items[17]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Valine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001811\",\n          \"gmo_id\": \"GMO_001811\",\n          \"label\": \"L-Valine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[19]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 20,\n                        \"compound\": \"L-Valine\",\n                        \"compound_id\": 1334,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 2.13402,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "L--Asparagine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[34]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Asparagine\n100.0\nmg", "quote_representation": "HTML tr[34] DOM text"}, {"locator": "$.components[9].items[18]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Asparagine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001870\",\n          \"gmo_id\": \"GMO_001870\",\n          \"label\": \"L-Asparagine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"L-Asparagine\",\n                        \"compound_id\": 829,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.89222,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "L--Histidine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[36].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[36].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[40]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Histidine\n100.0\nmg", "quote_representation": "HTML tr[40] DOM text"}, {"locator": "$.components[9].items[19]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Histidine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001872\",\n          \"gmo_id\": \"GMO_001872\",\n          \"label\": \"L-Histidine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[8]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"L-Histidine\",\n                        \"compound_id\": 132,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.61134,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "L--Methionine", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[37].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[37].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation": "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[44]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Methionine\n100.0\nmg", "quote_representation": "HTML tr[44] DOM text"}, {"locator": "$.components[9].items[20]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Methionine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001791\",\n          \"gmo_id\": \"GMO_001791\",\n          \"label\": \"L-Methionine \",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[12]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"L-Methionine\",\n                        \"compound_id\": 1330,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.67549,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "10 mM Potassium phosphate buffer (pH 7.2)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[38].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[38].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "This is a 100 ml addition of 10 mM potassium phosphate buffer at pH 7.2 to Vitamin solution A, not 100 g/L of a main-medium ingredient. Preserve dose, reagent strength and buffer pH independently; the buffer salt ratio is not supplied.", "sources": [{"locator": "HTML tr[66]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "10 mM Potassium phosphate buffer (pH 7.2)\n100.0\nml", "quote_representation": "HTML tr[66] DOM text"}, {"locator": "$.components[10].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"10 mM Potassium phosphate buffer (pH 7.2)\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001308\",\n          \"gmo_id\": \"GMO_001308\",\n          \"label\": \"Potassium phosphate buffer\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[13]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Potassium phosphate buffer\",\n                        \"compound_id\": 275,\n                        \"attribute\": \"pH 7.2, 10 mM\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"mmol_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[39].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[39].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 10 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[53]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Biotin\n10.0\nmg", "quote_representation": "HTML tr[53] DOM text"}, {"locator": "$.components[10].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.409316,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[40].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[40].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[62]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "p\n-Aminobenzoic acid\n100.0\nmg", "quote_representation": "HTML tr[62] DOM text"}, {"locator": "$.components[10].items[2]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[9]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 7.29182,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "Thiamine・HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[41].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[41].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[55]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Thiamine·HCl\n100.0\nmg", "quote_representation": "HTML tr[55] DOM text"}, {"locator": "$.components[10].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.96472,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[42].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[42].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[58]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Calcium pantothenate\n100.0\nmg", "quote_representation": "HTML tr[58] DOM text"}, {"locator": "$.components[10].items[4]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[5]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.09849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "Pyridoxine・HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[43].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[43].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[63]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Pyridoxine·HCl\n100.0\nmg", "quote_representation": "HTML tr[63] DOM text"}, {"locator": "$.components[10].items[5]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[10]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.86287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[44].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[44].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[59]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Folic acid\n100.0\nmg", "quote_representation": "HTML tr[59] DOM text"}, {"locator": "$.components[10].items[6]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[6]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.26552,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q46", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[45].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[45].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 10 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=0.1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[54]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Riboflavin\n10.0\nmg", "quote_representation": "HTML tr[54] DOM text"}, {"locator": "$.components[10].items[7]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.265675,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[46].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[46].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[61]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Nicotinic acid\n100.0\nmg", "quote_representation": "HTML tr[61] DOM text"}, {"locator": "$.components[10].items[8]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[8]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 8.12282,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q48", "subject": "Nicotinamide", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[47].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[47].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[60]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Nicotinamide\n100.0\nmg", "quote_representation": "HTML tr[60] DOM text"}, {"locator": "$.components[10].items[9]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Nicotinamide\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001162\",\n          \"gmo_id\": \"GMO_001162\",\n          \"label\": \"Nicotinamide\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[7]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Nicotinamide\",\n                        \"compound_id\": 337,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 8.18867,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject": "Thiamine pyrophosphate", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[48].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[48].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[56]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Thiamine pyrophosphate\n100.0\nmg", "quote_representation": "HTML tr[56] DOM text"}, {"locator": "$.components[10].items[10]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Thiamine pyrophosphate\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001660\",\n          \"gmo_id\": \"GMO_001660\",\n          \"label\": \"Thiamine pyrophosphate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine pyrophosphate\",\n                        \"compound_id\": 778,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 2.17029,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject": "β-NAD", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[49].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[49].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[65]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "β-NAD\n100.0\nmg", "quote_representation": "HTML tr[65] DOM text"}, {"locator": "$.components[10].items[11]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"β-NAD\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001691\",\n          \"gmo_id\": \"GMO_001691\",\n          \"label\": \"Beta-NAD\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[12]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"beta-NAD\",\n                        \"compound_id\": 1798,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 1.50504,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q51", "subject": "Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[50].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[50].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[64]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Lipoic acid\n100.0\nmg", "quote_representation": "HTML tr[64] DOM text"}, {"locator": "$.components[10].items[12]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[11]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.8466,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q52", "subject": "L--Ascorbic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[51].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[51].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[57]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Ascorbic acid\n100.0\nmg", "quote_representation": "HTML tr[57] DOM text"}, {"locator": "$.components[10].items[13]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"L--Ascorbic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001813\",\n          \"gmo_id\": \"GMO_001813\",\n          \"label\": \"L-Ascorbic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"L-Ascorbic acid\",\n                        \"compound_id\": 701,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.67795,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q53", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[52].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "ingredients[52].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution B (1000 x stock) composition", "interpretation": "The source specifies 100 mg in Vitamin solution B (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium ingredients and loses the source mg basis. Restore the exact stock input and nested dose chain. Provider g_l=1 is a separately declared stock normalization, not a final-medium rate.", "sources": [{"locator": "HTML tr[67]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Vitamin B\n12\n100.0\nmg", "quote_representation": "HTML tr[67] DOM text"}, {"locator": "$.components[11].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[10].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 0.73779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject": "Solution 1 (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation": "The exact source dose is 20 ml = 0.02 L to basal medium, not 20 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[2]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Solution 1 (see below)\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution 1 (see below)\n20.0\nml", "quote_representation": "HTML tr[0] DOM text"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution 1 (50 x stock)\",\n                        \"solution_id\": 5177,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q55", "subject": "Solution 2 (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation": "The exact source dose is 3 ml = 0.003 L to basal medium, not 3 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Solution 2 (see below)\",\n          \"volume\": 3,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[1]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution 2 (see below)\n3.0\nml", "quote_representation": "HTML tr[1] DOM text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution 2\",\n                        \"solution_id\": 5179,\n                        \"amount\": 3,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q56", "subject": "Solution 3 (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation": "The exact source dose is 2 ml = 0.002 L to basal medium, not 2 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[4]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Solution 3 (see below)\",\n          \"volume\": 2,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution 3 (see below)\n2.0\nml", "quote_representation": "HTML tr[2] DOM text"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution 3\",\n                        \"solution_id\": 5180,\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q57", "subject": "Solution 4 (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[3].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[3].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation": "The exact source dose is 2.5 ml = 0.0025 L to basal medium, not 2.5 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[5]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Solution 4 (see below)\",\n          \"volume\": 2.5,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution 4 (see below)\n2.5\nml", "quote_representation": "HTML tr[3] DOM text"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution 4\",\n                        \"solution_id\": 5181,\n                        \"amount\": 2.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q58", "subject": "Mixed solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[4].concentration", "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[4].concentration", "original": {"value": "30", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "After basal autoclaving liquid addition", "interpretation": "The exact source dose is 30 ml = 0.03 L to after basal autoclaving, not 30 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[1].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Mixed solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0 L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40 min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation. Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below) to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q59", "subject": "0.25 M EDTA・2Na solution (pH 8.0)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[5].concentration", "original": {"value": "0.6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[5].concentration", "original": {"value": "0.6", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 liquid addition", "interpretation": "The exact source dose is 0.6 ml = 0.0006 L to solution 1, not 0.6 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. The source also explicitly specifies 0.25 M disodium EDTA at pH 8.0; preserve that strength separately from this dose.", "sources": [{"locator": "$.components[2].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"0.25 M EDTA・2Na solution (pH 8.0)\",\n          \"volume\": 0.6,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.25,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001962\",\n          \"gmo_id\": \"GMO_001962\",\n          \"label\": \"Disodium EDTA solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[8]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "0.25 M EDTA·2Na solution (pH 8.0)\n0.60\nml", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"attribute\": \"pH 8.0, 0.25 M\",\n                        \"amount\": 0.6,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q60", "subject": "Trace metal solution (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[6].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[6].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 liquid addition", "interpretation": "The exact source dose is 50 ml = 0.05 L to solution 1, not 50 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[2].items[5]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Trace metal solution (see below)\",\n          \"volume\": 50,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[9]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Trace metal solution (see below)\n50.0\nml", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Trace metal solution\",\n                        \"solution_id\": 5178,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q61", "subject": "Solution 5 (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[7].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[7].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution liquid addition", "interpretation": "The exact source dose is 0.5 ml = 0.0005 L to mixed solution, not 0.5 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[7].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Solution 5 (see below)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[26]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution 5 (see below)\n0.5\nml", "quote_representation": "HTML tr[26] DOM text"}, {"locator": "$.data.solutions[6].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution 5\",\n                        \"solution_id\": 5183,\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q62", "subject": "Solution 6 (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[8].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[8].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution liquid addition", "interpretation": "The exact source dose is 10 ml = 0.01 L to mixed solution, not 10 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[7].items[4]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Solution 6 (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[27]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution 6 (see below)\n10.0\nml", "quote_representation": "HTML tr[27] DOM text"}, {"locator": "$.data.solutions[6].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution 6\",\n                        \"solution_id\": 5184,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q63", "subject": "Vitamin solution A (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[9].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[9].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution liquid addition", "interpretation": "The exact source dose is 0.25 ml = 0.00025 L to mixed solution, not 0.25 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[7].items[5]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin solution A (see below)\",\n          \"volume\": 0.25,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[28]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Vitamin solution A (see below)\n0.25\nml", "quote_representation": "HTML tr[28] DOM text"}, {"locator": "$.data.solutions[6].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Vitamin solution A (1000 x stock)\",\n                        \"solution_id\": 5185,\n                        \"amount\": 0.25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q64", "subject": "Vitamin solution B (see below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[10].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path": "solutions[10].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution liquid addition", "interpretation": "The exact source dose is 0.25 ml = 0.00025 L to mixed solution, not 0.25 g/L. Restore the enclosing stock hierarchy; nested doses are not all additions directly to the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[7].items[6]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Vitamin solution B (see below)\",\n          \"volume\": 0.25,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[29]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Vitamin solution B (see below)\n0.25\nml", "quote_representation": "HTML tr[29] DOM text"}, {"locator": "$.data.solutions[6].recipe[5]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Vitamin solution B (1000 x stock)\",\n                        \"solution_id\": 5186,\n                        \"amount\": 0.25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q65", "subject": "Solution 1 (50 x stock) separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[2].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[10]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[10] DOM text"}]}, {"decision_id": "q66", "subject": "Trace metal solution separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[3].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[17]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[17] DOM text"}]}, {"decision_id": "q67", "subject": "Solution 2 separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[4].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[19]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[19] DOM text"}]}, {"decision_id": "q68", "subject": "Solution 3 separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[5].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[21]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[21] DOM text"}]}, {"decision_id": "q69", "subject": "Solution 4 separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[6].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[23]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[23] DOM text"}]}, {"decision_id": "q70", "subject": "Solution 5 separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 100 ml water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[8].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[31]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n100.0\nml", "quote_representation": "HTML tr[31] DOM text"}]}, {"decision_id": "q71", "subject": "Solution 6 separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 400 ml water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[9].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 400,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[52]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n400.0\nml", "quote_representation": "HTML tr[52] DOM text"}]}, {"decision_id": "q72", "subject": "Vitamin solution B (1000 x stock) separate water input", "local_fields": [], "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve 100 ml water at this stock stage. This is an input, not an independently measured final stock volume, and must not be summed with other stock waters.", "sources": [{"locator": "$.components[11].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[68]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n100.0\nml", "quote_representation": "HTML tr[68] DOM text"}]}, {"decision_id": "q73", "subject": "Basal preparation controls", "local_fields": [], "decision": "add", "stage": "Basal medium before finishing addition", "interpretation": "Restore make-up to 1 L, pH 7.0 using 2 M KOH, autoclaving at 121°C for 40 min, immediate sealing to avoid oxygenation, cooling to around 70°C, and addition of 30 ml filter-sterilized Mixed solution. The source-specific 40 min supersedes the page-wide generic 15 min default. This preparation is not organism-growth evidence.", "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0 L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40 min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation. Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below) to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q74", "subject": "Mixed solution final volume", "local_fields": [], "decision": "add", "stage": "Mixed stock before addition", "interpretation": "The stock is explicitly made up to 30 ml. This supports 0.625 g / 0.030 L = 20.833333… g/L sodium bicarbonate and 0.125 g / 0.030 L = 4.166666… g/L sodium thioglycolate at this stock stage only. Retain uncertainty about other stock final volumes and the eventual finished-medium volume.", "sources": [{"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 143-143", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Add distilled water to bring final volume to 30 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q75", "subject": "EDTA reagent and stock pH", "local_fields": [], "decision": "add", "stage": "Solution 1 addition reagent", "interpretation": "Retain 0.25 M disodium EDTA reagent strength and pH 8.0; these are not the basal pH or final-medium EDTA concentration. Salt hydration and preparation are not further specified.", "sources": [{"locator": "HTML tr[8]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "0.25 M EDTA·2Na solution (pH 8.0)\n0.60\nml", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[2].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"0.25 M EDTA・2Na solution (pH 8.0)\",\n          \"volume\": 0.6,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.25,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001962\",\n          \"gmo_id\": \"GMO_001962\",\n          \"label\": \"Disodium EDTA solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q76", "subject": "Vitamin A phosphate buffer control", "local_fields": [], "decision": "add", "stage": "Vitamin A solvent reagent", "interpretation": "Retain the 10 mM phosphate buffer strength and pH 7.2 with its 100 ml addition. Do not infer its constituent salt ratio or treat pH 7.2 as the medium pH.", "sources": [{"locator": "HTML tr[66]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "10 mM Potassium phosphate buffer (pH 7.2)\n100.0\nml", "quote_representation": "HTML tr[66] DOM text"}, {"locator": "$.components[10].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\": \"10 mM Potassium phosphate buffer (pH 7.2)\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001308\",\n          \"gmo_id\": \"GMO_001308\",\n          \"label\": \"Potassium phosphate buffer\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q77", "subject": "Existing linked stock rate: NaHCO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml", "field_path": "composition[0].concentration", "original": {"value": "56.8182", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Standalone Mixed solution", "interpretation": "The retained claim and current API exactly authenticate the provider g_l value calculated on 11 ml. The existing explanation already limits it to that provider basis. However, the same source preparation and original JCM1100 explicitly make the stock to 30 ml. Preserve both authentic source statements and resolve their conflict before using this stock as the canonical formulation; do not transfer the 11 ml rate to CTM.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaHCO3\",\n                \"compound_id\": 55,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.625,\n                \"unit\": \"g\",\n                \"g_l\": 56.8182,\n                \"mmol_l\": 676.351,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q78", "subject": "Existing linked stock rate: Sodium thioglycolate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml", "field_path": "composition[1].concentration", "original": {"value": "11.3636", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Standalone Mixed solution", "interpretation": "The retained claim and current API exactly authenticate the provider g_l value calculated on 11 ml. The existing explanation already limits it to that provider basis. However, the same source preparation and original JCM1100 explicitly make the stock to 30 ml. Preserve both authentic source statements and resolve their conflict before using this stock as the canonical formulation; do not transfer the 11 ml rate to CTM.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Sodium thioglycolate\",\n                \"compound_id\": 1644,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.125,\n                \"unit\": \"g\",\n                \"g_l\": 11.3636,\n                \"mmol_l\": 99.5937,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q79", "subject": "Standalone placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder", "interpretation": "VARIABLE on See source for composition is not an ingredient amount or verified stock parameter. Preserve the historical placeholder until exact structure is repaired; retain incomplete_composition while real nested additions remain missing.", "sources": [{"locator": "$.data.solutions[6].steps[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\": \"Add distilled water to bring final volume to 30 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q80", "subject": "Missing nested addition in standalone5182: Solution 5", "local_fields": [], "decision": "add", "stage": "Standalone Mixed solution nested addition", "interpretation": "This exact liquid addition exists in current source but is absent from the standalone stock structure. Use its exact linked definition/stage; it is not a new direct ingredient in CTM.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\": \"Solution 5\",\n                \"solution_id\": 5183,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q81", "subject": "Missing nested addition in standalone5182: Solution 6", "local_fields": [], "decision": "add", "stage": "Standalone Mixed solution nested addition", "interpretation": "This exact liquid addition exists in current source but is absent from the standalone stock structure. Use its exact linked definition/stage; it is not a new direct ingredient in CTM.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\": \"Solution 6\",\n                \"solution_id\": 5184,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q82", "subject": "Missing nested addition in standalone5182: Vitamin solution A (1000 x stock)", "local_fields": [], "decision": "add", "stage": "Standalone Mixed solution nested addition", "interpretation": "This exact liquid addition exists in current source but is absent from the standalone stock structure. Use its exact linked definition/stage; it is not a new direct ingredient in CTM.", "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\": \"Vitamin solution A (1000 x stock)\",\n                \"solution_id\": 5185,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.25,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q83", "subject": "Missing nested addition in standalone5182: Vitamin solution B (1000 x stock)", "local_fields": [], "decision": "add", "stage": "Standalone Mixed solution nested addition", "interpretation": "This exact liquid addition exists in current source but is absent from the standalone stock structure. Use its exact linked definition/stage; it is not a new direct ingredient in CTM.", "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\": \"Vitamin solution B (1000 x stock)\",\n                \"solution_id\": 5186,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.25,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch067/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:007698.

data/merge_yaml/merged/CTM_MEDIUM.yaml: primary 44/53, secondary 34/53; data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml: primary 50/53, secondary 34/53. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 2 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:007698.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:007698.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Stock inputs and liquid additions are flattened into direct mass rates

major / open / confirmed; issue key: culturemech-007698-stock-flattening-and-units.

Both selected layers flatten stock masses into the main ingredient list, label milligram vitamin/amino-acid inputs as G_PER_L, treat the phosphate-buffer dose and all eleven liquid additions as mass rates, and combine multiple water inputs into 625 G_PER_L. HEPES 2.4 g/L is supported only in the explicitly prepared basal litre; its finished-medium basis is unverified.

### f2: Linked Mixed solution has conflicting volume bases and missing nested additions

major / open / confirmed; issue key: culturemech-007698-mixed-stock-denominator-conflict.

Standalone5182 retains two correctly authenticated provider rates based on 11 ml, while its preparation says to make up to 30 ml. Both facts already appear in the record. The source also supplies four nested liquid additions absent from its composition. Reusing this unresolved stock would not repair CTM.

### f3: The source preparation stages, pH controls and sterilization sequence are absent

major / open / confirmed; issue key: culturemech-007698-missing-source-preparation.

The selected documents omit the explicit basal make-up and pH 7.0, 2 M KOH strength, 121°C/40 min sequence, sealing/cooling and post-autoclave filtered stock addition. Stock pH 8.0 and 7.2 are different controls and must not become the root pH.

### f4: Generated CTM predates six verified owner groundings

minor / open / confirmed; issue key: culturemech-007698-stale-generated-groundings.

The maintained owner adds exact L-alanine, L-leucine, L-lysine, L-proline, L-serine and L-valine identifiers in its August20 event. The generated target from August6 lacks those six primary slots. Current OLS definitions match these source L forms; the owner repair is credited independently of the still incorrect amounts. Current single-owner merging retains owner science; it does not itself perform source verification.

### f5: Selected claims lack support and three secondary identifiers need bounded reconciliation

minor / open / confirmed; issue key: culturemech-007698-missing-evidence-current-linkage.

Selected formulation claims have no attached evidence. Glycine retains legacy MediaIngredientMech:000244; HEPES CHEBI:46756 and oxoglutarate CHEBI:16810 secondary assertions have no exact rows in the packaged current MIM index. These current absences do not prove historical invalidity. Literal OLS labels match; source oxoglutarate counterion/protonation, calcium-pantothenate stereochemistry and generic B12 form are not further resolved by the recipe.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the exact nested stock and basal stages in maintained input, preserving source batch amounts/units and every addition. Keep explicit basal and Mixed-solution make-up volumes distinct from mere solvent inputs; do not infer final-medium rates from listed water or stock labels.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve the old provider evidence and explicitly resolve the 11 versus 30 ml source conflict using the original preparation before canonical reuse. Restore all four nested additions, their exact definitions and stage-scoped evidence; retire the placeholder only when the structure is complete.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Represent each exact preparation stage and control, including stock-only reagent strengths/pH, with root evidence scoped to its field. Preserve the source-specific 40 min instruction rather than substituting a generic default.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

After repairing the maintained formulation, regenerate and verify retention of these six existing correct owner groundings. Preserve all prior history and append verified context with the actual correction date; do not rewrite historical events.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Attach claim-level evidence to retained as well as corrected amounts and stages. Reconcile current secondary links using exact authorities; preserve generic or unresolved source chemical scope instead of forcing an unsupported precise form. Do not treat current MIM absence as proof of historical error.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CTM_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch067/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch067/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch067/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch067/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm1100 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current official JCM page read, including the main and embedded stock tables, preparation and source-specific defaults. The page-wide default remains scoped to that source; named stock sections are separate from main-medium preparation. |
| apiJ1100 | https://mediadive.dsmz.de/rest/medium/J1100; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| togoM1173 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| solution5182 | https://mediadive.dsmz.de/rest/solution/5182; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15428 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15428; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15428 = glycine; definition ['The simplest (and the only achiral) proteinogenic amino acid, with a hydrogen atom as its side chain.']; formula ['C2H5NO2']; mass ['75.067']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15603 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15603; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15603 = L-leucine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of leucine.']; formula ['C6H13NO2']; mass ['131.175']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15971 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15971; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15971 = L-histidine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of the amino acid histidine.']; formula ['C6H9N3O2']; mass ['155.157']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16015 = L-glutamic acid; definition ['An optically active form of glutamic acid having &lt;small&gt;L&lt;/small&gt;-configuration.']; formula ['C5H9NO4']; mass ['147.13']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16414 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16414; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16414 = L-valine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of valine.']; formula ['C5H11NO2']; mass ['117.148']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16467 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16467; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16467 = L-arginine; definition ['An &lt;small&gt;L&lt;/small&gt;-α-amino acid that is the &lt;small&gt;L&lt;/small&gt;-isomer of arginine.']; formula ['C6H14N4O2']; mass ['174.204']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16643 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16643; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16643 = L-methionine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of methionine.']; formula ['C5H11NO2S']; mass ['149.215']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16810 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16810; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16810 = 2-oxoglutarate(2-); definition ['An oxo dicarboxylate obtained by deprotonation of both carboxy groups of 2-oxoglutaric acid.']; formula ['C5H4O5']; mass ['144.082']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16828 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16828; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16828 = L-tryptophan; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of tryptophan.']; formula ['C11H12N2O2']; mass ['204.229']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16857 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16857; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16857 = L-threonine; definition ['An optically active form of threonine having &lt;small&gt;L&lt;/small&gt;-configuration.']; formula ['C4H9NO3']; mass ['119.12']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16977 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16977; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16977 = L-alanine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of alanine.']; formula ['C3H7NO2']; mass ['89.094']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17053 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17053; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17053 = L-aspartic acid; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of aspartic acid.']; formula ['C4H7NO4']; mass ['133.103']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17115 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17115; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17115 = L-serine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of serine.']; formula ['C3H7NO3']; mass ['105.093']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17154 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17154 = nicotinamide; definition ['A pyridinecarboxamide that is pyridine in which the hydrogen at position 3 is replaced by a carboxamide group.']; formula ['C6H6N2O']; mass ['122.127']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17191 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17191; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17191 = L-isoleucine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of isoleucine.']; formula ['C6H13NO2']; mass ['131.175']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17196 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17196; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17196 = L-asparagine; definition ['An optically active form of asparagine having &lt;small&gt;L&lt;/small&gt;-configuration.']; formula ['C4H8N2O3']; mass ['132.119']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17203 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17203; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17203 = L-proline; definition ['Pyrrolidine in which the &lt;em&gt;pro&lt;/em&gt;-&lt;i&gt;S&lt;/i&gt; hydrogen at position 2 is substituted by a carboxylic acid group. &lt;small&gt;L&lt;/small&gt;-Proline is the only one of the twenty DNA-encoded amino acids which has a secondary amino group α to the carboxyl group. It is an essential component of collagen and is important for proper functioning of joints and tendons. It also helps maintain and strengthen heart muscles.']; formula ['C5H9NO2']; mass ['115.132']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17295 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17295; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17295 = L-phenylalanine; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of phenylalanine.']; formula ['C9H11NO2']; mass ['165.192']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17561 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17561 = L-cysteine; definition ['An optically active form of cysteine having &lt;small&gt;L&lt;/small&gt;-configuration.']; formula ['C3H7NO2S']; mass ['121.161']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17895 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17895; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17895 = L-tyrosine; definition ['An optically active form of tyrosine having &lt;small&gt;L&lt;/small&gt;-configuration.']; formula ['C9H11NO3']; mass ['181.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi18019 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18019; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:18019 = L-lysine; definition ['An &lt;small&gt;L&lt;/small&gt;-α-amino acid; the &lt;small&gt;L&lt;/small&gt;-isomer of lysine.']; formula ['C6H14N2O2']; mass ['146.19']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi18050 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18050; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:18050 = L-glutamine; definition ['An optically active form of glutamine having &lt;small&gt;L&lt;/small&gt;-configuration.']; formula ['C5H10N2O3']; mass ['146.146']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29073 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29073; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29073 = L-ascorbic acid; definition ['The &lt;small&gt;L&lt;/small&gt;-enantiomer of ascorbic acid and conjugate acid of &lt;small&gt;L&lt;/small&gt;-ascorbate.']; formula ['C6H8O6']; mass ['176.124']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30769 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30769; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30769 = citric acid; definition ['A tricarboxylic acid that is propane-1,2,3-tricarboxylic acid bearing a hydroxy substituent at position 2. It is an important metabolite in the pathway of all aerobic organisms.']; formula ['C6H8O7']; mass ['192.123']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31440 = copper(II) sulfate pentahydrate; definition ['The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid.']; formula ['Cu.5H2O.O4S']; mass ['249.684']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31604 = ferric ammonium citrate; definition ['A mixture of indefinite composition that contains ferric and ammonium cations and citrate(3−) anions, ferric ammonium citrate may be obtained as red crystals or a brownish yellow powder or as green crystals or powder. It is added to foods as an acidity regulator and anticaking agent. It is also used as a positive oral contrast agent in magnetic resonance imaging, and was formerly administered orally as a source of iron for the treatment of iron-deficiency anaemia.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32035 = potassium hydroxide; definition []; formula ['HO.K']; mass ['56.105']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi46756 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:46756 = HEPES; definition []; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86214 = cobalt dinitrate hexahydrate; definition ['A hydrate that is the hexahydrate form of cobalt dinitrate.']; formula ['Co.6H2O.2NO3']; mass ['291.031']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86481 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86481 = sodium thioglycolate; definition ['An organic sodium salt having thioglycolate(1−) as the counterion.']; formula ['C2H3O2S.Na']; mass ['114.101']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi9532 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9532; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:9532 = thiamine(1+) diphosphate; definition ['A thiamine phosphate that is thiamine(1+) in which the hydroxy group has been replaced by a diphosphate group. It is the active form of vitamin B&lt;small&gt;&lt;sub&gt;1&lt;/sub&gt;&lt;/small&gt; and an essential cofactor for enzymes in key metabolic pathways.']; formula ['C12H19N4O7P2S']; mass ['425.32']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch067/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/ctm_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CTM_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ctm_medium__057c0b18.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_5182_Mixed_solution.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current solution5182 raw bytes exactly match the cited historical SHA, and 6 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch067/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer69 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer70 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer71 | scripts/migrate_solutions_from_ingredients.py; _is_solution; _resolve_solution; _migrate_media_file | context_only | Current _is_solution uses name patterns, _resolve_solution keeps concentrations while creating empty reference stubs or matching a name-indexed solution, and _migrate_media_file appends those solutions and history. It does not reconstruct nested source batches or authenticate copied unit/basis. |
| writer72 | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _extract_assembled_solutions; _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph | context_only | Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions distinguish primary sections, nested stocks and assembled solutions. _parse_unit maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices still require a verified source basis. _extract_preparation_steps retains comments. _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied object. These present behaviors neither authenticate historical execution nor prove that all source metadata survived the old import. |
| writer73 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer74 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer75 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| dep76 | data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| stock-auth | REVIEW_WORK/batch067/record04/scoped-attached-claims.json; claims | supports | Both existing 5182 claims match the exact current raw digest and literal objects. Their provider-basis limitation is retained; the primary preparation conflict is independently assessed. |
| quantity-inventory | REVIEW_WORK/batch067/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The primary explicitly makes basal medium to 1 L and Mixed solution to 30 ml; other listed water amounts and the eventual combined-medium volume are not independent final-volume measurements.
- The provider publishes different normalization bases, including 28 ml for the main source and 11 ml for Mixed solution; these do not override the exact primary preparation.
- No organism-specific growth evidence is inferred. Same-name CultureMech:002279 historical reports are comparison-only and do not authorize owner or formulation transfer.
- Exact current raw/digest agreement authenticates the scoped historical snippets, not past retrieval time or code execution. Generic oxoglutarate, calcium-pantothenate and B12 supplied forms retain their documented uncertainty.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T125328Z-ctm-medium-batch067
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of ctm_medium
started_at: '2026-10-28T12:36:55.911963Z'
finished_at: '2026-10-28T12:53:28.395809Z'
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
summary: CTM identity is clear, but its basal medium, nested stocks and finishing
  addition were flattened. Repair source stages and units, restore the explicit preparation
  controls, resolve the linked Mixed-solution volume conflict, then regenerate while
  preserving the owner’s six later correct groundings.
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
  - path: data/merge_yaml/merged/CTM_MEDIUM.yaml
    sha256: ef6b87bae2a814467298df5a48741e46dcfe89ed836d77e43e8210f5de722949
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    sha256: 1a6894b1a0f1182db7e88840740c25f7446119cae3acbeb48813cebbd5882a20
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml
    sha256: ab2a4e320b78ffd86d89c9c967b60494df38cf2522c2fd66ac8ed6fdbd68b838
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_5182_Mixed_solution.yaml.md
    sha256: 397baf5f5078181d8382d83ca434db0532d7e836dce2ff1528c0f63efcda4bc1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CTM_MEDIUM.md
    sha256: e56d55cbce0d1d3d2799317a79018af60f9091f64d89f37ba515a309e1d9661a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ctm_medium__057c0b18.md
    sha256: bd88cc1852dec2ab514f7c458473acedbde2e77a632819eef9e7bf8f9cbea101
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.md
    sha256: 0d69193810f4054b5a8696b2db9507cb42c88c4135625793e98d388bde31303f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/ctm_medium.md
    sha256: 523f95faab35fbab647def3891d1d49ece621d8fd7b811f5ac2cefd6032ea2a1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.md
    sha256: 5bfeecf17024db22753fe52147458c6c7cee1095f4bf04cb43e7234104e4af6c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
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
  selection: Authoritative batch067 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007698
targets:
- target_id: CultureMech:007698
  path: data/merge_yaml/merged/CTM_MEDIUM.yaml
  label: ctm_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007698
  command: just validate-schema data/merge_yaml/merged/CTM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007698
  command: just validate-strict data/merge_yaml/merged/CTM_MEDIUM.yaml --workers 1
    --out REVIEW_WORK/batch067/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:007698
  command: just validate-terms data/merge_yaml/merged/CTM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:007698
  command: just validate-references data/merge_yaml/merged/CTM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CTM_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:53:28.312272Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: ef6b87bae2a814467298df5a48741e46dcfe89ed836d77e43e8210f5de722949
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:53:28.312471Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 1a6894b1a0f1182db7e88840740c25f7446119cae3acbeb48813cebbd5882a20
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch067/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:36:56.984666Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: b2b3144df84717d35d84f7c7e89c587f2f98e7a3f5e23b943adf18dd88b4cc91
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch067/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:36:57.925994Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: d437ed293e57fcee6068fbd3d4273ff7c2d11132b7ce369a07a523533b2ba51a
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch067/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:36:58.999129Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 30fb2dfa0259bba91596bf359c21b4304439ae12f2b9c0e728b9365f6335b503
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch067/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:36:59.849191Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 1adadc81511132bc1c93118b6dac640cf3f5fe4e2f0c9bfebfdf8d64bc350b2f
- evidence_id: jcm1100
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:37:49.799412Z'
  support: supports
  summary: Complete current official JCM page read, including the main and embedded
    stock tables, preparation and source-specific defaults. The page-wide default
    remains scoped to that source; named stock sections are separate from main-medium
    preparation.
  snapshot_sha256: 7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37
- evidence_id: apiJ1100
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1100
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:37:49.700332Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6
- evidence_id: togoM1173
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:37:49.472475Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1
- evidence_id: solution5182
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5182
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:37:49.435990Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:49.173221Z'
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
  accessed_at: '2026-10-28T12:37:42.846650Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15428
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15428
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:49.094464Z'
  support: supports
  summary: OLS current exact CHEBI:15428 = glycine; definition ['The simplest (and
    the only achiral) proteinogenic amino acid, with a hydrogen atom as its side chain.'];
    formula ['C2H5NO2']; mass ['75.067']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: fe15e67af15eb83fc8824f11d1ba2dec039cb13dee005535e9acc71c1a2dd9d2
- evidence_id: chebi15603
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15603
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:49.082043Z'
  support: supports
  summary: OLS current exact CHEBI:15603 = L-leucine; definition ['The <small>L</small>-enantiomer
    of leucine.']; formula ['C6H13NO2']; mass ['131.175']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 6521f1a28e5542f4f9e841cb5317a7a9e3f1533c75f75a642e1d733597e8eaae
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:49.024288Z'
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
  accessed_at: '2026-10-28T12:37:48.807449Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi15971
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15971
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.805712Z'
  support: supports
  summary: OLS current exact CHEBI:15971 = L-histidine; definition ['The <small>L</small>-enantiomer
    of the amino acid histidine.']; formula ['C6H9N3O2']; mass ['155.157']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0f82377c7d3db94cf3da496c0733d9f3d2c554afe30dba8a419e365481765ca2
- evidence_id: chebi16015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.529752Z'
  support: supports
  summary: OLS current exact CHEBI:16015 = L-glutamic acid; definition ['An optically
    active form of glutamic acid having <small>L</small>-configuration.']; formula
    ['C5H9NO4']; mass ['147.13']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d4c039ee9f11823d174df5fa637b67506440f658c3492afcdf8032f0316f77d3
- evidence_id: chebi16414
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16414
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.476071Z'
  support: supports
  summary: OLS current exact CHEBI:16414 = L-valine; definition ['The <small>L</small>-enantiomer
    of valine.']; formula ['C5H11NO2']; mass ['117.148']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 2132a900d3d49a2154d6af0140a372475bb7e26d8a5a0cb23a1ebd81e2c13f78
- evidence_id: chebi16467
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16467
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.454762Z'
  support: supports
  summary: OLS current exact CHEBI:16467 = L-arginine; definition ['An <small>L</small>-α-amino
    acid that is the <small>L</small>-isomer of arginine.']; formula ['C6H14N4O2'];
    mass ['174.204']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f119fe4b838d4a2f22f3ca2b773986a4176dc2faa472d514ee2244d1a0e268a0
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.384033Z'
  support: supports
  summary: OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic
    thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the
    5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi16643
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16643
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.173824Z'
  support: supports
  summary: OLS current exact CHEBI:16643 = L-methionine; definition ['The <small>L</small>-enantiomer
    of methionine.']; formula ['C5H11NO2S']; mass ['149.215']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 963a10130fd9176e9acef383e145461419b40fc9b1bdc6c1b2efacaaa2ebf7e4
- evidence_id: chebi16810
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16810
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:48.171206Z'
  support: supports
  summary: OLS current exact CHEBI:16810 = 2-oxoglutarate(2-); definition ['An oxo
    dicarboxylate obtained by deprotonation of both carboxy groups of 2-oxoglutaric
    acid.']; formula ['C5H4O5']; mass ['144.082']; obsolete=False. Literal label is
    distinct from supplied-form equivalence.
  snapshot_sha256: ed9d4b6102140f49ba3e57df7536a3825e73219eae009b89747d7cc01a6f7cd2
- evidence_id: chebi16828
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16828
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.878494Z'
  support: supports
  summary: OLS current exact CHEBI:16828 = L-tryptophan; definition ['The <small>L</small>-enantiomer
    of tryptophan.']; formula ['C11H12N2O2']; mass ['204.229']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 3fb1e4690c0329a6e8e938f940c1552828530f203cafef4bccf132f25c6fa670
- evidence_id: chebi16857
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16857
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.760267Z'
  support: supports
  summary: OLS current exact CHEBI:16857 = L-threonine; definition ['An optically
    active form of threonine having <small>L</small>-configuration.']; formula ['C4H9NO3'];
    mass ['119.12']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f24b1ae636c557bbe461a4e92885cae350d6e097a211ce515348eb0cfd742065
- evidence_id: chebi16977
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16977
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.555236Z'
  support: supports
  summary: OLS current exact CHEBI:16977 = L-alanine; definition ['The <small>L</small>-enantiomer
    of alanine.']; formula ['C3H7NO2']; mass ['89.094']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 26270a6494e38ac1668a42786239c2ad5e2de319005e9ce7b6b21cfe0818f62f
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.432728Z'
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
- evidence_id: chebi17053
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17053
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.400881Z'
  support: supports
  summary: OLS current exact CHEBI:17053 = L-aspartic acid; definition ['The <small>L</small>-enantiomer
    of aspartic acid.']; formula ['C4H7NO4']; mass ['133.103']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 126097ce9aff0f51245379fb0af89a63531805d82ab653deebbc7c97b8e8183e
- evidence_id: chebi17115
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17115
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.237240Z'
  support: supports
  summary: OLS current exact CHEBI:17115 = L-serine; definition ['The <small>L</small>-enantiomer
    of serine.']; formula ['C3H7NO3']; mass ['105.093']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 76fbf17336bdbaf863b725127c24ac48cf7a9be179ce1f38553e53147e1599fd
- evidence_id: chebi17154
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:47.035306Z'
  support: supports
  summary: OLS current exact CHEBI:17154 = nicotinamide; definition ['A pyridinecarboxamide
    that is pyridine in which the hydrogen at position 3 is replaced by a carboxamide
    group.']; formula ['C6H6N2O']; mass ['122.127']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 45306ecefbab1f5ece64d269af2560e313330916a57d04fa168f19044dfe37d8
- evidence_id: chebi17191
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17191
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.948843Z'
  support: supports
  summary: OLS current exact CHEBI:17191 = L-isoleucine; definition ['The <small>L</small>-enantiomer
    of isoleucine.']; formula ['C6H13NO2']; mass ['131.175']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 1e75aa711908898885e414e43a0a316664fd0615ed92846d45a131807f1d5607
- evidence_id: chebi17196
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17196
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.865051Z'
  support: supports
  summary: OLS current exact CHEBI:17196 = L-asparagine; definition ['An optically
    active form of asparagine having <small>L</small>-configuration.']; formula ['C4H8N2O3'];
    mass ['132.119']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 5e546def4d69297d487ef85c54167891ab8505aa4b59957410bcc05722f4b8a2
- evidence_id: chebi17203
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17203
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.793789Z'
  support: supports
  summary: OLS current exact CHEBI:17203 = L-proline; definition ['Pyrrolidine in
    which the <em>pro</em>-<i>S</i> hydrogen at position 2 is substituted by a carboxylic
    acid group. <small>L</small>-Proline is the only one of the twenty DNA-encoded
    amino acids which has a secondary amino group α to the carboxyl group. It is an
    essential component of collagen and is important for proper functioning of joints
    and tendons. It also helps maintain and strengthen heart muscles.']; formula ['C5H9NO2'];
    mass ['115.132']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 3ad4a8030e2e3a9b35b0316e79ef77ad5418ae26619793b4b738e8f113beaa95
- evidence_id: chebi17295
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17295
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.765630Z'
  support: supports
  summary: OLS current exact CHEBI:17295 = L-phenylalanine; definition ['The <small>L</small>-enantiomer
    of phenylalanine.']; formula ['C9H11NO2']; mass ['165.192']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: bd8c336021ba86896d58e890e2106545b39b403cd8d60e7d1af644aae27af3f2
- evidence_id: chebi17561
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.583511Z'
  support: supports
  summary: OLS current exact CHEBI:17561 = L-cysteine; definition ['An optically active
    form of cysteine having <small>L</small>-configuration.']; formula ['C3H7NO2S'];
    mass ['121.161']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: ea82f62413bdf5b5575ec20c8bd9e19bb3f41efb6f1efa500401656e6c186292
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.451757Z'
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
- evidence_id: chebi17895
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17895
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.319757Z'
  support: supports
  summary: OLS current exact CHEBI:17895 = L-tyrosine; definition ['An optically active
    form of tyrosine having <small>L</small>-configuration.']; formula ['C9H11NO3'];
    mass ['181.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f6b525337789bede30fa1955ec21ab2f90d5c2d0694e626246b6e47302e7d19d
- evidence_id: chebi18019
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18019
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.235690Z'
  support: supports
  summary: OLS current exact CHEBI:18019 = L-lysine; definition ['An <small>L</small>-α-amino
    acid; the <small>L</small>-isomer of lysine.']; formula ['C6H14N2O2']; mass ['146.19'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d814b9be1b9cf98dd3d47aa95462dca70f8e20369fb34533f9bb423dae81e2e6
- evidence_id: chebi18050
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18050
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:46.160890Z'
  support: supports
  summary: OLS current exact CHEBI:18050 = L-glutamine; definition ['An optically
    active form of glutamine having <small>L</small>-configuration.']; formula ['C5H10N2O3'];
    mass ['146.146']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: ea6962cb23b57693b704e4af74677da4591f3cf60cef9bb8377d9d364187ca30
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.940331Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi29073
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29073
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.821258Z'
  support: supports
  summary: OLS current exact CHEBI:29073 = L-ascorbic acid; definition ['The <small>L</small>-enantiomer
    of ascorbic acid and conjugate acid of <small>L</small>-ascorbate.']; formula
    ['C6H8O6']; mass ['176.124']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 0b28e968641b08cdf5ea7985f3cabadd3c3cf711178b96ed92a53f5eb2f115ad
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.672982Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30769
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30769
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.623887Z'
  support: supports
  summary: OLS current exact CHEBI:30769 = citric acid; definition ['A tricarboxylic
    acid that is propane-1,2,3-tricarboxylic acid bearing a hydroxy substituent at
    position 2. It is an important metabolite in the pathway of all aerobic organisms.'];
    formula ['C6H8O7']; mass ['192.123']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: caa0ca256c3120bc99d649d132215c88d06cdff463dffac90dcecef930e7c429
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.544543Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.356258Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.339187Z'
  support: supports
  summary: OLS current exact CHEBI:31440 = copper(II) sulfate pentahydrate; definition
    ['The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid.'];
    formula ['Cu.5H2O.O4S']; mass ['249.684']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31604
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:45.182855Z'
  support: supports
  summary: OLS current exact CHEBI:31604 = ferric ammonium citrate; definition ['A
    mixture of indefinite composition that contains ferric and ammonium cations and
    citrate(3−) anions, ferric ammonium citrate may be obtained as red crystals or
    a brownish yellow powder or as green crystals or powder. It is added to foods
    as an acidity regulator and anticaking agent. It is also used as a positive oral
    contrast agent in magnetic resonance imaging, and was formerly administered orally
    as a source of iron for the treatment of iron-deficiency anaemia.']; formula None;
    mass None; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 31acf125b469ffd64e2de503550d29336a7a0f99c8a3ea24b80b53bdb715e7f8
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:42.218657Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.999295Z'
  support: supports
  summary: OLS current exact CHEBI:32035 = potassium hydroxide; definition []; formula
    ['HO.K']; mass ['56.105']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 6ed3df00965b4707265cfced80411c4b1937b727f8c2093addbc467f88ce2ec8
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:42.212205Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.953496Z'
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
  accessed_at: '2026-10-28T12:37:41.629717Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:41.613499Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi46756
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.737747Z'
  support: supports
  summary: OLS current exact CHEBI:46756 = HEPES; definition []; formula None; mass
    None; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 4270cc705078ff2f1787f98b7dbcf05c96b1eccd333801a00cff01b855298a69
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.692710Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:40.995108Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:40.988661Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86214
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.588853Z'
  support: supports
  summary: OLS current exact CHEBI:86214 = cobalt dinitrate hexahydrate; definition
    ['A hydrate that is the hexahydrate form of cobalt dinitrate.']; formula ['Co.6H2O.2NO3'];
    mass ['291.031']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 90cf3337643bc22bd3940bfbdee70a144b13af549ea12534184385f036b4633c
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:40.106888Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi86481
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.299242Z'
  support: supports
  summary: OLS current exact CHEBI:86481 = sodium thioglycolate; definition ['An organic
    sodium salt having thioglycolate(1−) as the counterion.']; formula ['C2H3O2S.Na'];
    mass ['114.101']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 444afd61f333b50a1be0a902c67c78c7b97483187e4fb554b6f7deeb009cd966
- evidence_id: chebi9532
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9532
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:37:44.096177Z'
  support: supports
  summary: OLS current exact CHEBI:9532 = thiamine(1+) diphosphate; definition ['A
    thiamine phosphate that is thiamine(1+) in which the hydroxy group has been replaced
    by a diphosphate group. It is the active form of vitamin B<small><sub>1</sub></small>
    and an essential cofactor for enzymes in key metabolic pathways.']; formula ['C12H19N4O7P2S'];
    mass ['425.32']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d53690ac7132f9ea63b09705112112ef5dc13b26b5e42c9775fded98e7640100
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch067/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T12:53:28.328535Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 5309c049656b4afe6c0c8906b510a6c5434ec3481746bb905a412acf5e147002
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:53:28.329285Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 0d69193810f4054b5a8696b2db9507cb42c88c4135625793e98d388bde31303f
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/ctm_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:53:28.329311Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 523f95faab35fbab647def3891d1d49ece621d8fd7b811f5ac2cefd6032ea2a1
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CTM_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:53:28.329334Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: e56d55cbce0d1d3d2799317a79018af60f9091f64d89f37ba515a309e1d9661a
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ctm_medium__057c0b18.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:53:28.329356Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: bd88cc1852dec2ab514f7c458473acedbde2e77a632819eef9e7bf8f9cbea101
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_5182_Mixed_solution.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:53:28.329376Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    solution5182 raw bytes exactly match the cited historical SHA, and 6 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 397baf5f5078181d8382d83ca434db0532d7e836dce2ff1528c0f63efcda4bc1
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:53:28.329394Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 5bfeecf17024db22753fe52147458c6c7cee1095f4bf04cb43e7234104e4af6c
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch067/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T12:53:28.329416Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 58b2e5c14b947319bdaeef58348d44f006676f5621e6168e2a78461085cc5e33
- evidence_id: writer69
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T12:53:28.329475Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer70
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T12:53:28.329500Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer71
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _is_solution; _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T12:53:28.329533Z'
  support: context_only
  summary: Current _is_solution uses name patterns, _resolve_solution keeps concentrations
    while creating empty reference stubs or matching a name-indexed solution, and
    _migrate_media_file appends those solutions and history. It does not reconstruct
    nested source batches or authenticate copied unit/basis.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer72
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _extract_assembled_solutions;
    _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph
  accessed_at: '2026-10-28T12:53:28.329581Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions
    distinguish primary sections, nested stocks and assembled solutions. _parse_unit
    maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices
    still require a verified source basis. _extract_preparation_steps retains comments.
    _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied
    object. These present behaviors neither authenticate historical execution nor
    prove that all source metadata survived the old import.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer73
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T12:53:28.329605Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer74
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T12:53:28.329630Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer75
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T12:53:28.329652Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: dep76
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T12:53:28.329666Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: ab2a4e320b78ffd86d89c9c967b60494df38cf2522c2fd66ac8ed6fdbd68b838
- evidence_id: stock-auth
  kind: record_content
  reference: REVIEW_WORK/batch067/record04/scoped-attached-claims.json
  locator: claims
  accessed_at: '2026-10-28T12:53:28.332540Z'
  support: supports
  summary: Both existing 5182 claims match the exact current raw digest and literal
    objects. Their provider-basis limitation is retained; the primary preparation
    conflict is independently assessed.
  snapshot_sha256: 7301dd3cee58003bef0c4a5fe7be76260c2cac37107a54a149620d5e6a398158
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch067/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T12:53:28.395221Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: e4d39b8cce4cc5f063433c2759af69f3600fb40dbdaa36f84945f597fb688629
assessments:
- assessment_id: a1
  area: identity
  topic: Exact CTM source identity and stock graph
  outcome: supported
  summary: Selected TOGO M1173 is JCM1100. The source has a basal stage and a finishing
    Mixed solution, with separate named stocks. MediaDive5182 is the exact locally
    linked stock; the differently maintained CTM CultureMech:002279 report is comparison-only.
    No organism or experimental growth assertion is inferred.
  target_ids:
  - CultureMech:007698
  evidence_ids:
  - jcm1100
  - togoM1173
  - apiJ1100
  - solution5182
- assessment_id: a2
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: The selected owner and target have identical amounts; only six later owner
    primary groundings are missing from the generated target. Earlier zero-source-check
    reports remain incomplete leads. The exact5182 current raw matches six historical
    quoted objects and both attached claims, while its explicit provider-only limit
    and unresolved nested additions are preserved. The source instruction now makes
    the volume conflict actionable without pretending the old provider evidence was
    fabricated. Current conservative merging preserves scientific fields and rejects
    incompatible formulations. Inspected writer behavior is described separately by
    exact file and function; it does not prove historical execution.
  target_ids:
  - CultureMech:007698
  evidence_ids:
  - history-auth
  - writer69
  - writer70
  - writer71
  - writer72
  - writer73
  - writer74
  - writer75
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 128 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:007698
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:007698",
    "selected_concentration_field_count": 128, "selected_concentration_fields_covered":
    128, "decisions": [{"decision_id": "q1", "subject": "Collapsed water from multiple
    stocks", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "625.0", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "625.0", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Distinct basal and stock solvent
    inputs", "interpretation": "625 G_PER_L aggregates mixed-unit water entries from
    different recipe stages and is not a real concentration. Restore the basal make-up
    to 1 L separately from each stock water input. The TOGO mixed-stock 19 ml is arithmetic-derived;
    the primary requires make-up to 30 ml and does not independently measure that
    solvent amount.", "sources": [{"locator": "$.components[0].items[0]", "source_key":
    "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "$.components[7].items[0]", "source_key": "togoM1173",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 19,\n          \"unit\": \"ml\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0
    L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40
    min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation.
    Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below)
    to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject":
    "HEPES", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "2.4", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "2.4", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "One-litre basal medium before
    Mixed solution addition", "interpretation": "The primary supports 2.4 g in a basal
    preparation explicitly made up to 1 L, hence 2.4 g/L at that stage. The stored
    direct rate lacks that stage; the final medium receives 30 ml Mixed solution afterward
    without an independently measured final volume. Do not adopt API g_l=85.7143 based
    on its incomplete 28 ml metadata.", "sources": [{"locator": "HTML tr[4]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "HEPES\n2.4\ng",
    "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"HEPES\",\n          \"volume\": 2.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001142\",\n          \"gmo_id\": \"GMO_001142\",\n          \"label\":
    \"HEPES\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"HEPES\",\n                        \"compound_id\":
    371,\n                        \"amount\": 2.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 85.7143,\n                        \"mmol_l\":
    359.676,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key":
    "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0
    L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40
    min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation.
    Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below)
    to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject":
    "KOH adjustment", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "evidence_only", "stage": "Basal pH adjustment",
    "interpretation": "The fixed dose is not stated, so VARIABLE does not contradict
    the source. Preserve an unquantified adjustment and separately record source 2
    M reagent strength and pH 7.0; neither is represented by the placeholder itself.",
    "sources": [{"locator": "$.components[0].items[6]", "source_key": "togoM1173",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"KOH\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\":
    \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0
    L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40
    min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation.
    Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below)
    to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject":
    "MgSO4・7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "3.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "3.75", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 (50 x stock) composition",
    "interpretation": "The source specifies 3.75 g in Solution 1 (50 x stock), not
    as an undiluted direct main-medium rate. Restore that stock composition and its
    enclosing dose. Provider g_l=3.56803 is source metadata, not an independently
    measured stock/final-medium volume. Listed solvent does not alone justify a denominator.",
    "sources": [{"locator": "HTML tr[5]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n3.75\ng",
    "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[2].items[2]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 3.75,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3.75,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.56803,\n                        \"mmol_l\":
    14.4762,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "CaCl2・2H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "original": {"value": "1.8", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1.8", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 (50 x stock) composition",
    "interpretation": "The source specifies 1.8 g in Solution 1 (50 x stock), not
    as an undiluted direct main-medium rate. Restore that stock composition and its
    enclosing dose. Provider g_l=1.71265 is source metadata, not an independently
    measured stock/final-medium volume. Listed solvent does not alone justify a denominator.",
    "sources": [{"locator": "HTML tr[6]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "CaCl\n2\n·2H\n2\nO\n1.80\ng",
    "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[2].items[3]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 1.8,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 1.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.71265,\n                        \"mmol_l\":
    11.6495,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "Citric acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[5].concentration",
    "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 (50 x stock) composition",
    "interpretation": "The source specifies 0.3 g in Solution 1 (50 x stock), not
    as an undiluted direct main-medium rate. Restore that stock composition and its
    enclosing dose. Provider g_l=0.285442 is source metadata, not an independently
    measured stock/final-medium volume. Listed solvent does not alone justify a denominator.",
    "sources": [{"locator": "HTML tr[7]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Citric acid\n0.30\ng",
    "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[2].items[4]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Citric acid\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001112\",\n          \"gmo_id\": \"GMO_001112\",\n          \"label\":
    \"Citric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Citric acid\",\n                        \"compound_id\":
    348,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.285442,\n                        \"mmol_l\":
    1.48575,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "Na2MoO4・2H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "original": {"value": "0.39", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.39", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition",
    "interpretation": "The source specifies 0.39 g in Trace metal solution, not as
    an undiluted direct main-medium rate. Restore that stock composition and its enclosing
    dose. Provider g_l=0.39 is source metadata, not an independently measured stock/final-medium
    volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator":
    "HTML tr[14]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Na\n2\nMoO\n4\n·2H\n2\nO\n0.39\ng",
    "quote_representation": "HTML tr[14] DOM text"}, {"locator": "$.components[3].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 0.39,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.39,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.39,\n                        \"mmol_l\":
    1.6119,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[7].concentration",
    "original": {"value": "2.86", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "2.86", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition",
    "interpretation": "The source specifies 2.86 g in Trace metal solution, not as
    an undiluted direct main-medium rate. Restore that stock composition and its enclosing
    dose. Provider g_l=2.86 is source metadata, not an independently measured stock/final-medium
    volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator":
    "HTML tr[11]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "H\n3\nBO\n3\n2.86\ng",
    "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[3].items[2]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 2.86,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 2.86,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.86,\n                        \"mmol_l\":
    46.2484,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "MnCl2・4H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[8].concentration",
    "original": {"value": "1.81", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "1.81", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition",
    "interpretation": "The source specifies 1.81 g in Trace metal solution, not as
    an undiluted direct main-medium rate. Restore that stock composition and its enclosing
    dose. Provider g_l=1.81 is source metadata, not an independently measured stock/final-medium
    volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator":
    "HTML tr[12]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "MnCl\n2\n·4H\n2\nO\n1.81\ng",
    "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[3].items[3]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 1.81,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 1.81,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.81,\n                        \"mmol_l\":
    9.1458,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "ZnSO4・7H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[9].concentration",
    "original": {"value": "0.222", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.222", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition",
    "interpretation": "The source specifies 0.222 g in Trace metal solution, not as
    an undiluted direct main-medium rate. Restore that stock composition and its enclosing
    dose. Provider g_l=0.222 is source metadata, not an independently measured stock/final-medium
    volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator":
    "HTML tr[13]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "ZnSO\n4\n·7H\n2\nO\n0.222\ng",
    "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.components[3].items[4]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"ZnSO4・7H2O\",\n          \"volume\": 0.222,\n          \"unit\": \"g\",\n          \"gmo\":
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
    JSON object"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.222,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.222,\n                        \"mmol_l\":
    0.77201,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "CuSO4・5H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[10].concentration",
    "original": {"value": "0.079", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.079",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition",
    "interpretation": "The source specifies 0.079 g in Trace metal solution, not as
    an undiluted direct main-medium rate. Restore that stock composition and its enclosing
    dose. Provider g_l=0.079 is source metadata, not an independently measured stock/final-medium
    volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator":
    "HTML tr[15]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "CuSO\n4\n·5H\n2\nO\n0.079\ng",
    "quote_representation": "HTML tr[15] DOM text"}, {"locator": "$.components[3].items[5]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"CuSO4・5H2O\",\n          \"volume\": 0.079,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\":
    \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[2].recipe[4]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.079,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.079,\n                        \"mmol_l\":
    0.316397,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "Co(NO3)2・6H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[11].concentration",
    "original": {"value": "0.049", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.049",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace metal solution composition",
    "interpretation": "The source specifies 0.049 g in Trace metal solution, not as
    an undiluted direct main-medium rate. Restore that stock composition and its enclosing
    dose. Provider g_l=0.049 is source metadata, not an independently measured stock/final-medium
    volume. Listed solvent does not alone justify a denominator.", "sources": [{"locator":
    "HTML tr[16]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Co(NO\n3\n)\n2\n·6H\n2\nO\n0.049\ng",
    "quote_representation": "HTML tr[16] DOM text"}, {"locator": "$.components[3].items[6]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Co(NO3)2・6H2O\",\n          \"volume\": 0.049,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001110\",\n          \"gmo_id\": \"GMO_001110\",\n          \"label\":
    \"Cobalt(II) nitrate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[2].recipe[5]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Co(NO3)2 x 6 H2O\",\n                        \"compound_id\":
    541,\n                        \"amount\": 0.049,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.049,\n                        \"mmol_l\":
    0.168365,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "K2HPO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[12].concentration",
    "original": {"value": "15.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "15.3", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 2 composition", "interpretation":
    "The source specifies 15.3 g in Solution 2, not as an undiluted direct main-medium
    rate. Restore that stock composition and its enclosing dose. Provider g_l=15.3
    is source metadata, not an independently measured stock/final-medium volume. Listed
    solvent does not alone justify a denominator.", "sources": [{"locator": "HTML
    tr[18]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "K\n2\nHPO\n4\n15.3\ng",
    "quote_representation": "HTML tr[18] DOM text"}, {"locator": "$.components[4].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 15.3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 15.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15.3,\n                        \"mmol_l\":
    87.8422,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "Ferric ammonium citrate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "12", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "12", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Solution 3 composition", "interpretation": "The
    source specifies 12 g in Solution 3, not as an undiluted direct main-medium rate.
    Restore that stock composition and its enclosing dose. Provider g_l=12 is source
    metadata, not an independently measured stock/final-medium volume. Listed solvent
    does not alone justify a denominator.", "sources": [{"locator": "HTML tr[20]",
    "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Ferric ammonium
    citrate\n12.0\ng", "quote_representation": "HTML tr[20] DOM text"}, {"locator":
    "$.components[5].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Ferric ammonium citrate\",\n          \"volume\": 12,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001147\",\n          \"gmo_id\": \"GMO_001147\",\n          \"label\":
    \"Ammonium ferric citrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[4].recipe[0]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Ferric ammonium citrate\",\n                        \"compound_id\":
    97,\n                        \"amount\": 12,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\":
    45.805,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "2-Oxoglutarate", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[14].concentration",
    "original": {"value": "14.6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "14.6", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 4 composition", "interpretation":
    "The source specifies 14.6 g in Solution 4, not as an undiluted direct main-medium
    rate. Restore that stock composition and its enclosing dose. Provider g_l=14.6
    is source metadata, not an independently measured stock/final-medium volume. Listed
    solvent does not alone justify a denominator.", "sources": [{"locator": "HTML
    tr[22]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "2-Oxoglutarate\n14.6\ng",
    "quote_representation": "HTML tr[22] DOM text"}, {"locator": "$.components[6].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"2-Oxoglutarate\",\n          \"volume\": 14.6,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001861\",\n          \"gmo_id\": \"GMO_001861\",\n          \"label\":
    \"alpha-Ketoglutaric acid\",\n          \"properties\": [],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[5].recipe[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"2-Oxoglutarate\",\n                        \"compound_id\":
    1992,\n                        \"amount\": 14.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 14.6,\n                        \"mmol_l\":
    101.331,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "NaHCO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[15].concentration",
    "original": {"value": "0.625", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.625",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution composition",
    "interpretation": "The source specifies 0.625 g in Mixed solution, explicitly
    made up to 30 ml. Restore that stock stage; the entire 30 ml is added after preparing
    the basal litre. A final-medium g/L is not established by the stored direct value.
    The provider''s separate 11 ml normalization conflicts with its own preparation
    instruction.", "sources": [{"locator": "HTML tr[24]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "NaHCO\n3\n0.625\ng", "quote_representation":
    "HTML tr[24] DOM text"}, {"locator": "$.components[7].items[1]", "source_key":
    "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 0.625,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\":
    \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].recipe[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 0.625,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 56.8182,\n                        \"mmol_l\":
    676.351,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key":
    "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject":
    "Sodium thioglycolate", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.125",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.125",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution composition",
    "interpretation": "The source specifies 0.125 g in Mixed solution, explicitly
    made up to 30 ml. Restore that stock stage; the entire 30 ml is added after preparing
    the basal litre. A final-medium g/L is not established by the stored direct value.
    The provider''s separate 11 ml normalization conflicts with its own preparation
    instruction.", "sources": [{"locator": "HTML tr[25]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Sodium thioglycolate\n0.125\ng",
    "quote_representation": "HTML tr[25] DOM text"}, {"locator": "$.components[7].items[2]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Sodium thioglycolate\",\n          \"volume\": 0.125,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001132\",\n          \"gmo_id\": \"GMO_001132\",\n          \"label\":
    \"Sodium thioglycolate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].recipe[1]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Sodium thioglycolate\",\n                        \"compound_id\":
    1644,\n                        \"amount\": 0.125,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 11.3636,\n                        \"mmol_l\":
    99.5937,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]", "source_key":
    "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject":
    "Bacto peptone (BD--Difco)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 5 composition", "interpretation":
    "The source specifies 10 g in Solution 5, not as an undiluted direct main-medium
    rate. Restore that stock composition and its enclosing dose. Provider g_l=100
    is source metadata, not an independently measured stock/final-medium volume. Listed
    solvent does not alone justify a denominator.", "sources": [{"locator": "HTML
    tr[30]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Bacto peptone
    (BD-Difco)\n10.0\ng", "quote_representation": "HTML tr[30] DOM text"}, {"locator":
    "$.components[8].items[1]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Bacto peptone (BD--Difco)\",\n          \"volume\": 10,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001089\",\n          \"gmo_id\":
    \"GMO_001089\",\n          \"label\": \"Bacto &trade; Peptone\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[7].recipe[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\":
    19,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    100,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "L--Cysteine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[18].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[36]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Cysteine\n100.0\nmg",
    "quote_representation": "HTML tr[36] DOM text"}, {"locator": "$.components[9].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Cysteine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001318\",\n          \"gmo_id\": \"GMO_001318\",\n          \"label\":
    \"Cysteine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[4]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"L-Cysteine\",\n                        \"compound_id\":
    671,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    2.06339,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "Glycine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[19].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[39]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Glycine\n100.0\nmg",
    "quote_representation": "HTML tr[39] DOM text"}, {"locator": "$.components[9].items[2]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Glycine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001559\",\n          \"gmo_id\": \"GMO_001559\",\n          \"label\":
    \"Glycine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[7]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Glycine\",\n                        \"compound_id\":
    358,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    3.33023,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "L--Glutamic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[20].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[37]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Glutamic
    acid\n100.0\nmg", "quote_representation": "HTML tr[37] DOM text"}, {"locator":
    "$.components[9].items[3]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Glutamic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001570\",\n          \"gmo_id\": \"GMO_001570\",\n          \"label\":
    \"L-Glutamic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[5]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"L-Glutamic acid\",\n                        \"compound_id\":
    374,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.69918,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "L--Alanine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[21].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[32]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Alanine\n100.0\nmg",
    "quote_representation": "HTML tr[32] DOM text"}, {"locator": "$.components[9].items[4]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Alanine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001766\",\n          \"gmo_id\": \"GMO_001766\",\n          \"label\":
    \"L-Alanine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[0]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"L-Alanine\",\n                        \"compound_id\":
    274,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    2.80615,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "L--Arginine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[22].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[33]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Arginine\n100.0\nmg",
    "quote_representation": "HTML tr[33] DOM text"}, {"locator": "$.components[9].items[5]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Arginine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001767\",\n          \"gmo_id\": \"GMO_001767\",\n          \"label\":
    \"L-Arginine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[1]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"L-Arginine\",\n                        \"compound_id\":
    1327,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.43513,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "L--Aspartic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[23].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[35]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Aspartic
    acid\n100.0\nmg", "quote_representation": "HTML tr[35] DOM text"}, {"locator":
    "$.components[9].items[6]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Aspartic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001770\",\n          \"gmo_id\": \"GMO_001770\",\n          \"label\":
    \"L-Aspartic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[3]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"L-Aspartic acid\",\n                        \"compound_id\":
    1328,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.87829,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "L--Glutamine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[24].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[38]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Glutamine\n100.0\nmg",
    "quote_representation": "HTML tr[38] DOM text"}, {"locator": "$.components[9].items[7]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Glutamine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001776\",\n          \"gmo_id\": \"GMO_001776\",\n          \"label\":
    \"L-Glutamine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[6]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"L-Glutamine\",\n                        \"compound_id\":
    134,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.71069,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "L--Isoleucine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[25].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[41]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Isoleucine\n100.0\nmg",
    "quote_representation": "HTML tr[41] DOM text"}, {"locator": "$.components[9].items[8]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Isoleucine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001783\",\n          \"gmo_id\": \"GMO_001783\",\n          \"label\":
    \"L-Isoleucine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[9]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"L-Isoleucine\",\n                        \"compound_id\":
    447,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.90592,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "L--Leucine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[26].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[42]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Leucine\n100.0\nmg",
    "quote_representation": "HTML tr[42] DOM text"}, {"locator": "$.components[9].items[9]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Leucine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001785\",\n          \"gmo_id\": \"GMO_001785\",\n          \"label\":
    \"L-Leucine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[10]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"L-Leucine\",\n                        \"compound_id\":
    446,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.90592,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "L--Lysine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[27].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[43]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Lysine\n100.0\nmg",
    "quote_representation": "HTML tr[43] DOM text"}, {"locator": "$.components[9].items[10]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Lysine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001788\",\n          \"gmo_id\": \"GMO_001788\",\n          \"label\":
    \"L-Lysine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[11]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"L-Lysine\",\n                        \"compound_id\":
    1973,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.7101,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "L--Phenylalanine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[28].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[45]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Phenylalanine\n100.0\nmg",
    "quote_representation": "HTML tr[45] DOM text"}, {"locator": "$.components[9].items[11]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Phenylalanine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001794\",\n          \"gmo_id\": \"GMO_001794\",\n          \"label\":
    \"L-Phenylalanine \",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[13]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"L-Phenylalanine\",\n                        \"compound_id\":
    1332,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.51341,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "L--Proline", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[29].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[46]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Proline\n100.0\nmg",
    "quote_representation": "HTML tr[46] DOM text"}, {"locator": "$.components[9].items[12]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Proline\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001797\",\n          \"gmo_id\": \"GMO_001797\",\n          \"label\":
    \"L-Proline\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[14]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"L-Proline\",\n                        \"compound_id\":
    1130,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    2.17146,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "L--Serine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[30].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[47]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Serine\n100.0\nmg",
    "quote_representation": "HTML tr[47] DOM text"}, {"locator": "$.components[9].items[13]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Serine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001800\",\n          \"gmo_id\": \"GMO_001800\",\n          \"label\":
    \"L-Serine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[15]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"L-Serine\",\n                        \"compound_id\":
    133,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    2.37891,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q32", "subject": "L--Threonine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[31].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[48]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Threonine\n100.0\nmg",
    "quote_representation": "HTML tr[48] DOM text"}, {"locator": "$.components[9].items[14]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Threonine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001803\",\n          \"gmo_id\": \"GMO_001803\",\n          \"label\":
    \"L-Threonine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[16]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    17,\n                        \"compound\": \"L-Threonine\",\n                        \"compound_id\":
    658,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    2.09872,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "L--Tryptophan", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[32].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[49]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Tryptophan\n100.0\nmg",
    "quote_representation": "HTML tr[49] DOM text"}, {"locator": "$.components[9].items[15]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Tryptophan\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001805\",\n          \"gmo_id\": \"GMO_001805\",\n          \"label\":
    \"L-Tryptophan\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[17]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    18,\n                        \"compound\": \"L-Tryptophan\",\n                        \"compound_id\":
    449,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.22417,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "L--Tyrosine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[33].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[50]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Tyrosine\n100.0\nmg",
    "quote_representation": "HTML tr[50] DOM text"}, {"locator": "$.components[9].items[16]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Tyrosine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001808\",\n          \"gmo_id\": \"GMO_001808\",\n          \"label\":
    \"L-Tyrosine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[18]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    19,\n                        \"compound\": \"L-Tyrosine\",\n                        \"compound_id\":
    1333,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.37977,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q35", "subject": "L--Valine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[34].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[34].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[51]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Valine\n100.0\nmg",
    "quote_representation": "HTML tr[51] DOM text"}, {"locator": "$.components[9].items[17]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Valine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001811\",\n          \"gmo_id\": \"GMO_001811\",\n          \"label\":
    \"L-Valine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[19]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    20,\n                        \"compound\": \"L-Valine\",\n                        \"compound_id\":
    1334,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    2.13402,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "L--Asparagine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[35].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[35].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[34]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Asparagine\n100.0\nmg",
    "quote_representation": "HTML tr[34] DOM text"}, {"locator": "$.components[9].items[18]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Asparagine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001870\",\n          \"gmo_id\": \"GMO_001870\",\n          \"label\":
    \"L-Asparagine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[2]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"L-Asparagine\",\n                        \"compound_id\":
    829,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.89222,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q37", "subject": "L--Histidine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[36].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[36].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[40]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Histidine\n100.0\nmg",
    "quote_representation": "HTML tr[40] DOM text"}, {"locator": "$.components[9].items[19]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Histidine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001872\",\n          \"gmo_id\": \"GMO_001872\",\n          \"label\":
    \"L-Histidine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[8].recipe[8]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"L-Histidine\",\n                        \"compound_id\":
    132,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.61134,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q38", "subject": "L--Methionine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[37].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[37].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 6 composition", "interpretation":
    "The source specifies 100 mg in Solution 6; the local G_PER_L row incorrectly
    places it among direct main-medium ingredients and loses the source mg basis.
    Restore the exact stock input and nested dose chain. Provider g_l=0.25 is a separately
    declared stock normalization, not a final-medium rate.", "sources": [{"locator":
    "HTML tr[44]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Methionine\n100.0\nmg",
    "quote_representation": "HTML tr[44] DOM text"}, {"locator": "$.components[9].items[20]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Methionine\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001791\",\n          \"gmo_id\": \"GMO_001791\",\n          \"label\":
    \"L-Methionine \",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[12]", "source_key":
    "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"L-Methionine\",\n                        \"compound_id\":
    1330,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.67549,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q39", "subject": "10 mM Potassium phosphate
    buffer (pH 7.2)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "ingredients[38].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[38].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "This is a 100 ml addition of 10 mM potassium
    phosphate buffer at pH 7.2 to Vitamin solution A, not 100 g/L of a main-medium
    ingredient. Preserve dose, reagent strength and buffer pH independently; the buffer
    salt ratio is not supplied.", "sources": [{"locator": "HTML tr[66]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "10 mM Potassium
    phosphate buffer (pH 7.2)\n100.0\nml", "quote_representation": "HTML tr[66] DOM
    text"}, {"locator": "$.components[10].items[0]", "source_key": "togoM1173", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at":
    "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"10 mM Potassium phosphate buffer (pH 7.2)\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001308\",\n          \"gmo_id\": \"GMO_001308\",\n          \"label\":
    \"Potassium phosphate buffer\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "$.data.solutions[9].recipe[13]", "source_key": "apiJ1100",
    "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Potassium phosphate buffer\",\n                        \"compound_id\":
    275,\n                        \"attribute\": \"pH 7.2, 10 mM\",\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"mmol_l\":
    1,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q40", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[39].concentration",
    "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[39].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 10 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=0.1 is a separately declared stock normalization, not
    a final-medium rate.", "sources": [{"locator": "HTML tr[53]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Biotin\n10.0\nmg", "quote_representation":
    "HTML tr[53] DOM text"}, {"locator": "$.components[10].items[1]", "source_key":
    "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.409316,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q41", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "ingredients[40].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "ingredients[40].concentration", "original": {"value": "100", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition",
    "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock);
    the local G_PER_L row incorrectly places it among direct main-medium ingredients
    and loses the source mg basis. Restore the exact stock input and nested dose chain.
    Provider g_l=1 is a separately declared stock normalization, not a final-medium
    rate.", "sources": [{"locator": "HTML tr[62]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "p\n-Aminobenzoic acid\n100.0\nmg",
    "quote_representation": "HTML tr[62] DOM text"}, {"locator": "$.components[10].items[2]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[9]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    7.29182,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q42", "subject": "Thiamine・HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[41].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[41].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[55]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Thiamine·HCl\n100.0\nmg",
    "quote_representation": "HTML tr[55] DOM text"}, {"locator": "$.components[10].items[3]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[2]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    2.96472,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q43", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "ingredients[42].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "ingredients[42].concentration", "original": {"value": "100", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition",
    "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock);
    the local G_PER_L row incorrectly places it among direct main-medium ingredients
    and loses the source mg basis. Restore the exact stock input and nested dose chain.
    Provider g_l=1 is a separately declared stock normalization, not a final-medium
    rate.", "sources": [{"locator": "HTML tr[58]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Calcium pantothenate\n100.0\nmg",
    "quote_representation": "HTML tr[58] DOM text"}, {"locator": "$.components[10].items[4]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[5]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    2.09849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q44", "subject": "Pyridoxine・HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[43].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[43].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[63]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Pyridoxine·HCl\n100.0\nmg",
    "quote_representation": "HTML tr[63] DOM text"}, {"locator": "$.components[10].items[5]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\":
    \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[10]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.86287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q45", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[44].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[44].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[59]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Folic acid\n100.0\nmg",
    "quote_representation": "HTML tr[59] DOM text"}, {"locator": "$.components[10].items[6]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\":
    \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[6]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    2.26552,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q46", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[45].concentration",
    "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[45].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 10 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=0.1 is a separately declared stock normalization, not
    a final-medium rate.", "sources": [{"locator": "HTML tr[54]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Riboflavin\n10.0\nmg", "quote_representation":
    "HTML tr[54] DOM text"}, {"locator": "$.components[10].items[7]", "source_key":
    "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\":
    \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[1]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.265675,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q47", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[46].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[46].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[61]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Nicotinic acid\n100.0\nmg",
    "quote_representation": "HTML tr[61] DOM text"}, {"locator": "$.components[10].items[8]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[8]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    8.12282,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q48", "subject": "Nicotinamide", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[47].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[47].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[60]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Nicotinamide\n100.0\nmg",
    "quote_representation": "HTML tr[60] DOM text"}, {"locator": "$.components[10].items[9]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Nicotinamide\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001162\",\n          \"gmo_id\": \"GMO_001162\",\n          \"label\":
    \"Nicotinamide\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[7]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Nicotinamide\",\n                        \"compound_id\":
    337,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    8.18867,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q49", "subject": "Thiamine pyrophosphate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "ingredients[48].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "ingredients[48].concentration", "original": {"value": "100", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Vitamin solution A (1000 x stock) composition",
    "interpretation": "The source specifies 100 mg in Vitamin solution A (1000 x stock);
    the local G_PER_L row incorrectly places it among direct main-medium ingredients
    and loses the source mg basis. Restore the exact stock input and nested dose chain.
    Provider g_l=1 is a separately declared stock normalization, not a final-medium
    rate.", "sources": [{"locator": "HTML tr[56]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Thiamine pyrophosphate\n100.0\nmg",
    "quote_representation": "HTML tr[56] DOM text"}, {"locator": "$.components[10].items[10]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Thiamine pyrophosphate\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001660\",\n          \"gmo_id\": \"GMO_001660\",\n          \"label\":
    \"Thiamine pyrophosphate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[3]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine pyrophosphate\",\n                        \"compound_id\":
    778,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    2.17029,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q50", "subject": "β-NAD", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[49].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[49].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[65]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "β-NAD\n100.0\nmg", "quote_representation":
    "HTML tr[65] DOM text"}, {"locator": "$.components[10].items[11]", "source_key":
    "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"β-NAD\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001691\",\n          \"gmo_id\": \"GMO_001691\",\n          \"label\":
    \"Beta-NAD\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[12]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"beta-NAD\",\n                        \"compound_id\":
    1798,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    1.50504,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q51", "subject": "Lipoic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[50].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[50].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[64]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Lipoic acid\n100.0\nmg",
    "quote_representation": "HTML tr[64] DOM text"}, {"locator": "$.components[10].items[12]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Lipoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\":
    \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[11]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\":
    368,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.8466,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q52", "subject": "L--Ascorbic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[51].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[51].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution A (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    A (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[57]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "L-Ascorbic acid\n100.0\nmg",
    "quote_representation": "HTML tr[57] DOM text"}, {"locator": "$.components[10].items[13]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"L--Ascorbic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001813\",\n          \"gmo_id\": \"GMO_001813\",\n          \"label\":
    \"L-Ascorbic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[9].recipe[4]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"L-Ascorbic acid\",\n                        \"compound_id\":
    701,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.67795,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q53", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "ingredients[52].concentration",
    "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "ingredients[52].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Vitamin solution B (1000 x stock)
    composition", "interpretation": "The source specifies 100 mg in Vitamin solution
    B (1000 x stock); the local G_PER_L row incorrectly places it among direct main-medium
    ingredients and loses the source mg basis. Restore the exact stock input and nested
    dose chain. Provider g_l=1 is a separately declared stock normalization, not a
    final-medium rate.", "sources": [{"locator": "HTML tr[67]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Vitamin B\n12\n100.0\nmg",
    "quote_representation": "HTML tr[67] DOM text"}, {"locator": "$.components[11].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[10].recipe[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    0.73779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q54", "subject": "Solution 1 (see below)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "solutions[0].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "solutions[0].concentration", "original": {"value": "20", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation":
    "The exact source dose is 20 ml = 0.02 L to basal medium, not 20 g/L. Restore
    the enclosing stock hierarchy; nested doses are not all additions directly to
    the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[2]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Solution 1 (see below)\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[0]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution
    1 (see below)\n20.0\nml", "quote_representation": "HTML tr[0] DOM text"}, {"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution 1 (50 x stock)\",\n                        \"solution_id\":
    5177,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q55", "subject": "Solution 2 (see below)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "solutions[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "solutions[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation":
    "The exact source dose is 3 ml = 0.003 L to basal medium, not 3 g/L. Restore the
    enclosing stock hierarchy; nested doses are not all additions directly to the
    final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[3]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Solution 2 (see below)\",\n          \"volume\": 3,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[1]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution
    2 (see below)\n3.0\nml", "quote_representation": "HTML tr[1] DOM text"}, {"locator":
    "$.data.solutions[0].recipe[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution 2\",\n                        \"solution_id\":
    5179,\n                        \"amount\": 3,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q56", "subject": "Solution 3 (see below)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "solutions[2].concentration", "original": {"value": "2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "solutions[2].concentration", "original": {"value": "2", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation":
    "The exact source dose is 2 ml = 0.002 L to basal medium, not 2 g/L. Restore the
    enclosing stock hierarchy; nested doses are not all additions directly to the
    final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[4]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Solution 3 (see below)\",\n          \"volume\": 2,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[2]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution
    3 (see below)\n2.0\nml", "quote_representation": "HTML tr[2] DOM text"}, {"locator":
    "$.data.solutions[0].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution 3\",\n                        \"solution_id\":
    5180,\n                        \"amount\": 2,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q57", "subject": "Solution 4 (see below)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "solutions[3].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "solutions[3].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Basal medium liquid addition", "interpretation":
    "The exact source dose is 2.5 ml = 0.0025 L to basal medium, not 2.5 g/L. Restore
    the enclosing stock hierarchy; nested doses are not all additions directly to
    the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[0].items[5]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Solution 4 (see below)\",\n          \"volume\": 2.5,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[3]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution
    4 (see below)\n2.5\nml", "quote_representation": "HTML tr[3] DOM text"}, {"locator":
    "$.data.solutions[0].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution 4\",\n                        \"solution_id\":
    5181,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q58", "subject": "Mixed solution", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[4].concentration",
    "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "solutions[4].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "After basal autoclaving liquid
    addition", "interpretation": "The exact source dose is 30 ml = 0.03 L to after
    basal autoclaving, not 30 g/L. Restore the enclosing stock hierarchy; nested doses
    are not all additions directly to the final medium. No mass density is assumed.",
    "sources": [{"locator": "$.components[1].items[0]", "source_key": "togoM1173",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Mixed solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0
    L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40
    min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation.
    Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below)
    to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q59", "subject":
    "0.25 M EDTA・2Na solution (pH 8.0)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "solutions[5].concentration", "original": {"value": "0.6", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "solutions[5].concentration", "original": {"value": "0.6", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 liquid addition", "interpretation":
    "The exact source dose is 0.6 ml = 0.0006 L to solution 1, not 0.6 g/L. Restore
    the enclosing stock hierarchy; nested doses are not all additions directly to
    the final medium. The source also explicitly specifies 0.25 M disodium EDTA at
    pH 8.0; preserve that strength separately from this dose.", "sources": [{"locator":
    "$.components[2].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"0.25 M EDTA・2Na solution (pH 8.0)\",\n          \"volume\": 0.6,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 0.25,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001962\",\n          \"gmo_id\": \"GMO_001962\",\n          \"label\":
    \"Disodium EDTA solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}, {"locator": "HTML
    tr[8]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "0.25 M EDTA·2Na
    solution (pH 8.0)\n0.60\nml", "quote_representation": "HTML tr[8] DOM text"},
    {"locator": "$.data.solutions[1].recipe[3]", "source_key": "apiJ1100", "reference":
    "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\":
    34,\n                        \"attribute\": \"pH 8.0, 0.25 M\",\n                        \"amount\":
    0.6,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q60", "subject": "Trace metal solution (see below)", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path": "solutions[6].concentration",
    "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "solutions[6].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution 1 liquid addition", "interpretation":
    "The exact source dose is 50 ml = 0.05 L to solution 1, not 50 g/L. Restore the
    enclosing stock hierarchy; nested doses are not all additions directly to the
    final medium. No mass density is assumed.", "sources": [{"locator": "$.components[2].items[5]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Trace metal solution (see below)\",\n          \"volume\": 50,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"},
    {"locator": "HTML tr[9]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Trace metal
    solution (see below)\n50.0\nml", "quote_representation": "HTML tr[9] DOM text"},
    {"locator": "$.data.solutions[1].recipe[4]", "source_key": "apiJ1100", "reference":
    "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Trace metal solution\",\n                        \"solution_id\":
    5178,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q61", "subject": "Solution 5 (see below)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "solutions[7].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "solutions[7].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Mixed solution liquid addition", "interpretation":
    "The exact source dose is 0.5 ml = 0.0005 L to mixed solution, not 0.5 g/L. Restore
    the enclosing stock hierarchy; nested doses are not all additions directly to
    the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[7].items[3]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Solution 5 (see below)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[26]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution
    5 (see below)\n0.5\nml", "quote_representation": "HTML tr[26] DOM text"}, {"locator":
    "$.data.solutions[6].recipe[2]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution 5\",\n                        \"solution_id\":
    5183,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q62", "subject": "Solution 6 (see below)",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml", "field_path":
    "solutions[8].concentration", "original": {"value": "10", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml", "field_path":
    "solutions[8].concentration", "original": {"value": "10", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Mixed solution liquid addition", "interpretation":
    "The exact source dose is 10 ml = 0.01 L to mixed solution, not 10 g/L. Restore
    the enclosing stock hierarchy; nested doses are not all additions directly to
    the final medium. No mass density is assumed.", "sources": [{"locator": "$.components[7].items[4]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Solution 6 (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1173\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[27]", "source_key":
    "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Solution
    6 (see below)\n10.0\nml", "quote_representation": "HTML tr[27] DOM text"}, {"locator":
    "$.data.solutions[6].recipe[3]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution 6\",\n                        \"solution_id\":
    5184,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q63", "subject": "Vitamin solution A (see
    below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "solutions[9].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "solutions[9].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution liquid addition",
    "interpretation": "The exact source dose is 0.25 ml = 0.00025 L to mixed solution,
    not 0.25 g/L. Restore the enclosing stock hierarchy; nested doses are not all
    additions directly to the final medium. No mass density is assumed.", "sources":
    [{"locator": "$.components[7].items[5]", "source_key": "togoM1173", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at":
    "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Vitamin solution A (see below)\",\n          \"volume\": 0.25,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"},
    {"locator": "HTML tr[28]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Vitamin solution
    A (see below)\n0.25\nml", "quote_representation": "HTML tr[28] DOM text"}, {"locator":
    "$.data.solutions[6].recipe[4]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Vitamin solution A (1000 x stock)\",\n                        \"solution_id\":
    5185,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q64", "subject": "Vitamin solution B (see
    below)", "local_fields": [{"record_path": "data/merge_yaml/merged/CTM_MEDIUM.yaml",
    "field_path": "solutions[10].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml",
    "field_path": "solutions[10].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Mixed solution liquid addition",
    "interpretation": "The exact source dose is 0.25 ml = 0.00025 L to mixed solution,
    not 0.25 g/L. Restore the enclosing stock hierarchy; nested doses are not all
    additions directly to the final medium. No mass density is assumed.", "sources":
    [{"locator": "$.components[7].items[6]", "source_key": "togoM1173", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at":
    "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Vitamin solution B (see below)\",\n          \"volume\": 0.25,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M1173\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"},
    {"locator": "HTML tr[29]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Vitamin solution
    B (see below)\n0.25\nml", "quote_representation": "HTML tr[29] DOM text"}, {"locator":
    "$.data.solutions[6].recipe[5]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Vitamin solution B (1000 x stock)\",\n                        \"solution_id\":
    5186,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q65", "subject": "Solution 1 (50 x stock)
    separate water input", "local_fields": [], "decision": "add", "stage": "Stock
    preparation solvent", "interpretation": "Preserve 1 L water at this stock stage.
    This is an input, not an independently measured final stock volume, and must not
    be summed with other stock waters.", "sources": [{"locator": "$.components[2].items[1]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[10]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[10] DOM text"}]}, {"decision_id": "q66", "subject":
    "Trace metal solution separate water input", "local_fields": [], "decision": "add",
    "stage": "Stock preparation solvent", "interpretation": "Preserve 1 L water at
    this stock stage. This is an input, not an independently measured final stock
    volume, and must not be summed with other stock waters.", "sources": [{"locator":
    "$.components[3].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[17]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[17] DOM text"}]}, {"decision_id": "q67", "subject":
    "Solution 2 separate water input", "local_fields": [], "decision": "add", "stage":
    "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock
    stage. This is an input, not an independently measured final stock volume, and
    must not be summed with other stock waters.", "sources": [{"locator": "$.components[4].items[0]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[19]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[19] DOM text"}]}, {"decision_id": "q68", "subject":
    "Solution 3 separate water input", "local_fields": [], "decision": "add", "stage":
    "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock
    stage. This is an input, not an independently measured final stock volume, and
    must not be summed with other stock waters.", "sources": [{"locator": "$.components[5].items[0]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[21]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[21] DOM text"}]}, {"decision_id": "q69", "subject":
    "Solution 4 separate water input", "local_fields": [], "decision": "add", "stage":
    "Stock preparation solvent", "interpretation": "Preserve 1 L water at this stock
    stage. This is an input, not an independently measured final stock volume, and
    must not be summed with other stock waters.", "sources": [{"locator": "$.components[6].items[0]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[23]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[23] DOM text"}]}, {"decision_id": "q70", "subject":
    "Solution 5 separate water input", "local_fields": [], "decision": "add", "stage":
    "Stock preparation solvent", "interpretation": "Preserve 100 ml water at this
    stock stage. This is an input, not an independently measured final stock volume,
    and must not be summed with other stock waters.", "sources": [{"locator": "$.components[8].items[0]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[31]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n100.0\nml",
    "quote_representation": "HTML tr[31] DOM text"}]}, {"decision_id": "q71", "subject":
    "Solution 6 separate water input", "local_fields": [], "decision": "add", "stage":
    "Stock preparation solvent", "interpretation": "Preserve 400 ml water at this
    stock stage. This is an input, not an independently measured final stock volume,
    and must not be summed with other stock waters.", "sources": [{"locator": "$.components[9].items[0]",
    "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 400,\n          \"unit\": \"ml\",\n          \"gmo\":
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
    JSON object"}, {"locator": "HTML tr[52]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n400.0\nml",
    "quote_representation": "HTML tr[52] DOM text"}]}, {"decision_id": "q72", "subject":
    "Vitamin solution B (1000 x stock) separate water input", "local_fields": [],
    "decision": "add", "stage": "Stock preparation solvent", "interpretation": "Preserve
    100 ml water at this stock stage. This is an input, not an independently measured
    final stock volume, and must not be summed with other stock waters.", "sources":
    [{"locator": "$.components[11].items[0]", "source_key": "togoM1173", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at":
    "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
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
    JSON object"}, {"locator": "HTML tr[68]", "source_key": "jcm1100", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Distilled water\n100.0\nml",
    "quote_representation": "HTML tr[68] DOM text"}]}, {"decision_id": "q73", "subject":
    "Basal preparation controls", "local_fields": [], "decision": "add", "stage":
    "Basal medium before finishing addition", "interpretation": "Restore make-up to
    1 L, pH 7.0 using 2 M KOH, autoclaving at 121°C for 40 min, immediate sealing
    to avoid oxygenation, cooling to around 70°C, and addition of 30 ml filter-sterilized
    Mixed solution. The source-specific 40 min supersedes the page-wide generic 15
    min default. This preparation is not organism-growth evidence.", "sources": [{"locator":
    "$.data.solutions[0].steps[1]", "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Mix all ingredients in 1.0 L medium bottle. Add distilled water close to 1.0
    L. Adjust pH to 7.0 with 2 M KOH and fill up to 1.0 L. Autoclave at 121C for 40
    min. After autoclaving, seal medium bottle immediately in order to avoid oxygenation.
    Cool down to around 70C. Add 30 ml filter-sterilized Mixed solution (see below)
    to the autoclaved CTM medium basis for completing the CTM medium.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q74", "subject":
    "Mixed solution final volume", "local_fields": [], "decision": "add", "stage":
    "Mixed stock before addition", "interpretation": "The stock is explicitly made
    up to 30 ml. This supports 0.625 g / 0.030 L = 20.833333… g/L sodium bicarbonate
    and 0.125 g / 0.030 L = 4.166666… g/L sodium thioglycolate at this stock stage
    only. Retain uncertainty about other stock final volumes and the eventual finished-medium
    volume.", "sources": [{"locator": "$.data.solutions[6].steps[0]", "source_key":
    "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    143-143", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "Add distilled
    water to bring final volume to 30 ml.", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q75", "subject": "EDTA reagent and stock pH", "local_fields":
    [], "decision": "add", "stage": "Solution 1 addition reagent", "interpretation":
    "Retain 0.25 M disodium EDTA reagent strength and pH 8.0; these are not the basal
    pH or final-medium EDTA concentration. Salt hydration and preparation are not
    further specified.", "sources": [{"locator": "HTML tr[8]", "source_key": "jcm1100",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100", "source_raw_sha256":
    "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37", "source_text_sha256":
    "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421", "accessed_at":
    "2026-10-28T12:37:49.799412Z", "exact_source_quote": "0.25 M EDTA·2Na solution
    (pH 8.0)\n0.60\nml", "quote_representation": "HTML tr[8] DOM text"}, {"locator":
    "$.components[2].items[0]", "source_key": "togoM1173", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173",
    "source_raw_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "source_text_sha256": "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1",
    "accessed_at": "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"0.25 M EDTA・2Na solution (pH 8.0)\",\n          \"volume\": 0.6,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 0.25,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001962\",\n          \"gmo_id\": \"GMO_001962\",\n          \"label\":
    \"Disodium EDTA solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q76", "subject": "Vitamin A phosphate buffer control", "local_fields": [], "decision":
    "add", "stage": "Vitamin A solvent reagent", "interpretation": "Retain the 10
    mM phosphate buffer strength and pH 7.2 with its 100 ml addition. Do not infer
    its constituent salt ratio or treat pH 7.2 as the medium pH.", "sources": [{"locator":
    "HTML tr[66]", "source_key": "jcm1100", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1100",
    "source_raw_sha256": "7e1ae66a4acd07cf352b24f044396fd192c8135f001f2cd1c9a120da1c4bcd37",
    "source_text_sha256": "3ede543593f43fde49a0dfdf27c26fef9436c672a0b7e47a3219095990e44421",
    "accessed_at": "2026-10-28T12:37:49.799412Z", "exact_source_quote": "10 mM Potassium
    phosphate buffer (pH 7.2)\n100.0\nml", "quote_representation": "HTML tr[66] DOM
    text"}, {"locator": "$.components[10].items[0]", "source_key": "togoM1173", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1173", "source_raw_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "source_text_sha256":
    "e7819152f9392cafebb2405c1ecce11bc67bf5c886e4d99cf485f25ba708e6a1", "accessed_at":
    "2026-10-28T12:37:49.472475Z", "exact_source_quote": "{\n          \"component_name\":
    \"10 mM Potassium phosphate buffer (pH 7.2)\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001308\",\n          \"gmo_id\": \"GMO_001308\",\n          \"label\":
    \"Potassium phosphate buffer\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q77", "subject": "Existing linked stock rate:
    NaHCO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "56.8182",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Standalone Mixed solution",
    "interpretation": "The retained claim and current API exactly authenticate the
    provider g_l value calculated on 11 ml. The existing explanation already limits
    it to that provider basis. However, the same source preparation and original JCM1100
    explicitly make the stock to 30 ml. Preserve both authentic source statements
    and resolve their conflict before using this stock as the canonical formulation;
    do not transfer the 11 ml rate to CTM.", "sources": [{"locator": "$.data.recipe[0]",
    "source_key": "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182",
    "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3",
    "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3",
    "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"NaHCO3\",\n                \"compound_id\":
    55,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.625,\n                \"unit\":
    \"g\",\n                \"g_l\": 56.8182,\n                \"mmol_l\": 676.351,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q78", "subject":
    "Existing linked stock rate: Sodium thioglycolate", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml", "field_path":
    "composition[1].concentration", "original": {"value": "11.3636", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Standalone Mixed solution", "interpretation":
    "The retained claim and current API exactly authenticate the provider g_l value
    calculated on 11 ml. The existing explanation already limits it to that provider
    basis. However, the same source preparation and original JCM1100 explicitly make
    the stock to 30 ml. Preserve both authentic source statements and resolve their
    conflict before using this stock as the canonical formulation; do not transfer
    the 11 ml rate to CTM.", "sources": [{"locator": "$.data.recipe[1]", "source_key":
    "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256":
    "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256":
    "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at":
    "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"Sodium thioglycolate\",\n                \"compound_id\":
    1644,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.125,\n                \"unit\":
    \"g\",\n                \"g_l\": 11.3636,\n                \"mmol_l\": 99.5937,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[6].steps[0]",
    "source_key": "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100",
    "source_raw_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "source_text_sha256": "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6",
    "accessed_at": "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q79", "subject":
    "Standalone placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder",
    "interpretation": "VARIABLE on See source for composition is not an ingredient
    amount or verified stock parameter. Preserve the historical placeholder until
    exact structure is repaired; retain incomplete_composition while real nested additions
    remain missing.", "sources": [{"locator": "$.data.solutions[6].steps[0]", "source_key":
    "apiJ1100", "reference": "https://mediadive.dsmz.de/rest/medium/J1100", "source_raw_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "source_text_sha256":
    "dc2261353b529589bf4b677e43d69fd1f51e40fdbca32119eb51ff364a3c4fe6", "accessed_at":
    "2026-10-28T12:37:49.700332Z", "exact_source_quote": "{\n                        \"step\":
    \"Add distilled water to bring final volume to 30 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q80", "subject":
    "Missing nested addition in standalone5182: Solution 5", "local_fields": [], "decision":
    "add", "stage": "Standalone Mixed solution nested addition", "interpretation":
    "This exact liquid addition exists in current source but is absent from the standalone
    stock structure. Use its exact linked definition/stage; it is not a new direct
    ingredient in CTM.", "sources": [{"locator": "$.data.recipe[2]", "source_key":
    "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256":
    "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256":
    "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at":
    "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\":
    \"Solution 5\",\n                \"solution_id\": 5183,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q81", "subject": "Missing nested addition in standalone5182: Solution 6", "local_fields":
    [], "decision": "add", "stage": "Standalone Mixed solution nested addition", "interpretation":
    "This exact liquid addition exists in current source but is absent from the standalone
    stock structure. Use its exact linked definition/stage; it is not a new direct
    ingredient in CTM.", "sources": [{"locator": "$.data.recipe[3]", "source_key":
    "solution5182", "reference": "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256":
    "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "source_text_sha256":
    "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3", "accessed_at":
    "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\":
    \"Solution 6\",\n                \"solution_id\": 5184,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q82", "subject": "Missing nested addition in standalone5182: Vitamin solution
    A (1000 x stock)", "local_fields": [], "decision": "add", "stage": "Standalone
    Mixed solution nested addition", "interpretation": "This exact liquid addition
    exists in current source but is absent from the standalone stock structure. Use
    its exact linked definition/stage; it is not a new direct ingredient in CTM.",
    "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution5182", "reference":
    "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3",
    "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3",
    "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\":
    \"Vitamin solution A (1000 x stock)\",\n                \"solution_id\": 5185,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.25,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q83", "subject": "Missing nested addition in standalone5182: Vitamin solution
    B (1000 x stock)", "local_fields": [], "decision": "add", "stage": "Standalone
    Mixed solution nested addition", "interpretation": "This exact liquid addition
    exists in current source but is absent from the standalone stock structure. Use
    its exact linked definition/stage; it is not a new direct ingredient in CTM.",
    "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution5182", "reference":
    "https://mediadive.dsmz.de/rest/solution/5182", "source_raw_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3",
    "source_text_sha256": "0427bee089ebbe8b98f63d075252088472bcb8ba9b129164a798b06b50448ea3",
    "accessed_at": "2026-10-28T12:37:49.435990Z", "exact_source_quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\":
    \"Vitamin solution B (1000 x stock)\",\n                \"solution_id\": 5186,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.25,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch067/record04/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CTM_MEDIUM.yaml: primary 44/53, secondary 34/53;
    data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml: primary 50/53, secondary
    34/53. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI term is joined to
    its exact current OLS object and packaged MIM CSV rows. 2 numeric legacy MediaIngredientMech
    mentions occur across the complete selected documents, with exact locators in
    the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:007698
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
  - CultureMech:007698
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
  - CultureMech:007698
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-007698-stock-flattening-and-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock inputs and liquid additions are flattened into direct mass rates
  description: Both selected layers flatten stock masses into the main ingredient
    list, label milligram vitamin/amino-acid inputs as G_PER_L, treat the phosphate-buffer
    dose and all eleven liquid additions as mass rates, and combine multiple water
    inputs into 625 G_PER_L. HEPES 2.4 g/L is supported only in the explicitly prepared
    basal litre; its finished-medium basis is unverified.
  target_ids:
  - CultureMech:007698
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - jcm1100
  - togoM1173
  - apiJ1100
  rule_id: review-ingredient-concentrations/source-stage-unit-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-007698-mixed-stock-denominator-conflict
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Linked Mixed solution has conflicting volume bases and missing nested additions
  description: Standalone5182 retains two correctly authenticated provider rates based
    on 11 ml, while its preparation says to make up to 30 ml. Both facts already appear
    in the record. The source also supplies four nested liquid additions absent from
    its composition. Reusing this unresolved stock would not repair CTM.
  target_ids:
  - CultureMech:007698
  field_paths:
  - solutions[4].term
  - data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml::composition
  - data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml::preparation_notes
  - data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml::data_quality_flags
  evidence_ids:
  - solution5182
  - jcm1100
  - apiJ1100
  - stock-auth
  rule_id: review-ingredient-concentrations/source-volume-conflict
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml
    role: exact linked Mixed solution 5182 dependency; only this stock
- finding_id: f3
  issue_key: culturemech-007698-missing-source-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The source preparation stages, pH controls and sterilization sequence are
    absent
  description: The selected documents omit the explicit basal make-up and pH 7.0,
    2 M KOH strength, 121°C/40 min sequence, sealing/cooling and post-autoclave filtered
    stock addition. Stock pH 8.0 and 7.2 are different controls and must not become
    the root pH.
  target_ids:
  - CultureMech:007698
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - jcm1100
  - togoM1173
  - apiJ1100
  rule_id: review-yaml-record/source-preparation-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-007698-stale-generated-groundings
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated CTM predates six verified owner groundings
  description: The maintained owner adds exact L-alanine, L-leucine, L-lysine, L-proline,
    L-serine and L-valine identifiers in its August20 event. The generated target
    from August6 lacks those six primary slots. Current OLS definitions match these
    source L forms; the owner repair is credited independently of the still incorrect
    amounts. Current single-owner merging retains owner science; it does not itself
    perform source verification.
  target_ids:
  - CultureMech:007698
  field_paths:
  - ingredients[21].term
  - ingredients[26].term
  - ingredients[27].term
  - ingredients[29].term
  - ingredients[30].term
  - ingredients[34].term
  evidence_ids:
  - local0
  - local1
  - grounding
  rule_id: review-yaml-record/generated-record-freshness
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-007698-missing-evidence-current-linkage
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Selected claims lack support and three secondary identifiers need bounded
    reconciliation
  description: Selected formulation claims have no attached evidence. Glycine retains
    legacy MediaIngredientMech:000244; HEPES CHEBI:46756 and oxoglutarate CHEBI:16810
    secondary assertions have no exact rows in the packaged current MIM index. These
    current absences do not prove historical invalidity. Literal OLS labels match;
    source oxoglutarate counterion/protonation, calcium-pantothenate stereochemistry
    and generic B12 form are not further resolved by the recipe.
  target_ids:
  - CultureMech:007698
  field_paths:
  - evidence
  - references
  - ingredients[19].mediaingredientmech_term
  - ingredients[1].mediaingredientmech_chebi_term
  - ingredients[14].mediaingredientmech_chebi_term
  evidence_ids:
  - grounding
  - chebi15428
  - chebi46756
  - chebi16810
  - chebi31345
  - chebi176843
  rule_id: review-yaml-record/claim-evidence-and-secondary-lineage
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Reconstruct the exact nested stock and basal stages in maintained input,
    preserving source batch amounts/units and every addition. Keep explicit basal
    and Mixed-solution make-up volumes distinct from mere solvent inputs; do not infer
    final-medium rates from listed water or stock labels.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007698
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
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
  description: Preserve the old provider evidence and explicitly resolve the 11 versus
    30 ml source conflict using the original preparation before canonical reuse. Restore
    all four nested additions, their exact definitions and stage-scoped evidence;
    retire the placeholder only when the structure is complete.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007698
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5182_Mixed_solution.yaml
    role: exact linked Mixed solution 5182 dependency; only this stock
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Represent each exact preparation stage and control, including stock-only
    reagent strengths/pH, with root evidence scoped to its field. Preserve the source-specific
    40 min instruction rather than substituting a generic default.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007698
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
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
  description: After repairing the maintained formulation, regenerate and verify retention
    of these six existing correct owner groundings. Preserve all prior history and
    append verified context with the actual correction date; do not rewrite historical
    events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007698
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Attach claim-level evidence to retained as well as corrected amounts
    and stages. Reconcile current secondary links using exact authorities; preserve
    generic or unresolved source chemical scope instead of forcing an unsupported
    precise form. Do not treat current MIM absence as proof of historical error.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007698
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1173_CTM_Medium.yaml
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
- The primary explicitly makes basal medium to 1 L and Mixed solution to 30 ml; other
  listed water amounts and the eventual combined-medium volume are not independent
  final-volume measurements.
- The provider publishes different normalization bases, including 28 ml for the main
  source and 11 ml for Mixed solution; these do not override the exact primary preparation.
- No organism-specific growth evidence is inferred. Same-name CultureMech:002279 historical
  reports are comparison-only and do not authorize owner or formulation transfer.
- Exact current raw/digest agreement authenticates the scoped historical snippets,
  not past retrieval time or code execution. Generic oxoglutarate, calcium-pantothenate
  and B12 supplied forms retain their documented uncertainty.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
