# Chromohalobacter medium: retain authenticated owner evidence and the solid-medium variant

- Review: 20261028T094612Z-batch062-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:27:37.498108Z
- Finished UTC: 2026-10-28T09:46:12.825478Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All eleven provider-declared main-recipe concentrations agree with the maintained owner, including conditional agar. The generated copy is stale: it lost the owner’s authenticated ingredient evidence and October curation. Source water/preparation linkage and the two unmapped complex ingredients still need bounded curation.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch062 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000856 | data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml | generated | chromohalobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000856 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:000856 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:000856 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:000856 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact source and maintained owner

identity: supported. Targets: CultureMech:000856.

DSM1395 identity, selected stable ID and sole maintained contributor agree. This review concerns the existing solid-agar variant; the source also allows a liquid variant.

### Complex solid variant

consistency: supported. Targets: CultureMech:000856.

Peptone and yeast extract support COMPLEX/UNDEFINED. Conditional agar is expressly represented and SOLID_AGAR is supported; no forced liquid classification or strain-level growth inference follows.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:000856.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "NaCl", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 41,\n                        \"unit\": \"g\",\n                        \"g_l\": 41,\n                        \"mmol_l\": 701.574,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "NaCl", "compound_id": 43, "amount": 41, "unit": "g", "g_l": 41, "mmol_l": 701.574, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " NaCl                                                        41.000        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "41", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "41", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q2", "topic": "MgCl2 x 6 H2O", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 7,\n                        \"unit\": \"g\",\n                        \"g_l\": 7,\n                        \"mmol_l\": 34.4314,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "MgCl2 x 6 H2O", "compound_id": 79, "amount": 7, "unit": "g", "g_l": 7, "mmol_l": 34.4314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " MgCl2 x 6 H2O                                                7.000        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "7", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "7", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q3", "topic": "MgSO4 x 7 H2O", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 9.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.6,\n                        \"mmol_l\": 38.949,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 9.6, "unit": "g", "g_l": 9.6, "mmol_l": 38.949, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " MgSO x 7 H2O                                                 9.600        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "9.6", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "9.6", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q4", "topic": "CaCl2 x 2 H2O", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.36,\n                        \"mmol_l\": 2.44873,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.36, "unit": "g", "g_l": 0.36, "mmol_l": 2.44873, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " CaCl2 x 2 H2O                                                0.360        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.36", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.36", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q5", "topic": "KCl", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 26.8276,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "KCl", "compound_id": 61, "amount": 2, "unit": "g", "g_l": 2, "mmol_l": 26.8276, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " KCl                                                          2.000        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q6", "topic": "NaHCO3", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.714226,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "NaHCO3", "compound_id": 55, "amount": 0.06, "unit": "g", "g_l": 0.06, "mmol_l": 0.714226, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " NaHCO3                                                       0.060        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q7", "topic": "NaBr", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\": 0.026,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.026,\n                        \"mmol_l\": 0.252697,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "NaBr", "compound_id": 353, "amount": 0.026, "unit": "g", "g_l": 0.026, "mmol_l": 0.252697, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " NaBr                                                         0.026        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.026", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.026", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q8", "topic": "Peptone", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Peptone", "compound_id": 1, "amount": 5, "unit": "g", "g_l": 5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " Peptone                                                      5.000        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q9", "topic": "Yeast extract", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Yeast extract", "compound_id": 16, "amount": 10, "unit": "g", "g_l": 10, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 12; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " Yeast Extract                                               10.000        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q10", "topic": "Glucose", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Glucose", "compound_id": 5, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 5.55062, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 13; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " Glucose                                                      1.000        g"}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume.  Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q11", "topic": "Agar", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound": "Agar", "compound_id": 3, "condition": "for solid medium", "amount": 20, "unit": "g", "g_l": 20, "mmol_l": 59.4654, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 19; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": "20.0 g/l agar."}], "decision": "mixed", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. Agar is explicitly conditional on the solid variant, matching local SOLID_AGAR and the retained note.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. Agar is explicitly conditional on the solid variant, matching local SOLID_AGAR and the retained note. The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly supplies this main-recipe g_l value. Retain the amount; the primary mass table and water input alone would not prove final volume. Agar is explicitly conditional on the solid variant, matching local SOLID_AGAR and the retained note. Its existing exact attached JSON quotation and cited raw digest independently match the fresh capture."}]}, {"quantity_id": "q12", "topic": "Primary water input", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "PDF extracted line 14; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": " Distilled Water                                           1000.000       ml"}], "decision": "add", "rationale": "The water input is absent from the local formulation/preparation; adding it must preserve its source batch basis.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "MIX", "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."}], "decision": "add", "rationale": "Retain existing instruction and append a scoped water-input instruction supported by the source; do not turn the 1000 ml solvent input into a made-up final-volume assertion."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "MIX", "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."}], "decision": "add", "rationale": "Retain existing instruction and append a scoped water-input instruction supported by the source; do not turn the 1000 ml solvent input into a made-up final-volume assertion."}]}, {"quantity_id": "q13", "topic": "pH and autoclaving; conditional solidification", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:44.129613Z", "quote": "{\n                        \"step\": \"Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.\"\n                    }", "exact_decoded_object": {"step": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:44.371166Z", "quote": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding\n20.0 g/l agar."}], "decision": "evidence_only", "rationale": "Retain pH7.0, autoclaving and conditional20g/L agar. No autoclave temperature, duration, strain or growth temperature is supplied or inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "The existing pH and complete instruction are supported; attach claim-scoped source evidence at the root evidence slot without fabricating nested preparation evidence."}, {"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.", "decision": "evidence_only", "rationale": "The existing pH and complete instruction are supported; attach claim-scoped source evidence at the root evidence slot without fabricating nested preparation evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "The existing pH and complete instruction are supported; attach claim-scoped source evidence at the root evidence slot without fabricating nested preparation evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0 g/l agar.", "decision": "evidence_only", "rationale": "The existing pH and complete instruction are supported; attach claim-scoped source evidence at the root evidence slot without fabricating nested preparation evidence."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:000856.

All nine existing CHEBI identities and both repeated primary/secondary slots resolve with current canonical labels. Peptone and yeast extract remain unmapped mixtures. The PDF’s MgSO wording is retained literally; API MgSO4 and current CHEBI31795 support the stored heptahydrate, without rewriting the primary quotation.

### History and evidence scope

provenance: concern. Targets: CultureMech:000856.

All three exact historical reports were read; the thirteen October source objects and the complete cited raw digest match the fresh API response. All eleven attached owner quotations are authenticated as response content. Historical access events are not rerun. The selected merge predates and loses the owner repair, which must be retained.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:000856.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:000856.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Regenerate authenticated owner evidence

major / open / confirmed; issue key: culturemech-000856-regenerate-authenticated-owner-evidence.

The maintained contributor already carries eleven source-specific ingredient quotations and an October reference/curation event. Each literal quotation and the cited API raw digest match the independent current response. The selected August merge lacks these evidence lists, reference and later event despite retaining all amounts. Credit the existing repair and regenerate the sole contributor with the current evidence-preserving merge; do not repeat the quantity edits.

### f2: Link water and preparation at supported scope

minor / open / confirmed; issue key: culturemech-000856-link-water-and-preparation-at-supported-scope.

The source specifies a 1000 ml distilled-water input, pH7.0 and autoclaving. The local preparation retains pH/autoclaving/conditional agar but lacks the water input and root claim evidence. Add the water input as a batch quantity and root evidence that identifies the exact preparation fields; do not invent a final volume or absent sterilization settings.

### f3: Resolve the two complex-ingredient links

minor / open / confirmed; issue key: culturemech-000856-resolve-the-two-complex-ingredient-links.

Peptone and yeast extract have supported amounts and mixture identities but no primary or secondary ontology linkage. Current catalog candidates are lookup leads only; do not substitute a chemically defined compound or infer composition. Existing nine CHEBI identifiers and canonical labels resolve in current OLS.

## Recommended Actions And Acceptance Checks

### action1

Preserve all eleven already-supported owner quantities and evidence; regenerate the target so exact ingredient evidence, reference and appended curation survive. Confirm current merge output retains the solid-medium condition.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Append the exact water-input context and scoped root evidence for the retained preparation. Keep the existing pH and agar condition; make no final-volume, time or temperature claim not supplied by the source.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Verify an appropriate current mixture identifier for each unmapped ingredient and record its exact canonical label and mapping provenance; preserve the supported amounts and mixture status.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/chromohalobacter_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch062/record03/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/chromohalobacter_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 13 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chromohalobacter_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-reader | REVIEW_WORK/batch062/record03/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| attached-evidence-joins | REVIEW_WORK/batch062/record03/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| dsm1395 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf; Exact source identity and scoped formulation/preparation | supports | Complete primary DSM1395 page, table and preparation visually read. The printed magnesium-sulfate line says MgSO x7 H2O, whereas the current API explicitly says MgSO4 x7 H2O. The primary water input is not an explicit measured final volume. |
| api1395 | https://mediadive.dsmz.de/rest/medium/1395; Exact source identity and scoped formulation/preparation | supports | Complete current official provider response; all eleven g_l fields, solid-medium agar condition, water and preparation read. The raw digest matches the owner’s October reference and historical report. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63004; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch062/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch062/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch062/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch062/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch062/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch062/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch062/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch062/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch062/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The primary PDF prints MgSO x7 H2O without the sulfate subscript4. The API explicitly supplies MgSO4 x7 H2O; this source difference is disclosed rather than silently rewriting the quotation.
- Provider g_l fields support nominal main-recipe rates;1000 ml water is not an independently measured final volume. No stock-dilution or experimental-performance claim is inferred.
- Peptone and yeast-extract linkage remains unresolved here; no unverified candidate identifier is endorsed.
- The source has no strain-level growth demonstration or sterilization duration/temperature. Current term and reference diagnostics do not provide such evidence.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T094612Z-batch062-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Chromohalobacter medium: retain authenticated owner evidence and the solid-medium
  variant'
started_at: '2026-10-28T09:27:37.498108Z'
finished_at: '2026-10-28T09:46:12.825478Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'All eleven provider-declared main-recipe concentrations agree with the maintained
  owner, including conditional agar. The generated copy is stale: it lost the owner’s
  authenticated ingredient evidence and October curation. Source water/preparation
  linkage and the two unmapped complex ingredients still need bounded curation.'
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
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
    sha256: ef4979f6ae2638360ed5e490e7dd632015d40e7370e9fecdd08da2f601259849
    role: target
  - path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    sha256: 0d05c68e004e009a33e9bad8e6e5f0287e81fa20372e9384dff2dedcd48744c0
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/chromohalobacter_medium.yaml.md
    sha256: 947610c31f1ea85a14f777ba296613e679be93dc2114d56bb2a9315898a82d5b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.md
    sha256: 2961b5512eff989ae26c6855904760eb138932f5284d02ef6ae55b89db789507
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chromohalobacter_medium.md
    sha256: 3f29328c80a4d5731b125f8b648367b524f8ed1a72b4bd62794c7433b2f18806
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
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
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
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
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch062 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000856
targets:
- target_id: CultureMech:000856
  path: data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
  label: chromohalobacter_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:000856
  command: just validate-schema data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:000856
  command: just validate-strict data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
    --out REVIEW_WORK/batch062/record03/strict.tsv --workers 1
  exit_code: 0
  evidence_ids:
  - validate-strict
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:000856
  command: just validate-terms data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Native reference checker performed zero reference checks; this is not claim
    authentication.
  target_ids:
  - CultureMech:000856
  command: just validate-references data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: ef4979f6ae2638360ed5e490e7dd632015d40e7370e9fecdd08da2f601259849
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 0d05c68e004e009a33e9bad8e6e5f0287e81fa20372e9384dff2dedcd48744c0
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch062/record03/identity-search.json
  accessed_at: '2026-10-28T09:37:49.901772Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: ddb45da42621525c5511f43f4d9243c468d4d6404240627f77a15d7b89491b37
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/chromohalobacter_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    13 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 947610c31f1ea85a14f777ba296613e679be93dc2114d56bb2a9315898a82d5b
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 2961b5512eff989ae26c6855904760eb138932f5284d02ef6ae55b89db789507
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chromohalobacter_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 3f29328c80a4d5731b125f8b648367b524f8ed1a72b4bd62794c7433b2f18806
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch062/record03/historical-reader.json
  accessed_at: '2026-10-28T09:37:49.904558Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: ba9107f974bced927af96605c79b29599e481fba3045316ce68d2677fc1cce7e
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Current composition parser restricts ingredients to the primary solution,
    excludes solvent and recognized stock additions, and retains explicit g_l. The
    solution parser preserves referenced or percent-defined stocks and source attributes.
    Preparation parsing still concatenates all solution steps into root preparation_steps;
    source-stage annotation remains important. These present functions do not prove
    the historical execution that produced this record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Current compatibility preserves scientific fields and list order and rejects
    unequal formulations; only specified provenance/evidence lists are unioned. It
    performs no concentration conversion or stock expansion and does not authenticate
    historical merges.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients, merge_ingredient_group
  accessed_at: '2026-10-28T09:37:49.854306Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch062/record03/attached-evidence-joins.json
  accessed_at: '2026-10-28T09:37:49.904926Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: b9591f61cfbd1278c650fba073712f7e9e5e82a21b57b2a94a43e01bf1ed4242
- evidence_id: dsm1395
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:44.371166Z'
  support: supports
  summary: Complete primary DSM1395 page, table and preparation visually read. The
    printed magnesium-sulfate line says MgSO x7 H2O, whereas the current API explicitly
    says MgSO4 x7 H2O. The primary water input is not an explicit measured final volume.
  snapshot_sha256: 98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca
- evidence_id: api1395
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1395
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:44.129613Z'
  support: supports
  summary: Complete current official provider response; all eleven g_l fields, solid-medium
    agar condition, water and preparation read. The raw digest matches the owner’s
    October reference and historical report.
  snapshot_sha256: a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.403037Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:49.006017Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.844386Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:48.524475Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.994811Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.941682Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi63004
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63004
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:47.499788Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a541ff82243b2a3bb4c2b908cb3758c8c1acddad55e8b45010130907d345d23c
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:44.736109Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d78d31a7829da999c31ae102da842c5b5c37a5d334be6389539d92ecd786de7
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.320537Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch062/record03/quantity-inventory.json
  accessed_at: '2026-10-28T09:37:49.917542Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 50999d19bdd6c7b6876d3f80250da4887ed3171ecc275ca7197d515b1ccd67b6
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch062/record03/grounding-inventory.json
  accessed_at: '2026-10-28T09:37:49.917584Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 0c79264d705d7ee72dc84f38b7c01e021d08a0167d75e912a1f28eb36c8022d5
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch062/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T09:37:49.917638Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 6c795a61b13b9b55c86d7f61f85954b0b4f60a5479008721b26f73f988f9a669
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch062/record03/scalar-census.json
  accessed_at: '2026-10-28T09:37:49.917666Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: c8777ec3ea015aed92ae43148ec50f69af4badc512b40d62ab9ced9f77333780
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record03/validate-schema.json
  accessed_at: '2026-10-28T09:27:38.558556Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 9e7a3b9f5477b7c6acdf80e121cfb7b772a3d5c19e7b2c312ca841b19e1c3cb4
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record03/validate-strict.json
  accessed_at: '2026-10-28T09:27:39.526956Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch062/record03/strict.tsv\n"
  snapshot_sha256: 8df327616afc73b4b09736d2770b34828e6e8be27ba092b154d066b6b5a94c87
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record03/validate-terms.json
  accessed_at: '2026-10-28T09:27:40.601349Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 9514adb15a1ccf3671f25b9df6e3adce7ce44f60c28c7c5a9a36b96a8b9e6ca2
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch062/record03/validate-references.json
  accessed_at: '2026-10-28T09:27:41.302508Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 731e3ebd3237c173a509336d543bd9178ce09bfa01ba9e7ee4d81ae5df7ec27f
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and maintained owner
  outcome: supported
  summary: DSM1395 identity, selected stable ID and sole maintained contributor agree.
    This review concerns the existing solid-agar variant; the source also allows a
    liquid variant.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - identity-search
  - dsm1395
  - api1395
- assessment_id: a2
  area: consistency
  topic: Complex solid variant
  outcome: supported
  summary: Peptone and yeast extract support COMPLEX/UNDEFINED. Conditional agar is
    expressly represented and SOLID_AGAR is supported; no forced liquid classification
    or strain-level growth inference follows.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - dsm1395
  - api1395
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "NaCl", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    41,\n                        \"unit\": \"g\",\n                        \"g_l\":
    41,\n                        \"mmol_l\": 701.574,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "NaCl", "compound_id": 43, "amount": 41, "unit": "g", "g_l": 41, "mmol_l": 701.574,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " NaCl                                                        41.000        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "41",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "41",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  Its existing exact
    attached JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q2", "topic": "MgCl2 x 6 H2O", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    7,\n                        \"unit\": \"g\",\n                        \"g_l\":
    7,\n                        \"mmol_l\": 34.4314,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "MgCl2 x 6 H2O", "compound_id": 79, "amount": 7, "unit": "g", "g_l": 7, "mmol_l":
    34.4314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " MgCl2 x 6 H2O                                                7.000        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "7", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API
    explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "7", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly
    supplies this main-recipe g_l value. Retain the amount; the primary mass table
    and water input alone would not prove final volume.  Its existing exact attached
    JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q3", "topic": "MgSO4 x 7 H2O", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    9.6,\n                        \"unit\": \"g\",\n                        \"g_l\":
    9.6,\n                        \"mmol_l\": 38.949,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 9.6, "unit": "g", "g_l": 9.6, "mmol_l":
    38.949, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " MgSO x 7 H2O                                                 9.600        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "9.6",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "9.6",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  Its existing exact
    attached JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q4", "topic": "CaCl2 x 2 H2O", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.36,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.36,\n                        \"mmol_l\": 2.44873,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.36, "unit": "g", "g_l": 0.36, "mmol_l":
    2.44873, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " CaCl2 x 2 H2O                                                0.360        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.36",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.36",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  Its existing exact
    attached JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q5", "topic": "KCl", "source": [{"evidence_id": "api1395", "reference":
    "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2,\n                        \"mmol_l\": 26.8276,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "KCl", "compound_id": 61, "amount": 2, "unit": "g", "g_l": 2, "mmol_l": 26.8276,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " KCl                                                          2.000        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API
    explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "2", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly
    supplies this main-recipe g_l value. Retain the amount; the primary mass table
    and water input alone would not prove final volume.  Its existing exact attached
    JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q6", "topic": "NaHCO3", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    0.06,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.06,\n                        \"mmol_l\": 0.714226,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "NaHCO3", "compound_id": 55, "amount": 0.06, "unit": "g", "g_l": 0.06, "mmol_l":
    0.714226, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " NaHCO3                                                       0.060        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.06",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.06",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  Its existing exact
    attached JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q7", "topic": "NaBr", "source": [{"evidence_id": "api1395", "reference":
    "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\":
    0.026,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.026,\n                        \"mmol_l\": 0.252697,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "NaBr", "compound_id": 353, "amount": 0.026, "unit": "g", "g_l": 0.026, "mmol_l":
    0.252697, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " NaBr                                                         0.026        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.026",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.026",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  Its existing exact
    attached JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q8", "topic": "Peptone", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Peptone", "compound_id": 1, "amount": 5, "unit":
    "g", "g_l": 5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " Peptone                                                      5.000        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API
    explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly
    supplies this main-recipe g_l value. Retain the amount; the primary mass table
    and water input alone would not prove final volume.  Its existing exact attached
    JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q9", "topic": "Yeast extract", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    10,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 9, "compound": "Yeast extract", "compound_id": 16, "amount":
    10, "unit": "g", "g_l": 10, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 12; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " Yeast Extract                                               10.000        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  Its existing exact
    attached JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q10", "topic": "Glucose", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Glucose", "compound_id": 5, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 5.55062,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm1395",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 13; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " Glucose                                                      1.000        g"}],
    "decision": "mixed", "rationale": "The current official API explicitly supplies
    this main-recipe g_l value. Retain the amount; the primary mass table and water
    input alone would not prove final volume. ", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official API
    explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume.  The generated
    ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "The current official API explicitly
    supplies this main-recipe g_l value. Retain the amount; the primary mass table
    and water input alone would not prove final volume.  Its existing exact attached
    JSON quotation and cited raw digest independently match the fresh capture."}]},
    {"quantity_id": "q11", "topic": "Agar", "source": [{"evidence_id": "api1395",
    "reference": "https://mediadive.dsmz.de/rest/medium/1395", "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin",
    "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\":
    \"for solid medium\",\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    59.4654,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 12, "compound": "Agar", "compound_id": 3, "condition": "for solid
    medium", "amount": 20, "unit": "g", "g_l": 20, "mmol_l": 59.4654, "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 19; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": "20.0 g/l agar."}], "decision": "mixed", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume. Agar is explicitly
    conditional on the solid variant, matching local SOLID_AGAR and the retained note.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume. Agar is explicitly
    conditional on the solid variant, matching local SOLID_AGAR and the retained note.
    The generated ingredient has no claim evidence."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The current official
    API explicitly supplies this main-recipe g_l value. Retain the amount; the primary
    mass table and water input alone would not prove final volume. Agar is explicitly
    conditional on the solid variant, matching local SOLID_AGAR and the retained note.
    Its existing exact attached JSON quotation and cited raw digest independently
    match the fresh capture."}]}, {"quantity_id": "q12", "topic": "Primary water input",
    "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "PDF extracted line 14; visually checked page", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": " Distilled Water                                           1000.000       ml"}],
    "decision": "add", "rationale": "The water input is absent from the local formulation/preparation;
    adding it must preserve its source batch basis.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "preparation_steps",
    "stored_value": [{"step_number": 1, "action": "MIX", "description": "Adjust to
    pH 7.0 and sterilize by autoclaving. The medium may be solidified by adding 20.0
    g/l agar."}], "decision": "add", "rationale": "Retain existing instruction and
    append a scoped water-input instruction supported by the source; do not turn the
    1000 ml solvent input into a made-up final-volume assertion."}, {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "MIX", "description": "Adjust to pH 7.0 and sterilize by autoclaving. The medium
    may be solidified by adding 20.0 g/l agar."}], "decision": "add", "rationale":
    "Retain existing instruction and append a scoped water-input instruction supported
    by the source; do not turn the 1000 ml solvent input into a made-up final-volume
    assertion."}]}, {"quantity_id": "q13", "topic": "pH and autoclaving; conditional
    solidification", "source": [{"evidence_id": "api1395", "reference": "https://mediadive.dsmz.de/rest/medium/1395",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api1395.bin", "raw_sha256": "a1aca3c91d45650c16b147581a1d501f86b3c96b5d2a139cc6764b8fcb3f893c",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:44.129613Z",
    "quote": "{\n                        \"step\": \"Adjust to pH 7.0 and sterilize
    by autoclaving. The medium may be solidified by adding 20.0 g/l agar.\"\n                    }",
    "exact_decoded_object": {"step": "Adjust to pH 7.0 and sterilize by autoclaving.
    The medium may be solidified by adding 20.0 g/l agar."}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "dsm1395", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1395.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm1395.bin", "raw_sha256": "98501e484e9698374b1a4328698d5e8182bcc390e22078c04254d1b5a09a51ca",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:44.371166Z",
    "quote": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may be solidified
    by adding\n20.0 g/l agar."}], "decision": "evidence_only", "rationale": "Retain
    pH7.0, autoclaving and conditional20g/L agar. No autoclave temperature, duration,
    strain or growth temperature is supplied or inferred.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "ph_value",
    "stored_value": 7.0, "decision": "evidence_only", "rationale": "The existing pH
    and complete instruction are supported; attach claim-scoped source evidence at
    the root evidence slot without fabricating nested preparation evidence."}, {"path":
    "data/merge_yaml/merged/CHROMOHALOBACTER_MEDIUM.yaml", "field_path": "preparation_steps[0].description",
    "stored_value": "Adjust to pH 7.0 and sterilize by autoclaving. The medium may
    be solidified by adding 20.0 g/l agar.", "decision": "evidence_only", "rationale":
    "The existing pH and complete instruction are supported; attach claim-scoped source
    evidence at the root evidence slot without fabricating nested preparation evidence."},
    {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path":
    "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "The
    existing pH and complete instruction are supported; attach claim-scoped source
    evidence at the root evidence slot without fabricating nested preparation evidence."},
    {"path": "data/normalized_yaml/bacterial/chromohalobacter_medium.yaml", "field_path":
    "preparation_steps[0].description", "stored_value": "Adjust to pH 7.0 and sterilize
    by autoclaving. The medium may be solidified by adding 20.0 g/l agar.", "decision":
    "evidence_only", "rationale": "The existing pH and complete instruction are supported;
    attach claim-scoped source evidence at the root evidence slot without fabricating
    nested preparation evidence."}]}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All nine existing CHEBI identities and both repeated primary/secondary
    slots resolve with current canonical labels. Peptone and yeast extract remain
    unmapped mixtures. The PDF’s MgSO wording is retained literally; API MgSO4 and
    current CHEBI31795 support the stored heptahydrate, without rewriting the primary
    quotation.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: All three exact historical reports were read; the thirteen October source
    objects and the complete cited raw digest match the fresh API response. All eleven
    attached owner quotations are authenticated as response content. Historical access
    events are not rerun. The selected merge predates and loses the owner repair,
    which must be retained.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - history
  - scalars
- assessment_id: a6
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:000856
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000856-regenerate-authenticated-owner-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Regenerate authenticated owner evidence
  description: The maintained contributor already carries eleven source-specific ingredient
    quotations and an October reference/curation event. Each literal quotation and
    the cited API raw digest match the independent current response. The selected
    August merge lacks these evidence lists, reference and later event despite retaining
    all amounts. Credit the existing repair and regenerate the sole contributor with
    the current evidence-preserving merge; do not repeat the quantity edits.
  target_ids:
  - CultureMech:000856
  field_paths:
  - ingredients[0].evidence
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - ingredients[5].evidence
  - ingredients[6].evidence
  - ingredients[7].evidence
  - ingredients[8].evidence
  - ingredients[9].evidence
  - ingredients[10].evidence
  - references
  - curation_history
  evidence_ids:
  - owner-1
  - local-target
  - attached-evidence-joins
  - historical-reader
  - writer-merge
  - api1395
  rule_id: generated-evidence-staleness
  native_severity: P2
  normalization_reason: 'Major evidence-loss extension of native provenance review:
    eleven already-authenticated claims disappear from the published generated layer;
    no source amount is wrong.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-000856-link-water-and-preparation-at-supported-scope
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Link water and preparation at supported scope
  description: The source specifies a 1000 ml distilled-water input, pH7.0 and autoclaving.
    The local preparation retains pH/autoclaving/conditional agar but lacks the water
    input and root claim evidence. Add the water input as a batch quantity and root
    evidence that identifies the exact preparation fields; do not invent a final volume
    or absent sterilization settings.
  target_ids:
  - CultureMech:000856
  field_paths:
  - preparation_steps
  - ph_value
  - evidence
  evidence_ids:
  - dsm1395
  - api1395
  - quantities
  rule_id: P4.3
  native_severity: P4
  normalization_reason: Minor rather than optional because a required solvent input
    and claim-level preparation traceability are absent; supported pH/agar values
    remain unchanged.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-000856-resolve-the-two-complex-ingredient-links
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the two complex-ingredient links
  description: Peptone and yeast extract have supported amounts and mixture identities
    but no primary or secondary ontology linkage. Current catalog candidates are lookup
    leads only; do not substitute a chemically defined compound or infer composition.
    Existing nine CHEBI identifiers and canonical labels resolve in current OLS.
  target_ids:
  - CultureMech:000856
  field_paths:
  - ingredients[7].term
  - ingredients[7].mediaingredientmech_chebi_term
  - ingredients[8].term
  - ingredients[8].mediaingredientmech_chebi_term
  evidence_ids:
  - grounding
  - dsm1395
  - api1395
  rule_id: P3.2
  native_severity: P3
  normalization_reason: 'Native missing-ingredient-linkage rule, minor: the source
    supports complex ingredient names and amounts; no incorrect chemical identifier
    is alleged.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Preserve all eleven already-supported owner quantities and evidence;
    regenerate the target so exact ingredient evidence, reference and appended curation
    survive. Confirm current merge output retains the solid-medium condition.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000856
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Append the exact water-input context and scoped root evidence for the
    retained preparation. Keep the existing pH and agar condition; make no final-volume,
    time or temperature claim not supplied by the source.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000856
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Verify an appropriate current mixture identifier for each unmapped
    ingredient and record its exact canonical label and mapping provenance; preserve
    the supported amounts and mixture status.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000856
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromohalobacter_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The primary PDF prints MgSO x7 H2O without the sulfate subscript4. The API explicitly
  supplies MgSO4 x7 H2O; this source difference is disclosed rather than silently
  rewriting the quotation.
- Provider g_l fields support nominal main-recipe rates;1000 ml water is not an independently
  measured final volume. No stock-dilution or experimental-performance claim is inferred.
- Peptone and yeast-extract linkage remains unresolved here; no unverified candidate
  identifier is endorsed.
- The source has no strain-level growth demonstration or sterilization duration/temperature.
  Current term and reference diagnostics do not provide such evidence.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
