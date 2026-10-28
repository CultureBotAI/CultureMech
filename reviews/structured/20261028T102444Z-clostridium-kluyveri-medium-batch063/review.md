# Scientific review of clostridium_kluyveri_medium

- Review: 20261028T102444Z-clostridium-kluyveri-medium-batch063
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:18:57.333715Z
- Finished UTC: 2026-10-28T10:24:44.081762Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM 52/TOGO M2703 identity is established, but the generated target and maintained owner lose stock stages, liquid units, pH and preparation, and point at an unrelated vitamin stock. Correct primary quantities and fourteen earlier dependency claims are credited; stock residual errors and exact-form/linkage limits are scoped explicitly.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch063 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009256 | data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml | generated | clostridium_kluyveri_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009256 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:009256 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:009256 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:009256 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact TOGO source and wrong generic vitamin link

identity: concern. Targets: CultureMech:009256.

TOGO M2703 explicitly names DSM 52 and its own seven-vitamin section agrees with the primary. Linked mediadive.solution:6241 instead has only cyanocobalamin, thiamine HCl and biotin in100 ml; it is not the seven-vitamin stock. Culture name is source identity, not a strain-specific experimental growth claim.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:009256.

Two old reports explicitly performed zero source checks; their flags are now assessed against current primary/API/TOGO evidence. Existing selected layers have no attached formulation claims. Fourteen attached stock claims authenticate current raw bytes, without recreating historical access times. Current TOGO code preserves stock sections and units; current cleanup does not sum unequal values, while name-only stock migration remains a source-identity risk. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:009256.

All 74 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009256", "selected_concentration_field_count": 74, "selected_concentration_fields_covered": 74, "decisions": [{"decision_id": "q1", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 0.2 g per displayed recipe, and API 52 explicitly reports g_l=0.2, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "MgSO4 x 7 H2O                                              0.20         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 1 g per displayed recipe, and API 52 explicitly reports g_l=1, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Yeast extract                                              1.00         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.23", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.23", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 0.23 g per displayed recipe, and API 52 explicitly reports g_l=0.23, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.23,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.23,\n                        \"mmol_l\": 1.69012,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "KH2PO4                                                     0.23         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 0.25 g per displayed recipe, and API 52 explicitly reports g_l=0.25, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 4.67377,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "NH4Cl                                                      0.25         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.31", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.31", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 0.31 g per displayed recipe, and API 52 explicitly reports g_l=0.31, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.31,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.31,\n                        \"mmol_l\": 1.77981,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "K2HPO4                                                     0.31         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 0.25 g per displayed recipe, and API 52 explicitly reports g_l=0.25, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[13]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.04088,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Na2S x 9 H2O                                               0.25         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 1 g per displayed recipe, and API 52 explicitly reports g_l=1, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[10]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 9.43503,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Na2CO3                                                     1.00         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "K-acetate", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 10 g per displayed recipe, and API 52 explicitly reports g_l=10, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K-acetate\",\n                        \"compound_id\": 86,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 101.893,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 3-3", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "K-acetate                                                 10.00         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "L-Cysteine-HCl x H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch mass and provider-declared g_l", "interpretation": "The primary lists 0.25 g per displayed recipe, and API 52 explicitly reports g_l=0.25, equal to the stored value. Retain that declared normalization with exact evidence. The API volume is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus additions without a final-volume instruction. Do not silently recompute a measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.4234,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "L-Cysteine HCl x H2O                                       0.25         g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Water summed across four distinct preparation stages", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3990.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3990.0", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main water and three separate stock batches", "interpretation": "3990 G_PER_L is an invalid sum of 1000 ml main water,990 ml SL10 water,1000 ml SeW water and 1000 ml vitamin water. Preserve each absolute water amount in its own stage; SL10 explicitly makes up to 1000 ml. None is 3990 g/L in the receiving medium.", "sources": [{"locator": "$.data.solutions[0].recipe[14]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[7]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 54-54", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "make up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Absolute ethanol addition", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main liquid addition", "interpretation": "Both primary and TOGO specify20 ml ethanol, not20 g/L. Preserve an absolute20 ml batch addition and source grade; any per-litre or mass conversion needs an explicit final-volume or density basis.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Ethanol absolute\",\n                        \"compound_id\": 89,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.components[0].items[9]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703", "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n          \"component_name\": \"Ethanol\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001114\",\n          \"gmo_id\": \"GMO_001114\",\n          \"label\": \"Ethanol\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Ethanol absolute                                          20.00        ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Gas atmosphere at named preparation stages", "interpretation": "VARIABLE does not express the explicit gas proportions or stage. Main and carbonate use80% N2/20% CO2; vitamin and reducing stocks use100% N2. No dissolved-gas mass or concentration is inferred. Retain gas identity, remove ambiguous duplicate context only after source-scoped representation is established.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and vitamins from an anoxic and filter-sterilized stock solution prepared under 100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[10]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703", "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n      \"paragraph_index\": 15,\n      \"comment\": \"Solution is prepared under 100% N2 gas and sterilized by filtration.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "Nitrogen gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Gas atmosphere at named preparation stages", "interpretation": "VARIABLE does not express the explicit gas proportions or stage. Main and carbonate use80% N2/20% CO2; vitamin and reducing stocks use100% N2. No dissolved-gas mass or concentration is inferred. Retain gas identity, remove ambiguous duplicate context only after source-scoped representation is established.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and vitamins from an anoxic and filter-sterilized stock solution prepared under 100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[10]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703", "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n      \"paragraph_index\": 15,\n      \"comment\": \"Solution is prepared under 100% N2 gas and sterilized by filtration.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "N2 gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Gas atmosphere at named preparation stages", "interpretation": "VARIABLE does not express the explicit gas proportions or stage. Main and carbonate use80% N2/20% CO2; vitamin and reducing stocks use100% N2. No dissolved-gas mass or concentration is inferred. Retain gas identity, remove ambiguous duplicate context only after source-scoped representation is established.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and vitamins from an anoxic and filter-sterilized stock solution prepared under 100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.comments[10]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703", "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a", "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n      \"paragraph_index\": 15,\n      \"comment\": \"Solution is prepared under 100% N2 gas and sterilized by filtration.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "36", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "36", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 36 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.036 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "6", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 6 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.006 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 100 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.1 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "190", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "190", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 190 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.19 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "24", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "24", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 24 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.024 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 2 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.002 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "70", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "70", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 70 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.07 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "HCl (25%; 7.7 M)", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 10 ml for this component, separately from its1 ml receiving dose. Keep the 10 ml HCl stock addition with 25% primary notation and separate TOGO7.7M notation; do not turn it into10 g/L or infer a percent basis/density.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock, not main medium", "interpretation": "Source Trace element solution SL-10 lists 1.5 g for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 1.5 g/L. The number matches a stock rate but is placed directly in the medium. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate solution stock, not main medium", "interpretation": "Source Selenite-tungstate solution lists 3 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.003 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "4", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate solution stock, not main medium", "interpretation": "Source Selenite-tungstate solution lists 4 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.004 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate solution stock, not main medium", "interpretation": "Source Selenite-tungstate solution lists 0.5 g for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.5 g/L. The number matches a stock rate but is placed directly in the medium. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "80", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "80", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 80 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.08 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 100 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.1 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "300", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "300", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 300 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.3 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 100 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.1 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "200", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "200", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 200 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.2 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "200", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "200", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 200 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.2 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "D(+)-Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock, not main medium", "interpretation": "Source Seven vitamins solution lists 20 mg for this component, separately from its1 ml receiving dose. Its provider-declared stock rate is 0.02 g/L. The retained same digits were milligrams in the source, not grams per litre. Restore the stock composition and receiving dose separately. No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "Receiving dose Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation": "The primary adds0.5 ml, not the stored0.5 G_PER_L. Preserve the absolute batch dose and named stock. The resazurin stock is explicitly0.1% w/v;0.5 ml contains0.5 mg, but that does not establish a final-medium denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Sodium resazurin (0.1% w/v)                                0.50        ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q35", "subject": "Receiving dose Trace element solution SL-10", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation": "The primary adds1 ml, not the stored1 G_PER_L. Preserve the absolute batch dose and named stock. Do not double count its components as direct medium ingredients.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Trace element solution SL-10                               1.00        ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q36", "subject": "Receiving dose Selenite-tungstate solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation": "The primary adds1 ml, not the stored1 G_PER_L. Preserve the absolute batch dose and named stock. Do not double count its components as direct medium ingredients.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Selenite-tungstate solution                                1.00        ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject": "Receiving dose Seven vitamins solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "solutions[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml", "field_path": "solutions[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation": "The primary adds1 ml, not the stored1 G_PER_L. Preserve the absolute batch dose and named stock. Do not double count its components as direct medium ingredients.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 14-14", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Seven vitamins solution                                    1.00        ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q38", "subject": "solution4178 HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[0].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Separately scoped linked stock", "interpretation": "Provider reports2.5 g/L for10 ml HCl labelled25%,7.7M. The percent basis is unspecified and 7.7M is a distinct supplied-stock declaration; neither validates a simple2.5 g/L interpretation without resolving this inconsistency. Retain exact10 ml and source attributes, leaving derived mass rate unresolved.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "solution4178 FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[1].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "solution4178 ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[2].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "solution4178 MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[3].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "solution4178 H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[4].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "solution4178 CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[5].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "solution4178 CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[6].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[6]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "solution4178 NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[7].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[7]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q46", "subject": "solution4178 Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[8].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[8]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject": "solution4178 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "composition[9].concentration", "original": {"value": "990", "unit": "PERCENT_V_V"}}], "decision": "correct", "stage": "Separately scoped linked stock", "interpretation": "990 ml water is an absolute stock batch input, not990%v/v. Preserve the volume; the selected DSM 52 stock independently adds an explicit make-up-to 1000 ml instruction.", "sources": [{"locator": "$.data.recipe[9]", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 54-54", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "make up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q48", "subject": "solution4178 placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder only", "interpretation": "The source has a real composition; VARIABLE placeholder is not an ingredient amount. Reconcile the stale incomplete_composition flag and placeholder without deleting verified composition evidence.", "sources": [{"locator": "$.data", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da", "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n        \"id\": 4178,\n        \"name\": \"Trace element solution SL-10\",\n        \"volume\": 1000,\n        \"recipe\": [\n            {\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\": null,\n                \"step\": \"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts.\"\n            }\n        ],\n        \"equipment\": []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject": "solution5543 NaOH", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml", "field_path": "composition[0].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject": "solution5543 Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml", "field_path": "composition[1].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q51", "subject": "solution5543 Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml", "field_path": "composition[2].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q52", "subject": "solution5543 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml", "field_path": "composition[3].concentration", "original": {"value": "1", "unit": "L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q53", "subject": "solution5543 placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder only", "interpretation": "The source has a real composition; VARIABLE placeholder is not an ingredient amount. Reconcile the stale incomplete_composition flag and placeholder without deleting verified composition evidence.", "sources": [{"locator": "$.data", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882", "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n        \"id\": 5543,\n        \"name\": \"Selenite-tungstate solution\",\n        \"volume\": 1000,\n        \"recipe\": [\n            {\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [],\n        \"equipment\": []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject": "solution6241 Cyanocobalamine", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field_path": "composition[0].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q55", "subject": "solution6241 Thiamine HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field_path": "composition[1].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation": "Existing attached claim matches this exact current raw payload digest and literal source object. Retain its declared stock concentration or absolute water addition; this does not authenticate any receiving-medium concentration.", "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q56", "subject": "solution6241 Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field_path": "composition[2].concentration", "original": {"value": "2000.0", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separately scoped linked stock", "interpretation": "200micrograms=0.0002 g in an explicit100 ml final stock, so0.002 g/L, not2000 g/L. This stock is nevertheless the wrong vitamin recipe for DSM 52 and must not replace its seven-vitamin source.", "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.steps[0]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q57", "subject": "solution6241 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field_path": "composition[3].concentration", "original": {"value": "1000.0", "unit": "PERCENT_V_V"}}], "decision": "correct", "stage": "Separately scoped linked stock", "interpretation": "The source makes up to 100 ml with water. Preserve that final-stock make-up instruction, not1000%v/v or an independently measured water dose.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.steps[0]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q58", "subject": "solution6241 placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder only", "interpretation": "The source has a real composition; VARIABLE placeholder is not an ingredient amount. Reconcile the stale incomplete_composition flag and placeholder without deleting verified composition evidence.", "sources": [{"locator": "$.data", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n        \"id\": 6241,\n        \"name\": \"Vitamin solution\",\n        \"volume\": 100,\n        \"recipe\": [\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }\n        ],\n        \"equipment\": []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q59", "subject": "Primary preparation, pH and conditional reducing supplement", "local_fields": [], "decision": "evidence_only", "stage": "Main preparation and conditional source-only control", "interpretation": "Restore source pH 6.8–7.0,30–45 min sparging, the 80/20 and 100% gas stages, ordering of ethanol/autoclaving/carbonate/vitamins/reducing agents and anoxic filtration. The10–20 mg/L sodium dithionite from 5% w/v is conditional on incomplete reduction, not an unconditional ingredient or guessed dose.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere and vitamins from an anoxic and filter-sterilized stock solution prepared under 100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\": \"Note: If reduction of medium is not complete after inoculation, add 10 - 20 mg/l sodium dithionite from a 5% w/v solution freshly prepared under 100% N2 gas and filter sterilized.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q60", "subject": "SL10 preparation and final stock volume", "local_fields": [], "decision": "evidence_only", "stage": "SL10 only", "interpretation": "Dissolve FeCl2 first in HCl, dilute and dissolve remaining compounds, then make up to 1000 ml. This explicit stock volume does not establish the final volume of the main medium.", "sources": [{"locator": "$.data.solutions[1].steps[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 54-54", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf", "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829", "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807", "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "make up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch063/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:009256.

data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml: primary 30/33, secondary 27/33; data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml: primary 30/33, secondary 27/33. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 2 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:009256.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:009256.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Stock quantities and liquid additions have become direct mass concentrations

major / open / confirmed; issue key: culturemech-009256-stock-stage-and-liquid-unit-corruption.

Water3990 G_PER_L combines four preparation batches. Stock milligram amounts became equal-digit G_PER_L, and other stock rates were flattened directly. Ethanol20 ml and four stock additions were stored as G_PER_L. These are explicit unit/stage defects, while nine ordinary main rates are credited only as provider-declared nominal normalization.

### f2: Generic vitamin name resolves to an unrelated stock

major / open / confirmed; issue key: culturemech-009256-wrong-vitamin-stock-reference.

The selected Vitamin solution points to solution6241, a three-vitamin100 ml stock, whereas DSM 52/TOGO M2703 define seven vitamins. Matching a generic label does not establish recipe identity.

### f3: Source preparation and pH are absent

major / open / confirmed; issue key: culturemech-009256-missing-staged-preparation.

Neither selected layer retains preparation or pH, although the source specifies separate sterilization, anoxic additions, pH range and a conditional reducing supplement. VARIABLE gases do not retain these stage-specific controls.

### f4: Nickel hydrate and magnesium secondary mapping disagree with source forms

major / open / confirmed; issue key: culturemech-009256-hydrate-and-secondary-form-disagreement.

Nickel hexahydrate asserts anhydrous CHEBI:34887 in both selected slots and the SL10 dependency. Magnesium primary31795 correctly records heptahydrate but secondary32599 remains anhydrous. Calcium pantothenate source stereochemistry is unspecified; its D-associated current term is a mapping limit, not permission to change the supplied material.

### f5: Linked stocks retain liquid and microgram artifacts despite earlier partial repairs

major / open / confirmed; issue key: culturemech-009256-linked-stock-residual-unit-artifacts.

SL10 water 990%v/v and the vitamin stock water 1000%v/v are not source volumes; vitamin biotin2000 g/L conflicts with 200micrograms made up to 100 ml. HCl derived2.5 g/L remains unsupported by its mixed25%/7.7M declarations. Fourteen previously attached stock claims remain authenticated and must be retained. Placeholder ingredients and incomplete flags are separate stale metadata.

### f6: Potassium acetate retains an unresolved legacy secondary identifier

minor / open / confirmed; issue key: culturemech-009256-legacy-acetate-secondary-link.

Both layers retain MediaIngredientMech000580, which has no exact row in the pinned current CSV. Correct primary CHEBI:32029 remains supported. Current absence is not evidence the historical identifier was invalid.

## Recommended Actions And Acceptance Checks

### action1

Rebuild the main recipe and three stock compositions from exact source sections; restore liquid units and doses, avoid stock double counting, and retain the stated main-volume uncertainty.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Replace the wrong reference with a source-verified seven-vitamin definition or inline stock composition. Preserve6241 as a distinct record; do not overwrite it with the receiving recipe.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Restore source-specific preparation and root evidence scoped to each solution dose and preparation stage. Keep the conditional dithionite addition conditional.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve exact hydrate mappings and align the stale magnesium secondary link with the already-correct primary. Preserve generic source stereochemistry where not specified; do not infer hydrate molarities from provider mmol_l.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Repair only the demonstrated dependency fields with source-scoped evidence, retaining fourteen correct earlier claims. Keep6241 separate from DSM 52 and do not transfer a whole uncorrected stock automatically.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action6

Reconcile the legacy secondary link against the exact current potassium acetate record, preserving the old history and already-correct primary identity.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch063/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch063/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch063/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch063/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz52 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api52 | https://mediadive.dsmz.de/rest/medium/52; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| togoM2703 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| solution4178 | https://mediadive.dsmz.de/rest/solution/4178; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| solution5543 | https://mediadive.dsmz.de/rest/solution/5543; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O']; mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16236 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16236; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16236 = ethanol; definition ['A primary alcohol that is ethane in which one of the hydrogens is substituted by a hydroxy group.']; formula ['C2H6O']; mass ['46.069']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon compound with formula CO&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt; in which the carbon is attached to each oxygen atom by a double bond. A colourless, odourless gas under normal conditions, it is produced during respiration by all animals, fungi and microorganisms that depend directly or indirectly on living or decaying plants for food.']; formula ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17439 = cyanocob(III)alamin; definition ['A complex cob(III)alamin in which cobalt is positioned in the centre of a planar corrin tetrapyrrole ring and bound axially to a 5,6-dimethylbenzimidazole moiety and a cyano group. It is one of several forms of the vitamin known as vitamin B12.']; formula ['C63H88CoN14O14P']; mass ['1355.388']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32029 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32029; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32029 = potassium acetate; definition ['A potassium salt comprising equal numbers of potassium and acetate ions']; formula ['C2H3O2.K']; mass ['98.142']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W']; mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:91248 = L-cysteine hydrochloride hydrate; definition ['A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride.']; formula ['C3H7NO2S.H2O.HCl']; mass ['175.637']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| grounding | REVIEW_WORK/batch063/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch063/record05/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer50 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace legacy secondary MIM links or authenticate quantities. |
| writer51 | scripts/cleanup_media_quality.py; relevant functions named in summary | context_only | Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical quantities and flags conflicting quantities rather than summing them. Persisted old duplicate sums require independent source review; they do not establish that this current implementation still sums unequal stages. |
| writer52 | scripts/enrich_with_chebi.py; relevant functions named in summary | context_only | Current RecipeEnricher.enrich_ingredient skips already grounded terms and delegates ungrounded names to ChemicalMapper; enrich_recipe traverses ingredients and nested compositions, and enrich_file appends provenance. The wrapper does not independently verify supplied chemical forms or recipe amounts. ChemicalMapper internals were not added as a scientific authority. |
| writer53 | scripts/migrate_chebi_regrounding.py; relevant functions named in summary | context_only | Current rewrite_entry applies exact from-ID plus ingredient-label remaps across primary and secondary slots, while migrate_file appends a change-specific history event. The generic nickel chloride remap does not distinguish its hydrate; current mappings require independent supplied-form review. This read does not establish historical execution. |
| writer54 | scripts/migrate_legacy_mim_to_chebi.py; relevant functions named in summary | context_only | Full _resolve_chebi/_rewrite_entry/migrate_file read. Existing primary CHEBI is reused if present in MIM; exact-name/synonym resolution is limited by a stereo-prefix guard, and unresolved links remain. The code does not prove chemical equivalence or historical validity merely because an ID has a current row. |
| writer55 | scripts/migrate_mgso4_heptahydrate_term.py; relevant functions named in summary | context_only | iter_ingredients and main make a label-conditional primary-term-only 32599 to 31795 repair; secondary annotations are untouched. The current primary is credited while stale secondary linkage requires separate review. |
| writer56 | scripts/migrate_solutions_from_ingredients.py; relevant functions named in summary | context_only | Current _resolve_solution and _migrate_media_file identify stock references and move descriptors into solutions while preserving their stored concentration. The resolver selects a solution by normalized name and preserves the old concentration; neither operation proves source-specific stock equivalence. A generic Vitamin solution name can select an unrelated recipe. Current behavior does not prove the historical run. |
| writer57 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition uses only the primary recipe and prefers provider g_l; it excludes recognized solvent names. The ml fallback maps to ML_PER_L, requiring an independent denominator check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes. _parse_preparation_steps collects prose from all solution sections without separate stage fields. These present behaviors do not establish historical execution. |
| writer58 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer59 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer60 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer61 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| writer62 | src/culturemech/validation/schema_defaulter.py; relevant functions named in summary | context_only | Full apply_defaults/_fix_ingredient/_fix_solution read. The defaulter inserts VARIABLE concentrations and Unknown solution names to satisfy structure. These defaults are not evidence for a source dose, composition or final volume; copied historical default events remain contextual. |
| dep63 | data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep64 | data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| dep65 | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; explicit scoped stock rows in quantity inventory | supports | Current dependency read separately; only the stock composition named by the receiving source transfers. Earlier attached evidence and history retained; unrelated parent medium, doses, pH and growth do not transfer. |
| quantity-inventory | REVIEW_WORK/batch063/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The PDF lists main water and additions without an explicit final-medium volume; API 52 declares volume1023 ml while its g_l follows a nominal litre. No measured final concentrations are inferred.
- Source recipes establish a formulation and named-medium identity, not strain-specific experimental growth. Calcium pantothenate stereochemistry and the HCl percent/molar conversion remain bounded unresolved details.
- The current packaged MIM snapshot is pinned by commit and exact CSV rows. Current absence does not establish historical invalidity; no record was edited.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T102444Z-clostridium-kluyveri-medium-batch063
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of clostridium_kluyveri_medium
started_at: '2026-10-28T10:18:57.333715Z'
finished_at: '2026-10-28T10:24:44.081762Z'
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
summary: DSM 52/TOGO M2703 identity is established, but the generated target and maintained
  owner lose stock stages, liquid units, pH and preparation, and point at an unrelated
  vitamin stock. Correct primary quantities and fourteen earlier dependency claims
  are credited; stock residual errors and exact-form/linkage limits are scoped explicitly.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
    sha256: 98c0aaa787015c758fe1f7cde8d51cf0e263229f2a0fe37f2680cb73e22fcffc
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    sha256: 7dee06f544d931041a49255026a9046eada8cad7dfc3e7472798714f80fdd09a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
    sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.md
    sha256: 5e53044e4466908723e28767f4f70eab4f7d52e741eca1457e3cbdc5b660f56e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.md
    sha256: 2bfa52bd01c7c612ea999043d1e7917a12e64364b265b4aaab6e92b0730ffa6d
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
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch063 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009256
targets:
- target_id: CultureMech:009256
  path: data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
  label: clostridium_kluyveri_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009256
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009256
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch063/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009256
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:009256
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T10:24:43.948797Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 98c0aaa787015c758fe1f7cde8d51cf0e263229f2a0fe37f2680cb73e22fcffc
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T10:24:43.948943Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 7dee06f544d931041a49255026a9046eada8cad7dfc3e7472798714f80fdd09a
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch063/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T10:18:58.431403Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: a4c1a232900d10667af421e992d10d0646ad1fc35695620e6f78f92361fd2392
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch063/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T10:18:59.420836Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 2bf8e5339938782d571b4991d31652dd0192a26ab4715fdb049bb0394eff4447
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch063/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T10:19:00.520852Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: f721011c192d9abf886e9e6710d1172e9b72bab510b9a2bafde0b18702352b21
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch063/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T10:19:01.315224Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: b92faa920a83ab7e32e7d5684f58c3344fc809c4c8d2cc21a216b31f794c3b03
- evidence_id: dsmz52
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T10:19:34.401080Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829
- evidence_id: api52
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/52
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T10:19:34.367950Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857
- evidence_id: togoM2703
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T10:19:34.353457Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: 4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a
- evidence_id: solution4178
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4178
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T10:19:34.106562Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da
- evidence_id: solution5543
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5543
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T10:19:33.995460Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:32.142841Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.971586Z'
  support: supports
  summary: OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition
    ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula
    ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.751160Z'
  support: supports
  summary: OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition
    ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O'];
    mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.727756Z'
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
  accessed_at: '2026-10-28T10:19:30.689442Z'
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
  accessed_at: '2026-10-28T10:19:30.141987Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16236
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16236
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.621780Z'
  support: supports
  summary: OLS current exact CHEBI:16236 = ethanol; definition ['A primary alcohol
    that is ethane in which one of the hydrogens is substituted by a hydroxy group.'];
    formula ['C2H6O']; mass ['46.069']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: afdacc5e401c6545f51974e897eb96eee2a5fa3aef15119edbd415cb7bb802b8
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.488008Z'
  support: supports
  summary: OLS current exact CHEBI:16526 = carbon dioxide; definition ['A one-carbon
    compound with formula CO<small><sub>2</sub></small> in which the carbon is attached
    to each oxygen atom by a double bond. A colourless, odourless gas under normal
    conditions, it is produced during respiration by all animals, fungi and microorganisms
    that depend directly or indirectly on living or decaying plants for food.']; formula
    ['CO2']; mass ['44.009']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.395462Z'
  support: supports
  summary: OLS current exact CHEBI:17439 = cyanocob(III)alamin; definition ['A complex
    cob(III)alamin in which cobalt is positioned in the centre of a planar corrin
    tetrapyrrole ring and bound axially to a 5,6-dimethylbenzimidazole moiety and
    a cyano group. It is one of several forms of the vitamin known as vitamin B12.'];
    formula ['C63H88CoN14O14P']; mass ['1355.388']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:30.086070Z'
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
  accessed_at: '2026-10-28T10:19:33.330685Z'
  support: supports
  summary: OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear
    parent hydride consisting of covalently bonded hydrogen and chlorine atoms.'];
    formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.152104Z'
  support: supports
  summary: OLS current exact CHEBI:17997 = dinitrogen; definition ['An elemental molecule
    consisting of two trivalently-bonded nitrogen atoms.']; formula ['N2']; mass ['28.014'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.133464Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:29.483875Z'
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
  accessed_at: '2026-10-28T10:19:29.483808Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:29.464528Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:29.454963Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:29.439234Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32029
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32029
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:33.023023Z'
  support: supports
  summary: OLS current exact CHEBI:32029 = potassium acetate; definition ['A potassium
    salt comprising equal numbers of potassium and acetate ions']; formula ['C2H3O2.K'];
    mass ['98.142']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: ad3a69b398a98d72cdfc8e281c5c5c37f25059baa7675ca20adc51928cf2ba2c
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:32.907460Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:32.737612Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:31.621412Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:31.454729Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:28.857969Z'
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
  accessed_at: '2026-10-28T10:19:32.634604Z'
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
  accessed_at: '2026-10-28T10:19:28.851616Z'
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
  accessed_at: '2026-10-28T10:19:28.097973Z'
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
  accessed_at: '2026-10-28T10:19:31.420360Z'
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
  accessed_at: '2026-10-28T10:19:31.350185Z'
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
  accessed_at: '2026-10-28T10:19:31.243797Z'
  support: supports
  summary: OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition
    ['A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O.'];
    formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:32.567332Z'
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
  accessed_at: '2026-10-28T10:19:32.426399Z'
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
  accessed_at: '2026-10-28T10:19:28.097826Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T10:19:28.097486Z'
  support: supports
  summary: OLS current exact CHEBI:91248 = L-cysteine hydrochloride hydrate; definition
    ['A hydrate that is the monohydrate form of <small>L</small>-cysteine hydrochloride.'];
    formula ['C3H7NO2S.H2O.HCl']; mass ['175.637']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T10:18:42.762591Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch063/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T10:24:43.962089Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 7d0cbac4208345b95808617a8118a7394c8f8d8df1df6ef44c99281f538230bf
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T10:24:43.962428Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 2bfa52bd01c7c612ea999043d1e7917a12e64364b265b4aaab6e92b0730ffa6d
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T10:24:43.962450Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 5e53044e4466908723e28767f4f70eab4f7d52e741eca1457e3cbdc5b660f56e
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch063/record05/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T10:24:43.962469Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: bc04dd15bba71adeb60e8b50bde0c9652b4e4ed82e2b788f7f47dbb52fd6de1b
- evidence_id: writer50
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962490Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace legacy secondary MIM links or
    authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer51
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962510Z'
  support: context_only
  summary: Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical
    quantities and flags conflicting quantities rather than summing them. Persisted
    old duplicate sums require independent source review; they do not establish that
    this current implementation still sums unequal stages.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer52
  kind: record_content
  reference: scripts/enrich_with_chebi.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962529Z'
  support: context_only
  summary: Current RecipeEnricher.enrich_ingredient skips already grounded terms and
    delegates ungrounded names to ChemicalMapper; enrich_recipe traverses ingredients
    and nested compositions, and enrich_file appends provenance. The wrapper does
    not independently verify supplied chemical forms or recipe amounts. ChemicalMapper
    internals were not added as a scientific authority.
  snapshot_sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
- evidence_id: writer53
  kind: record_content
  reference: scripts/migrate_chebi_regrounding.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962548Z'
  support: context_only
  summary: Current rewrite_entry applies exact from-ID plus ingredient-label remaps
    across primary and secondary slots, while migrate_file appends a change-specific
    history event. The generic nickel chloride remap does not distinguish its hydrate;
    current mappings require independent supplied-form review. This read does not
    establish historical execution.
  snapshot_sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
- evidence_id: writer54
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962567Z'
  support: context_only
  summary: Full _resolve_chebi/_rewrite_entry/migrate_file read. Existing primary
    CHEBI is reused if present in MIM; exact-name/synonym resolution is limited by
    a stereo-prefix guard, and unresolved links remain. The code does not prove chemical
    equivalence or historical validity merely because an ID has a current row.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer55
  kind: record_content
  reference: scripts/migrate_mgso4_heptahydrate_term.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962583Z'
  support: context_only
  summary: iter_ingredients and main make a label-conditional primary-term-only 32599
    to 31795 repair; secondary annotations are untouched. The current primary is credited
    while stale secondary linkage requires separate review.
  snapshot_sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
- evidence_id: writer56
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962602Z'
  support: context_only
  summary: Current _resolve_solution and _migrate_media_file identify stock references
    and move descriptors into solutions while preserving their stored concentration.
    The resolver selects a solution by normalized name and preserves the old concentration;
    neither operation proves source-specific stock equivalence. A generic Vitamin
    solution name can select an unrelated recipe. Current behavior does not prove
    the historical run.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer57
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962630Z'
  support: context_only
  summary: Current _parse_api_composition uses only the primary recipe and prefers
    provider g_l; it excludes recognized solvent names. The ml fallback maps to ML_PER_L,
    requiring an independent denominator check. _is_api_stock_addition recognizes
    explicit stock IDs and percentage attributes. _parse_preparation_steps collects
    prose from all solution sections without separate stage fields. These present
    behaviors do not establish historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer58
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962657Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer59
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962674Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer60
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962692Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer61
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962710Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T10:24:43.962729Z'
  support: context_only
  summary: Full apply_defaults/_fix_ingredient/_fix_solution read. The defaulter inserts
    VARIABLE concentrations and Unknown solution names to satisfy structure. These
    defaults are not evidence for a source dose, composition or final volume; copied
    historical default events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: dep63
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T10:24:43.962734Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
- evidence_id: dep64
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T10:24:43.962736Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
- evidence_id: dep65
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: explicit scoped stock rows in quantity inventory
  accessed_at: '2026-10-28T10:24:43.962737Z'
  support: supports
  summary: Current dependency read separately; only the stock composition named by
    the receiving source transfers. Earlier attached evidence and history retained;
    unrelated parent medium, doses, pH and growth do not transfer.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch063/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T10:24:44.081357Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 4230817b0ab74ea841889b862a25c59c40ae0f270ee5e302da8613f499ccc695
assessments:
- assessment_id: a1
  area: identity
  topic: Exact TOGO source and wrong generic vitamin link
  outcome: concern
  summary: TOGO M2703 explicitly names DSM 52 and its own seven-vitamin section agrees
    with the primary. Linked mediadive.solution:6241 instead has only cyanocobalamin,
    thiamine HCl and biotin in100 ml; it is not the seven-vitamin stock. Culture name
    is source identity, not a strain-specific experimental growth claim.
  target_ids:
  - CultureMech:009256
  evidence_ids:
  - togoM2703
  - dsmz52
  - solution6241
- assessment_id: a2
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Two old reports explicitly performed zero source checks; their flags are
    now assessed against current primary/API/TOGO evidence. Existing selected layers
    have no attached formulation claims. Fourteen attached stock claims authenticate
    current raw bytes, without recreating historical access times. Current TOGO code
    preserves stock sections and units; current cleanup does not sum unequal values,
    while name-only stock migration remains a source-identity risk. Current conservative
    merging preserves scientific fields and rejects incompatible formulations. Inspected
    writer behavior is described separately by exact file and function; it does not
    prove historical execution.
  target_ids:
  - CultureMech:009256
  evidence_ids:
  - history-auth
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
  - writer61
  - writer62
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 74 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:009256
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009256",
    "selected_concentration_field_count": 74, "selected_concentration_fields_covered":
    74, "decisions": [{"decision_id": "q1", "subject": "MgSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 0.2 g per
    displayed recipe, and API 52 explicitly reports g_l=0.2, equal to the stored value.
    Retain that declared normalization with exact evidence. The API volume is 1023
    ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus
    additions without a final-volume instruction. Do not silently recompute a measured
    final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.811438,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "MgSO4 x 7
    H2O                                              0.20         g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q2", "subject": "Yeast extract",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 1 g per
    displayed recipe, and API 52 explicitly reports g_l=1, equal to the stored value.
    Retain that declared normalization with exact evidence. The API volume is 1023
    ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus
    additions without a final-volume instruction. Do not silently recompute a measured
    final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 10-10", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Yeast extract                                              1.00         g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.23", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.23", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 0.23 g per
    displayed recipe, and API 52 explicitly reports g_l=0.23, equal to the stored
    value. Retain that declared normalization with exact evidence. The API volume
    is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water
    plus additions without a final-volume instruction. Do not silently recompute a
    measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.23,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.23,\n                        \"mmol_l\":
    1.69012,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "KH2PO4                                                     0.23         g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 0.25 g per
    displayed recipe, and API 52 explicitly reports g_l=0.25, equal to the stored
    value. Retain that declared normalization with exact evidence. The API volume
    is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water
    plus additions without a final-volume instruction. Do not silently recompute a
    measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    4.67377,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "NH4Cl                                                      0.25         g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject":
    "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.31", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.31", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 0.31 g per
    displayed recipe, and API 52 explicitly reports g_l=0.31, equal to the stored
    value. Retain that declared normalization with exact evidence. The API volume
    is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water
    plus additions without a final-volume instruction. Do not silently recompute a
    measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.31,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.31,\n                        \"mmol_l\":
    1.77981,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "K2HPO4                                                     0.31         g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject":
    "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 0.25 g per
    displayed recipe, and API 52 explicitly reports g_l=0.25, equal to the stored
    value. Retain that declared normalization with exact evidence. The API volume
    is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water
    plus additions without a final-volume instruction. Do not silently recompute a
    measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[13]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.04088,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Na2S x 9
    H2O                                               0.25         g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q7", "subject": "Na2CO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 1 g per
    displayed recipe, and API 52 explicitly reports g_l=1, equal to the stored value.
    Retain that declared normalization with exact evidence. The API volume is 1023
    ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus
    additions without a final-volume instruction. Do not silently recompute a measured
    final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[10]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    9.43503,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Na2CO3                                                     1.00         g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject":
    "K-acetate", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 10 g per
    displayed recipe, and API 52 explicitly reports g_l=10, equal to the stored value.
    Retain that declared normalization with exact evidence. The API volume is 1023
    ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water plus
    additions without a final-volume instruction. Do not silently recompute a measured
    final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"K-acetate\",\n                        \"compound_id\":
    86,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\":
    101.893,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 3-3", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "K-acetate                                                 10.00         g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject":
    "L-Cysteine-HCl x H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.25", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main recipe: source batch
    mass and provider-declared g_l", "interpretation": "The primary lists 0.25 g per
    displayed recipe, and API 52 explicitly reports g_l=0.25, equal to the stored
    value. Retain that declared normalization with exact evidence. The API volume
    is 1023 ml but g_l uses the nominal one-litre basis; the PDF lists 1000 ml water
    plus additions without a final-volume instruction. Do not silently recompute a
    measured final concentration from either number.", "sources": [{"locator": "$.data.solutions[0].recipe[12]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\":
    1.4234,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "L-Cysteine
    HCl x H2O                                       0.25         g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q10", "subject": "Water summed
    across four distinct preparation stages", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3990.0",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3990.0",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Main water and three separate
    stock batches", "interpretation": "3990 G_PER_L is an invalid sum of 1000 ml main
    water,990 ml SL10 water,1000 ml SeW water and 1000 ml vitamin water. Preserve
    each absolute water amount in its own stage; SL10 explicitly makes up to 1000
    ml. None is 3990 g/L in the receiving medium.", "sources": [{"locator": "$.data.solutions[0].recipe[14]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[2].recipe[3]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[7]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 54-54", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "make up to
    1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "Absolute ethanol addition", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path": "ingredients[8].concentration",
    "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Main liquid addition", "interpretation":
    "Both primary and TOGO specify20 ml ethanol, not20 g/L. Preserve an absolute20
    ml batch addition and source grade; any per-litre or mass conversion needs an
    explicit final-volume or density basis.", "sources": [{"locator": "$.data.solutions[0].recipe[9]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Ethanol absolute\",\n                        \"compound_id\":
    89,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.components[0].items[9]", "source_key": "togoM2703",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703",
    "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n          \"component_name\":
    \"Ethanol\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001114\",\n          \"gmo_id\": \"GMO_001114\",\n          \"label\":
    \"Ethanol\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Ethanol absolute                                          20.00        ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject":
    "Carbon dioxide gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Gas atmosphere at
    named preparation stages", "interpretation": "VARIABLE does not express the explicit
    gas proportions or stage. Main and carbonate use80% N2/20% CO2; vitamin and reducing
    stocks use100% N2. No dissolved-gas mass or concentration is inferred. Retain
    gas identity, remove ambiguous duplicate context only after source-scoped representation
    is established.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and
    sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min
    to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere
    in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate
    from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and vitamins from an anoxic and filter-sterilized stock solution prepared under
    100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0,
    if necessary.\"\n                    }", "quote_representation": "raw JSON object"},
    {"locator": "$.comments[10]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703",
    "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n      \"paragraph_index\":
    15,\n      \"comment\": \"Solution is prepared under 100% N2 gas and sterilized
    by filtration.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q13", "subject": "Nitrogen gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Gas atmosphere at
    named preparation stages", "interpretation": "VARIABLE does not express the explicit
    gas proportions or stage. Main and carbonate use80% N2/20% CO2; vitamin and reducing
    stocks use100% N2. No dissolved-gas mass or concentration is inferred. Retain
    gas identity, remove ambiguous duplicate context only after source-scoped representation
    is established.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and
    sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min
    to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere
    in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate
    from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and vitamins from an anoxic and filter-sterilized stock solution prepared under
    100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0,
    if necessary.\"\n                    }", "quote_representation": "raw JSON object"},
    {"locator": "$.comments[10]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703",
    "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n      \"paragraph_index\":
    15,\n      \"comment\": \"Solution is prepared under 100% N2 gas and sterilized
    by filtration.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q14", "subject": "N2 gas", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Gas atmosphere at
    named preparation stages", "interpretation": "VARIABLE does not express the explicit
    gas proportions or stage. Main and carbonate use80% N2/20% CO2; vitamin and reducing
    stocks use100% N2. No dissolved-gas mass or concentration is inferred. Retain
    gas identity, remove ambiguous duplicate context only after source-scoped representation
    is established.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and
    sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min
    to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere
    in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate
    from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and vitamins from an anoxic and filter-sterilized stock solution prepared under
    100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0,
    if necessary.\"\n                    }", "quote_representation": "raw JSON object"},
    {"locator": "$.comments[10]", "source_key": "togoM2703", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2703",
    "source_raw_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "source_text_sha256": "4993feb6b611e3b4b3bf9c0770ce2aaf4985e36e73aeee910cfebb049354e34a",
    "accessed_at": "2026-10-28T10:19:34.353457Z", "exact_source_quote": "{\n      \"paragraph_index\":
    15,\n      \"comment\": \"Solution is prepared under 100% N2 gas and sterilized
    by filtration.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q15", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "36", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "36", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    36 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.036 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[8]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "6", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    6 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.006 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[4]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    100 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.1 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[3]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "190", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "190", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    190 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.19 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "24", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "24", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    24 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.024 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[7]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    2 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.002 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "70", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "70", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    70 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.07 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "HCl (25%; 7.7 M)", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "10", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    10 ml for this component, separately from its1 ml receiving dose. Keep the 10
    ml HCl stock addition with 25% primary notation and separate TOGO7.7M notation;
    do not turn it into10 g/L or infer a percent basis/density.", "sources": [{"locator":
    "$.data.solutions[1].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "$.data.solutions[0].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Trace element solution SL-10 stock,
    not main medium", "interpretation": "Source Trace element solution SL-10 lists
    1.5 g for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 1.5 g/L. The number matches a stock rate but is placed directly
    in the medium. Restore the stock composition and receiving dose separately. No
    final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[1].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "Na2SeO3 x 5 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate solution stock,
    not main medium", "interpretation": "Source Selenite-tungstate solution lists
    3 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.003 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[2].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Na2WO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "original": {"value": "4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "4", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate solution stock,
    not main medium", "interpretation": "Source Selenite-tungstate solution lists
    4 mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.004 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[2].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "NaOH", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate solution stock,
    not main medium", "interpretation": "Source Selenite-tungstate solution lists
    0.5 g for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.5 g/L. The number matches a stock rate but is placed directly
    in the medium. Restore the stock composition and receiving dose separately. No
    final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[2].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "80", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "80", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 80 mg
    for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.08 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[1]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 100
    mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.1 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[4]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "300", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "300", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 300
    mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.3 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[5]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[28].concentration", "original": {"value": "100", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "100", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 100
    mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.1 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[0]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[29].concentration", "original": {"value": "200", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 200
    mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.2 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[3]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q32", "subject": "Thiamine-HCl x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "200", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 200
    mg for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.2 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[6]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "D(+)-Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml", "field_path":
    "ingredients[31].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Seven vitamins solution stock,
    not main medium", "interpretation": "Source Seven vitamins solution lists 20 mg
    for this component, separately from its1 ml receiving dose. Its provider-declared
    stock rate is 0.02 g/L. The retained same digits were milligrams in the source,
    not grams per litre. Restore the stock composition and receiving dose separately.
    No final-medium rate is asserted without a final-volume basis.", "sources": [{"locator":
    "$.data.solutions[3].recipe[2]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[11]", "source_key":
    "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "Receiving dose Sodium
    resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation":
    "The primary adds0.5 ml, not the stored0.5 G_PER_L. Preserve the absolute batch
    dose and named stock. The resazurin stock is explicitly0.1% w/v;0.5 ml contains0.5
    mg, but that does not establish a final-medium denominator.", "sources": [{"locator":
    "$.data.solutions[0].recipe[8]", "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Sodium resazurin
    (0.1% w/v)                                0.50        ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q35", "subject": "Receiving dose
    Trace element solution SL-10", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation":
    "The primary adds1 ml, not the stored1 G_PER_L. Preserve the absolute batch dose
    and named stock. Do not double count its components as direct medium ingredients.",
    "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api52",
    "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Trace element
    solution SL-10                               1.00        ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q36", "subject": "Receiving dose
    Selenite-tungstate solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation":
    "The primary adds1 ml, not the stored1 G_PER_L. Preserve the absolute batch dose
    and named stock. Do not double count its components as direct medium ingredients.",
    "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api52",
    "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Selenite-tungstate
    solution                                1.00        ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q37", "subject": "Receiving dose
    Seven vitamins solution", "local_fields": [{"record_path": "data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml",
    "field_path": "solutions[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml",
    "field_path": "solutions[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Main stock addition", "interpretation":
    "The primary adds1 ml, not the stored1 G_PER_L. Preserve the absolute batch dose
    and named stock. Do not double count its components as direct medium ingredients.",
    "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api52",
    "reference": "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "source_text_sha256":
    "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857", "accessed_at":
    "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 14-14", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "Seven vitamins
    solution                                    1.00        ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q38", "subject": "solution4178
    HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Separately scoped linked stock",
    "interpretation": "Provider reports2.5 g/L for10 ml HCl labelled25%,7.7M. The
    percent basis is unspecified and 7.7M is a distinct supplied-stock declaration;
    neither validates a simple2.5 g/L interpretation without resolving this inconsistency.
    Retain exact10 ml and source attributes, leaving derived mass rate unresolved.",
    "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\":
    10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\":
    68.5683,\n                \"optional\": 0\n            }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q39", "subject": "solution4178 FeCl2 x
    4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[1].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\":
    260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q40", "subject": "solution4178 ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\":
    64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q41", "subject": "solution4178 MnCl2 x 4 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q42", "subject": "solution4178 H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[4].concentration", "original": {"value": "0.006", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[4]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q43", "subject": "solution4178 CoCl2 x 6 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[5].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[5]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q44", "subject": "solution4178 CuCl2 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[6].concentration", "original": {"value": "0.002", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[6]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\":
    39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q45", "subject": "solution4178 NiCl2 x 6 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[7].concentration", "original": {"value": "0.024", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[7]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q46", "subject": "solution4178 Na2MoO4 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[8].concentration", "original": {"value": "0.036", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[8]", "source_key": "solution4178", "reference":
    "https://mediadive.dsmz.de/rest/solution/4178", "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q47", "subject": "solution4178 Distilled water", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[9].concentration", "original": {"value": "990", "unit":
    "PERCENT_V_V"}}], "decision": "correct", "stage": "Separately scoped linked stock",
    "interpretation": "990 ml water is an absolute stock batch input, not990%v/v.
    Preserve the volume; the selected DSM 52 stock independently adds an explicit
    make-up-to 1000 ml instruction.", "sources": [{"locator": "$.data.recipe[9]",
    "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178",
    "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n                \"recipe_order\":
    10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text
    lines 54-54", "source_key": "dsmz52", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "make up to
    1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q48", "subject": "solution4178 placeholder", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder
    only", "interpretation": "The source has a real composition; VARIABLE placeholder
    is not an ingredient amount. Reconcile the stale incomplete_composition flag and
    placeholder without deleting verified composition evidence.", "sources": [{"locator":
    "$.data", "source_key": "solution4178", "reference": "https://mediadive.dsmz.de/rest/solution/4178",
    "source_raw_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "source_text_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da",
    "accessed_at": "2026-10-28T10:19:34.106562Z", "exact_source_quote": "{\n        \"id\":
    4178,\n        \"name\": \"Trace element solution SL-10\",\n        \"volume\":
    1000,\n        \"recipe\": [\n            {\n                \"recipe_order\":
    1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\":
    10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\":
    68.5683,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\":
    2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\":
    260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\":
    \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 6,\n                \"compound\":
    \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 7,\n                \"compound\":
    \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 8,\n                \"compound\":
    \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 9,\n                \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 10,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\":
    null,\n                \"step\": \"Dissolve FeCl2 x 4H2O first in HCl. Then dilute
    in distilled water and add the remaining salts.\"\n            }\n        ],\n        \"equipment\":
    []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49",
    "subject": "solution5543 NaOH", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution5543", "reference":
    "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"NaOH\",\n                \"compound_id\":
    256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q50", "subject": "solution5543 Na2SeO3 x 5 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
    "field_path": "composition[1].concentration", "original": {"value": "0.003", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[1]", "source_key": "solution5543", "reference":
    "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\":
    107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q51", "subject": "solution5543 Na2WO4 x 2 H2O", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "0.004", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[2]", "source_key": "solution5543", "reference":
    "https://mediadive.dsmz.de/rest/solution/5543", "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\":
    249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q52", "subject": "solution5543 Distilled water", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "1", "unit":
    "L"}}], "decision": "verified", "stage": "Separately scoped linked stock", "interpretation":
    "Existing attached claim matches this exact current raw payload digest and literal
    source object. Retain its declared stock concentration or absolute water addition;
    this does not authenticate any receiving-medium concentration.", "sources": [{"locator":
    "$.data.recipe[3]", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543",
    "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q53", "subject": "solution5543 placeholder", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder
    only", "interpretation": "The source has a real composition; VARIABLE placeholder
    is not an ingredient amount. Reconcile the stale incomplete_composition flag and
    placeholder without deleting verified composition evidence.", "sources": [{"locator":
    "$.data", "source_key": "solution5543", "reference": "https://mediadive.dsmz.de/rest/solution/5543",
    "source_raw_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "source_text_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882",
    "accessed_at": "2026-10-28T10:19:33.995460Z", "exact_source_quote": "{\n        \"id\":
    5543,\n        \"name\": \"Selenite-tungstate solution\",\n        \"volume\":
    1000,\n        \"recipe\": [\n            {\n                \"recipe_order\":
    1,\n                \"compound\": \"NaOH\",\n                \"compound_id\":
    256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\":
    \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [],\n        \"equipment\": []\n    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject":
    "solution6241 Cyanocobalamine", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field_path": "composition[0].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Separately scoped linked stock",
    "interpretation": "Existing attached claim matches this exact current raw payload
    digest and literal source object. Retain its declared stock concentration or absolute
    water addition; this does not authenticate any receiving-medium concentration.",
    "sources": [{"locator": "$.data.recipe[0]", "source_key": "solution6241", "reference":
    "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q55", "subject": "solution6241 Thiamine HCl", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field_path":
    "composition[1].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "Separately scoped linked stock", "interpretation":
    "Existing attached claim matches this exact current raw payload digest and literal
    source object. Retain its declared stock concentration or absolute water addition;
    this does not authenticate any receiving-medium concentration.", "sources": [{"locator":
    "$.data.recipe[1]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q56", "subject": "solution6241 Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field_path": "composition[2].concentration", "original": {"value": "2000.0",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separately scoped linked
    stock", "interpretation": "200micrograms=0.0002 g in an explicit100 ml final stock,
    so0.002 g/L, not2000 g/L. This stock is nevertheless the wrong vitamin recipe
    for DSM 52 and must not replace its seven-vitamin source.", "sources": [{"locator":
    "$.data.recipe[2]", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.steps[0]",
    "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q57", "subject":
    "solution6241 Distilled water", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field_path": "composition[3].concentration", "original": {"value": "1000.0",
    "unit": "PERCENT_V_V"}}], "decision": "correct", "stage": "Separately scoped linked
    stock", "interpretation": "The source makes up to 100 ml with water. Preserve
    that final-stock make-up instruction, not1000%v/v or an independently measured
    water dose.", "sources": [{"locator": "$.data.recipe[3]", "source_key": "solution6241",
    "reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_raw_sha256":
    "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "source_text_sha256":
    "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "accessed_at":
    "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.steps[0]",
    "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q58", "subject":
    "solution6241 placeholder", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Legacy placeholder
    only", "interpretation": "The source has a real composition; VARIABLE placeholder
    is not an ingredient amount. Reconcile the stale incomplete_composition flag and
    placeholder without deleting verified composition evidence.", "sources": [{"locator":
    "$.data", "source_key": "solution6241", "reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_raw_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "source_text_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "accessed_at": "2026-10-28T10:18:42.762591Z", "exact_source_quote": "{\n        \"id\":
    6241,\n        \"name\": \"Vitamin solution\",\n        \"volume\": 100,\n        \"recipe\":
    [\n            {\n                \"recipe_order\": 2,\n                \"compound\":
    \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }\n        ],\n        \"equipment\":
    []\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q59",
    "subject": "Primary preparation, pH and conditional reducing supplement", "local_fields":
    [], "decision": "evidence_only", "stage": "Main preparation and conditional source-only
    control", "interpretation": "Restore source pH 6.8–7.0,30–45 min sparging, the
    80/20 and 100% gas stages, ordering of ethanol/autoclaving/carbonate/vitamins/reducing
    agents and anoxic filtration. The10–20 mg/L sodium dithionite from 5% w/v is conditional
    on incomplete reduction, not an unconditional ingredient or guessed dose.", "sources":
    [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api52", "reference":
    "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve all ingredients (except ethanol, carbonate, vitamins, cysteine and
    sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min
    to make it anoxic. Add ethanol, then dispense medium under same gas atmosphere
    in Hungate-type tubes or serum vials and autoclave. After autoclaving, add carbonate
    from a sterile stock solution prepared under 80% N2 and 20% CO2 gas atmosphere
    and vitamins from an anoxic and filter-sterilized stock solution prepared under
    100% N2 gas. Before inoculation, add cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Adjust pH of medium to 6.8 - 7.0,
    if necessary.\"\n                    }", "quote_representation": "raw JSON object"},
    {"locator": "$.data.solutions[0].steps[1]", "source_key": "api52", "reference":
    "https://mediadive.dsmz.de/rest/medium/52", "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: If reduction of medium is not complete after inoculation, add 10 - 20
    mg/l sodium dithionite from a 5% w/v solution freshly prepared under 100% N2 gas
    and filter sterilized.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q60", "subject": "SL10 preparation and final
    stock volume", "local_fields": [], "decision": "evidence_only", "stage": "SL10
    only", "interpretation": "Dissolve FeCl2 first in HCl, dilute and dissolve remaining
    compounds, then make up to 1000 ml. This explicit stock volume does not establish
    the final volume of the main medium.", "sources": [{"locator": "$.data.solutions[1].steps[0]",
    "source_key": "api52", "reference": "https://mediadive.dsmz.de/rest/medium/52",
    "source_raw_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "source_text_sha256": "c3795f9082cc0a0bb7e3b590ddb9d7bbd91b9123890f315ddf11efd64d74a857",
    "accessed_at": "2026-10-28T10:19:34.367950Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 54-54", "source_key": "dsmz52",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium52.pdf",
    "source_raw_sha256": "cbdec1c64e8b478d408c114625393df2e2b59612a39f575d6e38faacca656829",
    "source_text_sha256": "6283308d3a9cabf4927b4e177cb7fa32790d34f2a3fad434ff81944daa422807",
    "accessed_at": "2026-10-28T10:19:34.401080Z", "exact_source_quote": "make up to
    1000.00 ml.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch063/record05/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml: primary 30/33,
    secondary 27/33; data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml:
    primary 30/33, secondary 27/33. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    2 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:009256
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
  - CultureMech:009256
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
  - CultureMech:009256
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009256-stock-stage-and-liquid-unit-corruption
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock quantities and liquid additions have become direct mass concentrations
  description: Water3990 G_PER_L combines four preparation batches. Stock milligram
    amounts became equal-digit G_PER_L, and other stock rates were flattened directly.
    Ethanol20 ml and four stock additions were stored as G_PER_L. These are explicit
    unit/stage defects, while nine ordinary main rates are credited only as provider-declared
    nominal normalization.
  target_ids:
  - CultureMech:009256
  field_paths:
  - ingredients
  - solutions[*].concentration
  evidence_ids:
  - dsmz52
  - api52
  - togoM2703
  rule_id: review-yaml-record/source-unit-and-stock-stage
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-009256-wrong-vitamin-stock-reference
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generic vitamin name resolves to an unrelated stock
  description: The selected Vitamin solution points to solution6241, a three-vitamin100
    ml stock, whereas DSM 52/TOGO M2703 define seven vitamins. Matching a generic
    label does not establish recipe identity.
  target_ids:
  - CultureMech:009256
  field_paths:
  - solutions[3].term
  - solutions[3].notes
  evidence_ids:
  - dsmz52
  - togoM2703
  - solution6241
  rule_id: review-yaml-record/exact-stock-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-009256-missing-staged-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and pH are absent
  description: Neither selected layer retains preparation or pH, although the source
    specifies separate sterilization, anoxic additions, pH range and a conditional
    reducing supplement. VARIABLE gases do not retain these stage-specific controls.
  target_ids:
  - CultureMech:009256
  field_paths:
  - preparation_steps
  - ph_range
  - evidence
  evidence_ids:
  - dsmz52
  - api52
  - togoM2703
  rule_id: review-yaml-record/source-preparation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-009256-hydrate-and-secondary-form-disagreement
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and magnesium secondary mapping disagree with source forms
  description: Nickel hexahydrate asserts anhydrous CHEBI:34887 in both selected slots
    and the SL10 dependency. Magnesium primary31795 correctly records heptahydrate
    but secondary32599 remains anhydrous. Calcium pantothenate source stereochemistry
    is unspecified; its D-associated current term is a mapping limit, not permission
    to change the supplied material.
  target_ids:
  - CultureMech:009256
  field_paths:
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  - ingredients[1].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml::composition[7].chebi_term
  evidence_ids:
  - chebi34887
  - chebi31795
  - chebi32599
  - chebi31345
  - grounding
  - dsmz52
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    role: 'SL10 stock dependency: nickel mapping only'
- finding_id: f5
  issue_key: culturemech-009256-linked-stock-residual-unit-artifacts
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Linked stocks retain liquid and microgram artifacts despite earlier partial
    repairs
  description: SL10 water 990%v/v and the vitamin stock water 1000%v/v are not source
    volumes; vitamin biotin2000 g/L conflicts with 200micrograms made up to 100 ml.
    HCl derived2.5 g/L remains unsupported by its mixed25%/7.7M declarations. Fourteen
    previously attached stock claims remain authenticated and must be retained. Placeholder
    ingredients and incomplete flags are separate stale metadata.
  target_ids:
  - CultureMech:009256
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml::composition[0].concentration
  - data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml::composition[9].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[2].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[3].concentration
  - data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::ingredients[0]
  evidence_ids:
  - solution4178
  - solution5543
  - solution6241
  rule_id: review-yaml-record/scoped-stock-unit-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    role: Explicit linked stock dependency, only fields named in finding
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
    role: Explicit linked stock dependency, only fields named in finding
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: Explicit linked stock dependency, only fields named in finding
- finding_id: f6
  issue_key: culturemech-009256-legacy-acetate-secondary-link
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Potassium acetate retains an unresolved legacy secondary identifier
  description: Both layers retain MediaIngredientMech000580, which has no exact row
    in the pinned current CSV. Correct primary CHEBI:32029 remains supported. Current
    absence is not evidence the historical identifier was invalid.
  target_ids:
  - CultureMech:009256
  field_paths:
  - ingredients[9].mediaingredientmech_term
  evidence_ids:
  - grounding
  - chebi32029
  rule_id: review-yaml-record/current-secondary-link-resolution
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Rebuild the main recipe and three stock compositions from exact source
    sections; restore liquid units and doses, avoid stock double counting, and retain
    the stated main-volume uncertainty.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
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
  description: Replace the wrong reference with a source-verified seven-vitamin definition
    or inline stock composition. Preserve6241 as a distinct record; do not overwrite
    it with the receiving recipe.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
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
  description: Restore source-specific preparation and root evidence scoped to each
    solution dose and preparation stage. Keep the conditional dithionite addition
    conditional.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
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
  description: Resolve exact hydrate mappings and align the stale magnesium secondary
    link with the already-correct primary. Preserve generic source stereochemistry
    where not specified; do not infer hydrate molarities from provider mmol_l.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    role: 'SL10 stock dependency: nickel mapping only'
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Repair only the demonstrated dependency fields with source-scoped evidence,
    retaining fourteen correct earlier claims. Keep6241 separate from DSM 52 and do
    not transfer a whole uncorrected stock automatically.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    role: Explicit linked stock dependency, only fields named in finding
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
    role: Explicit linked stock dependency, only fields named in finding
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: Explicit linked stock dependency, only fields named in finding
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action6
  description: Reconcile the legacy secondary link against the exact current potassium
    acetate record, preserving the old history and already-correct primary identity.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2703_Clostridium_Kluyveri_Medium.yaml
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
- The PDF lists main water and additions without an explicit final-medium volume;
  API 52 declares volume1023 ml while its g_l follows a nominal litre. No measured
  final concentrations are inferred.
- Source recipes establish a formulation and named-medium identity, not strain-specific
  experimental growth. Calcium pantothenate stereochemistry and the HCl percent/molar
  conversion remain bounded unresolved details.
- The current packaged MIM snapshot is pinned by commit and exact CSV rows. Current
  absence does not establish historical invalidity; no record was edited.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
