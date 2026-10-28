# Scientific review of desulfocella_halophila_medium

- Review: 20261028T191726Z-desulfocella-halophila-medium-batch075
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:56:04.448371Z
- Finished UTC: 2026-10-28T19:17:26.781948Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSM815a main ingredient rates, pH and much of its preparation are supported. Curation is needed to restore the SL-11 stock/dose boundary, locate its existing procedure correctly, resolve nickel hydrate and sodium-resazurin mappings, and attach field-scoped evidence.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch075 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000283 | data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml | generated | desulfocella_halophila_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000283 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:000283 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:000283 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:000283 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact DSM815a identity

identity: supported. Targets: CultureMech:000283.

Current maintained owner, generated target, complete two-page DSM815a source and API815a identify the same formulation. No other DSM815 or similarly named medium is silently substituted.

### Classification and retained preparation

consistency: supported. Targets: CultureMech:000283.

COMPLEX/UNDEFINED and LIQUID are appropriate to the yeast-extract-containing source and current API complex_medium:yes. Correct current pH, main staged preparation and optional supplement are explicitly credited; only SL-11 procedure placement requires restructuring.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:000283.

Three complete historical reports and one exact selected parent row were read. Earlier blanket conflicts are reassessed using the explicit current provider main/stock rates and positive SL-11 make-up. Existing main preparation and present source forms are credited independently of old diagnostic output. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:000283.

All 46 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:000283", "selected_concentration_field_count": 46, "selected_concentration_fields_covered": 46, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2SO4                                                   3.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 21.1208,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "6", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   CaCl2 x 2 H2O                                            6.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 40.8122,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "40", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 5-5", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   NaCl                                                    40.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 40,\n                        \"unit\": \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\": 684.463,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 6-6", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   KCl                                                      2.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 26.8276,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   NH4Cl                                                    0.30         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 5.60852,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   KH2PO4                                                   0.20         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.46967,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "8", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "8", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 9-9", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   MgCl2 x 6 H2O                                            8.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\": 39.3501,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "SrCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 10-10", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   SrCl2 x 6 H2O                                            0.10         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"SrCl2 x 6 H2O\",\n                        \"compound_id\": 176,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.37507,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "MOPS", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 12-12", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   MOPS                                                     3.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[9]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"MOPS\",\n                        \"compound_id\": 351,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 14.3362,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained.", "sources": [{"locator": "extracted-text physical LF lines 13-13", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Yeast extract                                            1.00         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.0005", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.0005", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained. The primary specifies 0.5 mL of 0.1% w/v sodium resazurin, corresponding to 0.0005 g on the declared nominal recipe basis; the supplied sodium form is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 14-14", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Sodium resazurin (0.1% w/v)                              0.50        ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Na-pyruvate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained. Its separately sterilized anoxic addition is part of the main recipe, not an unsupported stock concentration; retain the source preparation sequence.", "sources": [{"locator": "extracted-text physical LF lines 15-15", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na-pyruvate                                              2.50         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[12]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 22.7182,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained. Its separately sterilized anoxic addition is part of the main recipe, not an unsupported stock concentration; retain the source preparation sequence.", "sources": [{"locator": "extracted-text physical LF lines 16-16", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2CO3                                                   0.50         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[13]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 4.71751,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider basis", "interpretation": "The exact main-recipe amount and explicit current provider g_l support this existing rate on the provider nominal recipe basis. The provider declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency is not silently repaired or treated as measured final volume. Existing source values are retained. Its separately sterilized anoxic addition is part of the main recipe, not an unsupported stock concentration; retain the source preparation sequence.", "sources": [{"locator": "extracted-text physical LF lines 17-17", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2S x 9 H2O                                             0.10         g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[14]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.416351,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 35-35", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2-EDTA x 2 H2O                                         5.20        g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 36-36", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   FeCl2 x 4 H2O                                            1.50        g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 37-37", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   ZnCl2                                                   70.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 38-38", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   MnCl2 x 4 H2O                                          100.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 39-39", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   H3BO3                                                    6.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 40-40", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   CoCl2 x 6 H2O                                          190.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 41-41", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   CuCl2 x 2 H2O                                            2.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 42-42", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   NiCl2 x 6 H2O                                           24.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation": "The source batch mass and explicit make-up to1000 mL support this stock concentration, as does the current provider stock g_l. Its root ingredient placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values, supplied hydrates and positive stock denominator; do not promote them to final-medium rates.", "sources": [{"locator": "extracted-text physical LF lines 43-43", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2MoO4 x 2 H2O                                         36.00       mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "SL-11 receiving dose", "local_fields": [], "decision": "add", "stage": "Main recipe receives stock", "interpretation": "Preserve the exact1 mL SL-11 addition, separately from the stock composition and its own1 L make-up.", "sources": [{"locator": "extracted-text physical LF lines 11-11", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Trace element solution SL-11                             1.00        ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[8]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Main recipe water", "local_fields": [], "decision": "add", "stage": "Main solvent charge", "interpretation": "Preserve the specified1000 mL water charge; do not force a final-volume claim from it or from the API volume1001 metadata.", "sources": [{"locator": "extracted-text physical LF lines 18-18", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Distilled water                                       1000.00        ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[15]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "SL-11 water and positive final-volume instruction", "local_fields": [], "decision": "add", "stage": "Stock solvent and final volume", "interpretation": "The table lists1000 mL water, while the procedure starts with800 mL and finally brings the stock to1000 mL. Represent this operational stage distinction; the explicit final stock volume supports its mass concentrations.", "sources": [{"locator": "extracted-text physical LF lines 44-44", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Distilled water                                       1000.00       ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "Final pH and main preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ph_value", "original": 7.2}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "ph_value", "original": 7.2}, {"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with NaOH and sparge medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2."}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with NaOH and sparge medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2."}], "decision": "evidence_only", "stage": "Main medium", "interpretation": "Existing pH7.2 and main procedure agree with the primary: preliminary pH6,30-45 min100% N2 sparging, anaerobic dispensing/autoclaving, separate filtered pyruvate and anoxic sulfide/carbonate additions. Preserve the source wording distinguishing bicarbonate in the exception sentence and carbonate in the table; do not invent a different reagent or autoclave temperature/time.", "sources": [{"locator": "extracted-text physical LF lines 20-26", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "1. Dissolve ingredients except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with\nNaOH and sparge medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave. Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic\nstock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock\nsolution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be\n7.2.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with NaOH and sparge medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be 7.2.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Optional dithionite", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Note: Prior to inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution freshly prepared under N2 and filter-sterilized) can be added to the medium to stimulate growth at the beginning."}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Note: Prior to inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution freshly prepared under N2 and filter-sterilized) can be added to the medium to stimulate growth at the beginning."}], "decision": "evidence_only", "stage": "Conditional source supplement", "interpretation": "Retain the existing conditional10-20 mg/L direction from explicitly5% w/v fresh filtered N2 stock. It is optional, not a missing mandatory basal ingredient.", "sources": [{"locator": "extracted-text physical LF lines 27-29", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "2. Note: Prior to inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution\nfreshly prepared under N2 and filter-sterilized) can be added to the medium to stimulate\ngrowth at the beginning.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"step\": \"Note: Prior to inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution freshly prepared under N2 and filter-sterilized) can be added to the medium to stimulate growth at the beginning.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "SL-11 staged preparation retained at main level", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml", "field_path": "preparation_steps[2].description", "original": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."}], "decision": "correct", "stage": "SL-11 only", "interpretation": "All numeric controls are already retained and source-supported:800 mL initial water, pH7 using2 N NaOH, FeCl2 then other compounds, final pH6 and make-up to1000 mL. Move this existing exact procedure to its stock context rather than applying it to the completed medium.", "sources": [{"locator": "extracted-text physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].steps[0]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch075/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:000283.

data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml: primary 22/23, secondary 21/23; data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml: primary 22/23, secondary 21/23. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs. CHEBI:64758 correctly denotes the supplied EDTA disodium dihydrate. The literal preferred spelling 'Na2-EDTA x 2 H2O' is REJECTED in current CSV row 6338, while row 6339 maps the same local spelling as a synonym to the MAPPED preferred 'Na2EDTA·2H2O' (row 6372). This is a local-label mapping-status discrepancy, not a wrong-chemical-ID finding.

### Scope and source limits

scope: supported. Targets: CultureMech:000283.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:000283.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: SL-11 stock is represented as final-medium ingredients

major / open / confirmed; issue key: culturemech-000283-sl11-flattening.

Nine SL-11 components remain in the same root list as the main recipe at full stock g/L; the separate stock, receiving 1 mL dose and solvent/final-volume controls are missing from structured formulation fields. Existing main ingredient rates agree with provider g_l and are credited, rather than being indiscriminately labelled conflicts.

### f2: Nickel hydrate and sodium resazurin are linked to different supplied forms

major / open / confirmed; issue key: culturemech-000283-nickel-hydrate-and-sodium-resazurin-form.

Every selected layer names nickel chloride hexahydrate but asserts anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806; there is no asserted resazurin secondary slot to correct. Exact labels pass native checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms. Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.

### f3: Supported existing fields lack claim-level evidence

minor / open / confirmed; issue key: culturemech-000283-claim-evidence-gap.

Neither selected layer contains attached formulation claims. Current primary/provider agreement newly supports unchanged main amounts and preparation, while historical report objects are a separate population and do not authenticate old access dates.

## Recommended Actions And Acceptance Checks

### action1

Represent SL-11 as its exact source stock with positive 1000 mL make-up and 1 mL receiving dose. Move the supported stock procedure into that context, retain correct main recipe amounts and pH/procedure, and keep provider normalization explicitly qualified.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Resolve the exact source hydrate and sodium-salt identities against authoritative ontology and MIM records. Use verified supplied-form mappings or retain precise source labels with unresolved mapping; preserve source masses and do not substitute anhydrous molar arithmetic.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Attach precise ingredient or root evidence scoped to the exact source fields, including preparation and stock doses. Preserve existing source/history bytes and append verified current context; do not add evidence to unsupported SolutionDescriptor or PreparationStep slots.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch075/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch075/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch075/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch075/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm815a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and every rendered page read, including main recipe, separate stock tables and all staged procedures. Physical LF line locators refer to the preserved pdftotext output. |
| api815a | https://mediadive.dsmz.de/rest/medium/815a; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current provider identity, solution tables and preparation read. Explicit g_l and declared volumes are credited only on their named provider stock or recipe basis; they are not independent measured final volumes. Provider mmol_l values are not adopted as chemical-form authority. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi36385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:36385; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:36385 = strontium dichloride hexahydrate; definition []; formula ['Cl2Sr.6H2O']; mass ['266.616']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi39074 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:39074; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:39074 = MOPS; definition ['An oxygen molecular entity that acts as an excellent buffer for many biological systems at near-neutral pH.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:50144; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:50144 = sodium pyruvate; definition []; formula ['C3H3O3.Na']; mass ['110.044']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na']; mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch075/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected and dependency-context term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfocella_halophila_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocella_halophila_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history-auth | REVIEW_WORK/batch075/record05/historical-authentication.json; attached_claims; historical_plan_claims | supports | Actual attached claims in scoped stock sections and historical parent-plan claims are separate populations. Current raw-digest equality and literal or normalized-HTML excerpt equality are independently recorded. No attached formulation claims occur on the selected target or its maintained contributors. Current byte matches do not authenticate historical execution or access dates. |
| writer35 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer36 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer37 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer38 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer39 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer40 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. No particular source range is authenticated by this writer. |
| writer41 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer42 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer43 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer44 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer45 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer46 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer47 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer48 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| quantity-inventory | REVIEW_WORK/batch075/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Provider main volume1001 mL and nominal g_l are not treated as independent measured final-volume evidence.
- Historical execution, dates and experimental performance are not authenticated; no different DSM815 source variant is transferred.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T191726Z-desulfocella-halophila-medium-batch075
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfocella_halophila_medium
started_at: '2026-10-28T18:56:04.448371Z'
finished_at: '2026-10-28T19:17:26.781948Z'
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
summary: The exact DSM815a main ingredient rates, pH and much of its preparation are
  supported. Curation is needed to restore the SL-11 stock/dose boundary, locate its
  existing procedure correctly, resolve nickel hydrate and sodium-resazurin mappings,
  and attach field-scoped evidence.
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
  - path: data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
    sha256: ed1c703f93aff67ef967ae0d896b3c0431329f003f0dfe0075ad53cfe95d8237
    role: target
  - path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
    sha256: c568747b4bc089c06e89cf4c15ec26c8492d6aa2588d93f5291fcb5d3519bf0b
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfocella_halophila_medium.yaml.md
    sha256: b7b29e73f6f57653386df534eb83f0336de8936d00f8fba26b5aa388b92e8897
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.md
    sha256: ee5be87b88f22093ea03e9e8395189f2e80214c669d6b9581690574270d6d337
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocella_halophila_medium.md
    sha256: 71f34502c400920c04b2841258c022fa25df619d457bbb3344573f5299412b1c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
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
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
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
  selection: Authoritative batch075 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000283
targets:
- target_id: CultureMech:000283
  path: data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
  label: desulfocella_halophila_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000283
  command: just validate-schema data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000283
  command: just validate-strict data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch075/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000283
  command: just validate-terms data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:000283
  command: just validate-references data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:10:01.448810Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: ed1c703f93aff67ef967ae0d896b3c0431329f003f0dfe0075ad53cfe95d8237
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:10:01.448977Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: c568747b4bc089c06e89cf4c15ec26c8492d6aa2588d93f5291fcb5d3519bf0b
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch075/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:05.640540Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 3b60c6c25b18beb518f754d14282f95035619c612bf35128b10c48b3a086062a
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch075/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:06.746781Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 64360041796352dcb8552543cae52d9560cd5be4563d1a77ce434ec3551f2eab
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch075/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:07.990939Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 15694051a5d596c098945d48a39a6234f23de3c494ab0cda4ada585b9fdf00a6
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch075/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:08.850194Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 0beb8f3ea94e3147c2c52b66a95992ecdfd8ffa4ab3d379a5b62d957775048ef
- evidence_id: dsm815a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:56:02.531354Z'
  support: supports
  summary: Complete exact DSM primary PDF text and every rendered page read, including
    main recipe, separate stock tables and all staged procedures. Physical LF line
    locators refer to the preserved pdftotext output.
  snapshot_sha256: cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90
- evidence_id: api815a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/815a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:56:02.531405Z'
  support: supports
  summary: Complete current provider identity, solution tables and preparation read.
    Explicit g_l and declared volumes are credited only on their named provider stock
    or recipe basis; they are not independent measured final volumes. Provider mmol_l
    values are not adopted as chemical-form authority.
  snapshot_sha256: 0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:59:58.520514Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.099115Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.155193Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.717439Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:01.295632Z'
  support: supports
  summary: OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula
    ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:01.366440Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:01.449035Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:01.913830Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi36385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:36385
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:01.971932Z'
  support: supports
  summary: OLS current exact CHEBI:36385 = strontium dichloride hexahydrate; definition
    []; formula ['Cl2Sr.6H2O']; mass ['266.616']; obsolete=False. Literal label is
    distinct from supplied-form equivalence.
  snapshot_sha256: 8593f1fca0faaa416e71c19974851d342dfe12bc8c19ee6e34ddc78e8bbc5583
- evidence_id: chebi39074
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:39074
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:01.984909Z'
  support: supports
  summary: OLS current exact CHEBI:39074 = MOPS; definition ['An oxygen molecular
    entity that acts as an excellent buffer for many biological systems at near-neutral
    pH.']; formula None; mass None; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: ed129ea75a8e240eb53c047abc3f1af870d2434f97e65bce7b362fc45cfc659a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:02.509503Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:50144
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:02.542485Z'
  support: supports
  summary: OLS current exact CHEBI:50144 = sodium pyruvate; definition []; formula
    ['C3H3O3.Na']; mass ['110.044']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 55d173a8545b2fc57dea3f3a4b07b9052f0bbd86f9a3e9d5b0b7b5a08b9c0162
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:02.583313Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:02.597767Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.114801Z'
  support: supports
  summary: OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition
    ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na'];
    mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 326b128326745296132512f9e618ef60c9c3230252a9dac3a75db92f8caa3156
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.187771Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.247647Z'
  support: supports
  summary: OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition
    ['A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O.'];
    formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.325568Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.451309Z'
  support: supports
  summary: OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O'];
    mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.725104Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.799716Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.804524Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch075/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T19:10:01.456086Z'
  support: supports
  summary: Complete selected and dependency-context term slots and current packaged
    MIM CSV exact-identifier joins with row locators and metadata commit; includes
    separately scoped dependency context. No fuzzy mapping or historical-validity
    inference.
  snapshot_sha256: 7d77490446efd714e087411e551af348f27a783e4a7a29b724aa39f11109214c
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfocella_halophila_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:10:01.514000Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: b7b29e73f6f57653386df534eb83f0336de8936d00f8fba26b5aa388b92e8897
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:10:01.514032Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: ee5be87b88f22093ea03e9e8395189f2e80214c669d6b9581690574270d6d337
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocella_halophila_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:10:01.514057Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 71f34502c400920c04b2841258c022fa25df619d457bbb3344573f5299412b1c
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch075/record05/historical-authentication.json
  locator: attached_claims; historical_plan_claims
  accessed_at: '2026-10-28T19:10:01.514091Z'
  support: supports
  summary: Actual attached claims in scoped stock sections and historical parent-plan
    claims are separate populations. Current raw-digest equality and literal or normalized-HTML
    excerpt equality are independently recorded. No attached formulation claims occur
    on the selected target or its maintained contributors. Current byte matches do
    not authenticate historical execution or access dates.
  snapshot_sha256: 540e729617c861e0212a203eec0f41c522f90fc02eee0a116d1fe2d391f5a3a0
- evidence_id: writer35
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T19:10:01.514166Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer36
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T19:10:01.514193Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer37
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T19:10:01.514217Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer38
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T19:10:01.514245Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer39
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T19:10:01.514276Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer40
  kind: record_content
  reference: scripts/migrate_ph_range.py
  locator: parse_ph_range; migrate_one
  accessed_at: '2026-10-28T19:10:01.514298Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. No particular source range
    is authenticated by this writer.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer41
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T19:10:01.514329Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer42
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T19:10:01.514365Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer43
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T19:10:01.514407Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer44
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T19:10:01.514445Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer45
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T19:10:01.514468Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer46
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T19:10:01.514491Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer47
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T19:10:01.514514Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer48
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T19:10:01.514540Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch075/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T19:10:01.538700Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: f17cbfa45cbd7c3fc6e405dc7b327e68feb9e15199b6f3e172f32790d6bff0db
assessments:
- assessment_id: a1
  area: identity
  topic: Exact DSM815a identity
  outcome: supported
  summary: Current maintained owner, generated target, complete two-page DSM815a source
    and API815a identify the same formulation. No other DSM815 or similarly named
    medium is silently substituted.
  target_ids:
  - CultureMech:000283
  evidence_ids:
  - local0
  - local1
  - dsm815a
  - api815a
- assessment_id: a2
  area: consistency
  topic: Classification and retained preparation
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are appropriate to the yeast-extract-containing
    source and current API complex_medium:yes. Correct current pH, main staged preparation
    and optional supplement are explicitly credited; only SL-11 procedure placement
    requires restructuring.
  target_ids:
  - CultureMech:000283
  evidence_ids:
  - dsm815a
  - api815a
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Three complete historical reports and one exact selected parent row were
    read. Earlier blanket conflicts are reassessed using the explicit current provider
    main/stock rates and positive SL-11 make-up. Existing main preparation and present
    source forms are credited independently of old diagnostic output. Current conservative
    merging preserves scientific fields and rejects incompatible formulations. Inspected
    writer behavior is described separately by exact file and function; it does not
    prove historical execution.
  target_ids:
  - CultureMech:000283
  evidence_ids:
  - history-auth
  - writer35
  - writer36
  - writer37
  - writer38
  - writer39
  - writer40
  - writer41
  - writer42
  - writer43
  - writer44
  - writer45
  - writer46
  - writer47
  - writer48
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 46 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:000283
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:000283",
    "selected_concentration_field_count": 46, "selected_concentration_fields_covered":
    46, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    3-3", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2SO4                                                   3.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    21.1208,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "CaCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    4-4", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   CaCl2
    x 2 H2O                                            6.00         g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\":
    40.8122,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    5-5", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   NaCl                                                    40.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 40,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\":
    684.463,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    6-6", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   KCl                                                      2.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    26.8276,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    7-7", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   NH4Cl                                                    0.30         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    5.60852,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    8-8", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   KH2PO4                                                   0.20         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.46967,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "MgCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "8", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "8", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    9-9", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   MgCl2
    x 6 H2O                                            8.00         g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\":
    39.3501,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "SrCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    10-10", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   SrCl2
    x 6 H2O                                            0.10         g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"SrCl2 x 6 H2O\",\n                        \"compound_id\":
    176,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.37507,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "MOPS", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    12-12", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   MOPS                                                     3.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[9]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"MOPS\",\n                        \"compound_id\":
    351,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    14.3362,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained.", "sources": [{"locator": "extracted-text physical LF lines
    13-13", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Yeast
    extract                                            1.00         g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q11", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.0005",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.0005",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified
    provider basis", "interpretation": "The exact main-recipe amount and explicit
    current provider g_l support this existing rate on the provider nominal recipe
    basis. The provider declares volume1001 mL yet reports these rates without a 1001
    divisor; that inconsistency is not silently repaired or treated as measured final
    volume. Existing source values are retained. The primary specifies 0.5 mL of 0.1%
    w/v sodium resazurin, corresponding to 0.0005 g on the declared nominal recipe
    basis; the supplied sodium form is assessed separately.", "sources": [{"locator":
    "extracted-text physical LF lines 14-14", "source_key": "dsm815a", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf", "source_raw_sha256":
    "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90", "source_text_sha256":
    "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485", "accessed_at":
    "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Sodium resazurin (0.1%
    w/v)                              0.50        ml", "quote_representation": "captured
    extracted text"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "Na-pyruvate", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained. Its separately sterilized anoxic addition is part of the
    main recipe, not an unsupported stock concentration; retain the source preparation
    sequence.", "sources": [{"locator": "extracted-text physical LF lines 15-15",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na-pyruvate                                              2.50         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[12]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\":
    113,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    22.7182,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "Na2CO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained. Its separately sterilized anoxic addition is part of the
    main recipe, not an unsupported stock concentration; retain the source preparation
    sequence.", "sources": [{"locator": "extracted-text physical LF lines 16-16",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2CO3                                                   0.50         g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[13]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    4.71751,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "Na2S x 9 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe, qualified provider
    basis", "interpretation": "The exact main-recipe amount and explicit current provider
    g_l support this existing rate on the provider nominal recipe basis. The provider
    declares volume1001 mL yet reports these rates without a 1001 divisor; that inconsistency
    is not silently repaired or treated as measured final volume. Existing source
    values are retained. Its separately sterilized anoxic addition is part of the
    main recipe, not an unsupported stock concentration; retain the source preparation
    sequence.", "sources": [{"locator": "extracted-text physical LF lines 17-17",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2S x
    9 H2O                                             0.10         g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[14]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.416351,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2-EDTA x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation":
    "The source batch mass and explicit make-up to1000 mL support this stock concentration,
    as does the current provider stock g_l. Its root ingredient placement incorrectly
    omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values,
    supplied hydrates and positive stock denominator; do not promote them to final-medium
    rates.", "sources": [{"locator": "extracted-text physical LF lines 35-35", "source_key":
    "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2-EDTA
    x 2 H2O                                         5.20        g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation":
    "The source batch mass and explicit make-up to1000 mL support this stock concentration,
    as does the current provider stock g_l. Its root ingredient placement incorrectly
    omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values,
    supplied hydrates and positive stock denominator; do not promote them to final-medium
    rates.", "sources": [{"locator": "extracted-text physical LF lines 36-36", "source_key":
    "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   FeCl2
    x 4 H2O                                            1.50        g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation":
    "The source batch mass and explicit make-up to1000 mL support this stock concentration,
    as does the current provider stock g_l. Its root ingredient placement incorrectly
    omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values,
    supplied hydrates and positive stock denominator; do not promote them to final-medium
    rates.", "sources": [{"locator": "extracted-text physical LF lines 37-37", "source_key":
    "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   ZnCl2                                                   70.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation":
    "The source batch mass and explicit make-up to1000 mL support this stock concentration,
    as does the current provider stock g_l. Its root ingredient placement incorrectly
    omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values,
    supplied hydrates and positive stock denominator; do not promote them to final-medium
    rates.", "sources": [{"locator": "extracted-text physical LF lines 38-38", "source_key":
    "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   MnCl2
    x 4 H2O                                          100.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock",
    "interpretation": "The source batch mass and explicit make-up to1000 mL support
    this stock concentration, as does the current provider stock g_l. Its root ingredient
    placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the
    supported stock values, supplied hydrates and positive stock denominator; do not
    promote them to final-medium rates.", "sources": [{"locator": "extracted-text
    physical LF lines 39-39", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   H3BO3                                                    6.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock", "interpretation":
    "The source batch mass and explicit make-up to1000 mL support this stock concentration,
    as does the current provider stock g_l. Its root ingredient placement incorrectly
    omits the SL-11 stock and receiving1 mL dose. Preserve the supported stock values,
    supplied hydrates and positive stock denominator; do not promote them to final-medium
    rates.", "sources": [{"locator": "extracted-text physical LF lines 40-40", "source_key":
    "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   CoCl2
    x 6 H2O                                          190.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock",
    "interpretation": "The source batch mass and explicit make-up to1000 mL support
    this stock concentration, as does the current provider stock g_l. Its root ingredient
    placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the
    supported stock values, supplied hydrates and positive stock denominator; do not
    promote them to final-medium rates.", "sources": [{"locator": "extracted-text
    physical LF lines 41-41", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   CuCl2
    x 2 H2O                                            2.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock",
    "interpretation": "The source batch mass and explicit make-up to1000 mL support
    this stock concentration, as does the current provider stock g_l. Its root ingredient
    placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the
    supported stock values, supplied hydrates and positive stock denominator; do not
    promote them to final-medium rates.", "sources": [{"locator": "extracted-text
    physical LF lines 42-42", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   NiCl2
    x 6 H2O                                           24.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate SL-11 stock",
    "interpretation": "The source batch mass and explicit make-up to1000 mL support
    this stock concentration, as does the current provider stock g_l. Its root ingredient
    placement incorrectly omits the SL-11 stock and receiving1 mL dose. Preserve the
    supported stock values, supplied hydrates and positive stock denominator; do not
    promote them to final-medium rates.", "sources": [{"locator": "extracted-text
    physical LF lines 43-43", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Na2MoO4
    x 2 H2O                                         36.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "SL-11 receiving dose",
    "local_fields": [], "decision": "add", "stage": "Main recipe receives stock",
    "interpretation": "Preserve the exact1 mL SL-11 addition, separately from the
    stock composition and its own1 L make-up.", "sources": [{"locator": "extracted-text
    physical LF lines 11-11", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Trace
    element solution SL-11                             1.00        ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[8]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Main recipe water", "local_fields":
    [], "decision": "add", "stage": "Main solvent charge", "interpretation": "Preserve
    the specified1000 mL water charge; do not force a final-volume claim from it or
    from the API volume1001 metadata.", "sources": [{"locator": "extracted-text physical
    LF lines 18-18", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Distilled
    water                                       1000.00        ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[15]", "source_key":
    "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "SL-11 water and positive
    final-volume instruction", "local_fields": [], "decision": "add", "stage": "Stock
    solvent and final volume", "interpretation": "The table lists1000 mL water, while
    the procedure starts with800 mL and finally brings the stock to1000 mL. Represent
    this operational stage distinction; the explicit final stock volume supports its
    mass concentrations.", "sources": [{"locator": "extracted-text physical LF lines
    44-44", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "   Distilled
    water                                       1000.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 54-56",
    "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key": "api815a",
    "reference": "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "source_text_sha256":
    "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd", "accessed_at":
    "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "Final pH and main preparation",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "ph_value", "original": 7.2}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "ph_value", "original": 7.2}, {"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients
    except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with NaOH and sparge
    medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense medium under
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium
    pH should be 7.2."}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients
    except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with NaOH and sparge
    medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense medium under
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium
    pH should be 7.2."}], "decision": "evidence_only", "stage": "Main medium", "interpretation":
    "Existing pH7.2 and main procedure agree with the primary: preliminary pH6,30-45
    min100% N2 sparging, anaerobic dispensing/autoclaving, separate filtered pyruvate
    and anoxic sulfide/carbonate additions. Preserve the source wording distinguishing
    bicarbonate in the exception sentence and carbonate in the table; do not invent
    a different reagent or autoclave temperature/time.", "sources": [{"locator": "extracted-text
    physical LF lines 20-26", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "1. Dissolve
    ingredients except pyruvate, bicarbonate and sulfide, adjust pH to 6.0 with\nNaOH
    and sparge medium for 30 - 45 min with 100% N2 gas to make it anoxic. Dispense\nmedium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave.
    Before use add pyruvate (sterilized by filtration) and sulfide from sterile anoxic\nstock
    solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock\nsolution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Final medium pH should be\n7.2.",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients except pyruvate, bicarbonate and sulfide, adjust pH to
    6.0 with NaOH and sparge medium for 30 - 45 min with 100% N2 gas to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Before use add pyruvate (sterilized by filtration) and sulfide
    from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from
    a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.
    Final medium pH should be 7.2.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Optional dithionite",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Note: Prior to
    inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution freshly
    prepared under N2 and filter-sterilized) can be added to the medium to stimulate
    growth at the beginning."}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "Note: Prior to
    inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution freshly
    prepared under N2 and filter-sterilized) can be added to the medium to stimulate
    growth at the beginning."}], "decision": "evidence_only", "stage": "Conditional
    source supplement", "interpretation": "Retain the existing conditional10-20 mg/L
    direction from explicitly5% w/v fresh filtered N2 stock. It is optional, not a
    missing mandatory basal ingredient.", "sources": [{"locator": "extracted-text
    physical LF lines 27-29", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "2. Note:
    Prior to inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v solution\nfreshly
    prepared under N2 and filter-sterilized) can be added to the medium to stimulate\ngrowth
    at the beginning.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[0].steps[1]", "source_key": "api815a", "reference": "https://mediadive.dsmz.de/rest/medium/815a",
    "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: Prior to inoculation 10-20 mg/l sodium dithionite (added from a 5% w/v
    solution freshly prepared under N2 and filter-sterilized) can be added to the
    medium to stimulate growth at the beginning.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "SL-11 staged preparation
    retained at main level", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml",
    "field_path": "preparation_steps[2].description", "original": "Dissolve EDTA in
    800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0 and bring volume to 1000 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml",
    "field_path": "preparation_steps[2].description", "original": "Dissolve EDTA in
    800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0 and bring volume to 1000 ml."}], "decision": "correct", "stage": "SL-11 only",
    "interpretation": "All numeric controls are already retained and source-supported:800
    mL initial water, pH7 using2 N NaOH, FeCl2 then other compounds, final pH6 and
    make-up to1000 mL. Move this existing exact procedure to its stock context rather
    than applying it to the completed medium.", "sources": [{"locator": "extracted-text
    physical LF lines 54-56", "source_key": "dsm815a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium815a.pdf",
    "source_raw_sha256": "cded9d02e288e08f601e05652fdbbf68d0b56805effed8f29035a3fcdbc80d90",
    "source_text_sha256": "d2ccf121bf51414db418da38d696adc82bb7837a8b82fadf6313304624819485",
    "accessed_at": "2026-10-28T18:56:02.531354Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[1].steps[0]", "source_key": "api815a", "reference":
    "https://mediadive.dsmz.de/rest/medium/815a", "source_raw_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "source_text_sha256": "0b5e53d7c8fc592dc060526af3207cb07ecf9b0f8c308e962c0811ae0e9b18dd",
    "accessed_at": "2026-10-28T18:56:02.531405Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch075/record05/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFOCELLA_HALOPHILA_MEDIUM.yaml: primary 22/23,
    secondary 21/23; data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml:
    primary 22/23, secondary 21/23. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs. CHEBI:64758 correctly denotes the supplied EDTA disodium dihydrate. The literal
    preferred spelling ''Na2-EDTA x 2 H2O'' is REJECTED in current CSV row 6338, while
    row 6339 maps the same local spelling as a synonym to the MAPPED preferred ''Na2EDTA·2H2O''
    (row 6372). This is a local-label mapping-status discrepancy, not a wrong-chemical-ID
    finding.'
  target_ids:
  - CultureMech:000283
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
  - CultureMech:000283
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
  - CultureMech:000283
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000283-sl11-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: SL-11 stock is represented as final-medium ingredients
  description: Nine SL-11 components remain in the same root list as the main recipe
    at full stock g/L; the separate stock, receiving 1 mL dose and solvent/final-volume
    controls are missing from structured formulation fields. Existing main ingredient
    rates agree with provider g_l and are credited, rather than being indiscriminately
    labelled conflicts.
  target_ids:
  - CultureMech:000283
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[2]
  evidence_ids:
  - dsm815a
  - api815a
  rule_id: review-yaml-record/source-stock-stage-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-000283-nickel-hydrate-and-sodium-resazurin-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin are linked to different supplied forms
  description: Every selected layer names nickel chloride hexahydrate but asserts
    anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium
    resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806;
    there is no asserted resazurin secondary slot to correct. Exact labels pass native
    checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms.
    Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.
  target_ids:
  - CultureMech:000283
  field_paths:
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  - ingredients[10].term
  evidence_ids:
  - dsm815a
  - chebi34887
  - chebi8806
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-000283-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported existing fields lack claim-level evidence
  description: Neither selected layer contains attached formulation claims. Current
    primary/provider agreement newly supports unchanged main amounts and preparation,
    while historical report objects are a separate population and do not authenticate
    old access dates.
  target_ids:
  - CultureMech:000283
  field_paths:
  - evidence
  - ingredients
  - preparation_steps
  evidence_ids:
  - history-auth
  - dsm815a
  - api815a
  rule_id: review-yaml-record/claim-evidence-placement
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Represent SL-11 as its exact source stock with positive 1000 mL make-up
    and 1 mL receiving dose. Move the supported stock procedure into that context,
    retain correct main recipe amounts and pH/procedure, and keep provider normalization
    explicitly qualified.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000283
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
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
  description: Resolve the exact source hydrate and sodium-salt identities against
    authoritative ontology and MIM records. Use verified supplied-form mappings or
    retain precise source labels with unresolved mapping; preserve source masses and
    do not substitute anhydrous molar arithmetic.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000283
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
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
  description: Attach precise ingredient or root evidence scoped to the exact source
    fields, including preparation and stock doses. Preserve existing source/history
    bytes and append verified current context; do not add evidence to unsupported
    SolutionDescriptor or PreparationStep slots.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000283
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocella_halophila_medium.yaml
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
- Provider main volume1001 mL and nominal g_l are not treated as independent measured
  final-volume evidence.
- Historical execution, dates and experimental performance are not authenticated;
  no different DSM815 source variant is transferred.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
