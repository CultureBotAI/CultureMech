# COLBY AND ZATHMAN MEDIUM: separate trace stock and preserve preparation variants

- Review: 20261028T115218Z-batch065-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T11:30:17.604624Z
- Finished UTC: 2026-10-28T11:52:18.364725Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Current DSM606 and its API distinguish eight main ingredients from a seven-compound trace stock added separately. All three local layers flatten the stock rates into direct ingredients and omit its receiving dose. The DSM owner retains the main preparation text, while the generated target and KOMODO contributor lose it. Hydrates and main provider rates are supported; the exact KOMODO access branch remains unavailable and historical events remain append-only.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch065 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006095 | data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml | generated | colby_and_zathman_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006095 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:006095 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:006095 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:006095 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### DSM606, KOMODO606 and source variants

identity: concern. Targets: CultureMech:006095.

The selected target resolves to the exact two maintained contributors. Current DSM606 and API identity agree; historical KOMODO mapping names the same source, but both exact live KOMODO routes return403. Matching ingredient signatures do not establish full preparation compatibility: the DSM owner retains a main preparation paragraph absent from the KOMODO owner and target. The DSM15625 alternative remains separate.

### Source topology and retained source context

completeness: concern. Targets: CultureMech:006095.

Main provider rates and all fifteen chemical forms are assessed separately from stock topology. The seven trace constituents belong to a named stock with its own water input and receiving dose. Existing pH is correct; the DSM owner already preserves the main preparation. Purified agar and the separately scoped source alternative need explicit retention.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:006095.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "K2HPO4 main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.2,\n                        \"mmol_l\": 6.88958,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "K2HPO4", "compound_id": 10, "amount": 1.2, "unit": "g", "g_l": 1.2, "mmol_l": 6.88958, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " K2HPO4                                                           1.20        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}]}, {"quantity_id": "q2", "topic": "KH2PO4 main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.62,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.62,\n                        \"mmol_l\": 4.55598,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "KH2PO4", "compound_id": 11, "amount": 0.62, "unit": "g", "g_l": 0.62, "mmol_l": 4.55598, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " KH2PO4                                                           0.62        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.62", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.62", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.62", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}]}, {"quantity_id": "q3", "topic": "CaCl2 x 6 H2O main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 6 H2O\",\n                        \"compound_id\": 173,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.228231,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "CaCl2 x 6 H2O", "compound_id": 173, "amount": 0.05, "unit": "g", "g_l": 0.05, "mmol_l": 0.228231, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " CaCl2 x 6 H2O                                                    0.05        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}]}, {"quantity_id": "q4", "topic": "MgSO4 x 7 H2O main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.2, "unit": "g", "g_l": 0.2, "mmol_l": 0.811438, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " MgSO4 x 7 H2O                                                    0.20        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}]}, {"quantity_id": "q5", "topic": "NaCl main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.71116,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "NaCl", "compound_id": 43, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 1.71116, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " NaCl                                                             0.10        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}]}, {"quantity_id": "q6", "topic": "(NH4)2SO4 main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.78387,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "(NH4)2SO4", "compound_id": 27, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 3.78387, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "(NH4)2SO4                                                         0.50        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount."}]}, {"quantity_id": "q7", "topic": "Agar main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"attribute\": \"purified \",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "attribute": "purified ", "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " Purified agar                                                   15.00        g"}], "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount. The primary requires purified agar; the local generic agar label does not preserve that supplied grade.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount. The primary requires purified agar; the local generic agar label does not preserve that supplied grade."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount. The primary requires purified agar; the local generic agar label does not preserve that supplied grade."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l supports the unchanged local rate. The primary batch mass and water input do not independently establish a measured final volume. Add scoped evidence without changing the supported amount. The primary requires purified agar; the local generic agar label does not preserve that supplied grade."}]}, {"quantity_id": "q8", "topic": "Methanol main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Methanol\",\n                        \"compound_id\": 226,\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"g_l\": 1.584,\n                        \"mmol_l\": 49.4351,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Methanol", "compound_id": 226, "amount": 2, "unit": "ml", "g_l": 1.584, "mmol_l": 49.4351, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 12; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " Methanol                                                         2.00       ml"}], "decision": "evidence_only", "rationale": "The provider explicitly reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared rate, not an independently verified density conversion. Primary preparation also says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace the primary volume with an assumed mass.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.584", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared rate, not an independently verified density conversion. Primary preparation also says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace the primary volume with an assumed mass."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.584", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared rate, not an independently verified density conversion. Primary preparation also says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace the primary volume with an assumed mass."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.584", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared rate, not an independently verified density conversion. Primary preparation also says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace the primary volume with an assumed mass."}]}, {"quantity_id": "q9", "topic": "CuSO4 x 5 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0200252,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0200252, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 24; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "CuSO4 x 5 H2O                                                      5.0      mg"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q10", "topic": "MnSO4 x 5 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnSO4 x 5 H2O\",\n                        \"compound_id\": 234,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0414804,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "MnSO4 x 5 H2O", "compound_id": 234, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l": 0.0414804, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 25; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "MnSO4 x 5 H2O                                                     10.0      mg"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q11", "topic": "Na2MoO4 x 2 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l": 0.0413309, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 26; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Na2MoO4 x 2 H2O                                                   10.0      mg"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q12", "topic": "H3BO3 trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "H3BO3", "compound_id": 37, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l": 0.161708, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 27; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "H3BO3                                                             10.0      mg"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q13", "topic": "ZnSO4 x 7 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.243427,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l": 0.243427, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 28; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "ZnSO4 x 7 H2O                                                     70.0      mg"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q14", "topic": "CoCl2 x 6 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0385092,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0385092, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 29; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "CoCl2 x 6 H2O                                                      5.0      mg"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q15", "topic": "FeCl3 x 6 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 3.69965,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "FeCl3 x 6 H2O", "compound_id": 82, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 3.69965, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 30; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "FeCl3 x 6 H2O                                                      1.0       g"}], "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the provider-declared concentration of the separate trace stock, not a direct final-medium ingredient rate. Preserve its supported supplied form and stock amount, restore the separate stock and receiving dose, and do not silently divide by 1000 or infer final volume."}]}, {"quantity_id": "q16", "topic": "Trace-stock receiving dose", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace elements solution\",\n                        \"solution_id\": 1303,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "solution": "Trace elements solution", "solution_id": 1303, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " Trace element solution (see below)                               1.00       ml"}], "decision": "add", "rationale": "The source supplies one explicit stock addition, separate from its composition. No final-medium concentration is calculated without final-volume support.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent the separately named stock and the explicit 1 ml receiving dose; no stock identity may be substituted merely because it contains similar elements.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent the separately named stock and the explicit 1 ml receiving dose; no stock identity may be substituted merely because it contains similar elements.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent the separately named stock and the explicit 1 ml receiving dose; no stock identity may be substituted merely because it contains similar elements.", "missing": true}]}, {"quantity_id": "q17", "topic": "Main water input", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 13; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " Distilled water                                               1000.00       ml"}], "decision": "add", "rationale": "Preserve the exact source 1000 ml distilled-water input at this stage. It is not a water mass rate or an instruction to make up a measured final volume.", "layer_assessments": []}, {"quantity_id": "q18", "topic": "Trace-stock water input", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 31; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Distilled water                                                 1000.0      ml"}], "decision": "add", "rationale": "Preserve the exact source 1000 ml distilled-water input at this stage. It is not a water mass rate or an instruction to make up a measured final volume.", "layer_assessments": []}, {"quantity_id": "q19", "topic": "Existing pH 7.0", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at 121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}], "decision": "evidence_only", "rationale": "The pH value is retained in all layers; the missing preparation sequence is assessed separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing pH 7.0 agrees with the primary and provider; link the exact preparation claim without changing the value."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing pH 7.0 agrees with the primary and provider; link the exact preparation claim without changing the value."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing pH 7.0 agrees with the primary and provider; link the exact preparation claim without changing the value."}]}, {"quantity_id": "q20", "topic": "Autoclave temperature", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at 121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}], "decision": "mixed", "rationale": "The source explicitly supplies this part of the staged preparation. The source 0.2% basis is not stated; keep that limitation and do not manufacture a stock strength or dilution calculation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.", "decision": "evidence_only", "rationale": "The maintained DSM owner already contains this exact main preparation statement; preserve it and attach root evidence, without reapplying it as a missing field."}]}, {"quantity_id": "q21", "topic": "Autoclave duration", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at 121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}], "decision": "mixed", "rationale": "The source explicitly supplies this part of the staged preparation. The source 0.2% basis is not stated; keep that limitation and do not manufacture a stock strength or dilution calculation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.", "decision": "evidence_only", "rationale": "The maintained DSM owner already contains this exact main preparation statement; preserve it and attach root evidence, without reapplying it as a missing field."}]}, {"quantity_id": "q22", "topic": "Cooling temperature", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at 121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}], "decision": "mixed", "rationale": "The source explicitly supplies this part of the staged preparation. The source 0.2% basis is not stated; keep that limitation and do not manufacture a stock strength or dilution calculation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.", "decision": "evidence_only", "rationale": "The maintained DSM owner already contains this exact main preparation statement; preserve it and attach root evidence, without reapplying it as a missing field."}]}, {"quantity_id": "q23", "topic": "Filtered methanol addition and final percentage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at 121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}], "decision": "mixed", "rationale": "The source explicitly supplies this part of the staged preparation. The source 0.2% basis is not stated; keep that limitation and do not manufacture a stock strength or dilution calculation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore the exact source preparation context in this layer; all quantities and percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.", "decision": "evidence_only", "rationale": "The maintained DSM owner already contains this exact main preparation statement; preserve it and attach root evidence, without reapplying it as a missing field."}]}, {"quantity_id": "q24", "topic": "Existing DSM preparation action and order", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at 121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution of methanol to give a final concentration of 0.2%."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}], "decision": "evidence_only", "rationale": "The single composite DSM step already preserves the main instructions. Structured splitting may improve representation but must not lose any existing description.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "preparation_steps[0].action", "stored_value": "AUTOCLAVE", "decision": "evidence_only", "rationale": "AUTOCLAVE is a coarse existing action for the composite source paragraph; its complete description preserves the actual operations."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "preparation_steps[0].step_number", "stored_value": 1, "decision": "evidence_only", "rationale": "Local ordering index does not supply an experimental amount."}]}, {"quantity_id": "q25", "topic": "Purified agar supplied grade", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T11:30:48.316298Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"attribute\": \"purified \",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "attribute": "purified ", "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": " Purified agar                                                   15.00        g"}], "decision": "correct", "rationale": "The API attribute and primary both specify purified agar. Generic CHEBI agar remains chemically appropriate, while supplied-grade specificity needs retention.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[6].preferred_term", "stored_value": "Agar", "decision": "correct", "rationale": "Retain the source purified-grade qualifier with the existing generic agar ontology; no new chemical identity or amount is implied."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[6].preferred_term", "stored_value": "Agar", "decision": "correct", "rationale": "Retain the source purified-grade qualifier with the existing generic agar ontology; no new chemical identity or amount is implied."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path": "ingredients[6].preferred_term", "stored_value": "Agar", "decision": "correct", "rationale": "Retain the source purified-grade qualifier with the existing generic agar ontology; no new chemical identity or amount is implied."}]}, {"quantity_id": "q26", "topic": "DSM15625 source alternative only", "source": [{"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z", "quote": "For DSM 15625 replace the methanol with a filter-sterilized solution of\ntrimethylammonium chloride to give a final concentration of 0.1%."}], "decision": "add", "rationale": "This strain-specific alternative replaces methanol with filter-sterilized trimethylammonium chloride at source-stated final 0.1%, whose percent basis is unspecified. Preserve it as an explicitly separate source variant, not as another generic ingredient or a change to the selected methanol formulation. No strain-growth assertion is inferred.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:006095.

All fifteen distinct primary chemical IDs and their secondary slots resolve to current OLS canonical labels with source-consistent supplied forms, including calcium hexahydrate, manganese pentahydrate, molybdate dihydrate, cobalt hexahydrate and ferric chloride hexahydrate. MIM identifier/ontology row unions preserve exact statuses: CoCl2 x 6 H2O has a REJECTED preferred-name row while Cobalt chloride hexahydrate is MAPPED to the same53503 identity; neither status invalidates the independently verified chemical form. Generic agar does not by itself carry the purified-grade requirement.

### History and evidence scope

provenance: concern. Targets: CultureMech:006095.

Current source bytes, complete histories and scoped historical reports were read. Missing claim-level linkage and any malformed historical metadata are distinguished from authenticated source bytes; originals remain append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:006095.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:006095.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Restore separate trace-stock topology

major / open / confirmed; issue key: culturemech-006095-restore-separate-trace-stock-topology.

Seven direct ingredient rates in every layer are exactly the provider concentrations of trace solution1303. They are incorrectly presented alongside main-recipe rates, while the named stock and its 1 ml receiving dose are absent. Preserve all seven source masses/forms at stock stage and restore the separate addition. Do not turn them into guessed final-medium rates.

### f2: Preserve source preparation and supplied-form distinctions

major / open / confirmed; issue key: culturemech-006095-preserve-source-preparation-and-supplied-form-distinctions.

The DSM owner already retains the pH/autoclave/cooling/filtered-methanol paragraph. The KOMODO owner and generated target omit it, consistent with a current resolver that does not copy preparation_steps. All layers also lose the purified-agar qualifier and omit the separately identified DSM15625 source alternative. The API methanol g_l is credited as provider data while primary 2 ml and unspecified-basis 0.2% remain separate claims.

### f3: Qualify the unverified imported atmosphere flag

minor / open / confirmed; issue key: culturemech-006095-qualify-the-unverified-imported-atmosphere-flag.

The target and KOMODO owner say Aerobic: No. The historical catalogue excerpt contains a false flag, but the live catalogue is unavailable and the primary PDF/API provide no directly scoped atmosphere statement. This imported metadata is not proof of anaerobic growth, and absence of such a statement does not justify flipping it to aerobic.

### f4: Preserve and qualify historical event metadata

minor / open / confirmed; issue key: culturemech-006095-preserve-and-qualify-historical-event-metadata.

KOMODO import events contain a literal .fZ timestamp and resolver events omit a UTC offset. Historical concentration reports preserve unresolved claims and exact source mappings, but are not independent proof of those historical retrieval events. All current concentration claims also lack attached evidence. Fresh API bytes match both October606 report source digests and their exact objects, but this does not authenticate historical access events or the unavailable entire KOMODO catalogue.

## Recommended Actions And Acceptance Checks

### action1

Curate the two maintained contributors to represent source trace solution1303 separately, with exact stock components, solvent input and explicit receiving dose. Preserve supported main rates. Regenerate only after formulation compatibility is reconciled; do not infer final volume or compute ungrounded stock dilutions.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Retain the existing DSM main preparation and repair the missing KOMODO/target context using exact source claims. Preserve purified agar. Keep the DSM15625 alternative separate from the generic methanol formulation and leave bare-percent bases unresolved. Use schema-supported root evidence for source stages; do not overwrite the already-correct owner paragraph or force incompatible owners into a merge.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Retain original provenance and qualify the imported atmosphere flag as unverified until an exact source field and its semantics are authenticated. Do not infer growth or replace it with an opposite atmosphere claim.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Retain every original event byte-for-byte. If authoritative provenance is recovered, append a verified correction or context event; never invent or overwrite its timestamp. Link fresh source evidence separately and preserve unresolved accession limitations.

- Original malformed and timezone-unspecified events remain byte-preserved; any recovered correction is appended with verified provenance.
- All new amount, stage and preparation claims carry exact current source locators; old unsupported decisions remain historical observations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| dsm606 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf; Exact source identity and scoped formulation/preparation | supports | Complete one-page primary PDF visually read, including main recipe, separate trace stock, staged preparation and explicitly scoped DSM15625 alternative. Water inputs do not establish final volumes. |
| api606 | https://mediadive.dsmz.de/rest/medium/606; Exact source identity and scoped formulation/preparation | supports | Complete current response: two source solutions, all eighteen recipe rows and the main preparation object. Explicit g_l remains scoped to the named solution and is not a receiving-medium concentration for stock compounds. |
| komodo606 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=606; Exact source identity and scoped formulation/preparation | context_only | Exact historical /komodo/servlet MediaInfo=606 link returned403. Challenge bytes supply no current recipe or atmosphere evidence. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact source identity and scoped formulation/preparation | context_only | Exact historical MediaList route returned403. Historical mapping row remains derivative evidence; the original entire catalogue was not independently recovered. |
| dsm15625 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-15625; Exact source identity and scoped formulation/preparation | context_only | Current DSM15625 catalogue metadata identifies Methylobacillus sp. strain C2A1 and the medium606 link. Used only to identify the source-specific alternative; no cultivation conditions or organism assertions are transferred to the generic recipe. |
| identity-search | REVIEW_WORK/batch065/record03/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition | context_only | Current merge_composition copies nonplaceholder ingredients and available solutions, ph_value when absent, physical_state and medium_type. It does not copy preparation_steps or ph_range; present behavior is not proof of historical execution. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech builds KOMODO identity, source mapping and aerobic notes from table flags and emits placeholder ingredients. It uses time.strftime with %f, which does not itself establish a valid fractional timestamp. Existing malformed events remain original evidence, not a license to rewrite history. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Exact selected-owner matching rows, if present, plus report purpose/method and validation claims only; all other pair-specific conclusions outside scope. | context_only | Historical source-duplicate report: only exact selected-owner rows, where present, and its stated signature method are in scope. Similarity does not prove complete preparation identity; no assertion about absent exact pairs is inferred. |
| historical-2 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 19 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-3 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/colby_and_zathman_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 19 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/colby_and_zathman_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-reader | REVIEW_WORK/batch065/record03/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| historical-plan-1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json; $.records[182] | context_only | Exact selected contributor plan row only, including unchanged decisions and original source provenance. Current source comparisons never reauthenticate the historical access event. |
| historical-plan-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; $.records[146] | context_only | Exact selected contributor plan row only, including unchanged decisions and original source provenance. Current source comparisons never reauthenticate the historical access event. |
| historical-plan-rows | REVIEW_WORK/batch065/record03/historical-plan-rows.json | context_only | Exact scoped plan-row membership; full parent payload retained as an inspected pin without transferring neighboring records. |
| attached-evidence-joins | REVIEW_WORK/batch065/record03/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| complete-source-rows | REVIEW_WORK/batch065/record03/complete-source-rows.json | context_only | Every source recipe row and preparation object, with exact raw substring and decoded JSON locator, kept in its own solution stage. No biological recommendation follows from provider equipment metadata. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91243 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91243; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62946; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17790 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17790; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131524 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131524; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86254; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch065/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch065/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch065/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch065/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch065/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch065/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch065/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch065/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch065/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Exact historical KOMODO MediaInfo606 and MediaList routes both returned403; source identity on that branch remains partial. Fresh DSM/API support does not restore the original whole catalogue or reauthenticate past retrieval events.
- The primary gives water inputs rather than explicit final makeup for main and stock stages. Provider g_l values are credited at their named source stages only; no downstream stock rates are calculated.
- Methanol1.584 g/l is a provider declaration; no independent density conversion is established. The primary final0.2% and strain-specific final0.1% do not state percent basis, so no w/v or v/v assumption is made.
- DSM15625 is only the label of the primary source alternative; its catalogue conditions, generic applications and bacterial filing are not transferred as new growth assertions. The target remains the generic methanol formulation.
- Current writer behavior does not prove historical causality. Existing history is append-only; native reference validation performed zero checks.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T115218Z-batch065-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'COLBY AND ZATHMAN MEDIUM: separate trace stock and preserve preparation variants'
started_at: '2026-10-28T11:30:17.604624Z'
finished_at: '2026-10-28T11:52:18.364725Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Current DSM606 and its API distinguish eight main ingredients from a seven-compound
  trace stock added separately. All three local layers flatten the stock rates into
  direct ingredients and omit its receiving dose. The DSM owner retains the main preparation
  text, while the generated target and KOMODO contributor lose it. Hydrates and main
  provider rates are supported; the exact KOMODO access branch remains unavailable
  and historical events remain append-only.
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
  - path: data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
    sha256: 5c1cc625c9fb5a7fd4f2e133dd1000842f079722883a8aa99bffac027a1ee8fc
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    sha256: 3e508dcd1b296981eaf24032084b839d86e176d1a8381ab262890b7661a9531c
    role: context
  - path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    sha256: 0e2dbf9822b69b24eeb51f7114887454274e2111b50467a0714152c126578c5a
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml.md
    sha256: 98151799c1034b1c455bba782a1218b1afc8d23d30dccaf2838fe4bf30c97d3b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/colby_and_zathman_medium.yaml.md
    sha256: 7ab8b9c87006cd1bfc4c3e089d4d7b1793c353cdbf03421a2cadb8c623652377
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.md
    sha256: f9bba1ea32b1dd9153173181f1b3f0674a92fe9fffc455a37da80286a9c8f161
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.md
    sha256: 830930e9cc3c90f8913a27c2e4cb6af0d4849a8eb79611a142a56af8c3cf6d7d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/colby_and_zathman_medium.md
    sha256: 78602de80ac91317b23497f2852914838cff977c475844f944dd45b07c7ece9e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch065 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006095
targets:
- target_id: CultureMech:006095
  path: data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
  label: colby_and_zathman_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006095
  command: just validate-schema data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
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
  - CultureMech:006095
  command: just validate-strict data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
    --out REVIEW_WORK/batch065/record03/strict.tsv --workers 1 --quiet
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
  - CultureMech:006095
  command: just validate-terms data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
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
  - CultureMech:006095
  command: just validate-references data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 5c1cc625c9fb5a7fd4f2e133dd1000842f079722883a8aa99bffac027a1ee8fc
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 3e508dcd1b296981eaf24032084b839d86e176d1a8381ab262890b7661a9531c
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 0e2dbf9822b69b24eeb51f7114887454274e2111b50467a0714152c126578c5a
- evidence_id: dsm606
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T11:30:48.673162Z'
  support: supports
  summary: Complete one-page primary PDF visually read, including main recipe, separate
    trace stock, staged preparation and explicitly scoped DSM15625 alternative. Water
    inputs do not establish final volumes.
  snapshot_sha256: 5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4
- evidence_id: api606
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/606
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T11:30:48.316298Z'
  support: supports
  summary: 'Complete current response: two source solutions, all eighteen recipe rows
    and the main preparation object. Explicit g_l remains scoped to the named solution
    and is not a receiving-medium concentration for stock compounds.'
  snapshot_sha256: 739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92
- evidence_id: komodo606
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=606
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T11:30:47.690254Z'
  support: context_only
  summary: Exact historical /komodo/servlet MediaInfo=606 link returned403. Challenge
    bytes supply no current recipe or atmosphere evidence.
  snapshot_sha256: 1dd60de5d0d66a2666119c6f72734082b7a5f88cbc77ea2986cd76ea55960bef
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T11:30:47.659708Z'
  support: context_only
  summary: Exact historical MediaList route returned403. Historical mapping row remains
    derivative evidence; the original entire catalogue was not independently recovered.
  snapshot_sha256: a97f445bc54a447e18b153a0364237a84441294fe07a1f85839fb04a97a46329
- evidence_id: dsm15625
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-15625
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T11:30:50.466715Z'
  support: context_only
  summary: Current DSM15625 catalogue metadata identifies Methylobacillus sp. strain
    C2A1 and the medium606 link. Used only to identify the source-specific alternative;
    no cultivation conditions or organism assertions are transferred to the generic
    recipe.
  snapshot_sha256: faf537a49a97a86d8f411390fab869add57a1150d05c10f6fd664a83de0144f1
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch065/record03/identity-search.json
  accessed_at: '2026-10-28T11:42:00.895075Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: cff90204d39dc17cdd80c30a1852289d7d8e4a80bf30d67af2cdad859aa50cf7
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T11:42:00.845560Z'
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
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T11:42:00.845560Z'
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
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Current merge_composition copies nonplaceholder ingredients and available
    solutions, ph_value when absent, physical_state and medium_type. It does not copy
    preparation_steps or ph_range; present behavior is not proof of historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, source mapping
    and aerobic notes from table flags and emits placeholder ingredients. It uses
    time.strftime with %f, which does not itself establish a valid fractional timestamp.
    Existing malformed events remain original evidence, not a license to rewrite history.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Exact selected-owner matching rows, if present, plus report purpose/method
    and validation claims only; all other pair-specific conclusions outside scope.
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: 'Historical source-duplicate report: only exact selected-owner rows, where
    present, and its stated signature method are in scope. Similarity does not prove
    complete preparation identity; no assertion about absent exact pairs is inferred.'
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    19 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 98151799c1034b1c455bba782a1218b1afc8d23d30dccaf2838fe4bf30c97d3b
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/colby_and_zathman_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    19 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 7ab8b9c87006cd1bfc4c3e089d4d7b1793c353cdbf03421a2cadb8c623652377
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: f9bba1ea32b1dd9153173181f1b3f0674a92fe9fffc455a37da80286a9c8f161
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 830930e9cc3c90f8913a27c2e4cb6af0d4849a8eb79611a142a56af8c3cf6d7d
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/colby_and_zathman_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 78602de80ac91317b23497f2852914838cff977c475844f944dd45b07c7ece9e
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/historical-reader.json
  accessed_at: '2026-10-28T11:42:00.900647Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: 1501370586cd952b264f0b23b0b5090842db91a3ccd2fccfd8a7173f084b0ae6
- evidence_id: historical-plan-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
  locator: $.records[182]
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Exact selected contributor plan row only, including unchanged decisions
    and original source provenance. Current source comparisons never reauthenticate
    the historical access event.
  snapshot_sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
- evidence_id: historical-plan-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: $.records[146]
  accessed_at: '2026-10-28T11:42:00.845560Z'
  support: context_only
  summary: Exact selected contributor plan row only, including unchanged decisions
    and original source provenance. Current source comparisons never reauthenticate
    the historical access event.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: historical-plan-rows
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/historical-plan-rows.json
  accessed_at: '2026-10-28T11:42:00.966997Z'
  support: context_only
  summary: Exact scoped plan-row membership; full parent payload retained as an inspected
    pin without transferring neighboring records.
  snapshot_sha256: 7bfd03b083a5b022e4963ec4b5afb738e124869992074a4d49064031ac900145
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/attached-evidence-joins.json
  accessed_at: '2026-10-28T11:42:00.970658Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-source-rows
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/complete-source-rows.json
  accessed_at: '2026-10-28T11:42:00.972805Z'
  support: context_only
  summary: Every source recipe row and preparation object, with exact raw substring
    and decoded JSON locator, kept in its own solution stage. No biological recommendation
    follows from provider equipment metadata.
  snapshot_sha256: 273d78e5d20886789405fefa8d9d59f8469622ce4a4f39b02f0b6e49ed3282da
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:49.810864Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:52.553717Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi91243
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91243
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:53.336467Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 4540209235ed1123cf00f1084c32ee3b09be3efe6b89dc26634ce6d2796bffaf
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:51.291228Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:51.133929Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62946
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:52.390609Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b52cb60c424f5c8262c2b335bf4b428324d0e53dc8b9cbfbd77494460877275d
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:51.115544Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: chebi17790
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17790
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:50.680197Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 9a22b868fd25ad35f0431df9b213fe8687bab9fc5143c8fd95f3618b4db4cd38
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:51.144054Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi131524
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131524
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:49.874646Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b2592fe97ac4144afbfa0f8c33efbecfc1ca0fa177f9ee091bfd8d503046562b
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:52.683011Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:51.787793Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:51.787715Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:52.004610Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86254
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:30:53.231577Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 9ab13b3239309508e3fdfe4eed248db3fccb868d23243c20a61cf870527b1273
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/quantity-inventory.json
  accessed_at: '2026-10-28T11:52:18.364725Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 73c2571e500fd2950e41609d51d7356d815d98eeea356febeb0cd38a94bc3f04
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/grounding-inventory.json
  accessed_at: '2026-10-28T11:42:01.002457Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: cca5e09cd26805dd9c61781c822b7078392bb79845136ca21e76119fffccbd99
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T11:42:01.002723Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 0f6fefd5d1f03eb7146cb580e651084ed29336ec5d9ab45eb69f09bf7897d46d
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch065/record03/scalar-census.json
  accessed_at: '2026-10-28T11:42:01.002749Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: b73cf54e2b273cccf711ab5a15732dbe31d6ffda00d59d132ae12f633867fe85
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch065/record03/validate-schema.json
  accessed_at: '2026-10-28T11:30:18.636876Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: e713fe6c86307d170ff027caec3f72bd3aeb6210e8e569f566e6d0f6c1b509d6
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch065/record03/validate-strict.json
  accessed_at: '2026-10-28T11:30:19.551487Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch065/record03/strict.tsv\n"
  snapshot_sha256: 600312acf7fa3b52364efac99209c977ed9f64ca3bcb657b11569d497c5c5f1a
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch065/record03/validate-terms.json
  accessed_at: '2026-10-28T11:30:20.557004Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 8e5f38701c8f3da8e742e0bd4dddcb96c6d8d70b422bc858ee860c8106509b2d
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch065/record03/validate-references.json
  accessed_at: '2026-10-28T11:30:21.235664Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 1ac9796e6a8697cb8ab465a527d8e6220e7d0212a44e86254b9efaaef155c469
assessments:
- assessment_id: a1
  area: identity
  topic: DSM606, KOMODO606 and source variants
  outcome: concern
  summary: 'The selected target resolves to the exact two maintained contributors.
    Current DSM606 and API identity agree; historical KOMODO mapping names the same
    source, but both exact live KOMODO routes return403. Matching ingredient signatures
    do not establish full preparation compatibility: the DSM owner retains a main
    preparation paragraph absent from the KOMODO owner and target. The DSM15625 alternative
    remains separate.'
  target_ids:
  - CultureMech:006095
  evidence_ids:
  - identity-search
  - dsm606
  - api606
  - komodo606
  - komodoList
  - historical-reader
  - writer-formulation
- assessment_id: a2
  area: completeness
  topic: Source topology and retained source context
  outcome: concern
  summary: Main provider rates and all fifteen chemical forms are assessed separately
    from stock topology. The seven trace constituents belong to a named stock with
    its own water input and receiving dose. Existing pH is correct; the DSM owner
    already preserves the main preparation. Purified agar and the separately scoped
    source alternative need explicit retention.
  target_ids:
  - CultureMech:006095
  evidence_ids:
  - quantities
  - dsm606
  - api606
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:006095
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "K2HPO4 main stage", "source": [{"evidence_id":
    "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path":
    "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\":
    1.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.2,\n                        \"mmol_l\": 6.88958,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "K2HPO4", "compound_id": 10, "amount": 1.2, "unit": "g", "g_l": 1.2, "mmol_l":
    6.88958, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " K2HPO4                                                           1.20        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}]}, {"quantity_id": "q2", "topic": "KH2PO4
    main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.62,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.62,\n                        \"mmol_l\": 4.55598,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "KH2PO4", "compound_id": 11, "amount": 0.62, "unit": "g", "g_l": 0.62, "mmol_l":
    4.55598, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " KH2PO4                                                           0.62        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.62",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.62",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.62",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}]}, {"quantity_id": "q3", "topic": "CaCl2
    x 6 H2O main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"CaCl2 x 6 H2O\",\n                        \"compound_id\": 173,\n                        \"amount\":
    0.05,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.228231,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "CaCl2 x 6 H2O", "compound_id": 173, "amount": 0.05, "unit": "g", "g_l": 0.05,
    "mmol_l": 0.228231, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " CaCl2 x 6 H2O                                                    0.05        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}]}, {"quantity_id": "q4", "topic": "MgSO4
    x 7 H2O main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.2, "unit": "g", "g_l": 0.2, "mmol_l":
    0.811438, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " MgSO4 x 7 H2O                                                    0.20        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}]}, {"quantity_id": "q5", "topic": "NaCl
    main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 1.71116,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "NaCl", "compound_id": 43, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 1.71116,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm606", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf", "raw_path":
    "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " NaCl                                                             0.10        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}]}, {"quantity_id": "q6", "topic": "(NH4)2SO4
    main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 3.78387,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "(NH4)2SO4", "compound_id": 27, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    3.78387, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "(NH4)2SO4                                                         0.50        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount."}]}, {"quantity_id": "q7", "topic": "Agar
    main stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Agar\",\n                        \"compound_id\": 3,\n                        \"attribute\":
    \"purified \",\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "attribute": "purified
    ", "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " Purified agar                                                   15.00        g"}],
    "decision": "evidence_only", "rationale": "The explicit provider main-stage g_l
    supports the unchanged local rate. The primary batch mass and water input do not
    independently establish a measured final volume. Add scoped evidence without changing
    the supported amount. The primary requires purified agar; the local generic agar
    label does not preserve that supplied grade.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The explicit provider main-stage g_l supports the unchanged local
    rate. The primary batch mass and water input do not independently establish a
    measured final volume. Add scoped evidence without changing the supported amount.
    The primary requires purified agar; the local generic agar label does not preserve
    that supplied grade."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount. The primary requires purified agar; the
    local generic agar label does not preserve that supplied grade."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit provider
    main-stage g_l supports the unchanged local rate. The primary batch mass and water
    input do not independently establish a measured final volume. Add scoped evidence
    without changing the supported amount. The primary requires purified agar; the
    local generic agar label does not preserve that supplied grade."}]}, {"quantity_id":
    "q8", "topic": "Methanol main stage", "source": [{"evidence_id": "api606", "reference":
    "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin",
    "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Methanol\",\n                        \"compound_id\": 226,\n                        \"amount\":
    2,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    1.584,\n                        \"mmol_l\": 49.4351,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Methanol", "compound_id": 226, "amount": 2, "unit": "ml", "g_l": 1.584, "mmol_l":
    49.4351, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 12; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " Methanol                                                         2.00       ml"}],
    "decision": "evidence_only", "rationale": "The provider explicitly reports 1.584
    g_l for its 2 ml methanol input; retain this as a provider-declared rate, not
    an independently verified density conversion. Primary preparation also says final
    0.2% without a stated percent basis; do not infer w/v or v/v or replace the primary
    volume with an assumed mass.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.584",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared
    rate, not an independently verified density conversion. Primary preparation also
    says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace
    the primary volume with an assumed mass."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.584",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared
    rate, not an independently verified density conversion. Primary preparation also
    says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace
    the primary volume with an assumed mass."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.584",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    reports 1.584 g_l for its 2 ml methanol input; retain this as a provider-declared
    rate, not an independently verified density conversion. Primary preparation also
    says final 0.2% without a stated percent basis; do not infer w/v or v/v or replace
    the primary volume with an assumed mass."}]}, {"quantity_id": "q9", "topic": "CuSO4
    x 5 H2O trace-stock stage", "source": [{"evidence_id": "api606", "reference":
    "https://mediadive.dsmz.de/rest/medium/606", "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin",
    "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0200252,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "CuSO4 x 5 H2O", "compound_id": 121, "amount": 5, "unit": "mg", "g_l": 0.005,
    "mmol_l": 0.0200252, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 24; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "CuSO4 x 5 H2O                                                      5.0      mg"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q10", "topic": "MnSO4 x 5 H2O trace-stock
    stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MnSO4 x 5 H2O\",\n                        \"compound_id\": 234,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0414804,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "MnSO4 x 5 H2O", "compound_id": 234, "amount": 10, "unit": "mg", "g_l": 0.01,
    "mmol_l": 0.0414804, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 25; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "MnSO4 x 5 H2O                                                     10.0      mg"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q11", "topic": "Na2MoO4 x 2 H2O trace-stock
    stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 10, "unit": "mg", "g_l": 0.01,
    "mmol_l": 0.0413309, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 26; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Na2MoO4 x 2 H2O                                                   10.0      mg"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q12", "topic": "H3BO3 trace-stock stage",
    "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "H3BO3", "compound_id": 37, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l":
    0.161708, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 27; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "H3BO3                                                             10.0      mg"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q13", "topic": "ZnSO4 x 7 H2O trace-stock
    stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    70,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.07,\n                        \"mmol_l\": 0.243427,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l":
    0.243427, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 28; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "ZnSO4 x 7 H2O                                                     70.0      mg"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q14", "topic": "CoCl2 x 6 H2O trace-stock
    stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0385092,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l":
    0.0385092, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 29; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "CoCl2 x 6 H2O                                                      5.0      mg"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q15", "topic": "FeCl3 x 6 H2O trace-stock
    stage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 3.69965,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "FeCl3 x 6 H2O", "compound_id": 82, "amount": 1, "unit": "g", "g_l": 1, "mmol_l":
    3.69965, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm606",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 30; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "FeCl3 x 6 H2O                                                      1.0       g"}],
    "decision": "correct", "rationale": "This exact value is the provider-declared
    concentration of the separate trace stock, not a direct final-medium ingredient
    rate. Preserve its supported supplied form and stock amount, restore the separate
    stock and receiving dose, and do not silently divide by 1000 or infer final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This exact value is the
    provider-declared concentration of the separate trace stock, not a direct final-medium
    ingredient rate. Preserve its supported supplied form and stock amount, restore
    the separate stock and receiving dose, and do not silently divide by 1000 or infer
    final volume."}]}, {"quantity_id": "q16", "topic": "Trace-stock receiving dose",
    "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\":
    \"Trace elements solution\",\n                        \"solution_id\": 1303,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "solution":
    "Trace elements solution", "solution_id": 1303, "amount": 1, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " Trace element solution (see below)                               1.00       ml"}],
    "decision": "add", "rationale": "The source supplies one explicit stock addition,
    separate from its composition. No final-medium concentration is calculated without
    final-volume support.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent the separately named stock and the explicit 1 ml receiving dose; no
    stock identity may be substituted merely because it contains similar elements.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent the separately named stock and the explicit 1 ml receiving dose; no
    stock identity may be substituted merely because it contains similar elements.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent the separately named stock and the explicit 1 ml receiving dose; no
    stock identity may be substituted merely because it contains similar elements.",
    "missing": true}]}, {"quantity_id": "q17", "topic": "Main water input", "source":
    [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 13; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " Distilled water                                               1000.00       ml"}],
    "decision": "add", "rationale": "Preserve the exact source 1000 ml distilled-water
    input at this stage. It is not a water mass rate or an instruction to make up
    a measured final volume.", "layer_assessments": []}, {"quantity_id": "q18", "topic":
    "Trace-stock water input", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 31; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Distilled water                                                 1000.0      ml"}],
    "decision": "add", "rationale": "Preserve the exact source 1000 ml distilled-water
    input at this stage. It is not a water mass rate or an instruction to make up
    a measured final volume.", "layer_assessments": []}, {"quantity_id": "q19", "topic":
    "Existing pH 7.0", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at
    121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of
    methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object":
    {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a
    filter-sterilized solution of methanol to give a final concentration of 0.2%."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a
    filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}],
    "decision": "evidence_only", "rationale": "The pH value is retained in all layers;
    the missing preparation sequence is assessed separately.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path":
    "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing
    pH 7.0 agrees with the primary and provider; link the exact preparation claim
    without changing the value."}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Existing pH 7.0 agrees with the primary and provider; link the exact preparation
    claim without changing the value."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Existing pH 7.0 agrees with the primary and provider; link the exact preparation
    claim without changing the value."}]}, {"quantity_id": "q20", "topic": "Autoclave
    temperature", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at
    121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of
    methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object":
    {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a
    filter-sterilized solution of methanol to give a final concentration of 0.2%."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a
    filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}],
    "decision": "mixed", "rationale": "The source explicitly supplies this part of
    the staged preparation. The source 0.2% basis is not stated; keep that limitation
    and do not manufacture a stock strength or dilution calculation.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore
    the exact source preparation context in this layer; all quantities and percent-basis
    limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Restore the exact source preparation context in this layer; all quantities and
    percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to
    7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution
    of methanol to give a final concentration of 0.2%.", "decision": "evidence_only",
    "rationale": "The maintained DSM owner already contains this exact main preparation
    statement; preserve it and attach root evidence, without reapplying it as a missing
    field."}]}, {"quantity_id": "q21", "topic": "Autoclave duration", "source": [{"evidence_id":
    "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path":
    "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at
    121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of
    methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object":
    {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a
    filter-sterilized solution of methanol to give a final concentration of 0.2%."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a
    filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}],
    "decision": "mixed", "rationale": "The source explicitly supplies this part of
    the staged preparation. The source 0.2% basis is not stated; keep that limitation
    and do not manufacture a stock strength or dilution calculation.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore
    the exact source preparation context in this layer; all quantities and percent-basis
    limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Restore the exact source preparation context in this layer; all quantities and
    percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to
    7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution
    of methanol to give a final concentration of 0.2%.", "decision": "evidence_only",
    "rationale": "The maintained DSM owner already contains this exact main preparation
    statement; preserve it and attach root evidence, without reapplying it as a missing
    field."}]}, {"quantity_id": "q22", "topic": "Cooling temperature", "source": [{"evidence_id":
    "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path":
    "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at
    121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of
    methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object":
    {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a
    filter-sterilized solution of methanol to give a final concentration of 0.2%."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a
    filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}],
    "decision": "mixed", "rationale": "The source explicitly supplies this part of
    the staged preparation. The source 0.2% basis is not stated; keep that limitation
    and do not manufacture a stock strength or dilution calculation.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore
    the exact source preparation context in this layer; all quantities and percent-basis
    limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Restore the exact source preparation context in this layer; all quantities and
    percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to
    7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution
    of methanol to give a final concentration of 0.2%.", "decision": "evidence_only",
    "rationale": "The maintained DSM owner already contains this exact main preparation
    statement; preserve it and attach root evidence, without reapplying it as a missing
    field."}]}, {"quantity_id": "q23", "topic": "Filtered methanol addition and final
    percentage", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at
    121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of
    methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object":
    {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a
    filter-sterilized solution of methanol to give a final concentration of 0.2%."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a
    filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}],
    "decision": "mixed", "rationale": "The source explicitly supplies this part of
    the staged preparation. The source 0.2% basis is not stated; keep that limitation
    and do not manufacture a stock strength or dilution calculation.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Restore
    the exact source preparation context in this layer; all quantities and percent-basis
    limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Restore the exact source preparation context in this layer; all quantities and
    percent-basis limitations remain source-scoped.", "missing": true}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to
    7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a filter-sterilized solution
    of methanol to give a final concentration of 0.2%.", "decision": "evidence_only",
    "rationale": "The maintained DSM owner already contains this exact main preparation
    statement; preserve it and attach root evidence, without reapplying it as a missing
    field."}]}, {"quantity_id": "q24", "topic": "Existing DSM preparation action and
    order", "source": [{"evidence_id": "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606",
    "raw_path": "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 7.0. Autoclave at
    121\\u00b0C for 15 min. Cool to 50\\u00b0C. Add a filter-sterilized solution of
    methanol to give a final concentration of 0.2%.\"\n                    }", "exact_decoded_object":
    {"step": "Adjust pH to 7.0. Autoclave at 121°C for 15 min. Cool to 50°C. Add a
    filter-sterilized solution of methanol to give a final concentration of 0.2%."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "Adjust pH to 7.0. Autoclave at 121C for 15 min. Cool to 50C. Add a
    filter-sterilized\nsolution of methanol to give a final concentration of 0.2%."}],
    "decision": "evidence_only", "rationale": "The single composite DSM step already
    preserves the main instructions. Structured splitting may improve representation
    but must not lose any existing description.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "preparation_steps[0].action", "stored_value": "AUTOCLAVE", "decision":
    "evidence_only", "rationale": "AUTOCLAVE is a coarse existing action for the composite
    source paragraph; its complete description preserves the actual operations."},
    {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml", "field_path":
    "preparation_steps[0].step_number", "stored_value": 1, "decision": "evidence_only",
    "rationale": "Local ordering index does not supply an experimental amount."}]},
    {"quantity_id": "q25", "topic": "Purified agar supplied grade", "source": [{"evidence_id":
    "api606", "reference": "https://mediadive.dsmz.de/rest/medium/606", "raw_path":
    "REVIEW_WORK/batch065/source01-03/api606.bin", "raw_sha256": "739470b1c21651c90a42d42d07c705c5182b3a88b8287a0acd5e89e271727e92",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T11:30:48.316298Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Agar\",\n                        \"compound_id\": 3,\n                        \"attribute\":
    \"purified \",\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "attribute": "purified
    ", "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": " Purified agar                                                   15.00        g"}],
    "decision": "correct", "rationale": "The API attribute and primary both specify
    purified agar. Generic CHEBI agar remains chemically appropriate, while supplied-grade
    specificity needs retention.", "layer_assessments": [{"path": "data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml",
    "field_path": "ingredients[6].preferred_term", "stored_value": "Agar", "decision":
    "correct", "rationale": "Retain the source purified-grade qualifier with the existing
    generic agar ontology; no new chemical identity or amount is implied."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml", "field_path":
    "ingredients[6].preferred_term", "stored_value": "Agar", "decision": "correct",
    "rationale": "Retain the source purified-grade qualifier with the existing generic
    agar ontology; no new chemical identity or amount is implied."}, {"path": "data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml",
    "field_path": "ingredients[6].preferred_term", "stored_value": "Agar", "decision":
    "correct", "rationale": "Retain the source purified-grade qualifier with the existing
    generic agar ontology; no new chemical identity or amount is implied."}]}, {"quantity_id":
    "q26", "topic": "DSM15625 source alternative only", "source": [{"evidence_id":
    "dsm606", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium606.pdf",
    "raw_path": "REVIEW_WORK/batch065/source01-03/dsm606.bin", "raw_sha256": "5545dc1546f035b266bcf870479b2fb2f8f837bff07ecfc7da60f3a7eb54fcf4",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T11:30:48.673162Z",
    "quote": "For DSM 15625 replace the methanol with a filter-sterilized solution
    of\ntrimethylammonium chloride to give a final concentration of 0.1%."}], "decision":
    "add", "rationale": "This strain-specific alternative replaces methanol with filter-sterilized
    trimethylammonium chloride at source-stated final 0.1%, whose percent basis is
    unspecified. Preserve it as an explicitly separate source variant, not as another
    generic ingredient or a change to the selected methanol formulation. No strain-growth
    assertion is inferred.", "layer_assessments": []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: 'All fifteen distinct primary chemical IDs and their secondary slots resolve
    to current OLS canonical labels with source-consistent supplied forms, including
    calcium hexahydrate, manganese pentahydrate, molybdate dihydrate, cobalt hexahydrate
    and ferric chloride hexahydrate. MIM identifier/ontology row unions preserve exact
    statuses: CoCl2 x 6 H2O has a REJECTED preferred-name row while Cobalt chloride
    hexahydrate is MAPPED to the same53503 identity; neither status invalidates the
    independently verified chemical form. Generic agar does not by itself carry the
    purified-grade requirement.'
  target_ids:
  - CultureMech:006095
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Current source bytes, complete histories and scoped historical reports
    were read. Missing claim-level linkage and any malformed historical metadata are
    distinguished from authenticated source bytes; originals remain append-only.
  target_ids:
  - CultureMech:006095
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
  - CultureMech:006095
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:006095
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006095-restore-separate-trace-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore separate trace-stock topology
  description: Seven direct ingredient rates in every layer are exactly the provider
    concentrations of trace solution1303. They are incorrectly presented alongside
    main-recipe rates, while the named stock and its 1 ml receiving dose are absent.
    Preserve all seven source masses/forms at stock stage and restore the separate
    addition. Do not turn them into guessed final-medium rates.
  target_ids:
  - CultureMech:006095
  field_paths:
  - solutions
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  evidence_ids:
  - dsm606
  - api606
  - quantities
  - writer-mediadive
  - writer-cleanup
  rule_id: custom-stock-stage-flattening
  native_severity: P2
  normalization_reason: 'Major: correct source stock concentrations are assigned to
    the wrong solution stage. Their units match but denominators and preparation roles
    differ; this is not an invalid CHEBI claim.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-006095-preserve-source-preparation-and-supplied-form-distinctions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preserve source preparation and supplied-form distinctions
  description: The DSM owner already retains the pH/autoclave/cooling/filtered-methanol
    paragraph. The KOMODO owner and generated target omit it, consistent with a current
    resolver that does not copy preparation_steps. All layers also lose the purified-agar
    qualifier and omit the separately identified DSM15625 source alternative. The
    API methanol g_l is credited as provider data while primary 2 ml and unspecified-basis
    0.2% remain separate claims.
  target_ids:
  - CultureMech:006095
  field_paths:
  - preparation_steps
  - ingredients[6].preferred_term
  - evidence
  - data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml::preparation_steps[0].description
  - variant_modifications
  evidence_ids:
  - dsm606
  - api606
  - quantities
  - owner-1
  - owner-2
  - writer-resolver
  - writer-merge
  - writer-formulation
  rule_id: custom-source-preparation-loss
  native_severity: P3
  normalization_reason: Major normalization of a preparation-completeness concern
    because the generated target loses the entire operational sequence and supplied-grade/variant
    distinctions, while the maintained DSM owner already documents part of it. No
    supported quantity is replaced.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-006095-qualify-the-unverified-imported-atmosphere-flag
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the unverified imported atmosphere flag
  description: 'The target and KOMODO owner say Aerobic: No. The historical catalogue
    excerpt contains a false flag, but the live catalogue is unavailable and the primary
    PDF/API provide no directly scoped atmosphere statement. This imported metadata
    is not proof of anaerobic growth, and absence of such a statement does not justify
    flipping it to aerobic.'
  target_ids:
  - CultureMech:006095
  field_paths:
  - notes
  - data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml::notes
  evidence_ids:
  - historical-reader
  - komodo606
  - komodoList
  - dsm606
  - api606
  - writer-komodo
  rule_id: custom-unverified-source-flag
  native_severity: P3
  normalization_reason: 'Minor: unresolved semantics and current source access limit
    one imported metadata flag; no contradictory growth condition has been established.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-006095-preserve-and-qualify-historical-event-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve and qualify historical event metadata
  description: KOMODO import events contain a literal .fZ timestamp and resolver events
    omit a UTC offset. Historical concentration reports preserve unresolved claims
    and exact source mappings, but are not independent proof of those historical retrieval
    events. All current concentration claims also lack attached evidence. Fresh API
    bytes match both October606 report source digests and their exact objects, but
    this does not authenticate historical access events or the unavailable entire
    KOMODO catalogue.
  target_ids:
  - CultureMech:006095
  field_paths:
  - data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml::curation_history[0].timestamp
  - data/merge_yaml/merged/COLBY_AND_ZATHMAN_MEDIUM.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml::curation_history[1].timestamp
  evidence_ids:
  - history
  - historical-reader
  - writer-komodo
  rule_id: custom-event-metadata-provenance
  native_severity: P3
  normalization_reason: 'Minor: malformed or timezone-unspecified historical event
    metadata limits auditability without changing any recipe quantity; native P4.4
    only covers a one-event history and is not invoked.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate the two maintained contributors to represent source trace solution1303
    separately, with exact stock components, solvent input and explicit receiving
    dose. Preserve supported main rates. Regenerate only after formulation compatibility
    is reconciled; do not infer final volume or compute ungrounded stock dilutions.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006095
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Retain the existing DSM main preparation and repair the missing KOMODO/target
    context using exact source claims. Preserve purified agar. Keep the DSM15625 alternative
    separate from the generic methanol formulation and leave bare-percent bases unresolved.
    Use schema-supported root evidence for source stages; do not overwrite the already-correct
    owner paragraph or force incompatible owners into a merge.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006095
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Retain original provenance and qualify the imported atmosphere flag
    as unverified until an exact source field and its semantics are authenticated.
    Do not infer growth or replace it with an opposite atmosphere claim.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006095
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Retain every original event byte-for-byte. If authoritative provenance
    is recovered, append a verified correction or context event; never invent or overwrite
    its timestamp. Link fresh source evidence separately and preserve unresolved accession
    limitations.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006095
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Original malformed and timezone-unspecified events remain byte-preserved; any
    recovered correction is appended with verified provenance.
  - All new amount, stage and preparation claims carry exact current source locators;
    old unsupported decisions remain historical observations.
  generator: src/culturemech/merge/merger.py
limitations:
- Exact historical KOMODO MediaInfo606 and MediaList routes both returned403; source
  identity on that branch remains partial. Fresh DSM/API support does not restore
  the original whole catalogue or reauthenticate past retrieval events.
- The primary gives water inputs rather than explicit final makeup for main and stock
  stages. Provider g_l values are credited at their named source stages only; no downstream
  stock rates are calculated.
- Methanol1.584 g/l is a provider declaration; no independent density conversion is
  established. The primary final0.2% and strain-specific final0.1% do not state percent
  basis, so no w/v or v/v assumption is made.
- DSM15625 is only the label of the primary source alternative; its catalogue conditions,
  generic applications and bacterial filing are not transferred as new growth assertions.
  The target remains the generic methanol formulation.
- Current writer behavior does not prove historical causality. Existing history is
  append-only; native reference validation performed zero checks.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
