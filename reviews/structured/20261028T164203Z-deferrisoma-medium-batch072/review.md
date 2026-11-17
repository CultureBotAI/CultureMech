# Scientific review of deferrisoma_medium

- Review: 20261028T164203Z-deferrisoma-medium-batch072
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T16:12:04.461342Z
- Finished UTC: 2026-10-28T16:42:03.059650Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The nine main-medium rates and generic pH are supported, but three source stocks are flattened, anoxic preparation is lost from the generated branch, and nickel hexahydrate is mapped to anhydrous nickel chloride. Preserve supported values and the DSM owner’s retained preparation while repairing stock and evidence scope.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch072 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004165 | data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml | generated | deferrisoma_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004165 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:004165 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:004165 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:004165 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Generic DSM1451 and maintained source branches

identity: supported. Targets: CultureMech:004165.

The primary title/accession and both maintained source identities align with generic DSM1451. The primary-specific DSM 103037 note is not an unconditional recipe or growth assertion. Reciprocal SOURCE_DUPLICATE relations are present, but their current scientific fields differ in retained preparation and metadata, so they are not permission to merge unequal documents.

### Retained classification and conservative current merging

consistency: concern. Targets: CultureMech:004165.

LIQUID, COMPLEX and SEMI_DEFINED are consistent with this generic yeast-containing medium. Main pH and rounded main concentrations are supported. The stale flattened stock structure and lost preparation remain scientific defects; current conservative merge equality rejects incompatible content and does not recreate this historical output.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:004165.

The September narrative and both October plans/reports are derivative assessments, not permission to adopt every proposed value. All current raw-matched API excerpts are credited; nine main rates now independently pass, whereas stock topology still fails. The exact fresh KOMODO route is 403, leaving a bounded current-source access limit. Only the two selected plan rows transfer; prior zero-source-check reports do not authenticate chemistry. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:004165.

All 93 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:004165", "selected_concentration_field_count": 93, "selected_concentration_fields_covered": 93, "decisions": [{"decision_id": "q1", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003 L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\": 2.4177,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "KH2PO4                                                 0.33       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003 L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\": 2.48988,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "(NH4)2SO4                                              0.33       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003 L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\": 4.41332,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 9-9", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "KCl                                                    0.33       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "17.9462", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "17.9462", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "17.9462", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 17.9462 G_PER_L. Source 18 g / 1.003 L = 17.94616151545363908275174477 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 18,\n                        \"unit\": \"g\",\n                        \"g_l\": 17.9462,\n                        \"mmol_l\": 307.087,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-10", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "NaCl                                                  18.00       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.329013", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003 L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\": 2.23796,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 11-11", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "CaCl2 x 2 H2O                                          0.33       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "3.98804", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "3.98804", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "3.98804", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 3.98804 G_PER_L. Source 4 g / 1.003 L = 3.988035892323030907278165503 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.98804,\n                        \"mmol_l\": 19.6162,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 12-12", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "MgCl2 x 6 H2O                                          4.00       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 0.199402 G_PER_L. Source 0.2 g / 1.003 L = 0.1994017946161515453639082752 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 13-13", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Yeast extract                                          0.20       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Ferric citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.49252", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.49252", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.49252", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 2.49252 G_PER_L. Source 2.5 g / 1.003 L = 2.492522432701894317048853440 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Ferric citrate\",\n                        \"compound_id\": 863,\n                        \"attribute\": \"Aldrich F6129\",\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.49252,\n                        \"mmol_l\": 10.1759,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 16-16", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Ferric citrate (Aldrich F6129)                         2.50       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.997009", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.997009", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.997009", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit final 1003 ml", "interpretation": "Retain 0.997009 G_PER_L. Source 1 g / 1.003 L = 0.9970089730807577268195413759 g/L, rounded to the existing precision. Both current PDF and API support this main-medium value; no attached source excerpt currently authenticates it in these YAML layers. Supplied reagent form is assessed separately.", "sources": [{"locator": "$.data.solutions[0].recipe[10]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 9.40681,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 17-17", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2CO3                                                 1.00       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The local 2.5 G_PER_L is not established as a main-medium value or an independently verified acid mass. The primary stock calls for 10 ml of 25% HCl; percent basis and density are not specified. Preserve that stock addition and the explicit SL-10 make-up volume, without assuming 25% w/v or converting it into 2.5 g.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 39-39", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "HCl (25%)                                             10.00      ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 1.5 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 1.5 g. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 40-40", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "FeCl2 x 4 H2O                                          1.50       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.07 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 70 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 41-41", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "ZnCl2                                                 70.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.1 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 100 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 42-42", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "MnCl2 x 4 H2O                                        100.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.006 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 6 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 43-43", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "H3BO3                                                  6.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.19 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 190 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 44-44", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "CoCl2 x 6 H2O                                        190.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.002 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 2 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 45-45", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "CuCl2 x 2 H2O                                          2.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.024 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 24 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 46-46", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "NiCl2 x 6 H2O                                         24.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q18", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main ingredients", "interpretation": "The numeric rate 0.036 G_PER_L matches the provider-normalized SL-10 stock composition, not the main medium. Primary supplied amount is 36 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. SL-10 has an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 47-47", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2MoO4 x 2 H2O                                       36.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "selenite-tungstate stock flattened into main ingredients", "interpretation": "The numeric rate 0.5 G_PER_L matches the provider-normalized selenite-tungstate stock composition, not the main medium. Primary supplied amount is 0.5 g. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 64-64", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "NaOH                                                       0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q20", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "selenite-tungstate stock flattened into main ingredients", "interpretation": "The numeric rate 0.003 G_PER_L matches the provider-normalized selenite-tungstate stock composition, not the main medium. Primary supplied amount is 3 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 65-65", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2SeO3 x 5 H2O                                            3.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q21", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "selenite-tungstate stock flattened into main ingredients", "interpretation": "The numeric rate 0.004 G_PER_L matches the provider-normalized selenite-tungstate stock composition, not the main medium. Primary supplied amount is 4 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 66-66", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2WO4 x 2 H2O                                             4.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q22", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.02 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 20 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 72-72", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Biotin                                                    20.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.02 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 20 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 73-73", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Folic acid                                                20.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q24", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.1 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 100 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 74-74", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Pyridoxine hydrochloride                                 100.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q25", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 50 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 75-75", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Thiamine HCl                                              50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q26", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 50 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 76-76", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Riboflavin                                                50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q27", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 50 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[5]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 77-77", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Nicotinic acid                                            50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q28", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 50 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 78-78", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Calcium D-(+)-pantothenate                                50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q29", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.001 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 1 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[7]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Vitamin B12                                                1.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 50 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[8]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 80-80", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "p-Aminobenzoic acid                                       50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q31", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches the provider-normalized Wolin vitamins (10x) stock composition, not the main medium. Primary supplied amount is 50 mg. Preserve this amount/form inside its separately identified stock, and represent that stock's 1 ml receiving addition separately. The primary lists 1000 ml water; API volume 1000 ml supports provider normalization but is not an independently measured final stock volume.", "sources": [{"locator": "$.data.solutions[3].recipe[9]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 81-81", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "(DL)-alpha-Lipoic acid                                    50.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q32", "subject": "Trace element solution SL-10 receiving addition", "local_fields": [], "decision": "add", "stage": "Main-medium stock receiving dose", "interpretation": "The selected records omit the distinct stock addition. Preserve 1 ml per explicit 1003 ml final medium. If a per-litre dose is required, 1/1.003 = 0.997008973... ml/L; a historical recommendation of exactly 1 ML_PER_L changes the printed denominator. Do not copy stock component strengths into the receiving medium.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 14-14", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Trace element solution SL-10                           1.00      ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q33", "subject": "Selenite-tungstate solution receiving addition", "local_fields": [], "decision": "add", "stage": "Main-medium stock receiving dose", "interpretation": "The selected records omit the distinct stock addition. Preserve 1 ml per explicit 1003 ml final medium. If a per-litre dose is required, 1/1.003 = 0.997008973... ml/L; a historical recommendation of exactly 1 ML_PER_L changes the printed denominator. Do not copy stock component strengths into the receiving medium.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 15-15", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Selenite-tungstate solution                            1.00      ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q34", "subject": "Wolin's vitamin solution (10x) receiving addition", "local_fields": [], "decision": "add", "stage": "Main-medium stock receiving dose", "interpretation": "The selected records omit the distinct stock addition. Preserve 1 ml per explicit 1003 ml final medium. If a per-litre dose is required, 1/1.003 = 0.997008973... ml/L; a historical recommendation of exactly 1 ML_PER_L changes the printed denominator. Do not copy stock component strengths into the receiving medium.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 18-18", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Wolin's vitamin solution (10x)                         1.00      ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q35", "subject": "Main sol. 1451 solvent/volume", "local_fields": [], "decision": "add", "stage": "Source-only solvent and denominator", "interpretation": "Main water is 1000 ml and the primary separately declares final medium 1003 ml; preserve both roles.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 19-19", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled water                                     1000.00      ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume: 1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q36", "subject": "Trace element solution SL-10 solvent/volume", "local_fields": [], "decision": "add", "stage": "Source-only solvent and denominator", "interpretation": "SL-10 lists 990 ml water plus 10 ml 25% HCl, then explicitly makes up to 1000 ml. Preserve initial water and final make-up separately.", "sources": [{"locator": "$.data.solutions[1].recipe[9]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 48-48", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled water                                      990.00      ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject": "Selenite-tungstate solution solvent/volume", "local_fields": [], "decision": "add", "stage": "Source-only solvent and denominator", "interpretation": "Selenite-tungstate lists 1000 ml water. Do not call this an explicit final make-up absent such text.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 67-67", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q38", "subject": "Wolin's vitamin solution (10x) solvent/volume", "local_fields": [], "decision": "add", "stage": "Source-only solvent and denominator", "interpretation": "Wolin vitamins lists 1000 ml water. Keep the stock solvent basis distinct from its 1 ml receiving addition.", "sources": [{"locator": "$.data.solutions[3].recipe[10]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q39", "subject": "Final pH", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ph_value", "original": 6.5}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml", "field_path": "ph_value", "original": 6.5}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "ph_value", "original": 6.5}], "decision": "evidence_only", "stage": "Generic complete medium", "interpretation": "Retain pH 6.5 in all selected layers. The earlier preparation pH values 6.0 and 6.8 are distinct stages; the DSM 103037 range is a conditional variant.", "sources": [{"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final pH: 6.5", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 21-27", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First, dissolve ferric citrate in water by heating and adjust to pH 6.0, then add other\nmedium ingredients except carbonate and vitamins. Sparge medium with 80% N2 and 20%\nCO2 gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate and\nadjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave at 121°C for 15 min. Add vitamins from\nsterile anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration.\nAdjust pH of the complete medium to 6.5, if necessary.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q40", "subject": "Main preparation and stage controls", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "preparation_steps[0].description", "original": "First, dissolve ferric citrate in water by heating and adjust to pH 6.0, then add other\r\nmedium ingredients except carbonate and vitamins. Sparge medium with 80% N2 and\r\n20% CO2 gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate\r\nand adjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave at 121°C for 15 min. Add vitamins from sterile anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the complete medium to 6.5, if necessary."}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "preparation_steps[0].action", "original": "AUTOCLAVE"}], "decision": "evidence_only", "stage": "Ferric-citrate dissolution; anoxic preparation; autoclave; filtered vitamins", "interpretation": "The DSM owner retains the complete compound procedure, including ferric-citrate heating/pH 6.0, 80% N2/20% CO2 for 30–45 min, carbonate/pH 6.8, anoxic dispensing,121°C for 15 min and filtered vitamins under 100% N2. AUTOCLAVE identifies one real operation but cannot represent all stages alone. Preserve the prose while restructuring distinct actions; target and KOMODO omit it.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"step\": \"First, dissolve ferric citrate in water by heating and adjust to pH 6.0, then add other\\r\\nmedium ingredients except carbonate and vitamins. Sparge medium with 80% N2 and\\r\\n20% CO2 gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate\\r\\nand adjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave at 121\\u00b0C for 15 min. Add vitamins from sterile anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the complete medium to 6.5, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 21-27", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First, dissolve ferric citrate in water by heating and adjust to pH 6.0, then add other\nmedium ingredients except carbonate and vitamins. Sparge medium with 80% N2 and 20%\nCO2 gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate and\nadjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave at 121°C for 15 min. Add vitamins from\nsterile anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration.\nAdjust pH of the complete medium to 6.5, if necessary.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q41", "subject": "SL-10 preparation", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "preparation_steps[1].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path": "preparation_steps[1].action", "original": "DISSOLVE"}], "decision": "evidence_only", "stage": "SL-10 stock only", "interpretation": "The retained DSM prose and DISSOLVE action are supported for the SL-10 stock. Move this scope with the nested stock rather than treating its acid dissolution/final 1000 ml as main-medium preparation. Target/KOMODO omit it.", "sources": [{"locator": "$.data.solutions[1].steps[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q42", "subject": "DSM 103037 conditional supplement and pH", "local_fields": [], "decision": "evidence_only", "stage": "Excluded strain-specific source control", "interpretation": "Retain as explicitly conditional context only: acetate 0.41 g/L, formate 0.34 g/L, glucose 1 g/L, sodium sulfide nonahydrate 0.10 g/L, carbonate 0.50 g/L and pH 5.5–6.0 apply only to DSM 103037. No selected record asserts this strain. Do not silently substitute these values for the generic recipe or claim growth from a source prescription.", "sources": [{"locator": "extracted-text physical LF lines 30-33", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "For DSM 103037: Supplement autoclaved medium with 0.41 g/l Na-acetate, 0.34 g/l Na\n-formate, 1.00 g/l D-glucose and 0.10 g/l Na2S x 9 H2O added from sterile anoxic stock\nsolutions. Reduce amount of carbonate to 0.50 g/l and adjust pH of complete medium to\n5.5 - 6.0.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch072/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:004165.

data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml: primary 30/31, secondary 29/31; data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml: primary 30/31, secondary 29/31; data/normalized_yaml/bacterial/deferrisoma_medium.yaml: primary 30/31, secondary 29/31. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:004165.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:004165.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Three stock recipes are represented as main-medium ingredients

major / open / confirmed; issue key: culturemech-004165-separate-stock-topology.

All three selected layers flatten SL-10, selenite-tungstate and tenfold Wolin stock components into main-medium G_PER_L slots, while omitting the three distinct 1 ml receiving additions and solvent/volume context. Nine main-medium rates are correctly rounded to the explicit 1003 ml final volume and should be retained. The HCl 2.5 g/L mass is additionally unsupported by the primary bare 25% stock description.

### f2: Anoxic preparation is omitted from the generated branch

major / open / confirmed; issue key: culturemech-004165-anoxic-preparation-and-metadata.

The generated target and KOMODO owner lack the main procedure and contain Aerobic: Yes, whereas the primary requires anoxic preparation and staged additions. The DSM owner retains the full main prose and SL-10 dissolution, which must be credited; its single main AUTOCLAVE action is incomplete as a representation of all stages and its SL-10 procedure belongs to that stock.

### f3: Nickel hexahydrate is mapped to an anhydrous identifier

major / open / confirmed; issue key: culturemech-004165-nickel-hydrate-correspondence.

Every layer names NiCl2 x 6H2O but uses CHEBI:34887 nickel dichloride in both primary and secondary slots. Current OLS gives anhydrous Cl2Ni, while candidate CHEBI:53542 explicitly represents the hexahydrate. Correct labels on a wrong supplied form still pass native term checks. Calcium D-pantothenate CHEBI:31345 is supported by its D-form synonym and is not a correction target.

### f4: Supported claims remain unattached and old history needs qualified context

minor / open / confirmed; issue key: culturemech-004165-claim-evidence-and-append-only-provenance.

No selected layer attaches formulation source excerpts. Current API bytes exactly authenticate both older curation reports’ cited payload and their quoted objects, but not historical access times, execution or the distinct KOMODO catalogue. Historical blanket 31-row conflicts overreach the nine currently supported main rates. KOMODO/generated import events retain malformed .fZ, while the resolver event lacks an offset.

## Recommended Actions And Acceptance Checks

### action1

Repair the maintained inputs to distinguish the three named stocks, their source amounts/solvent bases and their exact receiving additions. Preserve the nine supported main rates and explicit 1003 ml final volume; do not apply a blanket dose of 1 ml/L or an assumed 25% acid mass basis.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve the DSM preparation text, structure each verified main and stock stage at its own scope, and resolve the contradictory aerobic note. Keep generic final pH 6.5 and conditional DSM 103037 prescriptions separate. Attach preparation evidence at enclosing recipe/stock-supported scopes rather than inventing PreparationStep evidence slots.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Curate the exact nickel hexahydrate mapping in both maintained slots using the verified hydrate authority; preserve supplied 24 mg stock mass. Retain other supported hydrate/stereo mappings and avoid copying provider molarity conversions that use an incompatible molecular mass.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Attach exact claim-level excerpts and source links to the supported quantities and preparation. Preserve original events unchanged; append a new verified correction/context event with the actual curation time. Correct future writer timestamp formatting without rewriting the old timestamps or claiming reconstruction of historical execution.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Verify future KOMODO importer and DSMZ resolver events serialize actual timezone-aware UTC timestamps without literal formatting tokens; confirm every original recipe history event remains byte-preserved and any correction is append-only.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/deferrisoma_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch072/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch072/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch072/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch072/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi144421 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:144421 = iron(III) citrate; definition ['An iron chelate resulting from the combination of iron(3+) and citrate(3−).']; formula ['C6H5FeO7']; mass ['244.944']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63939 = sodium tungstate dihydrate; definition ['A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones']; formula ['2H2O.2Na.O4W']; mass ['329.846']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state), chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| dsm1451 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api1451 | https://mediadive.dsmz.de/rest/medium/1451; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| komodo1451 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1451; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| grounding | REVIEW_WORK/batch072/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T142509Z-DEFERRISOMA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/deferrisoma_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api1451 raw bytes exactly match the cited historical SHA, and 40 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api1451 raw bytes exactly match the cited historical SHA, and 40 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferrisoma_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRISOMA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch072/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer49 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer50 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer51 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer52 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer53 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer54 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer55 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer56 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer57 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| scoped-plans | REVIEW_WORK/batch072/record04/historical-scoped-plan-rows.json; two exact $.records entries | supports | Only the two exact selected-owner plan objects were assessed. Blanket historical conflicts are reassessed against current primary main rates and separately scoped stocks; unrelated plan records are excluded. |
| quantity-inventory | REVIEW_WORK/batch072/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The exact historical KOMODO MediaInfo=1451 route returned HTTP 403. Current DSM/API evidence cannot establish the current contents of that separate page.
- All six complete historical reports and the two exact selected plan objects were assessed; unrelated plan records were not scientifically reviewed. Raw digest matches authenticate API bytes and quoted objects, not old execution or retrieval timestamps.
- No experimental growth publication was assessed. The conditional DSM 103037 source note is retained only as variant context. Bare25% HCl has no verified mass/volume basis; listed stock water is not automatically measured final stock volume.
- Provider mmol_l values were not used as independent supplied-form evidence. The generic vitamin B12 ontology group does not identify a specific vitamer, and mixture/complex ingredient labels are not forced to pure compounds.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T164203Z-deferrisoma-medium-batch072
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of deferrisoma_medium
started_at: '2026-10-28T16:12:04.461342Z'
finished_at: '2026-10-28T16:42:03.059650Z'
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
summary: The nine main-medium rates and generic pH are supported, but three source
  stocks are flattened, anoxic preparation is lost from the generated branch, and
  nickel hexahydrate is mapped to anhydrous nickel chloride. Preserve supported values
  and the DSM owner’s retained preparation while repairing stock and evidence scope.
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
  - path: data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
    sha256: e9d1653da79d9f539246d643d6b94ea67b9856dccd1cfc969eef1e9eed108a27
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    sha256: 5b3bde3dcd561e995c5ffd16f0720853b680ccca074bb699461ae19141fdafbf
    role: context
  - path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    sha256: 5a94e493ec1cd529202f2b280acf09aaa6e28c36a4c91dadede9a0e63e4ba066
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/plan.json
    sha256: 56e72694e73e28cee3666277d0f215973f770da991b4b42930105ec89d0ab6e3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/deferrisoma_medium.yaml.md
    sha256: 2bc0320a2a0474e804a8c74e09d8408a25cc0c3fca10d12ffbd5b1fcde243c68
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
    sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml.md
    sha256: 91b36d52df79542b6fdc94f47394b73eca25ece91f892ed0d1d50bd34631fdcf
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRISOMA_MEDIUM.md
    sha256: b8aeeb21db9fa3f03db6b79997a151fb2534b0d11556a3d9e184d7135d19a5f1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.md
    sha256: affdc322b912f33d239fbecd059602a30f794b2a8dc4cb8bb6c4ff02394a000c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferrisoma_medium.md
    sha256: 7956b292efab53a59329c9c1bba7bf25cf2a5e4f9804e1a2edc76adca76e436c
    role: context
  - path: reports/yaml_record_review/20260922T142509Z-DEFERRISOMA_MEDIUM.md
    sha256: 02dbcfcc4eccd8971d32e983935f786d2886b24421c594e460045eb2f6785e7e
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
  selection: Authoritative batch072 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004165
targets:
- target_id: CultureMech:004165
  path: data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
  label: deferrisoma_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:004165
  command: just validate-schema data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:004165
  command: just validate-strict data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch072/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:004165
  command: just validate-terms data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:004165
  command: just validate-references data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T16:23:26.249715Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: e9d1653da79d9f539246d643d6b94ea67b9856dccd1cfc969eef1e9eed108a27
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T16:23:26.249889Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 5b3bde3dcd561e995c5ffd16f0720853b680ccca074bb699461ae19141fdafbf
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T16:23:26.249919Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 5a94e493ec1cd529202f2b280acf09aaa6e28c36a4c91dadede9a0e63e4ba066
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch072/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T16:12:05.581324Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: f613c7dd108fc3c8941d7d358894cc60fdc9b12ec8631cdf0dd8eb45e5d60ca7
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch072/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T16:12:06.551884Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 459908f91f6bc5e9c18150fb8a3a910a1b99f38140a990e27111bc81a04088e0
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch072/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T16:12:07.617343Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 2f02a52f19cc370f44961505fbb46382b5f761eb16705c281b442e8ebca7d162
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch072/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T16:12:08.377908Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 239686c8fdd6c81b0239139a3b8352fae060728cba5690a7636b7640ad0fcc84
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:05.997459Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi144421
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_144421
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:09.116564Z'
  support: supports
  summary: OLS current exact CHEBI:144421 = iron(III) citrate; definition ['An iron
    chelate resulting from the combination of iron(3+) and citrate(3−).']; formula
    ['C6H5FeO7']; mass ['244.944']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 283ce05a4ff7d7b60c46f1b8447bc5f217ea1d84543f59ad566eb9f893b768a1
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:09.026585Z'
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
  accessed_at: '2026-10-28T16:14:08.586736Z'
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
  accessed_at: '2026-10-28T16:14:08.533324Z'
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
  accessed_at: '2026-10-28T16:14:08.473092Z'
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
  accessed_at: '2026-10-28T16:14:07.992761Z'
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
  accessed_at: '2026-10-28T16:14:07.924200Z'
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
  accessed_at: '2026-10-28T16:14:05.446886Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:07.808856Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:05.424397Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:07.333543Z'
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
  accessed_at: '2026-10-28T16:14:07.323153Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:07.255650Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:07.204239Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:04.825724Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:04.787888Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:04.783361Z'
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
  accessed_at: '2026-10-28T16:14:06.613942Z'
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
  accessed_at: '2026-10-28T16:14:06.587641Z'
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
  accessed_at: '2026-10-28T16:14:09.244994Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:06.056547Z'
  support: supports
  summary: OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic
    sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia.
    A high-melting (decomposes above 280°C) white solid which is very soluble in water
    (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as
    a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:04.759935Z'
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
  accessed_at: '2026-10-28T16:14:04.200733Z'
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
  accessed_at: '2026-10-28T16:14:04.180220Z'
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
  accessed_at: '2026-10-28T16:14:04.160363Z'
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
  accessed_at: '2026-10-28T16:14:06.050637Z'
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
  accessed_at: '2026-10-28T16:14:06.045970Z'
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
  accessed_at: '2026-10-28T16:14:04.153393Z'
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
  accessed_at: '2026-10-28T16:14:06.010955Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T16:14:03.087908Z'
  support: supports
  summary: OLS current exact CHEBI:53542 = nickel chloride hexahydrate; definition
    ['A hydrate of nickel chloride containing nickel (in the +2 oxidation state),
    chloride and water moeities in the ratio 1:2:6.']; formula ['2Cl.6H2O.Ni']; mass
    ['237.689']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: dsm1451
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T16:13:12.179911Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc
- evidence_id: api1451
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1451
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T16:13:12.180213Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5
- evidence_id: komodo1451
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1451
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T16:13:12.180302Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 776fb358fb6bc7017c54f5bd7a795dcec4bf055d55c2a07fb1ceee86dcded3db
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch072/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T16:23:26.266461Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: e08b6c9adc649ecbec09ab6f3773739af8b12b76e05ec20c6176611f684c4778
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T142509Z-DEFERRISOMA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T16:23:26.267900Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 02dbcfcc4eccd8971d32e983935f786d2886b24421c594e460045eb2f6785e7e
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/deferrisoma_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T16:23:26.267941Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api1451 raw bytes exactly match the cited historical SHA, and 40 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 2bc0320a2a0474e804a8c74e09d8408a25cc0c3fca10d12ffbd5b1fcde243c68
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T16:23:26.267981Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api1451 raw bytes exactly match the cited historical SHA, and 40 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 91b36d52df79542b6fdc94f47394b73eca25ece91f892ed0d1d50bd34631fdcf
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferrisoma_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T16:23:26.268009Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 7956b292efab53a59329c9c1bba7bf25cf2a5e4f9804e1a2edc76adca76e436c
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T16:23:26.268035Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: affdc322b912f33d239fbecd059602a30f794b2a8dc4cb8bb6c4ff02394a000c
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRISOMA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T16:23:26.268058Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: b8aeeb21db9fa3f03db6b79997a151fb2534b0d11556a3d9e184d7135d19a5f1
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch072/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T16:23:26.268089Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: e81bf342aa084cc7b022a5b45a6bd1833de1e5dde8dbb6d32bab9dce96425111
- evidence_id: writer49
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T16:23:26.268172Z'
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
  accessed_at: '2026-10-28T16:23:26.268199Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer51
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T16:23:26.268242Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer52
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T16:23:26.268278Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer53
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T16:23:26.268309Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer54
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T16:23:26.268343Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer55
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T16:23:26.268374Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer56
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T16:23:26.268397Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer57
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T16:23:26.268420Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: scoped-plans
  kind: prior_review
  reference: REVIEW_WORK/batch072/record04/historical-scoped-plan-rows.json
  locator: two exact $.records entries
  accessed_at: '2026-10-28T16:23:26.305721Z'
  support: supports
  summary: Only the two exact selected-owner plan objects were assessed. Blanket historical
    conflicts are reassessed against current primary main rates and separately scoped
    stocks; unrelated plan records are excluded.
  snapshot_sha256: 5c35e88f0ba022a9ff9bc8376a08219782e142a38647b09101f43d1ce5723d99
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch072/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T16:23:26.306419Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 01a09e5b5104c4f8c52afc65e960f6df4b2eddb8e63ac917edef9c10fb9a1b87
assessments:
- assessment_id: a1
  area: identity
  topic: Generic DSM1451 and maintained source branches
  outcome: supported
  summary: The primary title/accession and both maintained source identities align
    with generic DSM1451. The primary-specific DSM 103037 note is not an unconditional
    recipe or growth assertion. Reciprocal SOURCE_DUPLICATE relations are present,
    but their current scientific fields differ in retained preparation and metadata,
    so they are not permission to merge unequal documents.
  target_ids:
  - CultureMech:004165
  evidence_ids:
  - local0
  - local1
  - local2
  - dsm1451
  - api1451
  - scoped-plans
- assessment_id: a2
  area: consistency
  topic: Retained classification and conservative current merging
  outcome: concern
  summary: LIQUID, COMPLEX and SEMI_DEFINED are consistent with this generic yeast-containing
    medium. Main pH and rounded main concentrations are supported. The stale flattened
    stock structure and lost preparation remain scientific defects; current conservative
    merge equality rejects incompatible content and does not recreate this historical
    output.
  target_ids:
  - CultureMech:004165
  evidence_ids:
  - local0
  - local1
  - local2
  - api1451
  - dsm1451
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: The September narrative and both October plans/reports are derivative assessments,
    not permission to adopt every proposed value. All current raw-matched API excerpts
    are credited; nine main rates now independently pass, whereas stock topology still
    fails. The exact fresh KOMODO route is 403, leaving a bounded current-source access
    limit. Only the two selected plan rows transfer; prior zero-source-check reports
    do not authenticate chemistry. Current conservative merging preserves scientific
    fields and rejects incompatible formulations. Inspected writer behavior is described
    separately by exact file and function; it does not prove historical execution.
  target_ids:
  - CultureMech:004165
  evidence_ids:
  - history-auth
  - writer49
  - writer50
  - writer51
  - writer52
  - writer53
  - writer54
  - writer55
  - writer56
  - writer57
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 93 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:004165
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:004165",
    "selected_concentration_field_count": 93, "selected_concentration_fields_covered":
    93, "decisions": [{"decision_id": "q1", "subject": "KH2PO4", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "0.329013", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003
    L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\":
    2.4177,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "KH2PO4                                                 0.33       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q2", "subject": "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003
    L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\":
    2.48988,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "(NH4)2SO4                                              0.33       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q3", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003
    L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\":
    4.41332,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 9-9", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "KCl                                                    0.33       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "17.9462",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "17.9462",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "17.9462",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 17.9462 G_PER_L. Source 18 g / 1.003
    L = 17.94616151545363908275174477 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 17.9462,\n                        \"mmol_l\":
    307.087,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-10", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "NaCl                                                  18.00       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q5", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.329013",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 0.329013 G_PER_L. Source 0.33 g / 1.003
    L = 0.3290129611166500498504486540 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.329013,\n                        \"mmol_l\":
    2.23796,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 11-11", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "CaCl2 x 2
    H2O                                          0.33       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q6", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "3.98804",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "3.98804",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "3.98804",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 3.98804 G_PER_L. Source 4 g / 1.003
    L = 3.988035892323030907278165503 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.98804,\n                        \"mmol_l\":
    19.6162,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 12-12", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "MgCl2 x 6
    H2O                                          4.00       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q7", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 0.199402 G_PER_L. Source 0.2 g / 1.003
    L = 0.1994017946161515453639082752 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199402,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 13-13", "source_key": "dsm1451", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256":
    "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256":
    "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at":
    "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Yeast extract                                          0.20       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q8", "subject": "Ferric citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "2.49252",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "2.49252",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "2.49252",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 2.49252 G_PER_L. Source 2.5 g / 1.003
    L = 2.492522432701894317048853440 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Ferric citrate\",\n                        \"compound_id\":
    863,\n                        \"attribute\": \"Aldrich F6129\",\n                        \"amount\":
    2.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.49252,\n                        \"mmol_l\": 10.1759,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 16-16", "source_key": "dsm1451", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256":
    "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256":
    "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at":
    "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Ferric citrate (Aldrich
    F6129)                         2.50       g", "quote_representation": "captured
    extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q9", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.997009",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.997009",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.997009",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main medium; explicit
    final 1003 ml", "interpretation": "Retain 0.997009 G_PER_L. Source 1 g / 1.003
    L = 0.9970089730807577268195413759 g/L, rounded to the existing precision. Both
    current PDF and API support this main-medium value; no attached source excerpt
    currently authenticates it in these YAML layers. Supplied reagent form is assessed
    separately.", "sources": [{"locator": "$.data.solutions[0].recipe[10]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    9.40681,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 17-17", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2CO3                                                 1.00       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 4-4", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q10", "subject": "HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "SL-10 stock flattened into
    main ingredients", "interpretation": "The local 2.5 G_PER_L is not established
    as a main-medium value or an independently verified acid mass. The primary stock
    calls for 10 ml of 25% HCl; percent basis and density are not specified. Preserve
    that stock addition and the explicit SL-10 make-up volume, without assuming 25%
    w/v or converting it into 2.5 g.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 39-39", "source_key": "dsm1451", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf", "source_raw_sha256":
    "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc", "source_text_sha256":
    "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5", "accessed_at":
    "2026-10-28T16:13:12.179911Z", "exact_source_quote": "HCl (25%)                                             10.00      ml",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main
    ingredients", "interpretation": "The numeric rate 1.5 G_PER_L matches the provider-normalized
    SL-10 stock composition, not the main medium. Primary supplied amount is 1.5 g.
    Preserve this amount/form inside its separately identified stock, and represent
    that stock''s 1 ml receiving addition separately. SL-10 has an explicit 1000 ml
    final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 40-40", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "FeCl2 x 4
    H2O                                          1.50       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q12", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main
    ingredients", "interpretation": "The numeric rate 0.07 G_PER_L matches the provider-normalized
    SL-10 stock composition, not the main medium. Primary supplied amount is 70 mg.
    Preserve this amount/form inside its separately identified stock, and represent
    that stock''s 1 ml receiving addition separately. SL-10 has an explicit 1000 ml
    final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 41-41", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "ZnCl2                                                 70.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main
    ingredients", "interpretation": "The numeric rate 0.1 G_PER_L matches the provider-normalized
    SL-10 stock composition, not the main medium. Primary supplied amount is 100 mg.
    Preserve this amount/form inside its separately identified stock, and represent
    that stock''s 1 ml receiving addition separately. SL-10 has an explicit 1000 ml
    final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 42-42", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "MnCl2 x 4
    H2O                                        100.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q14", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.006 G_PER_L matches
    the provider-normalized SL-10 stock composition, not the main medium. Primary
    supplied amount is 6 mg. Preserve this amount/form inside its separately identified
    stock, and represent that stock''s 1 ml receiving addition separately. SL-10 has
    an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 43-43", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "H3BO3                                                  6.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 58-59", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q15", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened into main
    ingredients", "interpretation": "The numeric rate 0.19 G_PER_L matches the provider-normalized
    SL-10 stock composition, not the main medium. Primary supplied amount is 190 mg.
    Preserve this amount/form inside its separately identified stock, and represent
    that stock''s 1 ml receiving addition separately. SL-10 has an explicit 1000 ml
    final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 44-44", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "CoCl2 x 6
    H2O                                        190.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q16", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.002 G_PER_L matches
    the provider-normalized SL-10 stock composition, not the main medium. Primary
    supplied amount is 2 mg. Preserve this amount/form inside its separately identified
    stock, and represent that stock''s 1 ml receiving addition separately. SL-10 has
    an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 45-45", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "CuCl2 x 2
    H2O                                          2.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q17", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.024 G_PER_L matches
    the provider-normalized SL-10 stock composition, not the main medium. Primary
    supplied amount is 24 mg. Preserve this amount/form inside its separately identified
    stock, and represent that stock''s 1 ml receiving addition separately. SL-10 has
    an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[7]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 46-46", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "NiCl2 x 6
    H2O                                         24.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q18", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "SL-10 stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.036 G_PER_L matches
    the provider-normalized SL-10 stock composition, not the main medium. Primary
    supplied amount is 36 mg. Preserve this amount/form inside its separately identified
    stock, and represent that stock''s 1 ml receiving addition separately. SL-10 has
    an explicit 1000 ml final make-up.", "sources": [{"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 47-47", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2MoO4 x
    2 H2O                                       36.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q19", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "selenite-tungstate stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.5 G_PER_L matches
    the provider-normalized selenite-tungstate stock composition, not the main medium.
    Primary supplied amount is 0.5 g. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[2].recipe[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 64-64", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "NaOH                                                       0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q20", "subject":
    "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "selenite-tungstate stock
    flattened into main ingredients", "interpretation": "The numeric rate 0.003 G_PER_L
    matches the provider-normalized selenite-tungstate stock composition, not the
    main medium. Primary supplied amount is 3 mg. Preserve this amount/form inside
    its separately identified stock, and represent that stock''s 1 ml receiving addition
    separately. The primary lists 1000 ml water; API volume 1000 ml supports provider
    normalization but is not an independently measured final stock volume.", "sources":
    [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1451", "reference":
    "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 65-65", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2SeO3 x
    5 H2O                                            3.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q21", "subject": "Na2WO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "selenite-tungstate stock
    flattened into main ingredients", "interpretation": "The numeric rate 0.004 G_PER_L
    matches the provider-normalized selenite-tungstate stock composition, not the
    main medium. Primary supplied amount is 4 mg. Preserve this amount/form inside
    its separately identified stock, and represent that stock''s 1 ml receiving addition
    separately. The primary lists 1000 ml water; API volume 1000 ml supports provider
    normalization but is not an independently measured final stock volume.", "sources":
    [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api1451", "reference":
    "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 66-66", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Na2WO4 x
    2 H2O                                             4.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q22", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.02 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 20 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[0]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 72-72", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Biotin                                                    20.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject":
    "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.02 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 20 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[1]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 73-73", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Folic acid                                                20.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q24", "subject":
    "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.1 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 100 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[2]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 74-74", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Pyridoxine
    hydrochloride                                 100.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q25", "subject": "Thiamine HCl",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 50 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[3]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 75-75", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Thiamine
    HCl                                              50.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q26", "subject": "Riboflavin",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 50 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[4]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 76-76", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Riboflavin                                                50.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q27", "subject":
    "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 50 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[5]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 77-77", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Nicotinic
    acid                                            50.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q28", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 50 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[6]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 78-78", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Calcium D-(+)-pantothenate                                50.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q29", "subject":
    "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock
    flattened into main ingredients", "interpretation": "The numeric rate 0.001 G_PER_L
    matches the provider-normalized Wolin vitamins (10x) stock composition, not the
    main medium. Primary supplied amount is 1 mg. Preserve this amount/form inside
    its separately identified stock, and represent that stock''s 1 ml receiving addition
    separately. The primary lists 1000 ml water; API volume 1000 ml supports provider
    normalization but is not an independently measured final stock volume.", "sources":
    [{"locator": "$.data.solutions[3].recipe[7]", "source_key": "api1451", "reference":
    "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical
    LF lines 79-79", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Vitamin B12                                                1.00       mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject":
    "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 50 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[8]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 80-80", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "p-Aminobenzoic
    acid                                       50.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q31", "subject": "(DL)-alpha-Lipoic
    acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Wolin vitamins (10x) stock flattened
    into main ingredients", "interpretation": "The numeric rate 0.05 G_PER_L matches
    the provider-normalized Wolin vitamins (10x) stock composition, not the main medium.
    Primary supplied amount is 50 mg. Preserve this amount/form inside its separately
    identified stock, and represent that stock''s 1 ml receiving addition separately.
    The primary lists 1000 ml water; API volume 1000 ml supports provider normalization
    but is not an independently measured final stock volume.", "sources": [{"locator":
    "$.data.solutions[3].recipe[9]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 81-81", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "(DL)-alpha-Lipoic
    acid                                    50.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q32", "subject": "Trace element
    solution SL-10 receiving addition", "local_fields": [], "decision": "add", "stage":
    "Main-medium stock receiving dose", "interpretation": "The selected records omit
    the distinct stock addition. Preserve 1 ml per explicit 1003 ml final medium.
    If a per-litre dose is required, 1/1.003 = 0.997008973... ml/L; a historical recommendation
    of exactly 1 ML_PER_L changes the printed denominator. Do not copy stock component
    strengths into the receiving medium.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 14-14", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Trace element
    solution SL-10                           1.00      ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q33", "subject": "Selenite-tungstate solution receiving addition", "local_fields":
    [], "decision": "add", "stage": "Main-medium stock receiving dose", "interpretation":
    "The selected records omit the distinct stock addition. Preserve 1 ml per explicit
    1003 ml final medium. If a per-litre dose is required, 1/1.003 = 0.997008973...
    ml/L; a historical recommendation of exactly 1 ML_PER_L changes the printed denominator.
    Do not copy stock component strengths into the receiving medium.", "sources":
    [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api1451", "reference":
    "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 15-15", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Selenite-tungstate
    solution                            1.00      ml", "quote_representation": "captured
    extracted text"}, {"locator": "extracted-text physical LF lines 4-4", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q34", "subject": "Wolin''s vitamin solution (10x) receiving addition", "local_fields":
    [], "decision": "add", "stage": "Main-medium stock receiving dose", "interpretation":
    "The selected records omit the distinct stock addition. Preserve 1 ml per explicit
    1003 ml final medium. If a per-litre dose is required, 1/1.003 = 0.997008973...
    ml/L; a historical recommendation of exactly 1 ML_PER_L changes the printed denominator.
    Do not copy stock component strengths into the receiving medium.", "sources":
    [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api1451", "reference":
    "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 18-18", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Wolin''s
    vitamin solution (10x)                         1.00      ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q35", "subject": "Main sol. 1451 solvent/volume", "local_fields": [], "decision":
    "add", "stage": "Source-only solvent and denominator", "interpretation": "Main
    water is 1000 ml and the primary separately declares final medium 1003 ml; preserve
    both roles.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 19-19", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled
    water                                     1000.00      ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 4-4",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final volume:
    1003 ml", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q36", "subject": "Trace element solution SL-10 solvent/volume", "local_fields":
    [], "decision": "add", "stage": "Source-only solvent and denominator", "interpretation":
    "SL-10 lists 990 ml water plus 10 ml 25% HCl, then explicitly makes up to 1000
    ml. Preserve initial water and final make-up separately.", "sources": [{"locator":
    "$.data.solutions[1].recipe[9]", "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 48-48", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled
    water                                      990.00      ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 58-59",
    "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q37", "subject": "Selenite-tungstate solution solvent/volume", "local_fields":
    [], "decision": "add", "stage": "Source-only solvent and denominator", "interpretation":
    "Selenite-tungstate lists 1000 ml water. Do not call this an explicit final make-up
    absent such text.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 67-67", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q38", "subject": "Wolin''s vitamin
    solution (10x) solvent/volume", "local_fields": [], "decision": "add", "stage":
    "Source-only solvent and denominator", "interpretation": "Wolin vitamins lists
    1000 ml water. Keep the stock solvent basis distinct from its 1 ml receiving addition.",
    "sources": [{"locator": "$.data.solutions[3].recipe[10]", "source_key": "api1451",
    "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q39", "subject": "Final pH", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml", "field_path":
    "ph_value", "original": 6.5}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml",
    "field_path": "ph_value", "original": 6.5}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "ph_value", "original": 6.5}], "decision": "evidence_only", "stage":
    "Generic complete medium", "interpretation": "Retain pH 6.5 in all selected layers.
    The earlier preparation pH values 6.0 and 6.8 are distinct stages; the DSM 103037
    range is a conditional variant.", "sources": [{"locator": "extracted-text physical
    LF lines 3-3", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "Final pH:
    6.5", "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 21-27", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First, dissolve
    ferric citrate in water by heating and adjust to pH 6.0, then add other\nmedium
    ingredients except carbonate and vitamins. Sparge medium with 80% N2 and 20%\nCO2
    gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate
    and\nadjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic\nHungate-type
    tubes or serum vials and autoclave at 121°C for 15 min. Add vitamins from\nsterile
    anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration.\nAdjust
    pH of the complete medium to 6.5, if necessary.", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q40", "subject": "Main preparation and stage
    controls", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "First, dissolve
    ferric citrate in water by heating and adjust to pH 6.0, then add other\r\nmedium
    ingredients except carbonate and vitamins. Sparge medium with 80% N2 and\r\n20%
    CO2 gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate\r\nand
    adjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave at 121°C for 15 min. Add vitamins from sterile
    anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration.
    Adjust pH of the complete medium to 6.5, if necessary."}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "preparation_steps[0].action", "original": "AUTOCLAVE"}], "decision":
    "evidence_only", "stage": "Ferric-citrate dissolution; anoxic preparation; autoclave;
    filtered vitamins", "interpretation": "The DSM owner retains the complete compound
    procedure, including ferric-citrate heating/pH 6.0, 80% N2/20% CO2 for 30–45 min,
    carbonate/pH 6.8, anoxic dispensing,121°C for 15 min and filtered vitamins under
    100% N2. AUTOCLAVE identifies one real operation but cannot represent all stages
    alone. Preserve the prose while restructuring distinct actions; target and KOMODO
    omit it.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451", "source_raw_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "source_text_sha256":
    "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5", "accessed_at":
    "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"step\":
    \"First, dissolve ferric citrate in water by heating and adjust to pH 6.0, then
    add other\\r\\nmedium ingredients except carbonate and vitamins. Sparge medium
    with 80% N2 and\\r\\n20% CO2 gas mixture for 30 - 45 min to make it anoxic, then
    add and dissolve carbonate\\r\\nand adjust pH to 6.8. Dispense medium under the
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave
    at 121\\u00b0C for 15 min. Add vitamins from sterile anoxic stock solutions prepared
    under 100% N2 gas and sterilized by filtration. Adjust pH of the complete medium
    to 6.5, if necessary.\"\n                    }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text physical LF lines 21-27", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First, dissolve
    ferric citrate in water by heating and adjust to pH 6.0, then add other\nmedium
    ingredients except carbonate and vitamins. Sparge medium with 80% N2 and 20%\nCO2
    gas mixture for 30 - 45 min to make it anoxic, then add and dissolve carbonate
    and\nadjust pH to 6.8. Dispense medium under the same gas atmosphere into anoxic\nHungate-type
    tubes or serum vials and autoclave at 121°C for 15 min. Add vitamins from\nsterile
    anoxic stock solutions prepared under 100% N2 gas and sterilized by filtration.\nAdjust
    pH of the complete medium to 6.5, if necessary.", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q41", "subject": "SL-10 preparation", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml", "field_path":
    "preparation_steps[1].description", "original": "First dissolve FeCl2 in the HCl,
    then dilute in water, add and dissolve the other salts. Finally make up to 1000.00
    ml."}, {"record_path": "data/normalized_yaml/bacterial/deferrisoma_medium.yaml",
    "field_path": "preparation_steps[1].action", "original": "DISSOLVE"}], "decision":
    "evidence_only", "stage": "SL-10 stock only", "interpretation": "The retained
    DSM prose and DISSOLVE action are supported for the SL-10 stock. Move this scope
    with the nested stock rather than treating its acid dissolution/final 1000 ml
    as main-medium preparation. Target/KOMODO omit it.", "sources": [{"locator": "$.data.solutions[1].steps[0]",
    "source_key": "api1451", "reference": "https://mediadive.dsmz.de/rest/medium/1451",
    "source_raw_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "source_text_sha256": "1785233d92cc06b223c44db89db64d03ccc4274e793b946691034d78bfd091f5",
    "accessed_at": "2026-10-28T16:13:12.180213Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 58-59", "source_key":
    "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q42", "subject": "DSM 103037 conditional supplement and pH", "local_fields":
    [], "decision": "evidence_only", "stage": "Excluded strain-specific source control",
    "interpretation": "Retain as explicitly conditional context only: acetate 0.41
    g/L, formate 0.34 g/L, glucose 1 g/L, sodium sulfide nonahydrate 0.10 g/L, carbonate
    0.50 g/L and pH 5.5–6.0 apply only to DSM 103037. No selected record asserts this
    strain. Do not silently substitute these values for the generic recipe or claim
    growth from a source prescription.", "sources": [{"locator": "extracted-text physical
    LF lines 30-33", "source_key": "dsm1451", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1451.pdf",
    "source_raw_sha256": "19852002e8758ecb10970869d7e1e45b41c6b367af63ed6b2206d32600bbe4cc",
    "source_text_sha256": "db590c23b22212d4bbd7881ebfcda9de214bb3ca00a6f9767b4fa6f6b4726ee5",
    "accessed_at": "2026-10-28T16:13:12.179911Z", "exact_source_quote": "For DSM 103037:
    Supplement autoclaved medium with 0.41 g/l Na-acetate, 0.34 g/l Na\n-formate,
    1.00 g/l D-glucose and 0.10 g/l Na2S x 9 H2O added from sterile anoxic stock\nsolutions.
    Reduce amount of carbonate to 0.50 g/l and adjust pH of complete medium to\n5.5
    - 6.0.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch072/record04/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml: primary 30/31, secondary
    29/31; data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml: primary
    30/31, secondary 29/31; data/normalized_yaml/bacterial/deferrisoma_medium.yaml:
    primary 30/31, secondary 29/31. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:004165
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
  - CultureMech:004165
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
  - CultureMech:004165
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-004165-separate-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Three stock recipes are represented as main-medium ingredients
  description: All three selected layers flatten SL-10, selenite-tungstate and tenfold
    Wolin stock components into main-medium G_PER_L slots, while omitting the three
    distinct 1 ml receiving additions and solvent/volume context. Nine main-medium
    rates are correctly rounded to the explicit 1003 ml final volume and should be
    retained. The HCl 2.5 g/L mass is additionally unsupported by the primary bare
    25% stock description.
  target_ids:
  - CultureMech:004165
  field_paths:
  - ingredients
  - solutions
  - evidence
  evidence_ids:
  - dsm1451
  - api1451
  rule_id: review-yaml-record/stock-stage-and-denominator
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-004165-anoxic-preparation-and-metadata
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Anoxic preparation is omitted from the generated branch
  description: 'The generated target and KOMODO owner lack the main procedure and
    contain Aerobic: Yes, whereas the primary requires anoxic preparation and staged
    additions. The DSM owner retains the full main prose and SL-10 dissolution, which
    must be credited; its single main AUTOCLAVE action is incomplete as a representation
    of all stages and its SL-10 procedure belongs to that stock.'
  target_ids:
  - CultureMech:004165
  field_paths:
  - preparation_steps
  - evidence
  - notes
  - data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml::notes
  - data/normalized_yaml/bacterial/deferrisoma_medium.yaml::preparation_steps
  evidence_ids:
  - dsm1451
  - api1451
  - local0
  - local1
  - local2
  rule_id: review-yaml-record/source-preparation-scope
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-004165-nickel-hydrate-correspondence
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is mapped to an anhydrous identifier
  description: Every layer names NiCl2 x 6H2O but uses CHEBI:34887 nickel dichloride
    in both primary and secondary slots. Current OLS gives anhydrous Cl2Ni, while
    candidate CHEBI:53542 explicitly represents the hexahydrate. Correct labels on
    a wrong supplied form still pass native term checks. Calcium D-pantothenate CHEBI:31345
    is supported by its D-form synonym and is not a correction target.
  target_ids:
  - CultureMech:004165
  field_paths:
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm1451
  - chebi34887
  - chebi53542
  - chebi31345
  - grounding
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-004165-claim-evidence-and-append-only-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Supported claims remain unattached and old history needs qualified context
  description: No selected layer attaches formulation source excerpts. Current API
    bytes exactly authenticate both older curation reports’ cited payload and their
    quoted objects, but not historical access times, execution or the distinct KOMODO
    catalogue. Historical blanket 31-row conflicts overreach the nine currently supported
    main rates. KOMODO/generated import events retain malformed .fZ, while the resolver
    event lacks an offset.
  target_ids:
  - CultureMech:004165
  field_paths:
  - evidence
  - references
  - curation_history
  evidence_ids:
  - dsm1451
  - api1451
  - history-auth
  - scoped-plans
  rule_id: review-yaml-record/claim-traceability-and-history
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Repair the maintained inputs to distinguish the three named stocks,
    their source amounts/solvent bases and their exact receiving additions. Preserve
    the nine supported main rates and explicit 1003 ml final volume; do not apply
    a blanket dose of 1 ml/L or an assumed 25% acid mass basis.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004165
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
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
  description: Preserve the DSM preparation text, structure each verified main and
    stock stage at its own scope, and resolve the contradictory aerobic note. Keep
    generic final pH 6.5 and conditional DSM 103037 prescriptions separate. Attach
    preparation evidence at enclosing recipe/stock-supported scopes rather than inventing
    PreparationStep evidence slots.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004165
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
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
  description: Curate the exact nickel hexahydrate mapping in both maintained slots
    using the verified hydrate authority; preserve supplied 24 mg stock mass. Retain
    other supported hydrate/stereo mappings and avoid copying provider molarity conversions
    that use an incompatible molecular mass.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004165
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
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
  description: Attach exact claim-level excerpts and source links to the supported
    quantities and preparation. Preserve original events unchanged; append a new verified
    correction/context event with the actual curation time. Correct future writer
    timestamp formatting without rewriting the old timestamps or claiming reconstruction
    of historical execution.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004165
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferrisoma_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: Future UTC timestamp formatting only; preserve original imported events
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: Future timezone-aware timestamp serialization only; preserve original resolver
      events
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
  - Verify future KOMODO importer and DSMZ resolver events serialize actual timezone-aware
    UTC timestamps without literal formatting tokens; confirm every original recipe
    history event remains byte-preserved and any correction is append-only.
limitations:
- The exact historical KOMODO MediaInfo=1451 route returned HTTP 403. Current DSM/API
  evidence cannot establish the current contents of that separate page.
- All six complete historical reports and the two exact selected plan objects were
  assessed; unrelated plan records were not scientifically reviewed. Raw digest matches
  authenticate API bytes and quoted objects, not old execution or retrieval timestamps.
- No experimental growth publication was assessed. The conditional DSM 103037 source
  note is retained only as variant context. Bare25% HCl has no verified mass/volume
  basis; listed stock water is not automatically measured final stock volume.
- Provider mmol_l values were not used as independent supplied-form evidence. The
  generic vitamin B12 ontology group does not identify a specific vitamer, and mixture/complex
  ingredient labels are not forced to pure compounds.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
