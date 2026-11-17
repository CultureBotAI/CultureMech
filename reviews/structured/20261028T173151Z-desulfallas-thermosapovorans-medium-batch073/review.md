# Scientific review of desulfallas_thermosapovorans_medium

- Review: 20261028T173151Z-desulfallas-thermosapovorans-medium-batch073
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T17:16:31.365505Z
- Finished UTC: 2026-10-28T17:31:51.685684Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated record mixes A-stage and stock concentrations and retains a stale NaOH sum. Both normalized owners already repaired the numeric sum, but the two different NaOH stock inputs still require separate representation. Existing target/DSM preparation and pH are supported; KOMODO atmosphere/preparation and nickel/resazurin form mappings need curation.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch073 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001808 | data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml | generated | desulfallas_thermosapovorans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001808 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:001808 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:001808 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:001808 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Maintained source branches and current repairs

identity: concern. Targets: CultureMech:001808.

Both maintained owners resolve to DSM667, with historical KOMODO mapping supporting the shared accession but current exact KOMODO access unavailable. The DSM contributor and target retain source preparation; the KOMODO contributor does not. Both owners have already repaired the identical-number NaOH sum while the generated target remains stale. These source-duplicate candidates are not currently equal full formulations.

### Other chemical forms and complex components

grounding: supported. Targets: CultureMech:001808.

Current OLS supports the other asserted source forms, including sodium carbonate, acetate and butyrate. Source D-calcium pantothenate is compatible with the current OLS31345 D-calcium synonyms and salt formula; vitamin B12 remains the source generic class and lipoic acid remains racemic/generic. Yeast extract is not forced to a pure chemical identifier. Exact MIM dictionary membership is distinct from authority for a source-specific form.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:001808.

Five full reports and the two exact selected plan rows were read. The existing normalized NaOH repair is credited separately from the stale generated value and the unresolved multi-stock scientific problem. Current import/cleanup/merge behavior is scoped to the actual functions read. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:001808.

All 108 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001808", "selected_concentration_field_count": 108, "selected_concentration_fields_covered": 108, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.08325", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.08325", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.08325", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=3.08325 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.08325,\n                        \"mmol_l\": 21.7069,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 26-26", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2SO4                                                   3.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.20555", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.20555", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.20555", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.20555 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.20555,\n                        \"mmol_l\": 1.51045,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 27-27", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   KH2PO4                                                   0.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.02775", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.02775", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.02775", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=1.02775 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.02775,\n                        \"mmol_l\": 19.2139,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 28-28", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NH4Cl                                                    1.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "8.22199", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "8.22199", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "8.22199", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=8.22199 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8.22199,\n                        \"mmol_l\": 140.691,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 29-29", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NaCl                                                     8.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.4111", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.4111", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.4111", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.4111 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4111,\n                        \"mmol_l\": 2.0221,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 30-30", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   MgCl2 x 6 H2O                                            0.40        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.513875", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.513875", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.513875", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.513875 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.513875,\n                        \"mmol_l\": 6.89302,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 31-31", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   KCl                                                      0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.154162", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.154162", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.154162", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.154162 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.154162,\n                        \"mmol_l\": 1.04862,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 32-32", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   CaCl2 x 2 H2O                                            0.15        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Na-acetate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.513875", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.513875", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.513875", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.513875 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[9]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.513875,\n                        \"mmol_l\": 6.26418,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 35-35", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na-acetate                                               0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Na-butyrate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "2.26105", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "2.26105", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "2.26105", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=2.26105 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[10]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na-butyrate\",\n                        \"compound_id\": 232,\n                        \"amount\": 2.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.26105,\n                        \"mmol_l\": 20.5387,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 36-36", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na-butyrate                                              2.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.4111", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.4111", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.4111", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.4111 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator": "$.data.solutions[1].recipe[11]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4111,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 37-37", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Yeast extract                                            0.40        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.000513875", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.000513875", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.000513875", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation": "The current API explicitly supplies g_l=0.000513875 for Solution A. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These A-stage rates use provider volume 973 ml. The complete primary medium explicitly has final volume 1010 ml; do not equate the two bases. Sodium resazurin is explicitly 0.5 ml of a 0.1% w/v stock added to A; retain that dose and strength.", "sources": [{"locator": "$.data.solutions[1].recipe[12]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000513875,\n                        \"mmol_l\": 0.00204592,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 38-38", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Sodium resazurin (0.1% w/v)                              0.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution B", "interpretation": "The current API explicitly supplies g_l=50 for Solution B. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 44-44", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2CO3                                                   1.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution D", "interpretation": "The current API explicitly supplies g_l=40 for Solution D. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose.", "sources": [{"locator": "$.data.solutions[4].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\": 166.54,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 62-62", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2S x 9 H2O                                                0.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=2.5 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. Primary HCl is 10 ml of 25% solution with no percentage basis or density; g_l=2.5 remains provider output, not an independently proven mass conversion.", "sources": [{"locator": "$.data.solutions[6].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 73-73", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   HCl (25%)                                                  10.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=1.5 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 74-74", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   FeCl2 x 4 H2O                                               1.50       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.07 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 75-75", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   ZnCl2                                                      70.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.1 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 76-76", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   MnCl2 x 4 H2O                                             100.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q18", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.006 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[4]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 77-77", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   H3BO3                                                       6.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.19 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[5]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 78-78", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   CoCl2 x 6 H2O                                             190.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q20", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.002 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[6]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   CuCl2 x 2 H2O                                               2.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q21", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.024 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[7]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 80-80", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NiCl2 x 6 H2O                                              24.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q22", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10", "interpretation": "The current API explicitly supplies g_l=0.036 for Trace element solution SL-10. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[8]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 81-81", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2MoO4 x 2 H2O                                            36.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Selenite-tungstate solution", "interpretation": "The current API explicitly supplies g_l=0.003 for Selenite-tungstate solution. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose.", "sources": [{"locator": "$.data.solutions[7].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 91-91", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2SeO3 x 5 H2O                                            3.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Selenite-tungstate solution", "interpretation": "The current API explicitly supplies g_l=0.004 for Selenite-tungstate solution. This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose.", "sources": [{"locator": "$.data.solutions[7].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 92-92", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2WO4 x 2 H2O                                             4.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q25", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.02 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 98-98", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Biotin                                                     20.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q26", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.02 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 99-99", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Folic acid                                                 20.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q27", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.1 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 100-100", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Pyridoxine hydrochloride                                  100.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q28", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 101-101", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Thiamine HCl                                               50.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q29", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[4]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 102-102", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Riboflavin                                                 50.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[5]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 103-103", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Nicotinic acid                                             50.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q31", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[6]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 104-104", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Calcium D-(+)-pantothenate                                 50.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q32", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.001 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[7]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 105-105", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Vitamin B12                                                 1.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q33", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[8]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 106-106", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   p-Aminobenzoic acid                                        50.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q34", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[34].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin's vitamin solution (10x)", "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin's vitamin solution (10x). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml listed water, not the entire quantity added to the medium.", "sources": [{"locator": "$.data.solutions[8].recipe[9]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 114-114", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   (DL)-alpha-Lipoic acid                                  50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q35", "subject": "Na2S2O4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[35].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Na-dithionite solution (5% w/v)", "interpretation": "The current API explicitly supplies g_l=50 for Na-dithionite solution (5% w/v). This supports that stage's provider rate, not the current undifferentiated final-medium ingredient rate. Preserve the exact source amount/form, stock structure and receiving dose. The explicit source 5% w/v designation supports 50 g/L at dithionite-stock scope only.", "sources": [{"locator": "$.data.solutions[9].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2S2O4\",\n                        \"compound_id\": 653,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 287.175,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 121-121", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2S2O4                                                   0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q36", "subject": "NaOH amounts conflated across two stocks", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "1.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ingredients[22].notes", "original": " [Merged 2 duplicates: 0.5, 0.5]"}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ingredients[22].notes", "original": "[Collapsed 2 identical duplicates: 0.5, 0.5]"}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ingredients[22].notes", "original": "[Collapsed 2 identical duplicates: 0.5, 0.5]"}], "decision": "conflict", "stage": "Selenite-tungstate mass versus dithionite normal solution", "interpretation": "The generated target retains a historical sum 1.0 G_PER_L from two equal numeric 0.5 values. Both maintained owners already collapse it to 0.5 and retain the repair event; credit that correction. Neither flat value represents the source topology: Se/W uses 0.5 g NaOH with 1000 ml water, while dithionite uses 0.5 ml of 1 N NaOH with 9.5 ml water. These are different dimensions and stages and must be represented separately, not summed or collapsed merely because their numbers match.", "sources": [{"locator": "$.data.solutions[7].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 90-90", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NaOH                                                       0.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"1 N\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 120-120", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NaOH (1 N)                                                0.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject": "Solution A", "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1405,\n                        \"amount\": 973,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution A                                             973.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q38", "subject": "Solution B", "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1406,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution B                                              30.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q39", "subject": "Solution C", "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1407,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 9-9", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution C                                               1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q40", "subject": "Solution D", "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1408,\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-10", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution D                                               5.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q41", "subject": "Solution E", "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 1409,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 11-11", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution E                                               1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q42", "subject": "Trace element solution SL-10", "local_fields": [], "decision": "add", "stage": "Solution A", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 33-33", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Trace element solution SL-10                             1.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q43", "subject": "Selenite-tungstate solution", "local_fields": [], "decision": "add", "stage": "Solution A", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Selenite-tungstate solution                              1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q44", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Solution A", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[1].recipe[13]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 970,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 39-39", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                        970.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q45", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Solution B", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 45-45", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                         30.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q46", "subject": "Wolin's vitamin solution (10x)", "local_fields": [], "decision": "add", "stage": "Solution C", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 57-57", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Wolin's vitamin solution (10x)                              1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q47", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Solution D", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[4].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 63-63", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                             5.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q48", "subject": "Na-dithionite solution (5% w/v)", "local_fields": [], "decision": "add", "stage": "Solution E", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[5].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Na-dithionite solution (5% w/v)\",\n                        \"solution_id\": 6262,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 68-68", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na-dithionite solution (5% w/v)                             1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q49", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Trace element solution SL-10", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[6].recipe[9]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                           990.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q50", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Selenite-tungstate solution", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[7].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 93-93", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q51", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Wolin's vitamin solution (10x)", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[8].recipe[10]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 115-115", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                       1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q52", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Na-dithionite solution (5% w/v)", "interpretation": "Retain this exact source stock link, receiving dose or solvent input at its own stage. The main A–E doses are absolute batch inputs into the explicitly declared 1010 ml final medium; nested stock batches are not final-medium amounts.", "sources": [{"locator": "$.data.solutions[9].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 9.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 122-122", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled water                                           9.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q53", "subject": "Explicit final medium volume", "local_fields": [], "decision": "add", "stage": "Completed A–E medium", "interpretation": "The primary explicitly states final volume 1010 ml. The printed A–E additions sum exactly: 973 + 30 + 1 + 5 + 1 = 1010 ml. This positive final-volume support is distinct from the separate A-stage normalization and from stock-water listings.", "sources": [{"locator": "extracted-text physical LF lines 3-11", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Final pH: 7.0 - 7.2\nFinal volume: 1010 ml\n\n\n   Solution A                                             973.00       ml\n   Solution B                                              30.00       ml\n   Solution C                                               1.00       ml\n   Solution D                                               5.00       ml\n   Solution E                                               1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q54", "subject": "Retained preparation step 1", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and sterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution E  is prepared under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of solutions B to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.0 - 7.2."}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and sterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution E  is prepared under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of solutions B to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.0 - 7.2."}], "decision": "evidence_only", "stage": "Existing stage-specific preparation", "interpretation": "The generated target and DSM owner already preserve 80% N2/20% CO2 sparging to pH below 6 for at least 30 min, separate A/B autoclaving, C/D 100% N2 and E 80/20 scopes, filtration for C/E, ordered additions and final pH 7.0–7.2. Preserve that prose with exact source evidence. The KOMODO owner lacks it. No main autoclave time/temperature is specified here.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\": \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and sterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution E  is prepared under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of solutions B to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.0 - 7.2.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 13-20", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at\nleast 30 min), then distributed under same gas atmosphere into anoxic Hungate-type\ntubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2\nand 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and\nsterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution E is prepared\nunder 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete the\nmedium appropriate amounts of solutions B to E are added to the sterile solution A in the\nsequence as indicated. Final pH of the medium should be at 7.0 - 7.2.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q55", "subject": "Retained preparation step 2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "preparation_steps[1].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}], "decision": "evidence_only", "stage": "Existing stage-specific preparation", "interpretation": "The retained SL-10 preparation correctly states sequential dissolution and final make-up to 1000 ml. Keep it scoped to SL-10, not main-medium final volume.", "sources": [{"locator": "$.data.solutions[6].steps[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 84-85", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q56", "subject": "Retained preparation step 3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "Add 1 N NaOH to distilled water and make the solution anoxic by sparging with 100% N2 gas. Then dissolve the Na-dithionite and filter-sterilize the solution into anoxic Hungate tubes. The final pH of the solution should be between 9 and 10. Store the prepared solution in a dark and cool place. Prepare only small amounts of stock solution, as Na-dithionite decomposes rapidly."}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "preparation_steps[2].description", "original": "Add 1 N NaOH to distilled water and make the solution anoxic by sparging with 100% N2 gas. Then dissolve the Na-dithionite and filter-sterilize the solution into anoxic Hungate tubes. The final pH of the solution should be between 9 and 10. Store the prepared solution in a dark and cool place. Prepare only small amounts of stock solution, as Na-dithionite decomposes rapidly."}], "decision": "evidence_only", "stage": "Existing stage-specific preparation", "interpretation": "The retained dithionite preparation correctly uses 1 N NaOH, 100% N2/filter sterilization and stock pH 9–10. Preserve this evidence and distinguish it from final-medium pH; dark/cool storage has no numerical temperature here.", "sources": [{"locator": "$.data.solutions[9].steps[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\": \"Add 1 N NaOH to distilled water and make the solution anoxic by sparging with 100% N2 gas. Then dissolve the Na-dithionite and filter-sterilize the solution into anoxic Hungate tubes. The final pH of the solution should be between 9 and 10. Store the prepared solution in a dark and cool place. Prepare only small amounts of stock solution, as Na-dithionite decomposes rapidly.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 124-128", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Add 1 N NaOH to distilled water and make the solution anoxic by sparging with 100% N2\ngas. Then dissolve the Na-dithionite and filter-sterilize the solution into anoxic Hungate\ntubes. The final pH of the solution should be between 9 and 10. Store the prepared\nsolution in a dark and cool place. Prepare only small amounts of stock solution, as Na\n-dithionite decomposes rapidly.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q57", "subject": "Final pH range", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}], "decision": "evidence_only", "stage": "Completed medium", "interpretation": "All three layers retain source-supported final pH 7.0–7.2; this is separate from the initial A-stage pH below 6 and dithionite-stock pH 9–10.", "sources": [{"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Final pH: 7.0 - 7.2", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\": \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and sterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution E  is prepared under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of solutions B to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.0 - 7.2.\"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch073/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:001808.

data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml: primary 35/36, secondary 33/36; data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml: primary 35/36, secondary 33/36; data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml: primary 35/36, secondary 33/36. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:001808.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:001808.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Source A–E assembly is flattened into mixed-stage concentrations

major / open / confirmed; issue key: culturemech-001808-assembly-and-stock-topology.

Eleven A-stage rates based on 973 ml and multiple stock-strength rates are represented as undifferentiated main ingredients despite the primary explicit 1010 ml final medium. All receiving doses, stock solvents and nested structures are absent. The HCl 25% provider conversion does not establish an unqualified mass basis.

### f2: Generated NaOH sum is stale and the owner collapse still loses stock identity

major / open / confirmed; issue key: culturemech-001808-stale-naoh-and-conflated-stages.

The generated target retains 1.0 G_PER_L, whereas both maintained owners already carry 0.5 G_PER_L after the recorded identical-duplicate repair. Credit the repaired owner state, but neither representation separates 0.5 g NaOH in Se/W from 0.5 ml of 1 N NaOH in dithionite stock. Current cleanup and duplicate-repair functions cannot establish those chemical stages.

### f3: KOMODO preparation and atmosphere diverge from the retained primary procedure

major / open / confirmed; issue key: culturemech-001808-owner-preparation-divergence.

The target and DSM owner already preserve three preparation descriptions and correct final pH. Only the KOMODO owner lacks those descriptions and says Aerobic: Yes, contradicting the primary anaerobic procedure. The current merger rejects incompatible scientific projections; do not treat the existing duplicate relationship as permission to discard preparation.

### f4: Nickel hydrate and sodium resazurin are linked to different supplied forms

major / open / confirmed; issue key: culturemech-001808-nickel-hydrate-and-sodium-resazurin-form.

Every selected layer names nickel chloride hexahydrate but asserts anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806; there is no asserted resazurin secondary slot to correct. Exact labels pass native checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms. Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.

### f5: Evidence and historical timestamps need bounded curation

minor / open / confirmed; issue key: culturemech-001808-append-only-provenance.

No current layer contains attached formulation claims. Both maintained owners retain a September duplicate-repair event omitted from the older generated target. Historical full-report/API matches support only their exact current objects; separately cited KOMODO catalogue bytes and old execution remain unverified. The KOMODO owner also retains literal .fZ and offset-less timestamps.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the exact A–E assembly and embedded stocks; preserve supplied chemical forms, explicit 1010 ml final volume and stage-specific source inputs. Use provider rates only within their declared stage; do not independently convert bare HCl percentage to mass without a supported basis.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve existing repair provenance and reconstruct the two distinct NaOH stock inputs before regenerating. Do not merely replace the generated sum with a single owner value or reinterpret 1 N liquid volume as mass.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Preserve all supported target/DSM preparation and correct only the incomplete KOMODO source context. Review duplicate relationships and regenerate conservatively from reconciled owners.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve the exact source hydrate and sodium-salt identities against authoritative ontology and MIM records. Use verified supplied-form mappings or retain precise source labels with unresolved mapping; preserve source masses and do not substitute anhydrous molar arithmetic.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Attach claim-scoped fresh evidence and append a verified current event, preserving all historical bytes and the existing duplicate-repair record. Correct future timestamps in the exact inspected writers without rewriting historical dates.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Verify future importer/enrichment events use actual UTC with timezone, and existing repair and malformed historical events remain unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch073/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch073/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch073/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch073/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132194 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132194; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | context_only | Excluded candidate lead: current OLS identifies CHEBI:132194 as glycine-d5. It is unrelated to sodium resazurin and supplies no replacement mapping. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state), chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W']; mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi66870 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_66870; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:66870 = sodium dithionite; definition ['An inorganic sodium salt that is the disodium salt of dithionous acid.']; formula ['2Na.O4S2']; mass ['174.11']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| dsm667 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api667 | https://mediadive.dsmz.de/api/medium/667; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 404, error &lt;HTTPError 404: 'Not Found'&gt;. This response does not authenticate a recipe. |
| komodo667 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=667; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32954 = sodium acetate; definition []; formula ['C2H3O2.Na']; mass ['82.034']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi64103 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:64103 = sodium butyrate; definition ['An organic sodium salt resulting from the replacement of the proton from the carboxy group of butyric acid by a sodium ion.']; formula ['C4H7O2.Na']; mass ['110.088']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| api667Rest | https://mediadive.dsmz.de/rest/medium/667; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| grounding | REVIEW_WORK/batch073/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfallas_thermosapovorans_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api667Rest raw bytes exactly match the cited historical SHA, and 56 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/desulfotomaculum_thermosapovorans_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api667Rest raw bytes exactly match the cited historical SHA, and 56 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history-auth | REVIEW_WORK/batch073/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer55 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer56 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer57 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer58 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer59 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer60 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer61 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer62 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer63 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| quantity-inventory | REVIEW_WORK/batch073/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact historical KOMODO MediaInfo=667 returned HTTP 403; current primary/API evidence does not authenticate historical catalogue bytes or execution times.
- The source explicitly states final 1010 ml, and its A–E doses sum to that value; A-stage 973 ml rates are not final-medium rates.
- HCl 25% has no explicit percentage basis/density. No independent mass conversion or exact sodium-resazurin replacement is invented.
- The repeated 0.5 NaOH values have different dimensions and stock contexts. The owner duplicate collapse is credited but is not a complete scientific repair.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T173151Z-desulfallas-thermosapovorans-medium-batch073
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfallas_thermosapovorans_medium
started_at: '2026-10-28T17:16:31.365505Z'
finished_at: '2026-10-28T17:31:51.685684Z'
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
summary: The generated record mixes A-stage and stock concentrations and retains a
  stale NaOH sum. Both normalized owners already repaired the numeric sum, but the
  two different NaOH stock inputs still require separate representation. Existing
  target/DSM preparation and pH are supported; KOMODO atmosphere/preparation and nickel/resazurin
  form mappings need curation.
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
  - path: data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
    sha256: 440f15bfa91a22e037414ff956bb28bc35e3970d1dd424a25cb5b6277061cea9
    role: target
  - path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    sha256: 132f72bc5b58acabe58483f7c7bd09fb51d5d99733d179f81e50f7a5088a1f21
    role: context
  - path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    sha256: d256eacdb9dfb8675894ace71588ccb2beb8bc55930679bf0aafa0d3b009e70d
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/desulfotomaculum_thermosapovorans_medium.yaml.md
    sha256: 95377c9439e401878fb907d8142a3d8c6fdba3f02e2c8de2242b4182f0326956
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfallas_thermosapovorans_medium.yaml.md
    sha256: e8deb2741637a6e06d224380bc00acd0c3ebc4fecea505c4140b3d9c0758cdd0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.md
    sha256: b4ae44ad26519a2306851552d7292585ac6e31e51f95df80131410dbe46281d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.md
    sha256: 7d1ad69b6ae1d85b50402a8c504c1570047f149105c0aab34f21eb34ac0819a9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.md
    sha256: 24af9bd74476d2e824202e35b4667fef917255c3de81c1b2d9d5b66f2bea1645
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
  selection: Authoritative batch073 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001808
targets:
- target_id: CultureMech:001808
  path: data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
  label: desulfallas_thermosapovorans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001808
  command: just validate-schema data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001808
  command: just validate-strict data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch073/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001808
  command: just validate-terms data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:001808
  command: just validate-references data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T17:31:51.553332Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 440f15bfa91a22e037414ff956bb28bc35e3970d1dd424a25cb5b6277061cea9
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T17:31:51.553656Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 132f72bc5b58acabe58483f7c7bd09fb51d5d99733d179f81e50f7a5088a1f21
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T17:31:51.553715Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: d256eacdb9dfb8675894ace71588ccb2beb8bc55930679bf0aafa0d3b009e70d
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch073/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:32.430343Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 96824508cd9db7202a5d1fe3bdef906ddd3a7ef41bd117df5ada95be7906390c
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch073/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:33.351262Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: ac18b600fc960d6e84df4af54b0dea4901e7d1c0997bb700fda43dd6a9372742
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch073/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:34.363148Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: d6df5206fd305957cf240800597ce86d1778bf6deb9e4d4cd0f929ecfc951cfe
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch073/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:35.120119Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 9d52c56c8b796097688bee97b0d5c33e4dfd552665bf8e6a50ac0eb82079c58e
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:09.159827Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi132194
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132194
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:09.159865Z'
  support: context_only
  summary: 'Excluded candidate lead: current OLS identifies CHEBI:132194 as glycine-d5.
    It is unrelated to sodium resazurin and supplies no replacement mapping.'
  snapshot_sha256: b3ced33b9c7d461521c275844c95f4d5a9dda3689e0d4bb2971f32ac875898d1
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:09.159898Z'
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
  accessed_at: '2026-10-28T17:17:09.917327Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:09.919460Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:10.031619Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:10.223422Z'
  support: supports
  summary: OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula
    ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:10.375739Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:10.508449Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:10.524294Z'
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
  accessed_at: '2026-10-28T17:17:10.530481Z'
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
  accessed_at: '2026-10-28T17:17:10.733820Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:10.859552Z'
  support: supports
  summary: OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition
    ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state),
    chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass
    ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:11.061078Z'
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
  accessed_at: '2026-10-28T17:17:11.104876Z'
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
  accessed_at: '2026-10-28T17:17:11.206470Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:11.330235Z'
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
  accessed_at: '2026-10-28T17:17:11.493702Z'
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
  accessed_at: '2026-10-28T17:17:11.657659Z'
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
  accessed_at: '2026-10-28T17:17:11.694624Z'
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
  accessed_at: '2026-10-28T17:17:11.796774Z'
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
  accessed_at: '2026-10-28T17:17:11.807584Z'
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
  accessed_at: '2026-10-28T17:17:11.929773Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:12.415758Z'
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
  accessed_at: '2026-10-28T17:17:12.455005Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:12.936762Z'
  support: supports
  summary: OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic
    thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the
    5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:13.012254Z'
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
  accessed_at: '2026-10-28T17:17:13.020393Z'
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
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:13.100591Z'
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
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:13.187414Z'
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
  accessed_at: '2026-10-28T17:17:13.277362Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:13.554889Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:13.611383Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi66870
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_66870
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:13.746936Z'
  support: supports
  summary: OLS current exact CHEBI:66870 = sodium dithionite; definition ['An inorganic
    sodium salt that is the disodium salt of dithionous acid.']; formula ['2Na.O4S2'];
    mass ['174.11']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 4abd307c08e644fc9ec8bd5dfd2787bcb6a7bde25890e6a5eeb0a177e76216ed
- evidence_id: dsm667
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:13.756864Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c
- evidence_id: api667
  kind: database
  reference: https://mediadive.dsmz.de/api/medium/667
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:13.881206Z'
  support: unknown
  summary: 'Actual retrieval HTTP 404, error <HTTPError 404: ''Not Found''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 3f9685b5e0f7b66ddb1d45605efcc429ca2abe8711a24a34aeccff75445a2eac
- evidence_id: komodo667
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=667
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:13.960339Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 04b9e45c62b4d596d64d0a8f5228fea7d1daaab7be8faedb54cb922d842033af
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:14.084147Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:14.161495Z'
  support: supports
  summary: OLS current exact CHEBI:32954 = sodium acetate; definition []; formula
    ['C2H3O2.Na']; mass ['82.034']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi64103
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:14.220421Z'
  support: supports
  summary: OLS current exact CHEBI:64103 = sodium butyrate; definition ['An organic
    sodium salt resulting from the replacement of the proton from the carboxy group
    of butyric acid by a sodium ion.']; formula ['C4H7O2.Na']; mass ['110.088']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0499238461b934590c83719736c7a30bf942d95c204daee7da061e0ba99f4a74
- evidence_id: api667Rest
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/667
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:36.913135Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch073/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T17:31:51.589494Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 7eac428c23cdb98628396e1a68501dc871f6f31792d28ba8f6e724e3ad74bacf
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfallas_thermosapovorans_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:31:51.593666Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api667Rest raw bytes exactly match the cited historical SHA, and 56 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: e8deb2741637a6e06d224380bc00acd0c3ebc4fecea505c4140b3d9c0758cdd0
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/desulfotomaculum_thermosapovorans_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:31:51.593769Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api667Rest raw bytes exactly match the cited historical SHA, and 56 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 95377c9439e401878fb907d8142a3d8c6fdba3f02e2c8de2242b4182f0326956
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:31:51.593814Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: 24af9bd74476d2e824202e35b4667fef917255c3de81c1b2d9d5b66f2bea1645
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:31:51.593853Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: 7d1ad69b6ae1d85b50402a8c504c1570047f149105c0aab34f21eb34ac0819a9
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:31:51.593898Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: b4ae44ad26519a2306851552d7292585ac6e31e51f95df80131410dbe46281d0
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch073/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T17:31:51.594072Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: ffa0f527218d5e5fdb7381a933e84d5712739bc5ee7709ec4246e8b3fcbaffd2
- evidence_id: writer55
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T17:31:51.594181Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer56
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T17:31:51.594232Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer57
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T17:31:51.594394Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer58
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T17:31:51.594447Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer59
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T17:31:51.594499Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer60
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T17:31:51.594549Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer61
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T17:31:51.594589Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T17:31:51.594628Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer63
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T17:31:51.594666Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch073/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T17:31:51.685027Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 071d6a45b6f61c57927d2bacf895aa1e01b705b7c7d12203c707a407102816d3
assessments:
- assessment_id: a1
  area: identity
  topic: Maintained source branches and current repairs
  outcome: concern
  summary: Both maintained owners resolve to DSM667, with historical KOMODO mapping
    supporting the shared accession but current exact KOMODO access unavailable. The
    DSM contributor and target retain source preparation; the KOMODO contributor does
    not. Both owners have already repaired the identical-number NaOH sum while the
    generated target remains stale. These source-duplicate candidates are not currently
    equal full formulations.
  target_ids:
  - CultureMech:001808
  evidence_ids:
  - local0
  - local1
  - local2
  - dsm667
  - api667Rest
  - history-auth
- assessment_id: a2
  area: grounding
  topic: Other chemical forms and complex components
  outcome: supported
  summary: Current OLS supports the other asserted source forms, including sodium
    carbonate, acetate and butyrate. Source D-calcium pantothenate is compatible with
    the current OLS31345 D-calcium synonyms and salt formula; vitamin B12 remains
    the source generic class and lipoic acid remains racemic/generic. Yeast extract
    is not forced to a pure chemical identifier. Exact MIM dictionary membership is
    distinct from authority for a source-specific form.
  target_ids:
  - CultureMech:001808
  evidence_ids:
  - grounding
  - chebi31345
  - chebi176843
  - chebi16494
  - chebi29377
  - chebi32954
  - chebi64103
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Five full reports and the two exact selected plan rows were read. The existing
    normalized NaOH repair is credited separately from the stale generated value and
    the unresolved multi-stock scientific problem. Current import/cleanup/merge behavior
    is scoped to the actual functions read. Current conservative merging preserves
    scientific fields and rejects incompatible formulations. Inspected writer behavior
    is described separately by exact file and function; it does not prove historical
    execution.
  target_ids:
  - CultureMech:001808
  evidence_ids:
  - history-auth
  - writer55
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
  - writer61
  - writer62
  - writer63
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 108 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:001808
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001808",
    "selected_concentration_field_count": 108, "selected_concentration_fields_covered":
    108, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3.08325",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3.08325",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3.08325",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=3.08325 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.08325,\n                        \"mmol_l\":
    21.7069,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 26-26", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2SO4                                                   3.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject":
    "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.20555",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.20555",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.20555",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.20555 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.20555,\n                        \"mmol_l\":
    1.51045,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 27-27", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   KH2PO4                                                   0.20        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.02775",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.02775",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.02775",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=1.02775 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.02775,\n                        \"mmol_l\":
    19.2139,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 28-28", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NH4Cl                                                    1.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "8.22199",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "8.22199",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "8.22199",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=8.22199 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 8.22199,\n                        \"mmol_l\":
    140.691,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 29-29", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NaCl                                                     8.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject":
    "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.4111",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.4111",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.4111",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.4111 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[4]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.4111,\n                        \"mmol_l\":
    2.0221,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 30-30", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   MgCl2
    x 6 H2O                                            0.40        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q6", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.513875",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.513875",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.513875",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.513875 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[5]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.513875,\n                        \"mmol_l\":
    6.89302,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 31-31", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   KCl                                                      0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject":
    "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.154162",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.154162",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.154162",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.154162 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[6]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.154162,\n                        \"mmol_l\":
    1.04862,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 32-32", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   CaCl2
    x 2 H2O                                            0.15        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q8", "subject": "Na-acetate", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.513875",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.513875",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.513875",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.513875 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[9]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.513875,\n                        \"mmol_l\":
    6.26418,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 35-35", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na-acetate                                               0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject":
    "Na-butyrate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "2.26105",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "2.26105",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "2.26105",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=2.26105 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[10]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na-butyrate\",\n                        \"compound_id\":
    232,\n                        \"amount\": 2.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.26105,\n                        \"mmol_l\":
    20.5387,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 36-36", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na-butyrate                                              2.20        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject":
    "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.4111",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.4111",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.4111",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.4111 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases.", "sources": [{"locator":
    "$.data.solutions[1].recipe[11]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.4111,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 37-37", "source_key": "dsm667", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256":
    "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256":
    "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at":
    "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Yeast extract                                            0.40        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject":
    "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.000513875",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.000513875",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.000513875",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Solution A", "interpretation":
    "The current API explicitly supplies g_l=0.000513875 for Solution A. This supports
    that stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.
    These A-stage rates use provider volume 973 ml. The complete primary medium explicitly
    has final volume 1010 ml; do not equate the two bases. Sodium resazurin is explicitly
    0.5 ml of a 0.1% w/v stock added to A; retain that dose and strength.", "sources":
    [{"locator": "$.data.solutions[1].recipe[12]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000513875,\n                        \"mmol_l\": 0.00204592,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 38-38", "source_key": "dsm667", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256":
    "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256":
    "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at":
    "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Sodium resazurin (0.1%
    w/v)                              0.50       ml", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q12", "subject": "Na2CO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution B", "interpretation":
    "The current API explicitly supplies g_l=50 for Solution B. This supports that
    stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.",
    "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api667Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    471.752,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 44-44", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2CO3                                                   1.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject":
    "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Solution D", "interpretation":
    "The current API explicitly supplies g_l=40 for Solution D. This supports that
    stage''s provider rate, not the current undifferentiated final-medium ingredient
    rate. Preserve the exact source amount/form, stock structure and receiving dose.",
    "sources": [{"locator": "$.data.solutions[4].recipe[0]", "source_key": "api667Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\":
    166.54,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 62-62", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2S x
    9 H2O                                                0.20        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q14", "subject": "HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10",
    "interpretation": "The current API explicitly supplies g_l=2.5 for Trace element
    solution SL-10. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. Primary HCl is 10 ml of 25% solution with no percentage basis
    or density; g_l=2.5 remains provider output, not an independently proven mass
    conversion.", "sources": [{"locator": "$.data.solutions[6].recipe[0]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 73-73", "source_key": "dsm667", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256":
    "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256":
    "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at":
    "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   HCl (25%)                                                  10.00      ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject":
    "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10",
    "interpretation": "The current API explicitly supplies g_l=1.5 for Trace element
    solution SL-10. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g
    conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[1]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 74-74", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   FeCl2
    x 4 H2O                                               1.50       g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q16", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10",
    "interpretation": "The current API explicitly supplies g_l=0.07 for Trace element
    solution SL-10. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g
    conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[2]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 75-75", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   ZnCl2                                                      70.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject":
    "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10",
    "interpretation": "The current API explicitly supplies g_l=0.1 for Trace element
    solution SL-10. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g
    conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[3]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 76-76", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   MnCl2
    x 4 H2O                                             100.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q18", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution
    SL-10", "interpretation": "The current API explicitly supplies g_l=0.006 for Trace
    element solution SL-10. This supports that stage''s provider rate, not the current
    undifferentiated final-medium ingredient rate. Preserve the exact source amount/form,
    stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its
    stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[4]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 77-77", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   H3BO3                                                       6.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject":
    "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution SL-10",
    "interpretation": "The current API explicitly supplies g_l=0.19 for Trace element
    solution SL-10. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. SL-10 explicitly makes up to 1000 ml, so its stock mg-to-g
    conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[5]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 78-78", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   CoCl2
    x 6 H2O                                             190.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q20", "subject": "CuCl2 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution
    SL-10", "interpretation": "The current API explicitly supplies g_l=0.002 for Trace
    element solution SL-10. This supports that stage''s provider rate, not the current
    undifferentiated final-medium ingredient rate. Preserve the exact source amount/form,
    stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its
    stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[6]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   CuCl2
    x 2 H2O                                               2.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q21", "subject": "NiCl2 x 6 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution
    SL-10", "interpretation": "The current API explicitly supplies g_l=0.024 for Trace
    element solution SL-10. This supports that stage''s provider rate, not the current
    undifferentiated final-medium ingredient rate. Preserve the exact source amount/form,
    stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its
    stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[7]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 80-80", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NiCl2
    x 6 H2O                                              24.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q22", "subject": "Na2MoO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Trace element solution
    SL-10", "interpretation": "The current API explicitly supplies g_l=0.036 for Trace
    element solution SL-10. This supports that stage''s provider rate, not the current
    undifferentiated final-medium ingredient rate. Preserve the exact source amount/form,
    stock structure and receiving dose. SL-10 explicitly makes up to 1000 ml, so its
    stock mg-to-g conversion is supported.", "sources": [{"locator": "$.data.solutions[6].recipe[8]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 81-81", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2MoO4
    x 2 H2O                                            36.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q23", "subject": "Na2SeO3 x 5 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Selenite-tungstate solution",
    "interpretation": "The current API explicitly supplies g_l=0.003 for Selenite-tungstate
    solution. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose.", "sources": [{"locator": "$.data.solutions[7].recipe[1]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 91-91", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2SeO3
    x 5 H2O                                            3.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2WO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Selenite-tungstate solution",
    "interpretation": "The current API explicitly supplies g_l=0.004 for Selenite-tungstate
    solution. This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose.", "sources": [{"locator": "$.data.solutions[7].recipe[2]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 92-92", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2WO4
    x 2 H2O                                             4.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q25", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.02 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[0]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 98-98", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Biotin                                                     20.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q26", "subject":
    "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.02 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[1]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 99-99", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Folic
    acid                                                 20.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q27", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.1 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[2]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 100-100", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Pyridoxine
    hydrochloride                                  100.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q28", "subject": "Thiamine HCl",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[3]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 101-101", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Thiamine
    HCl                                               50.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q29", "subject": "Riboflavin",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[4]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 102-102", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Riboflavin                                                 50.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject":
    "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[5]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 103-103", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Nicotinic
    acid                                             50.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q31", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[6]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 104-104", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Calcium
    D-(+)-pantothenate                                 50.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q32", "subject": "Vitamin B12",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution
    (10x)", "interpretation": "The current API explicitly supplies g_l=0.001 for Wolin''s
    vitamin solution (10x). This supports that stage''s provider rate, not the current
    undifferentiated final-medium ingredient rate. Preserve the exact source amount/form,
    stock structure and receiving dose. These amounts describe the tenfold Wolin stock
    with 1000 ml listed water, not the entire quantity added to the medium.", "sources":
    [{"locator": "$.data.solutions[8].recipe[7]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical
    LF lines 105-105", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Vitamin
    B12                                                 1.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q33", "subject": "p-Aminobenzoic
    acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[8]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 106-106", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   p-Aminobenzoic
    acid                                        50.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q34", "subject": "(DL)-alpha-Lipoic
    acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[34].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[34].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[34].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "The current API explicitly supplies g_l=0.05 for Wolin''s vitamin
    solution (10x). This supports that stage''s provider rate, not the current undifferentiated
    final-medium ingredient rate. Preserve the exact source amount/form, stock structure
    and receiving dose. These amounts describe the tenfold Wolin stock with 1000 ml
    listed water, not the entire quantity added to the medium.", "sources": [{"locator":
    "$.data.solutions[8].recipe[9]", "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 114-114", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   (DL)-alpha-Lipoic
    acid                                  50.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q35", "subject": "Na2S2O4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[35].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[35].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[35].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Na-dithionite solution (5% w/v)",
    "interpretation": "The current API explicitly supplies g_l=50 for Na-dithionite
    solution (5% w/v). This supports that stage''s provider rate, not the current
    undifferentiated final-medium ingredient rate. Preserve the exact source amount/form,
    stock structure and receiving dose. The explicit source 5% w/v designation supports
    50 g/L at dithionite-stock scope only.", "sources": [{"locator": "$.data.solutions[9].recipe[1]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2S2O4\",\n                        \"compound_id\":
    653,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    287.175,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 121-121", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na2S2O4                                                   0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q36", "subject":
    "NaOH amounts conflated across two stocks", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "1.0", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[22].notes", "original": " [Merged 2 duplicates: 0.5,
    0.5]"}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "ingredients[22].notes", "original": "[Collapsed 2 identical duplicates:
    0.5, 0.5]"}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ingredients[22].notes", "original": "[Collapsed 2 identical duplicates:
    0.5, 0.5]"}], "decision": "conflict", "stage": "Selenite-tungstate mass versus
    dithionite normal solution", "interpretation": "The generated target retains a
    historical sum 1.0 G_PER_L from two equal numeric 0.5 values. Both maintained
    owners already collapse it to 0.5 and retain the repair event; credit that correction.
    Neither flat value represents the source topology: Se/W uses 0.5 g NaOH with 1000
    ml water, while dithionite uses 0.5 ml of 1 N NaOH with 9.5 ml water. These are
    different dimensions and stages and must be represented separately, not summed
    or collapsed merely because their numbers match.", "sources": [{"locator": "$.data.solutions[7].recipe[0]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 90-90", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NaOH                                                       0.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[0]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"attribute\": \"1 N\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 120-120", "source_key": "dsm667", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf", "source_raw_sha256":
    "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c", "source_text_sha256":
    "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf", "accessed_at":
    "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   NaOH (1 N)                                                0.50       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject":
    "Solution A", "local_fields": [], "decision": "add", "stage": "Main sol. 667",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    1405,\n                        \"amount\": 973,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution
    A                                             973.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q38", "subject": "Solution B",
    "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    1406,\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution
    B                                              30.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q39", "subject": "Solution C",
    "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    1407,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 9-9", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution
    C                                               1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q40", "subject": "Solution D",
    "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    1408,\n                        \"amount\": 5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-10", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution
    D                                               5.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q41", "subject": "Solution E",
    "local_fields": [], "decision": "add", "stage": "Main sol. 667", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\":
    1409,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 11-11", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Solution
    E                                               1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q42", "subject": "Trace element
    solution SL-10", "local_fields": [], "decision": "add", "stage": "Solution A",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 33-33", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Trace
    element solution SL-10                             1.50       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q43", "subject": "Selenite-tungstate
    solution", "local_fields": [], "decision": "add", "stage": "Solution A", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Selenite-tungstate
    solution                              1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q44", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Solution A", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[1].recipe[13]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 970,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 39-39", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                        970.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q45", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Solution B", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 45-45", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                         30.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q46", "subject": "Wolin''s vitamin
    solution (10x)", "local_fields": [], "decision": "add", "stage": "Solution C",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 57-57", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Wolin''s
    vitamin solution (10x)                              1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q47", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Solution D", "interpretation":
    "Retain this exact source stock link, receiving dose or solvent input at its own
    stage. The main A–E doses are absolute batch inputs into the explicitly declared
    1010 ml final medium; nested stock batches are not final-medium amounts.", "sources":
    [{"locator": "$.data.solutions[4].recipe[1]", "source_key": "api667Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 63-63", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                             5.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q48", "subject": "Na-dithionite
    solution (5% w/v)", "local_fields": [], "decision": "add", "stage": "Solution
    E", "interpretation": "Retain this exact source stock link, receiving dose or
    solvent input at its own stage. The main A–E doses are absolute batch inputs into
    the explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[5].recipe[0]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Na-dithionite solution (5% w/v)\",\n                        \"solution_id\":
    6262,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 68-68", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Na-dithionite
    solution (5% w/v)                             1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q49", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Trace element solution SL-10",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[6].recipe[9]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                           990.00      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q50", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Selenite-tungstate solution",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[7].recipe[3]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 93-93", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q51", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Wolin''s vitamin solution (10x)",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[8].recipe[10]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 115-115", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                       1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q52", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Na-dithionite solution (5% w/v)",
    "interpretation": "Retain this exact source stock link, receiving dose or solvent
    input at its own stage. The main A–E doses are absolute batch inputs into the
    explicitly declared 1010 ml final medium; nested stock batches are not final-medium
    amounts.", "sources": [{"locator": "$.data.solutions[9].recipe[2]", "source_key":
    "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667", "source_raw_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "source_text_sha256":
    "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41", "accessed_at":
    "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 9.5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 122-122", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "   Distilled
    water                                           9.50       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q53", "subject": "Explicit final
    medium volume", "local_fields": [], "decision": "add", "stage": "Completed A–E
    medium", "interpretation": "The primary explicitly states final volume 1010 ml.
    The printed A–E additions sum exactly: 973 + 30 + 1 + 5 + 1 = 1010 ml. This positive
    final-volume support is distinct from the separate A-stage normalization and from
    stock-water listings.", "sources": [{"locator": "extracted-text physical LF lines
    3-11", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Final pH:
    7.0 - 7.2\nFinal volume: 1010 ml\n\n\n   Solution A                                             973.00       ml\n   Solution
    B                                              30.00       ml\n   Solution C                                               1.00       ml\n   Solution
    D                                               5.00       ml\n   Solution E                                               1.00       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q54", "subject":
    "Retained preparation step 1", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Solution A is sparged
    with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then
    distributed under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%
    CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and sterilized
    by filtration. Solution D is autoclaved under 100% N2 gas. Solution E  is prepared
    under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete
    the medium appropriate amounts of solutions B to E are added to the sterile solution
    A in the sequence as indicated. Final pH of the medium should be at 7.0 - 7.2."},
    {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Solution A is sparged
    with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then
    distributed under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%
    CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and sterilized
    by filtration. Solution D is autoclaved under 100% N2 gas. Solution E  is prepared
    under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete
    the medium appropriate amounts of solutions B to E are added to the sterile solution
    A in the sequence as indicated. Final pH of the medium should be at 7.0 - 7.2."}],
    "decision": "evidence_only", "stage": "Existing stage-specific preparation", "interpretation":
    "The generated target and DSM owner already preserve 80% N2/20% CO2 sparging to
    pH below 6 for at least 30 min, separate A/B autoclaving, C/D 100% N2 and E 80/20
    scopes, filtration for C/E, ordered additions and final pH 7.0–7.2. Preserve that
    prose with exact source evidence. The KOMODO owner lacks it. No main autoclave
    time/temperature is specified here.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\":
    \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below
    6 (at least 30 min), then distributed under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere
    and sterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution
    E  is prepared under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration.
    To complete the medium appropriate amounts of solutions B to E are added to the
    sterile solution A in the sequence as indicated. Final pH of the medium should
    be at 7.0 - 7.2.\"\n                    }", "quote_representation": "raw JSON
    object"}, {"locator": "extracted-text physical LF lines 13-20", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Solution
    A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at\nleast
    30 min), then distributed under same gas atmosphere into anoxic Hungate-type\ntubes
    or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2\nand
    20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere and\nsterilized
    by filtration. Solution D is autoclaved under 100% N2 gas. Solution E is prepared\nunder
    80% N2 and 20% CO2 gas atmosphere and sterilized by filtration. To complete the\nmedium
    appropriate amounts of solutions B to E are added to the sterile solution A in
    the\nsequence as indicated. Final pH of the medium should be at 7.0 - 7.2.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q55", "subject": "Retained preparation
    step 2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}], "decision": "evidence_only", "stage": "Existing stage-specific
    preparation", "interpretation": "The retained SL-10 preparation correctly states
    sequential dissolution and final make-up to 1000 ml. Keep it scoped to SL-10,
    not main-medium final volume.", "sources": [{"locator": "$.data.solutions[6].steps[0]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 84-85", "source_key":
    "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q56", "subject": "Retained preparation step 3", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml", "field_path":
    "preparation_steps[2].description", "original": "Add 1 N NaOH to distilled water
    and make the solution anoxic by sparging with 100% N2 gas. Then dissolve the Na-dithionite
    and filter-sterilize the solution into anoxic Hungate tubes. The final pH of the
    solution should be between 9 and 10. Store the prepared solution in a dark and
    cool place. Prepare only small amounts of stock solution, as Na-dithionite decomposes
    rapidly."}, {"record_path": "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml",
    "field_path": "preparation_steps[2].description", "original": "Add 1 N NaOH to
    distilled water and make the solution anoxic by sparging with 100% N2 gas. Then
    dissolve the Na-dithionite and filter-sterilize the solution into anoxic Hungate
    tubes. The final pH of the solution should be between 9 and 10. Store the prepared
    solution in a dark and cool place. Prepare only small amounts of stock solution,
    as Na-dithionite decomposes rapidly."}], "decision": "evidence_only", "stage":
    "Existing stage-specific preparation", "interpretation": "The retained dithionite
    preparation correctly uses 1 N NaOH, 100% N2/filter sterilization and stock pH
    9–10. Preserve this evidence and distinguish it from final-medium pH; dark/cool
    storage has no numerical temperature here.", "sources": [{"locator": "$.data.solutions[9].steps[0]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\":
    \"Add 1 N NaOH to distilled water and make the solution anoxic by sparging with
    100% N2 gas. Then dissolve the Na-dithionite and filter-sterilize the solution
    into anoxic Hungate tubes. The final pH of the solution should be between 9 and
    10. Store the prepared solution in a dark and cool place. Prepare only small amounts
    of stock solution, as Na-dithionite decomposes rapidly.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical
    LF lines 124-128", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Add 1 N NaOH
    to distilled water and make the solution anoxic by sparging with 100% N2\ngas.
    Then dissolve the Na-dithionite and filter-sterilize the solution into anoxic
    Hungate\ntubes. The final pH of the solution should be between 9 and 10. Store
    the prepared\nsolution in a dark and cool place. Prepare only small amounts of
    stock solution, as Na\n-dithionite decomposes rapidly.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q57", "subject": "Final pH range",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml",
    "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path":
    "data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml", "field_path":
    "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml",
    "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}], "decision":
    "evidence_only", "stage": "Completed medium", "interpretation": "All three layers
    retain source-supported final pH 7.0–7.2; this is separate from the initial A-stage
    pH below 6 and dithionite-stock pH 9–10.", "sources": [{"locator": "extracted-text
    physical LF lines 3-3", "source_key": "dsm667", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium667.pdf",
    "source_raw_sha256": "9a213eabc518cdb817536146984a3d068e592ab8bff0a7695f884453f087530c",
    "source_text_sha256": "18a3f2967be7c447c25d1ce34219b844e54716e7431c31e5ff9d830b99ddfabf",
    "accessed_at": "2026-10-28T17:17:13.756864Z", "exact_source_quote": "Final pH:
    7.0 - 7.2", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api667Rest", "reference": "https://mediadive.dsmz.de/rest/medium/667",
    "source_raw_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "source_text_sha256": "625bccbc1ac75d31b9933feb2644bc99c8f70bdec47c77ee53ac56e3f681bb41",
    "accessed_at": "2026-10-28T17:17:36.913135Z", "exact_source_quote": "{\n                        \"step\":
    \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below
    6 (at least 30 min), then distributed under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas atmosphere. Solutions C is prepared under 100% N2 gas atmosphere
    and sterilized by filtration. Solution D is autoclaved under 100% N2 gas. Solution
    E  is prepared under 80% N2 and 20% CO2 gas atmosphere and sterilized by filtration.
    To complete the medium appropriate amounts of solutions B to E are added to the
    sterile solution A in the sequence as indicated. Final pH of the medium should
    be at 7.0 - 7.2.\"\n                    }", "quote_representation": "raw JSON
    object"}]}], "local_field_census_reference": "REVIEW_WORK/batch073/record06/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFALLAS_THERMOSAPOVORANS_MEDIUM.yaml: primary
    35/36, secondary 33/36; data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml:
    primary 35/36, secondary 33/36; data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml:
    primary 35/36, secondary 33/36. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:001808
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
  - CultureMech:001808
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
  - CultureMech:001808
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001808-assembly-and-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source A–E assembly is flattened into mixed-stage concentrations
  description: Eleven A-stage rates based on 973 ml and multiple stock-strength rates
    are represented as undifferentiated main ingredients despite the primary explicit
    1010 ml final medium. All receiving doses, stock solvents and nested structures
    are absent. The HCl 25% provider conversion does not establish an unqualified
    mass basis.
  target_ids:
  - CultureMech:001808
  field_paths:
  - ingredients
  - solutions
  - evidence
  evidence_ids:
  - dsm667
  - api667Rest
  rule_id: source-stage-and-dimensional-basis
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-001808-stale-naoh-and-conflated-stages
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Generated NaOH sum is stale and the owner collapse still loses stock identity
  description: The generated target retains 1.0 G_PER_L, whereas both maintained owners
    already carry 0.5 G_PER_L after the recorded identical-duplicate repair. Credit
    the repaired owner state, but neither representation separates 0.5 g NaOH in Se/W
    from 0.5 ml of 1 N NaOH in dithionite stock. Current cleanup and duplicate-repair
    functions cannot establish those chemical stages.
  target_ids:
  - CultureMech:001808
  field_paths:
  - ingredients[22].concentration
  - ingredients[22].notes
  - curation_history
  evidence_ids:
  - dsm667
  - api667Rest
  - local0
  - local1
  - local2
  rule_id: generated-freshness-and-independent-stock-inputs
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001808-owner-preparation-divergence
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: KOMODO preparation and atmosphere diverge from the retained primary procedure
  description: 'The target and DSM owner already preserve three preparation descriptions
    and correct final pH. Only the KOMODO owner lacks those descriptions and says
    Aerobic: Yes, contradicting the primary anaerobic procedure. The current merger
    rejects incompatible scientific projections; do not treat the existing duplicate
    relationship as permission to discard preparation.'
  target_ids:
  - CultureMech:001808
  field_paths:
  - data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml::notes
  - data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml::preparation_steps
  - data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml::parent_media
  - variant_children
  evidence_ids:
  - dsm667
  - api667Rest
  - local1
  - local2
  rule_id: source-preparation-and-owner-equivalence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-001808-nickel-hydrate-and-sodium-resazurin-form
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
  - CultureMech:001808
  field_paths:
  - ingredients[20].term
  - ingredients[20].mediaingredientmech_chebi_term
  - ingredients[10].term
  evidence_ids:
  - dsm667
  - chebi34887
  - chebi8806
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-001808-append-only-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Evidence and historical timestamps need bounded curation
  description: No current layer contains attached formulation claims. Both maintained
    owners retain a September duplicate-repair event omitted from the older generated
    target. Historical full-report/API matches support only their exact current objects;
    separately cited KOMODO catalogue bytes and old execution remain unverified. The
    KOMODO owner also retains literal .fZ and offset-less timestamps.
  target_ids:
  - CultureMech:001808
  field_paths:
  - evidence
  - data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml::curation_history
  - curation_history
  evidence_ids:
  - history-auth
  - komodo667
  rule_id: append-only-source-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current import timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
actions:
- action_id: action1
  description: Reconstruct the exact A–E assembly and embedded stocks; preserve supplied
    chemical forms, explicit 1010 ml final volume and stage-specific source inputs.
    Use provider rates only within their declared stage; do not independently convert
    bare HCl percentage to mass without a supported basis.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
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
  description: Preserve existing repair provenance and reconstruct the two distinct
    NaOH stock inputs before regenerating. Do not merely replace the generated sum
    with a single owner value or reinterpret 1 N liquid volume as mass.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
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
  description: Preserve all supported target/DSM preparation and correct only the
    incomplete KOMODO source context. Review duplicate relationships and regenerate
    conservatively from reconciled owners.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
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
  description: Resolve the exact source hydrate and sodium-salt identities against
    authoritative ontology and MIM records. Use verified supplied-form mappings or
    retain precise source labels with unresolved mapping; preserve source masses and
    do not substitute anhydrous molar arithmetic.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
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
  description: Attach claim-scoped fresh evidence and append a verified current event,
    preserving all historical bytes and the existing duplicate-repair record. Correct
    future timestamps in the exact inspected writers without rewriting historical
    dates.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfallas_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_thermosapovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current import timestamp writer
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
  - Verify future importer/enrichment events use actual UTC with timezone, and existing
    repair and malformed historical events remain unchanged.
limitations:
- Exact historical KOMODO MediaInfo=667 returned HTTP 403; current primary/API evidence
  does not authenticate historical catalogue bytes or execution times.
- The source explicitly states final 1010 ml, and its A–E doses sum to that value;
  A-stage 973 ml rates are not final-medium rates.
- HCl 25% has no explicit percentage basis/density. No independent mass conversion
  or exact sodium-resazurin replacement is invented.
- The repeated 0.5 NaOH values have different dimensions and stock contexts. The owner
  duplicate collapse is credited but is not a complete scientific repair.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
