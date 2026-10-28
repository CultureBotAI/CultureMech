# Scientific review of desulfosalsimonas_medium

- Review: 20261028T212353Z-desulfosalsimonas-medium-batch078
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:57:57.729503Z
- Finished UTC: 2026-10-28T21:23:53.209524Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Eleven main provider rates and all retained main controls are supported. Three stocks remain flattened, their receiving doses and separate waters are missing, the SL-10 instruction is misplaced, and nickel hydrate/sodium resazurin use different-form identifiers. Reconstruct those bounded source scopes while retaining correct fields.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim, embedded source stocks and current writers.

Selection: Authoritative batch078 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000485 | data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml | generated | desulfosalsimonas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000485 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:000485 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:000485 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:000485 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact DSM1056 source and strain association

identity: supported. Targets: CultureMech:000485.

The selected target and sole maintained owner both identify DSM1056. Full two-page primary and current API agree on the main recipe and three embedded stocks. DSM17721 collection context identifies Desulfosalsimonas propionicica PropA and its association with this medium; it is not a new experimental growth assertion.

### Correct fields and classification retained

consistency: supported. Targets: CultureMech:000485.

Eleven main provider rates, pH 7.0–7.2, the main procedure, prior-to-use hydrogen control and optional dithionite note are supported and retained. COMPLEX, SEMI_DEFINED and LIQUID match yeast extract and the current provider category. The separate stock makeup is the remaining preparation-placement defect.

### Source forms and exact MIM interpretation

grounding: concern. Targets: CultureMech:000485.

Nickel hexahydrate is assigned anhydrous 34887, and sodium resazurin neutral 8806. Other source hydrates, sodium propionate, sodium carbonate, calcium pantothenate and vitamin-class assertions are supported within their exact scope. Preferred CoCl2 x 6 H2O is REJECTED while Cobalt chloride hexahydrate is MAPPED for correct 53503; preferred Na2SeO3 x 5 H2O is MAPPED, distinct from the REJECTED dotted spelling. These spelling-specific statuses do not imply a new chemical-ID defect. Vitamin B12 stays a class and lipoic acid has no newly asserted enantiomer.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:000485.

All three full historical reports and the exact 77-claim parent row were read. The cited API raw digest equals current API1056 and all 44 historical source objects match literally and decoded. Remaining local unresolved claims and zero-source-check reports are context, not attached source evidence. Current explicit main g_l support narrows older blanket topology conflicts; no attached formulation claims occur and current equality cannot authenticate historical dates/execution. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:000485.

All 66 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:000485", "selected_concentration_field_count": 66, "selected_concentration_fields_covered": 66, "decisions": [{"decision_id": "q1", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "59.8205", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "59.8205", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=59.8205 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NaCl                                                     60.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 60,\n                        \"unit\": \"g\",\n                        \"g_l\": 59.8205,\n                        \"mmol_l\": 1023.62,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "9.97009", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "9.97009", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=9.97009 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   MgSO4 x 7 H2O                                            10.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.97009,\n                        \"mmol_l\": 40.4506,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5.98205", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5.98205", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=5.98205 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 5-5", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   KCl                                                       6.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.98205,\n                        \"mmol_l\": 80.2422,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=0.398804 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 6-6", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   CaCl2 x 2 H2O                                             0.40        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 2.71267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.997009", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.997009", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=0.997009 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NH4Cl                                                     1.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 18.6392,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.0997009", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.0997009", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=0.0997009 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   KH2PO4                                                    0.10        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 0.732637,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=0.498504 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 9-9", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Yeast extract                                             0.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=0.000498504 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. The source resazurin reagent is explicitly 0.1% w/v and added as 0.5 ml.", "sources": [{"locator": "extracted-text physical LF lines 12-12", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Sodium resazurin (0.1% w/v)                               0.50       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[9]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "1.49551", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "1.49551", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=1.49551 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 13-13", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2CO3                                                    1.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 14.1102,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Na-propionate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "1.49551", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "1.49551", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=1.49551 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 14-14", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na-propionate                                             1.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na-propionate\",\n                        \"compound_id\": 301,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 15.5685,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider main-medium normalization", "interpretation": "Both current layers retain provider g_l=0.299103 on its nominal 1003 ml recipe basis. The primary batch input is separately quoted and its 1000 ml water does not establish measured final volume. Preserve the supported provider rate with precise attribution and staged preparation; no attached formulation claim exists. ", "sources": [{"locator": "extracted-text physical LF lines 16-16", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2S x 9 H2O                                              0.30        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[13]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.24532,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=2.5 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary gives 10 ml HCl (25%) without percentage basis or density; provider 2.5 g/L is not an independently derived pure-acid mass.", "sources": [{"locator": "extracted-text physical LF lines 35-35", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   HCl (25%)                                                10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=1.5 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 36-36", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   FeCl2 x 4 H2O                                             1.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.07 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 37-37", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   ZnCl2                                                    70.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.1 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 38-38", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   MnCl2 x 4 H2O                                           100.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.006 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 39-39", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   H3BO3                                                     6.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.19 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 40-40", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   CoCl2 x 6 H2O                                           190.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q18", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.002 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 41-41", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   CuCl2 x 2 H2O                                             2.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.024 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 42-42", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NiCl2 x 6 H2O                                            24.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q20", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution SL-10", "interpretation": "The exact source batch input and explicit provider g_l=0.036 belong only to Trace element solution SL-10. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The SL-10 procedure explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator": "extracted-text physical LF lines 43-43", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2MoO4 x 2 H2O                                          36.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q21", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Selenite-tungstate solution", "interpretation": "The exact source batch input and explicit provider g_l=0.5 belong only to Selenite-tungstate solution. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 60-60", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NaOH                                                       0.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Selenite-tungstate solution", "interpretation": "The exact source batch input and explicit provider g_l=0.003 belong only to Selenite-tungstate solution. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 61-61", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2SeO3 x 5 H2O                                            3.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Selenite-tungstate solution", "interpretation": "The exact source batch input and explicit provider g_l=0.004 belong only to Selenite-tungstate solution. They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 62-62", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2WO4 x 2 H2O                                             4.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.02 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 68-68", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Biotin                                                    20.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.02 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 69-69", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Folic acid                                                20.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.1 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 70-70", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Pyridoxine hydrochloride                                 100.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[2]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.05 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 71-71", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Thiamine HCl                                              50.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[3]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.05 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 72-72", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Riboflavin                                                50.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[4]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.05 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 73-73", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Nicotinic acid                                            50.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[5]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.05 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 74-74", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Calcium D-(+)-pantothenate                                50.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[6]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.001 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 75-75", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Vitamin B12                                                1.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[7]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.05 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 76-76", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   p-Aminobenzoic acid                                       50.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[8]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin's vitamin solution (10x)", "interpretation": "The exact source batch input and explicit provider g_l=0.05 belong only to Wolin's vitamin solution (10x). They are wrongly flattened into main ingredients in both layers. Restore separate stock scope and receiving addition without inventing a final-medium concentration. The primary lists 1000 ml stock water; provider stock normalization is credited but is not a measured final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines 77-77", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   (DL)-alpha-Lipoic acid                                    50.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[9]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "Missing Trace element solution SL-10 addition", "local_fields": [], "decision": "add", "stage": "main batch receiving stage", "interpretation": "The primary specifies 1 ml as a separate batch addition. Preserve its exact stock identity and amount without converting it silently to exactly 1 ml per final litre.", "sources": [{"locator": "extracted-text physical LF lines 10-10", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Trace element solution SL-10                              1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "Missing Selenite-tungstate solution addition", "local_fields": [], "decision": "add", "stage": "main batch receiving stage", "interpretation": "The primary specifies 1 ml as a separate batch addition. Preserve its exact stock identity and amount without converting it silently to exactly 1 ml per final litre.", "sources": [{"locator": "extracted-text physical LF lines 11-11", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Selenite-tungstate solution                               1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[8]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "Missing Wolin's vitamin solution (10x) addition", "local_fields": [], "decision": "add", "stage": "main batch receiving stage", "interpretation": "The primary specifies 1 ml as a separate batch addition. Preserve its exact stock identity and amount without converting it silently to exactly 1 ml per final litre.", "sources": [{"locator": "extracted-text physical LF lines 15-15", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Wolin's vitamin solution (10x)                            1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[12]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "Water for Main sol. 1056", "local_fields": [], "decision": "add", "stage": "separate water input", "interpretation": "Preserve this water input in its own batch. Stock water is not an additional receiving input. SL-10 separately has explicit make-up to 1000 ml; other water amounts do not independently establish final volume.", "sources": [{"locator": "extracted-text physical LF lines 17-17", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled water                                        1000.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[14]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "Water for Trace element solution SL-10", "local_fields": [], "decision": "add", "stage": "separate water input", "interpretation": "Preserve this water input in its own batch. Stock water is not an additional receiving input. SL-10 separately has explicit make-up to 1000 ml; other water amounts do not independently establish final volume.", "sources": [{"locator": "extracted-text physical LF lines 44-44", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled water                                         990.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "Water for Selenite-tungstate solution", "local_fields": [], "decision": "add", "stage": "separate water input", "interpretation": "Preserve this water input in its own batch. Stock water is not an additional receiving input. SL-10 separately has explicit make-up to 1000 ml; other water amounts do not independently establish final volume.", "sources": [{"locator": "extracted-text physical LF lines 63-63", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "Water for Wolin's vitamin solution (10x)", "local_fields": [], "decision": "add", "stage": "separate water input", "interpretation": "Preserve this water input in its own batch. Stock water is not an additional receiving input. SL-10 separately has explicit make-up to 1000 ml; other water amounts do not independently establish final volume.", "sources": [{"locator": "extracted-text physical LF lines 78-78", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[10]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "Main volume basis", "local_fields": [], "decision": "unsupported", "stage": "main final-volume claim", "interpretation": "The primary lists 1000 ml water plus three 1 ml stocks; API declares nominal 1003 ml and explicit g_l. Preserve provider attribution and do not infer a measured-final-volume assertion.", "sources": [{"locator": "extracted-text physical LF lines 10-17", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Trace element solution SL-10                              1.00       ml\n   Selenite-tungstate solution                               1.00       ml\n   Sodium resazurin (0.1% w/v)                               0.50       ml\n   Na2CO3                                                    1.50        g\n   Na-propionate                                             1.50        g\n   Wolin's vitamin solution (10x)                            1.00       ml\n   Na2S x 9 H2O                                              0.30        g\n   Distilled water                                        1000.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                \"id\": 2133,\n                \"name\": \"Main sol. 1056\",\n                \"volume\": 1003,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 60,\n                        \"unit\": \"g\",\n                        \"g_l\": 59.8205,\n                        \"mmol_l\": 1023.62,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.97009,\n                        \"mmol_l\": 40.4506,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.98205,\n                        \"mmol_l\": 80.2422,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 2.71267,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 18.6392,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 0.732637,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 14.1102,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na-propionate\",\n                        \"compound_id\": 301,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 15.5685,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.24532,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve ingredients (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0 - 7.2, if necessary.\"\n                    },\n                    {\n                        \"step\": \"Prior to use add sterile 100% H2 gas to 0.5 bar overpressure.\"\n                    },\n                    {\n                        \"step\": \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) can be used to completely reduce the medium and may stimulate growth at the beginning.\"\n                    }\n                ],\n                \"equipment\": {\n                    \"569\": \"Autoclave\",\n                    \"1412\": \"Hungate tubes\",\n                    \"2416\": \"Filter\",\n                    \"4098\": \"Gassing station\"\n                }\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "Retained main pH and preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0 - 7.2, if necessary."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0 - 7.2, if necessary."}], "decision": "evidence_only", "stage": "main staged procedure", "interpretation": "Both layers preserve pH 7.0–7.2 and the correct main procedure, including 80% N2/20% CO2 for 30–45 min, separate sterile stock additions under their stated gas mixtures, and vitamin filtration. Retain those stages; AUTOCLAVE is not a replacement for the separately filtered additions.", "sources": [{"locator": "extracted-text physical LF lines 19-25", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "1. Dissolve ingredients (except carbonate, propionate, vitamins and sulfide) and sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave. Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic\nstock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock\nsolution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete\nmedium to 7.0 - 7.2, if necessary.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0 - 7.2, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "Retained hydrogen control", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Prior to use add sterile 100% H2 gas to 0.5 bar overpressure."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Prior to use add sterile 100% H2 gas to 0.5 bar overpressure."}], "decision": "evidence_only", "stage": "prior-to-use control", "interpretation": "The existing 100% H2 and 0.5 bar overpressure instruction matches the primary exactly. Preserve it as a separate prior-to-use control, not a mass concentration or routine ingredient amount.", "sources": [{"locator": "extracted-text physical LF lines 26-26", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "2. Prior to use add sterile 100% H2 gas to 0.5 bar overpressure.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\": \"Prior to use add sterile 100% H2 gas to 0.5 bar overpressure.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "Retained optional dithionite note", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) can be used to completely reduce the medium and may stimulate growth at the beginning."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "preparation_steps[2].description", "original": "Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) can be used to completely reduce the medium and may stimulate growth at the beginning."}], "decision": "evidence_only", "stage": "optional separate reducing addition", "interpretation": "The source and existing note preserve optional 10–20 mg per litre from an example 5% w/v freshly prepared N2-protected, filter-sterilized stock. Do not turn this optional range/example stock into a required fixed ingredient or infer a stock addition volume beyond the stated source.", "sources": [{"locator": "extracted-text physical LF lines 27-29", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "3. Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution,\nfreshly prepared under N2 and filter-sterilized) can be used to completely reduce the\nmedium and may stimulate growth at the beginning.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[2]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\": \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) can be used to completely reduce the medium and may stimulate growth at the beginning.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "SL-10 makeup and sequence", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "preparation_steps[3].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path": "preparation_steps[3].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}], "decision": "correct", "stage": "stock preparation only", "interpretation": "The existing FeCl2/HCl dissolve and make-up-to-1000 ml instruction is correct for SL-10 but appears as main preparation_steps[3]. Relocate it to the distinct stock and preserve its exact numeric and procedural text.", "sources": [{"locator": "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].steps[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch078/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:000485.

data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml: primary 32/33, secondary 30/33; data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml: primary 32/33, secondary 30/33. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:000485.

Complete selected target and every exact maintained contributor reviewed. All stocks assessed here are embedded in the exact named DSM source. No external dependency or unrelated medium formulation transfers. Collection identity pages establish association only.

### Native structural checks

schema: supported. Targets: CultureMech:000485.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Three stocks are flattened and their receiving doses are missing

major / open / confirmed; issue key: culturemech-000485-stock-topology.

Twenty-two SL-10, selenite-tungstate and Wolin component rates occupy main ingredients11–32 in both layers. Three 1 ml batch additions and distinct stock/main water inputs are absent. Eleven supported main provider rates should remain.

### f2: The trace-stock makeup instruction is at main-medium scope

major / open / confirmed; issue key: culturemech-000485-stock-preparation.

preparation_steps[3] is the SL-10 FeCl2/HCl sequence and final stock make-up, not another main-medium preparation step. Main procedure and the two separate controls are correct.

### f3: Nickel hydrate and sodium resazurin are linked to different supplied forms

major / open / confirmed; issue key: culturemech-000485-nickel-hydrate-and-sodium-resazurin-form.

Every selected layer names nickel chloride hexahydrate but asserts anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806; there is no asserted resazurin secondary slot to correct. Exact labels pass native checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms. Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.

### f4: Claims lack attached excerpts and the current resolver emits naive timestamps

minor / open / confirmed; issue key: culturemech-000485-claim-provenance.

Historical raw-byte matches and current source pointers do not attach evidence to claims. The current resolver records a naive timestamp; its present behavior does not authenticate the stored historical event.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the three exact embedded stocks and separate 1 ml batch additions, preserving provider attribution and explicit SL-10 make-up. Keep HCl percentage basis unresolved; retain supported main rates and optional controls.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Move the exact retained stock instruction into SL-10 while preserving main pH, anoxic stages, hydrogen control and optional dithionite note.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the exact source hydrate and sodium-salt identities against authoritative ontology and MIM records. Use verified supplied-form mappings or retain precise source labels with unresolved mapping; preserve source masses and do not substitute anhydrous molar arithmetic.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Attach source evidence at valid scopes and preserve all original history. Correct future resolver timestamps to explicit UTC, adding verified actual-dated context rather than rewriting old events.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Future resolver timestamps must include a UTC offset; original historical strings and current source-access times remain distinct and preserved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch078/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch078/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch078/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch078/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm1056 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and all rendered pages read, including the main recipe, embedded stock tables and staged procedures. Physical LF locators refer to preserved pdftototext output; no page-wide or stock instruction is transferred to another stage. |
| api1056 | https://mediadive.dsmz.de/rest/medium/1056; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current provider identity, solution tables and preparation read. Explicit g_l and declared volumes are credited only on their named provider stock or recipe basis; they are not independent measured final volumes. Provider mmol_l values are not adopted as chemical-form authority. |
| dsm17721Identity | https://www.dsmz.de/collection/catalogue/details/culture/DSM-17721; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current official collection identity, strain synonyms, environmental isolation and exact medium association only. The page is not a recipe or a new experimental growth assertion. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W']; mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132106 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:132106; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:132106 = sodium propionate; definition ['An organic sodium salt comprising equal numbers of sodium and propionate ions.']; formula ['C3H5O2.Na']; mass ['96.061']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch078/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; No external dependency is included. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/desulfosalsimonas_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosalsimonas_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history-auth | REVIEW_WORK/batch078/record06/historical-authentication.json; attached_claims; historical_plan_claims | supports | Actual attached claims and historical parent-plan claims are separate populations. Current raw-digest equality and literal or normalized-HTML excerpt equality are independently recorded. No attached formulation claims occur on the selected target or its maintained contributors. Current byte matches do not authenticate historical execution or access dates. |
| historical-current-joins | REVIEW_WORK/batch078/record06/historical-current-joins.json; all selected parents and claims | supports | Exact selected historical parent rows, source raw digest and all literal/decoded source-object joins. These are separate from absent attached formulation evidence and do not authenticate historical dates. |
| writer47 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer48 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer49 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer50 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer51 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer52 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. No particular source range is authenticated by this writer. |
| writer53 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer54 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer55 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer56 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer57 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer58 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer59 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer60 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| quantity-inventory | REVIEW_WORK/batch078/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Provider nominal main volume 1003 ml and stock g_l remain provider assertions rather than measured-final-volume evidence. HCl 25% has no verified percentage basis or density.
- Optional dithionite remains optional; collection association does not establish a new growth experiment.
- Current source-byte equality does not authenticate historical execution or dates; no record or source edits were made.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T212353Z-desulfosalsimonas-medium-batch078
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfosalsimonas_medium
started_at: '2026-10-28T20:57:57.729503Z'
finished_at: '2026-10-28T21:23:53.209524Z'
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
summary: Eleven main provider rates and all retained main controls are supported.
  Three stocks remain flattened, their receiving doses and separate waters are missing,
  the SL-10 instruction is misplaced, and nickel hydrate/sodium resazurin use different-form
  identifiers. Reconstruct those bounded source scopes while retaining correct fields.
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
  - path: data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
    sha256: 46911839b3493f0a7e275d43ac93be3f4e0e149e1cdd63390ae352b5d0aa42bc
    role: target
  - path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    sha256: d134d68f4c2aa1c0f925ddf43058c8a338def0942bd9c00b7fce8847a3152f3c
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/desulfosalsimonas_medium.yaml.md
    sha256: d8e3738462a82805ecc7a546494d94a09af9e3db5bf1a123edbf863bdda3ff35
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.md
    sha256: 818fd623401585984ff3efef88defffd8c2f8116ab89abf92dce3526f9d0bc1e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosalsimonas_medium.md
    sha256: 10f6260705a2e7959acf8feff67ab3981a0647b34d6c37d593017f55730bcdb4
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
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
    claim, embedded source stocks and current writers.
  selection: Authoritative batch078 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000485
targets:
- target_id: CultureMech:000485
  path: data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
  label: desulfosalsimonas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000485
  command: just validate-schema data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000485
  command: just validate-strict data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch078/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:000485
  command: just validate-terms data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:000485
  command: just validate-references data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T21:05:45.052565Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 46911839b3493f0a7e275d43ac93be3f4e0e149e1cdd63390ae352b5d0aa42bc
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T21:05:45.052758Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: d134d68f4c2aa1c0f925ddf43058c8a338def0942bd9c00b7fce8847a3152f3c
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch078/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:57:58.831078Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: a57ea65885e2a92669aa235108ec13fe3c0a3d6c0b845763e579672a8eddd236
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch078/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:57:59.809810Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: fb3f3fea61811108e487c71226eaeaa5309249d2f7afc9b7b881da8a03d537b4
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch078/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:58:00.897521Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 4d82ed586f028c1d4e2dabbbf83dcafb035607f10cbc790ea26af753f595535f
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch078/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:58:01.681782Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: b5fffcdda2cfce92556b90ad98fcf13c80bd890a2bda5e46c28f336c2d8d5dac
- evidence_id: dsm1056
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:57:49.519040Z'
  support: supports
  summary: Complete exact DSM primary PDF text and all rendered pages read, including
    the main recipe, embedded stock tables and staged procedures. Physical LF locators
    refer to preserved pdftototext output; no page-wide or stock instruction is transferred
    to another stage.
  snapshot_sha256: 3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19
- evidence_id: api1056
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1056
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:57:49.519078Z'
  support: supports
  summary: Complete current provider identity, solution tables and preparation read.
    Explicit g_l and declared volumes are credited only on their named provider stock
    or recipe basis; they are not independent measured final volumes. Provider mmol_l
    values are not adopted as chemical-form authority.
  snapshot_sha256: 57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a
- evidence_id: dsm17721Identity
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-17721
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:57:50.384060Z'
  support: supports
  summary: Current official collection identity, strain synonyms, environmental isolation
    and exact medium association only. The page is not a recipe or a new experimental
    growth assertion.
  snapshot_sha256: 417a7675c4cf32b5532f56d0a79e54fc2a5cc8a7a971baf3429602607eaf9589
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:18.896332Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:18.896620Z'
  support: supports
  summary: OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic
    acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy
    group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:18.896704Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:18.896775Z'
  support: supports
  summary: OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic
    thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the
    5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:18.896835Z'
  support: supports
  summary: OLS current exact CHEBI:17015 = riboflavin; definition ['<small>D</small>-Ribitol
    in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:18.896878Z'
  support: supports
  summary: OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear
    parent hydride consisting of covalently bonded hydrogen and chlorine atoms.'];
    formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:19.628135Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:19.653114Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:19.661385Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:19.697139Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:19.760461Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:19.804930Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.231810Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.275424Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.334041Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.362660Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.419186Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.849805Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.879786Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.931497Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:20.936976Z'
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
  accessed_at: '2026-10-28T20:58:20.957833Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:21.027718Z'
  support: supports
  summary: OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen
    peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W'];
    mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:21.446979Z'
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
  accessed_at: '2026-10-28T20:58:21.561689Z'
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
  accessed_at: '2026-10-28T20:58:21.562858Z'
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
  accessed_at: '2026-10-28T20:58:21.569110Z'
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
  accessed_at: '2026-10-28T20:58:21.647139Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:22.118640Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:22.168972Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi132106
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:132106
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:22.244585Z'
  support: supports
  summary: OLS current exact CHEBI:132106 = sodium propionate; definition ['An organic
    sodium salt comprising equal numbers of sodium and propionate ions.']; formula
    ['C3H5O2.Na']; mass ['96.061']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: d3b82c73f0c2e39278ef715ec98ad323e3f0bec01062eca60f47c7715486ca0b
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:58:22.711906Z'
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
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch078/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T21:05:45.057146Z'
  support: supports
  summary: Complete selected term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; No external dependency is included.
    No fuzzy mapping or historical-validity inference.
  snapshot_sha256: b17ba83a8d2466b5e95641e1d0fa2325bcb7a701ce9103f0045bdcc0ca437e55
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/desulfosalsimonas_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T21:05:45.090719Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: d8e3738462a82805ecc7a546494d94a09af9e3db5bf1a123edbf863bdda3ff35
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T21:05:45.090748Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 818fd623401585984ff3efef88defffd8c2f8116ab89abf92dce3526f9d0bc1e
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosalsimonas_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T21:05:45.090777Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 10f6260705a2e7959acf8feff67ab3981a0647b34d6c37d593017f55730bcdb4
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch078/record06/historical-authentication.json
  locator: attached_claims; historical_plan_claims
  accessed_at: '2026-10-28T21:05:45.090977Z'
  support: supports
  summary: Actual attached claims and historical parent-plan claims are separate populations.
    Current raw-digest equality and literal or normalized-HTML excerpt equality are
    independently recorded. No attached formulation claims occur on the selected target
    or its maintained contributors. Current byte matches do not authenticate historical
    execution or access dates.
  snapshot_sha256: a5a53a7216121da59235e385015fbd634616345a3a177cc311548acafa6dbd54
- evidence_id: historical-current-joins
  kind: record_content
  reference: REVIEW_WORK/batch078/record06/historical-current-joins.json
  locator: all selected parents and claims
  accessed_at: '2026-10-28T21:05:45.091059Z'
  support: supports
  summary: Exact selected historical parent rows, source raw digest and all literal/decoded
    source-object joins. These are separate from absent attached formulation evidence
    and do not authenticate historical dates.
  snapshot_sha256: c4a470792cbbcd3b34a5335d28c8ccc801802c3a16b9ab2de32f9ae65475f397
- evidence_id: writer47
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T21:05:45.091132Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer48
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T21:05:45.091163Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer49
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T21:05:45.091189Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer50
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T21:05:45.091215Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer51
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T21:05:45.091247Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer52
  kind: record_content
  reference: scripts/migrate_ph_range.py
  locator: parse_ph_range; migrate_one
  accessed_at: '2026-10-28T21:05:45.091267Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. No particular source range
    is authenticated by this writer.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer53
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T21:05:45.091297Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer54
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T21:05:45.091333Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer55
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T21:05:45.091364Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer56
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T21:05:45.091394Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer57
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T21:05:45.091417Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer58
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T21:05:45.091445Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer59
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T21:05:45.091467Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer60
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T21:05:45.091489Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch078/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T21:05:45.128143Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: bd79ea879ebc29c1f4fd49f5eb107260df1f59a00d82caecac9cbaecacd8b98e
assessments:
- assessment_id: a1
  area: identity
  topic: Exact DSM1056 source and strain association
  outcome: supported
  summary: The selected target and sole maintained owner both identify DSM1056. Full
    two-page primary and current API agree on the main recipe and three embedded stocks.
    DSM17721 collection context identifies Desulfosalsimonas propionicica PropA and
    its association with this medium; it is not a new experimental growth assertion.
  target_ids:
  - CultureMech:000485
  evidence_ids:
  - local0
  - local1
  - dsm1056
  - api1056
  - dsm17721Identity
- assessment_id: a2
  area: consistency
  topic: Correct fields and classification retained
  outcome: supported
  summary: Eleven main provider rates, pH 7.0–7.2, the main procedure, prior-to-use
    hydrogen control and optional dithionite note are supported and retained. COMPLEX,
    SEMI_DEFINED and LIQUID match yeast extract and the current provider category.
    The separate stock makeup is the remaining preparation-placement defect.
  target_ids:
  - CultureMech:000485
  evidence_ids:
  - dsm1056
  - api1056
- assessment_id: a3
  area: grounding
  topic: Source forms and exact MIM interpretation
  outcome: concern
  summary: Nickel hexahydrate is assigned anhydrous 34887, and sodium resazurin neutral
    8806. Other source hydrates, sodium propionate, sodium carbonate, calcium pantothenate
    and vitamin-class assertions are supported within their exact scope. Preferred
    CoCl2 x 6 H2O is REJECTED while Cobalt chloride hexahydrate is MAPPED for correct
    53503; preferred Na2SeO3 x 5 H2O is MAPPED, distinct from the REJECTED dotted
    spelling. These spelling-specific statuses do not imply a new chemical-ID defect.
    Vitamin B12 stays a class and lipoic acid has no newly asserted enantiomer.
  target_ids:
  - CultureMech:000485
  evidence_ids:
  - grounding
  - chebi34887
  - chebi8806
  - chebi53503
  - chebi131361
  - chebi132106
  - chebi31345
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: All three full historical reports and the exact 77-claim parent row were
    read. The cited API raw digest equals current API1056 and all 44 historical source
    objects match literally and decoded. Remaining local unresolved claims and zero-source-check
    reports are context, not attached source evidence. Current explicit main g_l support
    narrows older blanket topology conflicts; no attached formulation claims occur
    and current equality cannot authenticate historical dates/execution. Current conservative
    merging preserves scientific fields and rejects incompatible formulations. Inspected
    writer behavior is described separately by exact file and function; it does not
    prove historical execution.
  target_ids:
  - CultureMech:000485
  evidence_ids:
  - history-auth
  - historical-current-joins
  - writer47
  - writer48
  - writer49
  - writer50
  - writer51
  - writer52
  - writer53
  - writer54
  - writer55
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 66 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:000485
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:000485",
    "selected_concentration_field_count": 66, "selected_concentration_fields_covered":
    66, "decisions": [{"decision_id": "q1", "subject": "NaCl", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "59.8205", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "59.8205",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=59.8205 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 3-3", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NaCl                                                     60.00        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 60,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 59.8205,\n                        \"mmol_l\":
    1023.62,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "9.97009", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "9.97009",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=9.97009 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   MgSO4
    x 7 H2O                                            10.00        g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.97009,\n                        \"mmol_l\":
    40.4506,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "5.98205", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "5.98205",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=5.98205 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 5-5", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   KCl                                                       6.00        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.98205,\n                        \"mmol_l\":
    80.2422,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "CaCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.398804",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=0.398804 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 6-6", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   CaCl2
    x 2 H2O                                             0.40        g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    2.71267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "NH4Cl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "0.997009", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.997009",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=0.997009 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 7-7", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NH4Cl                                                     1.00        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    18.6392,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.0997009", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.0997009",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=0.0997009 on its nominal 1003 ml recipe basis. The primary batch input is
    separately quoted and its 1000 ml water does not establish measured final volume.
    Preserve the supported provider rate with precise attribution and staged preparation;
    no attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 8-8", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   KH2PO4                                                    0.10        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    0.732637,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=0.498504 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 9-9", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Yeast
    extract                                             0.50        g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q8", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=0.000498504 on its nominal 1003 ml recipe basis. The primary batch input is
    separately quoted and its 1000 ml water does not establish measured final volume.
    Preserve the supported provider rate with precise attribution and staged preparation;
    no attached formulation claim exists. The source resazurin reagent is explicitly
    0.1% w/v and added as 0.5 ml.", "sources": [{"locator": "extracted-text physical
    LF lines 12-12", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Sodium
    resazurin (0.1% w/v)                               0.50       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[9]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q9", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "1.49551",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "1.49551",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=1.49551 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 13-13", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2CO3                                                    1.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[10]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\":
    14.1102,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "Na-propionate", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "original": {"value": "1.49551", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "1.49551",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=1.49551 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 14-14", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na-propionate                                             1.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[11]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na-propionate\",\n                        \"compound_id\":
    301,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\":
    15.5685,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "Na2S x 9 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM1056 provider
    main-medium normalization", "interpretation": "Both current layers retain provider
    g_l=0.299103 on its nominal 1003 ml recipe basis. The primary batch input is separately
    quoted and its 1000 ml water does not establish measured final volume. Preserve
    the supported provider rate with precise attribution and staged preparation; no
    attached formulation claim exists. ", "sources": [{"locator": "extracted-text
    physical LF lines 16-16", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2S x
    9 H2O                                              0.30        g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[13]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    1.24532,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution
    SL-10", "interpretation": "The exact source batch input and explicit provider
    g_l=2.5 belong only to Trace element solution SL-10. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary gives 10
    ml HCl (25%) without percentage basis or density; provider 2.5 g/L is not an independently
    derived pure-acid mass.", "sources": [{"locator": "extracted-text physical LF
    lines 35-35", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   HCl (25%)                                                10.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 54-55", "source_key": "dsm1056", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256":
    "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256":
    "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at":
    "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve FeCl2 in
    the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution
    SL-10", "interpretation": "The exact source batch input and explicit provider
    g_l=1.5 belong only to Trace element solution SL-10. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The SL-10 procedure explicitly
    makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator":
    "extracted-text physical LF lines 36-36", "source_key": "dsm1056", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256":
    "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256":
    "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at":
    "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   FeCl2 x 4 H2O                                             1.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[1]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q14", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution
    SL-10", "interpretation": "The exact source batch input and explicit provider
    g_l=0.07 belong only to Trace element solution SL-10. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The SL-10 procedure explicitly
    makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator":
    "extracted-text physical LF lines 37-37", "source_key": "dsm1056", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256":
    "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256":
    "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at":
    "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   ZnCl2                                                    70.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q15", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution
    SL-10", "interpretation": "The exact source batch input and explicit provider
    g_l=0.1 belong only to Trace element solution SL-10. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The SL-10 procedure explicitly
    makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator":
    "extracted-text physical LF lines 38-38", "source_key": "dsm1056", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256":
    "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256":
    "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at":
    "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   MnCl2 x 4 H2O                                           100.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q16", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element
    solution SL-10", "interpretation": "The exact source batch input and explicit
    provider g_l=0.006 belong only to Trace element solution SL-10. They are wrongly
    flattened into main ingredients in both layers. Restore separate stock scope and
    receiving addition without inventing a final-medium concentration. The SL-10 procedure
    explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources":
    [{"locator": "extracted-text physical LF lines 39-39", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   H3BO3                                                     6.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q17", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element solution
    SL-10", "interpretation": "The exact source batch input and explicit provider
    g_l=0.19 belong only to Trace element solution SL-10. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The SL-10 procedure explicitly
    makes up to 1000 ml, supporting this stock mass rate.", "sources": [{"locator":
    "extracted-text physical LF lines 40-40", "source_key": "dsm1056", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256":
    "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256":
    "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at":
    "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   CoCl2 x 6 H2O                                           190.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q18", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element
    solution SL-10", "interpretation": "The exact source batch input and explicit
    provider g_l=0.002 belong only to Trace element solution SL-10. They are wrongly
    flattened into main ingredients in both layers. Restore separate stock scope and
    receiving addition without inventing a final-medium concentration. The SL-10 procedure
    explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources":
    [{"locator": "extracted-text physical LF lines 41-41", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   CuCl2
    x 2 H2O                                             2.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q19", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element
    solution SL-10", "interpretation": "The exact source batch input and explicit
    provider g_l=0.024 belong only to Trace element solution SL-10. They are wrongly
    flattened into main ingredients in both layers. Restore separate stock scope and
    receiving addition without inventing a final-medium concentration. The SL-10 procedure
    explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources":
    [{"locator": "extracted-text physical LF lines 42-42", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NiCl2
    x 6 H2O                                            24.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q20", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Trace element
    solution SL-10", "interpretation": "The exact source batch input and explicit
    provider g_l=0.036 belong only to Trace element solution SL-10. They are wrongly
    flattened into main ingredients in both layers. Restore separate stock scope and
    receiving addition without inventing a final-medium concentration. The SL-10 procedure
    explicitly makes up to 1000 ml, supporting this stock mass rate.", "sources":
    [{"locator": "extracted-text physical LF lines 43-43", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2MoO4
    x 2 H2O                                          36.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q21", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Selenite-tungstate solution",
    "interpretation": "The exact source batch input and explicit provider g_l=0.5
    belong only to Selenite-tungstate solution. They are wrongly flattened into main
    ingredients in both layers. Restore separate stock scope and receiving addition
    without inventing a final-medium concentration. The primary lists 1000 ml stock
    water; provider stock normalization is credited but is not a measured final-volume
    claim.", "sources": [{"locator": "extracted-text physical LF lines 60-60", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   NaOH                                                       0.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "Na2SeO3 x 5 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Selenite-tungstate
    solution", "interpretation": "The exact source batch input and explicit provider
    g_l=0.003 belong only to Selenite-tungstate solution. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    61-61", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2SeO3
    x 5 H2O                                            3.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "Na2WO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Selenite-tungstate
    solution", "interpretation": "The exact source batch input and explicit provider
    g_l=0.004 belong only to Selenite-tungstate solution. They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    62-62", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Na2WO4
    x 2 H2O                                             4.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[2]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.02 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    68-68", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Biotin                                                    20.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.02 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    69-69", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Folic
    acid                                                20.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.1 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    70-70", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Pyridoxine
    hydrochloride                                 100.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[2]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.05 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    71-71", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Thiamine
    HCl                                              50.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[3]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.05 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    72-72", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Riboflavin                                                50.00       mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[4]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.05 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    73-73", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Nicotinic
    acid                                            50.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[5]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.05 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    74-74", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Calcium
    D-(+)-pantothenate                                50.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[6]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml", "field_path":
    "ingredients[30].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin
    solution (10x)", "interpretation": "The exact source batch input and explicit
    provider g_l=0.001 belong only to Wolin''s vitamin solution (10x). They are wrongly
    flattened into main ingredients in both layers. Restore separate stock scope and
    receiving addition without inventing a final-medium concentration. The primary
    lists 1000 ml stock water; provider stock normalization is credited but is not
    a measured final-volume claim.", "sources": [{"locator": "extracted-text physical
    LF lines 75-75", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Vitamin
    B12                                                1.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[7]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject":
    "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.05 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    76-76", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   p-Aminobenzoic
    acid                                       50.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[8]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "separate Wolin''s vitamin solution
    (10x)", "interpretation": "The exact source batch input and explicit provider
    g_l=0.05 belong only to Wolin''s vitamin solution (10x). They are wrongly flattened
    into main ingredients in both layers. Restore separate stock scope and receiving
    addition without inventing a final-medium concentration. The primary lists 1000
    ml stock water; provider stock normalization is credited but is not a measured
    final-volume claim.", "sources": [{"locator": "extracted-text physical LF lines
    77-77", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   (DL)-alpha-Lipoic
    acid                                    50.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[9]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "Missing Trace element
    solution SL-10 addition", "local_fields": [], "decision": "add", "stage": "main
    batch receiving stage", "interpretation": "The primary specifies 1 ml as a separate
    batch addition. Preserve its exact stock identity and amount without converting
    it silently to exactly 1 ml per final litre.", "sources": [{"locator": "extracted-text
    physical LF lines 10-10", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Trace
    element solution SL-10                              1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[7]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q35", "subject": "Missing Selenite-tungstate
    solution addition", "local_fields": [], "decision": "add", "stage": "main batch
    receiving stage", "interpretation": "The primary specifies 1 ml as a separate
    batch addition. Preserve its exact stock identity and amount without converting
    it silently to exactly 1 ml per final litre.", "sources": [{"locator": "extracted-text
    physical LF lines 11-11", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Selenite-tungstate
    solution                               1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[8]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "Missing Wolin''s vitamin
    solution (10x) addition", "local_fields": [], "decision": "add", "stage": "main
    batch receiving stage", "interpretation": "The primary specifies 1 ml as a separate
    batch addition. Preserve its exact stock identity and amount without converting
    it silently to exactly 1 ml per final litre.", "sources": [{"locator": "extracted-text
    physical LF lines 15-15", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Wolin''s
    vitamin solution (10x)                            1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[12]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q37", "subject": "Water for Main sol. 1056",
    "local_fields": [], "decision": "add", "stage": "separate water input", "interpretation":
    "Preserve this water input in its own batch. Stock water is not an additional
    receiving input. SL-10 separately has explicit make-up to 1000 ml; other water
    amounts do not independently establish final volume.", "sources": [{"locator":
    "extracted-text physical LF lines 17-17", "source_key": "dsm1056", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf", "source_raw_sha256":
    "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19", "source_text_sha256":
    "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560", "accessed_at":
    "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled water                                        1000.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[14]",
    "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q38", "subject": "Water for Trace element
    solution SL-10", "local_fields": [], "decision": "add", "stage": "separate water
    input", "interpretation": "Preserve this water input in its own batch. Stock water
    is not an additional receiving input. SL-10 separately has explicit make-up to
    1000 ml; other water amounts do not independently establish final volume.", "sources":
    [{"locator": "extracted-text physical LF lines 44-44", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled
    water                                         990.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q39", "subject": "Water for Selenite-tungstate
    solution", "local_fields": [], "decision": "add", "stage": "separate water input",
    "interpretation": "Preserve this water input in its own batch. Stock water is
    not an additional receiving input. SL-10 separately has explicit make-up to 1000
    ml; other water amounts do not independently establish final volume.", "sources":
    [{"locator": "extracted-text physical LF lines 63-63", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q40", "subject": "Water for Wolin''s vitamin
    solution (10x)", "local_fields": [], "decision": "add", "stage": "separate water
    input", "interpretation": "Preserve this water input in its own batch. Stock water
    is not an additional receiving input. SL-10 separately has explicit make-up to
    1000 ml; other water amounts do not independently establish final volume.", "sources":
    [{"locator": "extracted-text physical LF lines 78-78", "source_key": "dsm1056",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[10]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q41", "subject": "Main volume basis", "local_fields":
    [], "decision": "unsupported", "stage": "main final-volume claim", "interpretation":
    "The primary lists 1000 ml water plus three 1 ml stocks; API declares nominal
    1003 ml and explicit g_l. Preserve provider attribution and do not infer a measured-final-volume
    assertion.", "sources": [{"locator": "extracted-text physical LF lines 10-17",
    "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "   Trace
    element solution SL-10                              1.00       ml\n   Selenite-tungstate
    solution                               1.00       ml\n   Sodium resazurin (0.1%
    w/v)                               0.50       ml\n   Na2CO3                                                    1.50        g\n   Na-propionate                                             1.50        g\n   Wolin''s
    vitamin solution (10x)                            1.00       ml\n   Na2S x 9 H2O                                              0.30        g\n   Distilled
    water                                        1000.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0]", "source_key": "api1056",
    "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                \"id\":
    2133,\n                \"name\": \"Main sol. 1056\",\n                \"volume\":
    1003,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 60,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 59.8205,\n                        \"mmol_l\":
    1023.62,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.97009,\n                        \"mmol_l\":
    40.4506,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.98205,\n                        \"mmol_l\":
    80.2422,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    2.71267,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    18.6392,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    0.732637,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\":
    14.1102,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na-propionate\",\n                        \"compound_id\":
    301,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\":
    15.5685,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    1.24532,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Dissolve ingredients
    (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80%
    N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the
    complete medium to 7.0 - 7.2, if necessary.\"\n                    },\n                    {\n                        \"step\":
    \"Prior to use add sterile 100% H2 gas to 0.5 bar overpressure.\"\n                    },\n                    {\n                        \"step\":
    \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v)
    solution, freshly prepared under N2 and filter-sterilized) can be used to completely
    reduce the medium and may stimulate growth at the beginning.\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"569\": \"Autoclave\",\n                    \"1412\":
    \"Hungate tubes\",\n                    \"2416\": \"Filter\",\n                    \"4098\":
    \"Gassing station\"\n                }\n            }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q42", "subject": "Retained main pH and
    preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path":
    "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml", "field_path":
    "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients
    (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80%
    N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the
    complete medium to 7.0 - 7.2, if necessary."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients
    (except carbonate, propionate, vitamins and sulfide) and sparge medium with 80%
    N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the
    complete medium to 7.0 - 7.2, if necessary."}], "decision": "evidence_only", "stage":
    "main staged procedure", "interpretation": "Both layers preserve pH 7.0–7.2 and
    the correct main procedure, including 80% N2/20% CO2 for 30–45 min, separate sterile
    stock additions under their stated gas mixtures, and vitamin filtration. Retain
    those stages; AUTOCLAVE is not a replacement for the separately filtered additions.",
    "sources": [{"locator": "extracted-text physical LF lines 19-25", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "1. Dissolve
    ingredients (except carbonate, propionate, vitamins and sulfide) and sparge\nmedium
    with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense\nmedium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave.
    Add propionate, vitamins (sterilized by filtration) and sulfide from sterile anoxic\nstock
    solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock\nsolution
    prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete\nmedium
    to 7.0 - 7.2, if necessary.", "quote_representation": "captured extracted text"},
    {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1056", "reference":
    "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients (except carbonate, propionate, vitamins and sulfide) and
    sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add propionate, vitamins (sterilized by filtration) and sulfide
    from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from
    a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.
    Adjust pH of the complete medium to 7.0 - 7.2, if necessary.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject":
    "Retained hydrogen control", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Prior to use add
    sterile 100% H2 gas to 0.5 bar overpressure."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "Prior to use add
    sterile 100% H2 gas to 0.5 bar overpressure."}], "decision": "evidence_only",
    "stage": "prior-to-use control", "interpretation": "The existing 100% H2 and 0.5
    bar overpressure instruction matches the primary exactly. Preserve it as a separate
    prior-to-use control, not a mass concentration or routine ingredient amount.",
    "sources": [{"locator": "extracted-text physical LF lines 26-26", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "2. Prior
    to use add sterile 100% H2 gas to 0.5 bar overpressure.", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[1]", "source_key":
    "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\":
    \"Prior to use add sterile 100% H2 gas to 0.5 bar overpressure.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject":
    "Retained optional dithionite note", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "preparation_steps[2].description", "original": "Note: Addition
    of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly
    prepared under N2 and filter-sterilized) can be used to completely reduce the
    medium and may stimulate growth at the beginning."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "preparation_steps[2].description", "original": "Note: Addition
    of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly
    prepared under N2 and filter-sterilized) can be used to completely reduce the
    medium and may stimulate growth at the beginning."}], "decision": "evidence_only",
    "stage": "optional separate reducing addition", "interpretation": "The source
    and existing note preserve optional 10–20 mg per litre from an example 5% w/v
    freshly prepared N2-protected, filter-sterilized stock. Do not turn this optional
    range/example stock into a required fixed ingredient or infer a stock addition
    volume beyond the stated source.", "sources": [{"locator": "extracted-text physical
    LF lines 27-29", "source_key": "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "3. Note:
    Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution,\nfreshly
    prepared under N2 and filter-sterilized) can be used to completely reduce the\nmedium
    and may stimulate growth at the beginning.", "quote_representation": "captured
    extracted text"}, {"locator": "$.data.solutions[0].steps[2]", "source_key": "api1056",
    "reference": "https://mediadive.dsmz.de/rest/medium/1056", "source_raw_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "source_text_sha256":
    "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a", "accessed_at":
    "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v)
    solution, freshly prepared under N2 and filter-sterilized) can be used to completely
    reduce the medium and may stimulate growth at the beginning.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject":
    "SL-10 makeup and sequence", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml",
    "field_path": "preparation_steps[3].description", "original": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml",
    "field_path": "preparation_steps[3].description", "original": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}], "decision": "correct", "stage": "stock preparation
    only", "interpretation": "The existing FeCl2/HCl dissolve and make-up-to-1000
    ml instruction is correct for SL-10 but appears as main preparation_steps[3].
    Relocate it to the distinct stock and preserve its exact numeric and procedural
    text.", "sources": [{"locator": "extracted-text physical LF lines 54-55", "source_key":
    "dsm1056", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1056.pdf",
    "source_raw_sha256": "3c6286ba4bce7b6915a49d5bbe84cd95c2ec7c6dc4a604aff9bac8ca96f00b19",
    "source_text_sha256": "42fca98832a6f928a7a486970e44586a4b1d5655eb28323d9623bc9b7129e560",
    "accessed_at": "2026-10-28T20:57:49.519040Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[1].steps[0]", "source_key": "api1056", "reference": "https://mediadive.dsmz.de/rest/medium/1056",
    "source_raw_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "source_text_sha256": "57f0155c6d78820a58b104c620ae0d8c6fec481fbddb8245d89e1db395c3418a",
    "accessed_at": "2026-10-28T20:57:49.519078Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch078/record06/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFOSALSIMONAS_MEDIUM.yaml: primary 32/33, secondary
    30/33; data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml: primary 32/33,
    secondary 30/33. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric
    legacy MediaIngredientMech mentions occur across the complete selected documents,
    with exact locators in the inventory; NNNNNN is a historical placeholder, not
    an ID. Complex commercial/product components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:000485
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and every exact maintained contributor reviewed.
    All stocks assessed here are embedded in the exact named DSM source. No external
    dependency or unrelated medium formulation transfers. Collection identity pages
    establish association only.
  target_ids:
  - CultureMech:000485
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
  - CultureMech:000485
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000485-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Three stocks are flattened and their receiving doses are missing
  description: Twenty-two SL-10, selenite-tungstate and Wolin component rates occupy
    main ingredients11–32 in both layers. Three 1 ml batch additions and distinct
    stock/main water inputs are absent. Eleven supported main provider rates should
    remain.
  target_ids:
  - CultureMech:000485
  field_paths:
  - ingredients[11].concentration
  - ingredients[32].concentration
  - solutions
  evidence_ids:
  - dsm1056
  - api1056
  - quantity-inventory
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-000485-stock-preparation
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: The trace-stock makeup instruction is at main-medium scope
  description: preparation_steps[3] is the SL-10 FeCl2/HCl sequence and final stock
    make-up, not another main-medium preparation step. Main procedure and the two
    separate controls are correct.
  target_ids:
  - CultureMech:000485
  field_paths:
  - preparation_steps[3].description
  evidence_ids:
  - dsm1056
  - api1056
  rule_id: source-preparation-stage-placement
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-000485-nickel-hydrate-and-sodium-resazurin-form
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
  - CultureMech:000485
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - dsm1056
  - chebi34887
  - chebi8806
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-000485-claim-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Claims lack attached excerpts and the current resolver emits naive timestamps
  description: Historical raw-byte matches and current source pointers do not attach
    evidence to claims. The current resolver records a naive timestamp; its present
    behavior does not authenticate the stored historical event.
  target_ids:
  - CultureMech:000485
  field_paths:
  - ingredients[*]
  - preparation_steps
  - curation_history
  evidence_ids:
  - history-auth
  - historical-current-joins
  - writer47
  - writer48
  - writer49
  - writer50
  - writer51
  - writer52
  - writer53
  - writer54
  - writer55
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
  rule_id: claim-scoped-source-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
actions:
- action_id: action1
  description: Reconstruct the three exact embedded stocks and separate 1 ml batch
    additions, preserving provider attribution and explicit SL-10 make-up. Keep HCl
    percentage basis unresolved; retain supported main rates and optional controls.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
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
  description: Move the exact retained stock instruction into SL-10 while preserving
    main pH, anoxic stages, hydrogen control and optional dithionite note.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
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
  description: Resolve the exact source hydrate and sodium-salt identities against
    authoritative ontology and MIM records. Use verified supplied-form mappings or
    retain precise source labels with unresolved mapping; preserve source masses and
    do not substitute anhydrous molar arithmetic.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
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
  description: Attach source evidence at valid scopes and preserve all original history.
    Correct future resolver timestamps to explicit UTC, adding verified actual-dated
    context rather than rewriting old events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosalsimonas_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
  - Future resolver timestamps must include a UTC offset; original historical strings
    and current source-access times remain distinct and preserved.
limitations:
- Provider nominal main volume 1003 ml and stock g_l remain provider assertions rather
  than measured-final-volume evidence. HCl 25% has no verified percentage basis or
  density.
- Optional dithionite remains optional; collection association does not establish
  a new growth experiment.
- Current source-byte equality does not authenticate historical execution or dates;
  no record or source edits were made.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
