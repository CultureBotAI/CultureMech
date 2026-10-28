# Scientific review of cytophaga_medium

- Review: 20261028T132431Z-cytophaga-medium-batch068
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:44.582792Z
- Finished UTC: 2026-10-28T13:24:31.404773Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM669 basal amounts and supplied forms are supported, but optional agar conflicts with the provider-normalized rate, tap water has the wrong unit, and the generated record lacks retained owner evidence and preparation. Exact KOMODO identity access remains incomplete.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch068 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006258 | data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml | generated | cytophaga_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006258 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:006258 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:006258 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:006258 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact base identity and conditional physical state

identity: concern. Targets: CultureMech:006258.

The current official source identifies DSM669 CYTOPHAGA MEDIUM. The maintained KOMODO identity claim maps 669 to that source, but current exact KOMODO routes and catalogue fail 403. SOLID_AGAR correctly identifies the selected solid branch; the generic record also needs the source optionality and liquid-alternative context. No species-specific growth assertion follows from the generic title.

### Existing source claims and generated freshness

evidence: concern. Targets: CultureMech:006258.

The six independently authenticated amount claims in each maintained owner are credited. The target carries none of those twelve claims or their references. The DSM owner retains its pH procedure. Current conservative merge code rejects incompatible owner formulations/notes and preserves scoped evidence; the observed target is stale generated content, not proof that the current merger discards evidence.

### Exact chemical forms

grounding: supported. Targets: CultureMech:006258.

All seven asserted ontology identities and labels resolve. Ammonium chloride, magnesium sulfate heptahydrate, dipotassium hydrogen phosphate, iron trichloride, sodium chloride, agar and water correspond at the stated granularity. Agar has no single molecular formula; yeast extract stays a complex mixture. Tap-water mineral content is not claimed by generic water.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:006258.

All five exact historical reports were fully read. Current API669 bytes authenticate twenty historical quoted objects and the two six-claim owner sets; the historical catalogue response remains unavailable. Old no-source-check reviews are triage only. The current primary final-volume header and agar amount are assessed directly, not inferred from those reports. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:006258.

All 24 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006258", "selected_concentration_field_count": 24, "selected_concentration_fields_covered": 24, "decisions": [{"decision_id": "q1", "subject": "Yeast extract in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation", "interpretation": "The unchanged local value matches the explicit provider g_l and current primary batch amount. The current PDF explicitly states final volume 1000 ml; this denominator is source-declared rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture and salt molarities are not imported. The generated field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Yeast extract                                          10.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Yeast extract in the two maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation": "Both existing ingredient excerpts are independently literal matches to the current API raw bytes and their cited SHA256. Credit those two owner claims without treating the separate KOMODO catalogue mapping as newly authenticated. Current primary and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Yeast extract                                          10.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "NH4Cl in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation", "interpretation": "The unchanged local value matches the explicit provider g_l and current primary batch amount. The current PDF explicitly states final volume 1000 ml; this denominator is source-declared rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture and salt molarities are not imported. The generated field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NH4Cl                                                   1.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "NH4Cl in the two maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation": "Both existing ingredient excerpts are independently literal matches to the current API raw bytes and their cited SHA256. Credit those two owner claims without treating the separate KOMODO catalogue mapping as newly authenticated. Current primary and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NH4Cl                                                   1.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "MgSO4 x 7 H2O in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation", "interpretation": "The unchanged local value matches the explicit provider g_l and current primary batch amount. The current PDF explicitly states final volume 1000 ml; this denominator is source-declared rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture and salt molarities are not imported. The generated field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "MgSO4 x 7 H2O                                           1.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "MgSO4 x 7 H2O in the two maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation": "Both existing ingredient excerpts are independently literal matches to the current API raw bytes and their cited SHA256. Credit those two owner claims without treating the separate KOMODO catalogue mapping as newly authenticated. Current primary and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "MgSO4 x 7 H2O                                           1.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "K2HPO4 in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation", "interpretation": "The unchanged local value matches the explicit provider g_l and current primary batch amount. The current PDF explicitly states final volume 1000 ml; this denominator is source-declared rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture and salt molarities are not imported. The generated field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "K2HPO4                                                  0.20         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "K2HPO4 in the two maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation": "Both existing ingredient excerpts are independently literal matches to the current API raw bytes and their cited SHA256. Credit those two owner claims without treating the separate KOMODO catalogue mapping as newly authenticated. Current primary and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "K2HPO4                                                  0.20         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "FeCl 3 in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation", "interpretation": "The unchanged local value matches the explicit provider g_l and current primary batch amount. The current PDF explicitly states final volume 1000 ml; this denominator is source-declared rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture and salt molarities are not imported. The generated field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeCl3\",\n                        \"compound_id\": 403,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00616523,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "FeCl3                                                   1.00        mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "FeCl 3 in the two maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation": "Both existing ingredient excerpts are independently literal matches to the current API raw bytes and their cited SHA256. Credit those two owner claims without treating the separate KOMODO catalogue mapping as newly authenticated. Current primary and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeCl3\",\n                        \"compound_id\": 403,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00616523,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "FeCl3                                                   1.00        mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "NaCl in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation", "interpretation": "The unchanged local value matches the explicit provider g_l and current primary batch amount. The current PDF explicitly states final volume 1000 ml; this denominator is source-declared rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture and salt molarities are not imported. The generated field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 342.231,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NaCl                                                   20.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "NaCl in the two maintained owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation": "Both existing ingredient excerpts are independently literal matches to the current API raw bytes and their cited SHA256. Credit those two owner claims without treating the separate KOMODO catalogue mapping as newly authenticated. Current primary and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 342.231,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NaCl                                                   20.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Optional agar", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Conditional solid formulation", "interpretation": "Every local layer has 3 g/L without optionality. Current PDF gives optional 15 g at explicit final 1000 ml, hence 15 g/L when selected; the API itself says amount 15 g but g_l 3, an internal provider conflict. Preserve the discrepancy and the alternative liquid formulation. Do not multiply the source amount by an invented dilution or regard agar mmol_l as meaningful for this mixture.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 8.91981,\n                        \"optional\": 1\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Agar (optional)                                        15.00         g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "Tap water volume", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Main preparation solvent", "interpretation": "The source specifies 1000 ml tap water, not 1000 g/L. Preserve a volumetric preparation input and the explicitly stated final 1000 ml separately. No density or mass concentration is supplied. Generic CHEBI water does not remove the source tap-water qualifier.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 14-14", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Tap water                                            1000.00        ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume: 1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "pH and existing DSM preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ph_value", "original": 7.5}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path": "ph_value", "original": 7.5}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "ph_value", "original": 7.5}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.5."}], "decision": "evidence_only", "stage": "Main preparation", "interpretation": "All pH7.5 assertions and the DSM owner ADJUST_PH description are supported. Target and KOMODO owner omit that explicit step; neither the scalar nor the omitted step establishes other cultivation conditions.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "1. Adjust pH to 7.5.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "Liquid handling source-only context", "local_fields": [], "decision": "add", "stage": "Liquid variant only", "interpretation": "Preserve the source screw-capped tubes/no-shaking context only for liquid cultures. This text does not prove anaerobiosis; retained Aerobic:No in KOMODO notes remains unauthenticated categorical metadata.", "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"step\": \"Note: for liquid cultures, use screw capped tubes and no shaking.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 17-17", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "2. Note: for liquid cultures, use screw capped tubes and no shaking.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch068/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:006258.

data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml: primary 7/8, secondary 7/8; data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml: primary 7/8, secondary 7/8; data/normalized_yaml/bacterial/cytophaga_medium.yaml: primary 7/8, secondary 7/8. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:006258.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:006258.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Agar rate and optionality disagree with the current primary

major / open / confirmed; issue key: culturemech-006258-optional-agar-provider-conflict.

The three local 3 g/L agar fields follow an inconsistent API g_l 3 even though its batch amount is 15 g. The current primary explicitly prints optional 15 g at final 1000 ml. SOLID_AGAR is valid for the selected solid branch. The generic record lacks the source optionality and liquid-alternative context.

### f2: Tap-water volume is represented as a mass concentration

major / open / confirmed; issue key: culturemech-006258-water-mass-volume-confusion.

All selected layers encode 1000 G_PER_L for a 1000 ml source solvent input. No density conversion supports that mass assertion.

### f3: Generated target omits authenticated claims and preparation context

major / open / confirmed; issue key: culturemech-006258-generated-evidence-and-preparation-loss.

The generated target lacks the twelve independently supported owner ingredient claims and references, and omits the DSM owner pH step. The source liquid handling context is absent across selected layers. Current source-equivalence guards must be respected when updating the generated record.

### f4: Import time and categorical aeration need bounded provenance context

minor / open / confirmed; issue key: culturemech-006258-unverified-import-provenance.

KOMODO-derived target and owner retain literal 2026-01-27T01:15:03.fZ and a timezone-less resolver event. Aerobic:No is not established by the current source instruction to avoid shaking. Existing SOURCE_DUPLICATE annotations and old catalogue digest are preserved leads, not fresh authentication.

## Recommended Actions And Acceptance Checks

### action1

Correct only the documented solid branch to the primary 15 g/L basis, retain its valid SOLID_AGAR classification, and represent source agar optionality/liquid-alternative context explicitly. Retain the provider contradiction as scoped evidence; do not silently repair the upstream API.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Replace the unsupported water mass assertion with an appropriately scoped volumetric preparation record. Keep the stated final volume separate and preserve tap-water identity.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Retain and propagate the verified owner claims at their existing ingredient scope. Attach new procedure/conditional-state evidence at the enclosing recipe with exact field paths. Preserve the already correct DSM pH step; resolve owner differences before regeneration.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Preserve old event bytes. Correct future timestamp generation and append verified provenance with the actual current curation date; do not invent historical instants. Qualify the aeration and identity claims until exact source evidence resolves them.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/cytophaga_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch068/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch068/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch068/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch068/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm669 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api669 | https://mediadive.dsmz.de/rest/medium/669; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| komodo669 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=669; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodoList | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30808 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30808; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30808 = iron trichloride; definition []; formula ['Cl3Fe']; mass ['162.204']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| komodoOriginalList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| grounding | REVIEW_WORK/batch068/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cytophaga_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api669 raw bytes exactly match the cited historical SHA, and 10 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api669 raw bytes exactly match the cited historical SHA, and 10 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cytophaga_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYTOPHAGA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch068/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer26 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer27 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer28 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer29 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer30 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer31 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer32 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer33 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| quantity-inventory | REVIEW_WORK/batch068/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Current exact KOMODO MediaInfo 669 and both catalogue routes returned 403; their original bodies/times are retained. The historical catalogue SHA is not authenticated by a quoted row alone.
- Current PDF final 1000 ml is explicit; other sources or variants must establish their own final-volume basis. No unsupported mass density or agar molarity is inferred.
- Current writer bodies describe present behavior only. Zero native reference checks do not certify scientific sources.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T132431Z-cytophaga-medium-batch068
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of cytophaga_medium
started_at: '2026-10-28T13:11:44.582792Z'
finished_at: '2026-10-28T13:24:31.404773Z'
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
summary: DSM669 basal amounts and supplied forms are supported, but optional agar
  conflicts with the provider-normalized rate, tap water has the wrong unit, and the
  generated record lacks retained owner evidence and preparation. Exact KOMODO identity
  access remains incomplete.
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
  - path: data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml
    sha256: d32d066456477fe7b918e34f926d3533dfdb74c146ee36d6c90f70fec11564b8
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    sha256: f68fd278864b4a5432f210b588ab0382a296e491cd589e665896d225c3d47c22
    role: context
  - path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
    sha256: 15656b6a5a17c7684a5e23d1e7995b077498203a95cfd36cdc73cae20ec42d77
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml.md
    sha256: 14f8814c9086cc92711d43290e9c16e11141a7b8905db70352dd99d8f8be0e57
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cytophaga_medium.yaml.md
    sha256: 04abd793b3a4f904b249cff9cfc902f492a1c9b0d47887f2a72c5df840ac7a60
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYTOPHAGA_MEDIUM.md
    sha256: 526e57198cd0ed3550f8cf545b3ac85c04702cc8b43e6eddc4fea83ba3216115
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.md
    sha256: 5ffad62de02a07288588d7ee52e5382900efad7ca5653aef51d5517cc563339c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cytophaga_medium.md
    sha256: 53d89f51689b09ec451fb07a3b89c58610c3d485aa3b5822d8493e7349ef23d9
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
  selection: Authoritative batch068 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006258
targets:
- target_id: CultureMech:006258
  path: data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml
  label: cytophaga_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006258
  command: just validate-schema data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006258
  command: just validate-strict data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch068/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006258
  command: just validate-terms data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:006258
  command: just validate-references data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T13:16:50.637482Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: d32d066456477fe7b918e34f926d3533dfdb74c146ee36d6c90f70fec11564b8
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T13:16:50.637628Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: f68fd278864b4a5432f210b588ab0382a296e491cd589e665896d225c3d47c22
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/cytophaga_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T13:16:50.637652Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 15656b6a5a17c7684a5e23d1e7995b077498203a95cfd36cdc73cae20ec42d77
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:45.615947Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: a5baecaca1cdd4fba41125321c7b2d901f5de9dd70e77aa93912dc6ec31a0d10
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:46.591999Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 8500e47e4e27aee4a5327154ce61781f68dcbaf0b6423928b29287ed10548aa5
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:47.619984Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 57e8dca6d704f8994814f37377105c258a9844d52aad25efe58ba7f4e13d1fb8
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch068/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:48.275686Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 5d7ceec28cb54926d19c81de7042bd842cf4d9815ca6e2f0d7f9bbc81b441a47
- evidence_id: dsm669
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:11:57.298639Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7
- evidence_id: api669
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/669
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:11:57.246725Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63
- evidence_id: komodo669
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=669
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:11:57.186953Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: de0c95187aaac5221f657ca7242f6040b8e2f7620542df96083f1c7d645f5700
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:11:57.086573Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: a4222a7d72844a59444e5c0882e256f454bb4046cde7ce11d21196b15c796600
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:57.074840Z'
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
  accessed_at: '2026-10-28T13:11:56.862457Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.897259Z'
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
  accessed_at: '2026-10-28T13:11:56.713703Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi30808
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30808
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:56.492089Z'
  support: supports
  summary: OLS current exact CHEBI:30808 = iron trichloride; definition []; formula
    ['Cl3Fe']; mass ['162.204']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 3053606ef0cc9275ce2a4d374db1f6d2f61ceb59c93b3c69c5e0c437c121060c
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:56.475649Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.076159Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: komodoOriginalList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:14:47.755190Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 2938e9f1284180959e33ab1718d0793a72ff6e4cdb8108c34dcd14e69446de5c
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch068/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T13:16:50.641350Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 200e9b0a3e253a4545c37ccd6eab174229c0833827983a55ea8af3801647c075
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cytophaga_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:16:50.642003Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api669 raw bytes exactly match the cited historical SHA, and 10 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 04abd793b3a4f904b249cff9cfc902f492a1c9b0d47887f2a72c5df840ac7a60
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:16:50.642027Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api669 raw bytes exactly match the cited historical SHA, and 10 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 14f8814c9086cc92711d43290e9c16e11141a7b8905db70352dd99d8f8be0e57
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cytophaga_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:16:50.642045Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 53d89f51689b09ec451fb07a3b89c58610c3d485aa3b5822d8493e7349ef23d9
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:16:50.642063Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 5ffad62de02a07288588d7ee52e5382900efad7ca5653aef51d5517cc563339c
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYTOPHAGA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:16:50.642080Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 526e57198cd0ed3550f8cf545b3ac85c04702cc8b43e6eddc4fea83ba3216115
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch068/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T13:16:50.642099Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 004cbd09478c7597bb46f2028e9388fa5ba03a0872c616b0f06def24d17a07b4
- evidence_id: writer26
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T13:16:50.642154Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer27
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T13:16:50.642198Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer28
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T13:16:50.642220Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer29
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T13:16:50.642249Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer30
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T13:16:50.642274Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer31
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T13:16:50.642293Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer32
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T13:16:50.642316Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer33
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T13:16:50.642338Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch068/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T13:16:50.650998Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: f2c52c2767955e5e238ea45023698b0eb5b80cf85d66f024cf11d7b84e2eb566
assessments:
- assessment_id: a1
  area: identity
  topic: Exact base identity and conditional physical state
  outcome: concern
  summary: The current official source identifies DSM669 CYTOPHAGA MEDIUM. The maintained
    KOMODO identity claim maps 669 to that source, but current exact KOMODO routes
    and catalogue fail 403. SOLID_AGAR correctly identifies the selected solid branch;
    the generic record also needs the source optionality and liquid-alternative context.
    No species-specific growth assertion follows from the generic title.
  target_ids:
  - CultureMech:006258
  evidence_ids:
  - dsm669
  - api669
  - komodo669
  - komodoList
  - komodoOriginalList
- assessment_id: a2
  area: evidence
  topic: Existing source claims and generated freshness
  outcome: concern
  summary: The six independently authenticated amount claims in each maintained owner
    are credited. The target carries none of those twelve claims or their references.
    The DSM owner retains its pH procedure. Current conservative merge code rejects
    incompatible owner formulations/notes and preserves scoped evidence; the observed
    target is stale generated content, not proof that the current merger discards
    evidence.
  target_ids:
  - CultureMech:006258
  evidence_ids:
  - local0
  - local1
  - local2
  - history-auth
- assessment_id: a3
  area: grounding
  topic: Exact chemical forms
  outcome: supported
  summary: All seven asserted ontology identities and labels resolve. Ammonium chloride,
    magnesium sulfate heptahydrate, dipotassium hydrogen phosphate, iron trichloride,
    sodium chloride, agar and water correspond at the stated granularity. Agar has
    no single molecular formula; yeast extract stays a complex mixture. Tap-water
    mineral content is not claimed by generic water.
  target_ids:
  - CultureMech:006258
  evidence_ids:
  - grounding
  - chebi2509
  - chebi31795
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: All five exact historical reports were fully read. Current API669 bytes
    authenticate twenty historical quoted objects and the two six-claim owner sets;
    the historical catalogue response remains unavailable. Old no-source-check reviews
    are triage only. The current primary final-volume header and agar amount are assessed
    directly, not inferred from those reports. Current conservative merging preserves
    scientific fields and rejects incompatible formulations. Inspected writer behavior
    is described separately by exact file and function; it does not prove historical
    execution.
  target_ids:
  - CultureMech:006258
  evidence_ids:
  - history-auth
  - writer26
  - writer27
  - writer28
  - writer29
  - writer30
  - writer31
  - writer32
  - writer33
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 24 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:006258
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006258",
    "selected_concentration_field_count": 24, "selected_concentration_fields_covered":
    24, "decisions": [{"decision_id": "q1", "subject": "Yeast extract in generated
    target", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM669 main formulation",
    "interpretation": "The unchanged local value matches the explicit provider g_l
    and current primary batch amount. The current PDF explicitly states final volume
    1000 ml; this denominator is source-declared rather than inferred from listed
    water. FeCl 3 1 mg equals 0.001 g. Preserve the source supplied form; mixture
    and salt molarities are not imported. The generated field has no attached evidence.",
    "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api669",
    "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256":
    "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256":
    "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at":
    "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 7-7", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Yeast extract                                          10.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q2", "subject": "Yeast extract in the two maintained owners", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation":
    "Both existing ingredient excerpts are independently literal matches to the current
    API raw bytes and their cited SHA256. Credit those two owner claims without treating
    the separate KOMODO catalogue mapping as newly authenticated. Current primary
    and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 7-7", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Yeast extract                                          10.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q3", "subject": "NH4Cl in generated target", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "DSM669 main formulation", "interpretation": "The unchanged local value
    matches the explicit provider g_l and current primary batch amount. The current
    PDF explicitly states final volume 1000 ml; this denominator is source-declared
    rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the
    source supplied form; mixture and salt molarities are not imported. The generated
    field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    18.6951,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NH4Cl                                                   1.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q4", "subject": "NH4Cl in the two maintained owners", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "DSM669 main formulation", "interpretation":
    "Both existing ingredient excerpts are independently literal matches to the current
    API raw bytes and their cited SHA256. Credit those two owner claims without treating
    the separate KOMODO catalogue mapping as newly authenticated. Current primary
    and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    18.6951,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NH4Cl                                                   1.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q5", "subject": "MgSO4 x 7 H2O in generated target", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[2].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "DSM669 main formulation", "interpretation": "The unchanged local value
    matches the explicit provider g_l and current primary batch amount. The current
    PDF explicitly states final volume 1000 ml; this denominator is source-declared
    rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the
    source supplied form; mixture and salt molarities are not imported. The generated
    field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.05719,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "MgSO4 x 7
    H2O                                           1.00         g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q6", "subject": "MgSO4 x 7 H2O in the two maintained owners", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "DSM669 main formulation", "interpretation":
    "Both existing ingredient excerpts are independently literal matches to the current
    API raw bytes and their cited SHA256. Credit those two owner claims without treating
    the separate KOMODO catalogue mapping as newly authenticated. Current primary
    and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    4.05719,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "MgSO4 x 7
    H2O                                           1.00         g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 4-4", "source_key":
    "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q7", "subject": "K2HPO4 in generated target", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[3].concentration",
    "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "DSM669 main formulation", "interpretation": "The unchanged local value
    matches the explicit provider g_l and current primary batch amount. The current
    PDF explicitly states final volume 1000 ml; this denominator is source-declared
    rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the
    source supplied form; mixture and salt molarities are not imported. The generated
    field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.14826,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "K2HPO4                                                  0.20         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q8", "subject": "K2HPO4 in the two maintained owners", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "DSM669 main formulation", "interpretation":
    "Both existing ingredient excerpts are independently literal matches to the current
    API raw bytes and their cited SHA256. Credit those two owner claims without treating
    the separate KOMODO catalogue mapping as newly authenticated. Current primary
    and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.14826,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "K2HPO4                                                  0.20         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q9", "subject": "FeCl 3 in generated target", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "DSM669 main formulation", "interpretation": "The unchanged local value
    matches the explicit provider g_l and current primary batch amount. The current
    PDF explicitly states final volume 1000 ml; this denominator is source-declared
    rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the
    source supplied form; mixture and salt molarities are not imported. The generated
    field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeCl3\",\n                        \"compound_id\":
    403,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00616523,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    11-11", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "FeCl3                                                   1.00        mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q10", "subject": "FeCl 3 in the two maintained owners", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "DSM669 main formulation", "interpretation":
    "Both existing ingredient excerpts are independently literal matches to the current
    API raw bytes and their cited SHA256. Credit those two owner claims without treating
    the separate KOMODO catalogue mapping as newly authenticated. Current primary
    and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeCl3\",\n                        \"compound_id\":
    403,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00616523,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    11-11", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "FeCl3                                                   1.00        mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "NaCl in generated target", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[5].concentration",
    "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "evidence_only",
    "stage": "DSM669 main formulation", "interpretation": "The unchanged local value
    matches the explicit provider g_l and current primary batch amount. The current
    PDF explicitly states final volume 1000 ml; this denominator is source-declared
    rather than inferred from listed water. FeCl 3 1 mg equals 0.001 g. Preserve the
    source supplied form; mixture and salt molarities are not imported. The generated
    field has no attached evidence.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    342.231,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NaCl                                                   20.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q12", "subject": "NaCl in the two maintained owners", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "20", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "DSM669 main formulation", "interpretation":
    "Both existing ingredient excerpts are independently literal matches to the current
    API raw bytes and their cited SHA256. Credit those two owner claims without treating
    the separate KOMODO catalogue mapping as newly authenticated. Current primary
    and provider agree for this field.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    342.231,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "NaCl                                                   20.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "Optional agar", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Conditional solid formulation",
    "interpretation": "Every local layer has 3 g/L without optionality. Current PDF
    gives optional 15 g at explicit final 1000 ml, hence 15 g/L when selected; the
    API itself says amount 15 g but g_l 3, an internal provider conflict. Preserve
    the discrepancy and the alternative liquid formulation. Do not multiply the source
    amount by an invented dilution or regard agar mmol_l as meaningful for this mixture.",
    "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api669",
    "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256":
    "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256":
    "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at":
    "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    8.91981,\n                        \"optional\": 1\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Agar (optional)                                        15.00         g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q14", "subject": "Tap water volume", "local_fields": [{"record_path": "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Main preparation solvent", "interpretation":
    "The source specifies 1000 ml tap water, not 1000 g/L. Preserve a volumetric preparation
    input and the explicitly stated final 1000 ml separately. No density or mass concentration
    is supplied. Generic CHEBI water does not remove the source tap-water qualifier.",
    "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api669",
    "reference": "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256":
    "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "source_text_sha256":
    "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63", "accessed_at":
    "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\":
    322,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 14-14", "source_key": "dsm669",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Tap water                                            1000.00        ml",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 4-4", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "Final volume:
    1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q15", "subject": "pH and existing DSM preparation", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml", "field_path": "ph_value", "original":
    7.5}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml",
    "field_path": "ph_value", "original": 7.5}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml",
    "field_path": "ph_value", "original": 7.5}, {"record_path": "data/normalized_yaml/bacterial/cytophaga_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.5."}],
    "decision": "evidence_only", "stage": "Main preparation", "interpretation": "All
    pH7.5 assertions and the DSM owner ADJUST_PH description are supported. Target
    and KOMODO owner omit that explicit step; neither the scalar nor the omitted step
    establishes other cultivation conditions.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api669", "reference": "https://mediadive.dsmz.de/rest/medium/669",
    "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 7.5.\"\n                    }", "quote_representation": "raw JSON
    object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsm669", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf", "source_raw_sha256":
    "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7", "source_text_sha256":
    "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6", "accessed_at":
    "2026-10-28T13:11:57.298639Z", "exact_source_quote": "1. Adjust pH to 7.5.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q16", "subject": "Liquid handling
    source-only context", "local_fields": [], "decision": "add", "stage": "Liquid
    variant only", "interpretation": "Preserve the source screw-capped tubes/no-shaking
    context only for liquid cultures. This text does not prove anaerobiosis; retained
    Aerobic:No in KOMODO notes remains unauthenticated categorical metadata.", "sources":
    [{"locator": "$.data.solutions[0].steps[1]", "source_key": "api669", "reference":
    "https://mediadive.dsmz.de/rest/medium/669", "source_raw_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "source_text_sha256": "e236b060ffcacd452c83239beaf5d13dacd8bf9df29e57a59a66b8d756a86e63",
    "accessed_at": "2026-10-28T13:11:57.246725Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: for liquid cultures, use screw capped tubes and no shaking.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    17-17", "source_key": "dsm669", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium669.pdf",
    "source_raw_sha256": "6455349e1946d7e9b797a32087a491750f783452c036186051c1449acfb314b7",
    "source_text_sha256": "5fd66adb77c6d206368fb68cb08a18e480f81b3d313f604f8fe91a10b9f032a6",
    "accessed_at": "2026-10-28T13:11:57.298639Z", "exact_source_quote": "2. Note:
    for liquid cultures, use screw capped tubes and no shaking.", "quote_representation":
    "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch068/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/CYTOPHAGA_MEDIUM.yaml: primary 7/8, secondary 7/8;
    data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml: primary 7/8,
    secondary 7/8; data/normalized_yaml/bacterial/cytophaga_medium.yaml: primary 7/8,
    secondary 7/8. These are ingredient-instance linkage fractions, not accuracy scores.
    Solution terms are audited separately. Every actually asserted CHEBI term is joined
    to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech
    mentions occur across the complete selected documents, with exact locators in
    the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:006258
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:006258
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
  - CultureMech:006258
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006258-optional-agar-provider-conflict
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Agar rate and optionality disagree with the current primary
  description: The three local 3 g/L agar fields follow an inconsistent API g_l 3
    even though its batch amount is 15 g. The current primary explicitly prints optional
    15 g at final 1000 ml. SOLID_AGAR is valid for the selected solid branch. The
    generic record lacks the source optionality and liquid-alternative context.
  target_ids:
  - CultureMech:006258
  field_paths:
  - ingredients[6].concentration
  - physical_state
  evidence_ids:
  - dsm669
  - api669
  rule_id: review-yaml-record/conditional-formulation-and-provider-conflict
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-006258-water-mass-volume-confusion
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Tap-water volume is represented as a mass concentration
  description: All selected layers encode 1000 G_PER_L for a 1000 ml source solvent
    input. No density conversion supports that mass assertion.
  target_ids:
  - CultureMech:006258
  field_paths:
  - ingredients[7].concentration
  evidence_ids:
  - dsm669
  - api669
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-006258-generated-evidence-and-preparation-loss
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits authenticated claims and preparation context
  description: The generated target lacks the twelve independently supported owner
    ingredient claims and references, and omits the DSM owner pH step. The source
    liquid handling context is absent across selected layers. Current source-equivalence
    guards must be respected when updating the generated record.
  target_ids:
  - CultureMech:006258
  field_paths:
  - ingredients[0].evidence
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - ingredients[5].evidence
  - references
  - preparation_steps
  - evidence
  evidence_ids:
  - local0
  - local1
  - local2
  - dsm669
  - history-auth
  rule_id: review-yaml-record/evidence-and-preparation-freshness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-006258-unverified-import-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Import time and categorical aeration need bounded provenance context
  description: KOMODO-derived target and owner retain literal 2026-01-27T01:15:03.fZ
    and a timezone-less resolver event. Aerobic:No is not established by the current
    source instruction to avoid shaking. Existing SOURCE_DUPLICATE annotations and
    old catalogue digest are preserved leads, not fresh authentication.
  target_ids:
  - CultureMech:006258
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  - notes
  - parent_media
  - variant_modifications
  - data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml::curation_history[0].timestamp
  evidence_ids:
  - local0
  - local1
  - history-auth
  - komodo669
  rule_id: review-yaml-record/append-only-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Correct only the documented solid branch to the primary 15 g/L basis,
    retain its valid SOLID_AGAR classification, and represent source agar optionality/liquid-alternative
    context explicitly. Retain the provider contradiction as scoped evidence; do not
    silently repair the upstream API.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006258
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
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
  description: Replace the unsupported water mass assertion with an appropriately
    scoped volumetric preparation record. Keep the stated final volume separate and
    preserve tap-water identity.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006258
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
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
  description: Retain and propagate the verified owner claims at their existing ingredient
    scope. Attach new procedure/conditional-state evidence at the enclosing recipe
    with exact field paths. Preserve the already correct DSM pH step; resolve owner
    differences before regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006258
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
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
  description: Preserve old event bytes. Correct future timestamp generation and append
    verified provenance with the actual current curation date; do not invent historical
    instants. Qualify the aeration and identity claims until exact source evidence
    resolves them.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006258
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cytophaga_medium.yaml
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
- Current exact KOMODO MediaInfo 669 and both catalogue routes returned 403; their
  original bodies/times are retained. The historical catalogue SHA is not authenticated
  by a quoted row alone.
- Current PDF final 1000 ml is explicit; other sources or variants must establish
  their own final-volume basis. No unsupported mass density or agar molarity is inferred.
- Current writer bodies describe present behavior only. Zero native reference checks
  do not certify scientific sources.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
