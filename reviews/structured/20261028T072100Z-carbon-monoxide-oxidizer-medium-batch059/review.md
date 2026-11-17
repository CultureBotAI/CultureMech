# Scientific review of carbon_monoxide_oxidizer_medium

- Review: 20261028T072100Z-carbon-monoxide-oxidizer-medium-batch059
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:48:48.662990Z
- Finished UTC: 2026-10-28T07:21:00.152578Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSM base identity and main amounts are supported, including its explicit 1 L final basis. The family remains scientifically incomplete: flattened SL-6, omitted branch prescriptions, two hydrate mismatches and stale generated topology need source-specific curation. Correct owner topology and retained base preparation receive explicit credit.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch059 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000797 | data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml | generated | carbon_monoxide_oxidizer_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000797 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:000797 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:000797 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:000797 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### DSM base and unresolved KOMODO equivalence

identity: concern. Targets: CultureMech:000797.

The DSM 133 base identity is supported. The ten maintained owners are exact source records, but nine current KOMODO pages returned HTTP 403. Copied DSM chemistry, old catalogue excerpts and shared signatures do not authenticate all current KOMODO recipes. Source strain prescriptions are kept separate; no organism taxonomy or experimental growth result is inferred.

### Historical report authentication

evidence: concern. Targets: CultureMech:000797.

All 22 exact reports were read through losslessly pooled duplicate lines. The ten October curation reports cite the same current API payload where hashes match, with every quoted object independently joined; their broad conflict labels do not override supported DSM basal amounts. The separate KOMODO catalogue digest and historical execution remain unauthenticated. September standalone-stock assertions were not transferred as current owner facts.

### Current writer and generated freshness

provenance: concern. Targets: CultureMech:000797.

The topology writer verifies a hardcoded flattened signature, promotes the correct base root and separates six strain labels, but does not restore their supplements. Its _upsert_event replacement semantics should not be used to rewrite old provenance. Current MediaDive separates stock references, and current merging retains scientific fields and rejects incompatible formulas. These present behaviors do not explain historical execution by themselves.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:000797.

All 165 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:000797", "selected_concentration_field_count": 165, "selected_concentration_fields_covered": 165, "decisions": [{"decision_id": "q1", "subject": "Na2HPO4 x 12 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 4.5 g gives the represented 4.5 g/L. The exact DSM base and generated representative match that DSM value. Retain the amount, with supplied-form grounding assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\": 95,\n                        \"amount\": 4.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.5,\n                        \"mmol_l\": 31.6993,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Na2HPO4 x 12 H2O                                           4.50    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Na2HPO4 x 12 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 4.5 g gives the represented 4.5 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO pages returned HTTP 403; matching copied DSM values do not independently authenticate each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\": 95,\n                        \"amount\": 4.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.5,\n                        \"mmol_l\": 31.6993,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Na2HPO4 x 12 H2O                                           4.50    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 0.75 g gives the represented 0.75 g/L. The exact DSM base and generated representative match that DSM value. Retain the amount, with supplied-form grounding assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.75,\n                        \"mmol_l\": 5.51122,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "KH2PO4                                                     0.75    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "KH2PO4", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 0.75 g gives the represented 0.75 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO pages returned HTTP 403; matching copied DSM values do not independently authenticate each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.75,\n                        \"mmol_l\": 5.51122,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "KH2PO4                                                     0.75    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 1.5 g gives the represented 1.5 g/L. The exact DSM base and generated representative match that DSM value. Retain the amount, with supplied-form grounding assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 28.0426,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "NH4Cl                                                      1.50    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "NH4Cl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 1.5 g gives the represented 1.5 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO pages returned HTTP 403; matching copied DSM values do not independently authenticate each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 28.0426,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "NH4Cl                                                      1.50    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 0.2 g gives the represented 0.2 g/L. The exact DSM base and generated representative match that DSM value. Retain the amount, with supplied-form grounding assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "MgSO4 x 7 H2O                                              0.20    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 0.2 g gives the represented 0.2 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO pages returned HTTP 403; matching copied DSM values do not independently authenticate each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "MgSO4 x 7 H2O                                              0.20    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 0.03 g gives the represented 0.03 g/L. The exact DSM base and generated representative match that DSM value. Retain the amount, with supplied-form grounding assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.204061,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CaCl2 x 2 H2O                                              0.03    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 0.03 g gives the represented 0.03 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO pages returned HTTP 403; matching copied DSM values do not independently authenticate each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.204061,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CaCl2 x 2 H2O                                              0.03    g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Ferric ammonium citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 18 mg gives the represented 0.018 g/L. The exact DSM base and generated representative match that DSM value. Retain the amount, with supplied-form grounding assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Ferric ammonium citrate\",\n                        \"compound_id\": 97,\n                        \"amount\": 18,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\": 0.0687075,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Ferric ammonium citrate                                   18.00   mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Ferric ammonium citrate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation": "DSM 133 explicitly states Final volume 1000 ml; 18 mg gives the represented 0.018 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO pages returned HTTP 403; matching copied DSM values do not independently authenticate each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Ferric ammonium citrate\",\n                        \"compound_id\": 97,\n                        \"amount\": 18,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\": 0.0687075,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Ferric ammonium citrate                                   18.00   mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Optional sodium acetate, DSM base", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "base and chemoorganotrophic option", "interpretation": "The base lists optional 3 g, and step 3 specifies 3 g for chemoorganotrophic growth under air. Preserve the optional qualifier and do not add the same 3 g twice.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"optional\": 1\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\": \"For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "Acetate in DSM 13294-labelled owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "specific strain branches", "interpretation": "The exact DSM 133 prescription for DSM 13294 says omit acetate. These two explicitly named owners nevertheless retain the copied 3 G_PER_L optional acetate. This contradiction applies to these two owners only; current KOMODO page equivalence remains unresolved.", "sources": [{"locator": "extracted-text lines 32-32", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294: Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "Acetate in the other seven KOMODO owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "unresolved source branch", "interpretation": "The copied 3 G_PER_L agrees with the DSM base optional amount, but does not establish each unavailable KOMODO recipe. No universal acetate-omission claim is made for these seven owners.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"optional\": 1\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\": \"For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "Optional agar", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "solid-medium option", "interpretation": "12 g on the explicit 1 L DSM base is supported only for the solid option. Retain optionality; SOLID_AGAR is not a complete representation of the liquid and solid family. Unavailable KOMODO formulations remain unauthenticated.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\": \"\",\n                        \"amount\": 12,\n                        \"unit\": \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\": 35.6792,\n                        \"optional\": 1\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Agar, for solid medium (optional)                         12.00    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "Optional agar", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "solid-medium option", "interpretation": "12 g on the explicit 1 L DSM base is supported only for the solid option. Retain optionality; SOLID_AGAR is not a complete representation of the liquid and solid family. Unavailable KOMODO formulations remain unauthenticated.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\": \"\",\n                        \"amount\": 12,\n                        \"unit\": \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\": 35.6792,\n                        \"optional\": 1\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Agar, for solid medium (optional)                         12.00    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q18", "subject": "ZnSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.1 g belongs to the separate SL-6 stock; API explicitly declares 0.1 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 0.0001 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 40-40", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "ZnSO4 x 7 H2O                                              0.10    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.03 g belongs to the separate SL-6 stock; API explicitly declares 0.03 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 3e-05 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 41-41", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "MnCl2 x 4 H2O                                              0.03    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q20", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.3 g belongs to the separate SL-6 stock; API explicitly declares 0.3 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 0.0003 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 42-42", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "H3BO3                                                      0.30    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q21", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.2 g belongs to the separate SL-6 stock; API explicitly declares 0.2 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 0.0002 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 43-43", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CoCl2 x 6 H2O                                              0.20    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q22", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.01 g belongs to the separate SL-6 stock; API explicitly declares 0.01 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 1e-05 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 44-44", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CuCl2 x 2 H2O                                              0.01    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.02 g belongs to the separate SL-6 stock; API explicitly declares 0.02 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 2e-05 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 45-45", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "NiCl2 x 6 H2O                                              0.02    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium", "interpretation": "0.03 g belongs to the separate SL-6 stock; API explicitly declares 0.03 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base. Using that declared stock strength yields 3e-05 g/L in the DSM base, not the stored stock-strength value as a direct ingredient. Prefer a nested stock plus dose. This calculation is not independent authentication of unavailable KOMODO branches.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 46-46", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Na2MoO4 x 2 H2O                                            0.03    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q25", "subject": "Main water and explicit final volume", "local_fields": [], "decision": "evidence_only", "stage": "DSM basal solvent and denominator", "interpretation": "Source lists 1000 ml water and explicitly states final volume 1000 ml. Retain both source claims without treating the sum of water and later additions as a separately measured total.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q26", "subject": "SL-6 receiving dose", "local_fields": [], "decision": "evidence_only", "stage": "separate stock addition", "interpretation": "The missing 1 ml stock addition belongs to the DSM 1 L base. It is not seven direct stock-strength ingredient additions.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "SL-6 water", "local_fields": [], "decision": "evidence_only", "stage": "stock solvent", "interpretation": "The stock lists 1000 ml distilled water. API separately declares stock rates; do not infer a measured final stock volume solely from the water input.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 55-55", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Distilled water                     1000.00   ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q28", "subject": "pH", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml", "field_path": "ph_value", "original": 7.0}], "decision": "evidence_only", "stage": "DSM source control", "interpretation": "All selected layers retain 7.0, matching DSM 133. This source correspondence does not independently verify unavailable KOMODO pages.", "sources": [{"locator": "extracted-text lines 3-3", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final pH: 7.0", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients, adjust pH to 7.0 and autoclave.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Dissolve, adjust pH and autoclave", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients, adjust pH to 7.0 and autoclave."}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients, adjust pH to 7.0 and autoclave."}], "decision": "evidence_only", "stage": "base preparation", "interpretation": "The target and DSM owner retain the source sequence; nine KOMODO owners omit it. No unprovided autoclave duration or temperature is invented.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients, adjust pH to 7.0 and autoclave.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "Chemoautotrophic gas options and bicarbonate", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "For chemoautotrophic growth incubate under a gas atmosphere of a) 20 - 80% carbon monoxide + 10% O2 + 70 - 10% N2 or b) 70% H2 + 20% O2 + 10% CO2 adding 2.50 g NaHCO3 per liter of medium."}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "preparation_steps[1].description", "original": "For chemoautotrophic growth incubate under a gas atmosphere of a) 20 - 80% carbon monoxide + 10% O2 + 70 - 10% N2 or b) 70% H2 + 20% O2 + 10% CO2 adding 2.50 g NaHCO3 per liter of medium."}], "decision": "evidence_only", "stage": "conditional source preparation", "interpretation": "Preserve option a 20–80% CO with 10% O2 and complementary 70–10% N2, or option b 70% H2/20% O2/10% CO2 with 2.50 g/L NaHCO3. The coupled ranges are not independent settings. The target/DSM owner retain this text; no gas pressure or temperature is added.", "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\": \"For chemoautotrophic growth incubate under a gas atmosphere of a) 20 - 80% carbon monoxide + 10% O2 + 70 - 10% N2 or b) 70% H2 + 20% O2 + 10% CO2 adding 2.50 g NaHCO3 per liter of medium.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "Chemoorganotrophic acetate and air", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air atmosphere."}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path": "preparation_steps[2].description", "original": "For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air atmosphere."}], "decision": "evidence_only", "stage": "conditional source preparation", "interpretation": "The retained 3 g acetate under air is the conditional base amount, not an additional 3 g on top of the optional row. Exact strain exceptions remain separate.", "sources": [{"locator": "$.data.solutions[0].steps[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\": \"For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "DSM 1083 vitamin dose and filtration", "local_fields": [], "decision": "evidence_only", "stage": "DSM 1083 branches only", "interpretation": "The source prescribes 10 ml/L of the vitamin solution from 141, filter-sterilized. Transfer only the named vitamin stock; do not import medium 141 basal chemistry, mineral stock, pH, gases or strain prescriptions.", "sources": [{"locator": "extracted-text lines 26-28", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1083: The medium has to be supplemented with 10.00 ml/l of the vitamin solution\nof medium 141, sterilized by filtration. For chemoorganotrophic growth with acetate under\nair add also 10.00 ml/l of a 5% w/v NaHCO3 solution, sterilized by filtration.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q33", "subject": "DSM 1083 organotrophic bicarbonate", "local_fields": [], "decision": "evidence_only", "stage": "DSM 1083 organotrophic branch only", "interpretation": "10 ml/L of 5% w/v NaHCO3, filter-sterilized, is explicitly prescribed under acetate/air conditions. This supplies 0.5 g per stated litre by 0.05 g/ml × 10 ml; it is distinct from the base H2/CO2 option.", "sources": [{"locator": "extracted-text lines 26-28", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1083: The medium has to be supplemented with 10.00 ml/l of the vitamin solution\nof medium 141, sterilized by filtration. For chemoorganotrophic growth with acetate under\nair add also 10.00 ml/l of a 5% w/v NaHCO3 solution, sterilized by filtration.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q34", "subject": "DSM 1085 seven-vitamin dose", "local_fields": [], "decision": "evidence_only", "stage": "DSM 1085 branches only", "interpretation": "1 ml/L of the seven-vitamin solution from 503 is prescribed. Do not substitute the ten-component Wolin stock or transfer the rest of medium 503.", "sources": [{"locator": "extracted-text lines 29-31", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1085: The medium has to be supplemented with 1 ml/l Seven Vitamins Solution\n(see medium 503). For chemoorganotrophic growth with acetate under air, add also 20.00\nml/l of a 5% w/v NaHCO3 solution, sterilized by filtration.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q35", "subject": "DSM 1085 organotrophic bicarbonate", "local_fields": [], "decision": "evidence_only", "stage": "DSM 1085 organotrophic branch only", "interpretation": "20 ml/L of 5% w/v NaHCO3, filter-sterilized, supplies 1 g per stated litre. Preserve the exact branch and do not collapse this dose with the DSM 1083 dose.", "sources": [{"locator": "extracted-text lines 29-31", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1085: The medium has to be supplemented with 1 ml/l Seven Vitamins Solution\n(see medium 503). For chemoorganotrophic growth with acetate under air, add also 20.00\nml/l of a 5% w/v NaHCO3 solution, sterilized by filtration.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q36", "subject": "DSM 13294 seven vitamins and acetate omission", "local_fields": [], "decision": "evidence_only", "stage": "DSM 13294 branches only", "interpretation": "Omit acetate and add 1 ml/L of seven vitamins from 503. These are named source prescriptions, not new experimental growth evidence.", "sources": [{"locator": "extracted-text lines 32-34", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294: Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution\n(see medium 503). For chemoorganotrophic growth under air, add also 2.00 g/l Na\n-pyruvate and 1.00 g/l yeast extract.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject": "DSM 13294 organotrophic pyruvate", "local_fields": [], "decision": "evidence_only", "stage": "DSM 13294 organotrophic branch only", "interpretation": "The source explicitly adds 2 g/L sodium pyruvate under air; this missing conditional ingredient does not apply to the entire family.", "sources": [{"locator": "extracted-text lines 32-34", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294: Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution\n(see medium 503). For chemoorganotrophic growth under air, add also 2.00 g/l Na\n-pyruvate and 1.00 g/l yeast extract.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q38", "subject": "DSM 13294 organotrophic yeast extract", "local_fields": [], "decision": "evidence_only", "stage": "DSM 13294 organotrophic branch only", "interpretation": "The source explicitly adds 1 g/L yeast extract under air; retain complex-component identity and branch scope.", "sources": [{"locator": "extracted-text lines 32-34", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294: Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution\n(see medium 503). For chemoorganotrophic growth under air, add also 2.00 g/l Na\n-pyruvate and 1.00 g/l yeast extract.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q39", "subject": "Biotin", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 94-94", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Biotin                                                     2.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q40", "subject": "Folic acid", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 95-95", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Folic acid                                                 2.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q41", "subject": "Pyridoxine hydrochloride", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 96-96", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Pyridoxine hydrochloride                                  10.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q42", "subject": "Thiamine HCl", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 97-97", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Thiamine HCl                                               5.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q43", "subject": "Riboflavin", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 98-98", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Riboflavin                                                 5.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q44", "subject": "Nicotinic acid", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 106-106", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Nicotinic acid                       5.00   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q45", "subject": "Calcium D-(+)-pantothenate", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 107-107", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Calcium D-(+)-pantothenate           5.00   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q46", "subject": "Vitamin B12", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 108-108", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Vitamin B12                          0.10   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q47", "subject": "p-Aminobenzoic acid", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 109-109", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "p-Aminobenzoic acid                  5.00   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q48", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 110-110", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "(DL)-alpha-Lipoic acid               5.00   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q49", "subject": "Distilled water", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The 1000 ml is stock solvent, not proof of a measured final stock volume. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 111-111", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Distilled water                   1000.00   ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q50", "subject": "Vitamin B12", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 177-177", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Vitamin B12                                              100.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q51", "subject": "p-Aminobenzoic acid", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 178-178", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "p-Aminobenzoic acid                                       80.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q52", "subject": "D-(+)-biotin", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 179-179", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "D-(+)-biotin                                              20.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q53", "subject": "Nicotinic acid", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 180-180", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Nicotinic acid                                           200.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q54", "subject": "Calcium pantothenate", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 181-181", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Calcium pantothenate                                     100.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q55", "subject": "Pyridoxine hydrochloride", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 182-182", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Pyridoxine hydrochloride                                 300.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q56", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The amount is a stock-preparation mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 183-183", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Thiamine-HCl x 2 H2O                                     200.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q57", "subject": "Distilled water", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock preparation only", "interpretation": "Retain the literal supplied form and batch amount from this exact stock table. The 1000 ml is stock solvent, not proof of a measured final stock volume. DSM 133 supplies the branch-specific receiving dose; unrelated parent-medium composition and conditions do not transfer.", "sources": [{"locator": "extracted-text lines 184-184", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch059/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:000797.

data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1083.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1085.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_13294.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml: primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml: primary 15/15, secondary 15/15. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:000797.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:000797.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Seven stock components are represented as direct medium concentrations

major / open / confirmed; issue key: culturemech-000797-flattened-sl6-and-missing-dose.

All 11 selected documents flatten SL-6 into direct ingredients at stock strength and omit its1 ml receiving dose. Current API declares the stock rates; the current DSM PDF explicitly declares the base final volume 1000 ml. Correct main basal amounts are retained, while the stock stage and solvent must be represented separately.

### f2: The generated family collapses distinct source prescriptions

major / open / confirmed; issue key: culturemech-000797-source-branches-and-stale-generated-topology.

DSM 133 distinguishes chemoautotrophic and organotrophic options and DSM 1083/1085/13294 supplements. The six strain owners retain correct variant labels after a partial topology repair, but all nine KOMODO owners still contain the same copied 15 ingredients and no preparation. Only the two DSM 13294-labelled owners contradict the explicit acetate omission. The generated target still uses the old DSM 1083 source-duplicate parent instead of the repaired family root. Current conservative merge code rejects incompatible scientific projections; old generated content and copied signatures do not prove recipe equivalence.

### f3: Two asserted IDs omit the source hydrates

major / open / confirmed; issue key: culturemech-000797-phosphate-and-nickel-hydrates.

Na2HPO4·12H2O uses CHEBI:34683 with formula HO4P.2Na, and NiCl2·6H2O uses CHEBI:34887 with formula Cl2Ni, in both primary and secondary slots. Current CHEBI:53542 explicitly represents nickel chloride hexahydrate. Correct cobalt, copper, magnesium, calcium, zinc, manganese and molybdate hydrate mappings are credited. Ferric ammonium citrate and agar are mixtures; their API mmol_l is not endorsed.

### f4: Source-specific preparation and claim evidence are incomplete

major / open / confirmed; issue key: culturemech-000797-missing-branch-preparation-and-evidence.

Target and DSM owner retain the three base preparation paragraphs, but nine KOMODO owners omit preparation and retain Aerobic: No despite the DSM source air/oxygen-containing options. Missing water, branch vitamins, bicarbonate, pyruvate and yeast-extract stages require scoped representation. No claim-level source evidence is attached. SOLID_AGAR represents only the optional agar branch.

### f5: Historical timestamps and curation flags need qualified context

minor / open / confirmed; issue key: culturemech-000797-historical-time-and-curation-claims.

KOMODO imported events literally end in .fZ and subsequent copied-DSM events lack timezone. The topology writer uses a fixed historical timestamp and _upsert_event replaces matching events. Existing ingredients_curated flags and exact-match prose do not certify source-specific chemistry. Current code is not proof of historical execution.

## Recommended Actions And Acceptance Checks

### action1

Restore the exact SL-6 stock and receiving dose in the maintained source-specific recipes, preserving compound forms and absolute water inputs. Link only an independently checked stock representation; this review did not assess a standalone solution25 owner. Attach root evidence scoped to each stock-dose field.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve the valid DSM 133 identity and the useful current family-root/strain-variant repair. Review each exact branch against its source, retain unresolved KOMODO equivalence honestly, represent missing branch supplements and regenerate after maintained-owner repair. Review the inspected topology writer hardcoded stock signature and duplicate assertions; do not reuse copied amounts as equivalence proof.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the exact supplied hydrate mappings, or retain precise source labels with unresolved linkage. Preserve supported masses and reject anhydrous-mass molarity shortcuts. Verify any newly proposed secondary linkage independently.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Preserve the supported base instructions and distinguish each source branch, including exact filtration, gas and supplement conditions. Attach root evidence with precise field/stage scope; no new PreparationStep or SolutionDescriptor evidence slot is proposed. Do not transfer medium 141 or503 whole recipes or interpret collection prescriptions as measured growth.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Preserve every original event and its bytes. Correct future writer timestamp generation and append a new verified context/correction event with the actual curation date; do not rewrite historical timestamps or infer missing times. Retain partial topology credit while qualifying scientific-completion flags.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local4 | data/normalized_yaml/bacterial/for_dsm_1083.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local5 | data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local6 | data/normalized_yaml/bacterial/for_dsm_1085.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local7 | data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local8 | data/normalized_yaml/bacterial/for_dsm_13294.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local9 | data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local10 | data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch059/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch059/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch059/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch059/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz133 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api133 | https://mediadive.dsmz.de/rest/medium/133; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| dsmz141 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| dsmz503 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| komodo133 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.1 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.1; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.2 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.2; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.3 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.3; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.4 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.4; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.5 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.5; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.6 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.6; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.7 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.7; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| komodo133.8 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.8; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. The exact historical hyperlink was attempted separately and is retained as distinct evidence. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31604 = ferric ammonium citrate; definition ['A mixture of indefinite composition that contains ferric and ammonium cations and citrate(3−) anions, ferric ammonium citrate may be obtained as red crystals or a brownish yellow powder or as green crystals or powder. It is added to foods as an acidity regulator and anticaking agent. It is also used as a positive oral contrast agent in magnetic resonance imaging, and was formerly administered orally as a source of iron for the treatment of iron-deficiency anaemia.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn']; mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32954 = sodium acetate; definition []; formula ['C2H3O2.Na']; mass ['82.034']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34683 = disodium hydrogenphosphate; definition []; formula ['HO4P.2Na']; mass ['141.958']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state), chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch059/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T034420Z-CARBON_MONOXIDE_OXIDIZER_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/carbon_monoxide_oxidizer_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1085.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history3 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history4 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_chemoorganotrophic_growth.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history5 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_for_carbon_monoxide_oxidizers.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history6 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_chemoautotrophic_growth.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history7 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1083.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history8 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history9 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_13294.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history10 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api133 raw bytes exactly match the cited historical SHA, and 21 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history11 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_13294.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history12 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history13 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_chemoautotrophic_growth.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history14 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1083.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history15 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history16 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1085.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history17 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_chemoorganotrophic_growth.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history21 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch059/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer68 | scripts/repair_komodo_133_carbon_monoxide_topology_score10.py; relevant functions named in summary | context_only | Full repair_parent/repair_child and _require_carbon_monoxide_record read: exact source IDs and a hardcoded flattened ingredient signature gate topology changes. Six strain variants and the base root are distinguished, but copied chemistry and exact-match prose remain unverified. _upsert_event replaces matching historical events; future corrections must retain originals and append verified current context. |
| writer69 | scripts/resolve_komodo_compositions.py; relevant functions named in summary | context_only | Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents copied ingredients/solutions but does not independently authenticate a particular past execution or variant. The underlying implementation was not an inspected input. |
| writer70 | src/culturemech/import/komodo_web_importer.py; relevant functions named in summary | context_only | Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes and initially empty ingredients for later DSMZ enrichment; its strftime format uses literal %f. Read code does not authenticate the past table values or source-copy execution. |
| writer71 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition restricts direct ingredients to primary recipe, skips stock additions and water, and prefers provider g_l; _parse_api_solutions preserves referenced/percent stocks. This limits the old flattening attribution; water needs preparation-volume representation and historical run provenance remains separate. |
| writer72 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer73 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer74 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch059/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |
| komodo-exact-1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.1; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-2 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.2; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-3 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.3; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-4 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.4; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-5 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.5; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-6 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.6; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-7 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.7; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-8 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.8; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-exact-9 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133; Complete failed HTTP response; exact historical discovery URL, report path/hash and line are in the separate route result. | unknown | The exact historical catalogue hyperlink was attempted once and returned HTTP 403. This does not authenticate current formulation, recipe equivalence, historical catalogue bytes or past access time. Earlier prefix-only route failures remain preserved separately. |
| komodo-catalogue-current | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Complete current failed MediaList response; exact reuse metadata pinned in the separate route result. | unknown | Root captured this exact historical catalogue endpoint once; current HTTP403 is reused with its original time and bytes. It does not authenticate the historical d825 catalogue digest. |
| exact-route-attempts | REVIEW_WORK/batch059/record06-exact-routes-20261028T072000Z/result.json; outcomes; exact_catalogue_current_reuse; request-plan.json contains report line/hash discovery | context_only | Nine exact historical MediaInfo hyperlinks captured once each, all403; separate current MediaList403 reuse. Original nine prefix-only failures are unchanged. These negative results preserve the existing partial scope and do not change any quantity or scientific formulation decision. |

## Limits And Additional Notes

- Nine exact historical /komodo/servlet MediaInfo hyperlinks and the exact MediaList endpoint returned HTTP 403. Original prefix-only route failures are preserved separately. Current recipe equivalence and historical catalogue bytes remain unresolved; this is a partial scientific review, not full family authentication.
- Only the Wolin vitamin table from 141 and seven-vitamin table from 503 transfer. Their whole parent media, unrelated stocks, conditions and strain examples remain excluded.
- Vitamin stock water is not inferred to be a measured final volume. SL-6 numerical dilution is explicitly based on provider-declared stock g_l and the DSM base final-volume statement.
- No standalone solution25 owner was assessed or automatically recommended for reuse. No source-derived organism taxonomy or experimental growth claim is added.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T072100Z-carbon-monoxide-oxidizer-medium-batch059
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of carbon_monoxide_oxidizer_medium
started_at: '2026-10-28T06:48:48.662990Z'
finished_at: '2026-10-28T07:21:00.152578Z'
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
summary: 'The DSM base identity and main amounts are supported, including its explicit
  1 L final basis. The family remains scientifically incomplete: flattened SL-6, omitted
  branch prescriptions, two hydrate mismatches and stale generated topology need source-specific
  curation. Correct owner topology and retained base preparation receive explicit
  credit.'
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
  - path: data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
    sha256: 72c0a7e752fba2c6d6bbc4bbc0be0f7ce37d6d78624c88b7e72570b19faced07
    role: target
  - path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    sha256: 957075c9fcec05b16285477ed39caa763aa6d63c96515e9f85f64b20e01e15d2
    role: context
  - path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    sha256: db7816160fbb8e32e426b466111fb47f721d8ce894c130ceb0f803dd162a1af4
    role: context
  - path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    sha256: e591df04fab52be458809095615bb3cd97479cec1e82992fe8755c553d672ee8
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    sha256: 14af6fca522d595fccf993b935a851a13179d03563418520a2bc2271aa73cce6
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    sha256: 1b4d284722ce4fd5f7c4acce5b47797e03a8efecca2df340d3017405e703485a
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    sha256: 068de1720d2cf4fddfb38ec76f626020b363175290e5a50b292d90e089728ac5
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    sha256: 47010d7f5ef864f7e86b0aff7eed3db39dfade108751468d096c5c223fcc3206
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    sha256: 687b726698253b68c8561649eb968f92b172afea009256a189229997e5bbdbc6
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    sha256: 6834998ea3c6875d9e650d6ff6cba763f9dc5d0572b077e2ac7170e31b24d0de
    role: context
  - path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    sha256: dc957caf301b7cc883d91f9fa689f70d8a59a1087844c6cbd7d88b399462d3da
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_chemoautotrophic_growth.yaml.md
    sha256: 3769c4adaec89fd26b4c69a67db6d9c3ec6336a7872b0b1c7219bd23777cef4d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_chemoorganotrophic_growth.yaml.md
    sha256: 3174359c6c3e5d72712a3be8c120d02a23cf361898959b5cbacfe9a806bda6ff
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1083.yaml.md
    sha256: be125d2e8b1716d4d7b71629ecd9e9974304c2754217c5ac505f775ffc464d81
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml.md
    sha256: 8ee0fad2cbf23ecdec0ef2f34e4c3c3433eba3938035744afed4fa7ac9c006df
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1085.yaml.md
    sha256: 735d37cb2768c7dd8504aae2d03c9a87e4aa80345aa4a656dab6cba720b491b3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml.md
    sha256: 0215c4dfd720e75eeec952d46c29ef4cd4951cfbeaffc361c183b95336bbe1fc
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_13294.yaml.md
    sha256: 6440ba27acab103f766a73bb6423b7d6c3e8f5bd75228e0b4b3ae3b25f7b9ddf
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml.md
    sha256: d69f5f5b92060baa1bd6684964270b81e59544b1cf15dd2a04bd9ba5800caa2f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_for_carbon_monoxide_oxidizers.yaml.md
    sha256: f01ecc818222f64e6c853e0c8a93fe45b9230b9d21e287eec3c1b48eb1f95ec2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/carbon_monoxide_oxidizer_medium.yaml.md
    sha256: 0a54c1665b61618b15d7e9c9f9321d263e2b6f06957059a7e9e5c1b16c843394
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.md
    sha256: 99db62010c7c1d1924a3a4ca42a55d1c9d4e3b018752dd337e19911aff4518ef
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.md
    sha256: a1866726750482cb37067f4700fa3a6098840f7cd78b97ec33e713ce2b568533
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_chemoautotrophic_growth.md
    sha256: 2bd472409c8bc0c95f0e06ff2a4c500eb0bb71c91c6e55c0d95b853532ab17ca
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_chemoorganotrophic_growth.md
    sha256: 6b3cdf6e464dce567cab295758384009e60a53a20d11aaaa876a0d4bb5d32a8b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1083.md
    sha256: 36094d22b78a88b3bd0fa32fc123e959db5c80c7d019b24a0b721de3551085c6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.md
    sha256: 9d4de49a61a585edb21cba73051ace1eb019a972fcb7b33845c43de6a303f296
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1085.md
    sha256: c9e813dd02f6e24b35db13f98cbe91ad018e798f3ceff72846f11b09692cad70
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.md
    sha256: dc7ee110c3d4034af316a62c0e5f6a5ed581454a98727d9d08005a23080f291a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_13294.md
    sha256: f9bacf314bb31b7a9fe8f76775411162ff399b3398813d050cc7508f0aaf3d93
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.md
    sha256: 0dc2004fb050be2285738820afac1ded444e2aa05402b29b3ca673542ef43150
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.md
    sha256: 6683d44592e6779fb3a4d12183f313073e3aea113ed2e4e4658172a5b1d2674f
    role: context
  - path: reports/yaml_record_review/20260922T034420Z-CARBON_MONOXIDE_OXIDIZER_MEDIUM.md
    sha256: a42cd6790fb88891c964f8033d33fe2b29d32001ba7816dce6cee654ef59062f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/repair_komodo_133_carbon_monoxide_topology_score10.py
    sha256: d3a88e8e513576cc43c64654c4118283527898e2c0c92efb0706a671833a42d9
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  selection: Authoritative batch059 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000797
targets:
- target_id: CultureMech:000797
  path: data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
  label: carbon_monoxide_oxidizer_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000797
  command: just validate-schema data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000797
  command: just validate-strict data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch059/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000797
  command: just validate-terms data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:000797
  command: just validate-references data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334000Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 72c0a7e752fba2c6d6bbc4bbc0be0f7ce37d6d78624c88b7e72570b19faced07
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334153Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 957075c9fcec05b16285477ed39caa763aa6d63c96515e9f85f64b20e01e15d2
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334176Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: db7816160fbb8e32e426b466111fb47f721d8ce894c130ceb0f803dd162a1af4
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334201Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: e591df04fab52be458809095615bb3cd97479cec1e82992fe8755c553d672ee8
- evidence_id: local4
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_1083.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334223Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 14af6fca522d595fccf993b935a851a13179d03563418520a2bc2271aa73cce6
- evidence_id: local5
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334244Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 1b4d284722ce4fd5f7c4acce5b47797e03a8efecca2df340d3017405e703485a
- evidence_id: local6
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_1085.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334265Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 068de1720d2cf4fddfb38ec76f626020b363175290e5a50b292d90e089728ac5
- evidence_id: local7
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334286Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 47010d7f5ef864f7e86b0aff7eed3db39dfade108751468d096c5c223fcc3206
- evidence_id: local8
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_13294.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334309Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 687b726698253b68c8561649eb968f92b172afea009256a189229997e5bbdbc6
- evidence_id: local9
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334331Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 6834998ea3c6875d9e650d6ff6cba763f9dc5d0572b077e2ac7170e31b24d0de
- evidence_id: local10
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:02:54.334354Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: dc957caf301b7cc883d91f9fa689f70d8a59a1087844c6cbd7d88b399462d3da
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:49.755138Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: d6cbaf34d0227dc18c3937e1ce7136bc5fb2a656186cb41adcee0f197d9c0a21
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:50.689323Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 1c7e6838594dda320c6d6616275426acf27a7a61d72b6e69c2a8c17b55b02aa0
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:51.713377Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: c03013c2c73dcd27b9b5153cc2f3fb5228d4597f6c6a2a6379b80a3de760b44b
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch059/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:52.409847Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 93e05f507ee63a3847dd3a604865900136ec72d160b84c81f028a956ee827dde
- evidence_id: dsmz133
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.743739Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385
- evidence_id: api133
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/133
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.760912Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13
- evidence_id: dsmz141
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.765816Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: dsmz503
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.792164Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa
- evidence_id: komodo133
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.860734Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: d5c99183628cd0e7253d3ec121764c628c7e30c505bef6558b4b6f230cfb77a9
- evidence_id: komodo133.1
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.1
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.922023Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: 1b7d7d5e4771464fc8fd9058ed556fa774b9e7703d5e63f5867cbdc3fdbf8729
- evidence_id: komodo133.2
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.2
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:25.972237Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: 066ea48aee56379179d764390fe168a7ce60bead0f4922223d8e87c7d8bd0749
- evidence_id: komodo133.3
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.3
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:26.031599Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: abbba43377e72cea8cdb84112a4c2e6743466b18bc533e9d4770966caf443a72
- evidence_id: komodo133.4
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.4
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:26.110194Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: 795671efa91d6b4bde3263125cb909e45dc247609e4a17b2980d5538fb27c289
- evidence_id: komodo133.5
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.5
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:26.172941Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: 25a7c5f3c52458b582f5a2e5b75e909e8d5a1a56d75d9cd68941143c8c576585
- evidence_id: komodo133.6
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.6
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:26.185495Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: d2c5269c40d30b76cb5b90b16a68171d3b5e61bda6cf3427c165b53ed9513f02
- evidence_id: komodo133.7
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.7
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:26.235563Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: 3a3d1050aa47c37bc530ef82bba811fb29c6cccf9c2362a8dfc08ecbd75db7a9
- evidence_id: komodo133.8
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.8
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:26.279198Z'
  support: unknown
  summary: 'Initial prefix-only MediaInfo route lead, which omitted the /komodo prefix
    printed in the historical catalogue hyperlink. Actual retrieval HTTP 403, error
    <HTTPError 403: ''Forbidden''>. This response does not authenticate a recipe.
    The exact historical hyperlink was attempted separately and is retained as distinct
    evidence.'
  snapshot_sha256: 19fe1cfb97aceaa4b8e55fe02aa9c938769a455b19dc2ccad65c555b55a597d7
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.289745Z'
  support: supports
  summary: OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of
    polysaccharides extracted from species of red algae. Its two main components are
    agarose and agaropectin. Agarose is the component responsible for the high-strength
    gelling properties of agar, while agaropectin provides the viscous properties.'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.290410Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31604
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.339633Z'
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
  accessed_at: '2026-10-28T06:49:26.772754Z'
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
  accessed_at: '2026-10-28T06:49:26.775513Z'
  support: supports
  summary: OLS current exact CHEBI:32312 = zinc sulfate heptahydrate; definition ['A
    hydrate that is the heptahydrate form of zinc sulfate.']; formula ['7H2O.O4S.Zn'];
    mass ['287.558']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.778560Z'
  support: supports
  summary: OLS current exact CHEBI:32954 = sodium acetate; definition []; formula
    ['C2H3O2.Na']; mass ['82.034']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.870541Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.878169Z'
  support: supports
  summary: OLS current exact CHEBI:34683 = disodium hydrogenphosphate; definition
    []; formula ['HO4P.2Na']; mass ['141.958']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:26.938443Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:27.365054Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:27.384639Z'
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
  accessed_at: '2026-10-28T06:49:27.387482Z'
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
  accessed_at: '2026-10-28T06:49:27.482883Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:27.489961Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:27.546401Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:27.994526Z'
  support: supports
  summary: OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition
    ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state),
    chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass
    ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch059/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T07:02:54.343341Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 09bb7a0139d78999fc098ec6f8909d36253e396d2916af5a42b2b0cb421efa44
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T034420Z-CARBON_MONOXIDE_OXIDIZER_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346679Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: a42cd6790fb88891c964f8033d33fe2b29d32001ba7816dce6cee654ef59062f
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/carbon_monoxide_oxidizer_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346709Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 0a54c1665b61618b15d7e9c9f9321d263e2b6f06957059a7e9e5c1b16c843394
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1085.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346737Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 735d37cb2768c7dd8504aae2d03c9a87e4aa80345aa4a656dab6cba720b491b3
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346763Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 8ee0fad2cbf23ecdec0ef2f34e4c3c3433eba3938035744afed4fa7ac9c006df
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_chemoorganotrophic_growth.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346789Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 3174359c6c3e5d72712a3be8c120d02a23cf361898959b5cbacfe9a806bda6ff
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_for_carbon_monoxide_oxidizers.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346815Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: f01ecc818222f64e6c853e0c8a93fe45b9230b9d21e287eec3c1b48eb1f95ec2
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_chemoautotrophic_growth.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346843Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 3769c4adaec89fd26b4c69a67db6d9c3ec6336a7872b0b1c7219bd23777cef4d
- evidence_id: history7
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1083.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346868Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: be125d2e8b1716d4d7b71629ecd9e9974304c2754217c5ac505f775ffc464d81
- evidence_id: history8
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346896Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: d69f5f5b92060baa1bd6684964270b81e59544b1cf15dd2a04bd9ba5800caa2f
- evidence_id: history9
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_13294.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346925Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 6440ba27acab103f766a73bb6423b7d6c3e8f5bd75228e0b4b3ae3b25f7b9ddf
- evidence_id: history10
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346958Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api133 raw bytes exactly match the cited historical SHA, and 21
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 0215c4dfd720e75eeec952d46c29ef4cd4951cfbeaffc361c183b95336bbe1fc
- evidence_id: history11
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_13294.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346978Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: f9bacf314bb31b7a9fe8f76775411162ff399b3398813d050cc7508f0aaf3d93
- evidence_id: history12
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.346999Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: a1866726750482cb37067f4700fa3a6098840f7cd78b97ec33e713ce2b568533
- evidence_id: history13
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_chemoautotrophic_growth.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347018Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 2bd472409c8bc0c95f0e06ff2a4c500eb0bb71c91c6e55c0d95b853532ab17ca
- evidence_id: history14
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1083.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347037Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 36094d22b78a88b3bd0fa32fc123e959db5c80c7d019b24a0b721de3551085c6
- evidence_id: history15
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347056Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 6683d44592e6779fb3a4d12183f313073e3aea113ed2e4e4658172a5b1d2674f
- evidence_id: history16
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1085.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347075Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: c9e813dd02f6e24b35db13f98cbe91ad018e798f3ceff72846f11b09692cad70
- evidence_id: history17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347093Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 0dc2004fb050be2285738820afac1ded444e2aa05402b29b3ca673542ef43150
- evidence_id: history18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347115Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: dc7ee110c3d4034af316a62c0e5f6a5ed581454a98727d9d08005a23080f291a
- evidence_id: history19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347133Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 9d4de49a61a585edb21cba73051ace1eb019a972fcb7b33845c43de6a303f296
- evidence_id: history20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_chemoorganotrophic_growth.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347151Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 6b3cdf6e464dce567cab295758384009e60a53a20d11aaaa876a0d4bb5d32a8b
- evidence_id: history21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:02:54.347173Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 99db62010c7c1d1924a3a4ca42a55d1c9d4e3b018752dd337e19911aff4518ef
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch059/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T07:02:54.347212Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 3d7dc691985246841d5f85cf5e16e8f8bfdac14af3651c390f006f03c1512fc0
- evidence_id: writer68
  kind: record_content
  reference: scripts/repair_komodo_133_carbon_monoxide_topology_score10.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347238Z'
  support: context_only
  summary: 'Full repair_parent/repair_child and _require_carbon_monoxide_record read:
    exact source IDs and a hardcoded flattened ingredient signature gate topology
    changes. Six strain variants and the base root are distinguished, but copied chemistry
    and exact-match prose remain unverified. _upsert_event replaces matching historical
    events; future corrections must retain originals and append verified current context.'
  snapshot_sha256: d3a88e8e513576cc43c64654c4118283527898e2c0c92efb0706a671833a42d9
- evidence_id: writer69
  kind: record_content
  reference: scripts/resolve_komodo_compositions.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347258Z'
  support: context_only
  summary: 'Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment
    to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents
    copied ingredients/solutions but does not independently authenticate a particular
    past execution or variant. The underlying implementation was not an inspected
    input.'
  snapshot_sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
- evidence_id: writer70
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347280Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes
    and initially empty ingredients for later DSMZ enrichment; its strftime format
    uses literal %f. Read code does not authenticate the past table values or source-copy
    execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer71
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347309Z'
  support: context_only
  summary: Current _parse_api_composition restricts direct ingredients to primary
    recipe, skips stock additions and water, and prefers provider g_l; _parse_api_solutions
    preserves referenced/percent stocks. This limits the old flattening attribution;
    water needs preparation-volume representation and historical run provenance remains
    separate.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer72
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347330Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer73
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347349Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer74
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:02:54.347369Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch059/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T07:02:54.384691Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 45a83a5ae60a0845b5b333011e615d183aae3be2a62c47b43b1906ceceb193a5
- evidence_id: komodo-exact-1
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.1
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:00.970491Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 822bac7395b7aeb5a0b9f122de2f0a3dae7e7f9e4c9bfb689de4361aa976c851
- evidence_id: komodo-exact-2
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.2
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:00.970733Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: a500adf091bb4ed5a849e4327f2b856ecb011355b2682911be3cbd55da230600
- evidence_id: komodo-exact-3
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.3
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:00.970866Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 3d3449169aef365042e09892150d9e5b8e79c61e3409e5ebdec2c4103c6ea327
- evidence_id: komodo-exact-4
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.4
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:00.970977Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 40344bd6287562d910047d58d19c2229209beca009b492a89e6c4a123d824868
- evidence_id: komodo-exact-5
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.5
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:01.040325Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 9d0a822dac93e672c788726e48d128f6fae80d6deb98083ed5c4e5007fdab9e8
- evidence_id: komodo-exact-6
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.6
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:01.065858Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 66f030d6e32bd98b80640aa8873d0ad3b82b51a21179b5501477ca3362cd7305
- evidence_id: komodo-exact-7
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.7
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:01.070492Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 6ff813a7bcf898d4d1768cd0208321cd6d0680eb49e5ee36278a963656a92e9e
- evidence_id: komodo-exact-8
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133.8
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:01.102249Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 2ae0104b32d54e07690c8623af73ee97b9eb9e0c13f8a1f7382e5f9def6ac341
- evidence_id: komodo-exact-9
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=133
  locator: Complete failed HTTP response; exact historical discovery URL, report path/hash
    and line are in the separate route result.
  accessed_at: '2026-10-28T07:20:01.132841Z'
  support: unknown
  summary: The exact historical catalogue hyperlink was attempted once and returned
    HTTP 403. This does not authenticate current formulation, recipe equivalence,
    historical catalogue bytes or past access time. Earlier prefix-only route failures
    remain preserved separately.
  snapshot_sha256: 6ae3f42b838dcb9c94eb8253860b47ce866cce8f9cf3eb6776b53c617a458a5f
- evidence_id: komodo-catalogue-current
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Complete current failed MediaList response; exact reuse metadata pinned
    in the separate route result.
  accessed_at: '2026-10-28T07:08:35.643697Z'
  support: unknown
  summary: Root captured this exact historical catalogue endpoint once; current HTTP403
    is reused with its original time and bytes. It does not authenticate the historical
    d825 catalogue digest.
  snapshot_sha256: dad86ae019c5da0a88b63143ffde0fbfc65248b341be6c798aa9d0d3c25e6bd5
- evidence_id: exact-route-attempts
  kind: record_content
  reference: REVIEW_WORK/batch059/record06-exact-routes-20261028T072000Z/result.json
  locator: outcomes; exact_catalogue_current_reuse; request-plan.json contains report
    line/hash discovery
  accessed_at: '2026-10-28T07:21:00.152578Z'
  support: context_only
  summary: Nine exact historical MediaInfo hyperlinks captured once each, all403;
    separate current MediaList403 reuse. Original nine prefix-only failures are unchanged.
    These negative results preserve the existing partial scope and do not change any
    quantity or scientific formulation decision.
  snapshot_sha256: db9183ec23479cb50a36a1401e84de291790a5dda5c1100b0fef1b9cd84b2343
assessments:
- assessment_id: a1
  area: identity
  topic: DSM base and unresolved KOMODO equivalence
  outcome: concern
  summary: The DSM 133 base identity is supported. The ten maintained owners are exact
    source records, but nine current KOMODO pages returned HTTP 403. Copied DSM chemistry,
    old catalogue excerpts and shared signatures do not authenticate all current KOMODO
    recipes. Source strain prescriptions are kept separate; no organism taxonomy or
    experimental growth result is inferred.
  target_ids:
  - CultureMech:000797
  evidence_ids:
  - dsmz133
  - api133
  - komodo133
  - komodo133.1
  - komodo133.2
  - komodo133.3
  - komodo133.4
  - komodo133.5
  - komodo133.6
  - komodo133.7
  - komodo133.8
- assessment_id: a2
  area: evidence
  topic: Historical report authentication
  outcome: concern
  summary: All 22 exact reports were read through losslessly pooled duplicate lines.
    The ten October curation reports cite the same current API payload where hashes
    match, with every quoted object independently joined; their broad conflict labels
    do not override supported DSM basal amounts. The separate KOMODO catalogue digest
    and historical execution remain unauthenticated. September standalone-stock assertions
    were not transferred as current owner facts.
  target_ids:
  - CultureMech:000797
  evidence_ids:
  - history-auth
  - api133
- assessment_id: a3
  area: provenance
  topic: Current writer and generated freshness
  outcome: concern
  summary: The topology writer verifies a hardcoded flattened signature, promotes
    the correct base root and separates six strain labels, but does not restore their
    supplements. Its _upsert_event replacement semantics should not be used to rewrite
    old provenance. Current MediaDive separates stock references, and current merging
    retains scientific fields and rejects incompatible formulas. These present behaviors
    do not explain historical execution by themselves.
  target_ids:
  - CultureMech:000797
  evidence_ids:
  - local0
  - writer68
  - writer69
  - writer70
  - writer71
  - writer72
  - writer73
  - writer74
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 165 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:000797
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:000797",
    "selected_concentration_field_count": 165, "selected_concentration_fields_covered":
    165, "decisions": [{"decision_id": "q1", "subject": "Na2HPO4 x 12 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 4.5 g gives the represented 4.5
    g/L. The exact DSM base and generated representative match that DSM value. Retain
    the amount, with supplied-form grounding assessed separately.", "sources": [{"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\":
    95,\n                        \"amount\": 4.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.5,\n                        \"mmol_l\":
    31.6993,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Na2HPO4 x
    12 H2O                                           4.50    g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q2", "subject": "Na2HPO4 x 12 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "4.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 4.5 g gives the represented 4.5
    g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO
    pages returned HTTP 403; matching copied DSM values do not independently authenticate
    each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\":
    95,\n                        \"amount\": 4.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.5,\n                        \"mmol_l\":
    31.6993,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Na2HPO4 x
    12 H2O                                           4.50    g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q3", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 0.75 g gives the represented
    0.75 g/L. The exact DSM base and generated representative match that DSM value.
    Retain the amount, with supplied-form grounding assessed separately.", "sources":
    [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api133", "reference":
    "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.75,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.75,\n                        \"mmol_l\":
    5.51122,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "KH2PO4                                                     0.75    g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q4", "subject": "KH2PO4", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.75", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 0.75 g gives the represented
    0.75 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO
    pages returned HTTP 403; matching copied DSM values do not independently authenticate
    each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.75,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.75,\n                        \"mmol_l\":
    5.51122,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "KH2PO4                                                     0.75    g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q5", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 1.5 g gives the represented 1.5
    g/L. The exact DSM base and generated representative match that DSM value. Retain
    the amount, with supplied-form grounding assessed separately.", "sources": [{"locator":
    "$.data.solutions[0].recipe[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    28.0426,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "NH4Cl                                                      1.50    g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q6", "subject": "NH4Cl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 1.5 g gives the represented 1.5
    g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO
    pages returned HTTP 403; matching copied DSM values do not independently authenticate
    each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    28.0426,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "NH4Cl                                                      1.50    g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q7", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 0.2 g gives the represented 0.2
    g/L. The exact DSM base and generated representative match that DSM value. Retain
    the amount, with supplied-form grounding assessed separately.", "sources": [{"locator":
    "$.data.solutions[0].recipe[3]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.811438,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "MgSO4 x 7
    H2O                                              0.20    g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q8", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 0.2 g gives the represented 0.2
    g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO
    pages returned HTTP 403; matching copied DSM values do not independently authenticate
    each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.811438,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "MgSO4 x 7
    H2O                                              0.20    g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q9", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 0.03 g gives the represented
    0.03 g/L. The exact DSM base and generated representative match that DSM value.
    Retain the amount, with supplied-form grounding assessed separately.", "sources":
    [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api133", "reference":
    "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.204061,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CaCl2 x 2
    H2O                                              0.03    g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q10", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 0.03 g gives the represented
    0.03 g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO
    pages returned HTTP 403; matching copied DSM values do not independently authenticate
    each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.204061,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CaCl2 x 2
    H2O                                              0.03    g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "Ferric ammonium citrate", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[5].concentration",
    "original": {"value": "0.018", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 18 mg gives the represented 0.018
    g/L. The exact DSM base and generated representative match that DSM value. Retain
    the amount, with supplied-form grounding assessed separately.", "sources": [{"locator":
    "$.data.solutions[0].recipe[5]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Ferric ammonium citrate\",\n                        \"compound_id\":
    97,\n                        \"amount\": 18,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\":
    0.0687075,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Ferric ammonium
    citrate                                   18.00   mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q12", "subject": "Ferric ammonium citrate", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.018", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.018", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "base-medium amount", "interpretation":
    "DSM 133 explicitly states Final volume 1000 ml; 18 mg gives the represented 0.018
    g/L. These copied KOMODO owner fields match that DSM value. The current KOMODO
    pages returned HTTP 403; matching copied DSM values do not independently authenticate
    each KOMODO formulation or branch.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Ferric ammonium citrate\",\n                        \"compound_id\":
    97,\n                        \"amount\": 18,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\":
    0.0687075,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Ferric ammonium
    citrate                                   18.00   mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "Optional sodium acetate, DSM base", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "base and chemoorganotrophic
    option", "interpretation": "The base lists optional 3 g, and step 3 specifies
    3 g for chemoorganotrophic growth under air. Preserve the optional qualifier and
    do not add the same 3 g twice.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"optional\": 1\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[2]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\":
    \"For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air
    atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q14", "subject": "Acetate in DSM 13294-labelled owners", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "specific strain branches", "interpretation":
    "The exact DSM 133 prescription for DSM 13294 says omit acetate. These two explicitly
    named owners nevertheless retain the copied 3 G_PER_L optional acetate. This contradiction
    applies to these two owners only; current KOMODO page equivalence remains unresolved.",
    "sources": [{"locator": "extracted-text lines 32-32", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294:
    Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q15", "subject": "Acetate in the
    other seven KOMODO owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "unresolved source branch",
    "interpretation": "The copied 3 G_PER_L agrees with the DSM base optional amount,
    but does not establish each unavailable KOMODO recipe. No universal acetate-omission
    claim is made for these seven owners.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"optional\": 1\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[2]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\":
    \"For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air
    atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q16", "subject": "Optional agar", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ingredients[7].concentration",
    "original": {"value": "12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "solid-medium option", "interpretation":
    "12 g on the explicit 1 L DSM base is supported only for the solid option. Retain
    optionality; SOLID_AGAR is not a complete representation of the liquid and solid
    family. Unavailable KOMODO formulations remain unauthenticated.", "sources": [{"locator":
    "$.data.solutions[0].recipe[8]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\":
    \"\",\n                        \"amount\": 12,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\":
    35.6792,\n                        \"optional\": 1\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Agar, for
    solid medium (optional)                         12.00    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q17", "subject": "Optional agar",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "12", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "solid-medium option", "interpretation":
    "12 g on the explicit 1 L DSM base is supported only for the solid option. Retain
    optionality; SOLID_AGAR is not a complete representation of the liquid and solid
    family. Unavailable KOMODO formulations remain unauthenticated.", "sources": [{"locator":
    "$.data.solutions[0].recipe[8]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\":
    \"\",\n                        \"amount\": 12,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 12,\n                        \"mmol_l\":
    35.6792,\n                        \"optional\": 1\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Agar, for
    solid medium (optional)                         12.00    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q18", "subject": "ZnSO4 x 7 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.1 g belongs to the separate SL-6 stock; API explicitly declares
    0.1 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 0.0001 g/L in the DSM base, not the
    stored stock-strength value as a direct ingredient. Prefer a nested stock plus
    dose. This calculation is not independent authentication of unavailable KOMODO
    branches.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.347752,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 40-40", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "ZnSO4 x 7
    H2O                                              0.10    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q19", "subject": "MnCl2 x 4 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.03 g belongs to the separate SL-6 stock; API explicitly declares
    0.03 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 3e-05 g/L in the DSM base, not the stored
    stock-strength value as a direct ingredient. Prefer a nested stock plus dose.
    This calculation is not independent authentication of unavailable KOMODO branches.",
    "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api133",
    "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.151588,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 41-41", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "MnCl2 x 4
    H2O                                              0.03    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q20", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.3 g belongs to the separate SL-6 stock; API explicitly declares
    0.3 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 0.0003 g/L in the DSM base, not the
    stored stock-strength value as a direct ingredient. Prefer a nested stock plus
    dose. This calculation is not independent authentication of unavailable KOMODO
    branches.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    4.85123,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 42-42", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "H3BO3                                                      0.30    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q21", "subject":
    "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.2 g belongs to the separate SL-6 stock; API explicitly declares
    0.2 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 0.0002 g/L in the DSM base, not the
    stored stock-strength value as a direct ingredient. Prefer a nested stock plus
    dose. This calculation is not independent authentication of unavailable KOMODO
    branches.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.54037,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 43-43", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CoCl2 x 6
    H2O                                              0.20    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q22", "subject": "CuCl2 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.01 g belongs to the separate SL-6 stock; API explicitly declares
    0.01 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 1e-05 g/L in the DSM base, not the stored
    stock-strength value as a direct ingredient. Prefer a nested stock plus dose.
    This calculation is not independent authentication of unavailable KOMODO branches.",
    "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api133",
    "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0586569,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 44-44", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "CuCl2 x 2
    H2O                                              0.01    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q23", "subject": "NiCl2 x 6 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.02 g belongs to the separate SL-6 stock; API explicitly declares
    0.02 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 2e-05 g/L in the DSM base, not the stored
    stock-strength value as a direct ingredient. Prefer a nested stock plus dose.
    This calculation is not independent authentication of unavailable KOMODO branches.",
    "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api133",
    "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.154322,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 45-45", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "NiCl2 x 6
    H2O                                              0.02    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2MoO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-6 stock, not direct final medium",
    "interpretation": "0.03 g belongs to the separate SL-6 stock; API explicitly declares
    0.03 g/L stock strength. The receiving dose is 1 ml on the explicit 1 L DSM base.
    Using that declared stock strength yields 3e-05 g/L in the DSM base, not the stored
    stock-strength value as a direct ingredient. Prefer a nested stock plus dose.
    This calculation is not independent authentication of unavailable KOMODO branches.",
    "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api133",
    "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.123993,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 46-46", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Na2MoO4 x
    2 H2O                                            0.03    g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q25", "subject": "Main water and
    explicit final volume", "local_fields": [], "decision": "evidence_only", "stage":
    "DSM basal solvent and denominator", "interpretation": "Source lists 1000 ml water
    and explicitly states final volume 1000 ml. Retain both source claims without
    treating the sum of water and later additions as a separately measured total.",
    "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api133",
    "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q26", "subject": "SL-6 receiving dose", "local_fields": [], "decision": "evidence_only",
    "stage": "separate stock addition", "interpretation": "The missing 1 ml stock
    addition belongs to the DSM 1 L base. It is not seven direct stock-strength ingredient
    additions.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "SL-6 water", "local_fields":
    [], "decision": "evidence_only", "stage": "stock solvent", "interpretation": "The
    stock lists 1000 ml distilled water. API separately declares stock rates; do not
    infer a measured final stock volume solely from the water input.", "sources":
    [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api133", "reference":
    "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 55-55", "source_key": "dsmz133",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Distilled
    water                     1000.00   ml", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q28", "subject": "pH", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "ph_value",
    "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml",
    "field_path": "ph_value", "original": 7.0}], "decision": "evidence_only", "stage":
    "DSM source control", "interpretation": "All selected layers retain 7.0, matching
    DSM 133. This source correspondence does not independently verify unavailable
    KOMODO pages.", "sources": [{"locator": "extracted-text lines 3-3", "source_key":
    "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "Final pH:
    7.0", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients, adjust pH to 7.0 and autoclave.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject":
    "Dissolve, adjust pH and autoclave", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients,
    adjust pH to 7.0 and autoclave."}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients,
    adjust pH to 7.0 and autoclave."}], "decision": "evidence_only", "stage": "base
    preparation", "interpretation": "The target and DSM owner retain the source sequence;
    nine KOMODO owners omit it. No unprovided autoclave duration or temperature is
    invented.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133", "source_raw_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "source_text_sha256":
    "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13", "accessed_at":
    "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients, adjust pH to 7.0 and autoclave.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject":
    "Chemoautotrophic gas options and bicarbonate", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml", "field_path": "preparation_steps[1].description",
    "original": "For chemoautotrophic growth incubate under a gas atmosphere of a)
    20 - 80% carbon monoxide + 10% O2 + 70 - 10% N2 or b) 70% H2 + 20% O2 + 10% CO2
    adding 2.50 g NaHCO3 per liter of medium."}, {"record_path": "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "For chemoautotrophic
    growth incubate under a gas atmosphere of a) 20 - 80% carbon monoxide + 10% O2
    + 70 - 10% N2 or b) 70% H2 + 20% O2 + 10% CO2 adding 2.50 g NaHCO3 per liter of
    medium."}], "decision": "evidence_only", "stage": "conditional source preparation",
    "interpretation": "Preserve option a 20–80% CO with 10% O2 and complementary 70–10%
    N2, or option b 70% H2/20% O2/10% CO2 with 2.50 g/L NaHCO3. The coupled ranges
    are not independent settings. The target/DSM owner retain this text; no gas pressure
    or temperature is added.", "sources": [{"locator": "$.data.solutions[0].steps[1]",
    "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\":
    \"For chemoautotrophic growth incubate under a gas atmosphere of a) 20 - 80% carbon
    monoxide + 10% O2 + 70 - 10% N2 or b) 70% H2 + 20% O2 + 10% CO2 adding 2.50 g
    NaHCO3 per liter of medium.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "Chemoorganotrophic acetate
    and air", "local_fields": [{"record_path": "data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml",
    "field_path": "preparation_steps[2].description", "original": "For chemoorganotrophic
    growth add 3.00 g sodium acetate and incubate under air atmosphere."}, {"record_path":
    "data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml", "field_path":
    "preparation_steps[2].description", "original": "For chemoorganotrophic growth
    add 3.00 g sodium acetate and incubate under air atmosphere."}], "decision": "evidence_only",
    "stage": "conditional source preparation", "interpretation": "The retained 3 g
    acetate under air is the conditional base amount, not an additional 3 g on top
    of the optional row. Exact strain exceptions remain separate.", "sources": [{"locator":
    "$.data.solutions[0].steps[2]", "source_key": "api133", "reference": "https://mediadive.dsmz.de/rest/medium/133",
    "source_raw_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "source_text_sha256": "d1cd25d4c2725024e7905139bb0d9f96216368d952a987e92cc6dee019ae3c13",
    "accessed_at": "2026-10-28T06:49:25.760912Z", "exact_source_quote": "{\n                        \"step\":
    \"For chemoorganotrophic growth add 3.00 g sodium acetate and incubate under air
    atmosphere.\"\n                    }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q32", "subject": "DSM 1083 vitamin dose and filtration", "local_fields":
    [], "decision": "evidence_only", "stage": "DSM 1083 branches only", "interpretation":
    "The source prescribes 10 ml/L of the vitamin solution from 141, filter-sterilized.
    Transfer only the named vitamin stock; do not import medium 141 basal chemistry,
    mineral stock, pH, gases or strain prescriptions.", "sources": [{"locator": "extracted-text
    lines 26-28", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1083:
    The medium has to be supplemented with 10.00 ml/l of the vitamin solution\nof
    medium 141, sterilized by filtration. For chemoorganotrophic growth with acetate
    under\nair add also 10.00 ml/l of a 5% w/v NaHCO3 solution, sterilized by filtration.",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q33", "subject":
    "DSM 1083 organotrophic bicarbonate", "local_fields": [], "decision": "evidence_only",
    "stage": "DSM 1083 organotrophic branch only", "interpretation": "10 ml/L of 5%
    w/v NaHCO3, filter-sterilized, is explicitly prescribed under acetate/air conditions.
    This supplies 0.5 g per stated litre by 0.05 g/ml × 10 ml; it is distinct from
    the base H2/CO2 option.", "sources": [{"locator": "extracted-text lines 26-28",
    "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1083:
    The medium has to be supplemented with 10.00 ml/l of the vitamin solution\nof
    medium 141, sterilized by filtration. For chemoorganotrophic growth with acetate
    under\nair add also 10.00 ml/l of a 5% w/v NaHCO3 solution, sterilized by filtration.",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q34", "subject":
    "DSM 1085 seven-vitamin dose", "local_fields": [], "decision": "evidence_only",
    "stage": "DSM 1085 branches only", "interpretation": "1 ml/L of the seven-vitamin
    solution from 503 is prescribed. Do not substitute the ten-component Wolin stock
    or transfer the rest of medium 503.", "sources": [{"locator": "extracted-text
    lines 29-31", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1085:
    The medium has to be supplemented with 1 ml/l Seven Vitamins Solution\n(see medium
    503). For chemoorganotrophic growth with acetate under air, add also 20.00\nml/l
    of a 5% w/v NaHCO3 solution, sterilized by filtration.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q35", "subject": "DSM 1085 organotrophic
    bicarbonate", "local_fields": [], "decision": "evidence_only", "stage": "DSM 1085
    organotrophic branch only", "interpretation": "20 ml/L of 5% w/v NaHCO3, filter-sterilized,
    supplies 1 g per stated litre. Preserve the exact branch and do not collapse this
    dose with the DSM 1083 dose.", "sources": [{"locator": "extracted-text lines 29-31",
    "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 1085:
    The medium has to be supplemented with 1 ml/l Seven Vitamins Solution\n(see medium
    503). For chemoorganotrophic growth with acetate under air, add also 20.00\nml/l
    of a 5% w/v NaHCO3 solution, sterilized by filtration.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q36", "subject": "DSM 13294 seven
    vitamins and acetate omission", "local_fields": [], "decision": "evidence_only",
    "stage": "DSM 13294 branches only", "interpretation": "Omit acetate and add 1
    ml/L of seven vitamins from 503. These are named source prescriptions, not new
    experimental growth evidence.", "sources": [{"locator": "extracted-text lines
    32-34", "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294:
    Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution\n(see medium
    503). For chemoorganotrophic growth under air, add also 2.00 g/l Na\n-pyruvate
    and 1.00 g/l yeast extract.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q37", "subject": "DSM 13294 organotrophic pyruvate", "local_fields":
    [], "decision": "evidence_only", "stage": "DSM 13294 organotrophic branch only",
    "interpretation": "The source explicitly adds 2 g/L sodium pyruvate under air;
    this missing conditional ingredient does not apply to the entire family.", "sources":
    [{"locator": "extracted-text lines 32-34", "source_key": "dsmz133", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf", "source_raw_sha256":
    "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385", "source_text_sha256":
    "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7", "accessed_at":
    "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294: Omit acetate
    and supplement medium with 1 ml/l Seven Vitamins Solution\n(see medium 503). For
    chemoorganotrophic growth under air, add also 2.00 g/l Na\n-pyruvate and 1.00
    g/l yeast extract.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q38", "subject": "DSM 13294 organotrophic yeast extract", "local_fields": [],
    "decision": "evidence_only", "stage": "DSM 13294 organotrophic branch only", "interpretation":
    "The source explicitly adds 1 g/L yeast extract under air; retain complex-component
    identity and branch scope.", "sources": [{"locator": "extracted-text lines 32-34",
    "source_key": "dsmz133", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium133.pdf",
    "source_raw_sha256": "6a6c1e38d440f50f654262ba92d728c30c958f955d60760b4a7342cb3911c385",
    "source_text_sha256": "b961b8b7b430cfd1847b26c7bb84ef908dece3e19b18eb6a797c01ca0982aed7",
    "accessed_at": "2026-10-28T06:49:25.743739Z", "exact_source_quote": "For DSM 13294:
    Omit acetate and supplement medium with 1 ml/l Seven Vitamins Solution\n(see medium
    503). For chemoorganotrophic growth under air, add also 2.00 g/l Na\n-pyruvate
    and 1.00 g/l yeast extract.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q39", "subject": "Biotin", "local_fields": [], "decision": "evidence_only",
    "stage": "named vitamin stock preparation only", "interpretation": "Retain the
    literal supplied form and batch amount from this exact stock table. The amount
    is a stock-preparation mass, not a direct final-medium concentration. DSM 133
    supplies the branch-specific receiving dose; unrelated parent-medium composition
    and conditions do not transfer.", "sources": [{"locator": "extracted-text lines
    94-94", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Biotin                                                     2.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q40", "subject":
    "Folic acid", "local_fields": [], "decision": "evidence_only", "stage": "named
    vitamin stock preparation only", "interpretation": "Retain the literal supplied
    form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 95-95", "source_key": "dsmz141",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Folic acid                                                 2.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q41", "subject":
    "Pyridoxine hydrochloride", "local_fields": [], "decision": "evidence_only", "stage":
    "named vitamin stock preparation only", "interpretation": "Retain the literal
    supplied form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 96-96", "source_key": "dsmz141",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Pyridoxine
    hydrochloride                                  10.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q42", "subject": "Thiamine HCl",
    "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock
    preparation only", "interpretation": "Retain the literal supplied form and batch
    amount from this exact stock table. The amount is a stock-preparation mass, not
    a direct final-medium concentration. DSM 133 supplies the branch-specific receiving
    dose; unrelated parent-medium composition and conditions do not transfer.", "sources":
    [{"locator": "extracted-text lines 97-97", "source_key": "dsmz141", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_raw_sha256":
    "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_text_sha256":
    "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1", "accessed_at":
    "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Thiamine HCl                                               5.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q43", "subject":
    "Riboflavin", "local_fields": [], "decision": "evidence_only", "stage": "named
    vitamin stock preparation only", "interpretation": "Retain the literal supplied
    form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 98-98", "source_key": "dsmz141",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Riboflavin                                                 5.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q44", "subject":
    "Nicotinic acid", "local_fields": [], "decision": "evidence_only", "stage": "named
    vitamin stock preparation only", "interpretation": "Retain the literal supplied
    form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 106-106", "source_key": "dsmz141",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Nicotinic
    acid                       5.00   mg", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q45", "subject": "Calcium D-(+)-pantothenate", "local_fields":
    [], "decision": "evidence_only", "stage": "named vitamin stock preparation only",
    "interpretation": "Retain the literal supplied form and batch amount from this
    exact stock table. The amount is a stock-preparation mass, not a direct final-medium
    concentration. DSM 133 supplies the branch-specific receiving dose; unrelated
    parent-medium composition and conditions do not transfer.", "sources": [{"locator":
    "extracted-text lines 107-107", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Calcium D-(+)-pantothenate           5.00   mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q46", "subject":
    "Vitamin B12", "local_fields": [], "decision": "evidence_only", "stage": "named
    vitamin stock preparation only", "interpretation": "Retain the literal supplied
    form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 108-108", "source_key": "dsmz141",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Vitamin B12                          0.10   mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q47", "subject":
    "p-Aminobenzoic acid", "local_fields": [], "decision": "evidence_only", "stage":
    "named vitamin stock preparation only", "interpretation": "Retain the literal
    supplied form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 109-109", "source_key": "dsmz141",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "p-Aminobenzoic
    acid                  5.00   mg", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q48", "subject": "(DL)-alpha-Lipoic acid", "local_fields":
    [], "decision": "evidence_only", "stage": "named vitamin stock preparation only",
    "interpretation": "Retain the literal supplied form and batch amount from this
    exact stock table. The amount is a stock-preparation mass, not a direct final-medium
    concentration. DSM 133 supplies the branch-specific receiving dose; unrelated
    parent-medium composition and conditions do not transfer.", "sources": [{"locator":
    "extracted-text lines 110-110", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "(DL)-alpha-Lipoic
    acid               5.00   mg", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q49", "subject": "Distilled water", "local_fields": [], "decision":
    "evidence_only", "stage": "named vitamin stock preparation only", "interpretation":
    "Retain the literal supplied form and batch amount from this exact stock table.
    The 1000 ml is stock solvent, not proof of a measured final stock volume. DSM
    133 supplies the branch-specific receiving dose; unrelated parent-medium composition
    and conditions do not transfer.", "sources": [{"locator": "extracted-text lines
    111-111", "source_key": "dsmz141", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_raw_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_text_sha256": "5bb21acfe88f20470ae00176b83b9d9a6b2a7f78143e7807e6866cf4f2b442a1",
    "accessed_at": "2026-10-28T06:49:25.765816Z", "exact_source_quote": "Distilled
    water                   1000.00   ml", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q50", "subject": "Vitamin B12", "local_fields": [],
    "decision": "evidence_only", "stage": "named vitamin stock preparation only",
    "interpretation": "Retain the literal supplied form and batch amount from this
    exact stock table. The amount is a stock-preparation mass, not a direct final-medium
    concentration. DSM 133 supplies the branch-specific receiving dose; unrelated
    parent-medium composition and conditions do not transfer.", "sources": [{"locator":
    "extracted-text lines 177-177", "source_key": "dsmz503", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf",
    "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa",
    "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76",
    "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Vitamin B12                                              100.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q51", "subject":
    "p-Aminobenzoic acid", "local_fields": [], "decision": "evidence_only", "stage":
    "named vitamin stock preparation only", "interpretation": "Retain the literal
    supplied form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 178-178", "source_key": "dsmz503",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf",
    "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa",
    "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76",
    "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "p-Aminobenzoic
    acid                                       80.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q52", "subject": "D-(+)-biotin",
    "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock
    preparation only", "interpretation": "Retain the literal supplied form and batch
    amount from this exact stock table. The amount is a stock-preparation mass, not
    a direct final-medium concentration. DSM 133 supplies the branch-specific receiving
    dose; unrelated parent-medium composition and conditions do not transfer.", "sources":
    [{"locator": "extracted-text lines 179-179", "source_key": "dsmz503", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256":
    "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256":
    "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at":
    "2026-10-28T06:49:25.792164Z", "exact_source_quote": "D-(+)-biotin                                              20.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q53", "subject":
    "Nicotinic acid", "local_fields": [], "decision": "evidence_only", "stage": "named
    vitamin stock preparation only", "interpretation": "Retain the literal supplied
    form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 180-180", "source_key": "dsmz503",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf",
    "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa",
    "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76",
    "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Nicotinic
    acid                                           200.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q54", "subject": "Calcium pantothenate",
    "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock
    preparation only", "interpretation": "Retain the literal supplied form and batch
    amount from this exact stock table. The amount is a stock-preparation mass, not
    a direct final-medium concentration. DSM 133 supplies the branch-specific receiving
    dose; unrelated parent-medium composition and conditions do not transfer.", "sources":
    [{"locator": "extracted-text lines 181-181", "source_key": "dsmz503", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256":
    "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256":
    "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at":
    "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Calcium pantothenate                                     100.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q55", "subject":
    "Pyridoxine hydrochloride", "local_fields": [], "decision": "evidence_only", "stage":
    "named vitamin stock preparation only", "interpretation": "Retain the literal
    supplied form and batch amount from this exact stock table. The amount is a stock-preparation
    mass, not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 182-182", "source_key": "dsmz503",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf",
    "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa",
    "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76",
    "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Pyridoxine
    hydrochloride                                 300.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q56", "subject": "Thiamine-HCl
    x 2 H2O", "local_fields": [], "decision": "evidence_only", "stage": "named vitamin
    stock preparation only", "interpretation": "Retain the literal supplied form and
    batch amount from this exact stock table. The amount is a stock-preparation mass,
    not a direct final-medium concentration. DSM 133 supplies the branch-specific
    receiving dose; unrelated parent-medium composition and conditions do not transfer.",
    "sources": [{"locator": "extracted-text lines 183-183", "source_key": "dsmz503",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf",
    "source_raw_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa",
    "source_text_sha256": "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76",
    "accessed_at": "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Thiamine-HCl
    x 2 H2O                                     200.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q57", "subject": "Distilled water",
    "local_fields": [], "decision": "evidence_only", "stage": "named vitamin stock
    preparation only", "interpretation": "Retain the literal supplied form and batch
    amount from this exact stock table. The 1000 ml is stock solvent, not proof of
    a measured final stock volume. DSM 133 supplies the branch-specific receiving
    dose; unrelated parent-medium composition and conditions do not transfer.", "sources":
    [{"locator": "extracted-text lines 184-184", "source_key": "dsmz503", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf", "source_raw_sha256":
    "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa", "source_text_sha256":
    "ee46b3be03841e09fbf4de1daaa9cc23560d96aba728686633f8aac09f419b76", "accessed_at":
    "2026-10-28T06:49:25.792164Z", "exact_source_quote": "Distilled water                                         1000.00       ml",
    "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch059/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml: primary 15/15,
    secondary 15/15; data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1083.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1085.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_13294.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml:
    primary 15/15, secondary 15/15; data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml:
    primary 15/15, secondary 15/15. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:000797
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
  - CultureMech:000797
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
  - CultureMech:000797
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000797-flattened-sl6-and-missing-dose
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Seven stock components are represented as direct medium concentrations
  description: All 11 selected documents flatten SL-6 into direct ingredients at stock
    strength and omit its1 ml receiving dose. Current API declares the stock rates;
    the current DSM PDF explicitly declares the base final volume 1000 ml. Correct
    main basal amounts are retained, while the stock stage and solvent must be represented
    separately.
  target_ids:
  - CultureMech:000797
  field_paths:
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz133
  - api133
  rule_id: source-stock-stage-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-000797-source-branches-and-stale-generated-topology
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The generated family collapses distinct source prescriptions
  description: DSM 133 distinguishes chemoautotrophic and organotrophic options and
    DSM 1083/1085/13294 supplements. The six strain owners retain correct variant
    labels after a partial topology repair, but all nine KOMODO owners still contain
    the same copied 15 ingredients and no preparation. Only the two DSM 13294-labelled
    owners contradict the explicit acetate omission. The generated target still uses
    the old DSM 1083 source-duplicate parent instead of the repaired family root.
    Current conservative merge code rejects incompatible scientific projections; old
    generated content and copied signatures do not prove recipe equivalence.
  target_ids:
  - CultureMech:000797
  field_paths:
  - merged_from
  - synonyms
  - parent_media
  - variant_relationship
  - variant_modifications
  - data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1083.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1085.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::ingredients[6]
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::ingredients[6]
  evidence_ids:
  - dsmz133
  - api133
  - local0
  - history-auth
  rule_id: source-variant-and-generated-freshness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-000797-phosphate-and-nickel-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two asserted IDs omit the source hydrates
  description: Na2HPO4·12H2O uses CHEBI:34683 with formula HO4P.2Na, and NiCl2·6H2O
    uses CHEBI:34887 with formula Cl2Ni, in both primary and secondary slots. Current
    CHEBI:53542 explicitly represents nickel chloride hexahydrate. Correct cobalt,
    copper, magnesium, calcium, zinc, manganese and molybdate hydrate mappings are
    credited. Ferric ammonium citrate and agar are mixtures; their API mmol_l is not
    endorsed.
  target_ids:
  - CultureMech:000797
  field_paths:
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  - ingredients[13].term
  - ingredients[13].mediaingredientmech_chebi_term
  evidence_ids:
  - grounding
  - chebi34683
  - chebi34887
  - chebi53542
  - dsmz133
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-000797-missing-branch-preparation-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source-specific preparation and claim evidence are incomplete
  description: 'Target and DSM owner retain the three base preparation paragraphs,
    but nine KOMODO owners omit preparation and retain Aerobic: No despite the DSM
    source air/oxygen-containing options. Missing water, branch vitamins, bicarbonate,
    pyruvate and yeast-extract stages require scoped representation. No claim-level
    source evidence is attached. SOLID_AGAR represents only the optional agar branch.'
  target_ids:
  - CultureMech:000797
  field_paths:
  - evidence
  - physical_state
  - data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml::notes
  - data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_1083.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_1085.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::notes
  - data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml::notes
  - data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1083.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1085.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::preparation_steps
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::preparation_steps
  - data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml::preparation_steps
  evidence_ids:
  - dsmz133
  - dsmz141
  - dsmz503
  - api133
  rule_id: source-preparation-and-evidence-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-000797-historical-time-and-curation-claims
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamps and curation flags need qualified context
  description: KOMODO imported events literally end in .fZ and subsequent copied-DSM
    events lack timezone. The topology writer uses a fixed historical timestamp and
    _upsert_event replaces matching events. Existing ingredients_curated flags and
    exact-match prose do not certify source-specific chemistry. Current code is not
    proof of historical execution.
  target_ids:
  - CultureMech:000797
  field_paths:
  - data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1083.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1085.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1083.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1085.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_dsm_1083.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_dsm_1085.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_dsm_13294.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml::data_quality_flags
  evidence_ids:
  - history-auth
  - writer68
  - writer69
  - writer70
  - writer71
  - writer72
  - writer73
  - writer74
  rule_id: append-only-source-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Restore the exact SL-6 stock and receiving dose in the maintained source-specific
    recipes, preserving compound forms and absolute water inputs. Link only an independently
    checked stock representation; this review did not assess a standalone solution25
    owner. Attach root evidence scoped to each stock-dose field.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000797
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
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
  description: Preserve the valid DSM 133 identity and the useful current family-root/strain-variant
    repair. Review each exact branch against its source, retain unresolved KOMODO
    equivalence honestly, represent missing branch supplements and regenerate after
    maintained-owner repair. Review the inspected topology writer hardcoded stock
    signature and duplicate assertions; do not reuse copied amounts as equivalence
    proof.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000797
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
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
  description: Resolve the exact supplied hydrate mappings, or retain precise source
    labels with unresolved linkage. Preserve supported masses and reject anhydrous-mass
    molarity shortcuts. Verify any newly proposed secondary linkage independently.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000797
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
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
  description: Preserve the supported base instructions and distinguish each source
    branch, including exact filtration, gas and supplement conditions. Attach root
    evidence with precise field/stage scope; no new PreparationStep or SolutionDescriptor
    evidence slot is proposed. Do not transfer medium 141 or503 whole recipes or interpret
    collection prescriptions as measured growth.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000797
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
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
  description: Preserve every original event and its bytes. Correct future writer
    timestamp generation and append a new verified context/correction event with the
    actual curation date; do not rewrite historical timestamps or infer missing times.
    Retain partial topology credit while qualifying scientific-completion flags.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000797
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoautotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_carbon_monoxide_oxidizers.yaml
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
- Nine exact historical /komodo/servlet MediaInfo hyperlinks and the exact MediaList
  endpoint returned HTTP 403. Original prefix-only route failures are preserved separately.
  Current recipe equivalence and historical catalogue bytes remain unresolved; this
  is a partial scientific review, not full family authentication.
- Only the Wolin vitamin table from 141 and seven-vitamin table from 503 transfer.
  Their whole parent media, unrelated stocks, conditions and strain examples remain
  excluded.
- Vitamin stock water is not inferred to be a measured final volume. SL-6 numerical
  dilution is explicitly based on provider-declared stock g_l and the DSM base final-volume
  statement.
- No standalone solution25 owner was assessed or automatically recommended for reuse.
  No source-derived organism taxonomy or experimental growth claim is added.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
