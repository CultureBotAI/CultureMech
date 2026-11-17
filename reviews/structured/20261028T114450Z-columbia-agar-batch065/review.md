# Scientific review of columbia_agar

- Review: 20261028T114450Z-columbia-agar-batch065
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T11:30:41.047366Z
- Finished UTC: 2026-10-28T11:44:50.702567Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

All four source 715 ingredient rates are supported, including eight already authenticated owner claims. The generated target loses evidence and preparation, source water is absent, and the KG link points to the distinct Columbia Blood Agar 687. Original KOMODO timestamp defects remain bounded provenance findings.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch065 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006352 | data/merge_yaml/merged/COLUMBIA_AGAR.yaml | generated | columbia_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006352 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:006352 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:006352 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:006352 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact Columbia Agar715 versus Columbia Blood Agar 687

identity: concern. Targets: CultureMech:006352.

Selected source identities identify 715 and the four current primary/API ingredients agree. Every selected layer nevertheless asserts kg_microbe_match=mediadive.medium:687, whose current provider identity and formulation differ. Shared CHEBI ingredient sets cannot establish equivalent media. Exact current KOMODO 715 and catalogue requests returned 403, so its separate historical mapping remains a bounded limitation.

### Classification, supplied forms and preparation scope

consistency: supported. Targets: CultureMech:006352.

Solid agar, complex/undefined composition and the existing pH range are consistent with source 715. Agar 10 is correct for this source and must not be changed to the blood-agar-base 15. The undefined peptone mixture is not forced into a single chemical identity. Current starch/NaCl/agar primary and secondary labels match their exact authority objects. No source-named organism or growth outcome is inferred.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:006352.

All five exact historical reports were read. The current API 715 raw digest matches both old source reports, and all twelve historical quantity/solvent/preparation objects plus eight attached owner quantity claims match literally and by JSON locator. The catalogue mapping claim is separate and remains unauthenticated because current catalogue/page requests return 403. Old zero-check reports are incomplete predecessors, not evidence against already authenticated current owner claims. Current merge/import/KG and history writers were read with their exact present scopes. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:006352.

All 12 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006352", "selected_concentration_field_count": 12, "selected_concentration_fields_covered": 12, "decisions": [{"decision_id": "q1", "subject": "Peptone mixture target", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "23", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main ingredient on provider-declared basis", "interpretation": "The generated target value agrees with the exact primary mass and provider g_l but lacks the existing owner evidence. Retain the number with scoped evidence. Listed water and volume=1000 metadata do not independently establish a measured final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Peptone mixture\",\n                        \"compound_id\": 156,\n                        \"amount\": 23,\n                        \"unit\": \"g\",\n                        \"g_l\": 23,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Special mixture of peptones                23.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Peptone mixture maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "23", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "23", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity claims", "interpretation": "Both maintained owners already attach exact literal API excerpts and the current matching response digest for this quantity. Credit that existing authentication. It covers provider-declared g_l and exact source ingredient identity, not a measured final volume, the separate KOMODO catalogue bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Peptone mixture\",\n                        \"compound_id\": 156,\n                        \"amount\": 23,\n                        \"unit\": \"g\",\n                        \"g_l\": 23,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Special mixture of peptones                23.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "Starch target", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main ingredient on provider-declared basis", "interpretation": "The generated target value agrees with the exact primary mass and provider g_l but lacks the existing owner evidence. Retain the number with scoped evidence. Listed water and volume=1000 metadata do not independently establish a measured final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Starch                                      1.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "Starch maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity claims", "interpretation": "Both maintained owners already attach exact literal API excerpts and the current matching response digest for this quantity. Credit that existing authentication. It covers provider-declared g_l and exact source ingredient identity, not a measured final volume, the separate KOMODO catalogue bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Starch                                      1.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "NaCl target", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main ingredient on provider-declared basis", "interpretation": "The generated target value agrees with the exact primary mass and provider g_l but lacks the existing owner evidence. Retain the number with scoped evidence. Listed water and volume=1000 metadata do not independently establish a measured final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 85.5578,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "NaCl                                        5.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "NaCl maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity claims", "interpretation": "Both maintained owners already attach exact literal API excerpts and the current matching response digest for this quantity. Credit that existing authentication. It covers provider-declared g_l and exact source ingredient identity, not a measured final volume, the separate KOMODO catalogue bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 85.5578,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "NaCl                                        5.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Agar target", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main ingredient on provider-declared basis", "interpretation": "The generated target value agrees with the exact primary mass and provider g_l but lacks the existing owner evidence. Retain the number with scoped evidence. Listed water and volume=1000 metadata do not independently establish a measured final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 29.7327,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Agar                                       10.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Agar maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity claims", "interpretation": "Both maintained owners already attach exact literal API excerpts and the current matching response digest for this quantity. Credit that existing authentication. It covers provider-declared g_l and exact source ingredient identity, not a measured final volume, the separate KOMODO catalogue bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 29.7327,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Agar                                       10.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Absolute main solvent input", "interpretation": "The source lists 1000 ml distilled water. Preserve this missing absolute input without inferring make-up to a final 1 L or introducing a new dilution.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Distilled water                          1000.0   ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Retained pH range", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}], "decision": "evidence_only", "stage": "Main preparation pH", "interpretation": "The existing structured 7.0 to 7.2 range agrees with the primary and API preparation. It is not an organism-growth optimum claim. Attach new root evidence scoped to the range.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.0 - 7.2.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Adjust pH to 7.0 - 7.2.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Direct DSM preparation", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0 - 7.2."}], "decision": "evidence_only", "stage": "Main pH adjustment", "interpretation": "The direct DSM owner correctly retains the pH-adjustment step. The target and KOMODO owner omit this preparation context; preserve the correct existing step and restore it only within the exact source branch.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.0 - 7.2.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf", "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b", "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37", "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Adjust pH to 7.0 - 7.2.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Linked medium687 comparison", "local_fields": [], "decision": "unsupported", "stage": "Identity comparison only; no dose transfer", "interpretation": "The local KG link identifies Columbia Blood Agar 687, whose current API includes a distinct blood-agar base and blood addition. Its base agar row is 15 rather than the selected source 10. This demonstrates non-equivalence; no 687 ingredient, processing setting or product composition transfers to 715.", "sources": [{"locator": "$.data.medium", "source_key": "api687", "reference": "https://mediadive.dsmz.de/rest/medium/687", "source_raw_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9", "source_text_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9", "accessed_at": "2026-10-28T11:31:04.031183Z", "exact_source_quote": "{\n            \"id\": 687,\n            \"name\": \"COLUMBIA BLOOD AGAR\",\n            \"complex_medium\": \"yes\",\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf\"\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api687", "reference": "https://mediadive.dsmz.de/rest/medium/687", "source_raw_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9", "source_text_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9", "accessed_at": "2026-10-28T11:31:04.031183Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch065/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:006352.

data/merge_yaml/merged/COLUMBIA_AGAR.yaml: primary 3/4, secondary 3/4; data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml: primary 3/4, secondary 3/4; data/normalized_yaml/bacterial/columbia_agar.yaml: primary 3/4, secondary 3/4. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:006352.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:006352.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: The KG cross-reference identifies a different medium

major / open / confirmed; issue key: culturemech-006352-kg-link-points-to-distinct-blood-agar.

All selected layers link to mediadive.medium:687 Columbia Blood Agar, while source 715 is Columbia Agar with a different formulation. The current matcher uses CHEBI/FOODON identity sets and ignores amounts, preparation and ungrounded peptone, so a set match is not proof of source equivalence.

### f2: Generated content omits supported owner evidence and source context

major / open / confirmed; issue key: culturemech-006352-generated-preparation-evidence-and-water-loss.

Both maintained owners already contain four authenticated quantity claims, but the target contains none. The direct DSM owner retains pH preparation while the target and KOMODO owner omit it; all selected layers omit absolute source water. Current conservative merging retains scientific fields and rejects incompatible projections, so old generated omissions are not attributed to an ingredient-only current merger.

### f3: KOMODO import history contains an unparseable timestamp

minor / open / confirmed; issue key: culturemech-006352-malformed-original-komodo-history.

The KOMODO owner has literal .fZ in its original import event and a later enrichment timestamp without timezone. The current strftime format contains unsupported %f, consistent with the observed defect but not proof of historical execution. The exact API quantity authentication does not reconstruct those event times.

## Recommended Actions And Acceptance Checks

### action1

Reconcile or remove the unsupported equivalent-medium link using exact source identities and formulation-aware comparison. Preserve correct 715 quantities and do not import blood or different base composition from 687. Review matcher scope before regenerating downstream linked content.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Retain all eight existing owner quantity claims and the correct DSM preparation. Repair the missing water and KOMODO preparation context with exact source evidence, reconcile source ownership explicitly, and regenerate through the present conservative guard. Do not invent autoclave parameters or treat the generic source recipe as growth evidence.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Preserve original event bytes and append verified corrective context with the actual current curation date. Fix timestamp generation for future writes; do not replace historical timestamps with guessed dates.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/COLUMBIA_AGAR.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/columbia_agar.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch065/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch065/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch065/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch065/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz715 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api715 | https://mediadive.dsmz.de/rest/medium/715; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| api687 | https://mediadive.dsmz.de/rest/medium/687; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| komodo715 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=715; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:28017 = starch; definition ['The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch065/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/columbia_agar.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api715 raw bytes exactly match the cited historical SHA, and 6 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api715 raw bytes exactly match the cited historical SHA, and 6 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/columbia_agar.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLUMBIA_AGAR.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch065/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer22 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer23 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer24 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer25 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer26 | scripts/enrich_with_chebi.py; RecipeEnricher.enrich_ingredient; enrich_recipe; enrich_file | context_only | Current RecipeEnricher.enrich_ingredient skips already grounded entries and delegates missing-term mapping to ChemicalMapper; enrich_recipe traverses ingredient and solution structure, and enrich_file writes results and history. Only the read wrapper behavior is claimed here; the mapper is not treated as an independent supplied-form authority. |
| writer27 | scripts/enrich_with_mediaingredientmech.py; main | context_only | Current main orchestrates a local or cloned MIM repository, its loader and ingredient linker. The CLI orchestration was read; it does not itself verify source recipe quantities, supplied chemical forms or the validity of historical MIM assertions. Linker internals are not claimed as separately audited scientific evidence. |
| writer28 | scripts/migrate_chebi_regrounding.py; rewrite_entry; migrate_file | context_only | Current rewrite_entry applies configured exact-ID/label remaps across primary and secondary slots; migrate_file records applied changes. A successful current mapping operation does not establish source-specific hydrate or stereochemical equivalence. |
| writer29 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer30 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. The already structured source-supported 7.0 to 7.2 range is credited; no new range is inferred. |
| writer31 | scripts/normalize_media_names_to_snake_case.py; process_file; add_curation_history | context_only | Current process_file preserves the original medium name while normalizing its machine name; add_curation_history appends a naming event. Name normalization does not prove equivalence of differently maintained source branches or recipe variants. |
| writer32 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer33 | scripts/repair_komodo_strain_backlinks.py; PARENTS; CHILDREN; repair_parent; plan_repairs; _upsert_event | context_only | Current repair_parent and plan_repairs target only the explicitly listed 131/777 parents and their two strain children. They do not repair the selected records. _upsert_event replaces a matching curator/action event or appends it; this existing behavior is not permission to rewrite history during this review. |
| writer34 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer35 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer36 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer37 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes recognized solvents; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer38 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer39 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer40 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer41 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer42 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| attached-auth | REVIEW_WORK/batch065/record06/attached-claim-authentication.json; claims | supports | All eight attached owner quantity claims match exact current API raw bytes, their quoted objects and supplied local ingredient rows. Target has no attached quantity claims. The separate KOMODO catalogue claim remains outside this authentication. |
| komodo-writer | scripts/review_komodo_concentration_evidence.py; identity_problem; review; mapping_evidence; verify_mapping | context_only | Current identity_problem checks exact accession/name/source and rejects variants or conflicting pH. review separates identity mapping from accepted quantity excerpts; verify_mapping checks persisted evidence and preserves historical curation prefixes through successors. These current guards and matching API bytes do not authenticate the unrecovered historical catalogue body or execution. |
| quantity-inventory | REVIEW_WORK/batch065/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact current KOMODO 715 and the historical catalogue endpoint returned 403; the direct primary 715 and current matching API authenticate formulation amounts but not the separately cited historical catalogue bytes or access time.
- Listed water and provider volume metadata are not a measured final-volume instruction. No687 ingredient, processing condition, manufacturer blend or organism-growth claim transfers into 715.
- No ingredient values, records, original evidence or historical events were changed. Generic mixture and polymer labels are not treated as pure compounds with exact formulation stoichiometry.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T114450Z-columbia-agar-batch065
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of columbia_agar
started_at: '2026-10-28T11:30:41.047366Z'
finished_at: '2026-10-28T11:44:50.702567Z'
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
summary: All four source 715 ingredient rates are supported, including eight already
  authenticated owner claims. The generated target loses evidence and preparation,
  source water is absent, and the KG link points to the distinct Columbia Blood Agar
  687. Original KOMODO timestamp defects remain bounded provenance findings.
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
  - path: data/merge_yaml/merged/COLUMBIA_AGAR.yaml
    sha256: b1f7eef86b59624b8d296119e930a3eb99571a6a65f2d7e8fd356b87c5e46f2e
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    sha256: 8b7413a35d81feb9f02529374723d29b4af833b4baf58fdcae1b979fcb334268
    role: context
  - path: data/normalized_yaml/bacterial/columbia_agar.yaml
    sha256: 869b9ce3f4056c131aeb901fd84d77ac53a16ca456155a88026c36d66ceae169
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml.md
    sha256: 70ce0c66aad4fc3bf42578ea0ec02aebccba43b3662de89c2d3d4379b07e39ab
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/columbia_agar.yaml.md
    sha256: b975d00f0af227be868fc537bd79b1edc78c793d65bc59189f278ea461aef8f0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLUMBIA_AGAR.md
    sha256: 303232f99d57d9eccaf20059269bc7bcadd333ea2d404293e2485b4283cd9d31
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.md
    sha256: c06957785fab76c4510cac7bb9f316fb95b8529eab6a43555e29f4467c1d45bd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/columbia_agar.md
    sha256: 1f575a2318f4cae53da1d31f8be1afc573bc5d8993a60cbb8284c0e826638de1
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
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
  - path: scripts/repair_komodo_strain_backlinks.py
    sha256: 06d56149f4e8333f31ae6dd7e4b9127881227810bc957429c849ba00de21c963
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
  selection: Authoritative batch065 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006352
targets:
- target_id: CultureMech:006352
  path: data/merge_yaml/merged/COLUMBIA_AGAR.yaml
  label: columbia_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006352
  command: just validate-schema data/merge_yaml/merged/COLUMBIA_AGAR.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006352
  command: just validate-strict data/merge_yaml/merged/COLUMBIA_AGAR.yaml --workers
    1 --out REVIEW_WORK/batch065/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006352
  command: just validate-terms data/merge_yaml/merged/COLUMBIA_AGAR.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:006352
  command: just validate-references data/merge_yaml/merged/COLUMBIA_AGAR.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/COLUMBIA_AGAR.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T11:44:50.692904Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: b1f7eef86b59624b8d296119e930a3eb99571a6a65f2d7e8fd356b87c5e46f2e
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T11:44:50.693057Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 8b7413a35d81feb9f02529374723d29b4af833b4baf58fdcae1b979fcb334268
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/columbia_agar.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T11:44:50.693087Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 869b9ce3f4056c131aeb901fd84d77ac53a16ca456155a88026c36d66ceae169
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch065/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:42.059788Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: c0a0a5a979aa20f33987a0e01bb43eee18453de2970e2004f1d98199f7507d16
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch065/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:42.962663Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 80ac04acaddae4b7e00ee2209c2651f2ac8cb3d31d3eadcc8ca3b735d89dde2e
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch065/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:43.974766Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: ae82952928951b5c8b4c070f5e3eb01967bbc96eb797d851fbc82e5a5a2c8724
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch065/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:44.646532Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: e58a2b96a520d2b4450520140d6026c75dc5d5ca404f6486e3cf2c6e02c20b0e
- evidence_id: dsmz715
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:04.497933Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b
- evidence_id: api715
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/715
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:04.373049Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e
- evidence_id: api687
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/687
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:04.031183Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9
- evidence_id: komodo715
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=715
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:04.031148Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 611f6c54c7fcdf752fbebb6e4aa16e9372ac5dc36fdbe2d431de5a2f333b49b4
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:04.031104Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: f0ebee33512659f4198e3f76bb1e73ab89a980fefee160cf3235caa69d62bad7
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:04.031044Z'
  support: supports
  summary: OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of
    polysaccharides extracted from species of red algae. Its two main components are
    agarose and agaropectin. Agarose is the component responsible for the high-strength
    gelling properties of agar, while agaropectin provides the viscous properties.'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:04.030956Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:04.030681Z'
  support: supports
  summary: OLS current exact CHEBI:28017 = starch; definition ['The most important
    reserve polysaccharide found in plants. It is a glucan consisting of amylose and
    amylopectin.']; formula None; mass None; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch065/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T11:44:50.695698Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 921d89a6d3641bac4c867adb3f31bdbe32ff5b9c1864120f4a2a15791491a997
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/columbia_agar.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:44:50.696340Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api715 raw bytes exactly match the cited historical SHA, and 6
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: b975d00f0af227be868fc537bd79b1edc78c793d65bc59189f278ea461aef8f0
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:44:50.696366Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api715 raw bytes exactly match the cited historical SHA, and 6
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 70ce0c66aad4fc3bf42578ea0ec02aebccba43b3662de89c2d3d4379b07e39ab
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:44:50.696392Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: c06957785fab76c4510cac7bb9f316fb95b8529eab6a43555e29f4467c1d45bd
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/columbia_agar.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:44:50.696416Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 1f575a2318f4cae53da1d31f8be1afc573bc5d8993a60cbb8284c0e826638de1
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLUMBIA_AGAR.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:44:50.696436Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 303232f99d57d9eccaf20059269bc7bcadd333ea2d404293e2485b4283cd9d31
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch065/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T11:44:50.696463Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 82001c796cf451959bc20f194a47ccee5d866650deaa9bd1e44c1366bf839aaf
- evidence_id: writer22
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T11:44:50.696525Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer23
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T11:44:50.696556Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer24
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T11:44:50.696585Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer25
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T11:44:50.696610Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer26
  kind: record_content
  reference: scripts/enrich_with_chebi.py
  locator: RecipeEnricher.enrich_ingredient; enrich_recipe; enrich_file
  accessed_at: '2026-10-28T11:44:50.696640Z'
  support: context_only
  summary: Current RecipeEnricher.enrich_ingredient skips already grounded entries
    and delegates missing-term mapping to ChemicalMapper; enrich_recipe traverses
    ingredient and solution structure, and enrich_file writes results and history.
    Only the read wrapper behavior is claimed here; the mapper is not treated as an
    independent supplied-form authority.
  snapshot_sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
- evidence_id: writer27
  kind: record_content
  reference: scripts/enrich_with_mediaingredientmech.py
  locator: main
  accessed_at: '2026-10-28T11:44:50.696662Z'
  support: context_only
  summary: Current main orchestrates a local or cloned MIM repository, its loader
    and ingredient linker. The CLI orchestration was read; it does not itself verify
    source recipe quantities, supplied chemical forms or the validity of historical
    MIM assertions. Linker internals are not claimed as separately audited scientific
    evidence.
  snapshot_sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
- evidence_id: writer28
  kind: record_content
  reference: scripts/migrate_chebi_regrounding.py
  locator: rewrite_entry; migrate_file
  accessed_at: '2026-10-28T11:44:50.696685Z'
  support: context_only
  summary: Current rewrite_entry applies configured exact-ID/label remaps across primary
    and secondary slots; migrate_file records applied changes. A successful current
    mapping operation does not establish source-specific hydrate or stereochemical
    equivalence.
  snapshot_sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
- evidence_id: writer29
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T11:44:50.696709Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer30
  kind: record_content
  reference: scripts/migrate_ph_range.py
  locator: parse_ph_range; migrate_one
  accessed_at: '2026-10-28T11:44:50.696730Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. The already structured source-supported
    7.0 to 7.2 range is credited; no new range is inferred.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer31
  kind: record_content
  reference: scripts/normalize_media_names_to_snake_case.py
  locator: process_file; add_curation_history
  accessed_at: '2026-10-28T11:44:50.696752Z'
  support: context_only
  summary: Current process_file preserves the original medium name while normalizing
    its machine name; add_curation_history appends a naming event. Name normalization
    does not prove equivalence of differently maintained source branches or recipe
    variants.
  snapshot_sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
- evidence_id: writer32
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T11:44:50.696773Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer33
  kind: record_content
  reference: scripts/repair_komodo_strain_backlinks.py
  locator: PARENTS; CHILDREN; repair_parent; plan_repairs; _upsert_event
  accessed_at: '2026-10-28T11:44:50.696794Z'
  support: context_only
  summary: Current repair_parent and plan_repairs target only the explicitly listed
    131/777 parents and their two strain children. They do not repair the selected
    records. _upsert_event replaces a matching curator/action event or appends it;
    this existing behavior is not permission to rewrite history during this review.
  snapshot_sha256: 06d56149f4e8333f31ae6dd7e4b9127881227810bc957429c849ba00de21c963
- evidence_id: writer34
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T11:44:50.696814Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer35
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T11:44:50.696845Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer36
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T11:44:50.696870Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer37
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T11:44:50.696904Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes recognized solvents; _is_api_stock_addition distinguishes
    stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer38
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T11:44:50.696931Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer39
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T11:44:50.696952Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer40
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T11:44:50.696974Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer41
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T11:44:50.696996Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer42
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T11:44:50.697022Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: attached-auth
  kind: record_content
  reference: REVIEW_WORK/batch065/record06/attached-claim-authentication.json
  locator: claims
  accessed_at: '2026-10-28T11:44:50.697204Z'
  support: supports
  summary: All eight attached owner quantity claims match exact current API raw bytes,
    their quoted objects and supplied local ingredient rows. Target has no attached
    quantity claims. The separate KOMODO catalogue claim remains outside this authentication.
  snapshot_sha256: 98faafd090c7c9f2a76659daa1d8e28151025fa65160ad97e1f2f07f295cf871
- evidence_id: komodo-writer
  kind: record_content
  reference: scripts/review_komodo_concentration_evidence.py
  locator: identity_problem; review; mapping_evidence; verify_mapping
  accessed_at: '2026-10-28T11:44:50.702251Z'
  support: context_only
  summary: Current identity_problem checks exact accession/name/source and rejects
    variants or conflicting pH. review separates identity mapping from accepted quantity
    excerpts; verify_mapping checks persisted evidence and preserves historical curation
    prefixes through successors. These current guards and matching API bytes do not
    authenticate the unrecovered historical catalogue body or execution.
  snapshot_sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch065/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T11:44:50.702498Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 32c22c32059a0848fcf26b2e63df07e2083d53640d64796aefbcae949d297774
assessments:
- assessment_id: a1
  area: identity
  topic: Exact Columbia Agar715 versus Columbia Blood Agar 687
  outcome: concern
  summary: Selected source identities identify 715 and the four current primary/API
    ingredients agree. Every selected layer nevertheless asserts kg_microbe_match=mediadive.medium:687,
    whose current provider identity and formulation differ. Shared CHEBI ingredient
    sets cannot establish equivalent media. Exact current KOMODO 715 and catalogue
    requests returned 403, so its separate historical mapping remains a bounded limitation.
  target_ids:
  - CultureMech:006352
  evidence_ids:
  - local0
  - local1
  - local2
  - dsmz715
  - api715
  - api687
  - komodo715
  - komodoList
- assessment_id: a2
  area: consistency
  topic: Classification, supplied forms and preparation scope
  outcome: supported
  summary: Solid agar, complex/undefined composition and the existing pH range are
    consistent with source 715. Agar 10 is correct for this source and must not be
    changed to the blood-agar-base 15. The undefined peptone mixture is not forced
    into a single chemical identity. Current starch/NaCl/agar primary and secondary
    labels match their exact authority objects. No source-named organism or growth
    outcome is inferred.
  target_ids:
  - CultureMech:006352
  evidence_ids:
  - grounding
  - dsmz715
  - api715
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: All five exact historical reports were read. The current API 715 raw digest
    matches both old source reports, and all twelve historical quantity/solvent/preparation
    objects plus eight attached owner quantity claims match literally and by JSON
    locator. The catalogue mapping claim is separate and remains unauthenticated because
    current catalogue/page requests return 403. Old zero-check reports are incomplete
    predecessors, not evidence against already authenticated current owner claims.
    Current merge/import/KG and history writers were read with their exact present
    scopes. Current conservative merging preserves scientific fields and rejects incompatible
    formulations. Inspected writer behavior is described separately by exact file
    and function; it does not prove historical execution.
  target_ids:
  - CultureMech:006352
  evidence_ids:
  - history-auth
  - writer22
  - writer23
  - writer24
  - writer25
  - writer26
  - writer27
  - writer28
  - writer29
  - writer30
  - writer31
  - writer32
  - writer33
  - writer34
  - writer35
  - writer36
  - writer37
  - writer38
  - writer39
  - writer40
  - writer41
  - writer42
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 12 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:006352
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006352",
    "selected_concentration_field_count": 12, "selected_concentration_fields_covered":
    12, "decisions": [{"decision_id": "q1", "subject": "Peptone mixture target", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "23", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "Main ingredient on provider-declared basis", "interpretation": "The
    generated target value agrees with the exact primary mass and provider g_l but
    lacks the existing owner evidence. Retain the number with scoped evidence. Listed
    water and volume=1000 metadata do not independently establish a measured final
    volume.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256":
    "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256":
    "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at":
    "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Peptone mixture\",\n                        \"compound_id\":
    156,\n                        \"amount\": 23,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 23,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-4", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Special mixture
    of peptones                23.0    g", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q2", "subject": "Peptone mixture maintained owners",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "23", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "23", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity
    claims", "interpretation": "Both maintained owners already attach exact literal
    API excerpts and the current matching response digest for this quantity. Credit
    that existing authentication. It covers provider-declared g_l and exact source
    ingredient identity, not a measured final volume, the separate KOMODO catalogue
    bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Peptone mixture\",\n                        \"compound_id\":
    156,\n                        \"amount\": 23,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 23,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-4", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Special mixture
    of peptones                23.0    g", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q3", "subject": "Starch target", "local_fields": [{"record_path":
    "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "Main ingredient on provider-declared basis", "interpretation": "The
    generated target value agrees with the exact primary mass and provider g_l but
    lacks the existing owner evidence. Retain the number with scoped evidence. Listed
    water and volume=1000 metadata do not independently establish a measured final
    volume.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256":
    "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256":
    "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at":
    "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Starch\",\n                        \"compound_id\":
    199,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 5-5", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Starch                                      1.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "Starch maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity
    claims", "interpretation": "Both maintained owners already attach exact literal
    API excerpts and the current matching response digest for this quantity. Credit
    that existing authentication. It covers provider-declared g_l and exact source
    ingredient identity, not a measured final volume, the separate KOMODO catalogue
    bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Starch\",\n                        \"compound_id\":
    199,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 5-5", "source_key": "dsmz715", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Starch                                      1.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject":
    "NaCl target", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main ingredient on provider-declared
    basis", "interpretation": "The generated target value agrees with the exact primary
    mass and provider g_l but lacks the existing owner evidence. Retain the number
    with scoped evidence. Listed water and volume=1000 metadata do not independently
    establish a measured final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    85.5578,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "NaCl                                        5.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject":
    "NaCl maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity
    claims", "interpretation": "Both maintained owners already attach exact literal
    API excerpts and the current matching response digest for this quantity. Credit
    that existing authentication. It covers provider-declared g_l and exact source
    ingredient identity, not a measured final volume, the separate KOMODO catalogue
    bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    85.5578,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "NaCl                                        5.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject":
    "Agar target", "local_fields": [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Main ingredient on provider-declared
    basis", "interpretation": "The generated target value agrees with the exact primary
    mass and provider g_l but lacks the existing owner evidence. Retain the number
    with scoped evidence. Listed water and volume=1000 metadata do not independently
    establish a measured final volume.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\":
    29.7327,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Agar                                       10.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject":
    "Agar maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "Existing attached provider quantity
    claims", "interpretation": "Both maintained owners already attach exact literal
    API excerpts and the current matching response digest for this quantity. Credit
    that existing authentication. It covers provider-declared g_l and exact source
    ingredient identity, not a measured final volume, the separate KOMODO catalogue
    bytes or a different blood-agar variant.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\":
    29.7327,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Agar                                       10.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject":
    "Distilled water", "local_fields": [], "decision": "add", "stage": "Absolute main
    solvent input", "interpretation": "The source lists 1000 ml distilled water. Preserve
    this missing absolute input without inferring make-up to a final 1 L or introducing
    a new dilution.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715", "source_raw_sha256":
    "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "source_text_sha256":
    "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e", "accessed_at":
    "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Distilled
    water                          1000.0   ml", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q10", "subject": "Retained pH range", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLUMBIA_AGAR.yaml", "field_path": "ph_range",
    "original": {"min": 7.0, "max": 7.2}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml",
    "field_path": "ph_range", "original": {"min": 7.0, "max": 7.2}}, {"record_path":
    "data/normalized_yaml/bacterial/columbia_agar.yaml", "field_path": "ph_range",
    "original": {"min": 7.0, "max": 7.2}}], "decision": "evidence_only", "stage":
    "Main preparation pH", "interpretation": "The existing structured 7.0 to 7.2 range
    agrees with the primary and API preparation. It is not an organism-growth optimum
    claim. Attach new root evidence scoped to the range.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 7.0 - 7.2.\"\n                    }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Adjust pH
    to 7.0 - 7.2.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "Direct DSM preparation", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/columbia_agar.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0
    - 7.2."}], "decision": "evidence_only", "stage": "Main pH adjustment", "interpretation":
    "The direct DSM owner correctly retains the pH-adjustment step. The target and
    KOMODO owner omit this preparation context; preserve the correct existing step
    and restore it only within the exact source branch.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api715", "reference": "https://mediadive.dsmz.de/rest/medium/715",
    "source_raw_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "source_text_sha256": "63db7aeb0f279ecc568b09c0bc243525a40a1876458e349c3ebe6a5c746ba24e",
    "accessed_at": "2026-10-28T11:31:04.373049Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 7.0 - 7.2.\"\n                    }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz715",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium715.pdf",
    "source_raw_sha256": "0f51a73fc11c2b65ca96c1dccf0fd9a81a86184881ad964b0ea52a2e51c0ec0b",
    "source_text_sha256": "8cb5040d433987566530f008dcfe150068e0221e997f2a171d9269363b8bfd37",
    "accessed_at": "2026-10-28T11:31:04.497933Z", "exact_source_quote": "Adjust pH
    to 7.0 - 7.2.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q12", "subject": "Linked medium687 comparison", "local_fields": [], "decision":
    "unsupported", "stage": "Identity comparison only; no dose transfer", "interpretation":
    "The local KG link identifies Columbia Blood Agar 687, whose current API includes
    a distinct blood-agar base and blood addition. Its base agar row is 15 rather
    than the selected source 10. This demonstrates non-equivalence; no 687 ingredient,
    processing setting or product composition transfers to 715.", "sources": [{"locator":
    "$.data.medium", "source_key": "api687", "reference": "https://mediadive.dsmz.de/rest/medium/687",
    "source_raw_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9",
    "source_text_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9",
    "accessed_at": "2026-10-28T11:31:04.031183Z", "exact_source_quote": "{\n            \"id\":
    687,\n            \"name\": \"COLUMBIA BLOOD AGAR\",\n            \"complex_medium\":
    \"yes\",\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf\"\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api687", "reference": "https://mediadive.dsmz.de/rest/medium/687",
    "source_raw_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9",
    "source_text_sha256": "e76ca8696e810ff753227180f4bea54cb34f8e19ff89e080ce258617e4cc3bc9",
    "accessed_at": "2026-10-28T11:31:04.031183Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch065/record06/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/COLUMBIA_AGAR.yaml: primary 3/4, secondary 3/4;
    data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml: primary 3/4, secondary
    3/4; data/normalized_yaml/bacterial/columbia_agar.yaml: primary 3/4, secondary
    3/4. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI term is joined to
    its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech
    mentions occur across the complete selected documents, with exact locators in
    the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:006352
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
  - CultureMech:006352
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
  - CultureMech:006352
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006352-kg-link-points-to-distinct-blood-agar
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The KG cross-reference identifies a different medium
  description: All selected layers link to mediadive.medium:687 Columbia Blood Agar,
    while source 715 is Columbia Agar with a different formulation. The current matcher
    uses CHEBI/FOODON identity sets and ignores amounts, preparation and ungrounded
    peptone, so a set match is not proof of source equivalence.
  target_ids:
  - CultureMech:006352
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - local0
  - local1
  - local2
  - dsmz715
  - api715
  - api687
  rule_id: review-yaml-record/exact-cross-reference-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-006352-generated-preparation-evidence-and-water-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated content omits supported owner evidence and source context
  description: Both maintained owners already contain four authenticated quantity
    claims, but the target contains none. The direct DSM owner retains pH preparation
    while the target and KOMODO owner omit it; all selected layers omit absolute source
    water. Current conservative merging retains scientific fields and rejects incompatible
    projections, so old generated omissions are not attributed to an ingredient-only
    current merger.
  target_ids:
  - CultureMech:006352
  field_paths:
  - ingredients[*].evidence
  - preparation_steps
  - evidence
  evidence_ids:
  - local0
  - local1
  - local2
  - dsmz715
  - api715
  - attached-auth
  rule_id: review-yaml-record/generated-evidence-and-preparation-staleness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-006352-malformed-original-komodo-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO import history contains an unparseable timestamp
  description: The KOMODO owner has literal .fZ in its original import event and a
    later enrichment timestamp without timezone. The current strftime format contains
    unsupported %f, consistent with the observed defect but not proof of historical
    execution. The exact API quantity authentication does not reconstruct those event
    times.
  target_ids:
  - CultureMech:006352
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml::curation_history[1].timestamp
  evidence_ids:
  - local1
  rule_id: review-yaml-record/history-timestamp-traceability
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Reconcile or remove the unsupported equivalent-medium link using exact
    source identities and formulation-aware comparison. Preserve correct 715 quantities
    and do not import blood or different base composition from 687. Review matcher
    scope before regenerating downstream linked content.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006352
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
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
  description: Retain all eight existing owner quantity claims and the correct DSM
    preparation. Repair the missing water and KOMODO preparation context with exact
    source evidence, reconcile source ownership explicitly, and regenerate through
    the present conservative guard. Do not invent autoclave parameters or treat the
    generic source recipe as growth evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006352
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
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
  description: Preserve original event bytes and append verified corrective context
    with the actual current curation date. Fix timestamp generation for future writes;
    do not replace historical timestamps with guessed dates.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006352
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/columbia_agar.yaml
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
- Exact current KOMODO 715 and the historical catalogue endpoint returned 403; the
  direct primary 715 and current matching API authenticate formulation amounts but
  not the separately cited historical catalogue bytes or access time.
- Listed water and provider volume metadata are not a measured final-volume instruction.
  No687 ingredient, processing condition, manufacturer blend or organism-growth claim
  transfers into 715.
- No ingredient values, records, original evidence or historical events were changed.
  Generic mixture and polymer labels are not treated as pure compounds with exact
  formulation stoichiometry.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
